"""Chapitre 08, Choisir les modèles et la lecture des documents : pages Préférence LLM, base vectorielle, découpage,
génération d'images, voix et parole, confidentialité ; choix d'un autre modèle pour un espace (gemma-4-e4b, montré
puis remis par défaut). Usage : lancer.sh outils/anythingllm/captures/c08_modeles.py [llm] [vecteurs] [decoupage] [images] [voix] [confidentialite] [modele_espace]
"""
from ui import Scenario, etapes

CH = "08-modeles-et-lecture"


def llm(s):
    p = s.page
    s.aller("/settings/llm-preference"); p.wait_for_timeout(1500)
    s.cap("01-preference-llm", [(p.locator("form button[type=button]").first, "fournisseur actuel (Generic OpenAI)"),
                                (p.locator("[name=GenericOpenAiModelPref]"), "Selected Model"),
                                (p.locator("[name=GenericOpenAiTokenLimit]"), "Model context window"),
                                (p.locator("[name=GenericOpenAiMaxTokens]"), "Max Tokens")])


def vecteurs(s):
    p = s.page
    s.aller("/settings/vector-database"); p.wait_for_timeout(1500)
    s.cap("02-base-vectorielle", [(p.locator("form button[type=button]").first, "LanceDB (base intégrée)")])


def decoupage(s):
    p = s.page
    s.aller("/settings/text-splitter-preference"); p.wait_for_timeout(1500)
    s.cap("03-decoupage", [(p.locator("[name=text_splitter_chunk_size]"), "Taille des segments de texte"),
                           (p.locator("[name=text_splitter_chunk_overlap]"), "Chevauchement des segments de texte")])
    s.note("découpage : " + p.inner_text("body")[-900:].replace("\n", " | "))


def images(s):
    p = s.page
    s.aller("/settings/image-generation-preference"); p.wait_for_timeout(1500)
    s.cap("04-generation-d-images", [(p.locator("form button[type=button]").first, "fournisseur de génération d'images")])
    s.note("images : " + p.inner_text("body")[-700:].replace("\n", " | "))


def voix(s):
    p = s.page
    s.aller("/settings/audio-preference"); p.wait_for_timeout(1500)
    boutons = p.locator("form button[type=button]")
    s.cap("05-voix-et-parole", [(boutons.nth(0), "Speech-to-text (dictée)"), (boutons.nth(1), "Text-to-speech (lecture)")],
          plein=True)
    s.note("voix : " + p.inner_text("body")[-1200:].replace("\n", " | "))


def confidentialite(s):
    p = s.page
    s.aller("/settings/privacy"); p.wait_for_timeout(1500)
    s.cap("06-confidentialite", [(p.get_by_text("Confidentialité et données").last, "Confidentialité et données")], plein=True)
    s.note("confidentialité : " + p.inner_text("body")[-1500:].replace("\n", " | "))


def modele_espace(s):
    p = s.page
    s.aller("/workspace/demo-velanor"); p.wait_for_timeout(1500)
    selecteur = p.get_by_text("chat", exact=True).first
    s.cap("07-modele-de-l-espace", [(selecteur, "modèle utilisé (Sélectionner le modèle)")])
    selecteur.click(); p.wait_for_timeout(1000)
    s.cap("08-choix-du-modele", [(p.locator("#llm-search-input"), "Rechercher des modèles")])
    s.note("sélecteur : " + p.inner_text("body")[-1200:].replace("\n", " | "))
    p.keyboard.press("Escape")


if __name__ == "__main__":
    s = Scenario(CH)
    try:
        etapes([llm, vecteurs, decoupage, images, voix, confidentialite, modele_espace], s)
    finally:
        s.fermer()
