# Rapport de mission — AnythingLLM

Mission `kit/PROMPT.md`, fiche `kit/fiches/04-anythingllm.md`, exécutée le 12 novembre 2026 en autonomie. Manuel : [docs/anythingllm/README.md](docs/anythingllm/README.md).

## Ce qui a été installé

| Élément | Version |
|---|---|
| AnythingLLM (édition Docker) | 1.19.0, image `mintplexlabs/anythingllm:1.19.0@sha256:daf5a6ae9d363ed578e7d41e2d0668c7eaa604bd90b0ff27435f893b0906833e` (3,39 Go), conteneur `rag-anythingllm` |
| Site de test | `nginx:alpine`, conteneur `rag-anythingllm-site`, sans port publié |
| Captures | `mcr.microsoft.com/playwright/python:v1.65.1-noble@sha256:0ab41a37431309d72b7a26f40ef1fdb464a62740196b2143965a2f59dc090409` |
| Service de modèles | LLM-Service (géré à part, non modifié) : LiteLLM v1.109.0, llama-swap v272 (llama.cpp build 12282), speaches 0.8.3 ; profil `gpu` |
| Modèles utilisés | `chat` = Qwen3.5-4B Q4_K_M (réflexion activée, 16 384 jetons), `embed` = bge-m3 Q8_0 (1 024 dimensions), `transcribe` = faster-whisper-small ; `rerank` = bge-reranker-v2-m3 disponible mais **non utilisable** par AnythingLLM |
| Modèles propres à AnythingLLM téléchargés | embedder intégré all-MiniLM-L6-v2 (23 Mo, pour la comparaison), tri de précision ms-marco-MiniLM-L-6-v2 (23 Mo), OCR Tesseract `eng` et `fra` (environ 5 Mo chacun) |

Versions relevées : `outils/resultats/anythingllm/versions-2026-11-12.json`.

## Où ouvrir la solution

- Depuis le navigateur Windows : **http://127.0.0.1:3001** (vérifié depuis WSL : `curl` répond 200).
- Instance en multi-utilisateur. Comptes fictifs et mot de passe : `donnees/IDENTIFIANTS-LOCAUX.txt` (administrateur `admin-velanor`, utilisateur `camille.martin`). Clé d'API des scripts : `donnees/anythingllm/cle-api.txt`.
- Jeu de démonstration : espace « Démo Vélanor » (10 documents du corpus, procédure épinglée, mode « Requête », question suggérée) avec trois conversations citées : « FAQ — garantie », « Fournisseur Batterix », « Point production ». Autres espaces : « Premier essai » (chapitre 04), « Sources externes » (site de test, dépôt GitHub, vidéo YouTube), « Mon Espace de Travail » (créé par l'assistant). Widget intégrable actif sur « Démo Vélanor », page de test `outils/anythingllm/essais/site/widget-actif.html`.

## Manuels écrits

- Partie 1, manuel utilisateur, 16 chapitres et 133 captures annotées : [01](docs/anythingllm/manuel/01-decouvrir-anythingllm.md) découvrir (configurations minimales sans et avec carte graphique), [02](docs/anythingllm/manuel/02-installer-anythingllm.md) installer, [03](docs/anythingllm/manuel/03-premiers-pas.md) premiers pas, [04](docs/anythingllm/manuel/04-premiere-question.md) première question, [05](docs/anythingllm/manuel/05-ajouter-et-organiser-ses-documents.md) documents, [06](docs/anythingllm/manuel/06-poser-des-questions-et-lire-les-sources.md) questions et sources, [07](docs/anythingllm/manuel/07-regler-un-espace-de-travail.md) réglages d'un espace, [08](docs/anythingllm/manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) modèles et lecture, [09](docs/anythingllm/manuel/09-sources-externes.md) sources externes, [10](docs/anythingllm/manuel/10-agents-et-outils.md) agents et MCP, [11](docs/anythingllm/manuel/11-memoires-taches-et-routage.md) mémoires, tâches, routage, [12](docs/anythingllm/manuel/12-personnaliser-et-administrer.md) personnaliser et administrer, [13](docs/anythingllm/manuel/13-comptes-equipe-et-widget.md) comptes, équipe et widget, [14](docs/anythingllm/manuel/14-cas-pratiques.md) cas pratiques, [15](docs/anythingllm/manuel/15-en-cas-de-probleme.md) en cas de problème, [16](docs/anythingllm/manuel/16-glossaire.md) glossaire.
- Partie 2 : [A1](docs/anythingllm/annexes/A1-evaluation-qualite-et-performances.md) évaluation, [A2](docs/anythingllm/annexes/A2-choisir-son-materiel-et-ses-modeles.md) matériel, [A3](docs/anythingllm/annexes/A3-automatiser-par-l-api.md) API, [A4](docs/anythingllm/annexes/A4-exploitation.md) exploitation, [A5](docs/anythingllm/annexes/A5-fonctionnement-interne.md) fonctionnement interne, [A6](docs/anythingllm/annexes/A6-rapport-d-essais.md) rapport d'essais, [carte de l'interface](docs/anythingllm/annexes/carte-interface.md).
- Exemples d'API : `exemples/anythingllm/` (7 exemples, sorties dans `sorties_verifiees.txt`).

