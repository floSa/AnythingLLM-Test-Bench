# Cadrage de l'interface AnythingLLM v1.19.0 (frontend) pour les captures Playwright

Source lue (lecture seule, rien lancé côté application) : `sources/anythingllm/frontend` (version `1.19.0` dans `frontend/package.json`).
Tous les chemins ci-dessous sont relatifs à `sources/anythingllm/frontend/src/` sauf mention contraire.
Cible : édition Docker, mode multi-utilisateur, rôle `admin`.

Méthode : routes lues dans `main.jsx`, garde-fous de rôle dans `components/PrivateRoute/index.jsx`, menu des réglages dans `components/SettingsSidebar/index.jsx`. Les traductions ont été aplaties (script Node lancé hors du dépôt, sur une copie de `locales/en/common.js` et `locales/fr/common.js`) puis comparées clé par clé.

Convention : « FR » = libellé de `locales/fr/common.js`, suivi de la clé entre crochets. « EN codé en dur » = texte écrit directement dans le JSX, qui reste en anglais même avec l'interface en français.

---

## 0. Points à retenir pour Playwright (synthèse)

1. **Aucun `data-testid`** dans tout le frontend (0 occurrence). Il faut viser les `id`, les `name`, les `aria-label`, les `placeholder` et le texte visible.
2. **Le français est complet côté clés** : 1 278 clés EN, 1 278 clés FR, aucune absente, aucune `null`, 39 identiques (mots transparents comme « Chat », « Admin », « Sources », « Document »). **Mais une part importante de l'interface est écrite en anglais en dur** : environ 1 354 appels `t("…")` contre environ 500 lignes de texte anglais en dur, réparties dans 164 fichiers (estimation par expression régulière). Les zones touchées sont listées au §3.
3. **Langue** : réglée côté navigateur seulement (i18next + `i18next-browser-languagedetector` 7.2.1), stockée dans `localStorage["i18nextLng"]`. Ce n'est pas un réglage serveur. Pour Playwright : `locale: "fr-FR"` dans le contexte, ou mieux `localStorage.setItem("i18nextLng","fr")` avant chargement (voir §3).
4. **Libellé « Show Citations » : absent en 1.19.0.** Le bouton sous chaque réponse s'appelle « Sources » [`chat_window.sources`], identique en FR et en EN (voir §5).
5. **Menu des réglages en mode multi-utilisateur** : « Sécurité » est **masqué** (route toujours accessible par URL), « Canaux / Telegram » est **masqué**, « Tâches planifiées » est **masqué et la route redirige vers l'accueil** (`SingleUserRoute`). « Fonctionnalités Expérimentales » est caché tant qu'on n'a pas maintenu Ctrl (ou Cmd) 3 s, ou posé `localStorage["anythingllm_experimental_feature_preview_unlocked"]="enabled"`.
6. **Les réglages d'un workspace s'enregistrent seuls** (`components/AutosaveForm/index.jsx`) : un champ texte est enregistré quand il perd le focus, une liste dès qu'on la change. Il n'y a pas de bouton « Enregistrer ». Une coche « Enregistré » [`common.saved`] s'affiche 2 s à côté du libellé du champ.
7. **Onboarding multi-utilisateur** : l'admin est connecté automatiquement. Ses codes de récupération sont générés et marqués comme vus sans être affichés, donc la fenêtre « Recovery Codes » ne s'ouvrira pas pour lui. Elle s'ouvrira à la première connexion de chaque nouvel utilisateur (fenêtre en anglais en dur, bouton « Download » puis « Close » obligatoires).
8. **Connexion par nom d'utilisateur, pas par e-mail** : `input[name="username"]` et `input[name="password"]`.

---

## 1. Routes (`main.jsx`, `utils/paths.js`, `components/PrivateRoute/index.jsx`)

Gardes :
- `PrivateRoute` : toute personne connectée. Sans session, redirection vers `/login`.
- `ManagerRoute` : `admin` ou `manager` (en mode utilisateur unique : tout le monde).
- `AdminRoute` : `admin` seulement.
- `SingleUserRoute` : mode utilisateur unique seulement. En mode multi-utilisateur, redirection vers `/`.

Dans tous les cas, si l'onboarding n'est pas terminé, redirection vers `/onboarding`.

