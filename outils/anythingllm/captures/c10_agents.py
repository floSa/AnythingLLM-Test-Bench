"""Chapitre 10, Agents et outils : compétences, agent flows, serveurs MCP (velanor-outils, outils/anythingllm/mcp/),
puis agent à l'œuvre dans « Démo Vélanor » (appel du modèle : à lancer hors banc).
Usage : lancer.sh outils/anythingllm/captures/c10_agents.py [competences] [flows] [mcp] [agent]
"""
from ui import Scenario, etapes

CH = "10-agents"


def competences(s):
    p = s.page
    s.aller("/settings/agents"); p.wait_for_timeout(2000)
    s.cap_souple("01-competences", [(p.get_by_text("RAG et mémoire à long terme", exact=False).first, "RAG et mémoire à long terme"),
                                    (p.get_by_text("Recherche web en direct", exact=False).first, "Recherche web en direct et navigation"),
                                    (p.get_by_text("Générer des graphiques", exact=False).first, "Générer des graphiques"),
                                    (p.get_by_text("Agent Flows", exact=False).first, "Agent Flows"),
                                    (p.get_by_text("Serveurs MCP", exact=False).first, "Serveurs MCP")])
    s.note("compétences : " + p.inner_text("body")[:3000].replace("\n", " | "))
    graph = p.get_by_text("Générer des graphiques", exact=False).first
    graph.click(); p.wait_for_timeout(1200)
    inter = p.locator("label:has(input[type=checkbox])").last
    inter.click(); p.wait_for_timeout(800)
    s.cap_souple("02-competence-detail", [(p.get_by_text("Générer des graphiques", exact=False).last, "compétence choisie"),
                                          (inter, "interrupteur (activée)"), (s.bouton("Save").last, "Save")])
    s.bouton("Save").last.click(); p.wait_for_timeout(1500)
    s.note("détail graphique : " + p.inner_text("body")[-1500:].replace("\n", " | "))


def flows(s):
    p = s.page
    s.aller("/settings/agents"); p.wait_for_timeout(1500)
    creer = p.get_by_text("Create Flow", exact=True).first
    s.cap_souple("03-agent-flows", [(creer, "Create Flow")])
    creer.click(); p.wait_for_load_state("networkidle"); p.wait_for_timeout(2500)
    nom = p.locator("input").filter(has=p.locator("xpath=.")).nth(0)
    champs = p.locator("input:visible, textarea:visible")
    for c in champs.all():
        s.note(f"champ flow : {c.evaluate('e => e.tagName')} name={c.get_attribute('name')} ph={c.get_attribute('placeholder')}")
    nom = p.get_by_placeholder('"SendMessageToDiscord"', exact=False).first.or_(champs.nth(0))
    nom.fill("ConsignesBatteries")
    desc = p.locator("textarea:visible").first
    desc.fill("Rappelle les consignes de sécurité pour manipuler une batterie de vélo Vélanor, à partir de la procédure interne.")
    p.get_by_text("Add Block", exact=True).first.click(); p.wait_for_timeout(1000)
    s.note("blocs : " + p.inner_text("body")[-1200:].replace("\n", " | "))
    s.cap_souple("04-editeur-de-flow", [(nom, "Flow Name"), (desc, "Description"),
                                        (p.get_by_text("Add Block", exact=True).first, "Add Block"),
                                        (s.bouton("Save").first, "Save")])
    p.keyboard.press("Escape")
    s.bouton("Save").first.click(); p.wait_for_timeout(2000)
    s.note("après enregistrement : " + p.url + " " + p.inner_text("body")[:600].replace("\n", " | "))
    s.note("éditeur : " + p.url + " " + p.inner_text("body")[:2500].replace("\n", " | "))


def mcp(s):
    p = s.page
    s.aller("/settings/agents"); p.wait_for_timeout(1500)
    vo = p.get_by_text("Velanor Outils", exact=True).first
    vo.click(); p.wait_for_timeout(2000)
    s.cap_souple("05-serveur-mcp", [(p.get_by_text("Rafraîchir", exact=True).first, "Rafraîchir"), (vo, "Velanor Outils"),
                                    (p.get_by_text("1/1 outils activés", exact=False).first, "1/1 outils activés"),
                                    (p.get_by_text("stock_piece", exact=True).first, "outil stock_piece")])
    s.note("mcp : " + p.inner_text("body")[-2500:].replace("\n", " | "))


def agent(s):
    p = s.page
    s.aller("/workspace/demo-velanor")
    p.locator("[aria-label=Threads]").get_by_text("New Thread", exact=True).last.click(); p.wait_for_timeout(2500)
    champ = p.locator("#primary-prompt-input")
    champ.fill("@agent Quel est le stock de la pièce BAT-500 ?")
    s.cap_souple("07-question-agent", [(champ, "@agent + question"), (p.locator('button[data-tooltip-id="agent-session"]'), "@ (démarrer l'agent)")])
    p.locator('button[data-tooltip-id="send-prompt"]').click()
    p.wait_for_timeout(5000)
    try:
        p.wait_for_function("() => document.body.innerText.includes('184')", timeout=300000)
    except Exception as e:
        s.note("pas de 184 : " + str(e)[:80])
    p.wait_for_timeout(4000)
    s.cap_souple("08-reponse-agent", [(p.get_by_text("stock_piece", exact=False).first, "appel de l'outil MCP"),
                                      (p.get_by_text("184", exact=False).last, "réponse")])
    s.note("agent : " + p.inner_text("body")[-2500:].replace("\n", " | "))


if __name__ == "__main__":
    s = Scenario(CH)
    try:
        etapes([competences, flows, mcp, agent], s)
    finally:
        s.fermer()
