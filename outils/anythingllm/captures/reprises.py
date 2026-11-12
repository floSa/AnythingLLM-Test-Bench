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


if __name__ == "__main__":
    s = Scenario("reprises")
    try:
        etapes([agents, admin, experimental, widget, citation, ocr], s)
    finally:
        s.fermer()
