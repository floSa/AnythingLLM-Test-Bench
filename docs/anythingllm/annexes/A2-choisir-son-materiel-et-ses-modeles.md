# A2. Choisir son matériel et ses modèles

> **Objet** : dire quelle machine faire tourner AnythingLLM et son service de modèles, sans et avec carte graphique NVIDIA, quelle place prend chaque élément, combien de documents passent et combien de temps attendre.
> **Prérequis** : [chapitre 01](../manuel/01-decouvrir-anythingllm.md) ; annexe [A1](A1-evaluation-qualite-et-performances.md) pour les résultats du banc.
> **Version décrite** : AnythingLLM 1.19.0 ; service LLM central (LiteLLM v1.109.0, llama-swap v272, llama.cpp build 12282, speaches 0.8.3) ; essais du 12 novembre 2026.
> **Statut des informations** : [Vérifié] mesuré sur la machine d'essai (profil B) ; [Source] repris des mesures de LLM-Service, fichier cité ; [Estimation] calcul expliqué ; [À tester] non mesuré.
> **Précautions** : le profil A (sans carte graphique) n'a pas été mesuré avec AnythingLLM ; ses temps sont des estimations à partir des mesures du service central.

## Sommaire

1. [Ce qui consomme la mémoire](#1-ce-qui-consomme-la-mémoire)
2. [Profil A : sans carte graphique](#2-profil-a--sans-carte-graphique)
3. [Profil B : avec carte graphique NVIDIA](#3-profil-b--avec-carte-graphique-nvidia)
4. [Budget de contexte et volume de documents](#4-budget-de-contexte-et-volume-de-documents)
5. [Modèles](#5-modèles)
6. [Dépannage](#dépannage)
7. [Sources](#sources)

## 1. Ce qui consomme la mémoire

| Élément | Mémoire | Statut |
|---|---|---|
| AnythingLLM au repos | 390 à 600 Mio | [Vérifié] (`installation-2026-11-12.log`, `etat.sh`) |
| AnythingLLM pendant le banc, embedding par le service | 887 Mio | [Vérifié] (`banc-2026-11-12-defaut-sans-rerank.json`) |
| AnythingLLM avec le tri de précision chargé | environ 1,56 Gio (le petit modèle reste en mémoire) | [Vérifié] (`banc-2026-11-12-rerank-natif.json`) |
| Service central, profil `cpu` : LiteLLM, llama-swap, speaches | 0,59 + 3,6 + 0,13 Gio ≈ 4,3 Go | [Source] (`LLM-Service/mesures/cpu/memoire-vive-conteneurs.txt`) |
| Service central, profil `gpu` : mémoire vive | LiteLLM 0,8, llama-swap 4,4, speaches 0,2 à 1,5 Go | [Source] (`LLM-Service/README.md`, « Mesures ») |
| Service central, profil `gpu` : carte graphique | 7,0 Go pour `chat`, `embed` et `rerank` ; 8,1 Go relevés en fin de banc avec le bureau Windows | [Source] [Vérifié] |

Le volume de documents ne change presque pas la mémoire : les vecteurs sont sur disque (LanceDB) et seuls quelques passages partent au modèle.

## 2. Profil A : sans carte graphique

Machine type : PC portable Intel Core Ultra 7 255H, 15,3 Go dans WSL ; service en profil `cpu` (`demarrer.sh cpu`).

| Élément | Valeur | Statut |
|---|---|---|
| Processeur | 8 cœurs récents (AVX2) | [Estimation] (profil A du banc) |
| Mémoire vive | 16 Go : 4,3 Go service, 0,9 à 1,6 Go AnythingLLM, le reste pour Windows, WSL et Docker | [Estimation] (somme des lignes de la section 1) |
| Disque | 15 Go : image AnythingLLM 3,4 Go, modèles du service environ 5 Go, données | [Estimation] |
| Débit de `chat` | 14 jetons/s pour une requête, 31 jetons/s cumulés pour quatre | [Source] (`LLM-Service/README.md`) |
| Réflexion sur une question de calcul | environ 2 minutes | [Source] (idem) |
| Temps de réponse attendu | environ 5 fois le profil B : 1 à 2 minutes par question, réflexion comprise | [Estimation] (68 / 14 ≈ 4,9 appliqué à la médiane de 11 à 14 s du profil B) |
| Indexation des 9 documents | 10 à 20 s (embedding 0,08 s pour 10 passages contre 0,05 s ; OCR et transcription sur le processeur) | [Estimation] |

| Profil A | Valeur |
|---|---|
| Profil du service | `cpu` (`llm-swap-cpu`) |
| Modèles | `chat` = Qwen3.5-4B Q4_K_M, `embed` = bge-m3 Q8_0, `rerank` = bge-reranker-v2-m3 (non utilisé par AnythingLLM), `transcribe` = faster-whisper-small |
| Contexte | 16 384 jetons |
| Mémoire service et application | 4,3 Go + 0,9 à 1,6 Go [Estimation] |
| Réglages conseillés | 4 passages, « Max Tokens » 8192, historique 20 ; tri de précision possible (calculé sur le processeur, 0,25 s pour 10 passages) |
| Résultats du banc | non mesurés sur ce profil ; la qualité ne dépend pas du matériel (mêmes modèles) [Estimation] |
| Temps d'attente | 1 à 2 minutes par réponse [Estimation] |

## 3. Profil B : avec carte graphique NVIDIA

Machine d'essai : Ryzen 5 9600X, 32 Go dans WSL, RTX 4060 Ti 16 Go, pilote 616.92 ; service en profil `gpu`. [Vérifié] (`outils/resultats/machine/diagnostic-2026-11-12.json`)

| Profil B | Valeur | Statut |
|---|---|---|
| Profil du service | `gpu` (`llm-swap`) | [Vérifié] |
| Modèles | mêmes que le profil A | [Vérifié] (`/v1/models`) |
| Contexte | 16 384 jetons | [Vérifié] |
| Carte graphique | 8 Go minimum (7,0 Go pour les trois modèles permanents) | [Source] |
| Mémoire vive | 16 Go : 5,4 Go service, 0,9 à 1,6 Go AnythingLLM | [Source] [Vérifié] |
| Débit de `chat` | 68 jetons/s pour une requête, 174 jetons/s cumulés pour quatre | [Source] |
| Réglages | embedder `embed`, mode « Requête », 4 ou 8 passages, avec ou sans tri de précision | [Vérifié] |
| Résultats du banc | 33/34 à 34/34 justes, 3/4 à 4/4 refus | [Vérifié] (A1) |
| Temps d'attente | médiane 10,7 à 14,3 s, p95 28 à 50 s ; indexation des 9 documents 8,5 s | [Vérifié] |

## 4. Budget de contexte et volume de documents

AnythingLLM partage la fenêtre de 16 384 jetons en consigne et passages (15 %, 2 457 jetons), historique (15 %) et question (70 %), avec 600 jetons de marge ; le plafond de réponse (« Max Tokens ») n'est pas retranché. [Source] (annexe A5, section 7)

| Réglage | Passages | Jetons de passages | Place restante dans la part « consigne et passages » |
|---|---|---|---|
| 4 passages de 1 000 caractères | 4 | environ 1 200 | environ 1 000 [Estimation] (≈ 300 jetons par passage) |
| 8 passages | 8 | environ 2 400 | presque pleine : au-delà, AnythingLLM coupe le milieu [Estimation] |
| document épinglé | entier | taille du document | un document de plus de 2 000 jetons fait réduire les autres [Estimation] |

Le nombre de documents d'un espace n'est pas limité par le contexte : seuls les passages retrouvés partent au modèle. La limite vient de la question elle-même : le modèle `embed` refuse une question de plus de 8 192 jetons (« input (20418 tokens) is too large to process », message de 81 667 caractères). [Vérifié] (`outils/resultats/anythingllm/contexte-2026-11-12.txt`)

## 5. Modèles

- Les modèles sont ceux du service central, noms fixes `chat`, `embed`, `transcribe` ; `rerank` est disponible mais AnythingLLM ne sait pas l'utiliser (annexe A1, section 4). [Vérifié]
- Un modèle plus léger, pour situer un plancher de qualité, relève de LLM-Service : proposition inscrite dans les décisions en attente du [journal](../../../JOURNAL.md#décisions-en-attente).
- La réflexion de `chat` ne peut pas être coupée depuis AnythingLLM (fournisseur Generic OpenAI sans paramètre de réflexion) ; le levier serait côté service. [Source]
- Un second modèle de réponse est exposé sans modification du service : `gemma-4-e4b` (chargé à la demande, environ 5,3 Go de carte graphique en plus). Il se choisit par espace (chapitre 08) ; non passé au banc. [À tester]

## Dépannage

| Symptôme | Cause probable | Action |
|---|---|---|
| WSL ralentit fortement | moins de 2 Go de mémoire libre | arrêter les autres applications du banc ; vérifier `free -m` |
| Réponses de plusieurs minutes | profil `cpu` et longue réflexion | normal sur processeur ; préférer des questions précises |
| Question refusée avec « too large to process » | question de plus de 8 192 jetons | envoyer le texte comme document |

## Sources

- LLM-Service, `README.md` section « Mesures » et dossiers `mesures/cpu`, `mesures/gpu` (commit `8568e75`, 12 novembre 2026).
- Bancs : `outils/resultats/anythingllm/banc-2026-11-12-*.json`.
- Diagnostic : `outils/resultats/machine/diagnostic-2026-11-12.json`.
