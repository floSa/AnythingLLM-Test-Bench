# A1. Évaluation : qualité et performances

> **Objet** : mesurer la justesse des réponses, les citations, le refus sur les questions pièges, les temps de réponse et la mémoire d'AnythingLLM 1.19.0, et l'effet des réglages (embedder, tri de précision, nombre de passages).
> **Prérequis** : installation et modèles déclarés ([chapitres 02 et 03](../manuel/03-premiers-pas.md)) ; service LLM central en marche.
> **Version décrite** : AnythingLLM 1.19.0, modèles `chat` (Qwen3.5-4B, réflexion activée) et `embed` (bge-m3) du service LLM central, profil carte graphique ; essais du 12 novembre 2026.
> **Statut des informations** : [Vérifié] mesuré par le banc, fichiers JSON liés ; [Source] lu dans le code ; [Estimation] calcul expliqué ; [À tester] non mesuré.
> **Précautions** : 38 questions sur un corpus fictif de 9 documents : un ordre de grandeur, pas une garantie sur d'autres documents.

## Sommaire

1. [Méthode](#1-méthode)
2. [Résultats](#2-résultats)
3. [Ce qui change le résultat](#3-ce-qui-change-le-résultat)
4. [Reranker : ce que la solution accepte](#4-reranker--ce-que-la-solution-accepte)
5. [Questions manquées](#5-questions-manquées)
6. [Temps et mémoire](#6-temps-et-mémoire)
7. [Préconisations](#7-préconisations)
8. [Dépannage](#dépannage)
9. [Sources](#sources)

## 1. Méthode

- Banc commun `outils/communs/banc/commun.py`, adaptateur `outils/anythingllm/banc.py` (API développeur). [Vérifié]
- Corpus `corpus/documents/` (9 fichiers : PDF texte avec tableaux, PDF scanné, DOCX, PPTX, XLSX, HTML, Markdown, PDF en anglais, MP3), questions `corpus/questions.json` (34 avec réponse attendue, 4 pièges sans réponse). [Vérifié]
- Un espace « Banc-… » par embedder ; documents envoyés avec `addToWorkspaces` ; mode `query` ; une session neuve par question (pas d'historique). Le raisonnement `<think>…</think>` est retiré avant notation. [Vérifié]
- Exactitude : présence des éléments attendus dans la réponse ; refus : formule de refus reconnue sur les pièges ; jugement complémentaire par le modèle `chat` (réflexion coupée), signalé « juge LLM ». [Vérifié]
- Citation : bon document parmi les sources renvoyées ; AnythingLLM ne donne pas la page (les pages d'un PDF sont mises bout à bout avant découpage). [Source] (`cadrage-serveur.md`)
- `free -m` et `outils/communs/llm_central_sante.sh --essai` relevés avant chaque banc (en tête de chaque `banc-*.log`). [Vérifié]
- Série : `outils/anythingllm/serie_banc.sh` ; même espace « Banc-bge-m3 », mêmes questions, seul le réglage change. [Vérifié]

## 2. Résultats

| Solution | Banc | Modèle | Réglages | Exactes | Refus pièges | Bon document cité | Bonne page | p50 (s) | p95 (s) | Indexation (s) | Pic RAM application (Mo) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AnythingLLM | [defaut-sans-rerank](../../../outils/resultats/anythingllm/banc-2026-11-12-defaut-sans-rerank.json) | chat, embedder embed | mode query, topN 4, seuil 0.25, recherche default | 33/34 | 3/4 | 33 | non exposée | 14.25 | 27.78 | 8.5 | 887 |
| AnythingLLM | [embedder-natif](../../../outils/resultats/anythingllm/banc-2026-11-12-embedder-natif.json) | chat, embedder Xenova/all-MiniLM-L6-v2 | mode query, topN 4, seuil 0.25, recherche default | 25/34 | 4/4 | 32 | non exposée | 11.97 | 45.18 | - | 617 |
| AnythingLLM | [rerank-natif](../../../outils/resultats/anythingllm/banc-2026-11-12-rerank-natif.json) | chat, embedder embed | mode query, topN 4, seuil 0.25, recherche rerank | 34/34 | 4/4 | 34 | non exposée | 13.54 | 50.17 | - | 1560 |
| AnythingLLM | [serre-top2](../../../outils/resultats/anythingllm/banc-2026-11-12-serre-top2.json) | chat, embedder embed | mode query, topN 2, seuil 0.25, recherche default | 31/34 | 4/4 | 32 | non exposée | 13.43 | 34.71 | 0.2 | 1568 |
| AnythingLLM | [top8-rerank-natif](../../../outils/resultats/anythingllm/banc-2026-11-12-top8-rerank-natif.json) | chat, embedder embed | mode query, topN 8, seuil 0.25, recherche rerank | 34/34 | 4/4 | 34 | non exposée | 10.69 | 37.64 | - | 1573 |
| AnythingLLM | [top8](../../../outils/resultats/anythingllm/banc-2026-11-12-top8.json) | chat, embedder embed | mode query, topN 8, seuil 0.25, recherche default | 34/34 | 4/4 | 34 | non exposée | 13.55 | 28.56 | - | 1559 |

Lecture [Vérifié] :

- **Embedder** : passer de l'embedder intégré (all-MiniLM-L6-v2, surtout anglais) à `embed` (bge-m3, multilingue) fait passer de 25 à 33 réponses justes sur 34, surtout sur les tableaux (5/10 → 10/10) et les questions à plusieurs documents (1/3 → 3/3).
- **Tri de précision natif** (« Accuracy Optimized ») : 34/34 et 4/4 au lieu de 33/34 et 3/4, médiane identique (13,5 s contre 14,3 s), queue plus longue (p95 50 s contre 28 s).
- **8 passages** au lieu de 4 : 34/34 et 4/4 sans tri ; avec tri, la médiane la plus basse (10,7 s).
- **Réglage serré** (2 passages) : 31/34 ; les questions qui croisent deux informations perdent une moitié de réponse.
- **Juge LLM** : 35 à 37 « oui » sur 38 selon le réglage, cohérent avec la notation par mots-clés.
- Indexation des 9 documents avec `embed` : 8,5 s (OCR et transcription compris) ; les autres bancs réutilisent l'espace déjà indexé (« - » ou 0).

## 3. Ce qui change le résultat

| Réglage | Où | Effet mesuré |
|---|---|---|
| Embedder `embed` (bge-m3) au lieu de l'embedder intégré | Préférences d'intégration | +8 réponses justes sur 34 [Vérifié] |
| « Accuracy Optimized » | réglages de l'espace › Base de données vectorielle | +1 juste, +1 refus correct ; p95 plus longue [Vérifié] |
| « Nombre maximum de contextes » 8 | même onglet | +1 juste, +1 refus correct [Vérifié] |
| « Nombre maximum de contextes » 2 | même onglet | −2 justes par rapport à 4 [Vérifié] |
| « Max Tokens » 8192 au lieu de 1024 | Préférence LLM | évite les réponses coupées par la réflexion ; avec 64, message de limite atteinte [Vérifié] (chapitre 15) |
| OCR en français (`TARGET_OCR_LANG=fra,eng`) | `donnees/anythingllm/options.env` | « Brême » et « l'Acheteur » lus correctement ; non rejoué sur le banc, les 4 questions du scan étant déjà justes en anglais [Vérifié] (`ocr-fra-2026-11-12.log`) |

## 4. Reranker : ce que la solution accepte

AnythingLLM 1.19.0 **n'accepte pas de reranker externe** : aucune variable ni route `/rerank` dans le code ; le modèle `rerank` du service central (bge-reranker-v2-m3) ne peut donc pas être branché. [Source] (`cadrage-serveur.md`, section 4)

Seul existe le reranker intégré `Xenova/ms-marco-MiniLM-L-6-v2` (23 Mo, téléchargé au premier usage depuis Hugging Face), activé par espace avec « Accuracy Optimized » (`vectorSearchMode: "rerank"`) : 10 à 50 candidats sont retrouvés puis reclassés, les `topN` meilleurs gardés. [Source] Il a été comparé à l'absence de tri (section 2). Journal : « Reranking 10 documents to top 4 took 225ms » à « 255ms ». [Vérifié] (`journal-extraits-2026-11-12.txt`)

## 5. Questions manquées

| Banc | Question | Constat |
|---|---|---|
| défaut | Q34 « Qui est le directeur de production de Vélanor ? » (attendu : Moreau, dans le message vocal) | le passage de la transcription n'est pas retrouvé parmi les 4 ; trouvé avec le tri ou 8 passages [Vérifié] |
| défaut | Q38 (piège, salaire d'un salarié) | réponse vide : ni refus ni invention [Vérifié] |
| serré (2) | Q12, Q30 | moitié de la réponse seulement (pays du fournisseur, délai moyen constaté) [Vérifié] |
| embedder intégré | 9 questions (tableaux, plusieurs documents) | passages pertinents non retrouvés par un modèle surtout anglais [Vérifié] |

## 6. Temps et mémoire

- Médiane de 10,7 à 14,3 s par question, réflexion du modèle comprise ; p95 de 28 à 50 s (questions où le modèle réfléchit longtemps). [Vérifié]
- Mémoire de l'application en pointe : 617 Mio (embedder intégré), 887 Mio (bge-m3), environ 1,56 Gio dès que le reranker intégré a été chargé (il reste en mémoire). [Vérifié] (`pic_ram_mo`)
- Service central pendant les bancs : `llm-swap` 5,7 Gio, `llm-speaches` 1,3 Gio, `llm-central` 0,7 Gio ; carte graphique 8,1 Go sur 16. [Vérifié]

## 7. Préconisations

Pour des questions sur des documents en français : embedder `embed`, mode « Requête », « Accuracy Optimized », 6 à 8 passages, « Max Tokens » 8192, OCR en français si des scans sont prévus. Ce réglage donne 34/34 et 4/4 sur le banc. [Vérifié]

## Dépannage

| Symptôme | Cause probable | Action |
|---|---|---|
| Réponses fausses sur des tableaux | embedder intégré | brancher `embed` (chapitre 03) |
| Réponse vide | réflexion qui consomme le plafond, ou mode Agent | « Max Tokens » 8192 ; mode « Requête » |
| p95 élevée | longue réflexion du modèle | non réglable dans AnythingLLM (pas de paramètre de réflexion pour Generic OpenAI) [Source] |

## Sources

- Résultats bruts : `outils/resultats/anythingllm/banc-2026-11-12-*.json`, `.md` et `.log`.
- Code : `outils/anythingllm/banc.py`, `serie_banc.sh`, `outils/communs/banc/commun.py`.
