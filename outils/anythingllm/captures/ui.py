"""Socle des scénarios de captures d'AnythingLLM (exécutés dans le conteneur Playwright, outils/communs/captures/lancer.sh).

- navigateur 1440 × 900, interface en français (locale fr-FR et localStorage « i18nextLng » = « fr ») ;
- connexion avec les identifiants fictifs de donnees/IDENTIFIANTS-LOCAUX.txt (mot de passe de l'instance, puis compte
  administrateur après passage en multi-utilisateur) ;
- Scenario.cap(...) : capture annotée (annoter.capture) dans docs/anythingllm/img/<chapitre>/<nom>.png, texte de la page dans
  outils/resultats/anythingllm/captures/<chapitre>/<nom>.txt, libellés des pastilles dans .../<chapitre>/scenario.json ;
- les secrets (clé du service central, mots de passe) sont masqués avant capture.
"""
import json, os, re, sys, time
from pathlib import Path

from playwright.sync_api import sync_playwright, expect  # noqa: F401
import annoter

RACINE = Path("/depot") if Path("/depot").exists() else Path(__file__).resolve().parents[3]
BASE = os.environ.get("ANYTHINGLLM_URL", "http://rag-anythingllm:3001")
IMG = RACINE / "docs/anythingllm/img"
TXT = RACINE / "outils/resultats/anythingllm/captures"
IDENT = RACINE / "donnees/IDENTIFIANTS-LOCAUX.txt"


def identifiants():
    d = {}
    if IDENT.exists():
        for l in IDENT.read_text().splitlines():
            if "=" in l and l.startswith("anythingllm."):
                k, v = l.split("=", 1); d[k.strip()] = v.strip()
    return d


