"""Chapitre 12, Personnaliser et administrer : apparence, nom, chat, espaces, historique des conversations, consigne
par défaut, journaux, clés d'API, variables, extension, mobile, Telegram, fonctions expérimentales, Swagger.
Usage : lancer.sh outils/anythingllm/captures/c12_administrer.py [pages...]
"""
import sys
from ui import Scenario, etapes

CH = "12-administrer"
PAGES = [
    ("01-interface", "/settings/interface", ["Thème", "Palette de couleurs", "Langue d'affichage"]),
    ("02-personnalisation", "/settings/branding", ["Identité", "Couleurs", "Barre latérale", "Navigateur"]),
    ("03-apparence-du-chat", "/settings/chat", ["Soumission automatique", "Rendu HTML"]),
    ("04-espaces-de-travail", "/settings/workspaces", ["New Workspace", "Démo Vélanor"]),
    ("05-historique-des-conversations", "/settings/workspace-chats", ["Exporter", "Clear Chats"]),
    ("06-consigne-par-defaut", "/settings/default-system-prompt", ["System Prompt", "Save Changes"]),
    ("07-journaux", "/settings/event-logs", ["Effacer les journaux d'événements"]),
    ("08-cles-api", "/settings/api-keys", ["Générer une nouvelle clé API", "Lire la documentation de l'API"]),
    ("09-variables", "/settings/system-prompt-variables", ["Add Variable", "{date}"]),
    ("10-extension", "/settings/browser-extension", ["Generate New API Key"]),
    ("11-mobile", "/settings/mobile-connections", ["Connected Mobile Devices"]),
    ("12-telegram", "/settings/external-connections/telegram", ["Telegram"]),
]


def pages(s):
    p = s.page
    for nom, chemin, textes in PAGES:
        s.aller(chemin); p.wait_for_timeout(1500)
        s.cap_souple(nom, [(p.get_by_text(t, exact=False).first, t) for t in textes])


def experimental(s):
    p = s.page
    s.aller("/settings/interface"); p.wait_for_timeout(1000)
    p.evaluate("localStorage.setItem('anythingllm_experimental_feature_preview_unlocked','enabled')")
    s.aller("/settings/beta-features"); p.wait_for_timeout(2000)
    s.cap_souple("13-experimental", [(p.get_by_text("Live Document Sync", exact=False).first, "Live Document Sync")])
    s.note("expérimental : " + p.inner_text("body")[-1500:].replace("\n", " | "))


def swagger(s):
    p = s.page
    s.aller("/api/docs"); p.wait_for_timeout(3000)
    s.cap_souple("14-documentation-api", [(p.get_by_text("Authorize", exact=False).first, "Authorize"),
                                          (p.get_by_text("Workspaces", exact=True).first, "Workspaces")])


def creer_cle(s):
    p = s.page
    s.aller("/settings/api-keys"); p.wait_for_timeout(1500)
    s.bouton("Générer une nouvelle clé API").first.click(); p.wait_for_timeout(1000)
    s.note("fenêtre clé : " + p.inner_text("body")[-800:].replace("\n", " | "))
    creer = p.get_by_role("button").filter(has_text="Créer").last
    s.cap_souple("15-creer-une-cle", [(creer, "Créer la clé API")])
    creer.click(); p.wait_for_timeout(2000)
    champ = p.get_by_text("Créer une nouvelle clé API").last.locator("xpath=ancestor::*[.//input][1]").locator("input").first
    s.cap_souple("16-cle-creee", [(champ, "nouvelle clé (masquée)"), (p.get_by_role("button", name="Fermer").last, "Fermer")],
                 masques=[champ])
    p.get_by_role("button", name="Fermer").last.click(); p.wait_for_timeout(1000)
    s.note("après création : " + p.inner_text("body")[-800:].replace("\n", " | "))


if __name__ == "__main__":
    s = Scenario(CH)
    try:
        etapes([pages, experimental, swagger, creer_cle], s)
    finally:
        s.fermer()
