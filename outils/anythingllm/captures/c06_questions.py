"""Chapitre 06, Poser des questions et lire les sources, dans « Démo Vélanor » : mode Requête, question, réflexion,
actions sur la réponse, question sans réponse, mode Chat, fils, commandes abrégées, export.
Usage : lancer.sh outils/anythingllm/captures/c06_questions.py [mode] [question] [actions] [piege] [fils] [commandes] [export]
"""
from ui import Scenario, etapes

CH = "06-questions-et-sources"
SLUG = "demo-velanor"
Q1 = "Combien de vélos Vélanor a-t-elle produits en 2025, et dans quelle usine ?"
PIEGE = "Quel est le cours de l'action Vélanor en bourse ?"


def menu_chat(p):
    return p.locator("div.absolute.z-30 > button[type=button]").first


def attendre_reponse(s, n_avant):
    p = s.page
    p.wait_for_function(f"() => !document.querySelector('#stop-generation-button')", timeout=300000)
    p.wait_for_timeout(2500)


def mode(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}/settings/chat-settings")
    req = s.bouton("Requête", exact=True)
    s.cap("01-mode-de-chat", [(s.bouton("Agent", exact=True), "Agent"), (s.bouton("Chat", exact=True), "Chat"), (req, "Requête")],
          attendre=req)
    req.click(); p.wait_for_timeout(1500)
    s.note("après choix Requête : " + p.inner_text("main")[:600].replace("\n", " | ") if p.locator("main").count() else "")


def question(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}")
    p.locator("#primary-prompt-input").fill(Q1)
    p.locator('button[data-tooltip-id="send-prompt"]').click()
    p.wait_for_timeout(2000)
    try:
        p.locator("#stop-generation-button").wait_for(timeout=10000)
        s.cap("02-reponse-en-cours", [(p.locator("#stop-generation-button"), "arrêter la génération"),
                                      (p.get_by_text("Thinking...").last, "Thinking...")])
    except Exception as e:
        s.note("pas de capture en cours : " + str(e)[:100])
    p.locator("#stop-generation-button").wait_for(state="detached", timeout=300000)
    p.wait_for_timeout(2500)
    pensee = p.get_by_text("Thought for", exact=False).last
    sources = p.get_by_role("button", name="Sources").last
    s.cap("03-reponse-et-sources", [(pensee, "réflexion repliée (Thought for …)"), (sources, "Sources")])
    pensee.click(); p.wait_for_timeout(1000)
    s.cap("04-reflexion-depliee", [(pensee, "réflexion dépliée")])
    pensee.click()
    sources.click(); p.wait_for_timeout(1200)
    s.cap("05-panneau-sources", [(p.get_by_text("Références").first.or_(p.get_by_text("référence").first), "documents cités")])
    s.note("réponse Q1 : " + p.inner_text("body")[-2500:].replace("\n", " | "))


def actions(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}")
    p.wait_for_timeout(1500)
    rep = p.locator("[class*=group]").filter(has=p.get_by_role("button", name="Copier")).last
    rep.hover()
    plus = p.get_by_role("button", name="Plus d'actions").last
    s.cap("06-actions-sur-la-reponse", [(p.get_by_role("button", name="Copier").last, "Copier"),
                                        (p.get_by_role("button", name="Régénérer").last, "Régénérer"),
                                        (p.get_by_role("button", name="Bonne réponse").last, "Bonne réponse"),
                                        (plus, "Plus d'actions")])
    plus.click(); p.wait_for_timeout(600)
    s.cap("07-plus-d-actions", [(p.get_by_text("Dupliquer").last, "Dupliquer"), (p.get_by_text("Supprimer").last, "Supprimer")])
    p.keyboard.press("Escape")


def piege(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}")
    p.locator("#primary-prompt-input").fill(PIEGE)
    p.locator('button[data-tooltip-id="send-prompt"]').click(); p.wait_for_timeout(3000)
    p.locator("#stop-generation-button").wait_for(state="detached", timeout=300000); p.wait_for_timeout(2500)
    s.cap("08-question-sans-reponse", [(p.locator("#chat-history, [id*=chat]").last.get_by_text("cours").last, "question sans réponse dans les documents")])
    s.note("réponse piège Requête : " + p.inner_text("body")[-1500:].replace("\n", " | "))


def fils(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}")
    nouveau = p.get_by_text("New Thread", exact=True).last
    s.cap("09-nouveau-fil", [(p.locator("[aria-label=Threads]"), "fils de l'espace"), (nouveau, "New Thread")])
    nouveau.click(); p.wait_for_timeout(2500)
    opt = p.locator("button[aria-label='Thread options']").last
    p.locator("[aria-label=Threads] a").last.hover()
    opt.click(); p.wait_for_timeout(600)
    s.cap("10-options-du-fil", [(p.get_by_text("Rename", exact=True), "Rename"), (p.get_by_text("Delete Thread", exact=True), "Delete Thread")])
    p.once("dialog", lambda d: d.accept("Questions production"))
    p.get_by_text("Rename", exact=True).click(); p.wait_for_timeout(1500)
    s.note("fils : " + p.locator("[aria-label=Threads]").inner_text().replace("\n", " | "))


def commandes(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}")
    p.locator("#tools-btn").click(); p.wait_for_timeout(800)
    s.cap("11-commandes-abregees", [(p.get_by_text("Commandes abrégées").first, "Commandes abrégées"),
                                    (p.get_by_text("/reset").first, "/reset"), (s.bouton("Ajouter").first, "Ajouter"),
                                    (p.get_by_text("Compétences des agents").first, "Compétences des agents")])
    s.bouton("Ajouter").first.click(); p.wait_for_timeout(600)
    p.fill("#command", "resume")
    p.fill("#prompt", "Résume en trois points les documents de cet espace.")
    p.fill("#description", "Résumé rapide de l'espace")
    s.cap("12-ajouter-une-commande", [(p.locator("#command"), "commande"), (p.locator("#prompt"), "prompt"),
                                      (p.locator("#description"), "description"), (s.bouton("Sauvegarder").last, "Sauvegarder")])
    s.bouton("Sauvegarder").last.click(); p.wait_for_timeout(1500)


def export(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}")
    p.locator("[aria-label=Threads] a").first.click(); p.wait_for_load_state("networkidle"); p.wait_for_timeout(1500)
    menu_chat(p).click(); p.wait_for_timeout(600)
    exp = p.get_by_text("Exporter la conversation", exact=False).first
    s.cap("13-menu-de-la-discussion", [(menu_chat(p), "réglages de la discussion"), (p.get_by_text("Taille du texte").first, "Taille du texte"),
                                       (p.get_by_text("Souvenirs").first, "Souvenirs"), (exp, "Exporter la conversation au format...")])
    exp.hover(); exp.click(); p.wait_for_timeout(800)
    s.note("menu export : " + p.inner_text("body")[-500:].replace("\n", " | "))
    s.cap("14-formats-d-export", [(p.get_by_text("JSON", exact=False).last, "formats proposés")])


if __name__ == "__main__":
    s = Scenario(CH)
    try:
        etapes([mode, question, actions, piege, fils, commandes, export], s)
    finally:
        s.fermer()
