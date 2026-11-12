"""Chapitre 09, Sources externes : site web local de test (outils/anythingllm/essais/site.sh), dépôt GitHub public,
vidéo YouTube, lien simple. Espace « Sources externes ».
Usage : lancer.sh outils/anythingllm/captures/c09_sources_externes.py [espace] [liste] [site] [github] [youtube] [lien] [resultat]
"""
from ui import Scenario, etapes

CH = "09-sources-externes"
NOM, SLUG = "Sources externes", "sources-externes"
SITE = "http://rag-anythingllm-site/index.html"
DEPOT = "https://github.com/octocat/Hello-World"
VIDEO = "https://www.youtube.com/watch?v=jNQXAC9IVRw"


def ouvrir(s, onglet=True):
    p = s.page
    s.aller(f"/workspace/{SLUG}")
    ligne = p.locator(f'a[href="/workspace/{SLUG}"]').locator('xpath=ancestor::*[@role="listitem"][1]')
    ligne.hover(); ligne.locator('button[data-tooltip-id="upload-workspace"]').click()
    p.get_by_text("Mes documents").first.wait_for(); p.wait_for_timeout(800)
    if onglet:
        p.get_by_text("Connecteurs de données").first.click(); p.wait_for_timeout(1000)


def espace(s):
    p = s.page
    s.aller("/")
    p.locator('button[data-tooltip-id="new-workspace-tooltip"]').click()
    p.locator("input#name").fill(NOM); p.locator("form button[type=submit]").last.click()
    p.wait_for_url(f"**/workspace/{SLUG}**")


def liste(s):
    p = s.page
    ouvrir(s)
    s.cap("01-connecteurs", [(p.get_by_text("Connecteurs de données").first, "Connecteurs de données"),
                             (p.get_by_text("GitHub", exact=False).first, "GitHub Repo"),
                             (p.get_by_text("YouTube", exact=False).first, "YouTube Transcript"),
                             (p.get_by_text("Bulk Link Scraper").first.or_(p.get_by_text("Site", exact=False).first), "site web (en profondeur)")])
    s.note("connecteurs : " + p.inner_text("body")[-1500:].replace("\n", " | "))


def _soumettre(s, nom, carte, champs, capture, attente=240000):
    p = s.page
    ouvrir(s)
    p.get_by_text(carte, exact=False).first.click(); p.wait_for_timeout(800)
    elems = []
    for name, val, lib in champs:
        loc = p.locator(f"[name={name}]")
        loc.fill(str(val)); elems.append((loc, lib))
    sub = p.locator("form button[type=submit]").last
    elems.append((sub, sub.inner_text().strip() or "envoyer"))
    s.cap(capture, elems)
    sub.click()
    try:
        p.wait_for_function("() => !document.querySelector('form button[type=submit][disabled]')", timeout=attente)
    except Exception as e:
        s.note(f"{nom} : attente dépassée " + str(e)[:100])
    p.wait_for_timeout(3000)
    s.note(f"{nom} après envoi : " + p.inner_text("body")[-700:].replace("\n", " | "))


def site(s):
    _soumettre(s, "site", "Bulk Link Scraper", [("url", SITE, "URL du site"), ("depth", 1, "profondeur"), ("maxLinks", 5, "nombre maximal de pages")],
               "02-site-web")


def github(s):
    _soumettre(s, "github", "GitHub", [("repo", DEPOT, "URL du dépôt GitHub")], "03-github")


def youtube(s):
    _soumettre(s, "youtube", "YouTube", [("url", VIDEO, "URL de la vidéo YouTube")], "04-youtube")


def lien(s):
    p = s.page
    ouvrir(s, onglet=False)
    champ = p.get_by_placeholder("https://exemple.com")
    champ.fill("http://rag-anythingllm-site/livraisons.html")
    s.cap("05-lien-simple", [(champ, "ou soumettre un lien"), (s.bouton("Récupérer le site web"), "Récupérer le site web")])
    s.bouton("Récupérer le site web").click(); p.wait_for_timeout(8000)
    s.note("lien après envoi : " + p.inner_text("body")[:1200].replace("\n", " | "))


def resultat(s):
    p = s.page
    ouvrir(s, onglet=False)
    p.wait_for_timeout(1500)
    s.cap("06-documents-importes", [(p.locator('[data-tooltip-id="directory-item"], #directory-item').first, "dossiers des documents importés")], plein=False)
    s.note("mes documents : " + p.inner_text("body")[:2500].replace("\n", " | "))


if __name__ == "__main__":
    s = Scenario(CH)
    try:
        etapes([espace, liste, site, github, youtube, lien, resultat], s)
    finally:
        s.fermer()
