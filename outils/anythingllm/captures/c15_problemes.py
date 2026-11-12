"""Chapitre 15, En cas de problème : erreurs réellement provoquées dans l'interface, puis remises en état.
Usage : lancer.sh ... c15_problemes.py [mot_de_passe] [fichier] [agent_vide] [cle] [max_tokens] [ocr]
"""
import os, re
from ui import Scenario, etapes, identifiants

CH = "15-problemes"


def mot_de_passe(s):
    ctx = s.navigateur.new_context(viewport={"width": 1440, "height": 900}, locale="fr-FR")
    ctx.add_init_script("localStorage.setItem('i18nextLng','fr')")
    vieux, s.page = s.page, ctx.new_page(); p = s.page
    s.aller("/")
    if p.locator("input[name=username]").count():
        p.locator("input[name=username]").fill(identifiants()["anythingllm.admin.utilisateur"])
    p.locator("input[name=password]").fill("mauvais-mot-de-passe")
    p.locator("form button[type=submit]").click(); p.wait_for_timeout(2000)
    s.cap_souple("01-mauvais-mot-de-passe", [(p.get_by_text(re.compile("Error|Erreur|invalid|Invalid")).first, "message d'erreur")])
    s.note("mot de passe : " + p.inner_text("body")[:500].replace("\n", " | "))
    ctx.close(); s.page = vieux


def fichier(s):
    p = s.page
    f = "/depot/donnees/anythingllm-essai-format.xyz"
    open(f, "w").write("format inconnu")
    s.gestionnaire("premier-essai")
    p.locator("input[type=file]").first.set_input_files(f); p.wait_for_timeout(4000)
    s.cap_souple("02-extension-inconnue", [(p.get_by_text("anythingllm-essai-format.xyz").first, "fichier accepté malgré une extension inconnue")])
    s.note("fichier : " + p.inner_text("body")[:1500].replace("\n", " | "))


def agent_vide(s):
    p = s.page
    s.aller("/workspace/premier-essai/settings/chat-settings")
    s.bouton("Agent", exact=True).click(); p.wait_for_timeout(1500)
    s.aller("/workspace/premier-essai")
    p.locator("[aria-label=Threads]").get_by_text("New Thread", exact=True).last.click(); p.wait_for_timeout(2500)
    p.locator("#primary-prompt-input").fill("Quel est le résultat net 2025 de Vélanor ?")
    p.locator('button[data-tooltip-id="send-prompt"]').click()
    p.wait_for_timeout(5000)
    try:
        p.wait_for_function("() => !document.body.innerText.includes('Thinking...') && !document.querySelector('#stop-generation-button')", timeout=240000)
    except Exception:
        pass
    p.wait_for_timeout(8000)
    s.cap_souple("03-reponse-vide-mode-agent", [(p.get_by_text(re.compile("Thought for|Réflexions")).last, "réflexion seule, sans réponse")])
    s.note("agent vide : " + p.inner_text("body")[-900:].replace("\n", " | "))
    s.aller("/workspace/premier-essai/settings/chat-settings")
    s.bouton("Requête", exact=True).click(); p.wait_for_timeout(1500)


def _llm(s, cle=None, max_tokens=None):
    p = s.page
    s.aller("/settings/llm-preference"); p.wait_for_timeout(1500)
    if cle is not None:
        p.locator("[name=GenericOpenAiKey]").fill(cle)
    if max_tokens is not None:
        p.locator("[name=GenericOpenAiMaxTokens]").fill(str(max_tokens))
    p.get_by_role("button", name=re.compile("Save changes|Enregistrer")).first.click(); p.wait_for_timeout(2000)


def _question(s, q):
    p = s.page
    s.aller("/workspace/premier-essai")
    p.locator("[aria-label=Threads]").get_by_text("New Thread", exact=True).last.click(); p.wait_for_timeout(2500)
    p.locator("#primary-prompt-input").fill(q)
    p.locator('button[data-tooltip-id="send-prompt"]').click(); p.wait_for_timeout(5000)
    try:
        p.wait_for_function("() => !document.body.innerText.includes('Thinking...') && !document.body.innerText.includes('Le modèle réfléchit') && !document.querySelector('#stop-generation-button')", timeout=240000)
    except Exception:
        pass
    p.wait_for_timeout(4000)


