# Manuel d'AnythingLLM

Ce manuel apprend à installer et à utiliser AnythingLLM 1.19.0 (édition Docker) sur un poste Windows 11 avec WSL2, branché sur un service de modèles d'IA local. Il s'adresse à une personne à l'aise avec un terminal, sans être forcément développeur. Chaque étape a été faite dans l'interface, à la souris, et montrée par une capture d'écran annotée.

Le manuel se lit en deux parties : la **partie 1** est le manuel utilisateur, à lire dans l'ordre ; la **partie 2** évalue l'outil (qualité des réponses, matériel, automatisation, exploitation) et n'est pas nécessaire pour suivre la partie 1.

## Par où commencer

Lire les chapitres 01 à 04 dans l'ordre : en une heure environ, l'application est installée, configurée, et une première réponse citant un document est obtenue.

## Partie 1 — Manuel utilisateur

| N° | Chapitre | Ce qu'on saura faire |
|---|---|---|
| 01 | [Découvrir AnythingLLM](manuel/01-decouvrir-anythingllm.md) | dire à quoi sert l'outil, pour qui, sur quelle machine, et ce qu'il vaut d'après les essais |
| 02 | [Installer AnythingLLM](manuel/02-installer-anythingllm.md) | installer, ouvrir, arrêter, redémarrer et supprimer l'application |
| 03 | [Premiers pas](manuel/03-premiers-pas.md) | faire l'assistant de premier lancement, se connecter, se repérer dans l'écran, régler la langue, déclarer les modèles |
| 04 | [Première question en dix minutes](manuel/04-premiere-question.md) | créer un espace de travail, y déposer un document, poser une question et lire la source citée |
| 05 | [Ajouter et organiser ses documents](manuel/05-ajouter-et-organiser-ses-documents.md) | téléverser des fichiers, les ranger en dossiers, les placer dans un espace, les épingler, les retirer |
| 06 | [Poser des questions et lire les sources](manuel/06-poser-des-questions-et-lire-les-sources.md) | choisir entre les modes Chat, Requête et Agent, lire les sources, gérer les fils, reprendre ou exporter une réponse |
| 07 | [Régler un espace de travail](manuel/07-regler-un-espace-de-travail.md) | régler la consigne, l'historique, la température, le nombre de passages, le seuil et le tri de précision |
| 08 | [Choisir les modèles et la lecture des documents](manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) | changer de modèle, régler le découpage des textes, la voix, la base vectorielle, vérifier ce qui sort du poste |
| 09 | [Sources externes](manuel/09-sources-externes.md) | importer un site web, un dépôt GitHub public, une vidéo YouTube |
| 10 | [Agents et outils](manuel/10-agents-et-outils.md) | lancer un agent, choisir ses compétences, construire un enchaînement sans code, brancher un serveur MCP |
| 11 | [Mémoires, tâches planifiées et routage de modèles](manuel/11-memoires-taches-et-routage.md) | faire retenir des informations, programmer une tâche, répartir les questions entre plusieurs modèles |
| 12 | [Personnaliser et administrer](manuel/12-personnaliser-et-administrer.md) | changer l'apparence et le nom, consulter les journaux et l'historique des conversations, créer une clé d'API |
| 13 | [Comptes, équipe et widget](manuel/13-comptes-equipe-et-widget.md) | passer en multi-utilisateur, créer des comptes et des rôles, inviter, intégrer une fenêtre de discussion dans un site |
| 14 | [Cas pratiques](manuel/14-cas-pratiques.md) | mettre en place trois usages complets, de bout en bout |
| 15 | [En cas de problème](manuel/15-en-cas-de-probleme.md) | reconnaître les erreurs réellement rencontrées et les corriger |
| 16 | [Glossaire](manuel/16-glossaire.md) | retrouver le sens des mots employés |

## Partie 2 — Évaluation et compléments

| N° | Annexe | Contenu |
|---|---|---|
| A1 | [Évaluation : qualité et performances](annexes/A1-evaluation-qualite-et-performances.md) | résultats du banc de 38 questions, effet de l'embedder, du tri de précision et du nombre de passages |
| A2 | [Choisir son matériel et ses modèles](annexes/A2-choisir-son-materiel-et-ses-modeles.md) | configurations minimales sans et avec carte graphique, budget de contexte, temps d'attente |
| A3 | [Automatiser par l'API](annexes/A3-automatiser-par-l-api.md) | API développeur, exemples exécutés |
| A4 | [Exploitation](annexes/A4-exploitation.md) | sauvegarde, restauration, mise à jour, journaux, sécurité, connexions sortantes |
| A5 | [Fonctionnement interne](annexes/A5-fonctionnement-interne.md) | architecture, conteneur, ports, découpage, budget de contexte |
| A6 | [Rapport d'essais](annexes/A6-rapport-d-essais.md) | méthode, preuves, ce qui a été vérifié et ce qui ne l'a pas été |
| — | [Carte de l'interface](annexes/carte-interface.md) | chaque page et menu de l'interface, avec le chapitre qui le couvre |

## Parcours conseillés

| Besoin | Chapitres |
|---|---|
| Interroger ses documents, seul | 01 à 07, puis 14 |
| Mettre l'outil à disposition d'une équipe | 01 à 07, 12, 13, puis annexe A4 |
| Automatiser (scripts, autre application) | 01 à 04, 12, puis annexe A3 |
| Choisir l'outil ou le matériel | 01, puis annexes A1 et A2 |

## Ce qui reste ouvert

- Le mode « Agent », mode par défaut d'un nouvel espace, n'est pas fiable dans l'interface : préférer « Requête » (chapitres 04 et 15).
- La lecture des scans en français demande un réglage hors de l'interface (chapitre 15).
- Non décrits : règles du routeur de modèles, blocs des agent flows, compétences personnalisées, extension de navigateur, application mobile, Telegram, Centre communautaire.
- Détail de ce qui a été vérifié ou non : [rapport d'essais](annexes/A6-rapport-d-essais.md).

## Décisions en attente

Réservé aux responsables de l'installation : les choix qui dépassent ce manuel (réglages du service de modèles) sont listés dans le [journal du projet](../../JOURNAL.md#décisions-en-attente).
