# 01. Découvrir AnythingLLM

> Ce chapitre explique à quoi sert AnythingLLM, pour qui, ce qu'il sait faire, sur quelle machine il tourne et ce qu'il a donné aux essais.
> **Point de départ** : aucun ; ce chapitre se lit sans l'application.
> **Durée** : environ 10 minutes. **Avant** : aucun.

## Ce qu'il faut savoir

AnythingLLM est une application web qui permet de **poser des questions à ses propres documents** et d'obtenir des réponses rédigées qui indiquent de quel document elles viennent. Elle sait aussi faire travailler un **agent** : un assistant qui enchaîne des actions (chercher dans les documents, lire un site web, créer un fichier) pour accomplir une tâche.

Le travail s'organise en **espaces de travail**. Un espace réunit :

- des **documents** : PDF (y compris scannés), Word, Excel, PowerPoint, pages web, Markdown, fichiers audio et vidéo ;
- des **conversations**, rangées en fils ;
- des **réglages** : consigne donnée au modèle, nombre de passages lus, mode de réponse.

Les espaces sont cloisonnés : une question posée dans un espace ne voit que les documents de cet espace.

AnythingLLM ne contient pas de modèle d'IA dans cette installation : il s'appuie sur un **service de modèles** installé sur le même poste (le service LLM central), qui fournit le modèle de réponse, le modèle d'embedding (qui représente le sens des textes) et la transcription de l'audio. Rien ne part vers un service en ligne pour répondre aux questions.

## Pour qui

| Adapté | Peu adapté |
|---|---|
| Une personne ou une petite équipe qui veut interroger quelques dizaines à quelques centaines de documents et obtenir des réponses avec leur source | Un besoin de citer la page exacte d'un PDF : AnythingLLM indique le document et le passage, pas la page |
| Plusieurs équipes avec chacune ses documents : espaces cloisonnés, comptes et rôles | Un service ouvert au public sans précaution : la fenêtre de discussion intégrable doit être limitée (nombre de messages, domaines autorisés) |
| Automatiser des tâches simples sans programmer : agents, enchaînements sans code, tâches planifiées | Des documents scannés en français : la lecture optique (OCR) est réglée en anglais par défaut et se règle seulement par un fichier de configuration |
| Brancher ses documents à d'autres applications par une API ou par le protocole MCP | Un poste sans service de modèles : il faut un service compatible OpenAI, ou l'un des fournisseurs en ligne payants |

## Le projet

| | |
|---|---|
| Dépôt | https://github.com/Mintplex-Labs/anything-llm |
| Site | https://anythingllm.com |
| Licence | MIT : libre, usage commercial autorisé |
| Popularité | 68 209 étoiles, 7 700 copies (forks) sur GitHub |
| Activité | très active : 406 modifications sur les 90 derniers jours, 295 contributeurs, une nouvelle version toutes les deux à trois semaines |
| Ancienneté | projet créé en juin 2023 ; version décrite 1.19.0 du 26 octobre 2026 |
| Éditions | version Docker (plusieurs comptes, décrite ici) et application de bureau pour Windows, Mac et Linux (une seule personne) |
| Coût | gratuit ; aucun abonnement |

Chiffres relevés sur GitHub le 12 novembre 2026.

## Fonctions

Réponses : **Oui**, **Non**, ou **Partiel** avec la limite en une phrase.

### Modèles d'IA

| Fonction | Réponse |
|---|---|
| Service de modèles local compatible OpenAI (llama.cpp, vLLM, LM Studio, LiteLLM…) | Oui (« Generic OpenAI ») |
| Ollama, LM Studio, LocalAI en direct | Oui |
| Fournisseurs en ligne (OpenAI, Anthropic, Mistral, Google…) | Oui, une quarantaine |
| Embedding sur le poste | Oui : modèle intégré (surtout anglais) ou service de modèles |
| Tri de précision des passages (reranker) | Partiel : seulement le petit modèle intégré (« Accuracy Optimized ») ; aucun reranker externe |
| Transcription de l'audio | Oui, par le service de modèles ou un modèle intégré |
| Lecture à voix haute et dictée | Oui : voix du navigateur, voix Piper intégrée ou service compatible |
| Un modèle différent par espace, routage automatique entre modèles | Oui |

### Documents acceptés

| Fonction | Réponse |
|---|---|
| PDF, Word, PowerPoint, Excel, OpenDocument, EPUB, texte, Markdown, HTML, CSV | Oui |
| PDF scannés et images (OCR) | Partiel : lus, mais en anglais par défaut |
| Audio et vidéo | Oui, transcrits |
| Sites web, dépôts GitHub et GitLab, vidéos YouTube, Confluence, Obsidian | Oui, par les connecteurs de données |
| Dossiers et rangement des documents | Oui |

### Recherche et réponses

