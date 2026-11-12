"""Chapitre 05, Ajouter et organiser ses documents, dans l'espace « Démo Vélanor » (jeu de démonstration) :
création de l'espace, dossier, envoi de plusieurs fichiers, rangement, placement dans l'espace et intégration,
recherche, épinglage, retrait d'un document et suppression d'un fichier (note de test fictive).
Usage : lancer.sh outils/anythingllm/captures/c05_documents.py [espace] [dossier] [envoi] [integrer] [epingler] [retirer]
"""
from pathlib import Path
from ui import Scenario, etapes

CH = "05-documents"
NOM, SLUG = "Démo Vélanor", "demo-velanor"
DOSSIER = "velanor-2025"
CORPUS = sorted(str(f) for f in Path("/depot/corpus/documents").iterdir() if f.is_file())
NOTE = "/depot/outils/anythingllm/essais/note-de-test.txt"


def ouvrir_gestionnaire(s, deplier=None):
    s.page.goto("about:blank")
    s.gestionnaire(SLUG)
    if deplier and not fichier(s, "rapport-annuel-2025").is_visible():
        s.page.get_by_text(deplier, exact=True).first.click(); s.page.wait_for_timeout(1500)


def fichier(s, nom):
    return s.page.locator('[data-tooltip-id="directory-item"]').filter(has_text=nom).first


def espace(s):
    p = s.page
    s.aller("/")
    p.locator('button[data-tooltip-id="new-workspace-tooltip"]').click()
    p.locator("input#name").fill(NOM)
    p.locator("form button[type=submit]").last.click()
    p.wait_for_url(f"**/workspace/{SLUG}**")


def dossier(s):
    p = s.page
    ouvrir_gestionnaire(s)
    nouveau = s.bouton("Nouveau dossier")
    s.cap("01-gestionnaire", [(p.get_by_placeholder("Rechercher un document"), "Rechercher un document"),
                              (nouveau, "Nouveau dossier"),
                              (p.get_by_text("Cliquez pour télécharger ou glissez-déposez"), "zone d'envoi"),
                              (p.get_by_text("Connecteurs de données").first, "Connecteurs de données")])
    nouveau.click()
    champ = p.locator("input[name=folderName]")
    champ.fill(DOSSIER)
    creer = champ.locator("xpath=ancestor::form[1]").locator("button[type=submit]")
    s.cap("02-nouveau-dossier", [(champ, "nom du dossier"), (creer, creer.inner_text().strip())], attendre=champ)
    creer.click(); p.wait_for_timeout(1500)


def envoi(s):
    p = s.page
    ouvrir_gestionnaire(s)
    p.locator("input[type=file]").first.set_input_files(CORPUS + [NOTE])
    p.get_by_text("custom-documents").first.wait_for(timeout=300000)
    p.wait_for_function("n => document.body.innerText.includes(n)", arg="note-de-test", timeout=300000)
    p.wait_for_timeout(2000); s.sans_toasts()
    if not fichier(s, "rapport-annuel-2025").is_visible():
        p.get_by_text("custom-documents").first.click(); p.wait_for_timeout(1000)
    s.cap("03-fichiers-televerses", [(fichier(s, "rapport-annuel-2025"), "fichier téléversé"),
                                     (p.get_by_text("custom-documents").first, "dossier par défaut custom-documents")])
    # AnythingLLM 1.19.0 : fermer puis rouvrir la fenêtre avant de sélectionner les fichiers envoyés
    ouvrir_gestionnaire(s, deplier="custom-documents")
    for f in CORPUS:
        if not f.endswith(".xlsx"):  # le classeur a son propre dossier (une feuille = un document)
            fichier(s, Path(f).stem).click()
    s.sans_toasts()
    s.note("sélection : " + p.inner_text("body")[:900].replace("\n", " | "))
    deplacer_dossier = s.bouton("Déplacer vers l'espace de travail").locator("xpath=following-sibling::div[1]/button")
    deplacer_dossier.click()
    p.wait_for_timeout(600)
    cible = p.get_by_text(DOSSIER, exact=True).last
    s.cap("04-ranger-dans-un-dossier", [(s.bouton("Déplacer vers l'espace de travail"), "Déplacer vers l'espace de travail"),
                                        (deplacer_dossier, "déplacer vers un dossier"), (cible, DOSSIER)])
    cible.click(); p.wait_for_timeout(2500)
    s.note("après rangement : " + p.inner_text("body")[:1500].replace("\n", " | "))


