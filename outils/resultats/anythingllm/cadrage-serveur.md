# Cadrage serveur AnythingLLM v1.19.0 (lecture du code source)

- Source lue : `sources/anythingllm` (étiquette `v1.19.0`, commit `9b1fcab`), en lecture seule, sans exécution ni réseau.
- Les chemins ci-dessous sont relatifs à `sources/anythingllm/`. Le format `fichier:ligne` renvoie à la ligne qui prouve l'affirmation.
- Contexte visé : image `mintplexlabs/anythingllm:1.19.0`, modèles servis par LiteLLM à `http://llm-central:8080/v1` (clé Bearer), modèles `chat`, `embed`, `rerank`, `transcribe`.

---

## 1. Docker

### 1.1 `docker/Dockerfile`
- Base `ubuntu:noble-20251013` (`docker/Dockerfile:2`), Node 18 (`:98`), `uv`/`uvx` 0.6.10 pour MCP (`:105-109`), `ffmpeg` (`:93`).
- Utilisateur `anythingllm`, UID/GID par défaut 1000 (`ARG_UID=1000`, `ARG_GID=1000` : `:5-6`, création `:115-119`, `USER anythingllm` `:138`/`:168`). Répertoire de travail `/app`.
- Le fichier `docker/.env.example` est copié en `/app/server/.env` dans l'image (`:124`).
- Variables figées dans l'image : `NODE_ENV=production`, `ANYTHING_LLM_RUNTIME=docker`, `DEPLOYMENT_VERSION=1.19.0` (`:176-178`).
- Aucune instruction `EXPOSE` ni `VOLUME` dans le Dockerfile : le port 3001 et le volume viennent de la commande `docker run` / compose.
- Healthcheck : toutes les minutes, délai 10 s, période de démarrage 1 min, script `docker-healthcheck.sh` (`:181-182`) qui appelle `http://localhost:${SERVER_PORT:-3001}/api/ping` et attend HTTP 200 (`docker/docker-healthcheck.sh:5-8`). `/api/ping` répond `{online:true}` sans authentification (`server/endpoints/system.js:84-86`).
- Point d'entrée `docker/docker-entrypoint.sh` : avertit si `STORAGE_DIR` est vide (`docker/docker-entrypoint.sh:3-16`), désactive la télémétrie Prisma (`CHECKPOINT_DISABLE=1`), lance `prisma generate` + `prisma migrate deploy`, puis le serveur (`node /app/server/index.js`) et le collecteur (`node /app/collector/index.js`) en parallèle ; le conteneur s'arrête dès que l'un des deux s'arrête (`wait -n`).
- Le collecteur écoute sur `COLLECTOR_PORT` (8888 par défaut, interne) (`docker/.env.example:528-529`).

### 1.2 `docker/docker-compose.yml` (compose de construction locale, pas d'image publiée)
- Construit depuis les sources (`build:` `:10-15`), `cap_add: SYS_ADMIN` (`:16-17`), volumes `./.env:/app/server/.env`, `../server/storage:/app/server/storage`, `hotdir`, `outputs` (`:18-22`), `user: "${UID:-1000}:${GID:-1000}"` (`:23`), port `"3001:3001"` (`:24-25`, donc publié sur toutes les interfaces), `extra_hosts: host.docker.internal:host-gateway` (`:30-31`).

### 1.3 `docker/HOW_TO_USE_DOCKER.md` (commande recommandée)
- `docker run -d --rm -p 3001:3001 --cap-add SYS_ADMIN -v ${STORAGE_LOCATION}:/app/server/storage -v ${STORAGE_LOCATION}/.env:/app/server/.env -e STORAGE_DIR="/app/server/storage" mintplexlabs/anythingllm` (`docker/HOW_TO_USE_DOCKER.md:54-64`). Le fichier `.env` doit exister avant (`touch`, `:57`).
- Exemple compose avec `cap_add: SYS_ADMIN`, `STORAGE_DIR`, `JWT_SECRET`, fournisseurs par variables d'environnement (`:94-133`).
- `SYS_ADMIN` sert au bac à sable de Chromium (Puppeteer, collecte de pages web). Alternative documentée sans cette capacité : `ANYTHINGLLM_CHROMIUM_ARGS="--no-sandbox,--disable-setuid-sandbox"` (`docker/.env.example:536-539`).
- UID/GID 1000 par défaut ; un écart avec l'utilisateur hôte cause des problèmes de droits (`HOW_TO_USE_DOCKER.md:283-285`).
- Moteur LLM intégré (Lemonade/llama.cpp) optionnel, désactivé sauf `ENABLE_BUILT_IN_LLM=true` (`:146-161`) ; sans objet ici.

