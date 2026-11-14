"""Interroge l'espace par la route compatible OpenAI (le « modèle » est le nom court de l'espace)."""
import re
from commun import appel

print("modèles :", [m["id"] for m in appel("GET", "/openai/models")["data"]])
r = appel("POST", "/openai/chat/completions", {"model": "exemple-api", "stream": False, "temperature": 0,
          "messages": [{"role": "user", "content": "Combien de temps dure la garantie de la batterie ?"}]})
print("réponse :", re.sub(r"<think>.*?</think>", "", r["choices"][0]["message"]["content"], flags=re.S).strip()[:300])
