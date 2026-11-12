# Relecture avant lancement — AnythingLLM v1.19.0

Sources relues au tag `v1.19.0` (commit `9b1fcab141000eaba9f78ed131151de04904454b`, clone dans `sources/anythingllm`, ignoré par git).

| Fichier relu | Points relevés |
|---|---|
| `docker/docker-compose.yml` | Construit l'image localement (`build`) ; `cap_add: SYS_ADMIN` ; port `3001:3001` publié sur toutes les interfaces ; montages `./.env`, `server/storage`, `collector/hotdir`, `collector/outputs` ; `host.docker.internal`. Remplacé par `outils/anythingllm/compose.yml` : image officielle figée, port `127.0.0.1:3001`, un seul dossier de stockage, réseaux `llm-net` et `rag-local`. |
| `docker/HOW_TO_USE_DOCKER.md` | Commande recommandée : `docker run -p 3001:3001 --cap-add SYS_ADMIN -v $STORAGE:/app/server/storage -v $STORAGE/.env:/app/server/.env -e STORAGE_DIR=/app/server/storage`. Reprise telle quelle dans le compose, sauf l'adresse d'écoute. |
| `docker/Dockerfile` | Base `ubuntu:noble-20251013`, utilisateur `anythingllm` (UID/GID 1000), `NODE_ENV=production`, `ANYTHING_LLM_RUNTIME=docker`, `DEPLOYMENT_VERSION=1.19.0`, Chromium intégré (`/app/chrome-linux/chrome`, Puppeteer), `HEALTHCHECK` sur `/api/ping` toutes les minutes. |
| `docker/docker-entrypoint.sh` | Avertit si `STORAGE_DIR` manque ; `prisma generate` puis `prisma migrate deploy` (base SQLite), télémétrie de Prisma coupée (`CHECKPOINT_DISABLE=1`), puis le serveur (`server/index.js`) et le collecteur (`collector/index.js`) dans le même conteneur. |
| `docker/docker-healthcheck.sh` | `curl http://localhost:3001/api/ping`, sain si 200. |
| `docker/.env.example` | Variables par fournisseur ; `generic-openai` : `GENERIC_OPEN_AI_BASE_PATH`, `GENERIC_OPEN_AI_MODEL_PREF`, `GENERIC_OPEN_AI_MODEL_TOKEN_LIMIT`, `GENERIC_OPEN_AI_API_KEY`, `GENERIC_OPEN_AI_MODEL_MAX_TOKEN_KEY`, `GENERIC_OPEN_AI_CUSTOM_HEADERS`. Secrets `SIG_KEY`, `SIG_SALT`, `JWT_SECRET`. |
| `server/utils/boot/markOnboarded.js` | **Piège** : si `LLM_PROVIDER`, `VECTOR_DB`, `AUTH_TOKEN` ou `JWT_SECRET` sont présents au démarrage, l'instance est marquée « déjà accueillie » et l'assistant de premier lancement ne s'affiche plus (constaté au premier essai, `installation-2026-11-12-essai1-jwt.log`). `installer.sh` ne génère donc que `SIG_KEY` et `SIG_SALT` ; `JWT_SECRET` est créé par l'application (`server/endpoints/system.js`, ligne 705) à l'activation du mot de passe ou du mode multi-utilisateur. |

## Connexions sortantes observées au démarrage (télémétrie coupée)

Journal : `outils/resultats/anythingllm/demarrage-2026-11-12.log`. Avec `DISABLE_TELEMETRY="true"`, le journal affiche `[TELEMETRY DISABLED] Telemetry is marked as disabled - no events will send.` mais aussi :

- `[ContextWindowFinder] Pulling remote model map...` puis `Remote model map synced and cached` (table des tailles de contexte des modèles : `https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json`, `server/utils/AiProviders/modelMap/index.js`, ligne 30) ;
- `[ModelPricing] Remote pricing data synced and cached.` (table des prix des modèles : `https://models.dev/api.json`, `server/utils/helpers/modelPricing/index.js`, ligne 70).

Ces deux téléchargements ne transmettent aucune donnée de l'utilisateur mais montrent que l'instance contacte Internet même télémétrie coupée.
