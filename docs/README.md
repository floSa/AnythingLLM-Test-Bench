# Index de la série

Manuels vérifiés de solutions de RAG local sous Windows 11 + WSL2. Chaque solution a son dépôt ; ce dépôt décrit AnythingLLM et reprend les résultats des solutions déjà passées au banc.

## Solutions décrites

| Solution | Version décrite | Date des essais | Machine de test | Langue de l'interface | Manuels |
|---|---|---|---|---|---|
| Open Notebook | 1.15.1 | 2026-11-08, 2026-11-09 et 2026-11-12 | Intel Core Ultra 7 255H sans GPU NVIDIA, puis Ryzen 5 9600X, RTX 4060 Ti 16 Go | français (langue du navigateur) | dépôt https://github.com/floSa/Open-Notebook-Test-Bench |
| RAGFlow | v1.0.0 | 2026-11-09 au 2026-11-12 | Ryzen 5 9600X, 32 Go (WSL), RTX 4060 Ti 16 Go | français (sélecteur de l'en-tête) | dépôt https://github.com/floSa/RAGFlow-Test-Bench |
| AnythingLLM | 1.19.0 | 2026-11-12 | Ryzen 5 9600X, 32 Go (WSL), RTX 4060 Ti 16 Go ; service LLM central en profil `gpu` | français partiel (langue du navigateur, environ un quart des libellés en anglais) | [manuel utilisateur](anythingllm/README.md) |

## Comparatif du banc

Mêmes 38 questions ([corpus/questions.json](../corpus/questions.json) : 34 avec réponse, 4 pièges), même corpus fictif de 9 documents, même machine.

### Service LLM central (modèles `chat` Qwen3.5-4B avec réflexion, `embed` bge-m3) — comparables entre eux

| Solution | Banc | Modèle | Réglages | Exactes | Refus pièges | Bon document cité | Bonne page | p50 (s) | p95 (s) | Indexation (s) | Pic RAM application (Mo) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| open-notebook | [central-chat](../outils/resultats/open-notebook/banc-2026-11-12-central-chat.json) | chat | mode chat, sources full content, Docling true | 28/34 | 4/4 | 29 | non exposée | 8.69 | 27.92 | 64.9 | 4696 |
| ragflow | [defaut-reranker](../outils/resultats/ragflow/banc-2026-11-12-defaut-reranker.json) | chat (Qwen3.5-4B, service LLM central) | gabarit general, top_n 6, poids vecteurs 0.3, contexte 16384 | 34/34 | 4/4 | 33 | 23/23 | 8.31 | 58.31 | - | 5104 |
| ragflow | [defaut](../outils/resultats/ragflow/banc-2026-11-12-defaut.json) | chat (Qwen3.5-4B, service LLM central) | gabarit general, top_n 6, poids vecteurs 0.3, contexte 16384 | 33/34 | 4/4 | 34 | 24/24 | 7.8 | 50.03 | 64.0 | 5407 |
| ragflow | [hybride-vecteurs07-top8-reranker](../outils/resultats/ragflow/banc-2026-11-12-hybride-vecteurs07-top8-reranker.json) | chat (Qwen3.5-4B, service LLM central) | gabarit general, top_n 8, poids vecteurs 0.7, contexte 16384 | 34/34 | 4/4 | 34 | 24/24 | 8.78 | 55.04 | - | 5072 |
| ragflow | [hybride-vecteurs07-top8](../outils/resultats/ragflow/banc-2026-11-12-hybride-vecteurs07-top8.json) | chat (Qwen3.5-4B, service LLM central) | gabarit general, top_n 8, poids vecteurs 0.7, contexte 16384 | 34/34 | 4/4 | 34 | 24/24 | 7.76 | 56.92 | - | 5076 |
| AnythingLLM | [defaut-sans-rerank](../outils/resultats/anythingllm/banc-2026-11-12-defaut-sans-rerank.json) | chat, embedder embed | mode query, topN 4, seuil 0.25, recherche default | 33/34 | 3/4 | 33 | non exposée | 14.25 | 27.78 | 8.5 | 887 |
| AnythingLLM | [embedder-natif](../outils/resultats/anythingllm/banc-2026-11-12-embedder-natif.json) | chat, embedder Xenova/all-MiniLM-L6-v2 | mode query, topN 4, seuil 0.25, recherche default | 25/34 | 4/4 | 32 | non exposée | 11.97 | 45.18 | - | 617 |
| AnythingLLM | [rerank-natif](../outils/resultats/anythingllm/banc-2026-11-12-rerank-natif.json) | chat, embedder embed | mode query, topN 4, seuil 0.25, recherche rerank | 34/34 | 4/4 | 34 | non exposée | 13.54 | 50.17 | - | 1560 |
| AnythingLLM | [serre-top2](../outils/resultats/anythingllm/banc-2026-11-12-serre-top2.json) | chat, embedder embed | mode query, topN 2, seuil 0.25, recherche default | 31/34 | 4/4 | 32 | non exposée | 13.43 | 34.71 | 0.2 | 1568 |
| AnythingLLM | [top8-rerank-natif](../outils/resultats/anythingllm/banc-2026-11-12-top8-rerank-natif.json) | chat, embedder embed | mode query, topN 8, seuil 0.25, recherche rerank | 34/34 | 4/4 | 34 | non exposée | 10.69 | 37.64 | - | 1573 |
| AnythingLLM | [top8](../outils/resultats/anythingllm/banc-2026-11-12-top8.json) | chat, embedder embed | mode query, topN 8, seuil 0.25, recherche default | 34/34 | 4/4 | 34 | non exposée | 13.55 | 28.56 | - | 1559 |

### Ancienne pile (Ollama ou vLLM, autres modèles) — modèles différents, non comparable tel quel

| Solution | Banc | Modèle | Réglages | Exactes | Refus pièges | Bon document cité | Bonne page | p50 (s) | p95 (s) | Indexation (s) | Pic RAM application (Mo) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| open-notebook | [docling-qwen-fullcontent-ollama040](../outils/resultats/open-notebook/banc-2026-11-08-docling-qwen-fullcontent-ollama040.json) | qwen3:4b-instruct | mode chat, sources full content, num_ctx 16384, Docling true | 28/34 | 4/4 | 28 | non exposée | 7.44 | 24.19 | 84.3 | 3133 |
| open-notebook | [gpu-vllm](../outils/resultats/open-notebook/banc-2026-11-09-gpu-vllm.json) | gemma4:e4b | mode chat, sources full content, Docling false | 27/34 | 4/4 | 24 | non exposée | 1.86 | 4.28 | 54.2 | 624 |
| ragflow | [defaut](../outils/resultats/ragflow/banc-2026-11-09-defaut.json) | gemma4:e4b (vLLM, LLM-Service service-vllm) | gabarit general, top_n 6, poids vecteurs 0.3, contexte 16384 | 33/34 | 4/4 | 34 | 24/24 | 1.28 | 1.88 | 53.0 | 5394 |
| ragflow | [hybride-vecteurs07-top8](../outils/resultats/ragflow/banc-2026-11-09-hybride-vecteurs07-top8.json) | gemma4:e4b (vLLM, LLM-Service service-vllm) | gabarit general, top_n 8, poids vecteurs 0.7, contexte 16384 | 34/34 | 4/4 | 34 | 24/24 | 1.36 | 1.83 | - | 5041 |

Lecture :

- « Bonne page » : seul RAGFlow expose la page du passage cité ; AnythingLLM et Open Notebook citent le document et le passage.
- AnythingLLM atteint 34/34 et 4/4 avec son tri de précision intégré ou 8 passages, comme RAGFlow avec ses meilleurs réglages, pour environ 1,5 Gio de mémoire contre 5 Gio pour RAGFlow. Il n'accepte pas le reranker externe `rerank`, que RAGFlow utilise.
- Avec l'embedder intégré d'AnythingLLM (surtout anglais), le résultat tombe à 25/34 : le modèle d'embedding du service central est indispensable sur ce corpus français.
- Les temps de réponse sont du même ordre pour les trois solutions sur le service central (médiane 8 à 14 s), car le modèle `chat` réfléchit avant de répondre.

## Parcours de lecture conseillés

| Profil | Parcours |
|---|---|
| Découvrir le RAG local | [glossaire](glossaire.md), puis [Découvrir AnythingLLM](anythingllm/manuel/01-decouvrir-anythingllm.md), puis l'annexe [Fonctionnement interne](anythingllm/annexes/A5-fonctionnement-interne.md) |
| Installer et essayer rapidement | chapitres [01 à 04 du manuel AnythingLLM](anythingllm/README.md#par-où-commencer) |
| Choisir entre solutions | comparatif ci-dessus, puis annexes [Qualité et performances](anythingllm/annexes/A1-evaluation-qualite-et-performances.md) et [Matériel et modèles](anythingllm/annexes/A2-choisir-son-materiel-et-ses-modeles.md) |
| Automatiser | [Automatiser par l'API](anythingllm/annexes/A3-automatiser-par-l-api.md) |

## Conventions

| Étiquette | Sens |
|---|---|
| [Vérifié] | observé ou mesuré sur la machine d'essai, à la date indiquée ; renvoie à un script et à un résultat brut de `outils/` |
| [Source] | lu dans la documentation officielle ou le code source, non essayé |
| [Estimation] | calcul non mesuré, avec son raisonnement |
| [À tester] | ni documenté ni essayé |
| [Testée] | commande exécutée pendant les essais |
| [Aide] | commande lue dans l'aide, non exécutée |

Les libellés de l'interface sont cités tels qu'affichés. Les données sont fictives (entreprise Vélanor).
