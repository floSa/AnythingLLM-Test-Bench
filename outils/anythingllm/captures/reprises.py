"""Captures reprises après la relecture novice (pastilles décalées ou écran incomplet), sans changer l'état de l'instance
sauf l'acceptation des conditions des fonctions expérimentales et une question posée pour la capture de l'OCR.
Usage : lancer.sh outils/anythingllm/captures/reprises.py [etapes]"""
import re
from ui import Scenario, etapes


def agents(s):
    p = s.page; s.chapitre = "10-agents"
    s.aller("/settings/agents"); p.wait_for_timeout(2000)
    s.cap_souple("01-competences", [(p.get_by_text("RAG et mémoire à long terme", exact=False).first, "RAG et mémoire à long terme"),
                                    (p.get_by_text("Recherche web en direct", exact=False).first, "Recherche web en direct et navigation"),
                                    (p.get_by_text("Générer des graphiques", exact=False).first, "Générer des graphiques"),
                                    (p.get_by_text("Agent Flows", exact=True).first, "Agent Flows"),
                                    (p.get_by_text("Serveurs MCP", exact=False).first, "Serveurs MCP")])
    vo = p.get_by_text("Velanor Outils", exact=True).first
    vo.click(); p.wait_for_timeout(2000)
    s.cap_souple("05-serveur-mcp", [(p.get_by_text("Rafraîchir", exact=True).first, "Rafraîchir"), (vo, "Velanor Outils"),
                                    (p.get_by_text("1/1 outils activés", exact=False).first, "1/1 outils activés"),
                                    (p.get_by_text("stock_piece", exact=True).first, "outil stock_piece"),
                                    (p.get_by_text("ConsignesBatteries", exact=False).first, "flow ConsignesBatteries")])


def experimental(s):
    p = s.page; s.chapitre = "12-administrer"
    s.aller("/settings/beta-features"); p.wait_for_timeout(2500)
    s.cap_souple("13b-live-document-sync", [(p.get_by_text("Live Document Sync", exact=False).first, "Live Document Sync")])
    s.note("expérimental : " + p.inner_text("body")[-900:].replace("\n", " | "))


def admin(s):
    p = s.page; s.chapitre = "12-administrer"
    s.aller("/settings/workspaces"); p.wait_for_timeout(1500)
    s.cap_souple("04-espaces-de-travail", [(p.get_by_text("New Workspace", exact=False).first, "New Workspace"),
                                           (p.get_by_text("Démo Vélanor", exact=True).first, "Démo Vélanor")])
    s.aller("/settings/beta-features"); p.wait_for_timeout(2000)
    comp = p.get_by_role("button", name="I understand")
    s.cap_souple("13-experimental", [(p.get_by_role("button", name=re.compile("Reject")).first, "Reject & close"), (comp.first, "I understand")])
    try:
        comp.first.click(); p.wait_for_timeout(6000); s.aller("/settings/beta-features"); p.wait_for_timeout(2000)
    except Exception as e:
        s.note("conditions : " + str(e)[:100])
    s.cap_souple("13b-live-document-sync", [(p.get_by_text("Live Document Sync", exact=False).first, "Live Document Sync")])
    s.note("expérimental après acceptation : " + p.inner_text("body")[-900:].replace("\n", " | "))
    s.aller("/api/docs"); p.wait_for_timeout(3000); p.mouse.wheel(0, -3000); p.wait_for_timeout(500)
    s.cap_souple("14-documentation-api", [(p.get_by_role("button", name=re.compile("Authorize")).first, "Authorize"),
                                          (p.get_by_text("Workspaces", exact=True).first, "Workspaces")])


def widget(s):
    p = s.page; s.chapitre = "13-comptes-et-widget"
    s.aller("/settings/embed-chat-widgets"); p.wait_for_timeout(1500)
    p.get_by_role("button").filter(has_text="Créer un widget intégré").first.click(); p.wait_for_timeout(1200)
    sel = p.locator("select[name=workspace_id]"); sel.select_option(label="Démo Vélanor")
    q = p.locator("input[name=chat_mode][value=query]"); q.check(force=True)
    p.locator("input[name=max_chats_per_day]").fill("200")
    s.cap_souple("12-nouveau-widget", [(q.locator("xpath=.."), "mode Requête (Query)"),
                                       (p.get_by_text("Restrict requests from domains", exact=False).first, "domaines autorisés"),
                                       (p.locator("input[name=max_chats_per_day]"), "limite par jour"),
                                       (p.get_by_role("button").filter(has_text="Create embed").last, "Create embed")])
    p.keyboard.press("Escape")