| Chemin URL | Composant (fichier) | Rôle requis |
|---|---|---|
| `/` | `pages/Main` → `pages/Main/Home` | connecté |
| `/login` (`?nt=1`) | `pages/Login` → `components/Modals/Password/MultiUserAuth.jsx` | public |
| `/sso/simple` | `pages/Login/SSO/simple` | public |
| `/onboarding`, `/onboarding/:step` (`home`, `llm-preference`, `user-setup`, `data-handling`, `survey`) | `pages/OnboardingFlow` | public (redirige vers `/` si l'onboarding est déjà fait) |
| `/accept-invite/:code` | `pages/Invite` | public |
| `/workspace/:slug` et `/workspace/:slug/t/:threadSlug` | `pages/WorkspaceChat` | connecté |
| `/workspace/:slug/settings/:tab` (`general-appearance`, `chat-settings`, `vector-database`, `members`, `agent-config`) | `pages/WorkspaceSettings` | manager |
| `/settings/llm-preference` | `pages/GeneralSettings/LLMPreference` | admin |
| `/settings/vector-database` | `pages/GeneralSettings/VectorDatabase` | admin |
| `/settings/embedding-preference` | `pages/GeneralSettings/EmbeddingPreference` | admin |
| `/settings/text-splitter-preference` | `pages/GeneralSettings/EmbeddingTextSplitterPreference` | admin |
| `/settings/image-generation-preference` | `pages/GeneralSettings/ImageGenerationPreference` | admin |
| `/settings/audio-preference` | `pages/GeneralSettings/AudioPreference` (`stt.jsx` + `tts.jsx`) | admin |
| `/settings/transcription-preference` | `pages/GeneralSettings/TranscriptionPreference` | admin |
| `/settings/model-routers`, `/settings/model-routers/:id` | `pages/GeneralSettings/ModelRouters` (+ `RouterRulesPage`) | admin |
| `/settings/users` | `pages/Admin/Users` | manager |
| `/settings/workspaces` | `pages/Admin/Workspaces` | manager |
| `/settings/workspace-chats` | `pages/GeneralSettings/Chats` | manager |
| `/settings/invites` | `pages/Admin/Invitations` | manager |
| `/settings/default-system-prompt` | `pages/Admin/DefaultSystemPrompt` | admin |
| `/settings/agents` | `pages/Admin/Agents` | admin |
| `/settings/agents/builder`, `/settings/agents/builder/:flowId` | `pages/Admin/AgentBuilder` (sans menu utilisateur) | admin |
| `/settings/community-hub/trending` · `/authentication` · `/import-item` | `pages/GeneralSettings/CommunityHub/*` | admin |
| `/settings/interface` | `pages/GeneralSettings/Settings/Interface` | manager |
| `/settings/branding` (`?tab=identity|colors|sidebar|browser`) | `pages/GeneralSettings/Settings/Branding` | manager |
| `/settings/chat` | `pages/GeneralSettings/Settings/Chat` | manager |
| `/settings/external-connections/telegram` | `pages/GeneralSettings/Connections/TelegramBot` | admin (masqué du menu en multi-utilisateur) |
| `/settings/embed-chat-widgets` | `pages/GeneralSettings/ChatEmbedWidgets` | admin |
| `/settings/event-logs` | `pages/Admin/Logging` | admin |
| `/settings/scheduled-jobs` (+ `/:id/runs`, `/:id/runs/:runId`) | `pages/GeneralSettings/ScheduledJobs` | **mode utilisateur unique seulement** |
| `/settings/api-keys` | `pages/GeneralSettings/ApiKeys` | admin |
| `/settings/system-prompt-variables` | `pages/Admin/SystemPromptVariables` | admin |
| `/settings/browser-extension` | `pages/GeneralSettings/BrowserExtensionApiKey` | manager |
| `/settings/mobile-connections` | `pages/GeneralSettings/MobileConnections` | manager (menu : admin) |
| `/settings/security` | `pages/GeneralSettings/Security` | manager (masqué du menu en multi-utilisateur) |
| `/settings/privacy` | `pages/GeneralSettings/PrivacyAndData` | admin (lien en bas du menu) |
| `/settings/beta-features` | `pages/Admin/ExperimentalFeatures` | admin |
| `/settings/beta-features/live-document-sync/manage` | `pages/Admin/ExperimentalFeatures/Features/LiveSync/manage` | admin |
| `*` | `pages/404.jsx` | — |

« Memories » n'a **pas de page** dans `/settings`. Les souvenirs passent par un panneau latéral du chat (voir §1.6).

### 1.1 Connexion (`/login`)

Fichier `components/Modals/Password/MultiUserAuth.jsx`.
- Titre « Bienvenue » [`login.multi-user.welcome`], sous-titre « Connectez-vous à votre compte {{appName}}. » [`login.sign-in`].
- Champ « Nom d'utilisateur » [`login.multi-user.placeholder-username`] : `input[name="username"]`. Ces libellés sont des `<label>` sans `for`, donc pas de `placeholder`.
- Champ « Mot de passe » [`login.multi-user.placeholder-password`] : `input[name="password"]` (composant `PasswordInput`, bouton œil `aria-label="Hold to show password"`).
- Bouton « Connexion » [`login.multi-user.login`], qui devient « Validation... » pendant l'envoi : `button[type="submit"]`.
- Lien « Mot de passe oublié? Réinitialiser » [`login.multi-user.forgot-pass`, `login.multi-user.reset`]. Il ouvre le formulaire « Réinitialisation du mot de passe » : nom d'utilisateur, puis « Codes de récupération » `recoveryCode1..4`, puis « Retour à la connexion ».
- En cas d'erreur : `Error: <message>` (EN codé en dur).
- La session est stockée dans `localStorage` sous les clés `anythingllm_user`, `anythingllm_authToken` et `anythingllm_authTimestamp` (`utils/constants.js`).
- Fenêtre « Recovery Codes » (`components/Modals/DisplayRecoveryCodeModal`, **EN codé en dur**) : 4 codes UUID, bouton « Download » puis « Close ». On ne peut pas la fermer avant d'avoir cliqué « Download ». Elle apparaît si le serveur renvoie `recoveryCodes`, c'est-à-dire à la première connexion d'un utilisateur (`server/endpoints/system.js` l. 300).

### 1.2 Page d'accueil (`/`)

Fichiers `pages/Main/Home/index.jsx` et `pages/Main/index.jsx`.
- Message d'accueil aléatoire qui dépend de l'heure : « Comment puis-je vous aider aujourd'hui ? » [`main-page.greeting`] ou une variante [`main-page.greetings.*`].
- La barre de saisie centrée (même composant que dans le chat, §1.4) écrit dans le dernier workspace ou en crée un « Mon Espace de Travail » [`new-workspace.placeholder`].
- Actions rapides (`components/lib/QuickActions`) : « Créer un agent » [`main-page.quickActions.createAgent`] mène à `/settings/agents`. « Modifier l'espace de travail » [`main-page.quickActions.editWorkspace`]. « Télécharger un document » [`main-page.quickActions.uploadDocument`] clique sur `#dnd-chat-file-uploader`, c'est-à-dire une pièce jointe au chat, **pas** le gestionnaire de documents.
- Messages suggérés (`components/lib/SuggestedMessages`), sélecteur de modèle en haut (`WorkspaceModelPicker`), menu des réglages du chat (`ChatSettingsMenu`).
- Un utilisateur `default` sans workspace voit le texte [`home.notAssigned`].

### 1.3 Barre latérale (`components/Sidebar/*`)

- Logo : lien `a[aria-label="Home"]`.
- Bouton masquer/afficher : `aria-label="Hide Sidebar (<raccourci>)"` / `"Show Sidebar (…)"` (EN codé en dur).
- Champ de recherche : `placeholder` « Rechercher » [`common.search`] (`Sidebar/SearchBox`).
- **Nouveau workspace** : bouton « + » à côté de la recherche (`ShortWidthNewWorkspaceButton`), avec `data-tooltip-id="new-workspace-tooltip"` et l'info-bulle « Nouvel Espace de Travail » [`new-workspace.title`]. Masqué pour le rôle `default`. Sélecteur : `button[data-tooltip-id="new-workspace-tooltip"]`.
  - Fenêtre `components/Modals/NewWorkspace.jsx` : titre « Nouvel Espace de Travail », champ « Nom des espaces de travail » [`common.workspaces-name`], `input#name[name="name"]`, placeholder « Mon Espace de Travail ». Bouton **« Save »** (EN codé en dur), `button[type="submit"]`. Après validation, navigation vers `/workspace/<slug>`.
- Liste des workspaces : `[aria-label="Workspaces"]`, chaque élément `[role="listitem"]`, réordonnable par la poignée (glisser-déposer).
  - Lien `a[href="/workspace/<slug>"]`, `aria-current="page"` quand il est actif.
  - Icône d'envoi (visible au survol ou quand le workspace est actif), `button[data-tooltip-id="upload-workspace"]`, info-bulle « Upload documents to this workspace for RAG indexing » (EN codé en dur). Elle ouvre le gestionnaire de documents (§1.5).
  - Roue dentée, `button[aria-label="General appearance settings"]` (EN codé en dur). Elle mène à `/workspace/<slug>/settings/general-appearance`.
- Fils de discussion du workspace actif (`ThreadContainer`, `[aria-label="Threads"]`) : fil « default », bouton « New Thread » (« Starting Thread... » pendant la création), fil virtuel « *New Thread ». Menu d'un fil : `button[aria-label="Thread options"]`, avec « Rename » (fenêtre `window.prompt` native : « What would you like to rename this thread to? ») et « Delete Thread ». Avec Ctrl enfoncé, sélection multiple puis « Delete Selected ». Tout cela est **EN codé en dur**.
- Pied de la barre (`components/Footer`) : liens GitHub (`aria-label="Find us on GitHub"`), Docs (`aria-label="Docs"`), Discord (`aria-label="Join our Discord server"`). **Bouton Réglages** `a[aria-label="Settings"]` (info-bulle « Open settings »), qui mène à **`/settings/interface`**. Il est masqué pour le rôle `default`.
- Menu utilisateur en haut à droite (`components/UserMenu/UserButton`) : pastille avec l'initiale, puis « Compte » [`profile_settings.account`], « Support » [`profile_settings.support`] et « Déconnexion » [`profile_settings.signout`].
  - Fenêtre « Compte » (`UserMenu/AccountModal`) : « Modifier le compte » [`profile_settings.edit_account`], photo de profil, nom d'utilisateur, nouveau mot de passe, Bio (EN codé en dur). « Thème » [`profile_settings.theme`] `select[name="theme"]`. **« Langue » [`profile_settings.language`] `select[name="userLang"]`**. Envoi automatique et lecture automatique. Boutons « Annuler » / « Mettre à jour le compte ».

### 1.4 Fenêtre de chat (`/workspace/:slug[/t/:thread]`)

Fichiers sous `components/WorkspaceChat/ChatContainer/`.

**Barre de saisie** (`PromptInput/index.jsx`) :

| Élément | Sélecteur | Libellé FR [clé] |
|---|---|---|
| Conteneur | `#prompt-input-wrapper` | — |
| Zone de texte | `textarea#primary-prompt-input` | placeholder « Envoyer un message » [`chat_window.send_message`] |
| Pièce jointe (+) | `#attach-item-btn` | aria-label « Joindre un fichier » [`chat_window.attach_file`]. Il clique `input#dnd-chat-file-uploader`. |
| @agent | `button[aria-label="Démarrer la session de l'agent"]` (`data-tooltip-id="agent-session"`) | [`chat_window.start_agent_session`]. Il insère `@agent` au début du message. Visible seulement si l'agent est disponible pour le workspace. |
| Effort de raisonnement | `button[data-tooltip-id="reasoning-effort"]` | [`chat.reasoning_effort.title`]. Affiché seulement si le modèle le permet. |
| Outils | `#tools-btn` | « Outils » [`chat_window.tools`]. Il ouvre `ToolsMenu` avec 2 onglets : « Commandes abrégées » [`chat_window.slash_commands`] et « Compétences des agents » [`chat_window.agent_skills`]. Taper `/` l'ouvre aussi. |
| Micro | `button[aria-label="Enregistrer un message vocal"]` (`data-tooltip-id="tooltip-microphone-btn"`) | [`chat_window.microphone`], raccourci CTRL + M |
| Envoyer | `#send-prompt` (aria-label « Envoyer le message au chatbot » [`chat_window.send`]) | — |
| Arrêter | `#stop-generation-button`, `aria-label="Stop generating"` (EN codé en dur) | info-bulle « Arrêtez de générer des réponses » [`chat_window.stop_generating`] |

- Commandes abrégées : préréglages `/reset` (« Efface l'historique du chat actuel… » [`chat_window.preset_reset_description`]) et `/img` [`chat_window.preset_img_description`]. Bouton « Ajouter » [`chat_window.add_new`] qui ouvre la fenêtre « Ajouter une nouvelle commande preset » : `#command`, `#prompt`, `#description`, puis « Annuler » / « Sauvegarder ».
- Onglet Compétences : recherche « Rechercher », texte [`chat_window.use_agent_session_to_use_tools`], lien « Gérer les compétences des agents » [`chat_window.manage_agent_skills`].
- Sélecteur de modèle en tête du chat (`WorkspaceModelPicker`) : « Sélectionner le modèle » [`chat_window.select_model`]. Il ouvre `#llm-selector-modal` avec la recherche `#llm-search-input` (« Rechercher des modèles ») et le bouton « Sauvegarder ». Raccourci ⌘/Ctrl + Shift + L.
- Menu des réglages du chat (`ChatSettingsMenu`, icône curseurs, **sans aria-label**) : « Taille du texte » (Petit / Normal / Grand), « Souvenirs » [`chat_window.memories.title`] (toujours visible pour un admin), « Exporter la conversation au format... » [`chat_window.export`] (si l'historique n'est pas vide), « Copy chat link » (EN codé en dur).
- Glisser-déposer : un calque « Add anything / Drop a file or image here to attach it to your workspace auto-magically. » (EN codé en dur). Un fichier déposé dans le chat est **analysé et joint au fil, pas intégré**. Le menu `ParsedFilesMenu` propose « Embed Files into Workspace ». Si le contexte dépasse : fenêtre « Context Window Warning » (EN codé en dur), puis « Embedding files ».
- Actions sur une réponse (`ChatHistory/HistoricalMessage/Actions`) : lecture audio (« Speak message » / « Pause speech », EN codé en dur), « Copier » [`chat_window.copy`], « Régénérer » [`chat_window.regenerate`], « Bonne réponse » [`chat_window.good_response`] (pouce), modification (`aria-label="Edit Modifier le prompt"` ou « … la réponse »), « Plus d'actions » [`chat_window.more_actions`] qui contient « Dupliquer » [`chat_window.fork`] et « Supprimer » [`chat_window.delete`]. Il y a aussi les métriques (`data-tooltip-id="metrics-visibility"`).

### 1.5 Gestion des documents (fenêtre `components/Modals/ManageWorkspace`)

On l'ouvre par l'icône d'envoi du workspace dans la barre latérale.
- En-tête : bouton de fermeture (icône X, **sans aria-label**). Onglets « Documents » [`connectors.manage.documents`] et « Connecteurs de données » [`connectors.manage.data-connectors`], masqués pour le rôle `default`.
- **Colonne gauche « Mes documents »** [`connectors.directory.my-documents`] (`Documents/Directory`) :
  - Recherche, placeholder « Rechercher un document » [`connectors.directory.search-document`]. Bouton « Nouveau dossier » [`connectors.directory.new-folder`], fenêtre `NewFolderModal`.
  - Zone d'envoi (`Documents/UploadFile`) : « Cliquez pour télécharger ou glissez-déposez » [`connectors.upload.click-upload`], « prend en charge les fichiers texte, CSV… » [`connectors.upload.file-types`]. Il y a un `<input type="file">` caché, généré par react-dropzone : `page.setInputFiles()` sur l'`input[type=file]` de cette zone.
  - Lien web : « ou soumettre un lien » [`connectors.upload.or-submit-link`], placeholder « https://exemple.com », bouton « Récupérer le site web » [`connectors.upload.fetch-website`]. Note : « Ces fichiers seront téléchargés sur cette instance AnythingLLM uniquement. » [`connectors.upload.privacy-notice`]. Si le collecteur est absent : « Processeur de documents hors ligne » [`connectors.upload.processor-offline`].
  - Lignes : `#directory-item`, case à cocher, badge « Cached » (EN codé en dur). Une fois des lignes sélectionnées, le bouton **« Déplacer vers l'espace de travail »** [`connectors.directory.move-workspace`] apparaît, avec à côté une icône « déplacer vers un dossier » (`FolderSelectionPopup`) et une corbeille (suppression, confirmation [`connectors.directory.delete-confirmation`]).
- **Colonne droite = le workspace** (`Documents/WorkspaceDirectory`) : en-tête « Name » (EN codé en dur), lignes `#ws-directory-item`.
  - **Épingle** : `data-tooltip-id="pin-document"`, info-bulle « Pin to workspace » / « Un-pin from workspace » (EN codé en dur), badge « Pinned ». La première fois, une fenêtre explique : « Qu'est-ce que l'épinglage de documents ? » [`connectors.pinning.what_pinning`], bouton « J'ai compris » [`connectors.pinning.accept`].
  - Surveillance (œil, `data-tooltip-id="watch-changes"`) : visible seulement si la fonction expérimentale Live Document Sync est activée. Fenêtre « Qu'est-ce que la surveillance de documents ? ».
  - Retrait : `data-tooltip-id="remove-document"`, « Remove document from workspace » (EN codé en dur). Sélection multiple : « Tout sélectionner » / « Tout désélectionner » / « Supprimer la sélection ».
  - **« Sauvegarder et intégrer » [`connectors.directory.save_embed`]** (EN : « Save and Embed ») : ce bouton n'apparaît que s'il y a des changements en attente (`hasChanges`), c'est-à-dire après un « Déplacer vers l'espace de travail ». Sélecteur : `getByRole("button", { name: "Sauvegarder et intégrer" })`. Il lance l'intégration, avec la progression `EmbeddingProgressProvider`.
- Onglet Connecteurs de données : GitHub, GitLab, Gitea, YouTube, Site web (website-depth), Confluence (libellés traduits [`connectors.<x>.name`]), plus Drupal Wiki, Obsidian et Paperless-ngx (EN codé en dur). Recherche [`connectors.search-placeholder`].
- Sur mobile : « Cette fonctionnalité n'est disponible que sur ordinateur de bureau. » [`connectors.manage.desktop-only`].

### 1.6 Souvenirs (Memories)

Il n'y a pas de route. On passe par le panneau `ChatContainer/MemoriesSidebar`, ouvert depuis le menu des réglages du chat, entrée « Souvenirs ».
- Onglets « Espace de travail » / « Global » (`#memories-workspace-pill`).
- Interrupteurs « Activer la personnalisation » [`chat_window.memories.toggle.label`] et « Souvenirs automatisés » [`chat_window.memories.auto_extraction.label`].
- État vide [`chat_window.memories.empty`], lien « créer un nouveau souvenir ».
- Fenêtre « Créer un souvenir » (champ « Mémoire », boutons « Créer » / « Annuler »). Menu d'une carte : Modifier / Passer à l'échelle mondiale / Passer à l'espace de travail / Supprimer.

### 1.7 Réglages d'un workspace (`/workspace/:slug/settings/:tab`)

Fichiers `pages/WorkspaceSettings/*`. Rôle `manager` ou `admin`. Enregistrement automatique (voir §0 point 6). Les valeurs par défaut viennent du frontend et sont confirmées par `server/prisma/schema.prisma` l. 127-141.

Onglets : « Paramètres généraux » [`workspaces—settings.general`], « Paramètres du chat » [`workspaces—settings.chat`], « Base de données vectorielle » [`workspaces—settings.vector`], « Membres » [`workspaces—settings.members`] (visible pour admin et manager), « Configuration de l'agent » [`workspaces—settings.agent`]. Une flèche ramène au chat.

**Paramètres généraux** (`general-appearance`) :
- « Nom des espaces de travail » [`common.workspaces-name`], `input[name="name"]`, placeholder « My Workspace » (EN), aide [`general.names.description`].
- « Messages de chat suggérés » [`general.message.title`] : `input[name="message"]` (placeholder « Message »), « Ajouter un nouveau message », « Enregistrer les messages ». 4 messages au maximum. Les exemples par défaut sont « Expliquez-moi » / « les avantages de AnythingLLM ».
- « Supprimer l'Espace de Travail » [`general.delete.title`], bouton « Supprimer l'espace de travail » [`general.delete.delete`], confirmation `window.confirm`. Absent si `WorkspaceDeletionProtection` est actif.

**Paramètres du chat** (`chat-settings`, `form#chat-settings-form`) :

| Champ | Clé FR | `name` | Défaut |
|---|---|---|---|
| Fournisseur LLM de l'espace de travail | `chat.llm.title` | `chatProvider` | « System default » (`default`) |
| Modèle de chat de l'espace de travail | `chat.model.title` | `chatModel` | vide = modèle du système |
| Model Router (si routeur choisi) | `model-router.router-selection.*` | `router_id` | — |
| Mode de chat : « Agent » / « Chat » / « Requête » | `chat.mode.title`, `chat.mode.{automatic,chat,query}.title` | `chatMode` (caché) | `chat` |
| Historique des chats | `chat.history.title` | `openAiHistory` | 20 |
| Invite (prompt système) | `chat.prompt.title` | `openAiPrompt` | prompt système par défaut de l'instance, avec historique des versions [`chat.prompt.history.*`] |
| Réponse de refus en mode requête | `chat.refusal.title` | `queryRefusalResponse` | « There is no relevant information in this workspace to answer your query. » (`utils/chat/index.js` l. 225) |
| Température LLM | `chat.temperature.title` | `openAiTemp` | vide, placeholder « Valeur par défaut du fournisseur » |

**Base de données vectorielle** (`vector-database`) :
- « Identifiant de la base de données vectorielle » [`vector-workspace.identifier`] (lecture seule).
- « Nombre de vecteurs » [`general.vector.title`].
- Préférence de recherche `select[name="vectorSearchMode"]` : « Default » / « Accuracy Optimized » (rerank, EN codé en dur). Affichée seulement si la base vectorielle est `lancedb`. Défaut `default`.
- « Nombre maximum de contextes » [`vector-workspace.snippets.title`], `topN`, défaut 4.
- « Seuil de similarité des documents » [`vector-workspace.doc.title`], `similarityThreshold`, défaut 0.25. Options : Aucune restriction / Bas ≥ .25 / Moyen ≥ .50 / Élevé ≥ .75.
- « Réinitialiser la base de données vectorielle » [`vector-workspace.reset.reset`], avec confirmation.

**Membres** (`members`) : tableau des membres, bouton **« Manage Users »** (EN codé en dur). Il ouvre une fenêtre avec la recherche « Search for a user », des cases à cocher et le bouton « Save ».

**Configuration de l'agent** (`agent-config`, `form#agent-settings-form`) :
- « Fournisseur LLM de l'agent de l'espace de travail » [`agent.provider.title`], `agentProvider`, défaut « System Default » (`none`, EN codé en dur). Recherche « Search available LLM providers ».
- « Modèle de l'agent de l'espace de travail » [`agent.mode.title`], `agentModel`.
- Avertissement de performance [`agent.performance-warning`] pour Ollama, LocalAI, etc.
- Lien « Configure Agent Skills » vers `/settings/agents` (EN codé en dur, admin).

---

## 1 bis. Réglages de l'instance (`/settings/...`) : menu latéral réel en 1.19.0

Fichier `components/SettingsSidebar/index.jsx`. Titre du menu : « Paramètres de l'instance » [`settings.title`]. Les groupes se déplient au clic (l'état est mémorisé dans `localStorage["anything_llm_menu_<libellé>_expanded"]`). Liens : `a[href="/settings/…"]`.

Visibilité ci-dessous pour un **admin en multi-utilisateur**.

| Groupe FR [clé] | Entrée FR [clé] | URL | Visible ? |
|---|---|---|---|
| Fournisseurs d'IA [`settings.ai-providers`] | Préférence LLM [`settings.llm`] | `/settings/llm-preference` | oui |
| | Base de données vectorielle [`settings.vector-database`] | `/settings/vector-database` | oui |
| | Préférences d'intégration [`settings.embedder`] | `/settings/embedding-preference` | oui |
| | Diviseur de texte et découpage [`settings.text-splitting`] | `/settings/text-splitter-preference` | oui |
| | Génération d'images [`settings.image-generation`] | `/settings/image-generation-preference` | oui |
| | Voix et Parole [`settings.voice-speech`] | `/settings/audio-preference` | oui |
| | Modèle de transcription [`settings.transcription`] | `/settings/transcription-preference` | oui |
| | Routeur modèle [`settings.model-router`] | `/settings/model-routers` | oui |
| Admin [`settings.admin`] | Utilisateurs [`settings.users`] | `/settings/users` | oui |
| | Espaces de travail [`settings.workspaces`] | `/settings/workspaces` | oui |
| | Chat de l'espace de travail [`settings.workspace-chats`] | `/settings/workspace-chats` | oui, sauf si `DISABLE_VIEW_CHAT_HISTORY` |
| | Invitation [`settings.invites`] | `/settings/invites` | oui |
| | « Default System Prompt » (**EN codé en dur**) | `/settings/default-system-prompt` | oui |
| Compétences de l'agent [`settings.agent-skills`] (entrée directe) | — | `/settings/agents` | oui |
| Centre communautaire [`settings.community-hub.title`] | Découvrez les tendances / Votre compte / Importer | `/settings/community-hub/{trending,authentication,import-item}` | oui (contenu chargé depuis Internet) |
| Apparence [`settings.customization`] | Interface [`settings.interface`] | `/settings/interface` | oui |
| | Personnalisation [`settings.branding`] | `/settings/branding` | oui |
| | Chat [`settings.chat`] | `/settings/chat` | oui |
| Canaux [`settings.channels`] | Telegram | `/settings/external-connections/telegram` | **non** (`hidden: !!user`, donc tout le groupe disparaît) |
| Outils [`settings.tools`] | Widgets de chat intégrés [`settings.embeds`] | `/settings/embed-chat-widgets` | oui, sauf si `DISABLE_VIEW_CHAT_HISTORY` |
| | Journaux d'événements [`settings.event-logs`] | `/settings/event-logs` | oui |
| | Tâches planifiées [`settings.scheduled-jobs`] | `/settings/scheduled-jobs` | **non** (et la route redirige) |
| | Clés API [`settings.api-keys`] (EN « Developer API ») | `/settings/api-keys` | oui |
| | Variables de prompt système [`settings.system-prompt-variables`] | `/settings/system-prompt-variables` | oui |
| | Extension de navigateur [`settings.browser-extension`] | `/settings/browser-extension` | oui |
| | AnythingLLM Mobile [`settings.mobile-app`] | `/settings/mobile-connections` | oui |
| Sécurité [`settings.security`] (entrée directe) | — | `/settings/security` | **non** (`hidden={user?.role}`), mais l'URL reste accessible |
| Fonctionnalités Expérimentales [`settings.experimental-features`] | — | `/settings/beta-features` | seulement après Ctrl/Cmd maintenu 3 s (toast « Experimental feature previews unlocked! ») ou la clé `localStorage` du §0 |
| (bas du menu) | Contacter le Support [`settings.contact`], Confidentialité et données [`settings.privacy`] (admin), numéro de version `v1.19.0` | `mailto:` / `/settings/privacy` / GitHub | oui |

Absents de la 1.19.0 : aucune entrée « Memories » ni « Security / Privacy & data » groupée. « Privacy » n'est qu'un petit lien en bas du menu.

### Contenu de chaque page de réglages

Le bouton d'enregistrement apparaît seulement après une modification (`hasChanges`). Son libellé est « Enregistrer les modifications » [`common.save`] sur les pages traduites, et « Save changes » (EN codé en dur) sur LLM et Voix.

- **Préférence LLM** (`LLMPreference`) : titre « Préférence LLM » [`llm.title`], « Fournisseur LLM » [`llm.provider`]. Le bouton-carte du fournisseur courant (`ProviderSearchMenu`, `button[type=button]`) ouvre une recherche, placeholder « Search all LLM providers ». La liste comprend notamment « Generic OpenAI » (`generic-openai`) et « Model Router ». Champs Generic OpenAI (`components/LLMSelection/GenericOpenAiOptions`, EN codé en dur) : « Base URL » `GenericOpenAiBasePath`, « API Key » `GenericOpenAiKey`, « Selected Model » `GenericOpenAiModelPref` (liste si `/models` répond, sinon champ libre), « Model context window » `GenericOpenAiTokenLimit`, « Max Tokens » `GenericOpenAiMaxTokens` (défaut 1024).
- **Base de données vectorielle** : `form#vectordb-form`, recherche « Search all vector database providers ». Choix : LanceDB (défaut), PGVector, Chroma, Chroma Cloud, Pinecone, Zilliz Cloud, QDrant, Weaviate, Milvus, AstraDB.
- **Préférences d'intégration** : `form#embedding-form`, recherche « Search all embedding providers ». Choix : AnythingLLM Embedder (`native`, défaut de l'onboarding), OpenAI, Azure OpenAI, Gemini, Local AI, Ollama, LM Studio, Lemonade, OpenRouter, LiteLLM, Cohere, Voyage AI, Mistral AI, Generic OpenAI. Champs Generic OpenAI (EN) : « Base URL » `EmbeddingBasePath`, « Embedding Model » `EmbeddingModelPref`, « Max embedding chunk length » `EmbeddingModelMaxChunkLength`, clé `GenericOpenAiEmbeddingApiKey`, et derrière « Show advanced settings » : « Max concurrent Chunks » et « Passage Prefix ».
- **Diviseur de texte** : `form#text-splitter-chunking-form`. « Taille des segments de texte » `text_splitter_chunk_size` (défaut 1000, plafonnée à la longueur maximale de l'embedder). « Chevauchement des segments de texte » `text_splitter_chunk_overlap` (défaut 20).
- **Génération d'images** : `form#image-generation-form`. Choix : OpenAI, Gemini, Ollama, Lemonade, LocalAI, llmman, OpenRouter.
- **Voix et Parole** (EN codé en dur) : « Speech-to-text Preference » (System native, OpenAI, Lemonade, Deepgram, Groq, Generic OpenAI) et la section TTS (System native, OpenAI, ElevenLabs, PiperTTS, Kokoro, OpenAI Compatible).
- **Modèle de transcription** : [`transcription.title`]. Choix : OpenAI, OpenAI Compatible, AnythingLLM Built-In (`local`).
- **Routeurs modèles** : [`model-router.title`], bouton « Nouveau routeur » [`model-router.new-router-button`]. Tableau Nom / Règles / Espaces de travail / Plan de secours.
- **Utilisateurs** (EN codé en dur) : titre « Users », bouton « Add user ». Fenêtre « Add user to instance » : `username` (placeholder « User's username »), `password`, `bio`, `select[name=role]` Default / Manager / Administrator, interrupteur « Limit messages per day ». Lignes : « Edit », « Suspend » / « Unsuspend », « Delete ».
- **Espaces de travail** (EN) : « Instance Workspaces », bouton « New Workspace », fenêtre « Create new workspace » / « Create workspace ». Colonnes Name / Link / Users / Created On.
- **Chat de l'espace de travail** : « Chats de l'espace de travail » [`recorded.title`], « Exporter » [`recorded.export`], « Clear Chats » (EN). Colonnes Id / Envoyé par / Espace de travail / Invite / Réponse / Envoyé à.
- **Invitations** (EN) : « Invitations », bouton « Create Invite Link ». Fenêtre « Create new invite » (case « Auto-add invitee to workspaces », bouton « Create Invite »). Lignes « Copy Invite Link », corbeille.
- **Default System Prompt** (EN) : un champ « System Prompt » et un bouton « Save Changes ».
- **Compétences de l'agent** (`pages/Admin/Agents`) : sections « Agent Skills », « App Integrations », « Custom Skills », « Agent Flows » (« Create Flow » / « Open Builder ») et « MCP Servers » [`agent.mcp.title`] (titres EN codés en dur). Compétences traduites : RAG et mémoire à long terme, Voir et résumer des documents, Récupérer des sites web, Recherche web en direct et navigation, Accès au système de fichiers, Création de documents, Générer des graphiques, Générer des images, Connecteur SQL, Créer des tâches planifiées, puis les connecteurs GMail, Google Calendar et Outlook. « Paramètres des compétences des agents » [`agent.settings.title`]. La barre d'enregistrement `ContextualSaveBar` affiche « Cancel » / « Save » (EN).
- **Interface** : « Thème » [`customization.items.theme.title`] (System / Light / Dark, stocké dans `localStorage["theme"]`), « Palette de couleurs », **« Langue d'affichage » [`customization.items.display-language.title`], `select[name="userLang"]`**.
- **Personnalisation** : onglets Identité / Couleurs / Barre latérale / Navigateur [`customization.branding.tabs.*`]. « Nom de l'application » (`customAppName`), « Logo » (`#logo-upload`), pied de page de la barre latérale, « E-mail de support » (`supportEmail`), apparence du navigateur (`meta_page_title`, `meta_page_favicon`). Boutons « Save » / « Clear » (EN).
- **Chat** (apparence) : Soumission automatique, Lecture automatique, Correction orthographique, Afficher la barre de défilement, Désactiver le défilement automatique, Rendu HTML.
- **Widgets de chat intégrés** : onglets « Widgets » / « History » (EN). « Widgets de chat intégrables » [`embeddable.title`], bouton « Créer un widget intégré ». Historique « Chats intégrés » [`embed-chats.title`].
- **Journaux d'événements** : [`event.title`], bouton « Effacer les journaux d'événements » [`event.clear`].
- **Clés API** : [`api.title`], bouton « Générer une nouvelle clé API » [`api.generate`]. Fenêtre « Créer une nouvelle clé API ».
- **Variables de prompt système** (EN) : tableau Value / Description / Type.
- **Extension de navigateur** (EN) : « Browser Extension API Keys », « Generate New API Key ».
- **AnythingLLM Mobile** (EN) : « Connected Mobile Devices ».
- **Sécurité** (accessible par URL) : « Mode multi-utilisateurs » [`security.multiuser.title`]. Une fois activé, il affiche « Le mode multi-utilisateurs est activé ».
- **Confidentialité et données** : [`privacy.title`], cartes LLM / embedder / base vectorielle (`components/ProviderPrivacy`), « Télémétrie anonyme activée ».
- **Fonctionnalités expérimentales** (EN) : conditions d'utilisation, puis la seule fonction « Live Document Sync » (`features.js`).
- **Community Hub** (EN) : « Community Hub », « Your AnythingLLM Community Hub Account », « Import a Community Item ». Ces pages dépendent du réseau.

---

## 2. Sélecteurs utiles (récapitulatif)

| Cible | Sélecteur recommandé |
|---|---|
| Nom d'utilisateur (connexion) | `input[name="username"]` |
| Mot de passe (connexion) | `input[name="password"]` |
| Bouton de connexion | `form button[type="submit"]` (texte « Connexion ») |
| Fenêtre codes de récupération | `getByRole("button",{name:"Download"})` puis `{name:"Close"}` |
| Nouveau workspace | `button[data-tooltip-id="new-workspace-tooltip"]` puis `input#name`, puis `button[type=submit]` (« Save ») |
| Lien d'un workspace | `a[href="/workspace/<slug>"]` |
| Envoi de documents (barre latérale) | `button[data-tooltip-id="upload-workspace"]` (au survol de la ligne) |
| Réglages du workspace | `button[aria-label="General appearance settings"]` |
| Champ de message | `textarea#primary-prompt-input` |
| Envoyer | `#send-prompt` |
| Arrêter | `#stop-generation-button` |
| Pièce jointe | `#attach-item-btn` / `input#dnd-chat-file-uploader` (pour `setInputFiles`) |
| @agent | `button[data-tooltip-id="agent-session"]` |
| Outils / commandes `/` | `#tools-btn` |
| Micro | `button[data-tooltip-id="tooltip-microphone-btn"]` |
| Envoi dans le gestionnaire de documents | `input[type="file"]` de la zone d'envoi (react-dropzone) |
| Déplacer vers le workspace | `getByRole("button",{name:"Déplacer vers l'espace de travail"})` |
| Save and Embed | `getByRole("button",{name:"Sauvegarder et intégrer"})` |
| Épingler | `[data-tooltip-id="pin-document"]` dans `#ws-directory-item` |
| Sources sous une réponse | `getByRole("button",{name:/^Sources/})` |
| Réglages de l'instance | `a[aria-label="Settings"]` (mène à `/settings/interface`) |
| Liens du menu de réglages | `a[href="/settings/llm-preference"]`, etc. (déplier le groupe d'abord, ou naviguer directement) |
| Sélecteur de langue | `select[name="userLang"]` (`/settings/interface` ou fenêtre Compte), valeur `fr` |
| Bouton de fermeture des fenêtres `lib/Modal` | `button[aria-label="Close"]` |
| Onboarding précédent / suivant | `button[aria-label="Back"]` / `button[aria-label="Continue"]` |
| Interrupteurs | `[role="switch"]` (`components/lib/Toggle`) |

---

## 3. Langue

- `i18n.js` : `i18next` + `LanguageDetector`, `fallbackLng: "en"`, `lowerCaseLng: true`. Ordre de détection par défaut de la bibliothèque v7.2.1 (valeurs de la bibliothèque, non redéfinies dans le dépôt) : paramètre d'URL `?lng=` → cookie `i18next` → `localStorage["i18nextLng"]` → `sessionStorage` → `navigator.language` → `<html lang>`. Le choix est mis en cache dans `localStorage`.
- Changement dans l'interface : `select[name="userLang"]` dans **Apparence > Interface** (« Langue d'affichage ») ou dans la fenêtre **Compte** du menu utilisateur (« Langue »). Les deux appellent `i18n.changeLanguage()` (`hooks/useLanguageOptions.js`). C'est propre à chaque navigateur, **rien n'est enregistré sur le serveur**, et ce n'est pas un réglage d'administrateur.
- Les options affichent le nom de la langue via `Intl.DisplayNames`. Le français apparaît comme « French » (ou « français » selon la langue du navigateur), avec la valeur `fr`.
- Si la langue détectée est `fr-fr` (navigateur `fr-FR`), l'interface est bien en français (repli `fr-fr` → `fr`). En revanche, la liste peut afficher la première option, car `fr-fr` n'est pas une valeur proposée. **Recommandation Playwright** : `context.addInitScript(() => localStorage.setItem("i18nextLng","fr"))` et `locale: "fr-FR"`.
- **Complétude** : les clés sont complètes à 100 %, mais certaines traductions sont approximatives (exemples : `chat_window.source_count_other` = « Références à {{count}} », `chat_window.memories.menu.move_to_global` = « Passer à l'échelle mondiale », `settings.branding` = « Personnalisation », `settings.customization` = « Apparence »).
- **Restent en anglais (codé en dur)** : fenêtre des codes de récupération ; panneaux d'options des fournisseurs (Base URL, API Key, etc.) ; boutons « Save changes » des pages LLM et Voix ; page Voix et Parole ; pages Admin Utilisateurs, Espaces de travail et Invitations ; Default System Prompt ; Variables de prompt système ; Extension de navigateur ; Mobile ; Fonctionnalités expérimentales ; Community Hub ; titres de sections de Compétences de l'agent ; barre « Cancel / Save » ; fils de discussion (« New Thread », « Rename », « Delete Thread ») ; info-bulles de la barre latérale ; « Manage Users » ; « Default / Accuracy Optimized » ; calque de glisser-déposer ; « Context Window Warning » ; « Copy chat link » ; bouton « Save » de la fenêtre Nouvel espace de travail ; « Clear Chats » ; toasts de succès (« LLM preferences saved successfully. », etc.) ; libellé « Search all … providers ».

---

## 4. Onboarding (`/onboarding`)

Fichiers `pages/OnboardingFlow/Steps/*`. Navigation par les flèches `aria-label="Back"` et `aria-label="Continue"`, sur les côtés de l'écran.

1. **`home`** : « Bienvenue » [`onboarding.home.welcome`], bouton « Commencer » [`onboarding.home.getStarted`].
2. **`llm-preference`** : « Préférence LLM » [`onboarding.llm.title`] et sa description. Liste des fournisseurs avec recherche, placeholder « Search LLM providers » (EN). Défaut OpenAI, ou Lemonade intégré si disponible. Les champs du fournisseur choisi s'affichent dessous (Generic OpenAI : voir §1 bis). La flèche « Continue » **marque l'onboarding comme terminé** (`System.markOnboardingComplete`), puis enregistre en imposant `EmbeddingEngine="native"` et `VectorDB="lancedb"`. **Il n'y a pas d'étape embedder ni base vectorielle dans l'onboarding.** On ne peut pas passer cette étape : il faut un fournisseur valide.
3. **`user-setup`** : « Configuration utilisateur » ; « Combien de personnes utiliseront cette instance ? » [`onboarding.userSetup.howManyUsers`], boutons « Juste moi » / « Mon équipe ».
   - Juste moi : « Définir un mot de passe » Oui / Non, puis « Mot de passe de l'instance » (`name="password"`, placeholder « Your admin password », 8 caractères minimum, jeu de caractères limité par `PW_REGEX` = `[a-zA-Z0-9_\-!@$%^&*();]`).
   - **Mon équipe (multi-utilisateur)** : « Nom d'utilisateur administrateur » `input[name="username"]` (placeholder « Your admin username » ; règle `common.username_requirements` : 2 à 64 caractères, minuscule en tête, `[a-z0-9._@-]`) et « Mot de passe administrateur » `input[name="password"]` (placeholder « Your admin password », 8 caractères minimum ; règles serveur `PASSWORDMINCHAR`, par défaut 8). La flèche Continue envoie `System.setupMultiUser`, puis connecte automatiquement l'admin (jeton stocké).
4. **`data-handling`** : « Gestion des données », cartes de confidentialité LLM / embedder / base vectorielle, texte « Ces paramètres peuvent être modifiés ultérieurement… ». Pas de bouton retour.
5. **`survey`** : « Bienvenue », enquête facultative (`email`, `use_case` = travail / personnel / autre, `comment`). Bouton **« Ignorer l'enquête »** [`onboarding.survey.skip`]. Continue sans rien remplir mène à `/`. À l'affichage, un workspace « Mon Espace de Travail » est créé s'il n'en existe aucun. Remplir l'e-mail enverrait le questionnaire en ligne : **à ne pas faire** (règle « aucun compte en ligne »).

On peut passer seulement l'enquête. Une fois l'onboarding terminé, `/onboarding/*` redirige vers l'accueil (`useRedirectToHomeOnOnboardingComplete`). Le mode multi-utilisateur peut aussi s'activer plus tard dans `/settings/security`.

---

## 5. Citations dans le chat

- Composant `components/WorkspaceChat/ChatContainer/ChatHistory/Citation/index.jsx` (export par défaut `Citations`), rendu sous chaque réponse de l'assistant qui a des sources (`HistoricalMessage/index.jsx` l. 212).
- Apparence : un bouton pilule « **Sources** » [`chat_window.sources`, FR = EN = « Sources »] suivi de 3 pastilles au maximum (icône du type de source : fichier, lien, YouTube, GitHub, etc.) et « + N » s'il y en a plus. Les morceaux qui viennent d'un même document sont regroupés par titre (`combineLikeSources`). **Il n'y a pas de libellé « Show Citations » en 1.19.0.**
- Au clic, un **panneau latéral droit « Sources »** s'ouvre (`SourcesSidebar`, fermeture par un X **sans aria-label**). Il contient une ligne par document (`SourceItem`) : le titre, le sous-titre « Document » [`chat_window.document`] (ou l'URL pour un lien), et « {{count}} référence » / « Références à {{count}} » [`chat_window.source_count_*`]. Un nouveau clic sur le bouton referme le panneau.
- Au clic sur un document, une **fenêtre `CitationDetailModal`** s'ouvre. Elle affiche le titre (tronqué à 45 caractères, avec un lien externe si la source est une URL) et « Referenced N times. » (EN). Pour chaque morceau : le pourcentage de similarité suivi de « match » [`chat_window.similarity_match`], avec l'info-bulle EN « This is the semantic similarity score… » (`data-tooltip-id="similarity-score"`), puis le texte du morceau, sans l'en-tête `<document_metadata>`. Fermeture : `button[aria-label="Close"]`.
- Sur mobile, ce panneau est remplacé par `MobileCitationModal`.
