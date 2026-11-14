"""Liste les espaces de travail et leurs réglages principaux."""
from commun import appel

for w in appel("GET", "/workspaces")["workspaces"]:
    print(f"{w['slug']:20} mode={w['chatMode']:9} topN={w['topN']} seuil={w['similarityThreshold']} "
          f"recherche={w['vectorSearchMode']} historique={w['openAiHistory']}")
