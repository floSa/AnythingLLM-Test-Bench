# A6. Rapport d'essais

> **Objet** : dire comment le manuel a été produit, ce qui a été vérifié, avec quelle preuve, et ce qui ne l'a pas été.
> **Prérequis** : aucun.
> **Version décrite** : AnythingLLM 1.19.0 (image `mintplexlabs/anythingllm:1.19.0@sha256:daf5a6ae9d363ed578e7d41e2d0668c7eaa604bd90b0ff27435f893b0906833e`), essais du 12 novembre 2026.
> **Statut des informations** : [Vérifié] observé ou mesuré, résultat brut cité ; [Source] lu dans le code ou la documentation, non essayé ; [Estimation] calcul expliqué ; [À tester] ni lu ni essayé.
> **Précautions** : données fictives uniquement ; identifiants d'essai dans `donnees/IDENTIFIANTS-LOCAUX.txt` (non versionné) ; la clé du service central n'apparaît dans aucun fichier versionné ni aucune capture.

## Sommaire

1. [Machine et service de modèles](#1-machine-et-service-de-modèles)
2. [Méthode](#2-méthode)
3. [Preuves par sujet](#3-preuves-par-sujet)
4. [Incidents et comportements surprenants](#4-incidents-et-comportements-surprenants)
5. [Ce qui n'a pas été vérifié](#5-ce-qui-na-pas-été-vérifié)
6. [Dépannage](#dépannage)
7. [Sources](#sources)

## 1. Machine et service de modèles

- Windows 11 (version 10.0.26300), WSL 3.0.5, Ubuntu 24.04.5, noyau 6.18.58.1 ; Ryzen 5 9600X, 32 Go dans WSL ; RTX 4060 Ti 16 Go, pilote 616.92 ; Docker 29.9.3, Compose 5.7.0. [Vérifié] (`outils/resultats/machine/diagnostic-2026-11-12.json`)
- Service LLM central, profil `gpu` : `chat`, `embed`, `rerank`, `transcribe` ; essai réussi en début de session. [Vérifié] (`outils/resultats/anythingllm/sante-2026-11-12-debut.txt`)
- Versions relevées : `outils/resultats/anythingllm/versions-2026-11-12.json` (AnythingLLM v1.19.0 à jour ; Playwright 1.65.1 ; LiteLLM v1.109.0 en retard d'une version, relevé pour traçabilité, hors mission). [Vérifié]

## 2. Méthode

- Lecture du code au tag par deux sous-agents : `outils/resultats/anythingllm/cadrage-serveur.md`, `cadrage-interface.md`. [Source]
- Installation par `outils/anythingllm/installer.sh` ; relecture consignée dans `relecture.md`. [Vérifié]
- Chaque action de la partie 1 faite à la souris par Playwright (conteneur `mcr.microsoft.com/playwright/python:v1.65.1-noble`), scénarios `outils/anythingllm/captures/c03_…` à `c15_…` ; texte de chaque page capturée et libellés des pastilles dans `outils/resultats/anythingllm/captures/<chapitre>/`. [Vérifié]
- Banc : `outils/anythingllm/banc.py`, `serie_banc.sh` (annexe A1). [Vérifié]
- Exemples d'API : `exemples/anythingllm/`, sorties dans `sorties_verifiees.txt`. [Vérifié]

## 3. Preuves par sujet

| Affirmation | Preuve |
|---|---|
| Ports liés à `127.0.0.1` seulement | `installation-2026-11-12.log` (`rag-anythingllm 127.0.0.1:3001->3001/tcp`) [Vérifié] |
| Télémétrie coupée | `demarrage-2026-11-12.log`, `journal-extraits-2026-11-12.txt` (« Telemetry is marked as disabled ») [Vérifié] |
| `JWT_SECRET` prérempli fait sauter l'assistant | `installation-2026-11-12-essai1-jwt.log` [Vérifié] |
| Embedder intégré 25/34, bge-m3 33/34, tri de précision 34/34 | `banc-2026-11-12-*.json` [Vérifié] |
| Reranker externe non pris en charge | `cadrage-serveur.md` section 4 [Source] |
| Tri de précision : 10 passages en 225 à 255 ms | `journal-extraits-2026-11-12.txt` [Vérifié] |
| Arrêt, redémarrage (8 s), sauvegarde (36 Mo), restauration | `exploitation-2026-11-12.log` [Vérifié] |
| OCR en français par `options.env`, sans effet par `storage/.env` | `ocr-fra-2026-11-12.log` [Vérifié] |
| Dépassement : question de 20 418 jetons refusée par `embed` | `contexte-2026-11-12.txt` [Vérifié] |
| Serveur MCP d'exemple : initialisation, liste, appel | sortie de `outils/anythingllm/mcp/installer-mcp.sh` ; capture du chapitre 10 [Vérifié] |
| Connecteurs site (3 pages), GitHub (1 fichier), YouTube (transcription) | `captures/09-sources-externes/notes.log` [Vérifié] |
| Widget : réponse dans une page de test | `captures/13-comptes-et-widget/notes.log`, capture 16 [Vérifié] |
| Exemples d'API, code de sortie 0 | `exemples/anythingllm/sorties_verifiees.txt` [Vérifié] |

## 4. Incidents et comportements surprenants

| Constat | Détail | Statut |
|---|---|---|
| Fichier envoyé non déplaçable | dans la fenêtre des documents encore ouverte, « Déplacer vers l'espace de travail » reste sans effet ; fermer et rouvrir la fenêtre | [Vérifié] (essai A/B, `captures/04-premiere-question/notes.log`) |
| Mode « Agent » peu fiable dans l'interface | réponse vide au premier essai ; réponse tirée d'Internet sur une autre entreprise au second ; par l'API, réponse juste | [Vérifié] (chapitre 15, capture 03) |
| Extension inconnue acceptée | un fichier `.xyz` est lu comme du texte | [Vérifié] |
| Clé fausse : message peu clair | « 400 No connected db. » (message du service central) | [Vérifié] |
| Arrêt forcé | le conteneur s'arrête en code 137 au bout de 10 s | [Vérifié] (`exploitation-2026-11-12.log`) |
| Traductions approximatives | « Nouvelle offre d'emploi » pour « New Job », environ un quart des libellés restent en anglais | [Vérifié] |
| Clé d'API locale visible sur une capture | repérée, capture refaite, masquage automatique ajouté aux scénarios (`ui.py`), textes enregistrés nettoyés ; jamais commitée | [Vérifié] |
| Réponse vide sur une question piège (Q38, banc par défaut) | ni refus ni invention | [Vérifié] |

## 5. Ce qui n'a pas été vérifié

- Profil A (sans carte graphique) : temps estimés à partir des mesures de LLM-Service, non mesurés avec AnythingLLM. [Estimation]
- `outils/communs/nettoyer.sh anythingllm` : relu, non rejoué pour ne pas détruire le jeu de démonstration. [À tester]
- Mise à jour vers une version suivante d'AnythingLLM. [À tester]
- Réglage du découpage (taille des passages) et effet sur le banc. [À tester]
- Règles d'un routeur de modèles et exécution d'une tâche planifiée (la tâche « Point stocks du lundi » est programmée, jamais exécutée pendant les essais). [À tester]
- Second modèle de réponse `gemma-4-e4b` sur le banc. [À tester]
- Extension de navigateur, application mobile, Telegram, Centre communautaire (comptes en ligne ou applications hors périmètre). [À tester]
- Dictée et lecture à voix haute par le navigateur (pas de micro ni de son dans le navigateur automatisé). [À tester]
- Acceptation d'une invitation par la personne invitée. [À tester]

## Dépannage

| Symptôme | Cause probable | Action |
|---|---|---|
| Une capture ne correspond plus à l'écran | version différente d'AnythingLLM | rejouer le scénario du chapitre (`outils/communs/captures/lancer.sh outils/anythingllm/captures/cNN_….py`) |
| Un banc ne se lance pas | clé d'API absente | `outils/anythingllm/client.py` la recrée par l'API interne si les identifiants existent |

## Sources

- Résultats bruts : `outils/resultats/anythingllm/`.
- Journal de mission : [JOURNAL.md](../../../JOURNAL.md).
