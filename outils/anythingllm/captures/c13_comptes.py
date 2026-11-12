"""Chapitre 13, Comptes, équipe et widget : passage en multi-utilisateur (irréversible), comptes et rôles, membres d'un
espace, invitation, première connexion d'un utilisateur, compte, widget intégrable essayé sur le site de test.
Identifiants fictifs ajoutés à donnees/IDENTIFIANTS-LOCAUX.txt. Usage : lancer.sh ... c13_comptes.py [etapes]
"""
import os, re
from ui import Scenario, etapes, identifiants, IDENT, BASE

CH = "13-comptes-et-widget"
ADMIN, UTIL = "admin-velanor", "camille.martin"


def ajouter_ident(cle, valeur):
    d = identifiants()
    if cle not in d:
        with IDENT.open("a") as f:
            f.write(f"{cle}={valeur}\n")
    return identifiants()[cle]


def multi(s):
    p = s.page
    mdp = ajouter_ident("anythingllm.admin.mot_de_passe", "Admin-Velanor-" + os.urandom(4).hex())
    ajouter_ident("anythingllm.admin.utilisateur", ADMIN)
    s.aller("/settings/security"); p.wait_for_timeout(1500)
    inter = p.get_by_text("Activer le mode multi-utilisateurs", exact=False).first
    inter.click(); p.wait_for_timeout(800)
    form = p.locator("form").filter(has=p.locator("input[name=username]")).first
    form.locator("input[name=username]").fill(ADMIN)
    form.locator("input[name=password]").fill(mdp)
    s.note("sécurité : " + p.inner_text("body")[-1500:].replace("\n", " | "))
    enr = form.get_by_role("button").filter(has_text=re.compile("Enregistrer|Save")).first
    s.cap_souple("01-mode-multi-utilisateurs", [(inter, "Activer le mode multi-utilisateurs"),
                                                (p.locator("input[name=username]"), "Nom d'utilisateur du compte administrateur"),
                                                (form.locator("input[name=password]"), "Mot de passe du compte administrateur"),
                                                (enr, enr.inner_text() if enr.count() else "Enregistrer")])
    p.on("dialog", lambda d: (s.note("confirmation : " + d.message), d.accept()))
    enr.click(); p.wait_for_timeout(1200)
    s.note("toast : " + " / ".join(p.locator(".Toastify__toast").all_inner_texts()))
    p.wait_for_timeout(4000)
    s.note("après activation : " + p.url + " " + p.inner_text("body")[:600].replace("\n", " | "))


def connexion(s):
    ctx = s.navigateur.new_context(viewport={"width": 1440, "height": 900}, locale="fr-FR")
    ctx.add_init_script("localStorage.setItem('i18nextLng','fr')")
    vieux, s.page = s.page, ctx.new_page()
    p = s.page; d = identifiants()
    s.aller("/")
    p.locator("input[name=username]").fill(d["anythingllm.admin.utilisateur"])
    p.locator("input[name=password]").fill(d["anythingllm.admin.mot_de_passe"])
    s.cap_souple("02-connexion-multi", [(p.locator("input[name=username]"), "Nom d'utilisateur"),
                                        (p.locator("input[name=password]"), "Mot de passe"),
                                        (p.locator("form button[type=submit]"), "Connexion")])
    ctx.close(); s.page = vieux


def utilisateurs(s):
    p = s.page
    mdp = ajouter_ident("anythingllm.utilisateur.mot_de_passe", "Camille-" + os.urandom(4).hex())
    ajouter_ident("anythingllm.utilisateur.nom", UTIL)
    s.aller("/settings/users"); p.wait_for_timeout(1500)
    p.get_by_text("Add user", exact=True).first.click(); p.wait_for_timeout(1200)
    p.locator("input[name=username]").last.fill(UTIL)
    p.locator("input[name=password]").last.fill(mdp)
    role = p.locator("select[name=role]")
    s.note("rôles : " + str(role.locator("option").all_inner_texts()))
    role.select_option("default")
    ajout = p.locator("form").filter(has=p.locator("select[name=role]")).locator("button[type=submit]")
    s.cap_souple("03-nouvel-utilisateur", [(p.locator("input[name=username]").last, "User's username"),
                                           (p.locator("input[name=password]").last, "mot de passe"), (role, "rôle"), (ajout, "Add user")])
    ajout.click(); p.wait_for_timeout(2000)
    s.cap_souple("04-utilisateurs", [(p.get_by_text(UTIL, exact=True).first, UTIL), (p.get_by_text(ADMIN, exact=True).first, ADMIN),
                                     (p.get_by_text("Add user", exact=True).first, "Add user")])
    s.note("utilisateurs : " + p.inner_text("body")[-1000:].replace("\n", " | "))