def integrer(s):
    p = s.page
    ouvrir_gestionnaire(s)
    dossier_ligne = p.locator("tr").filter(has_text=DOSSIER).first
    dossier_ligne.locator("[role=checkbox]").first.click()
    classeur = p.locator("tr").filter(has_text="stocks-octobre-2025.xlsx").first
    classeur.locator("[role=checkbox]").first.click()
    deplacer = s.bouton("Déplacer vers l'espace de travail")
    deplacer.wait_for()
    s.sans_toasts()
    s.cap("05-dossier-selectionne", [(dossier_ligne, DOSSIER + " (coché)"), (classeur, "dossier du classeur (coché)"),
                                     (deplacer, "Déplacer vers l'espace de travail")])
    s.sans_toasts()
    deplacer.click()
    integrer = s.bouton("Sauvegarder et intégrer")
    integrer.wait_for()
    s.cap("06-en-attente", [(p.locator('[data-tooltip-id="ws-directory-item"]').first, "documents en attente"), (integrer, "Sauvegarder et intégrer")])
    integrer.click()
    p.wait_for_timeout(1500)
    s.cap("07-integration-en-cours", [(p.locator('[data-tooltip-id="ws-directory-item"]').first, "progression")])
    p.wait_for_function("() => !document.body.innerText.includes('Sauvegarder et intégrer')", timeout=600000)
    p.wait_for_timeout(3000)
    s.note("après intégration : " + p.inner_text("body")[-1500:].replace("\n", " | "))


def epingler(s):
    p = s.page
    ouvrir_gestionnaire(s)
    ligne = p.locator('[data-tooltip-id="ws-directory-item"]').filter(has_text="procedure-batteries").first.locator("xpath=..")
    ligne.hover()
    epingle = ligne.locator('[data-tooltip-id="pin-document"]')
    s.cap("08-epingle", [(ligne, "procedure-batteries.docx"), (epingle, "épingle (Pin to workspace)")])
    epingle.click()
    compris = s.bouton("J'ai compris")
    try:
        compris.wait_for(timeout=5000)
        s.cap("09-explication-epinglage", [(compris, "J'ai compris")])
        compris.click()
    except Exception as e:
        s.note("pas de fenêtre d'explication : " + str(e)[:120])
    p.wait_for_timeout(1500)
    s.cap("10-document-epingle", [(ligne, "document épinglé")])


def retirer(s):
    p = s.page
    ouvrir_gestionnaire(s)
    # la note de test est placée dans l'espace, puis retirée, puis supprimée
    if not fichier(s, "note-de-test").is_visible():
        p.get_by_text("custom-documents", exact=True).first.click(); p.wait_for_timeout(1200)
    fichier(s, "note-de-test").click(); s.sans_toasts()
    s.bouton("Déplacer vers l'espace de travail").click()
    s.bouton("Sauvegarder et intégrer").click()
    p.wait_for_function("() => !document.body.innerText.includes('Sauvegarder et intégrer')", timeout=300000)
    p.wait_for_timeout(1500)
    ligne = p.locator('[data-tooltip-id="ws-directory-item"]').filter(has_text="note-de-test").first.locator("xpath=..")
    ligne.hover()
    retrait = ligne.locator('[data-tooltip-id="remove-document"]')
    s.cap("11-retirer-de-l-espace", [(ligne, "note-de-test.txt"), (retrait, "retirer de l'espace (Remove document from workspace)")])
    retrait.click(); p.wait_for_timeout(2500)
    p.once("dialog", lambda d: d.accept())
    ouvrir_gestionnaire(s)
    if not fichier(s, "note-de-test").is_visible():
        p.get_by_text("custom-documents", exact=True).first.click(); p.wait_for_timeout(1200)
    f = fichier(s, "note-de-test")
    f.click(); s.sans_toasts()
    corbeille = s.bouton("Déplacer vers l'espace de travail").locator("xpath=following-sibling::button[1]")
    s.cap("12-supprimer-le-fichier", [(f, "note-de-test.txt (coché)"), (corbeille, "corbeille (supprimer)")])
    corbeille.click(); p.wait_for_timeout(3000)
    recherche = p.get_by_placeholder("Rechercher un document")
    recherche.fill("stocks")
    p.wait_for_timeout(1000)
    s.cap("13-rechercher", [(recherche, "Rechercher un document")])
    s.note("après suppression : " + p.inner_text("body")[:1200].replace("\n", " | "))


if __name__ == "__main__":
    s = Scenario(CH)
    try:
        etapes([espace, dossier, envoi, integrer, epingler, retirer], s)
    finally:
        s.fermer()