def citation(s):
    p = s.page; s.chapitre = "04-premiere-question"
    s.aller("/workspace/premier-essai")
    p.locator("[aria-label=Threads]").get_by_text("Quel est le chiffre", exact=False).first.click()
    p.wait_for_load_state("networkidle"); p.wait_for_timeout(2500)
    p.get_by_role("button", name=re.compile("^Sources")).last.click(); p.wait_for_timeout(1200)
    p.get_by_text("rapport-annuel-2025", exact=False).last.click(); p.wait_for_timeout(1500)
    s.cap_souple("14-extrait-cite", [(p.get_by_text(re.compile(r"Referenced \d+ times")).first, "Referenced 4 times."),
                                     (p.get_by_text(re.compile(r"^\d+% match$")).first, "pourcentage de similarité"),
                                     (p.locator("button[aria-label=Close]").last, "fermer")])


def ocr(s):
    p = s.page; s.chapitre = "15-problemes"
    s.aller("/workspace/demo-velanor")
    p.locator("[aria-label=Threads]").get_by_text("New Thread", exact=True).last.click(); p.wait_for_timeout(2500)
    n = p.get_by_role("button", name=re.compile("^Sources")).count()
    p.locator("#primary-prompt-input").fill("Quelle est la pénalité de retard prévue par le contrat Batterix ?")
    p.locator('button[data-tooltip-id="send-prompt"]').click()
    p.wait_for_function(f"() => [...document.querySelectorAll('button')].filter(b => b.innerText.trim().startsWith('Sources')).length > {n}", timeout=300000)
    p.wait_for_timeout(3000)
    p.get_by_role("button", name=re.compile("^Sources")).last.click(); p.wait_for_timeout(1200)
    p.get_by_text("contrat-batterix-scan.pdf").last.click(); p.wait_for_timeout(1500)
    s.cap_souple("06-texte-ocr", [(p.get_by_text("Bréme", exact=False).first, "« Bréme » au lieu de « Brême »"),
                                  (p.get_by_text("Nantes (I'Acheteur)", exact=False).first, "« I'Acheteur » au lieu de « l'Acheteur »")])


def envoi(s):
    """Chapitre 04, capture 05 : fichier envoyé et croix de la fenêtre (doublon d'essai supprimé ensuite)."""
    p = s.page; s.chapitre = "04-premiere-question"
    s.gestionnaire("premier-essai")
    p.locator("input[type=file]").first.set_input_files("/depot/corpus/documents/rapport-annuel-2025.pdf")
    p.wait_for_timeout(5000); s.sans_toasts()
    if not p.get_by_text("Cliquez pour télécharger", exact=False).count():
        pass
    croix = p.evaluate_handle("() => { const b = document.elementFromPoint(1366, 126); return b && b.closest('button'); }").as_element()
    item = p.locator('[data-tooltip-id="directory-item"]').filter(has_text="rapport-annuel-2025").first
    if not item.is_visible():
        p.get_by_text("custom-documents").first.click(); p.wait_for_timeout(1000)
    from playwright.sync_api import Locator
    s.cap_souple("05-document-televerse", [(item, "rapport-annuel-2025.pdf"), (p.locator("button:near(:text('Connecteurs de données'))").last if croix is None else p.locator("xpath=//button[.//*[name()='svg']]").filter(has_not_text=" ").nth(0), "croix (fermer)")])