class Scenario:
    def __init__(self, chapitre, connecter=True, langue="fr"):
        self.chapitre = chapitre
        self.journal = []
        self._pw = sync_playwright().start()
        self.navigateur = self._pw.chromium.launch()
        self.contexte = self.navigateur.new_context(viewport={"width": 1440, "height": 900}, locale="fr-FR",
                                                    accept_downloads=True)
        if langue:
            self.contexte.add_init_script(f"try {{ if (!localStorage.getItem('i18nextLng')) localStorage.setItem('i18nextLng', '{langue}') }} catch (e) {{}}")
        self.page = self.contexte.new_page()
        self.page.set_default_timeout(30000)
        if connecter:
            self.connecter()

    # ---------- navigation ----------
    def aller(self, chemin, attendre=None):
        self.page.goto(BASE + chemin)
        self.page.wait_for_load_state("networkidle")
        if attendre is not None:
            attendre.wait_for(state="visible")
        self.page.wait_for_timeout(600)

    def connecter(self):
        d = identifiants()
        self.page.goto(BASE + "/")
        self.page.wait_for_load_state("networkidle")
        mdp = self.page.locator("input[name=password]")
        try:
            mdp.wait_for(state="visible", timeout=4000)
        except Exception:
            return  # déjà ouvert (pas de mot de passe) ou session valide
        if self.page.locator("input[name=username]").count():
            self.page.fill("input[name=username]", d["anythingllm.admin.utilisateur"])
            mdp.fill(d["anythingllm.admin.mot_de_passe"])
        else:
            mdp.fill(d["anythingllm.instance.mot_de_passe"])
        self.page.locator("form button[type=submit]").click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1500)

    # ---------- captures ----------
    def cap(self, nom, elements=(), masques=(), plein=False, clip=None, attendre=None, note="", auto=True):
        """elements : liste de (locator, libellé). Écrit image, texte de la page et libellés."""
        if attendre is not None:
            attendre.wait_for(state="visible")
        self.page.wait_for_timeout(400)
        img = IMG / self.chapitre / f"{nom}.png"
        txt = TXT / self.chapitre / f"{nom}.txt"
        masques = list(masques) + (self._secrets_visibles() if auto else [])
        libs = annoter.capture(self.page, img, elements, masques=masques, plein=plein, clip=clip, texte=txt)
        self.journal.append({"capture": f"{self.chapitre}/{nom}.png", "url": self.page.url.replace(BASE, ""),
                             "pastilles": libs, "note": note, "heure": time.strftime("%H:%M:%S")})
        self._ecrire_journal()
        return libs

    def _secrets_visibles(self):
        """Champs de clé ou de mot de passe remplis : masqués d'office."""
        res = []
        for sel in ("input[type=password]", "input[name$=Key]", "input[name*=ApiKey]", "input[name*=api_key]"):
            for loc in self.page.locator(sel).all():
                try:
                    if loc.is_visible() and loc.input_value():
                        res.append(loc)
                except Exception:
                    pass
        return res

    def _ecrire_journal(self):
        f = TXT / self.chapitre / "scenario.json"
        f.parent.mkdir(parents=True, exist_ok=True)
        anciens = json.loads(f.read_text()) if f.exists() else []
        noms = {j["capture"] for j in self.journal}
        anciens = [a for a in anciens if a["capture"] not in noms]
        f.write_text(json.dumps(anciens + self.journal, ensure_ascii=False, indent=1))

    def note(self, texte):
        print("NOTE", texte, flush=True)
        f = TXT / self.chapitre / "notes.log"
        f.parent.mkdir(parents=True, exist_ok=True)
        with f.open("a") as h:
            h.write(time.strftime("%Y-%m-%d %H:%M:%S ") + texte + "\n")

    # ---------- aides ----------
    def sans_toasts(self, delai=15000):
        """Attend la disparition des notifications (elles couvrent les boutons du bas de la fenêtre des documents)."""
        try:
            self.page.wait_for_function("() => document.querySelectorAll('.Toastify__toast').length === 0", timeout=delai)
        except Exception:
            self.page.evaluate("() => document.querySelectorAll('.Toastify__toast').forEach(t => t.remove())")

    def croix(self):
        """Bouton de fermeture (croix, sans libellé) en haut à droite de la fenêtre des documents."""
        return self.page.locator("button:has(svg)").filter(has_not_text=" ").locator(
            "xpath=self::*[ancestor::*[contains(@class,'fixed')]]").last

    def gestionnaire(self, slug):
        """Ouvre la fenêtre des documents de l'espace par l'icône d'envoi de la barre latérale."""
        p = self.page
        if not p.url.endswith(f"/workspace/{slug}"):
            self.aller(f"/workspace/{slug}")
        ligne = p.locator(f'a[href="/workspace/{slug}"]').locator('xpath=ancestor::*[@role="listitem"][1]')
        ligne.hover(); ligne.locator('button[data-tooltip-id="upload-workspace"]').click()
        p.get_by_text("Mes documents").first.wait_for(); p.wait_for_timeout(1500)

    def fermer_gestionnaire(self):
        p = self.page
        x = p.evaluate_handle("() => { const b = document.elementFromPoint(1366, 126); return b && b.closest('button'); }")
        if x.as_element():
            x.as_element().click()
        else:
            p.keyboard.press("Escape")
        p.wait_for_timeout(1000)

    def bouton(self, nom, exact=False):
        return self.page.get_by_role("button", name=nom, exact=exact)

    def texte(self, t, exact=False):
        return self.page.get_by_text(t, exact=exact)

    def lien_espace(self, slug):
        return self.page.locator(f'a[href="/workspace/{slug}"]')

    def fermer(self):
        try:
            self.navigateur.close()
        finally:
            self._pw.stop()


def etapes(fonctions, scenario):
    """Lance les fonctions demandées en argument (ou toutes), dans l'ordre."""
    noms = sys.argv[1:] or [f.__name__ for f in fonctions]
    for f in fonctions:
        if f.__name__ in noms:
            print("==", f.__name__, flush=True)
            f(scenario)