def cle(s):
    p = s.page
    _llm(s, cle="cle-fausse-pour-essai")
    _question(s, "Quel est le chiffre d'affaires 2025 de Vélanor ?")
    try:
        p.get_by_text("Could not respond to message", exact=False).last.wait_for(timeout=60000)
    except Exception:
        pass
    s.cap_souple("04-cle-refusee", [(p.get_by_text("Could not respond to message", exact=False).last, "Could not respond to message."),
                                    (p.get_by_text("No connected db", exact=False).last, "400 No connected db.")])
    s.note("clé fausse : " + p.inner_text("body")[-900:].replace("\n", " | "))
    _llm(s, cle=os.environ["LLM_CENTRAL_KEY"])


def max_tokens(s):
    p = s.page
    _llm(s, max_tokens=64)
    _question(s, "Explique en détail l'évolution du chiffre d'affaires trimestriel de Vélanor en 2025.")
    s.cap_souple("05-reponse-coupee", [(p.get_by_text(re.compile("Thought for|Réflexions")).last, "réflexion coupée, réponse vide ou tronquée")])
    s.note("max tokens 64 : " + p.inner_text("body")[-900:].replace("\n", " | "))
    _llm(s, max_tokens=8192)


def ocr(s):
    p = s.page
    s.aller("/workspace/demo-velanor")
    _question_demo = "Quelle est la pénalité de retard prévue par le contrat Batterix ?"
    p.locator("[aria-label=Threads]").get_by_text("New Thread", exact=True).last.click(); p.wait_for_timeout(2500)
    n = p.get_by_role("button", name="Sources").count()
    p.locator("#primary-prompt-input").fill(_question_demo)
    p.locator('button[data-tooltip-id="send-prompt"]').click()
    p.wait_for_function(f"() => [...document.querySelectorAll('button')].filter(b => b.innerText.trim().startsWith('Sources')).length > {n}", timeout=300000)
    p.wait_for_timeout(3000)
    p.get_by_role("button", name="Sources").last.click(); p.wait_for_timeout(1200)
    p.get_by_text("contrat-batterix-scan.pdf").last.click(); p.wait_for_timeout(1500)
    s.cap_souple("06-texte-ocr", [(p.get_by_text("Bréme", exact=False).first, "« Bréme » au lieu de « Brême »"),
                                  (p.get_by_text("I'Acheteur", exact=False).first, "« I'Acheteur » au lieu de « l'Acheteur »")])
    s.note("ocr : " + p.inner_text("body")[-1500:].replace("\n", " | "))


def reprise(s):
    """Rouvre les fils des essais (sans rien reposer) pour annoter les messages d'erreur et le texte lu par OCR."""
    p = s.page
    s.aller("/workspace/premier-essai")
    for fil in p.locator("[aria-label=Threads] a").all():
        fil.click(); p.wait_for_load_state("networkidle"); p.wait_for_timeout(1500)
        if p.get_by_text("Could not respond to message", exact=False).count():
            s.cap_souple("04-cle-refusee", [(p.get_by_text("Could not respond to message", exact=False).last, "Could not respond to message."),
                                            (p.get_by_text("No connected db", exact=False).last, "400 No connected db.")])
            break
    s.aller("/workspace/demo-velanor")
    p.locator("[aria-label=Threads] a").filter(has_text="Quelle est la pénalit").first.click()
    p.wait_for_load_state("networkidle"); p.wait_for_timeout(2000)
    p.get_by_role("button", name=re.compile("^Sources")).last.click(); p.wait_for_timeout(1200)
    p.get_by_text("contrat-batterix-scan.pdf").last.click(); p.wait_for_timeout(1500)
    s.cap_souple("06-texte-ocr", [(p.get_by_text("Bréme", exact=False).first, "« Bréme » au lieu de « Brême »"),
                                  (p.get_by_text("I'Acheteur", exact=False).first, "« I'Acheteur » au lieu de « l'Acheteur »")])


if __name__ == "__main__":
    s = Scenario(CH)
    try:
        etapes([mot_de_passe, fichier, agent_vide, cle, max_tokens, ocr], s)
    finally:
        s.fermer()
