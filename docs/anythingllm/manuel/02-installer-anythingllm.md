# 02. Installer AnythingLLM

> Ce chapitre apprend à installer AnythingLLM sous Windows 11 avec WSL2, à l'ouvrir dans le navigateur, puis à l'arrêter, le redémarrer et le supprimer.
> **Point de départ** : un terminal Ubuntu (WSL2) ouvert sur le poste, Docker Desktop démarré, et le service de modèles LLM-Service installé et démarré sur le même poste (voir « Ce qu'il faut savoir »).
> **Durée** : environ 15 minutes, dont 5 de téléchargement. **Avant** : chapitre 01.

**Attention** : l'application n'est ouverte qu'au poste lui-même (adresse `127.0.0.1`). Ne pas modifier les ports dans les fichiers fournis : une adresse ouverte sur le réseau exposerait les documents et la clé du service de modèles.

## Ce qu'il faut savoir

AnythingLLM tient dans **un seul conteneur Docker** (un « conteneur » est une petite machine isolée qui contient l'application et tout ce dont elle a besoin). Ce conteneur ne contient aucun modèle d'IA : les réponses, la représentation des textes et la transcription de l'audio sont demandées à un **service de modèles** installé à part sur le même poste : le service LLM central, projet LLM-Service (https://github.com/floSa/llm-service). Il s'installe en suivant son propre README, avant ce chapitre, et se démarre par son script `scripts/demarrer.sh` (dans le dossier où il a été installé ; ajouter `cpu` sans carte graphique NVIDIA). Il est protégé par une clé, que sa personne responsable fournit.

Ce service a deux adresses : depuis le terminal du poste, `http://127.0.0.1:8080/v1` ; depuis AnythingLLM, qui tourne dans un conteneur Docker relié au service par un réseau Docker nommé `llm-net`, `http://llm-central:8080/v1`. Le chapitre 03 fait saisir cette seconde adresse dans AnythingLLM.

L'installation se fait avec un script fourni dans ce dépôt. Il télécharge l'image officielle d'AnythingLLM à une version précise, crée un dossier de données, coupe l'envoi de statistiques d'usage et démarre l'application. Le compte, la langue et le choix des modèles se font ensuite dans le navigateur (chapitre 03).

Les données (documents, conversations, réglages) sont rangées dans le dossier `donnees/anythingllm/` du dépôt. Les supprimer efface tout.

## Vérifier les prérequis

**Étape 1. Vérifier Docker**
*Où* : terminal Ubuntu.

```bash
docker version --format '{{.Server.Version}}'
docker compose version
```

*Résultat* : deux numéros de version s'affichent (par exemple `29.9.3` et `Docker Compose version v5.7.0`). Une erreur signifie que Docker Desktop n'est pas démarré, ou que l'intégration WSL n'est pas activée dans ses réglages (Docker Desktop › Settings › Resources › WSL integration).

**Étape 2. Récupérer le dépôt**
*Où* : terminal Ubuntu, dans le dossier où ranger le projet.

```bash
git clone https://github.com/floSa/AnythingLLM-Test-Bench.git
cd AnythingLLM-Test-Bench
```

*Résultat* : le dossier `AnythingLLM-Test-Bench` existe ; toutes les commandes suivantes se lancent depuis ce dossier.

**Étape 3. Déclarer la clé du service de modèles**
*Où* : terminal Ubuntu, dossier du dépôt.

```bash
cp .env.example .env
nano .env
```

Dans le fichier ouvert, remplacer la valeur de `LLM_CENTRAL_KEY` par la clé du service LLM central (la personne qui gère ce service la fournit), enregistrer avec Ctrl+O puis quitter avec Ctrl+X. Ce fichier `.env` n'est jamais envoyé sur GitHub.

*Résultat* : le fichier `.env` contient la clé ; il n'est lisible que sur le poste.

**Étape 4. Vérifier que le service de modèles répond**
*Où* : terminal Ubuntu, dossier du dépôt.

```bash
outils/communs/llm_central_sante.sh --essai
```

*Résultat* : la liste des modèles s'affiche (`chat`, `embed`, `rerank`, `transcribe` et quelques autres), puis une ligne par essai : un mot de réponse, `dimensions : 1024`, deux scores de tri, le début de la transcription d'un message vocal. Si la commande répond « service injoignable », démarrer le service avec le script `scripts/demarrer.sh` du dossier de LLM-Service (sur le poste d'essai : `~/mes_projets/Projet-IA/LLM-Service/scripts/demarrer.sh` ; ajouter `cpu` sans carte graphique NVIDIA), puis relancer la vérification.

## Installer et ouvrir l'application

**Étape 5. Lancer l'installation**
*Où* : terminal Ubuntu, dossier du dépôt.

```bash
outils/anythingllm/installer.sh
```

Le script télécharge l'image (3,4 Go, une seule fois), écrit les réglages dans `donnees/anythingllm/storage/.env`, démarre le conteneur `rag-anythingllm` et attend qu'il réponde.

*Résultat* : les dernières lignes affichent `AnythingLLM prêt : http://127.0.0.1:3001`, la ligne `rag-anythingllm 127.0.0.1:3001->3001/tcp` (l'application n'écoute que sur le poste), la durée et la mémoire prise au repos (environ 400 Mo). Sans téléchargement, l'installation prend une dizaine de secondes.

**Étape 6. Ouvrir AnythingLLM dans le navigateur**
*Où* : navigateur de Windows (Edge, Firefox, Chrome), barre d'adresse.

Taper `http://127.0.0.1:3001` puis Entrée.

![Écran d'accueil au premier lancement](../img/03-premiers-pas/01-bienvenue.png)
*Écran : assistant de premier lancement, page « Bienvenue ».*

| N° | Élément | Rôle |
|---|---|---|
| 1 | « Commencer » | lance l'assistant de premier lancement (chapitre 03) |

*Résultat* : la page « Bienvenue » s'affiche, en français si le navigateur est en français. L'installation est terminée ; la suite se passe au chapitre 03.

## Arrêter, redémarrer, supprimer

**Étape 7. Voir l'état de l'application**
*Où* : terminal Ubuntu, dossier du dépôt.

```bash
outils/anythingllm/etat.sh
```

*Résultat* : l'état du conteneur (`Up … (healthy)`), la réponse `{"online":true}`, la mémoire utilisée, la place occupée par les données et la liste des modèles du service central.

**Étape 8. Arrêter AnythingLLM**
*Où* : terminal Ubuntu, dossier du dépôt.

```bash
outils/anythingllm/arreter.sh
```

*Résultat* : `AnythingLLM arrêté.` Les documents et réglages sont conservés. Le service de modèles, partagé avec d'autres applications, continue de tourner.

**Étape 9. Redémarrer AnythingLLM**
*Où* : terminal Ubuntu, dossier du dépôt.

```bash
outils/anythingllm/demarrer.sh
```

*Résultat* : `AnythingLLM prêt : http://127.0.0.1:3001` après quelques secondes. Dans le navigateur, l'écran de connexion demande le mot de passe choisi au chapitre 03.

**Étape 10. Tout supprimer**
*Où* : terminal Ubuntu, dossier du dépôt.

```bash
outils/communs/nettoyer.sh anythingllm
```

Le script annonce ce qu'il va supprimer et demande de taper `oui`. Il supprime le conteneur et le dossier `donnees/anythingllm/` (documents, conversations, réglages, clés d'API). Il ne touche pas au service de modèles. L'image téléchargée reste dans Docker ; pour la retirer aussi : `docker image rm mintplexlabs/anythingllm:1.19.0`.

*Résultat* : `Terminé.` ; l'adresse `http://127.0.0.1:3001` ne répond plus.

## Bon à savoir

- Le script d'installation peut être relancé sans risque : il garde les réglages et les données existants.
- L'installation n'écrit pas de clé de session (`JWT_SECRET`) d'avance : si cette valeur existe au premier démarrage, AnythingLLM considère l'assistant de premier lancement comme déjà fait et ne l'affiche plus.
- Avec l'envoi de statistiques coupé, l'application télécharge quand même, au démarrage, deux tables publiques (tailles de contexte et prix des modèles). Elles ne contiennent aucune donnée du poste.
- La version installée est AnythingLLM 1.19.0. Une version de bureau existe aussi pour Windows, Mac et Linux (une seule personne, sans comptes) ; ce manuel décrit la version Docker, qui permet plusieurs comptes.

## En cas de problème

| Symptôme | Cause | Que faire |
|---|---|---|
| `réseau llm-net absent` | le service de modèles n'est pas démarré (`llm-net` est le réseau Docker qu'il crée) | démarrer LLM-Service (`scripts/demarrer.sh` de son dossier), puis relancer l'installation |
| `AnythingLLM ne répond pas après 180 s` | démarrage en échec | `docker logs rag-anythingllm` ; voir le [chapitre 15](15-en-cas-de-probleme.md) |
| La page affiche directement l'écran de connexion ou l'espace de travail au lieu de « Bienvenue » | l'assistant a déjà été fait (ou une clé de session existait) | se connecter avec le mot de passe existant, ou tout supprimer (étape 10) puis réinstaller |

---
*Version décrite : AnythingLLM 1.19.0, essais du 12 novembre 2026. Détails et preuves : [rapport d'essais](../annexes/A6-rapport-d-essais.md).*