### 1.4 Variables d'environnement indispensables / utiles
| Variable | Rôle | Preuve |
|---|---|---|
| `STORAGE_DIR=/app/server/storage` | Stockage persistant (sinon perte de données). La base SQLite est en chemin fixe `server/storage/anythingllm.db`, d'où l'intérêt de garder exactement cette valeur | `docker/docker-entrypoint.sh:3-16`, `server/prisma/schema.prisma:15` |
| `SERVER_PORT` | Port HTTP, 3001 par défaut | `server/index.js:198`, `docker/.env.example:1` |
| `SIG_KEY`, `SIG_SALT` | Clé/sel de chiffrement ; générés automatiquement (32 octets aléatoires) et écrits dans `.env` s'ils manquent | `server/utils/EncryptionManager/index.js:38-43` |
| `JWT_SECRET` | Signature des sessions ; requis pour la protection par mot de passe et le multi-utilisateur ; généré (`uuid v4`) quand on active un mot de passe ou le multi-utilisateur | `server/utils/http/index.js:26-28`, `server/endpoints/system.js:648-654`, `:703-708` |
| `AUTH_TOKEN` | Mot de passe de l'instance en mode mono-utilisateur | `server/utils/middleware/validatedRequest.js:15-23`, `server/endpoints/system.js:319-325` |
| `JWT_EXPIRY` | Durée de session (ex. `30d`) | `docker/.env.example:8`, `server/endpoints/system.js:296-298` |
| `DISABLE_TELEMETRY="true"` | Coupe PostHog (voir §7) | `server/models/telemetry.js:50` |
| `DISABLE_SWAGGER_DOCS="true"` | Retire `/api/docs` | `server/swagger/utils.js:12-17` |
| `UID`, `GID` | Seulement pour le compose de construction | `docker/.env.example:3-4` |

Attention : si ni `AUTH_TOKEN` ni `JWT_SECRET` ne sont définis et que le mode multi-utilisateur est inactif, toutes les routes internes sont ouvertes sans authentification (`server/utils/middleware/validatedRequest.js:15-23`).

Point important sur `.env` : à chaque `updateENV` (réglage par l'interface ou l'API), `dumpENV()` réécrit `/app/server/.env` avec toutes les clés connues, secrets compris (`GENERIC_OPEN_AI_API_KEY`, `SIG_KEY`, etc.) (`server/utils/helpers/updateENV.js:1586-1715`, chemin `:1712`). Les valeurs sont tronquées au premier caractère parmi `" ' \` #` et blancs (`:1694-1701`). La clé du service LLM se retrouve donc en clair dans le `.env` monté depuis `donnees/`.

---

## 2. Fournisseur LLM « Generic OpenAI »

Fichier : `server/utils/AiProviders/genericOpenAi/index.js`.

### 2.1 Variables
| Variable | Défaut | Preuve |
|---|---|---|
| `LLM_PROVIDER='generic-openai'` | — | `docker/.env.example:83` |
| `GENERIC_OPEN_AI_BASE_PATH` (obligatoire, URL) | erreur si absent | `genericOpenAi/index.js:24-30` ; contrôle `isValidURL` `server/utils/helpers/updateENV.js:209-211` |
| `GENERIC_OPEN_AI_MODEL_PREF` (obligatoire) | erreur si absent | `genericOpenAi/index.js:39-45` |
| `GENERIC_OPEN_AI_MODEL_TOKEN_LIMIT` | **4096** si absent | `genericOpenAi/index.js:121-126` |
| `GENERIC_OPEN_AI_API_KEY` | `null` (envoyé en `Authorization: Bearer` par le SDK `openai`) | `genericOpenAi/index.js:31-33` |
| `GENERIC_OPEN_AI_MAX_TOKENS` | **1024** si absent | `genericOpenAi/index.js:41-43` |
| `GENERIC_OPEN_AI_MODEL_MAX_TOKEN_KEY` | `max_tokens` (ex. `max_completion_tokens`) | `genericOpenAi/index.js:71-73` |
| `GENERIC_OPEN_AI_CUSTOM_HEADERS` | format `Nom:valeur,Nom2:valeur2` | `genericOpenAi/index.js:75-93` |
| `GENERIC_OPENAI_STREAMING_DISABLED="true"` | streaming actif par défaut | `genericOpenAi/index.js:107-110` |
| `GENERIC_OPEN_AI_REPORT_USAGE="true"` | ajoute `stream_options.include_usage` | `genericOpenAi/index.js:227-235` |
| `PROVIDER_DISABLE_NATIVE_TOOL_CALLING="generic-openai"` | appel d'outils natif actif par défaut | `genericOpenAi/index.js:454-457` |
| `PROVIDER_SUPPORTS_REASONING`, `_VISION`, `_IMAGE_GENERATION` | désactivés par défaut | `genericOpenAi/index.js:458-469` |

Noms de champs côté API interne `update-env` : `LLMProvider`, `GenericOpenAiBasePath`, `GenericOpenAiModelPref`, `GenericOpenAiTokenLimit`, `GenericOpenAiKey`, `GenericOpenAiMaxTokens` (`server/utils/helpers/updateENV.js:5-6`, `:209-228`).

### 2.2 Requête envoyée
- Corps : `model`, `messages`, `temperature` (seulement si définie), `max_tokens` (= `GENERIC_OPEN_AI_MAX_TOKENS`, 1024 par défaut) (`genericOpenAi/index.js:243-248` non streamé, `:285-292` streamé). `maxTokensParam` n'émet le champ que pour un nombre > 0 (`server/utils/agents/aibitat/providers/helpers/tooled.js:174-182`).
- Conséquence pratique : avec la réflexion `<think>` de Qwen, 1024 jetons de sortie risquent de couper la réponse ; régler `GENERIC_OPEN_AI_MAX_TOKENS`.
- Température : `workspace.openAiTemp` ; si vide, aucun champ `temperature` n'est envoyé (`server/utils/helpers/index.js:138-144`, `tooled.js:204-208`).
- **Aucun moyen de passer `chat_template_kwargs` ni de paramètre libre** pour ce fournisseur : la fonction `reasoningParams` ne connaît pas `generic-openai` (cas `default` → `{}`) (`server/utils/helpers/reasoningEffort.js:134-195`) et les méthodes du fournisseur n'acceptent que `temperature` (`genericOpenAi/index.js:237-240`, `:280-283`). `chat_template_kwargs.enable_thinking` n'est envoyé que pour Lemonade (`reasoningEffort.js:169-176`). Désactiver la réflexion doit donc se faire côté LiteLLM (paramètres par défaut du modèle `chat`).
- Le fournisseur `LLM_PROVIDER='litellm'` existe aussi (`server/utils/AiProviders/liteLLM/index.js`, variables `LITE_LLM_BASE_PATH`, `LITE_LLM_MODEL_PREF`, `LITE_LLM_MODEL_TOKEN_LIMIT`, `LITE_LLM_API_KEY` : `docker/.env.example:91-95`). Il n'envoie pas `max_tokens` (`liteLLM/index.js:136-140`) et, en non-streamé, ne renvoie que `message.content` (le `reasoning_content` est perdu) (`liteLLM/index.js:152-153`).