## Résultats du banc en cinq lignes

1. bge-m3 (`embed`), réglages par défaut, sans tri : 33/34 justes, 3/4 refus, médiane 14,3 s, indexation des 9 documents 8,5 s.
2. Avec le tri de précision intégré (« Accuracy Optimized », seul reranker accepté) : 34/34, 4/4, médiane 13,5 s.
3. 8 passages : 34/34, 4/4 ; 8 passages et tri : 34/34, 4/4, médiane 10,7 s (meilleur réglage).
4. Embedder intégré (all-MiniLM-L6-v2) : 25/34 seulement ; 2 passages (réglage serré) : 31/34.
5. Mémoire de l'application : 0,4 Gio au repos, 0,9 Gio en charge, 1,6 Gio avec le tri de précision chargé.

## Ce qui a été vérifié, ce qui ne l'a pas été

- Vérifié : installation, ports sur `127.0.0.1`, télémétrie coupée, chaque écran de la partie 1 à la souris, bancs (6 réglages), exemples d'API, arrêt, redémarrage, sauvegarde, restauration, OCR en français, dépassement de contexte, connecteurs (site, GitHub, YouTube), serveur MCP, widget, multi-utilisateur.
- Non vérifié (détail en A6, section 5) : profil sans carte graphique (estimé), `nettoyer.sh` (relu, non rejoué pour garder la démonstration), mise à jour de version, réglage du découpage, règles du routeur, exécution d'une tâche planifiée, `gemma-4-e4b` au banc, extension de navigateur, mobile, Telegram, Centre communautaire, dictée et lecture vocale, acceptation d'une invitation.
- Reranker `rerank` du service central : non essayé, car AnythingLLM 1.19.0 n'accepte aucun reranker externe (code source) ; le reranker intégré a été comparé à l'absence de tri.

## Incidents rencontrés

- `JWT_SECRET` prérempli à la première installation : l'assistant de premier lancement était sauté ; installation refaite sans cette variable.
- Fichier envoyé non déplaçable tant que la fenêtre des documents n'est pas rouverte (bogue de la 1.19.0, documenté).
- Mode « Agent » de l'interface : réponse vide, puis réponse tirée d'Internet sur une autre entreprise (documenté, mode « Requête » conseillé).
- Clé d'API locale visible sur une capture et dans un texte enregistré : capture refaite, masquage automatique ajouté, textes nettoyés avant tout commit.
- `TARGET_OCR_LANG` écrit dans le `.env` de l'application sans effet ; passé au conteneur par `donnees/anythingllm/options.env`.
- Arrêt du conteneur forcé par Docker au bout de 10 s (code 137), sans perte de données.

## Décisions en attente

Voir [JOURNAL.md](JOURNAL.md#décisions-en-attente) :

1. Proposer dans LLM-Service une option pour couper ou borner la réflexion de `chat` par défaut pour les applications qui ne savent pas le demander (AnythingLLM ne transmet aucun paramètre de réflexion) ; effet attendu : temps de réponse plus courts.
2. Proposer un modèle de réponse plus léger dans LLM-Service pour situer un plancher de qualité (hors mission).
3. Tâche planifiée « Point stocks du lundi » laissée programmée (09:00 UTC chaque jour) : sa page n'est plus accessible en multi-utilisateur ; à supprimer par l'utilisateur s'il ne veut pas d'appel quotidien au modèle (restaurer la sauvegarde d'avant le passage en multi-utilisateur, ou base SQLite).

## Disque, RAM et VRAM occupés (fin de mission)

| Élément | Valeur |
|---|---|
| Image AnythingLLM | 3,39 Go ; image Playwright 2,46 Go |
| Données `donnees/anythingllm/` | 57 Mo ; sauvegarde `donnees/sauvegardes/` 36 Mo |
| RAM `rag-anythingllm` | 472 Mio au repos |
| RAM service central | `llm-swap` 5,4 Gio, `llm-speaches` 1,3 Gio, `llm-central` 0,7 Gio |
| VRAM | 8,3 Go sur 16,4 (service central et bureau Windows) |

## Comment tout arrêter ou tout supprimer

```bash
outils/anythingllm/arreter.sh                 # arrêt, données gardées
outils/anythingllm/essais/site.sh stop        # arrêt du site de test
outils/communs/nettoyer.sh anythingllm        # suppression du conteneur et de donnees/anythingllm (confirmation)
docker image rm mintplexlabs/anythingllm:1.19.0
```

LLM-Service n'est jamais arrêté par ces scripts.

## Proposition pour la solution suivante

Open WebUI (fiche 05) : interface généraliste multi-utilisateur. Points à reprendre d'ici : masquage automatique des clés dans `ui.py` dès le premier scénario, vérification du mode par défaut des conversations (agent ou non), test d'un reranker externe dès le cadrage, et un banc « réglages par défaut » puis « meilleur réglage » plutôt que six variantes, pour gagner du temps quand le modèle réfléchit.
