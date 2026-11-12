#!/usr/bin/env python3
"""Adaptateur du banc commun pour AnythingLLM (API développeur /api/v1).

Indexation : espace « Banc-<nom> » créé par l'API, chaque fichier du corpus téléversé avec addToWorkspaces (lecture,
découpage et calcul des vecteurs par l'embedder réglé dans l'instance). Questions : mode « query » (réponse tirée des
seuls documents, kit/fiches/04-anythingllm.md « Adaptateur du banc »), une session neuve par question (pas d'historique).
Le raisonnement <think>…</think> du modèle chat est retiré avant notation (il reste dans le JSON, champ reponse_brute).

Usage :
  outils/anythingllm/banc.py --etiquette defaut-sans-rerank [--espace Banc-bge-m3] [--reindexer]
       [--rerank] [--top-n 4] [--seuil 0.25] [--historique 20] [--limite N] [--ids q01,q02] [--sans-juge]
Le même espace sert à plusieurs réglages (même corpus) : seuls les réglages passés changent.
"""
import argparse, json, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "communs/banc"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import commun  # noqa: E402
from client import API, BASE, sans_pensee  # noqa: E402

APP = ["rag-anythingllm"]
MODELES = ["llm-central", "llm-swap", "llm-speaches"]


class Adaptateur:
    nom = "AnythingLLM"

    def __init__(self, a):
        self.a, self.api = a, API()
        self.slug = None
        reglages = {"chatMode": "query", "topN": a.top_n, "similarityThreshold": a.seuil, "openAiHistory": a.historique,
                    "vectorSearchMode": "rerank" if a.rerank else "default"}
        self.reglages = reglages

    def _espace(self):
        if not self.slug:
            self.slug = self.api.espace(self.a.espace, **self.reglages)
        return self.slug

    def indexer(self, fichiers):
        slug = self._espace()
        docs = self.api.get(f"/workspace/{slug}")["workspace"]
        docs = docs[0]["documents"] if isinstance(docs, list) else docs.get("documents", [])
        if docs and not self.a.reindexer:
            return {"espace": slug, "documents": len(docs), "reprise": "espace déjà indexé, réutilisé"}
        detail = []
        for f in fichiers:
            t0 = time.time()
            r = self.api.televerser(f, slug)
            detail.append({"fichier": f.name, "succes": r.get("success"), "duree_s": round(time.time() - t0, 1),
                           "mots": sum(d.get("wordCount", 0) or 0 for d in r.get("documents", [])),
                           "erreur": r.get("error")})
            print(f"  {f.name}: {detail[-1]}", flush=True)
        return {"espace": slug, "fichiers": detail}

    def demander(self, question):
        r = self.api.demander(self._espace(), question, mode="query")
        cits = [{"document": s.get("title") or "", "page": None, "extrait": (s.get("text") or "")[:300],
                 "score": s.get("score"), "rerank_score": s.get("rerank_score")} for s in r.get("sources") or []]
        brute = r.get("textResponse") or ""
        if r.get("error"):
            raise RuntimeError(r["error"])
        return {"reponse": sans_pensee(brute), "citations": cits, "reponse_brute": brute}

    def config(self):
        sysinfo = {}
        try:
            s = self.api.get("/system")["settings"]
            sysinfo = {k: s.get(k) for k in ("LLMProvider", "GenericOpenAiModelPref", "GenericOpenAiTokenLimit",
                                              "GenericOpenAiMaxTokens", "EmbeddingEngine", "EmbeddingModelPref",
                                              "EmbeddingModelMaxChunkLength", "VectorDB", "TextSplitterChunkSize",
                                              "TextSplitterChunkOverlap", "WhisperProvider")}
        except Exception as e:  # la route système peut évoluer : le banc continue
            sysinfo = {"erreur": str(e)[:200]}
        return {"url": BASE, "espace": self.a.espace, "mode": "query", **self.reglages, "instance": sysinfo}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--etiquette", required=True)
    p.add_argument("--espace", default="Banc-bge-m3")
    p.add_argument("--reindexer", action="store_true")
    p.add_argument("--rerank", action="store_true", help="reranker natif (« Accuracy Optimized », vectorSearchMode=rerank)")
    p.add_argument("--top-n", type=int, default=4)
    p.add_argument("--seuil", type=float, default=0.25)
    p.add_argument("--historique", type=int, default=20)
    p.add_argument("--limite", type=int)
    p.add_argument("--ids")
    p.add_argument("--sans-juge", action="store_true")
    a = p.parse_args()
    ad = Adaptateur(a)
    res = commun.lancer(ad, a.etiquette, APP, MODELES, indexer=True, juge=not a.sans_juge, limite=a.limite,
                        ids=a.ids.split(",") if a.ids else None)
    # réponse brute (raisonnement compris) gardée à côté de la réponse notée
    commun.ecrire(res, commun.RACINE / "outils/resultats/anythingllm")


if __name__ == "__main__":
    main()