### 2.3 Réflexion `<think>` / `reasoning_content`
- Champs lus : `reasoning_content`, `reasoning` ou `thinking` (`server/utils/helpers/chat/responses.js:11-18`).
- Non streamé : le raisonnement est réinjecté en tête du texte sous la forme `<think>…</think>` + contenu (`genericOpenAi/index.js:213-219`).
- Streamé : envoi d'un `<think>` d'ouverture, des jetons de raisonnement, puis `</think>` avant le premier jeton de contenu (`genericOpenAi/index.js:346-387`).
- Si LiteLLM renvoie le `<think>` directement dans `content`, il est conservé tel quel.
- Le texte enregistré (`response.text`) contient donc le bloc `<think>` ; il est renvoyé tel quel dans `textResponse` de l'API (`server/utils/chats/apiChatHandler.js:474-498`).
- L'interface masque/replie le bloc (`frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/HistoricalMessage/index.jsx:27-32`, `:339-343`). Le serveur ne le retire que pour l'export de conversations (`server/utils/chats/exportChatToFile.js:36`), la synthèse vocale et les notifications (`server/utils/helpers/index.js:799-815`). **Il n'est pas retiré de l'historique renvoyé au modèle** : `convertToPromptHistory` reprend `data.text` sans filtrage (`server/utils/helpers/chat/responses.js:284-315`).

### 2.4 Budget de contexte
- Fenêtre = `promptWindowLimit()` = `GENERIC_OPEN_AI_MODEL_TOKEN_LIMIT` (4096 par défaut) (`genericOpenAi/index.js:121-126`). Le `max_tokens` de sortie n'est **pas** retranché de cette fenêtre ; seule une marge fixe de 600 jetons est prise (`server/utils/helpers/chat/index.js:53-57`).
- Répartition : système (prompt + contexte documentaire) 15 %, historique 15 %, question 70 % (`genericOpenAi/index.js:46-50`, explication `server/utils/helpers/chat/index.js:24-29`).
- `compressMessages` → `messageArrayCompressor` (`genericOpenAi/index.js:506-510`) : rien n'est compressé si l'ensemble + 600 tient dans la fenêtre (`chat/index.js:56-57`). Sinon :
  - question > 70 % : envoyée seule, tronquée par le milieu à 80 % de la fenêtre (`:67-78`) ;
  - système > 15 % : la consigne est ramenée à 25 % de la part système, le contexte documentaire à 75 % de la part système, par « cannonball » (suppression au milieu) (`:80-122`) ;
  - historique : paires les plus récentes jusqu'à 15 %, les 3 dernières éventuellement tronquées (`:130-190`).
- Avec 16 384 jetons : système 2 457, historique 2 457, question 11 468. Le contexte documentaire n'est comprimé que si le total dépasse 16 384 - 600.
- Comptage par `js-tiktoken`, encodage `cl100k_base` par défaut pour un modèle inconnu (`server/utils/helpers/tiktoken.js:37-43`) : estimation, pas le tokeniseur de Qwen.
- Contexte injecté dans le message système sous la forme `Context:` puis `[CONTEXT i]…[END CONTEXT i]` (`genericOpenAi/index.js:95-105`, `:177-188`).
- Historique : `openAiHistory` messages (20 par défaut) (`server/utils/chats/apiChatHandler.js:269`, `server/models/workspace.js:74-80`).
- Documents épinglés : injectés en entier, dans la limite de `promptWindowLimit()` jetons (estimation `token_count_estimate`) (`apiChatHandler.js:321-338`, `server/utils/DocumentManager/index.js:13`, `:60-68`).
- Complément par l'historique : si la recherche renvoie moins de `topN` extraits, des extraits cités aux tours précédents complètent le contexte (`fillSourceWindow`, `server/utils/helpers/chat/index.js:436-446`, appel `apiChatHandler.js:382-397`).

---

## 3. Embedder « Generic OpenAI » et découpage

Fichier : `server/utils/EmbeddingEngines/genericOpenAi/index.js`.

| Variable | Défaut | Preuve |
|---|---|---|
| `EMBEDDING_ENGINE='generic-openai'` | sinon `native` | `server/utils/helpers/index.js:348-352`, `:362-363` |
| `EMBEDDING_BASE_PATH` (obligatoire) | erreur si absent | `genericOpenAi/index.js:9-15` |
| `EMBEDDING_MODEL_PREF` | `null` | `genericOpenAi/index.js:20` |
| `GENERIC_OPEN_AI_EMBEDDING_API_KEY` | `null` | `genericOpenAi/index.js:16-19` |
| `EMBEDDING_MODEL_MAX_CHUNK_LENGTH` (en **caractères**) | 1000 | `server/utils/helpers/index.js:633-642` |
| `GENERIC_OPEN_AI_EMBEDDING_MAX_CONCURRENT_CHUNKS` (taille de lot par requête) | 500 | `genericOpenAi/index.js:70-78` |
| `GENERIC_OPEN_AI_EMBEDDING_API_DELAY_MS` (pause entre lots, min 500 ms) | aucune | `genericOpenAi/index.js:44-63` |
| `GENERIC_OPEN_AI_EMBEDDING_PASSAGE_PREFIX` / `_QUERY_PREFIX` | vides | `genericOpenAi/index.js:87-120` |

