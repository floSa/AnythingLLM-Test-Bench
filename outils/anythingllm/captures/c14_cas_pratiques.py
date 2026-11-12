"""Chapitre 14, Cas pratiques, dans « Démo Vélanor » (jeu de démonstration) : trois conversations citées, créées par
l'interface. Usage : lancer.sh ... c14_cas_pratiques.py [faq] [fournisseur] [production]
"""
import re
from ui import Scenario, etapes

CH = "14-cas-pratiques"
SLUG = "demo-velanor"


def demander(s, fil, question, attendu):
    """Nouveau fil renommé, question, attente de la réponse (bouton Sources), sources ouvertes."""
    p = s.page
    s.aller(f"/workspace/{SLUG}")
    p.locator("[aria-label=Threads]").get_by_text("New Thread", exact=True).last.click(); p.wait_for_timeout(2500)
    n = p.get_by_role("button", name="Sources").count()
    p.locator("#primary-prompt-input").fill(question)
    p.locator('button[data-tooltip-id="send-prompt"]').click()
    p.wait_for_function(f"() => [...document.querySelectorAll('button')].filter(b => b.innerText.trim().startsWith('Sources')).length > {n}", timeout=300000)
    p.wait_for_timeout(3000)
    p.get_by_role("button", name="Sources").last.click(); p.wait_for_timeout(1500)
    lien = p.locator("[aria-label=Threads] a").filter(has_text=question[:12]).first
    try:
        lien.hover(); lien.locator("xpath=..").locator("button[aria-label='Thread options']").first.click(); p.wait_for_timeout(500)
        p.once("dialog", lambda d: d.accept(fil))
        p.get_by_text("Rename", exact=True).click(); p.wait_for_timeout(1500)
    except Exception as e:
        s.note("renommage : " + str(e)[:120])
    s.note(f"{fil} : " + p.inner_text("body")[-1500:].replace("\n", " | "))
    return p.get_by_text(re.compile(attendu)).last


def faq(s):
    p = s.page
    s.aller(f"/workspace/{SLUG}/settings/general-appearance"); p.wait_for_timeout(1500)
    msg = p.locator("input[name=message]")
    s.note("messages suggérés : " + str(msg.count()))
    s.cap_souple("01-messages-suggeres", [(p.get_by_text("Messages de chat suggérés").first, "Messages de chat suggérés"),
                                          (p.get_by_text("Ajouter un nouveau message", exact=False).first, "Ajouter un nouveau message")])
    rep = demander(s, "FAQ — garantie", "Quelle est la durée de garantie du cadre et de la batterie ?", "7 ans")
    s.cap_souple("02-faq-garantie", [(rep, "réponse"), (p.get_by_text("faq-sav.html").last, "source : faq-sav.html")])


def fournisseur(s):
    p = s.page
    rep = demander(s, "Fournisseur Batterix", "Quel délai de livraison prévoit le contrat Batterix, et quel score l'audit fournisseur a-t-il donné à Batterix ?", "21 jours|score")
    s.cap_souple("03-fournisseur-batterix", [(rep, "réponse croisant deux documents"),
                                             (p.get_by_text("contrat-batterix-scan.pdf").last, "contrat scanné"),
                                             (p.get_by_text("supplier-audit-batterix-en.pdf").last, "audit en anglais")])


def production(s):
    p = s.page
    rep = demander(s, "Point production", "Quand la ligne d'assemblage numéro 3 de Nantes sera-t-elle arrêtée, et pourquoi ?", "mars")
    s.cap_souple("04-message-vocal", [(rep, "réponse"), (p.get_by_text("message-vocal-production.mp3").last, "source : message vocal transcrit")])


if __name__ == "__main__":
    s = Scenario(CH)
    try:
        etapes([faq, fournisseur, production], s)
    finally:
        s.fermer()