def croix_seule(s):
    p = s.page; s.chapitre = "04-premiere-question"
    s.gestionnaire("premier-essai")
    p.locator("input[type=file]").first.set_input_files("/depot/corpus/documents/rapport-annuel-2025.pdf")
    p.wait_for_timeout(5000); s.sans_toasts()
    item = p.locator('[data-tooltip-id="directory-item"]').filter(has_text="rapport-annuel-2025").first
    if not item.is_visible():
        p.get_by_text("custom-documents").first.click(); p.wait_for_timeout(1000)
    p.evaluate("() => { const b = document.elementFromPoint(1366, 126).closest('button'); b.setAttribute('data-manuel', 'croix'); }")
    s.cap_souple("05-document-televerse", [(item, "rapport-annuel-2025.pdf"), (p.locator("[data-manuel=croix]"), "croix (fermer)")])


def citation2(s):
    p = s.page; s.chapitre = "04-premiere-question"
    s.aller("/workspace/premier-essai")
    p.locator("[aria-label=Threads]").get_by_text("Quel est le chiffre", exact=False).first.click()
    p.wait_for_load_state("networkidle"); p.wait_for_timeout(2500)
    p.get_by_role("button", name=re.compile("^Sources")).last.click(); p.wait_for_timeout(1200)
    p.get_by_text("rapport-annuel-2025", exact=False).last.click(); p.wait_for_timeout(1500)
    s.cap_souple("14-extrait-cite", [(p.get_by_text(re.compile(r"Referenced \d+ times")).first, "Referenced 4 times."),
                                     (p.locator("button[aria-label=Close]").last, "fermer")])


def ocr2(s):
    p = s.page; s.chapitre = "15-problemes"
    s.aller("/workspace/demo-velanor")
    p.locator("[aria-label=Threads]").get_by_text("New Thread", exact=True).last.click(); p.wait_for_timeout(2500)
    n = p.get_by_role("button", name=re.compile("^Sources")).count()
    p.locator("#primary-prompt-input").fill("Quelle est la pénalité de retard prévue par le contrat Batterix ?")
    p.locator('button[data-tooltip-id="send-prompt"]').click()
    p.wait_for_function(f"() => [...document.querySelectorAll('button')].filter(b => b.innerText.trim().startsWith('Sources')).length > {n}", timeout=300000)
    p.wait_for_timeout(3000)
    p.get_by_role("button", name=re.compile("^Sources")).last.click(); p.wait_for_timeout(1200)
    p.get_by_text("contrat-batterix-scan.pdf").last.click(); p.wait_for_timeout(1500)
    s.cap_souple("06-texte-ocr", [(p.get_by_text("contrat-batterix-scan.pdf", exact=True).last, "contrat scanné : texte lu par OCR")])


def widget_fichier(s):
    """Chapitre 13 : page HTML ouverte directement depuis un fichier (sans serveur web), widget et réponse."""
    p = s.page; s.chapitre = "13-comptes-et-widget"
    html = open("/depot/outils/anythingllm/essais/site/widget-actif.html").read()
    open("/depot/donnees/widget-fichier.html", "w").write(html)
    p.goto("file:///depot/donnees/widget-fichier.html"); p.wait_for_timeout(3000)
    p.locator("#anything-llm-embed-chat-button").click(); p.wait_for_timeout(1500)
    p.locator("#message-input").fill("Quelle est la durée de garantie du cadre ?"); p.locator("#message-input").press("Enter")
    try:
        p.wait_for_function("() => document.body.innerText.includes('7 ans')", timeout=240000); ok = True
    except Exception:
        ok = False
    p.wait_for_timeout(2500)
    s.note("widget depuis un fichier local : " + ("réponse reçue" if ok else "pas de réponse") + " | " + p.inner_text("body")[-400:].replace("\n", " | "))
    if ok:
        bulle = p.get_by_text("7 ans", exact=False).last.locator("xpath=ancestor::div[2]")
        s.cap_souple("16-widget-reponse", [(bulle, "réponse dans la page")])


def envoi_vierge(s):
    """Chapitre 04, capture 05, dans un espace temporaire vierge nommé comme celui du chapitre (supprimé ensuite)."""
    p = s.page; s.chapitre = "04-premiere-question"
    s.gestionnaire("premier-essai-86397990")
    p.locator("input[type=file]").first.set_input_files("/depot/corpus/documents/rapport-annuel-2025.pdf")
    p.wait_for_timeout(5000); s.sans_toasts()
    item = p.locator('[data-tooltip-id="directory-item"]').filter(has_text="rapport-annuel-2025").first
    if not item.is_visible():
        p.get_by_text("custom-documents").first.click(); p.wait_for_timeout(1000)
    p.evaluate("() => { const b = document.elementFromPoint(1366, 126).closest('button'); b.setAttribute('data-manuel', 'croix'); }")
    s.cap_souple("05-document-televerse", [(item, "rapport-annuel-2025.pdf"), (p.locator("[data-manuel=croix]"), "croix (fermer)")])