- Les lots sont envoyés **séquentiellement** (une requête `embeddings.create` par lot, pas de parallélisme) ; une erreur annule tout le document (`genericOpenAi/index.js:130-165`).
- Pas de paramètre `dimensions` : `EMBEDDING_OUTPUT_DIMENSIONS` n'est lu que par LocalAI (`server/utils/EmbeddingEngines/localAi/index.js:40-44`). La dimension (1024 pour bge-m3) est déduite des vecteurs.
- Changer `EmbeddingEngine` ou `EmbeddingModelPref` par `update-env` déclenche une remise à zéro des bases vectorielles (`updateENV.js:252-264`, `:1398-1413`).
- Validation `validDockerizedUrl` : refuse seulement une adresse de boucle locale injoignable ; un nom d'hôte comme `llm-central` passe (`updateENV.js:1366-1386`).

Embedder natif par défaut : `Xenova/all-MiniLM-L6-v2` (23 Mo, anglais, 1000 caractères, lots de 25) ; autres choix `Xenova/nomic-embed-text-v1`, `MintplexLabs/multilingual-e5-small` (`server/utils/EmbeddingEngines/native/constants.js:1-59`). Téléchargé au premier usage depuis Hugging Face via transformers.js, repli `https://cdn.anythingllm.com/support/models/`, cache `$STORAGE_DIR/models` (`server/utils/EmbeddingEngines/native/index.js:37-56`, `:140-176`).

