"""Crée l'espace « Exemple-API » en mode requête, y téléverse la FAQ du service après-vente et l'intègre."""
import uuid
from pathlib import Path
from commun import appel

esp = appel("POST", "/workspace/new", {"name": "Exemple-API", "chatMode": "query", "topN": 4})["workspace"]
print("espace créé :", esp["slug"], "mode", esp["chatMode"])
fichier = Path(__file__).resolve().parents[2] / "corpus/documents/faq-sav.html"
borne = uuid.uuid4().hex
corps = (f"--{borne}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{fichier.name}\"\r\n"
         f"Content-Type: text/html\r\n\r\n").encode() + fichier.read_bytes() + \
        f"\r\n--{borne}\r\nContent-Disposition: form-data; name=\"addToWorkspaces\"\r\n\r\n{esp['slug']}\r\n--{borne}--\r\n".encode()
r = appel("POST", "/document/upload", donnees=corps, entetes={"Content-Type": f"multipart/form-data; boundary={borne}"})
d = r["documents"][0]
print("téléversé :", r["success"], d["title"], d["wordCount"], "mots ->", d["location"])
docs = appel("GET", f"/workspace/{esp['slug']}")["workspace"][0]["documents"]
print("documents dans l'espace :", [x["filename"] for x in docs])
