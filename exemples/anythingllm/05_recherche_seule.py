"""Recherche des passages sans appeler le modèle de réponse (route vector-search)."""
from commun import appel

r = appel("POST", "/workspace/exemple-api/vector-search", {"query": "garantie batterie", "topN": 3, "scoreThreshold": 0.2})
for x in r["results"]:
    print(f"{x['score']:.3f}  {x['metadata']['title']}  {x['text'][:90]!r}")
