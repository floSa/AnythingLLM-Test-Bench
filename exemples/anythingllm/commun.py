"""Aide commune des exemples : adresse et clé de l'API développeur d'AnythingLLM (bibliothèque standard seulement).
La clé est lue dans donnees/anythingllm/cle-api.txt (créée dans Paramètres › Outils › « Clés API », ou par
outils/anythingllm/client.py) ou dans la variable ANYTHINGLLM_API_KEY. Elle n'est jamais affichée."""
import json, os, urllib.request
from pathlib import Path

BASE = os.environ.get("ANYTHINGLLM_URL", "http://127.0.0.1:3001") + "/api/v1"
_f = Path(__file__).resolve().parents[2] / "donnees/anythingllm/cle-api.txt"
CLE = os.environ.get("ANYTHINGLLM_API_KEY") or _f.read_text().strip()


def appel(methode, chemin, corps=None, donnees=None, entetes=None):
    h = {"Authorization": f"Bearer {CLE}", **(entetes or {})}
    if corps is not None:
        donnees = json.dumps(corps).encode(); h["Content-Type"] = "application/json"
    req = urllib.request.Request(BASE + chemin, data=donnees, method=methode, headers=h)
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read())
