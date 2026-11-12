# Carte de l'interface d'AnythingLLM 1.19.0

Liste de contrôle de la couverture : chaque page, menu, onglet et réglage visible de l'interface (édition Docker, interface en français, compte administrateur), avec le chapitre de la partie 1 qui le couvre. Relevé par parcours de l'interface avec Playwright (captures de repérage en fin de page) et lecture du code du frontend (`outils/resultats/anythingllm/cadrage-interface.md`).

Une partie de l'interface reste en anglais même en français (libellés écrits en dur dans le code) : ces libellés sont cités tels qu'affichés.

## Écrans principaux

| Page ou menu | Chemin d'accès | Éléments (boutons, onglets, réglages) | Manuel qui le couvre |
|---|---|---|---|
| Assistant de premier lancement | `/onboarding` (premier lancement) | « Bienvenue », « Commencer », Préférence LLM, Configuration utilisateur (« Juste moi », « Mon équipe »), Gestion des données, enquête (« Ignorer l'enquête ») | [03](../manuel/03-premiers-pas.md) |
| Connexion | `/login` | « Mot de passe » (mono-utilisateur) ou « Nom d'utilisateur » et « Mot de passe » (multi-utilisateur), « Connexion », « Mot de passe oublié? Réinitialiser » | [03](../manuel/03-premiers-pas.md), [13](../manuel/13-comptes-equipe-et-widget.md) |
| Écran principal | `/` | message d'accueil, zone « Envoyer un message », « Créer un agent », « Modifier l'espace de travail », « Télécharger un document » | [03](../manuel/03-premiers-pas.md) |
| Barre latérale | toutes les pages | « Rechercher », « + » (Nouvel Espace de Travail), liste des espaces, icône d'envoi, roue dentée de l'espace, fils (« New Thread », « Rename », « Delete Thread »), liens GitHub, Docs, Discord, bouton des paramètres | [03](../manuel/03-premiers-pas.md), [06](../manuel/06-poser-des-questions-et-lire-les-sources.md) |
| Fenêtre « Nouvel Espace de Travail » | barre latérale › « + » | « Nom des espaces de travail », « Save » | [04](../manuel/04-premiere-question.md) |
| Discussion d'un espace | `/workspace/<espace>` | zone « Envoyer un message », « Envoyer », « Outils » (« Commandes abrégées », « Compétences des agents »), pièce jointe, micro, sélecteur de modèle, menu des réglages du chat (« Taille du texte », « Souvenirs », « Exporter la conversation au format... ») | [04](../manuel/04-premiere-question.md), [06](../manuel/06-poser-des-questions-et-lire-les-sources.md) |
| Réponse et sources | sous chaque réponse | « Sources », panneau « Sources », fenêtre d'extrait (pourcentage « match »), « Copier », « Régénérer », « Bonne réponse », modification, « Plus d'actions » (« Dupliquer », « Supprimer »), réflexion repliée | [04](../manuel/04-premiere-question.md), [06](../manuel/06-poser-des-questions-et-lire-les-sources.md) |
| Gestionnaire de documents, onglet « Documents » | barre latérale › icône d'envoi de l'espace | « Mes documents », « Rechercher un document », « Nouveau dossier », zone d'envoi, « ou soumettre un lien », « Déplacer vers l'espace de travail », déplacer vers un dossier, corbeille, « Sauvegarder et intégrer », épingle, retrait | [05](../manuel/05-ajouter-et-organiser-ses-documents.md) |
| Gestionnaire de documents, onglet « Connecteurs de données » | même fenêtre | GitHub, GitLab, Gitea, YouTube, site web, Confluence, Drupal Wiki, Obsidian, Paperless-ngx | [09](../manuel/09-sources-externes.md) |
| Souvenirs | discussion › menu des réglages du chat › « Souvenirs » | onglets « Espace de travail » et « Global », « Activer la personnalisation », « Souvenirs automatisés », « Créer un souvenir » | [11](../manuel/11-memoires-taches-et-routage.md) |
| Compte | menu du compte (multi-utilisateur) › « Compte » | photo, nom d'utilisateur, mot de passe, « Thème », « Langue », « Mettre à jour le compte » | [13](../manuel/13-comptes-equipe-et-widget.md) |

## Réglages d'un espace de travail

| Page ou menu | Chemin d'accès | Éléments (boutons, onglets, réglages) | Manuel qui le couvre |
|---|---|---|---|
| Paramètres généraux | roue dentée de l'espace › « Paramètres généraux » | « Nom des espaces de travail », « Messages de chat suggérés », « Supprimer l'espace de travail » | [07](../manuel/07-regler-un-espace-de-travail.md) |
| Paramètres du chat | › « Paramètres du chat » | fournisseur et modèle de l'espace, mode (« Agent », « Chat », « Requête »), « Historique des chats », invite système, « Réponse de refus en mode requête », « Température LLM » | [07](../manuel/07-regler-un-espace-de-travail.md) |
| Base de données vectorielle | › « Base de données vectorielle » | identifiant, « Nombre de vecteurs », préférence de recherche (« Default », « Accuracy Optimized »), « Nombre maximum de contextes », « Seuil de similarité des documents », « Réinitialiser la base de données vectorielle » | [07](../manuel/07-regler-un-espace-de-travail.md) |
| Membres | › « Membres » (multi-utilisateur) | liste des membres, « Manage Users » | [13](../manuel/13-comptes-equipe-et-widget.md) |
| Configuration de l'agent | › « Configuration de l'agent » | fournisseur et modèle de l'agent de l'espace, « Configure Agent Skills » | [10](../manuel/10-agents-et-outils.md) |

## Paramètres de l'instance

| Page ou menu | Chemin d'accès | Éléments (boutons, onglets, réglages) | Manuel qui le couvre |
|---|---|---|---|
| Préférence LLM | Paramètres › Fournisseurs d'IA › « Préférence LLM » | fournisseur, « Base URL », « API Key », « Selected Model », « Model context window », « Max Tokens », « Save changes » | [03](../manuel/03-premiers-pas.md), [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Base de données vectorielle | › « Base de données vectorielle » | LanceDB (défaut) et autres bases | [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Préférences d'intégration | › « Préférences d'intégration » | fournisseur d'embedding, « Base URL », « Embedding Model », « Max embedding chunk length », clé, réglages avancés | [03](../manuel/03-premiers-pas.md), [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Diviseur de texte et découpage | › « Diviseur de texte et découpage » | « Taille des segments de texte », « Chevauchement des segments de texte » | [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Génération d'images | › « Génération d'images » | fournisseur d'images | [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Voix et Parole | › « Voix et Parole » | « Speech-to-text Preference », synthèse vocale (System native, PiperTTS, OpenAI Compatible…) | [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Modèle de transcription | › « Modèle de transcription » | OpenAI, OpenAI Compatible, AnythingLLM Built-In | [03](../manuel/03-premiers-pas.md) |
| Routeur modèle | › « Routeur modèle » | « Nouveau routeur », règles, plan de secours | [11](../manuel/11-memoires-taches-et-routage.md) |
| Utilisateurs | Paramètres › Admin › « Utilisateurs » (multi-utilisateur) | « Add user », rôles Default, Manager, Administrator, « Edit », « Suspend », « Delete » | [13](../manuel/13-comptes-equipe-et-widget.md) |
| Espaces de travail | › « Espaces de travail » | « New Workspace », liste, suppression | [12](../manuel/12-personnaliser-et-administrer.md) |
| Chat de l'espace de travail | › « Chat de l'espace de travail » | historique de toutes les conversations, « Exporter », « Clear Chats » | [12](../manuel/12-personnaliser-et-administrer.md) |
| Invitation | › « Invitation » (multi-utilisateur) | « Create Invite Link », « Copy Invite Link » | [13](../manuel/13-comptes-equipe-et-widget.md) |
| Default System Prompt | › « Default System Prompt » | « System Prompt », « Save Changes » | [12](../manuel/12-personnaliser-et-administrer.md) |
| Compétences de l'agent | Paramètres › « Compétences de l'agent » | compétences intégrées, « Agent Flows », « MCP Servers », « Custom Skills » | [10](../manuel/10-agents-et-outils.md) |
| Éditeur d'agent flow | › « Agent Flows » › « Create Flow » | blocs, enregistrement | [10](../manuel/10-agents-et-outils.md) |
| Centre communautaire | Paramètres › « Centre communautaire » | tendances, compte, import | Non couvert : contenu chargé depuis un service en ligne qui demande un compte ; hors périmètre (aucun compte en ligne) |
| Interface | Paramètres › Apparence › « Interface » | « Thème », « Palette de couleurs », « Langue d'affichage » | [03](../manuel/03-premiers-pas.md), [12](../manuel/12-personnaliser-et-administrer.md) |
| Personnalisation | › « Personnalisation » | onglets Identité, Couleurs, Barre latérale, Navigateur ; nom de l'application, logo, e-mail de support | [12](../manuel/12-personnaliser-et-administrer.md) |
| Chat (apparence) | › « Chat » | envoi et lecture automatiques, correction orthographique, barre de défilement, rendu HTML | [12](../manuel/12-personnaliser-et-administrer.md) |
| Canaux, Telegram | Paramètres › « Canaux » (mono-utilisateur) | connexion d'un robot Telegram | Non couvert : demande un compte Telegram en ligne (hors périmètre) ; page montrée au [chapitre 12](../manuel/12-personnaliser-et-administrer.md) |
| Widgets de chat intégrés | Paramètres › Outils › « Widgets de chat intégrés » | « Créer un widget intégré », onglets « Widgets » et « History » | [13](../manuel/13-comptes-equipe-et-widget.md) |
| Journaux d'événements | › « Journaux d'événements » | liste des événements, « Effacer les journaux d'événements » | [12](../manuel/12-personnaliser-et-administrer.md) |
| Tâches planifiées | › « Tâches planifiées » (mono-utilisateur seulement) | création d'une tâche, exécutions | [11](../manuel/11-memoires-taches-et-routage.md) |
| Clés API | › « Clés API » | « Générer une nouvelle clé API », documentation de l'API | [12](../manuel/12-personnaliser-et-administrer.md) |
| Variables de prompt système | › « Variables de prompt système » | variables de la consigne | [12](../manuel/12-personnaliser-et-administrer.md) |
| Extension de navigateur | › « Extension de navigateur » | « Generate New API Key » | [12](../manuel/12-personnaliser-et-administrer.md) |
| AnythingLLM Mobile | › « AnythingLLM Mobile » | appareils connectés | Non couvert : demande l'application mobile (hors périmètre de la fiche) ; page montrée au [chapitre 12](../manuel/12-personnaliser-et-administrer.md) |
| Sécurité | Paramètres › « Sécurité » (mono-utilisateur) | mot de passe de l'instance, « Mode multi-utilisateurs » | [13](../manuel/13-comptes-equipe-et-widget.md) |
| Confidentialité et données | lien en bas du menu des paramètres | fournisseurs et ce qu'ils voient, télémétrie | [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Fonctionnalités expérimentales | Ctrl maintenu 3 s dans les paramètres | « Live Document Sync » | [12](../manuel/12-personnaliser-et-administrer.md) |

## Captures de repérage

Une capture par page, prise le 12 novembre 2026 avec le compte administrateur, en multi-utilisateur (scénario `outils/anythingllm/captures/carte.py`, texte de chaque page dans `outils/resultats/anythingllm/captures/carte/`). Les pages réservées au mode « Juste moi » (tâches planifiées, Telegram) sont montrées aux chapitres 11 et 12.

![Repérage : accueil](../img/carte/accueil.png)
*accueil*

![Repérage : apparence-chat](../img/carte/apparence-chat.png)
*apparence-chat*

![Repérage : base-vectorielle](../img/carte/base-vectorielle.png)
*base-vectorielle*

![Repérage : centre-communautaire](../img/carte/centre-communautaire.png)
*centre-communautaire*

![Repérage : cles-api](../img/carte/cles-api.png)
*cles-api*

![Repérage : competences](../img/carte/competences.png)
*competences*

![Repérage : confidentialite](../img/carte/confidentialite.png)
*confidentialite*

![Repérage : consigne-par-defaut](../img/carte/consigne-par-defaut.png)
*consigne-par-defaut*

![Repérage : conversations](../img/carte/conversations.png)
*conversations*

![Repérage : decoupage](../img/carte/decoupage.png)
*decoupage*

![Repérage : discussion](../img/carte/discussion.png)
*discussion*

![Repérage : documentation-api](../img/carte/documentation-api.png)
*documentation-api*

![Repérage : embedding](../img/carte/embedding.png)
*embedding*

![Repérage : espace-agent](../img/carte/espace-agent.png)
*espace-agent*

![Repérage : espace-chat](../img/carte/espace-chat.png)
*espace-chat*

![Repérage : espace-general](../img/carte/espace-general.png)
*espace-general*

![Repérage : espace-membres](../img/carte/espace-membres.png)
*espace-membres*

![Repérage : espace-vecteurs](../img/carte/espace-vecteurs.png)
*espace-vecteurs*

![Repérage : espaces](../img/carte/espaces.png)
*espaces*

![Repérage : experimental](../img/carte/experimental.png)
*experimental*

![Repérage : extension](../img/carte/extension.png)
*extension*

![Repérage : images](../img/carte/images.png)
*images*

![Repérage : interface](../img/carte/interface.png)
*interface*

![Repérage : invitations](../img/carte/invitations.png)
*invitations*

![Repérage : journaux](../img/carte/journaux.png)
*journaux*

![Repérage : mobile](../img/carte/mobile.png)
*mobile*

![Repérage : personnalisation](../img/carte/personnalisation.png)
*personnalisation*

![Repérage : preference-llm](../img/carte/preference-llm.png)
*preference-llm*

![Repérage : routeurs](../img/carte/routeurs.png)
*routeurs*

![Repérage : securite](../img/carte/securite.png)
*securite*

![Repérage : transcription](../img/carte/transcription.png)
*transcription*

![Repérage : utilisateurs](../img/carte/utilisateurs.png)
*utilisateurs*

![Repérage : variables](../img/carte/variables.png)
*variables*

![Repérage : voix](../img/carte/voix.png)
*voix*

![Repérage : widgets](../img/carte/widgets.png)
*widgets*

---
*Version décrite : AnythingLLM 1.19.0, relevé du 12 novembre 2026. Les lignes sont vérifiées à la fin de la mission contre les chapitres écrits.*