def github_form(s):
    p = s.page; s.chapitre = "09-sources-externes"
    s.gestionnaire("sources-externes")
    p.get_by_text("Connecteurs de données").first.click(); p.wait_for_timeout(1000)
    p.get_by_text("Dépôt GitHub", exact=False).first.click(); p.wait_for_timeout(800)
    repo = p.locator("[name=repo]"); repo.fill("https://github.com/octocat/Hello-World")
    sub = repo.locator("xpath=ancestor::form[1]").locator("button[type=submit]")
    s.cap_souple("03-github", [(repo, "URL du dépôt GitHub"), (sub, "Submit")])


def widget_espace(s):
    p = s.page; s.chapitre = "13-comptes-et-widget"
    s.aller("/settings/embed-chat-widgets"); p.wait_for_timeout(1500)
    p.get_by_role("button").filter(has_text="Créer un widget intégré").first.click(); p.wait_for_timeout(1200)
    sel = p.locator("select[name=workspace_id]"); sel.select_option(label="Démo Vélanor")
    s.cap_souple("11b-widget-espace", [(sel, "espace de travail (Démo Vélanor)")])
    p.keyboard.press("Escape")


def suggestion_editeur(s):
    p = s.page; s.chapitre = "14-cas-pratiques"
    s.aller("/workspace/demo-velanor/settings/general-appearance"); p.wait_for_timeout(1500)
    p.get_by_text("Quelle est la durée de garantie", exact=False).first.click(); p.wait_for_timeout(800)
    champ = p.locator("input[name=message]")
    v = champ.input_value(); champ.fill(v + " "); champ.fill(v); p.wait_for_timeout(500)  # fait apparaître le bouton d'enregistrement
    s.note("champs de l'éditeur : " + str([i.get_attribute("name") for i in p.locator("input:visible").all()]))
    s.cap_souple("01b-editer-une-question", [(p.get_by_text("Quelle est la durée de garantie", exact=False).first, "carte de la question"),
                                             (champ, "Message"), (p.get_by_role("button", name="Enregistrer les messages"), "Enregistrer les messages")])


def invitation2(s):
    p = s.page; s.chapitre = "13-comptes-et-widget"
    s.aller("/settings/invites"); p.wait_for_timeout(1500)
    s.bouton("Create Invite Link").first.click(); p.wait_for_timeout(1000)
    p.get_by_role("button", name="Create Invite").last.click(); p.wait_for_timeout(2500)
    s.note("fenêtre invitation : " + p.inner_text("body")[-700:].replace("\n", " | "))
    fen = p.get_by_text("Create new invite").last.locator("xpath=ancestor::*[.//button][1]")
    lien = p.locator("input:visible").last
    copie = lien.locator("xpath=following::button[1]")
    s.cap_souple("07-invitation-creee", [(lien, "lien d invitation (masqué)"), (copie, "copier le lien"), (p.get_by_role("button", name="Close").last, "Close")], masques=[lien])


def swagger2(s):
    p = s.page; s.chapitre = "12-administrer"
    s.aller("/api/docs"); p.wait_for_timeout(3000)
    p.evaluate("() => { window.scrollTo(0, 0); document.querySelectorAll('*').forEach(e => { if (e.scrollTop) e.scrollTop = 0; }); }")
    p.wait_for_timeout(500)
    s.cap_souple("14-documentation-api", [(p.get_by_role("button", name=re.compile("Authorize")).first, "Authorize")])


if __name__ == "__main__":
    s = Scenario("reprises")
    try:
        etapes([invitation2, swagger2, suggestion_editeur, widget_espace, envoi_vierge, github_form, agents, admin, experimental, widget, citation, ocr, envoi, croix_seule, citation2, ocr2, widget_fichier], s)
    finally:
        s.fermer()
