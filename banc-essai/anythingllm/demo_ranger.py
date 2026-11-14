#!/usr/bin/env python3
"""Range le jeu de démonstration (kit/PROMPT.md phase H) : dans « Démo Vélanor », garde un seul fil par question
d'exemple (le plus récent, renommé), supprime les autres fils d'essai ; supprime l'espace du banc. Sortie : liste finale."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from client import API

DEMO = {"Quelle est la durée de garantie du cadre et de la batterie": "FAQ — garantie",
        "Quel délai de livraison prévoit le contrat Batterix": "Fournisseur Batterix",
        "Quand la ligne d'assemblage numéro 3": "Point production"}
api = API()
w = api.get("/workspace/demo-velanor")["workspace"][0]
gardes = {}
for t in w.get("threads", []):  # ordre de création
    chats = api.get(f"/workspace/demo-velanor/thread/{t['slug']}/chats").get("history", [])
    premiere = next((c["content"] for c in chats if c.get("role") == "user"), "")
    nom = next((n for q, n in DEMO.items() if premiere.replace("’", "'").startswith(q)), None)
    if nom and any(c.get("role") == "assistant" and c.get("sources") for c in chats):
        if nom in gardes:
            api.delete(f"/workspace/demo-velanor/thread/{gardes[nom]}")
        gardes[nom] = t["slug"]
    else:
        api.delete(f"/workspace/demo-velanor/thread/{t['slug']}")
for nom, slug in gardes.items():
    api.post(f"/workspace/demo-velanor/thread/{slug}/update", {"name": nom})
try:
    api.delete("/workspace/banc-bge-m3")
except Exception as e:
    print("banc :", str(e)[:120])
w = api.get("/workspace/demo-velanor")["workspace"][0]
print("fils de Démo Vélanor :", len(w.get("threads", [])), "gardés :", gardes)
print("espaces :", [x["slug"] for x in api.get("/workspaces")["workspaces"]])
