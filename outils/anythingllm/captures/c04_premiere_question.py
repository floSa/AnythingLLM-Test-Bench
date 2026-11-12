"""Chapitre 04, Première question : créer l'espace « Premier essai », y déposer le rapport annuel, poser une question,
lire la source. Usage : lancer.sh outils/anythingllm/captures/c04_premiere_question.py [espace] [document] [question]
"""
from ui import Scenario, etapes

CH = "04-premiere-question"
NOM = "Premier essai"
SLUG = "premier-essai"
FICHIER = "/depot/corpus/documents/rapport-annuel-2025.pdf"
QUESTION = "Quel est le chiffre d'affaires 2025 de Vélanor ?"


def espace(s):
    p = s.page
    s.aller("/")
    plus = p.locator('button[data-tooltip-id="new-workspace-tooltip"]')
    s.cap("01-bouton-nouvel-espace", [(plus, "+ (Nouvel Espace de Travail)")])
    plus.click()
    nom = p.locator("input#name")
    nom.fill(NOM)
    s.cap("02-nom-de-l-espace", [(nom, "Nom des espaces de travail"), (p.locator("form button[type=submit]").last, "Save")],
          attendre=nom)
    p.locator("form button[type=submit]").last.click()
    p.wait_for_url(f"**/workspace/{SLUG}**"); p.wait_for_load_state("networkidle"); p.wait_for_timeout(1000)


def document(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}")
    ligne = s.lien_espace(SLUG)
    ligne.hover()
    envoi = p.locator(f'a[href="/workspace/{SLUG}"]').locator('xpath=ancestor::*[@role="listitem"][1]').locator(
        'button[data-tooltip-id="upload-workspace"]')
    s.cap("03-icone-envoi", [(envoi, "envoi de documents (flèche vers le haut)")])
    envoi.click()
    zone = p.get_by_text("Cliquez pour télécharger ou glissez-déposez")
    zone.wait_for()
    s.cap("04-gestionnaire-vide", [(p.get_by_text("Mes documents").first, "Mes documents"), (zone, "zone d'envoi"),
                                   (p.get_by_placeholder("https://exemple.com"), "ou soumettre un lien")])
    p.locator("input[type=file]").first.set_input_files(FICHIER)
    p.get_by_text("custom-documents").first.wait_for(timeout=120000)
    p.wait_for_timeout(3000); s.sans_toasts()
    item = p.locator('[data-tooltip-id="directory-item"]').filter(has_text="rapport-annuel-2025")
    if not item.first.is_visible():
        p.get_by_text("custom-documents").first.click(); p.wait_for_timeout(1000)
    s.cap("05-document-televerse", [(item.first, "rapport-annuel-2025.pdf"), (p.locator("button:has(svg)").last, "croix (fermer)")])
    # AnythingLLM 1.19.0 : un fichier envoyé ne peut être placé dans l'espace qu'après fermeture et réouverture de la fenêtre
    s.fermer_gestionnaire()
    s.gestionnaire(SLUG)
    p.get_by_text("custom-documents").first.click(); p.wait_for_timeout(1200)
    item.first.click()
    deplacer = s.bouton("Déplacer vers l'espace de travail")
    deplacer.wait_for()
    s.cap("06-document-coche", [(item.first, "rapport-annuel-2025.pdf (coché)"),
                                (deplacer, "Déplacer vers l'espace de travail")])
    s.sans_toasts()
    deplacer.click()
    p.wait_for_timeout(2000)
    integrer = p.get_by_text("Sauvegarder et intégrer", exact=True)
    try:
        integrer.wait_for(timeout=15000)
    except Exception:
        t = p.inner_text("body"); s.note("après déplacer : " + t[t.find("Premier essai"):][:600].replace("\n", " | "))
        deplacer.click(); p.wait_for_timeout(2000); integrer.wait_for(timeout=15000)
    s.cap("07-sauvegarder-et-integrer", [(p.locator('[data-tooltip-id="ws-directory-item"]').first, "document en attente dans l'espace"),
                                         (integrer, "Sauvegarder et intégrer")])
    integrer.click()
    p.wait_for_timeout(1000)
    p.locator('[data-tooltip-id="ws-directory-item"]').first.wait_for()
    p.wait_for_function("() => !document.body.innerText.includes('Sauvegarder et intégrer')", timeout=180000)
    p.wait_for_timeout(1500)
    s.cap("08-document-integre", [(p.locator('[data-tooltip-id="ws-directory-item"]').first, "document intégré à l'espace")])
    s.note("texte après intégration : " + p.inner_text("body")[-600:].replace("\n", " | "))


