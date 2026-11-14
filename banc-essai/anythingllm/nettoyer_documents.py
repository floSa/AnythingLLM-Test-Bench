#!/usr/bin/env python3
"""Supprime de « Mes documents » les fichiers téléversés qui ne sont dans aucun espace listé à garder.
Usage : nettoyer_documents.py [--garder slug1,slug2] [--motif texte]   (sans --motif : tous les fichiers non gardés)
Sert à retirer les restes d'essais (banc, scénarios) sans toucher au jeu de démonstration."""
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from client import API, _req

p = argparse.ArgumentParser(); p.add_argument("--garder", default=""); p.add_argument("--motif", default="")
a = p.parse_args()
api = API()
gardes = set()
for slug in filter(None, a.garder.split(",")):
    for d in api.get(f"/workspace/{slug}")["workspace"][0]["documents"]:
        gardes.add(d["docpath"])
noms = []
def parcourir(n, chemin=""):
    for it in n.get("items", []):
        if it.get("type") == "folder":
            parcourir(it, it["name"])
        else:
            noms.append(f"{chemin}/{it['name']}")
parcourir(api.get("/documents")["localFiles"])
a_supprimer = [n for n in noms if n not in gardes and a.motif in n]
if a_supprimer:
    _req("DELETE", "/api/v1/system/remove-documents", {"names": a_supprimer}, jeton=api.cle)
# dossiers devenus vides (sauf custom-documents)
vides = 0
for it in api.get("/documents")["localFiles"].get("items", []):
    if it.get("type") == "folder" and it["name"] != "custom-documents" and not it.get("items") and a.motif in it["name"]:
        _req("DELETE", "/api/v1/document/remove-folder", {"name": it["name"]}, jeton=api.cle); vides += 1
print(f"{len(a_supprimer)} fichier(s) supprimé(s), {len(noms) - len(a_supprimer)} gardé(s), {vides} dossier(s) vide(s) supprimé(s)")
