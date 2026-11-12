# A3. Automatiser par l'API

> **Objet** : piloter AnythingLLM par programme : vérifier une clé, lister et créer des espaces, envoyer et intégrer un document, poser une question, chercher des passages sans le modèle, utiliser la route compatible OpenAI.
> **Prérequis** : une clé d'API créée dans l'interface ([chapitre 12](../manuel/12-personnaliser-et-administrer.md), étapes 8 à 10) ; Python 3 (bibliothèque standard seulement) ou `curl`.
> **Version décrite** : AnythingLLM 1.19.0, API développeur `/api/v1`, essais du 12 novembre 2026.
> **Statut des informations** : [Vérifié] exécuté, sortie dans `exemples/anythingllm/sorties_verifiees.txt` ; [Source] lu dans le code ou la documentation Swagger ; [Estimation] ; [À tester] non essayé.
> **Précautions** : la clé d'API donne accès à tout ; elle se lit dans `donnees/anythingllm/cle-api.txt` ou la variable `ANYTHINGLLM_API_KEY`, jamais dans un fichier versionné.

## Sommaire

1. [Principe](#1-principe)
2. [Exemples exécutés](#2-exemples-exécutés)
3. [Routes utiles](#3-routes-utiles)
4. [Points d'attention](#4-points-dattention)
5. [Dépannage](#dépannage)
6. [Sources](#sources)

## 1. Principe

- Adresse : `http://127.0.0.1:3001/api/v1/…` ; en-tête `Authorization: Bearer <clé>`. [Vérifié]
- Documentation interactive : `http://127.0.0.1:3001/api/docs` (chapitre 12, étape 15). [Vérifié]
- La clé reste valable après le passage en multi-utilisateur : les exemples ont été exécutés en multi-utilisateur avec une clé créée en mode « Juste moi ». [Vérifié]

## 2. Exemples exécutés

Dossier `exemples/anythingllm/`, lancés par `exemples/anythingllm/lancer.sh` [Testée] ; chaque sortie réelle est dans `sorties_verifiees.txt`.

| Exemple | Ce qu'il fait | Résultat obtenu |
|---|---|---|
| `01_sante.sh` | `/api/ping`, `/api/v1/auth` avec la clé, puis avec une fausse clé | `{"online":true}`, `{"authenticated":true}`, `403` [Vérifié] |
| `02_lister_les_espaces.py` | `GET /workspaces` : mode, `topN`, seuil, recherche, historique | 5 espaces, dont « mon-espace-de-travail » en mode `automatic` (Agent) [Vérifié] |
| `03_creer_et_alimenter.py` | `POST /workspace/new` en mode `query`, puis `POST /document/upload` avec `addToWorkspaces` | espace `exemple-api` créé, `faq-sav.html` (104 mots) intégré dans l'espace en un appel [Vérifié] |
| `04_poser_une_question.py` | `POST /workspace/exemple-api/chat`, mode `query` | « le cadre de vélo Vélanor est garanti pendant 7 ans », source `faq-sav.html` score 0,746, 18,2 s ; la réflexion `<think>` est en tête de `textResponse` [Vérifié] |
| `05_recherche_seule.py` | `POST /workspace/exemple-api/vector-search` | passage de `faq-sav.html`, score 0,591, sans appel au modèle de réponse [Vérifié] |
| `06_compatible_openai.py` | `GET /openai/models`, `POST /openai/chat/completions` avec le nom court de l'espace comme modèle | liste des espaces comme « modèles » ; « La garantie de la batterie est de 2 ans. » [Vérifié] |
| `07_nettoyer.py` | `DELETE /workspace/exemple-api` | code 200 ; espace supprimé, fichier gardé dans « Mes documents » [Vérifié] |

Exemple minimal avec `curl` [Testée] (`01_sante.sh`) :

```bash
CLE=$(cat donnees/anythingllm/cle-api.txt)
curl -s -H "Authorization: Bearer $CLE" http://127.0.0.1:3001/api/v1/auth
```

Le client plus complet utilisé par le banc et les scripts est `outils/anythingllm/client.py` (création de la clé par l'API interne de l'interface si elle manque, envoi multipart, retrait de la réflexion). [Vérifié]

## 3. Routes utiles

| Besoin | Route | Statut |
|---|---|---|
| Vérifier la clé | `GET /api/v1/auth` | [Vérifié] |
| Lister, lire un espace | `GET /api/v1/workspaces`, `GET /api/v1/workspace/{slug}` | [Vérifié] |
| Créer, régler, supprimer | `POST /workspace/new`, `POST /workspace/{slug}/update` (`chatMode`, `topN`, `similarityThreshold`, `vectorSearchMode`, `openAiHistory`, `openAiPrompt`, `queryRefusalResponse`), `DELETE /workspace/{slug}` | [Vérifié] (banc et exemples) |
| Envoyer un document | `POST /document/upload` (multipart `file`, option `addToWorkspaces`) | [Vérifié] |
| Intégrer ou retirer | `POST /workspace/{slug}/update-embeddings` (`adds`, `deletes`) | [Source] |
| Épingler | `POST /workspace/{slug}/update-pin` | [Source] |
| Poser une question | `POST /workspace/{slug}/chat` (`message`, `mode` : `query`, `chat` ou `automatic`, `sessionId`) ; `stream-chat` en flux | [Vérifié] |
| Chercher sans le modèle | `POST /workspace/{slug}/vector-search` | [Vérifié] |
| Compatible OpenAI | `/api/v1/openai/models`, `/chat/completions`, `/embeddings` | [Vérifié] (deux premières) |
| Documents | `GET /documents`, `DELETE /system/remove-documents`, `DELETE /document/remove-folder` | [Vérifié] (`nettoyer_documents.py`) |
| Widgets | `GET /embed` | [Vérifié] |
| Réglages de l'instance | `GET /system`, `POST /system/update-env` | [Vérifié] (lecture) [Source] (écriture) |
| Administration (multi-utilisateur) | `/admin/users`, `/admin/invites`, `/admin/workspace-chats` | [Source] |

## 4. Points d'attention

- **Réflexion dans la réponse** : `textResponse` commence par `<think>…</think>` ; la retirer avant affichage (`client.sans_pensee`). [Vérifié]
- **Mode** : un espace créé sans `chatMode` est en `automatic` (Agent) ; préciser `mode` à chaque question ou `chatMode` à la création. [Vérifié]
- **Sources** : chaque source donne `title`, `text` (avec un en-tête `<document_metadata>`), `score` et, avec le tri de précision, `rerank_score` ; pas de numéro de page. [Vérifié]
- **Historique** : un même `sessionId` garde l'historique entre deux appels ; une session neuve par question pour des réponses indépendantes. [Source]
- **Questions longues** : au-delà de 8 192 jetons, l'embedding de la question échoue (erreur 500). [Vérifié] (`contexte-2026-11-12.txt`)

## Dépannage

| Symptôme | Cause probable | Action |
|---|---|---|
| `403` sur toutes les routes | clé fausse ou supprimée | créer une nouvelle clé (chapitre 12) |
| `textResponse` vide | mode `automatic` ou réflexion qui atteint le plafond | `mode: "query"` ; « Max Tokens » 8192 |
| `500` « too large to process » | question trop longue pour l'embedding | envoyer le texte comme document |

## Sources

- Documentation Swagger servie par l'instance : `http://127.0.0.1:3001/api/docs`.
- Code : `server/endpoints/api/` au tag `v1.19.0` ; relevé `outils/resultats/anythingllm/cadrage-serveur.md`, section 8.
- Sorties : `exemples/anythingllm/sorties_verifiees.txt`.