def mode(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}")
    ligne = p.locator(f'a[href="/workspace/{SLUG}"]').locator('xpath=ancestor::*[@role="listitem"][1]')
    ligne.hover()
    roue = ligne.locator('button[aria-label="General appearance settings"]')
    s.cap("09-roue-dentee", [(roue, "roue dentée de l'espace")])
    roue.click(); p.wait_for_load_state("networkidle"); p.wait_for_timeout(1000)
    onglet = p.get_by_text("Paramètres du chat", exact=True).first
    onglet.click(); p.wait_for_timeout(1200)
    req = s.bouton("Requête", exact=True)
    req.click(); p.wait_for_timeout(1500)
    s.cap("10-mode-requete", [(onglet, "Paramètres du chat"), (s.bouton("Agent", exact=True), "Agent"),
                              (s.bouton("Chat", exact=True), "Chat"), (req, "Requête")])
    s.note("après Requête : " + p.inner_text("body")[:1500].replace("\n", " | "))


def question(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}")
    champ = p.locator("#primary-prompt-input")
    champ.fill(QUESTION)
    s.cap("11-question", [(champ, "Envoyer un message"), (p.locator('button[data-tooltip-id="send-prompt"]'), "Envoyer")])
    p.locator('button[data-tooltip-id="send-prompt"]').click()
    sources = p.get_by_role("button", name="Sources")
    try:
        sources.last.wait_for(timeout=300000)
    except Exception:
        s.note("pas de bouton Sources après 300 s : " + p.inner_text("body")[-800:].replace("\n", " | "))
    p.locator("#stop-generation-button").wait_for(state="detached", timeout=300000)
    p.wait_for_timeout(3000)
    s.cap("12-reponse", [(p.locator(".markdown, [class*=markdown]").last, "réponse"), (sources.last, "Sources")])
    sources.last.click()
    p.wait_for_timeout(1000)
    doc = p.get_by_text("rapport-annuel-2025", exact=False).last
    s.cap("13-panneau-sources", [(doc, "rapport-annuel-2025.pdf")])
    doc.click()
    p.wait_for_timeout(1000)
    s.cap("14-extrait-cite", [(p.get_by_text("match").first, "pourcentage de similarité"),
                              (p.locator("button[aria-label=Close]").last, "fermer")])
    s.note("réponse : " + p.inner_text("body")[-1500:].replace("\n", " | "))


def reprise(s):
    """Rouvre la conversation (sans reposer la question) et refait les captures de la réponse et des sources."""
    import re
    p = s.page
    s.aller(f"/workspace/{SLUG}")
    p.locator("[aria-label=Threads]").get_by_text("Quel est le chiffre", exact=False).first.click()
    p.wait_for_load_state("networkidle"); p.wait_for_timeout(2500)
    reponse = p.get_by_text("48,6", exact=False).last
    sources = p.get_by_role("button", name="Sources").last
    s.cap("12-reponse", [(p.get_by_text("Réflexions", exact=True).last, "Réflexions (repliées)"), (reponse, "réponse"),
                         (sources, "Sources")])
    sources.click(); p.wait_for_timeout(1200)
    doc = p.get_by_text("rapport-annuel-2025", exact=False).last
    s.cap("13-panneau-sources", [(doc, "rapport-annuel-2025.pdf")])
    doc.click(); p.wait_for_timeout(1200)
    s.cap("14-extrait-cite", [(p.get_by_text(re.compile(r"Referenced \d+ times")).first, "Referenced 4 times."),
                              (p.get_by_text("Chiffre d'affaires48,6", exact=False).first, "passage cité"),
                              (p.locator("button[aria-label=Close]").last, "fermer")])


if __name__ == "__main__":
    s = Scenario(CH)
    try:
        etapes([espace, document, mode, question, reprise], s)
    finally:
        s.fermer()
