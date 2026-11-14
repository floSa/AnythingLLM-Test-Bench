"""Pose une question en mode requête à l'espace « Exemple-API » et affiche la réponse (sans la réflexion) et ses sources."""
import re, time
from commun import appel

t0 = time.time()
r = appel("POST", "/workspace/exemple-api/chat",
          {"message": "Quelle est la durée de garantie d'un cadre de vélo Vélanor ?", "mode": "query",
           "sessionId": "exemple-04"})
texte = r["textResponse"]
print("réflexion présente dans textResponse :", texte.lstrip().startswith("<think>"))
print("réponse :", re.sub(r"<think>.*?</think>", "", texte, flags=re.S).strip()[:400])
for s in r["sources"]:
    print(f"source : {s['title']}  score={round(s['score'], 3)}  extrait={s['text'][:80]!r}")
print(f"durée : {time.time() - t0:.1f} s")
