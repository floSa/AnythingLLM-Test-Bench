"""Repérage : ouvre une adresse de l'interface, enregistre une capture brute (donnees/repere/, ignoré par git) et le texte.
Usage (dans le conteneur Playwright) : explorer.py <chemin> [nom]"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = "http://rag-anythingllm:3001"
chemin, nom = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "repere")
out = Path("donnees/repere"); out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1440, "height": 900}, locale="fr-FR")
    pg.goto(BASE + chemin); pg.wait_for_load_state("networkidle"); pg.wait_for_timeout(1500)
    pg.screenshot(path=str(out / f"{nom}.png"))
    print(pg.url); print(pg.inner_text("body")[:3000])
    b.close()
