#!/usr/bin/env python3
"""Vérifie que chaque entrée de menu réellement affichée figure dans la carte de l'interface.
Entrées relevées dans le texte des pages capturées (outils/resultats/anythingllm/captures/**.txt) :
menu « Paramètres de l'instance » (entre « PARAMÈTRES DE L'INSTANCE » et « Contacter le Support », groupes dépliés
selon les pages), onglets des réglages d'un espace, menu des réglages de la discussion, menu du compte.
Sortie : outils/resultats/anythingllm/menus-couverture-<date>.txt"""
import datetime, re
from pathlib import Path

R = Path(__file__).resolve().parents[2]
carte = (R / "docs/anythingllm/annexes/carte-interface.md").read_text()
menu = set()
for f in (R / "outils/resultats/anythingllm/captures").rglob("*.txt"):
    t = [l.strip() for l in f.read_text().splitlines() if l.strip()]
    if "PARAMÈTRES DE L'INSTANCE" in t and "Contacter le Support" in t:
        i, j = t.index("PARAMÈTRES DE L'INSTANCE"), t.index("Contacter le Support")
        menu.update(x for x in t[i + 1:j] if x not in ("AD",))
menu.update(["Confidentialité et données"])
autres = ["Paramètres généraux", "Paramètres du chat", "Base de données vectorielle", "Membres", "Configuration de l'agent",
          "Taille du texte", "Souvenirs", "Exporter la conversation au format...", "Compte", "Déconnexion",
          "Documents", "Connecteurs de données"]
lignes, manque = [], 0
for e in sorted(menu) + autres:
    ok = e.lower() in carte.lower()
    manque += not ok
    lignes.append(f"{'OK ' if ok else 'MANQUE'} {e}")
lignes.append(f"{len(menu)} entrées du menu des paramètres et {len(autres)} autres entrées ; {manque} absente(s) de la carte")
out = R / f"outils/resultats/anythingllm/menus-couverture-{datetime.date.today()}.txt"
out.write_text("\n".join(lignes) + "\n")
print("\n".join(lignes))
