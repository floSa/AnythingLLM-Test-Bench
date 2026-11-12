"""Chapitre 03, Premiers pas : assistant de premier lancement, écran principal, connexion, langue, transcription,
puis (étape « embedder », lancée après le banc de l'embedder natif) déclaration de l'embedder du service central.
Usage : lancer.sh outils/anythingllm/captures/c03_premiers_pas.py [accueil] [ecran] [connexion] [langue] [transcription] [embedder]
"""
import os
from ui import Scenario, etapes, identifiants

CH = "03-premiers-pas"
URL_CENTRAL = "http://llm-central:8080/v1"


def choisir(p, sel, valeur):
    """Champ libre ou liste (la liste apparaît quand le service répond à /models) : choisit la valeur."""
    loc = p.locator(sel)
    p.wait_for_timeout(1500)
    if loc.evaluate("e => e.tagName") == "SELECT":
        p.locator(sel + ":not([disabled])").wait_for(timeout=20000)
        loc.select_option(valeur)
    else:
        loc.fill(valeur)


def accueil(s):
    p = s.page
    s.page.close(); s.page = s.contexte.new_page(); p = s.page
    s.aller("/onboarding")
    s.cap("01-bienvenue", [(s.bouton("Commencer"), "Commencer")])
    s.bouton("Commencer").click(); p.wait_for_load_state("networkidle")
    recherche = p.get_by_placeholder("Search LLM providers")
    recherche.fill("Generic")
    carte = p.get_by_text("Generic OpenAI", exact=True)
    s.cap("02-preference-llm-recherche", [(recherche, "Search LLM providers"), (carte, "Generic OpenAI")])
    carte.click()
    p.fill("[name=GenericOpenAiBasePath]", URL_CENTRAL)
    p.fill("[name=GenericOpenAiKey]", os.environ["LLM_CENTRAL_KEY"])
    choisir(p, "[name=GenericOpenAiModelPref]", "chat")
    p.fill("[name=GenericOpenAiTokenLimit]", "16384")
    p.fill("[name=GenericOpenAiMaxTokens]", "8192")
    s.cap("03-preference-llm-champs", [(p.locator("[name=GenericOpenAiBasePath]"), "Base URL"),
                                       (p.locator("[name=GenericOpenAiKey]"), "API Key"),
                                       (p.locator("[name=GenericOpenAiModelPref]"), "Selected Model"),
                                       (p.locator("[name=GenericOpenAiTokenLimit]"), "Model context window"),
                                       (p.locator("[name=GenericOpenAiMaxTokens]"), "Max Tokens"),
                                       (p.locator("button[aria-label=Continue]"), "flèche Continuer")])
    p.locator("button[aria-label=Continue]").click(); p.wait_for_load_state("networkidle")
    juste_moi = s.texte("Juste moi", exact=True)
    s.cap("04-configuration-utilisateur", [(juste_moi, "Juste moi"), (s.texte("Mon équipe", exact=True), "Mon équipe")],
          attendre=juste_moi)
    juste_moi.click()
    oui = s.bouton("Oui", exact=True)
    oui.click()
    mdp = p.locator("input[name=password]")
    mdp.fill(identifiants()["anythingllm.instance.mot_de_passe"])
    s.cap("05-mot-de-passe-instance", [(oui, "Oui"), (mdp, "Mot de passe de l'instance"),
                                       (p.locator("button[aria-label=Continue]"), "flèche Continuer")])
    p.locator("button[aria-label=Continue]").click(); p.wait_for_load_state("networkidle")
    p.wait_for_timeout(1500)
    s.cap("06-gestion-des-donnees", [(p.locator("button[aria-label=Continue]"), "flèche Continuer")])
    p.locator("button[aria-label=Continue]").click(); p.wait_for_load_state("networkidle")
    ignorer = s.bouton("Ignorer l'enquête")
    s.cap("07-enquete", [(ignorer, "Ignorer l'enquête")], attendre=ignorer)
    ignorer.click(); p.wait_for_load_state("networkidle"); p.wait_for_timeout(2000)
    s.note("fin de l'assistant : " + p.url)


def ecran(s):
    p = s.page
    s.aller("/")
    p.wait_for_timeout(1500)
    s.cap("08-ecran-principal", [
        (p.locator("[aria-label=Workspaces]"), "liste des espaces de travail"),
        (p.locator('button[data-tooltip-id="new-workspace-tooltip"]'), "+ (Nouvel Espace de Travail)"),
        (p.locator('button[data-tooltip-id="upload-workspace"]').first, "envoi de documents (flèche)"),
        (p.locator("#primary-prompt-input"), "Envoyer un message"),
        (p.locator("#tools-btn"), "Outils"),
        (p.locator('a[aria-label="Settings"]'), "Paramètres (clé)"),
    ])


def connexion(s):
    # nouveau navigateur sans session : écran de connexion
    ctx = s.navigateur.new_context(viewport={"width": 1440, "height": 900}, locale="fr-FR")
    ctx.add_init_script("localStorage.setItem('i18nextLng','fr')")
    vieux = s.page
    s.page = ctx.new_page()
    s.aller("/")
    mdp = s.page.locator("input[name=password]")
    mdp.fill(identifiants()["anythingllm.instance.mot_de_passe"])
    s.cap("09-connexion", [(mdp, "Mot de passe"), (s.page.locator("form button[type=submit]"), "Connexion")], attendre=mdp)
    s.page.locator("form button[type=submit]").click(); s.page.wait_for_load_state("networkidle")
    ctx.close(); s.page = vieux