def membres(s):
    p = s.page
    s.aller("/workspace/demo-velanor/settings/members"); p.wait_for_timeout(1500)
    s.bouton("Manage Users").first.click(); p.wait_for_timeout(1000)
    p.get_by_text(UTIL, exact=True).last.click(); p.wait_for_timeout(400)
    enr = p.get_by_role("button", name="Save").last
    s.cap_souple("05-membres-de-l-espace", [(p.get_by_text(UTIL, exact=True).last, UTIL + " (coché)"), (enr, "Save")])
    enr.click(); p.wait_for_timeout(1500)
    s.note("membres : " + p.inner_text("body")[-800:].replace("\n", " | "))


def invitation(s):
    p = s.page
    s.aller("/settings/invites"); p.wait_for_timeout(1500)
    s.bouton("Create Invite Link").first.click(); p.wait_for_timeout(1000)
    s.note("invitation : " + p.inner_text("body")[-900:].replace("\n", " | "))
    creer = p.get_by_role("button", name="Create Invite").last
    s.cap_souple("06-invitation", [(p.get_by_text("Auto-add invitee to workspaces", exact=False).first, "Auto-add invitee to workspaces"),
                                   (creer, "Create Invite")])
    creer.click(); p.wait_for_timeout(2000)
    s.cap_souple("07-invitation-creee", [(p.get_by_text("Copy Invite Link", exact=False).first, "Copy Invite Link")])