| Fonction | Réponse |
|---|---|
| Réponse à partir des documents d'un espace | Oui |
| Mode « Requête » : ne répond qu'à partir des documents et refuse sinon | Oui |
| Sources affichées sous la réponse, avec le passage et son score | Oui |
| Numéro de page du passage | Non |
| Document lu en entier à chaque question (épinglage) | Oui |
| Recherche combinant mots exacts et sens | Non : recherche par le sens seulement |

### Agents et automatisation

| Fonction | Réponse |
|---|---|
| Agent avec compétences intégrées (documents, web, fichiers, graphiques, SQL) | Oui |
| Enchaînements sans code (agent flows) | Oui |
| Serveurs MCP | Oui |
| Souvenirs (mémoire entre conversations) | Oui, désactivés par défaut |
| Tâches planifiées | Partiel : seulement en mode une personne |
| API développeur et documentation interactive | Oui |
| Fenêtre de discussion à intégrer dans un site | Oui |

### Installation et exploitation

| Fonction | Réponse |
|---|---|
| Installation | Docker, un seul conteneur |
| Mémoire nécessaire, hors modèles d'IA | 0,4 Go au repos, 1,6 Go au plus avec le tri de précision |
| Interface en français | Partiel : environ trois quarts des libellés |
| Comptes et rôles | Oui : administrateur, gestionnaire, utilisateur |
| Envoi de statistiques d'usage | Oui par défaut, coupé ici ; deux tables publiques restent téléchargées au démarrage |
| Sauvegarde | Oui, par copie du dossier de données |

## Matériel nécessaire

Le matériel se partage entre le service de modèles (le plus gros) et AnythingLLM (léger). Le détail des mesures est dans l'[annexe A2](../annexes/A2-choisir-son-materiel-et-ses-modeles.md).

### Sans carte graphique

| Élément | Minimum |
|---|---|
| Processeur | 8 cœurs récents |
| Mémoire vive | 16 Go : environ 4,3 Go pour le service de modèles, 1 à 1,6 Go pour AnythingLLM, le reste pour Windows et WSL |
| Disque libre | 15 Go : 3,4 Go pour l'image d'AnythingLLM, environ 5 Go pour les modèles du service, le reste pour les documents |
| Temps d'attente | le modèle produit environ 14 jetons par seconde, cinq fois moins qu'avec une carte graphique : compter 1 à 2 minutes par réponse, réflexion comprise (estimation, annexe A2) |

### Avec une carte graphique NVIDIA

| Élément | Minimum |
|---|---|
| Carte graphique | 8 Go de mémoire (7 Go pris par les trois modèles permanents) ; 16 Go sur le poste d'essai |
| Mémoire vive | 16 Go : environ 5,4 Go pour le service de modèles, 1 à 1,6 Go pour AnythingLLM |
| Disque libre | 15 Go |
| Temps d'attente | environ 68 jetons par seconde : la plupart des réponses arrivent en 11 à 14 secondes, réflexion comprise, les plus longues en 50 secondes |

Le volume de documents n'est pas limité par la mémoire : AnythingLLM ne transmet au modèle que les quelques passages utiles (4 par défaut, environ 1 200 jetons), quelle que soit la taille de l'espace.

## Résultats mesurés

Test sur 38 questions dont la réponse est connue, posées à 9 documents d'une entreprise fictive (rapport annuel, contrat scanné, procédure, présentation, tableur, page web, note, audit en anglais, message vocal), avec le modèle de réponse `chat` sur une carte graphique de 16 Go.

| Mesure | Résultat |
|---|---|
| Réponses justes | 33 sur 34 avec les réglages par défaut ; 34 sur 34 avec le tri de précision « Accuracy Optimized » ou 8 passages |
| Questions sans réponse dans les documents | 4 refus sur 4 avec le tri de précision, aucune réponse inventée |
| Embedder intégré à la place du service | 25 sur 34 seulement : brancher le modèle d'embedding du service est indispensable en français |
| Temps de réponse | 11 à 14 secondes en général, réflexion du modèle comprise ; jusqu'à 50 secondes pour les plus longues |
| Ajout des 9 documents | 8,5 secondes, lecture du scan et transcription de l'audio comprises |

Détail : [annexe A1](../annexes/A1-evaluation-qualite-et-performances.md).

## Pour aller plus loin

| Pour | Lire |
|---|---|
| Installer | [02. Installer AnythingLLM](02-installer-anythingllm.md) |
| Première réponse citée | [04. Première question en dix minutes](04-premiere-question.md) |
| Trois usages complets | [14. Cas pratiques](14-cas-pratiques.md) |
| Choisir le matériel | [annexe A2](../annexes/A2-choisir-son-materiel-et-ses-modeles.md) |

## Résultat

Le lecteur sait ce que fait AnythingLLM, s'il convient à son besoin et quelle machine prévoir.

---
*Version décrite : AnythingLLM 1.19.0, essais du 12 novembre 2026. Détails et preuves : [rapport d'essais](../annexes/A6-rapport-d-essais.md).*