def langue(s):
    p = s.page
    s.aller("/settings/interface")
    sel = p.locator("select[name=userLang]")
    s.cap("10-langue", [(p.get_by_text("Paramètres de l'instance").first, "Paramètres de l'instance (menu)"),
                        (sel, "Langue d'affichage")], attendre=sel)
    s.note("langue proposée : " + sel.input_value())


def transcription(s):
    p = s.page
    s.aller("/settings/transcription-preference")
    p.wait_for_timeout(1000)
    s.cap("11-transcription-defaut", [(p.locator("form button[type=button]").first, "fournisseur actuel")])
    p.locator("form button[type=button]").first.click()
    p.get_by_text("OpenAI Compatible", exact=True).click()
    p.wait_for_timeout(500)
    champs = p.locator("form input:visible")
    s.note("champs transcription : " + str([c.get_attribute("name") for c in champs.all()]))
    for c in champs.all():
        n = c.get_attribute("name") or ""
        if "BaseUrl" in n or "BasePath" in n:
            c.fill(URL_CENTRAL)
        elif "Key" in n:
            c.fill(os.environ["LLM_CENTRAL_KEY"])
        elif "Model" in n:
            c.fill("transcribe")
    enr = p.get_by_role("button", name="Enregistrer les modifications").or_(p.get_by_role("button", name="Save changes"))
    elements = [(c, c.get_attribute("name")) for c in champs.all()] + [(enr.first, "Enregistrer les modifications")]
    s.cap("12-transcription-compatible", elements)
    enr.first.click(); p.wait_for_timeout(1500)
    s.note("après enregistrement transcription : " + p.inner_text("body")[:300].replace("\n", " | "))


def embedder_natif(s):
    """Remet l'embedder intégré (sans capture) pour rejouer l'étape « embedder »."""
    p = s.page
    s.aller("/settings/embedding-preference"); p.wait_for_timeout(1000)
    p.locator("form button[type=button]").first.click()
    p.get_by_placeholder("Search all embedding providers").fill("AnythingLLM")
    p.get_by_text("AnythingLLM Embedder", exact=True).click(); p.wait_for_timeout(500)
    p.get_by_role("button", name="Enregistrer les modifications").or_(p.get_by_role("button", name="Save changes")).first.click()
    try:
        p.get_by_role("button", name="Confirm").click(timeout=5000)
    except Exception:
        pass  # pas de confirmation quand on revient à l embedder intégré
    p.wait_for_timeout(2000)


def embedder(s):
    p = s.page
    s.aller("/settings/embedding-preference")
    p.wait_for_timeout(1000)
    s.cap("13-embedder-defaut", [(p.locator("form button[type=button]").first, "fournisseur actuel")])
    p.locator("form button[type=button]").first.click()
    p.get_by_placeholder("Search all embedding providers").fill("Generic")
    p.get_by_text("Generic OpenAI", exact=True).click()
    p.wait_for_timeout(500)
    p.fill("[name=EmbeddingBasePath]", URL_CENTRAL)
    choisir(p, "[name=EmbeddingModelPref]", "embed")
    p.fill("[name=EmbeddingModelMaxChunkLength]", "1000")
    p.fill("[name=GenericOpenAiEmbeddingApiKey]", os.environ["LLM_CENTRAL_KEY"])
    enr = p.get_by_role("button", name="Enregistrer les modifications").or_(p.get_by_role("button", name="Save changes"))
    s.cap("14-embedder-generic", [(p.locator("[name=EmbeddingBasePath]"), "Base URL"),
                                  (p.locator("[name=EmbeddingModelPref]"), "Embedding Model"),
                                  (p.locator("[name=EmbeddingModelMaxChunkLength]"), "Max embedding chunk length"),
                                  (p.locator("[name=GenericOpenAiEmbeddingApiKey]"), "API Key"),
                                  (enr.first, "Enregistrer les modifications")])
    enr.first.click(); p.wait_for_timeout(1500)
    dialogue = p.locator("dialog, [role=dialog], .fixed").filter(has_text="Confirm").or_(
        p.locator("[role=dialog]"))
    s.note("après clic enregistrer embedder : " + p.inner_text("body")[-800:].replace("\n", " | "))
    confirmer = p.get_by_role("button", name="Confirmer").or_(p.get_by_role("button", name="Confirm"))
    try:
        confirmer.first.wait_for(state="visible", timeout=5000)
        s.cap("15-embedder-confirmation", [(confirmer.first, confirmer.first.inner_text())], auto=False)  # clé sous le voile, illisible
        confirmer.first.click(); p.wait_for_timeout(2000)
    except Exception as e:
        s.note("pas de fenêtre de confirmation : " + str(e)[:200])
    s.note("après confirmation : " + p.inner_text("body")[-500:].replace("\n", " | "))


if __name__ == "__main__":
    import sys
    s = Scenario(CH, connecter="accueil" not in sys.argv[1:] and bool(sys.argv[1:]))
    try:
        etapes([accueil, ecran, connexion, langue, transcription, embedder_natif, embedder], s)
    finally:
        s.fermer()
