"""Client minimal d'AnythingLLM (bibliothèque standard seulement).

- identifiants locaux fictifs : donnees/IDENTIFIANTS-LOCAUX.txt (ignoré par git) ;
- session administrateur : POST /api/request-token (API interne de l'interface) ;
- clé de l'API développeur : donnees/anythingllm/cle-api.txt, créée une fois par POST /api/admin/generate-api-key
  si absente (la même clé se crée à la souris : Paramètres › Outils › « API pour développeurs ») ;
- appels de l'API développeur : /api/v1/... avec « Authorization: Bearer <clé> ».
Aucun secret n'est affiché.
"""
import json, mimetypes, os, re, urllib.error, urllib.request, uuid
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
BASE = os.environ.get("ANYTHINGLLM_URL", "http://127.0.0.1:3001")
IDENT = RACINE / "donnees/IDENTIFIANTS-LOCAUX.txt"
CLE = RACINE / "donnees/anythingllm/cle-api.txt"
PENSEE = re.compile(r"<think>.*?</think>\s*", re.S)


def identifiants():
    """Lit donnees/IDENTIFIANTS-LOCAUX.txt : « anythingllm.instance.mot_de_passe=… » (mode mono-utilisateur) et,
    après passage en multi-utilisateur, « anythingllm.admin.utilisateur=… » / « anythingllm.admin.mot_de_passe=… »."""
    d = {}
    for l in IDENT.read_text().splitlines() if IDENT.exists() else []:
        if "=" in l and l.startswith("anythingllm."):
            k, v = l.split("=", 1); d[k.strip()] = v.strip()
    return d


def _req(methode, chemin, corps=None, jeton=None, multipart=None, timeout=900):
    h = {}
    data = None
    if multipart is not None:
        borne = uuid.uuid4().hex
        parts = []
        for nom, val in multipart.items():
            if isinstance(val, Path):
                type_ = mimetypes.guess_type(val.name)[0] or "application/octet-stream"
                parts.append(f'--{borne}\r\nContent-Disposition: form-data; name="{nom}"; filename="{val.name}"\r\n'
                             f"Content-Type: {type_}\r\n\r\n".encode() + val.read_bytes() + b"\r\n")
            else:
                parts.append(f'--{borne}\r\nContent-Disposition: form-data; name="{nom}"\r\n\r\n{val}\r\n'.encode())
        data = b"".join(parts) + f"--{borne}--\r\n".encode()
        h["Content-Type"] = f"multipart/form-data; boundary={borne}"
    elif corps is not None:
        data = json.dumps(corps).encode(); h["Content-Type"] = "application/json"
    if jeton:
        h["Authorization"] = "Bearer " + jeton
    r = urllib.request.Request(BASE + chemin, data=data, method=methode, headers=h)
    try:
        with urllib.request.urlopen(r, timeout=timeout) as rep:
            txt = rep.read().decode()
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{methode} {chemin} -> {e.code} {e.read().decode()[:300]}") from None
    return json.loads(txt) if txt.strip().startswith(("{", "[")) else txt


def multi_utilisateur():
    return bool(_req("GET", "/api/system/multi-user-mode").get("multiUserMode"))


def session_admin():
    d = identifiants()
    if multi_utilisateur():
        corps = {"username": d["anythingllm.admin.utilisateur"], "password": d["anythingllm.admin.mot_de_passe"]}
    else:
        corps = {"password": d.get("anythingllm.instance.mot_de_passe", "")}
    r = _req("POST", "/api/request-token", corps)
    if not r.get("valid"):
        raise RuntimeError("connexion refusée : " + str(r.get("message")))
    return r["token"]


def cle_api():
    if CLE.exists():
        return CLE.read_text().strip()
    route = "/api/admin/generate-api-key" if multi_utilisateur() else "/api/system/generate-api-key"
    r = _req("POST", route, {"name": "Scripts du banc"}, jeton=session_admin())
    CLE.parent.mkdir(parents=True, exist_ok=True)
    old = os.umask(0o077); CLE.write_text(r["apiKey"]["secret"]); os.umask(old)
    return CLE.read_text().strip()


class API:
    """API développeur /api/v1."""

    def __init__(self, cle=None):
        self.cle = cle or cle_api()

    def get(self, chemin):
        return _req("GET", "/api/v1" + chemin, jeton=self.cle)

    def post(self, chemin, corps=None, **kw):
        return _req("POST", "/api/v1" + chemin, corps, jeton=self.cle, **kw)

    def delete(self, chemin):
        return _req("DELETE", "/api/v1" + chemin, jeton=self.cle)

    def espace(self, nom, **reglages):
        """Crée l'espace s'il n'existe pas (par nom), applique les réglages, renvoie son slug."""
        for w in self.get("/workspaces")["workspaces"]:
            if w["name"] == nom:
                slug = w["slug"]; break
        else:
            slug = self.post("/workspace/new", {"name": nom})["workspace"]["slug"]
        if reglages:
            self.post(f"/workspace/{slug}/update", reglages)
        return slug

    def televerser(self, fichier, slug=None):
        champs = {"file": Path(fichier)}
        if slug:
            champs["addToWorkspaces"] = slug
        return self.post("/document/upload", multipart=champs)

    def demander(self, slug, message, mode="query", session=None):
        r = self.post(f"/workspace/{slug}/chat", {"message": message, "mode": mode,
                                                  "sessionId": session or uuid.uuid4().hex})
        return r


def sans_pensee(texte):
    """Retire le raisonnement <think>…</think> que le modèle chat place en tête de la réponse."""
    texte = PENSEE.sub("", texte or "")
    return texte.split("</think>", 1)[-1].strip() if "</think>" in texte else texte.strip()
