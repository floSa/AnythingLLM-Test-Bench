"""Chapitre 07, Régler un espace de travail : onglets des réglages de « Démo Vélanor » (sans rien changer d'autre que
le texte de refus, mis en français, et la préférence de recherche, montrée puis remise à « Default »).
Usage : lancer.sh outils/anythingllm/captures/c07_reglages_espace.py [general] [chat] [vecteurs] [agent]
"""
from ui import Scenario, etapes

CH = "07-reglages-espace"
SLUG = "demo-velanor"
REFUS = "Aucune information pertinente dans les documents de cet espace pour répondre à cette question."


def general(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}")
    ligne = p.locator(f'a[href="/workspace/{SLUG}"]').locator('xpath=ancestor::*[@role="listitem"][1]')
    ligne.hover()
    roue = ligne.locator('button[aria-label="General appearance settings"]')
    s.cap("01-roue-dentee", [(roue, "roue dentée de l'espace")])
    roue.click(); p.wait_for_load_state("networkidle"); p.wait_for_timeout(1200)
    s.cap("02-parametres-generaux", [(p.get_by_text("Paramètres généraux").first, "Paramètres généraux"),
                                     (p.locator("input[name=name]"), "Nom des espaces de travail"),
                                     (p.get_by_text("Messages de chat suggérés").first, "Messages de chat suggérés"),
                                     (s.bouton("Supprimer l'espace de travail"), "Supprimer l'espace de travail")])


def chat(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}/settings/chat-settings")
    p.wait_for_timeout(1000)
    s.cap("03-parametres-du-chat-haut", [(p.locator("[name=chatProvider]").locator("xpath=..").first, "fournisseur LLM de l'espace"),
                                         (p.get_by_text("Mode de chat").first, "Mode de chat"),
                                         (p.locator("[name=openAiHistory]"), "Historique des chats")], plein=False)
    refus = p.locator("[name=queryRefusalResponse]")
    refus.scroll_into_view_if_needed()
    refus.fill(REFUS); refus.blur(); p.wait_for_timeout(1500)
    s.cap("04-parametres-du-chat-bas", [(p.locator("[name=openAiPrompt]"), "Invite système"),
                                        (refus, "Réponse de refus en mode requête"),
                                        (p.locator("[name=openAiTemp]"), "Température LLM")])


def vecteurs(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}/settings/vector-database")
    p.wait_for_timeout(1000)
    mode = p.locator("select[name=vectorSearchMode]")
    s.cap("05-base-vectorielle", [(p.get_by_text("Nombre de vecteurs").first, "Nombre de vecteurs"), (mode, "préférence de recherche"),
                                  (p.locator("[name=topN]"), "Nombre maximum de contextes"),
                                  (p.locator("[name=similarityThreshold]"), "Seuil de similarité des documents"),
                                  (s.bouton("Réinitialiser la base de données vectorielle"), "Réinitialiser la base de données vectorielle")])
    s.note("options recherche : " + str(mode.locator("option").all_inner_texts()) + " seuil : " +
           str(p.locator("[name=similarityThreshold] option").all_inner_texts()))


def agent(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}/settings/agent-config")
    p.wait_for_timeout(1200)
    s.cap("06-configuration-agent", [(p.get_by_text("Fournisseur LLM de l'agent", exact=False).first, "fournisseur de l'agent"),
                                     (p.get_by_text("Configure Agent Skills", exact=False).first, "Configure Agent Skills")])


if __name__ == "__main__":
    s = Scenario(CH)
    try:
        etapes([general, chat, vecteurs, agent], s)
    finally:
        s.fermer()
