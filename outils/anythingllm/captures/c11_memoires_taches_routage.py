"""Chapitre 11, Mémoires, tâches planifiées et routage de modèles (mode « Juste moi » : les tâches planifiées
disparaissent en multi-utilisateur). Usage : lancer.sh ... c11_memoires_taches_routage.py [memoires] [taches] [routeur]
"""
from ui import Scenario, etapes

CH = "11-memoires-taches-routage"


def memoires(s):
    p = s.page
    s.aller("/workspace/demo-velanor"); p.wait_for_timeout(1500)
    p.locator("div.absolute.z-30 > button[type=button]").first.click(); p.wait_for_timeout(600)
    p.get_by_text("Souvenirs", exact=True).first.click(); p.wait_for_timeout(1500)
    s.cap_souple("01-souvenirs", [(p.get_by_text("Activer la personnalisation", exact=False).first, "Activer la personnalisation"),
                                  (p.get_by_text("Souvenirs automatisés", exact=False).first, "Souvenirs automatisés"),
                                  (p.get_by_text("Espace de travail", exact=True).first, "Espace de travail"),
                                  (p.get_by_text("Global", exact=True).first, "Global")])
    s.note("souvenirs : " + p.inner_text("body")[-1500:].replace("\n", " | "))
    sw = p.locator("[role=switch]")
    if sw.count():
        sw.first.click(); p.wait_for_timeout(1200)
    lien = p.get_by_text("créer un nouveau souvenir", exact=False).first
    try:
        lien.click(timeout=5000); p.wait_for_timeout(800)
        zone = p.locator("textarea").last
        zone.fill("Les réponses doivent toujours citer le nom du document source.")
        s.cap_souple("02-creer-un-souvenir", [(zone, "Mémoire"), (s.bouton("Créer").last, "Créer")])
        s.bouton("Créer").last.click(); p.wait_for_timeout(1500)
        s.cap_souple("03-souvenir-cree", [(p.get_by_text("citer le nom du document", exact=False).first, "souvenir enregistré")])
    except Exception as e:
        s.note("création souvenir : " + str(e)[:150])
    s.note("après souvenir : " + p.inner_text("body")[-1500:].replace("\n", " | "))
    # personnalisation recoupée ensuite : l'extraction automatique appellerait le modèle après chaque conversation (bancs)
    if sw.count():
        sw.first.click(); p.wait_for_timeout(1000)


def taches(s):
    p = s.page
    s.aller("/settings/scheduled-jobs"); p.wait_for_timeout(2000)
    s.note("tâches : " + p.inner_text("body")[:2000].replace("\n", " | "))
    nouveau = p.get_by_role("button").filter(has_text="Nouvel").or_(p.get_by_role("button").filter(has_text="New")).or_(
        p.get_by_role("button").filter(has_text="Créer")).first
    s.cap_souple("04-taches-planifiees", [(nouveau, nouveau.inner_text() if nouveau.count() else "nouvelle tâche")])
    nouveau.click(); p.wait_for_timeout(1500)
    s.note("formulaire tâche : " + p.inner_text("body")[-2500:].replace("\n", " | "))
    for loc in p.locator("input:visible, textarea:visible, select:visible").all():
        s.note(f"champ : {loc.evaluate('e => e.tagName')} name={loc.get_attribute('name')} ph={loc.get_attribute('placeholder')}")
    p.locator("input[name=name]").fill("Point stocks du lundi")
    p.locator("textarea[name=prompt]").fill("Résume l'état des stocks de pièces à partir des documents de l'espace Démo Vélanor.")
    sel = p.locator("select:visible").first
    s.note("options calendrier : " + str(sel.locator("option").all_inner_texts()))
    creer = p.get_by_role("button").filter(has_text="Créer").last
    s.cap_souple("05-nouvelle-tache", [(p.locator("input[name=name]"), "nom"), (p.locator("textarea[name=prompt]"), "instruction"),
                                       (sel, "calendrier"), (creer, creer.inner_text() if creer.count() else "Créer")])
    creer.click(); p.wait_for_timeout(2500)
    s.cap_souple("05b-tache-creee", [(p.get_by_text("Point stocks du lundi", exact=False).first, "tâche créée")])
    s.note("après création tâche : " + p.inner_text("body")[-1500:].replace("\n", " | "))


def routeur(s):
    p = s.page
    s.aller("/settings/model-routers"); p.wait_for_timeout(2000)
    nouveau = s.bouton("Nouveau routeur").first
    s.cap_souple("06-routeurs", [(nouveau, "Nouveau routeur")])
    nouveau.click(); p.wait_for_timeout(1500)
    s.note("formulaire routeur : " + p.inner_text("body")[-2500:].replace("\n", " | "))
    for loc in p.locator("input:visible, textarea:visible, select:visible").all():
        s.note(f"champ : {loc.evaluate('e => e.tagName')} name={loc.get_attribute('name')} ph={loc.get_attribute('placeholder')}")
    p.locator("input[name=name]").fill("Routeur Vélanor")
    p.locator("input[name=description]").fill("chat par défaut ; gemma-4-e4b pour les questions courtes")
    p.locator("select[name=fallback_provider]").select_option("generic-openai"); p.wait_for_timeout(1500)
    p.locator("[name=fallback_model]").fill("chat")
    creer = p.get_by_role("button").filter(has_text="Créer").last
    s.cap_souple("07-nouveau-routeur", [(p.locator("input[name=name]"), "Nom"), (p.locator("select[name=fallback_provider]"), "Prestataire principal"),
                                        (p.locator("[name=fallback_model]"), "modèle"), (creer, "Créer")])
    creer.click(); p.wait_for_timeout(2500)
    s.note("après routeur : " + p.url + " " + p.inner_text("body")[-1500:].replace("\n", " | "))
    s.cap_souple("08-routeur-regles", [(p.get_by_text("Routeur Vélanor", exact=False).first, "Routeur Vélanor")])
    for loc in p.locator("button:visible").all()[:60]:
        t = (loc.inner_text() or "").strip()
        if t: s.note("bouton routeur : " + t[:60])


if __name__ == "__main__":
    s = Scenario(CH)
    try:
        etapes([memoires, taches, routeur], s)
    finally:
        s.fermer()