Découpage (`server/utils/TextSplitter/index.js`) :
- `RecursiveCharacterTextSplitter` de LangChain, tailles en caractères (`:193-209`).
- Taille : réglage système `text_splitter_chunk_size` ; s'il est absent, on prend la limite de l'embedder (`EMBEDDING_MODEL_MAX_CHUNK_LENGTH`, donc 1000 par défaut, ou 8192 si on suit l'exemple `.env`) ; la valeur est plafonnée à cette limite (`server/utils/vectorDbProviders/lance/index.js:351-363`, `TextSplitter/index.js:47-56`, `server/endpoints/admin.js:389-391`).
- Chevauchement : `text_splitter_chunk_overlap`, 20 par défaut (`lance/index.js:357-360`, `server/models/systemSettings.js:138-150`).
- Un en-tête de métadonnées (titre, source, date) est préfixé à chaque extrait (`TextSplitter/index.js:63-80`, `:175-178`).
- Réglage par l'interface : page `/settings/text-splitter-preference` (`frontend/src/utils/paths.js:133`) ; par API interne : `POST /api/admin/system-preferences` avec `text_splitter_chunk_size` / `text_splitter_chunk_overlap` ; toute modification vide le cache de vecteurs (`server/models/systemSettings.js:123-150`).

---

## 4. Reranker

- **Pas de reranker externe** en 1.19.0 : aucune variable `RERANK*` ni appel à une route `/rerank` ; seul le dossier `server/utils/EmbeddingRerankers/native` existe. Les seules variables « reranker » concernent le tri des outils d'agent (`AGENT_SKILL_RERANKER_ENABLED`, `AGENT_SKILL_RERANKER_TOP_N`, `docker/.env.example:559-565`).
- Reranker natif : modèle cross-encoder `Xenova/ms-marco-MiniLM-L-6-v2` (ONNX, transformers.js) (`server/utils/EmbeddingRerankers/native/index.js:20-23`), téléchargé depuis `huggingface.co`, repli `https://cdn.anythingllm.com/support/models/`, cache `$STORAGE_DIR/models` (`:15-33`, `:45-52`). Lots de 10 (`:8`).
- Activation par espace de travail : champ `vectorSearchMode` = `"rerank"` (valeurs `default` | `rerank`) (`server/models/workspace.js:121-129`), lu par `rerank: workspace?.vectorSearchMode === "rerank"` (`server/utils/chats/apiChatHandler.js:361`). Interface : « Search Preference » → « Default » / « Accuracy Optimized », libellés en dur en anglais, affiché seulement pour LanceDB (`frontend/src/pages/WorkspaceSettings/VectorDatabase/VectorSearchMode/index.jsx:6-47`).
- Par API : `POST /api/v1/workspace/{slug}/update` avec `{"vectorSearchMode":"rerank"}` (`server/endpoints/api/workspace/index.js:279-345`, champ inscriptible `server/models/workspace.js:41-58`).
- Fonctionnement : recherche vectorielle de `max(10, min(50, ceil(10 % du nombre de vecteurs)))` candidats, rerank, garde `topN` ; le seuil `similarityThreshold` est appliqué sur la similarité cosinus, pas sur le score de rerank ; le score renvoyé est `rerank_score` (`server/utils/vectorDbProviders/lance/index.js:99-170`).
- Le tri d'outils d'agent utilise aussi ce reranker natif, activé par défaut, dès qu'il y a plus de 15 outils (`server/utils/agents/aibitat/utils/toolReranker.js:32-36`, `:126-133`) : téléchargement possible du modèle même sans rerank documentaire.

---

## 5. Transcription (STT) et synthèse vocale (TTS)

Deux mécanismes distincts.

**Transcription des fichiers audio/vidéo téléversés** (collecteur) — `WHISPER_PROVIDER` :
- `local` (défaut), `openai`, `generic-openai` (`collector/processSingleFile/convert/asAudio.js:15-31`, défaut `server/utils/collectorApi/index.js:67`).
- `openai` : modèle fixe `whisper-1`, clé `OPEN_AI_KEY`, **pas d'URL personnalisée** (`collector/utils/WhisperProviders/OpenAiWhisper.js:11`, `server/utils/collectorApi/index.js:69`).
- `generic-openai` : URL personnalisée `WHISPER_GENERIC_OPEN_AI_BASE_URL`, clé `WHISPER_GENERIC_OPEN_AI_API_KEY`, modèle `WHISPER_GENERIC_OPEN_AI_MODEL` (défaut `whisper-small`), `temperature: 0`, appel `audio.transcriptions.create` (donc `POST {base}/audio/transcriptions`) (`collector/utils/WhisperProviders/GenericOpenAiWhisper.js:4-37`, `docker/.env.example:366-370`). Convient pour `transcribe`.
- `local` : `Xenova/whisper-small` (≈250 Mo) par défaut, ou `Xenova/whisper-large` (`WHISPER_MODEL_PREF`), téléchargé depuis Hugging Face au premier usage (`collector/utils/WhisperProviders/localWhisper.js:4-20`, `:119-151`).

**Dictée dans la zone de chat** — `STT_PROVIDER` (`server/utils/SpeechToText/index.js:1-24`) :
- `native` (défaut, API vocale du navigateur, côté client) (`server/models/systemSettings.js:582`), `openai` (`STT_OPEN_AI_MODEL`, réutilise `OPEN_AI_KEY`), `lemonade`, `deepgram`, `generic-openai` (`STT_OPEN_AI_COMPATIBLE_ENDPOINT` obligatoire, `STT_OPEN_AI_COMPATIBLE_KEY`, `STT_OPEN_AI_COMPATIBLE_MODEL` défaut `whisper-1`, conversion en WAV avant envoi) (`server/utils/SpeechToText/openAiGeneric/index.js:4-50`), `groq` (`docker/.env.example:397-419`).
- Route serveur : `POST /api/system/transcribe-audio` (`server/endpoints/system.js:1546`).

**TTS** — `TTS_PROVIDER` :
- `native` (navigateur, défaut affiché `server/models/systemSettings.js:560`), `openai` (`TTS_OPEN_AI_KEY`, `TTS_OPEN_AI_VOICE_MODEL`), `generic-openai` (`TTS_OPEN_AI_COMPATIBLE_ENDPOINT`, `_KEY`, `_MODEL` défaut `tts-1`, `_VOICE_MODEL` défaut `alloy`), `elevenlabs` (`TTS_ELEVEN_LABS_KEY`, `TTS_ELEVEN_LABS_VOICE_MODEL`), `kokoro` (`TTS_KOKORO_ENDPOINT`, `_KEY`, `_VOICE_MODEL`) (`server/utils/TextToSpeech/index.js:1-19`, `server/utils/TextToSpeech/openAiGeneric/index.js:3-28`, `docker/.env.example:375-395`).
- Piper : exécuté dans le navigateur (`@mintplex-labs/piper-tts-web`), voix `TTS_PIPER_VOICE_MODEL` défaut `en_US-hfc_female-medium` (`frontend/src/utils/piperTTS/worker.js:1`, `server/models/systemSettings.js:567-569`).
- Pages : `/settings/transcription-preference` et `/settings/audio-preference` (`frontend/src/utils/paths.js:122-126`).

---

## 6. Base vectorielle

- LanceDB par défaut (`docker/HOW_TO_USE_DOCKER.md:16`, `VECTOR_DB="lancedb"` `docker/.env.example:302-303`), dossier `$STORAGE_DIR/lancedb` (`server/utils/vectorDbProviders/lance/index.js:25-29`).
- Recherche cosinus, `limit(topN)`, filtrage par `similarityThreshold` (défaut 0,25), score = similarité (`lance/index.js:183-224`).
- Autres emplacements dans `$STORAGE_DIR` : `documents`, `direct-uploads`, `vector-cache` (`server/utils/files/index.js:10-18`), `models` (embedder, reranker, whisper, `pricing`, `tesseract`), `plugins` (MCP).

---

## 7. Télémétrie et connexions sortantes

- Télémétrie PostHog (bibliothèque `posthog-node`, clé publique `phc_9qu7…` en dur, hôte par défaut de la bibliothèque) (`server/models/telemetry.js:11`, `:49-53`). Désactivée si `DISABLE_TELEMETRY === "true"` (chaîne exacte) (`:50`, `server/utils/telemetry/index.js:8-14`). Sinon, événement `server_boot` au démarrage (`server/utils/telemetry/index.js:26-29`) puis événements d'usage (`sent_chat`, `workspace_created`…).
- Piège : désactiver la télémétrie depuis l'interface (`update-env` `DisableTelemetry=true`) envoie d'abord un événement `telemetry_disabled` (`server/utils/helpers/updateENV.js:622-629`). La fixer dans l'environnement avant le premier démarrage évite tout envoi.
- **Tarifs des modèles** : au démarrage, téléchargement de `https://models.dev/api.json` (délai 5 s, cache 3 jours dans `$STORAGE_DIR/models/pricing`), **sans variable pour le couper** (`server/index.js:7`, `server/utils/helpers/modelPricing/index.js:69-71`, `:171-191`, `:403`). Échec sans conséquence (journal « Background pricing refresh failed »).
- Téléchargements de modèles à la demande : embedder natif, reranker natif, whisper local (Hugging Face + repli `cdn.anythingllm.com`) — voir §3, §4, §5. Rien au démarrage tant qu'ils ne servent pas.
- OCR (PDF scannés) : `tesseract.js` avec cache `$STORAGE_DIR/models/tesseract`, sans `langPath` fixé (`collector/utils/OCRLoader/index.js:25-29`, `:111-122`) ; les données de langue viennent donc de l'emplacement par défaut de tesseract.js (déduction, non vérifiée).
- Agent : compétence `web-browsing` activée par défaut (`server/utils/agents/defaults.js:10-15`) ; sans moteur configuré, recherche via You.com sans clé, repli DuckDuckGo (`server/utils/agents/aibitat/plugins/web-browsing.js:66-128`, `:1140`).
- Hub communautaire : `https://hub.external.anythingllm.com/v1` (seulement si utilisé) (`server/models/communityHub.js:11`).
- Questionnaire d'accueil : envoyé depuis le navigateur vers `https://onboarding.anythingllm.com` seulement si un champ est rempli (`frontend/src/utils/constants.js:2`, `frontend/src/pages/OnboardingFlow/Steps/Survey/index.jsx:12-42`, `:60-78`).
- Pas de vérification de version trouvée dans le code serveur ni frontend.
- Tâches de fond au démarrage (locales) : nettoyages, synchronisation des documents surveillés (1 h), extraction de mémoires si activée (`server/utils/BackgroundWorkers/index.js:29-60`, `:106-139`).

---

## 8. API développeur

- Préfixe : `/api/v1/…` (routeur monté sur `/api` `server/index.js:98`, routes `/v1/...` dans `server/endpoints/api/*`). Authentification : `Authorization: Bearer <clé API>` (`server/utils/middleware/validApiKey.js:8-22`).
- Swagger : `/api/docs` (`server/swagger/utils.js:18-38`), sauf `DISABLE_SWAGGER_DOCS="true"`.

Points d'entrée utiles :
| Besoin | Route | Preuve |
|---|---|---|
| Vérifier la clé | `GET /api/v1/auth` | `server/endpoints/api/auth/index.js:6` |
| Créer un espace | `POST /api/v1/workspace/new` (`name` + champs optionnels) | `server/endpoints/api/workspace/index.js:28-106` |
| Lister / lire | `GET /api/v1/workspaces`, `GET /api/v1/workspace/{slug}` | `:109`, `:163` |
| Téléverser | `POST /api/v1/document/upload` (multipart, champ `file`, option `addToWorkspaces="slug1,slug2"`, `metadata` JSON) ; réponse `documents[].location` | `server/endpoints/api/document/index.js:50-125` |
| Autres entrées | `/v1/document/upload/{folderName}`, `/v1/document/upload-link`, `/v1/document/raw-text`, `/v1/documents` | `document/index.js:181`, `:335`, `:517`, `:665` |
| Intégrer | `POST /api/v1/workspace/{slug}/update-embeddings` `{"adds":["custom-documents/x.json"],"deletes":[]}` | `workspace/index.js:457-532` |
| Épingler | `POST /api/v1/workspace/{slug}/update-pin` `{"docPath":…,"pinStatus":true}` | `workspace/index.js:534-601` |
| Régler | `POST /api/v1/workspace/{slug}/update` | `workspace/index.js:279-358` |
| Chat | `POST /api/v1/workspace/{slug}/chat` ; aussi `stream-chat`, `vector-search`, fils `thread/...` | `workspace/index.js:603-735`, `:737`, `:899`, `server/endpoints/api/workspaceThread/index.js` |
| Compatible OpenAI | `/api/v1/openai/models`, `/chat/completions`, `/embeddings`, `/vector_stores` | `server/endpoints/api/openai/index.js:19-358` |
| Réglages système | `GET /api/v1/system`, `POST /api/v1/system/update-env` | `server/endpoints/api/system/index.js:39`, `:108-156` |

Champs inscriptibles d'un espace et validation (`server/models/workspace.js:41-138`) : `name`, `openAiTemp` (null par défaut, ≥ 0), `openAiHistory` (20), `openAiPrompt`, `similarityThreshold` (0,25, borné 0-1), `topN` (4, ≥ 1), `chatMode` (`chat` | `query` | `automatic`, défaut `automatic`), `chatProvider`, `chatModel`, `agentProvider`, `agentModel`, `queryRefusalResponse`, `vectorSearchMode` (`default` | `rerank`), `router_id`.

**Mode par défaut `automatic`** : `Workspace.new` force `chatMode: "automatic"` (`server/models/workspace.js:220-226`) malgré le défaut `"chat"` du schéma (`server/prisma/schema.prisma:136`). En `automatic`, si le fournisseur sait appeler des outils nativement, toute question part en **agent** (`server/utils/agents/ephemeral.js:633-645`, `server/utils/chats/agents.js:68-71`) ; c'est le cas de `generic-openai` sauf `PROVIDER_DISABLE_NATIVE_TOOL_CALLING=generic-openai` (`server/utils/agents/aibitat/providers/ai-provider.js:217-234`, `providers/genericOpenAi.js:28`). Pour un banc RAG reproductible, fixer `mode: "query"` ou `"chat"` dans chaque requête, ou `chatMode` sur l'espace.

Requête de chat : `{"message", "mode": "automatic|query|chat", "sessionId", "attachments", "reset"}` ; mode absent → `workspace.chatMode` (`server/endpoints/api/workspace/index.js:659-700`, mode résolu `:682-684`).
- `query` : pas d'appel au LLM si aucun extrait ; réponse `queryRefusalResponse` ou « There is no relevant information in this workspace to answer your query. » (`server/utils/chats/apiChatHandler.js:273-305`, `:400-432`). Malgré la description Swagger, l'historique est chargé dans les deux modes (`apiChatHandler.js:313-319`).

Réponse (`apiChatHandler.js:489-498`) : `{id, type:"textResponse"|"abort", close, error, chatId, textResponse, sources, metrics}`.
- `textResponse` peut commencer par `<think>…</think>` (§2.3).
- `sources[]` = métadonnées du document + `text` (extrait) + `score` (`server/utils/vectorDbProviders/lance/index.js:216-219`, `:459-462`, `:503-517`) : `id`, `url`, `title`, `docAuthor`, `description`, `docSource`, `chunkSource`, `published`, `wordCount`, `token_count_estimate`, `text`, `score` (champs du document : `collector/processSingleFile/convert/asPDF/index.js:56-73`). **Aucun numéro de page** : les pages d'un PDF sont concaténées avant découpage (`asPDF/index.js:35-55`). Les documents épinglés figurent avec `text` tronqué à 1000 caractères (`apiChatHandler.js:331-336`).
- En mode agent : champs supplémentaires `thoughts`, `outputs` et `sources` = citations de l'agent (`apiChatHandler.js:244-254`).

Clé API :
- Mono-utilisateur (sans compte) : `POST /api/system/generate-api-key` (interface `/settings/api-keys`), refusé en multi-utilisateur (`server/endpoints/system.js:1063-1090`, `frontend/src/utils/paths.js:159-160`). Aucun compte n'est requis ; avec mot de passe, il faut le jeton de session (`POST /api/request-token`).
- Multi-utilisateur : `POST /api/admin/generate-api-key`, administrateur seulement (`server/endpoints/admin.js:524-526`).
- Création : `ApiKey.create` / `makeSecret()` (`server/models/apiKeys.js:7`, `:12-21`).

Administration (API v1) : `GET/POST /api/v1/admin/users`, `/users/new`, `/users/{id}`, invitations, `/workspaces/{id}/update-users`, `/workspace-chats`, `/preferences` (`server/endpoints/api/admin/index.js:15-735`). La création d'utilisateurs renvoie 401 tant que le multi-utilisateur n'est pas activé (`server/endpoints/api/admin/index.js:85`, test `:129-131`).

---

## 9. Compte initial, modes, endpoints internes

- Onboarding (interface) : étapes `home`, `llm-preference`, `user-setup`, `data-handling`, `survey` (`frontend/src/pages/OnboardingFlow/Steps/index.jsx:12-16`). `user-setup` propose « seul » (mot de passe facultatif) ou « équipe » (création de l'administrateur) (`frontend/src/pages/OnboardingFlow/Steps/UserSetup/index.jsx:17-53`, `:122-172`).
- Mono-utilisateur sans mot de passe : aucune authentification (`server/utils/middleware/validatedRequest.js:15-23`).
- Mono-utilisateur avec mot de passe : `POST /api/system/update-password` `{"usePassword":true,"newPassword":"…"}` → écrit `AUTH_TOKEN` et un nouveau `JWT_SECRET` (`server/endpoints/system.js:618-661`) ; connexion `POST /api/request-token` `{"password"}` (`:204`, `:319-325`).
- Multi-utilisateur : `POST /api/system/enable-multi-user` `{"username","password"}` crée l'administrateur, bascule `multi_user_mode`, irréversible par l'API (`server/endpoints/system.js:664-724`) ; connexion `POST /api/request-token` `{"username","password"}` qui renvoie aussi des codes de récupération à la première connexion (`:204-317`).
- Réglage des fournisseurs par script : `POST /api/system/update-env` (rôle admin ou accès libre en mono-utilisateur sans mot de passe) avec les noms de champs `KEY_MAPPING` (`server/endpoints/system.js:599-616`, `server/utils/helpers/updateENV.js:4-…`), ou `POST /api/v1/system/update-env` avec clé API (`server/endpoints/api/system/index.js:108-156`). Exemple de corps : `{"LLMProvider":"generic-openai","GenericOpenAiBasePath":"http://llm-central:8080/v1","GenericOpenAiModelPref":"chat","GenericOpenAiTokenLimit":16384,"GenericOpenAiKey":"…","GenericOpenAiMaxTokens":…,"EmbeddingEngine":"generic-openai","EmbeddingBasePath":"http://llm-central:8080/v1","EmbeddingModelPref":"embed","GenericOpenAiEmbeddingApiKey":"…","EmbeddingModelMaxChunkLength":…,"WhisperProvider":"generic-openai","WhisperGenericOpenAiBaseUrl":"http://llm-central:8080/v1","WhisperGenericOpenAiModel":"transcribe","WhisperGenericOpenAiApiKey":"…"}` (clés : `updateENV.js:209-228`, `:252-300`, `:587-611`).
- Autres routes internes : `GET /api/onboarding`, `POST /api/onboarding` (marque l'accueil terminé), `GET /api/setup-complete` (réglages publics, secrets en booléens), `GET /api/system/multi-user-mode` (`server/endpoints/system.js:101-131`, `:726-734`). L'accueil est réputé terminé dès que `LLM_PROVIDER`, `VECTOR_DB`, `AUTH_TOKEN` ou `JWT_SECRET` est défini (`server/utils/boot/markOnboarded.js:37-49`, notamment `:39` et `:45`) : fixer les fournisseurs par l'environnement saute l'assistant.
- Réglages système (taille d'extrait, compétences d'agent désactivées…) : `POST /api/admin/system-preferences` (`server/endpoints/admin.js:466-…`).

---

## 10. Langue de l'interface

- Français disponible : `frontend/src/locales/fr/common.js` (2103 lignes contre 2050 pour l'anglais), déclaré dans `frontend/src/locales/resources.js:20`, `:67-68`.
- Choix : détection automatique par `i18next-browser-languagedetector` (langue du navigateur, mémorisée dans le navigateur), repli `en` (`frontend/src/i18n.js:6-19`). Changement manuel : page `/settings/interface`, « Langue d'affichage » (`frontend/src/pages/GeneralSettings/Settings/Interface/index.jsx:4`, `frontend/src/locales/fr/common.js:1433-1436`, `frontend/src/hooks/useLanguageOptions.js:9-12`). Également dans la fenêtre de compte (`frontend/src/components/UserMenu/AccountModal/index.jsx`).
- Certaines chaînes restent en anglais en dur (ex. « Search Preference », « Accuracy Optimized ») (`frontend/src/pages/WorkspaceSettings/VectorDatabase/VectorSearchMode/index.jsx:30-47`).

---

## 11. Fonctions présentes en 1.19.0

| Fonction | Existe | Preuve |
|---|---|---|
| Agents `@agent` | Oui ; en mode `automatic` sans `@agent` si appel d'outils natif | `server/utils/agents/defaults.js:63`, `server/models/workspace.js:666-708`, `:719-722` |
| Compétences intégrées | Actives par défaut : `rag-memory`, résumé de document, `web-scraping`, `web-browsing` ; configurables : SQL, système de fichiers, création de fichiers, graphiques (`rechart`), génération d'image, Gmail, Outlook, Google Agenda, demande de précision, création de tâche planifiée (mono-utilisateur seulement) | `server/utils/agents/defaults.js:10-18`, `server/utils/agents/aibitat/plugins/index.js:1-55` |
| Agent flows | Oui (sauvegarde, liste, suppression ; exécution directe commentée) | `server/endpoints/agentFlows.js:14-139`, `server/utils/agentFlows/` |
| MCP | Oui ; fichier `$STORAGE_DIR/plugins/anythingllm_mcp_servers.json` (créé vide `{ "mcpServers": {} }`) ; `uvx` présent dans l'image | `server/utils/MCP/hypervisor/index.js:67-85`, `docker/Dockerfile:105-109` |
| Mémoires | Oui, **désactivées par défaut** (`memory_enabled` doit valoir `"true"`) ; extraction automatique en tâche de fond | `server/models/systemSettings.js:773-791`, `server/endpoints/memory.js:45-146`, `server/utils/BackgroundWorkers/index.js:47-52` |
| Tâches planifiées | Oui (`/settings/scheduled-jobs`, concurrence `SCHEDULED_JOB_MAX_CONCURRENT`=1) | `server/endpoints/scheduledJobs.js:19-142`, `server/models/scheduledJob.js`, `server/utils/BackgroundWorkers/index.js:20-22` |
| Routage de modèles | Oui (« model routers », règles, champ `router_id` de l'espace) | `server/endpoints/modelRouter.js:16-163`, `server/utils/router/index.js`, `server/utils/AiProviders/modelRouter/` |
| Widget intégrable | Oui (script `anythingllm-chat-widget.min.js`, routes publiques `/api/embed`, gestion `/api/v1/embed`) ; le sous-module `embed/` est vide dans le clone, le script compilé est dans `frontend/public/embed/` | `server/index.js:70-74`, `server/endpoints/api/embed/index.js:10-357`, `frontend/public/embed/`, `.gitmodules` |
| Connecteurs | GitHub, GitLab, Gitea, YouTube (transcription), site web en profondeur, Confluence, DrupalWiki, coffre Obsidian, Paperless-ngx, resynchronisation | `collector/extensions/index.js:16-222`, `collector/utils/extensions/RepoLoader/{GithubRepo,GitlabRepo,GiteaRepo}` |
| Mode chat / query | Oui, plus `automatic` (défaut) | `server/models/workspace.js:36`, `server/utils/chats/stream.js:22` |
| Épinglage de documents | Oui (document entier injecté) | `server/endpoints/api/workspace/index.js:534-601`, `server/utils/DocumentManager/index.js:10-68` |
| Rerank externe | **Non** | §4 |

---

## Écarts relevés entre documentation et code

- `docker/.env.example:568` annonce `MEMORY_EXTRACTION_INTERVAL` à 15 min par défaut ; le code utilise `3hr` (`server/utils/BackgroundWorkers/index.js:50`).
- Description Swagger du mode `query` (« does not recall chat history », `server/endpoints/api/workspace/index.js:611`) : le code charge l'historique quel que soit le mode (`server/utils/chats/apiChatHandler.js:313-319`).
- Défaut de `chatMode` : `"chat"` dans le schéma Prisma, `"automatic"` à la création (`server/prisma/schema.prisma:136` contre `server/models/workspace.js:224`).
