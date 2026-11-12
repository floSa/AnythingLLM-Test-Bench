# Carte de l'interface d'AnythingLLM 1.19.0

Liste de contrôle de la couverture : chaque page, menu, onglet et réglage visible de l'interface (édition Docker, interface en français, compte administrateur), avec le chapitre de la partie 1 qui le couvre. Relevé par parcours de l'interface avec Playwright (captures de repérage en fin de page) et lecture du code du frontend (`outils/resultats/anythingllm/cadrage-interface.md`).

Une partie de l'interface reste en anglais même en français (libellés écrits en dur dans le code) : ces libellés sont cités tels qu'affichés.

## Écrans principaux

| Page ou menu | Chemin d'accès | Éléments (boutons, onglets, réglages) | Manuel qui le couvre |
|---|---|---|---|
| Assistant de premier lancement | `/onboarding` (premier lancement) | « Bienvenue », « Commencer », Préférence LLM, Configuration utilisateur (« Juste moi », « Mon équipe »), Gestion des données, enquête (« Ignorer l'enquête ») | [03](../manuel/03-premiers-pas.md) |
| Connexion | `/login` | « Mot de passe » (mono-utilisateur) ou « Nom d'utilisateur » et « Mot de passe » (multi-utilisateur), « Connexion », « Mot de passe oublié? Réinitialiser » | [03](../manuel/03-premiers-pas.md), [13](../manuel/13-comptes-equipe-et-widget.md) |
| Écran principal | `/` | message d'accueil, zone « Envoyer un message », « Outils » | [03](../manuel/03-premiers-pas.md) |
| Actions rapides de l'écran principal | `/`, sous la zone de saisie | « Créer un agent », « Modifier l'espace de travail », « Télécharger un document » | Non couvert : raccourcis vers des pages décrites ailleurs (chapitres 10, 07 et 05) |
| Barre latérale | toutes les pages | « + » (Nouvel Espace de Travail), liste des espaces, icône d'envoi, roue dentée de l'espace, fils (« New Thread », « Rename », « Delete Thread »), bouton des paramètres | [03](../manuel/03-premiers-pas.md), [06](../manuel/06-poser-des-questions-et-lire-les-sources.md) |
| Barre latérale, éléments secondaires | toutes les pages | « Rechercher », bouton qui replie la barre, poignées de réordonnancement des espaces, liens GitHub, Docs et Discord | Non couvert : confort d'affichage et liens vers des sites en ligne |
| Fenêtre « Nouvel Espace de Travail » | barre latérale › « + » | « Nom des espaces de travail », « Save » | [04](../manuel/04-premiere-question.md) |
| Discussion d'un espace | `/workspace/<espace>` | zone « Envoyer un message », « Envoyer », « Outils » (« Commandes abrégées » avec `/reset` et « Ajouter », « Compétences des agents »), « @ » (agent), menu des réglages du chat (« Taille du texte », « Souvenirs », « Exporter la conversation au format... ») | [04](../manuel/04-premiere-question.md), [06](../manuel/06-poser-des-questions-et-lire-les-sources.md), [10](../manuel/10-agents-et-outils.md) |
| Fenêtre « Ajouter une nouvelle commande preset » | « Outils » › « Commandes abrégées » › « Ajouter » | commande, prompt, description, « Annuler », « Sauvegarder » | [06](../manuel/06-poser-des-questions-et-lire-les-sources.md) |
| Menu des réglages du chat, lien du fil | menu des réglages du chat | « Copy chat link » | [06](../manuel/06-poser-des-questions-et-lire-les-sources.md) |
| Discussion, micro et sélecteur de modèle | `/workspace/<espace>` | micro (dictée), nom du modèle qui ouvre le sélecteur (« Rechercher des modèles ») | [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Discussion, pièce jointe | `/workspace/<espace>`, « + » de la zone de saisie | fichier joint à la conversation sans intégration | Non couvert : non essayé ; l'ajout de documents passe par la fenêtre des documents (chapitre 05) |
| Réponse et sources | sous chaque réponse | « Sources », panneau « Sources », fenêtre d'extrait (pourcentage « match »), haut-parleur (lecture à voix haute), « Copier », « Régénérer », « Bonne réponse », modification, « Plus d'actions » (« Dupliquer », « Supprimer »), réflexion repliée | [04](../manuel/04-premiere-question.md), [06](../manuel/06-poser-des-questions-et-lire-les-sources.md) |
| Gestionnaire de documents, onglet « Documents » | barre latérale › icône d'envoi de l'espace | « Mes documents », « Rechercher un document », « Nouveau dossier », zone d'envoi, « ou soumettre un lien », « Déplacer vers l'espace de travail », déplacer vers un dossier, corbeille, « Sauvegarder et intégrer », épingle, retrait | [05](../manuel/05-ajouter-et-organiser-ses-documents.md) |
| Gestionnaire de documents, onglet « Connecteurs de données » | même fenêtre | GitHub, GitLab, Gitea, YouTube, site web, Confluence, Drupal Wiki, Obsidian, Paperless-ngx | [09](../manuel/09-sources-externes.md) |
| Souvenirs | discussion › menu des réglages du chat › « Souvenirs » | « Activer la personnalisation », « Souvenirs automatisés », onglet au nom de l'espace (par exemple « DÉMO VÉLANOR ») et onglet global, lien « créer un nouveau souvenir » puis « + », fenêtre de création (« Mémoire », « Créer »), menu « ⋮ » d'un souvenir (modifier, « Passer à l'échelle mondiale », supprimer) | [11](../manuel/11-memoires-taches-et-routage.md) |
| Menu du compte | pastille aux initiales (multi-utilisateur) | « Compte », « Support », « Déconnexion » | [13](../manuel/13-comptes-equipe-et-widget.md) |
| Compte | menu du compte (multi-utilisateur) › « Compte » | photo, nom d'utilisateur, mot de passe, « Thème », « Langue », « Mettre à jour le compte » | [13](../manuel/13-comptes-equipe-et-widget.md) |
| Codes de récupération | première connexion d'un compte (multi-utilisateur) | fenêtre « Recovery Codes », « Download », « Close » | [13](../manuel/13-comptes-equipe-et-widget.md) |

## Réglages d'un espace de travail

| Page ou menu | Chemin d'accès | Éléments (boutons, onglets, réglages) | Manuel qui le couvre |
|---|---|---|---|
| Paramètres généraux | roue dentée de l'espace › « Paramètres généraux » | flèche de retour vers la discussion, « Nom des espaces de travail », « Messages de chat suggérés », « Supprimer l'espace de travail » | [07](../manuel/07-regler-un-espace-de-travail.md), [14](../manuel/14-cas-pratiques.md) |
| Paramètres du chat | › « Paramètres du chat » | fournisseur et modèle de l'espace, mode (« Agent », « Chat », « Requête »), « Historique des chats », invite système et « View History », « Réponse de refus en mode requête », « Température LLM » | [07](../manuel/07-regler-un-espace-de-travail.md) |
| Base de données vectorielle | › « Base de données vectorielle » | identifiant, « Nombre de vecteurs », préférence de recherche (« Default », « Accuracy Optimized »), « Nombre maximum de contextes », « Seuil de similarité des documents », « Réinitialiser la base de données vectorielle » | [07](../manuel/07-regler-un-espace-de-travail.md) |
| Membres | › « Membres » (multi-utilisateur) | liste des membres, « Manage Users » | [13](../manuel/13-comptes-equipe-et-widget.md) |
| Configuration de l'agent | › « Configuration de l'agent » | fournisseur et modèle de l'agent de l'espace, « Configure Agent Skills » | [07](../manuel/07-regler-un-espace-de-travail.md), [10](../manuel/10-agents-et-outils.md) |

## Paramètres de l'instance

| Page ou menu | Chemin d'accès | Éléments (boutons, onglets, réglages) | Manuel qui le couvre |
|---|---|---|---|
| Préférence LLM | Paramètres › Fournisseurs d'IA › « Préférence LLM » | fournisseur, « Base URL », « API Key », « Selected Model », « Model context window », « Max Tokens », « Save changes » | [03](../manuel/03-premiers-pas.md), [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Base de données vectorielle | › « Base de données vectorielle » | LanceDB (défaut) et autres bases | [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Préférences d'intégration | › « Préférences d'intégration » | fournisseur d'embedding, « Base URL », « Embedding Model », « Max embedding chunk length », clé, réglages avancés | [03](../manuel/03-premiers-pas.md), [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Diviseur de texte et découpage | › « Diviseur de texte et découpage » | « Taille des segments de texte », « Chevauchement des segments de texte » | [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Génération d'images | › « Génération d'images » | fournisseur d'images | [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Voix et Parole | › « Voix et Parole » | « Speech-to-text Preference », synthèse vocale (System native, PiperTTS, OpenAI Compatible…) | [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Modèle de transcription | › « Modèle de transcription » | OpenAI, OpenAI Compatible, AnythingLLM Built-In ; « Base URL », « API Key », « Transcription Model », « Save changes » | [03](../manuel/03-premiers-pas.md) |
| Routeur modèle | › « Routeur modèle » | « Nouveau routeur » (fenêtre « Créer un nouveau routeur »), liste des routeurs avec crayon (modifier) et croix (supprimer) | [11](../manuel/11-memoires-taches-et-routage.md) |
| Utilisateurs | Paramètres › Admin › « Utilisateurs » (multi-utilisateur) | « Add user », rôles Default, Manager, Administrator, « Edit », « Suspend », « Delete » | [13](../manuel/13-comptes-equipe-et-widget.md) |
| Espaces de travail | › « Espaces de travail » (multi-utilisateur) | « New Workspace », liste (lien de l'espace, nombre d'utilisateurs), suppression | [12](../manuel/12-personnaliser-et-administrer.md) |
| Chat de l'espace de travail | › « Chat de l'espace de travail » | historique de toutes les conversations, corbeille par message, pages suivantes, « Exporter », « Clear Chats » | [12](../manuel/12-personnaliser-et-administrer.md) |
| Invitation | › « Invitation » (multi-utilisateur) | « Create Invite Link » (fenêtre « Create new invite »), « Copy Invite Link », corbeille par invitation | [13](../manuel/13-comptes-equipe-et-widget.md) |
| Default System Prompt | › « Default System Prompt » | « System Prompt », « Save Changes » | [12](../manuel/12-personnaliser-et-administrer.md) |
| Compétences de l'agent | Paramètres › « Compétences de l'agent » | compétences intégrées (« Agent Skills ») avec interrupteur et barre « Cancel » / « Save », « Agent Flows » (« Create Flow », puis « Open Builder » quand un flow existe), « Serveurs MCP » (« Rafraîchir ») | [10](../manuel/10-agents-et-outils.md) |
| Compétences de l'agent, éléments non décrits | même page | section « App Integrations » (Connecteur GMail, Google Calendar, Outlook), compétence « Créer des tâches planifiées », bouton à curseurs d'« Agent Skills » | Non couvert : connecteurs vers des comptes en ligne (hors périmètre) ; réglages avancés non essayés |
| Compétences personnalisées | même page, « Custom Skills » | import de compétences écrites en code | Non couvert : aucune compétence personnalisée importée (demande du code tiers à relire) |
| Éditeur d'agent flow | › « Agent Flows » › « Create Flow » | « Flow Name », « Description », « Add Block », « Save », « Publish », flèche « < » de retour | [10](../manuel/10-agents-et-outils.md) |
| Bouton « Open Builder » | « Agent Flows », quand un flow existe | ouvre l'éditeur sur un flow existant | Non couvert : le manuel décrit la création d'un flow (« Create Flow »), pas sa réouverture |
| Centre communautaire | Paramètres › « Centre communautaire » | « Découvrez les tendances », « Votre compte », « Importer », « Explore More », « Import » | Non couvert : contenu chargé depuis un service en ligne qui demande un compte ; hors périmètre (aucun compte en ligne) |
| Interface | Paramètres › Apparence › « Interface » | « Thème », « Palette de couleurs », « Langue d'affichage » | [03](../manuel/03-premiers-pas.md), [12](../manuel/12-personnaliser-et-administrer.md) |
| Personnalisation | › « Personnalisation » | onglets Identité, Couleurs, Barre latérale, Navigateur ; nom de l'application, logo, e-mail de support | [12](../manuel/12-personnaliser-et-administrer.md) |
| Chat (apparence) | › « Chat » | « Soumission automatique », « Rendu HTML » | [12](../manuel/12-personnaliser-et-administrer.md) |
| Chat (apparence), autres options | › « Chat » | lecture automatique, correction orthographique, barre de défilement, « Désactiver le défilement automatique » | [12](../manuel/12-personnaliser-et-administrer.md) (résumées en une phrase, sans libellé exact) |
| Canaux, Telegram | Paramètres › « Canaux » (mono-utilisateur) | connexion d'un robot Telegram | Non couvert : demande un compte Telegram en ligne (hors périmètre) ; page montrée au [chapitre 12](../manuel/12-personnaliser-et-administrer.md) |
| Widgets de chat intégrés | Paramètres › Outils › « Widgets de chat intégrés » | « Créer un widget intégré », onglets « Widgets » et « History », actions « Code », « Disable », « Delete » | [13](../manuel/13-comptes-equipe-et-widget.md) |
| Fenêtre de création d'un widget | « Créer un widget intégré » | « Workspace », mode « Chat » ou « Query », « Restrict requests from domains », « Max chats per day », « Max chats per session », « Message History Limit », trois interrupteurs « Enable … », « Cancel », « Create embed » | [13](../manuel/13-comptes-equipe-et-widget.md) |
| Journaux d'événements | › « Journaux d'événements » | liste des événements, « show », « Effacer les journaux d'événements », pages suivantes | [12](../manuel/12-personnaliser-et-administrer.md) |
| Tâches planifiées | › « Tâches planifiées » (mono-utilisateur seulement) | création d'une tâche, exécutions | [11](../manuel/11-memoires-taches-et-routage.md) |
| Clés API | › « Clés API » | « Générer une nouvelle clé API » (fenêtre « Créer une nouvelle clé API »), « Copier la clé API », corbeille par clé, lien vers la documentation de l'API | [12](../manuel/12-personnaliser-et-administrer.md) |
| Variables de prompt système | › « Variables de prompt système » | variables de la consigne, « Add Variable » | [12](../manuel/12-personnaliser-et-administrer.md) |
| Extension de navigateur | › « Extension de navigateur » | « Generate New API Key » | [12](../manuel/12-personnaliser-et-administrer.md) |
| AnythingLLM Mobile | › « AnythingLLM Mobile » | appareils connectés, « Register New Device », fenêtre de présentation (code QR, « Learn more », croix) | Non couvert : demande l'application mobile (hors périmètre de la fiche) ; page montrée au [chapitre 12](../manuel/12-personnaliser-et-administrer.md) |
| Sécurité | Paramètres › « Sécurité » (mono-utilisateur) | mot de passe de l'instance, « Mode multi-utilisateurs » | [13](../manuel/13-comptes-equipe-et-widget.md) |
| Confidentialité et données | lien en bas du menu des paramètres | fournisseurs et ce qu'ils voient, télémétrie | [08](../manuel/08-choisir-les-modeles-et-la-lecture-des-documents.md) |
| Bas du menu des paramètres | menu « Paramètres de l'instance » | flèche de retour vers l'écran principal | [03](../manuel/03-premiers-pas.md) |
| Contacter le Support | lien en bas du menu des paramètres | adresse de contact de l'éditeur | Non couvert : lien vers un service en ligne |
| Documentation de l'API | adresse `/api/docs` (lien « Lisez la documentation de l'API » de la page « Clés API ») | « Authorize », routes regroupées par thème | [12](../manuel/12-personnaliser-et-administrer.md) |
| Fonctionnalités expérimentales | Paramètres › « Fonctionnalités Expérimentales » (entrée visible en multi-utilisateur ; en mode « Juste moi », après Ctrl maintenu 3 s) | fenêtre des conditions (« I understand », « Reject & close »), « Live Document Sync » | [12](../manuel/12-personnaliser-et-administrer.md) |

## Écrans secondaires

| Page ou menu | Chemin d'accès | Éléments (boutons, onglets, réglages) | Manuel qui le couvre |
|---|---|---|---|
| Acceptation d'une invitation | lien d'invitation (`/accept-invite/<code>`) | choix du nom d'utilisateur et du mot de passe | Non couvert : l'acceptation par la personne invitée n'a pas été essayée ; création du lien au [chapitre 13](../manuel/13-comptes-equipe-et-widget.md) |
| Connexion unique (SSO) | `/sso/simple` | connexion par jeton externe | Non couvert : demande un fournisseur d'identité externe, non configuré |
| Page introuvable | toute adresse inconnue | message d'erreur 404 | Non couvert : page d'erreur sans action |
| Règles d'un routeur | Routeur modèle › ligne d'un routeur (`/settings/model-routers/<id>`) | règles de routage | Non couvert : règles non décrites ; création du routeur au [chapitre 11](../manuel/11-memoires-taches-et-routage.md) |
| Exécutions d'une tâche planifiée | Tâches planifiées › ligne d'une tâche (`/settings/scheduled-jobs/<id>/runs`) | liste et détail des exécutions | Non couvert : aucune exécution observée pendant les essais ; création de la tâche au [chapitre 11](../manuel/11-memoires-taches-et-routage.md) |
| Gestion des documents surveillés | Fonctionnalités expérimentales › « Manage Watched Documents » | documents suivis par Live Document Sync | Non couvert : aucun document mis sous surveillance ; fonction présentée au [chapitre 12](../manuel/12-personnaliser-et-administrer.md) |

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