def premiere_connexion(s):
    ctx = s.navigateur.new_context(viewport={"width": 1440, "height": 900}, locale="fr-FR", accept_downloads=True)
    ctx.add_init_script("localStorage.setItem('i18nextLng','fr')")
    vieux, s.page = s.page, ctx.new_page()
    p = s.page; d = identifiants()
    s.aller("/")
    p.locator("input[name=username]").fill(UTIL); p.locator("input[name=password]").fill(d["anythingllm.utilisateur.mot_de_passe"])
    p.locator("form button[type=submit]").click(); p.wait_for_timeout(2500)
    dl = s.bouton("Download").first
    try:
        dl.wait_for(timeout=10000)
        s.cap_souple("08-codes-de-recuperation", [(dl, "Download"), (s.bouton("Close").first, "Close")],
                     masques=[x for x in p.get_by_text(re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-")).all()])
        with p.expect_download() as tel:
            dl.click()
        tel.value.save_as("/depot/donnees/anythingllm/codes-recuperation-camille.txt")
        s.bouton("Close").first.click(); p.wait_for_timeout(1500)
    except Exception as e:
        s.note("codes : " + str(e)[:200])
    s.cap_souple("09-vue-utilisateur", [(p.locator("[aria-label=Workspaces]"), "seuls les espaces dont l'utilisateur est membre"),
                                        (p.locator("#primary-prompt-input"), "Envoyer un message")])
    s.note("vue utilisateur : " + p.inner_text("body")[:900].replace("\n", " | "))
    ctx.close(); s.page = vieux


def compte(s):
    p = s.page
    s.aller("/"); p.wait_for_timeout(1500)
    pastille = p.locator("button:visible").filter(has_text=re.compile(r"^AD$")).first
    s.note("boutons : " + str([b.inner_text() for b in p.locator("button:visible").all()[:30]]))
    p.mouse.click(1383, 54); p.wait_for_timeout(1000)  # pastille du compte, en haut à droite
    s.note("après clic pastille : " + p.inner_text("body")[-400:].replace("\n", " | "))
    s.cap_souple("10-menu-du-compte", [(p.get_by_text("Compte", exact=True).first, "Compte"), (p.get_by_text("Déconnexion", exact=True).first, "Déconnexion")])
    p.get_by_text("Compte", exact=True).first.click(); p.wait_for_timeout(1200)
    s.cap_souple("11-fenetre-compte", [(p.locator("select[name=theme]"), "Thème"), (p.locator("select[name=userLang]"), "Langue"),
                                       (p.get_by_role("button", name="Mettre à jour le compte"), "Mettre à jour le compte")])
    p.keyboard.press("Escape")


def widget(s):
    p = s.page
    s.aller("/settings/embed-chat-widgets"); p.wait_for_timeout(1500)
    creer = p.get_by_role("button").filter(has_text="Créer un widget intégré").first
    creer.click(); p.wait_for_timeout(1200)
    sel = p.locator("select[name=workspace_id]")
    sel.select_option(label="Démo Vélanor")
    p.locator("input[name=chat_mode][value=query]").check(force=True)
    dom = p.get_by_placeholder(re.compile("mysite|domain|exemple|example", re.I)).first
    try:
        dom.fill("rag-anythingllm-site"); dom.press("Enter")
    except Exception as e:
        s.note("domaine : " + str(e)[:120])
    p.locator("input[name=max_chats_per_day]").fill("200")
    p.locator("input[name=max_chats_per_session]").fill("20")
    fin = p.get_by_role("button").filter(has_text=re.compile("Créer|Create")).last
    s.cap_souple("12-nouveau-widget", [(sel, "espace de travail"), (p.locator("input[name=chat_mode][value=query]"), "mode Requête"),
                                       (p.locator("input[name=max_chats_per_day]"), "limite par jour"), (fin, fin.inner_text() if fin.count() else "Créer")], plein=True)
    fin.click(); p.wait_for_timeout(2500)
    s.note("widget : " + p.inner_text("body")[-1500:].replace("\n", " | "))
    code = p.get_by_text("Code", exact=False).first
    s.cap_souple("13-widgets", [(p.get_by_text("Démo Vélanor", exact=False).last, "widget de Démo Vélanor"), (code, "code à intégrer")])
    try:
        code.click(); p.wait_for_timeout(1500)
        snippet = p.locator("pre, code, textarea").first.inner_text()
        m = re.search(r'data-embed-id="([^"]+)"', snippet)
        if m:
            page = open("/depot/outils/anythingllm/essais/site/widget.html").read().replace("EMBED_ID", m.group(1))
            open("/depot/outils/anythingllm/essais/site/widget-actif.html", "w").write(page)
        s.cap_souple("14-code-du-widget", [(p.locator("pre, code, textarea").first, "code HTML à coller dans le site")])
        s.note("snippet : " + snippet[:600].replace("\n", " "))
    except Exception as e:
        s.note("code widget : " + str(e)[:200])


def widget_code(s):
    p = s.page
    s.aller("/settings/embed-chat-widgets"); p.wait_for_timeout(1500)
    p.get_by_text("Code", exact=True).first.click(); p.wait_for_timeout(1500)
    bloc = p.get_by_text("data-embed-id", exact=False).first
    s.cap_souple("14-code-du-widget", [(bloc, "code HTML à coller dans le site")])
    s.note("code : " + p.inner_text("body")[-1500:].replace("\n", " | "))


def widget_essai(s):
    p = s.page
    p.goto("http://rag-anythingllm-site/widget-actif.html"); p.wait_for_load_state("networkidle"); p.wait_for_timeout(3000)
    bulle = p.locator("#anything-llm-embed-chat-button")
    s.cap_souple("15-site-avec-widget", [(bulle, "bulle de discussion")])
    bulle.click(); p.wait_for_timeout(2000)
    champ = p.locator("#message-input")
    champ.fill("Quelle est la durée de garantie du cadre ?"); champ.press("Enter")
    try:
        p.wait_for_function("() => document.body.innerText.includes('7 ans')", timeout=240000)
    except Exception as e:
        s.note("widget réponse : " + str(e)[:100])
    p.wait_for_timeout(3000)
    s.cap_souple("16-widget-reponse", [(p.get_by_text("7 ans", exact=False).last, "réponse dans le site")])
    s.note("widget essai : " + p.inner_text("body")[-900:].replace("\n", " | "))


if __name__ == "__main__":
    s = Scenario(CH)
    try:
        etapes([multi, connexion, utilisateurs, membres, invitation, premiere_connexion, compte, widget, widget_code, widget_essai], s)
    finally:
        s.fermer()
