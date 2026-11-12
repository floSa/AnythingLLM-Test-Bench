"""Supprime l'espace « Exemple-API » créé par les exemples (le fichier reste dans « Mes documents »)."""
from commun import appel, BASE, CLE
import urllib.request

req = urllib.request.Request(BASE + "/workspace/exemple-api", method="DELETE", headers={"Authorization": f"Bearer {CLE}"})
print("suppression :", urllib.request.urlopen(req).status)
print("espaces restants :", [w["slug"] for w in appel("GET", "/workspaces")["workspaces"]])
