#!/usr/bin/env python3
"""Dépassement volontaire du contexte (kit/PROMPT.md phase B, point 3) : question de ~80 000 caractères
(≈ 20 000 jetons, plus que les 16 384 du modèle chat) envoyée à l'espace « Premier essai » en mode chat.
Sortie : outils/resultats/anythingllm/contexte-2026-11-12.txt"""
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from client import API, sans_pensee

api = API()
phrase = "Le service qualité de Vélanor vérifie chaque vélo avant expédition. "
longue = phrase * 1200 + "\nQuestion : combien de fois la phrase précédente est-elle répétée ?"
lignes = [f"longueur du message : {len(longue)} caractères"]
t0 = time.time()
try:
    r = api.post("/workspace/premier-essai/chat", {"message": longue, "mode": "chat", "sessionId": "essai-contexte"}, timeout=900)
    lignes.append(f"durée : {time.time() - t0:.1f} s")
    lignes.append("type : " + str(r.get("type")) + " ; erreur : " + str(r.get("error")))
    lignes.append("réponse (sans réflexion, début) : " + sans_pensee(r.get("textResponse") or "")[:400])
except Exception as e:
    lignes.append(f"durée : {time.time() - t0:.1f} s ; exception : {str(e)[:600]}")
out = Path(__file__).resolve().parents[2] / "outils/resultats/anythingllm/contexte-2026-11-12.txt"
out.write_text("\n".join(lignes) + "\n")
print("\n".join(lignes))
