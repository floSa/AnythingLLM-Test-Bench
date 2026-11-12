#!/usr/bin/env python3
"""Essai réel : peut-on brancher un reranker externe (le modèle `rerank` du service central) dans AnythingLLM 1.19.0 ?
1. réglages de l'instance (POST /api/v1/system/update-env) avec des clés de reranker plausibles ;
2. réglage de l'espace (POST /api/v1/workspace/<slug>/update) avec des valeurs de recherche autres que default/rerank ;
3. relecture des réglages après coup. La clé du service n'est jamais envoyée ni affichée (valeur factice).
Sortie : outils/resultats/anythingllm/essai-reranker-externe-<date>.txt"""
import datetime, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from client import API

api, lignes = API(), []
avant = api.get("/system")["settings"]
cles = {"RerankerEngine": "generic-openai", "RerankingProvider": "generic-openai", "RerankerBasePath": "http://llm-central:8080/v1",
        "RerankerModelPref": "rerank", "RERANKER_PROVIDER": "generic-openai"}
for k, v in cles.items():
    try:
        r = api.post("/system/update-env", {k: v})
        lignes.append(f"update-env {k}={v} -> {json.dumps(r, ensure_ascii=False)[:200]}")
    except Exception as e:
        lignes.append(f"update-env {k}={v} -> erreur {str(e)[:200]}")
apres = api.get("/system")["settings"]
lignes.append("clés de réglage contenant « rerank » avant : " + str(sorted(k for k in avant if "rerank" in k.lower())))
lignes.append("clés de réglage contenant « rerank » après : " + str(sorted(k for k in apres if "rerank" in k.lower())))
slug = api.post("/workspace/new", {"name": "Essai-reranker"})["workspace"]["slug"]
for mode in ("generic-openai", "cohere", "rerank@llm-central", "rerank"):
    try:
        api.post(f"/workspace/{slug}/update", {"vectorSearchMode": mode})
        lu = api.get(f"/workspace/{slug}")["workspace"][0]["vectorSearchMode"]
        lignes.append(f"vectorSearchMode demandé={mode!r} -> enregistré={lu!r}")
    except Exception as e:
        lignes.append(f"vectorSearchMode demandé={mode!r} -> erreur {str(e)[:150]}")
api.delete(f"/workspace/{slug}")
out = Path(__file__).resolve().parents[2] / f"outils/resultats/anythingllm/essai-reranker-externe-{datetime.date.today()}.txt"
out.write_text("\n".join(lignes) + "\n")
print("\n".join(lignes))
