# Journal — AnythingLLM

Mission : `kit/PROMPT.md` pour la fiche `kit/fiches/04-anythingllm.md`. Une entrée par étape (date, phase, fait, résultat, fichiers, prochaine étape).

## Décisions en attente

1. LLM-Service : option pour couper ou borner la réflexion de `chat` pour les applications qui ne la règlent pas (AnythingLLM n'envoie aucun paramètre de réflexion au fournisseur Generic OpenAI). Hors mission (modification de LLM-Service).
2. LLM-Service : modèle de réponse plus léger pour situer un plancher de qualité. Hors mission.
4. ~~Ports affichés par `docker ps`~~ — **Réglée le 12 novembre 2026.** `4000/tcp` (llm-central) et `8000/tcp` (llm-speaches) sont des ports déclarés par les images, non publiés. LLM-Service refuse de les publier (4000 est fermé, LiteLLM écoute sur 8080 ; 8000 ouvrirait speaches sans clé). La règle du kit vise désormais seulement les ports publiés (avec « -> ») : `kit/PROMPT.md` et les six fiches corrigés. Test : `outils/resultats/anythingllm/ports-publies-2026-11-12.txt`, aucune sortie, règle respectée.
5. Reranker : condition « banc sans puis avec le reranker rerank si la solution en accepte un » remplie au sens de sa clause : AnythingLLM 1.19.0 n'accepte aucun reranker externe (essai réel, `essai-reranker-externe-2026-11-12.txt`) ; banc passé sans puis avec le seul tri accepté (tri de précision intégré).
3. Tâche planifiée « Point stocks du lundi » (09:00 UTC chaque jour) laissée en place : sa page disparaît en multi-utilisateur ; à supprimer si l'appel quotidien au modèle n'est pas souhaité.

### 2026-11-12 12:55 — Phase A : diagnostic de la machine et santé du service central

- Fait : `outils/communs/llm_central_sante.sh --essai` en début de session : modèles listés (`chat`, `embed`, `rerank`, `transcribe` et alias), une requête réussie par usage (sortie : `outils/resultats/anythingllm/sante-2026-11-12-debut.txt`, code 0).
- `outils/communs/diagnostic.sh` adapté au service central (conteneurs `llm-*`, profil, réseau `llm-net`, santé ; essai GPU dans un conteneur éphémère de l'image de `llm-swap`, sans toucher au service) ; sortie `outils/resultats/machine/diagnostic-2026-11-12.json`.
- Résultat : machine du profil B (Ryzen 5 9600X, 32 Go visibles dans WSL, RTX 4060 Ti 16 Go, pilote 616.92), Docker 29.9.3, Compose 5.7.0 (greffon sain), 536 Go libres, `vm.max_map_count` 1 048 576, port `127.0.0.1` joignable depuis WSL, service central en profil `gpu` (LiteLLM v1.109.0, llama-swap v272 cuda b12282, speaches 0.8.3-cpu).
- Juge du banc (`outils/communs/banc/commun.py`) adapté au service central : `/v1/chat/completions`, modèle `chat`, réflexion coupée, clé lue dans `.env` ; essai : OUI pour « Paris », NON pour « Lyon ».
- Version retenue : AnythingLLM v1.19.0 (26 octobre 2026), image `mintplexlabs/anythingllm:1.19.0@sha256:daf5a6ae9d363ed578e7d41e2d0668c7eaa604bd90b0ff27435f893b0906833e` (3,39 Go), sources au tag dans `sources/anythingllm` (commit 9b1fcab, ignoré par git).
- Prochaine étape : cadrage (lecture du code par sous-agents), versions, relecture, installation.

### 2026-11-12 13:00 — Cadrage, installation, configuration

- Cadrage par deux sous-agents (`cadrage-serveur.md`, `cadrage-interface.md`) : pas de reranker externe en 1.19.0 (seul le tri intégré « Accuracy Optimized ») ; « Max Tokens » 1024 par défaut ; réflexion `<think>` dans les réponses ; mode par défaut `automatic` (Agent) ; pas de page dans les sources ; français partiel.
- Installation `outils/anythingllm/installer.sh` (11 s, 390 à 425 Mio au repos, port `127.0.0.1:3001`) ; premier essai avec `JWT_SECRET` prérempli : assistant sauté (`installation-2026-11-12-essai1-jwt.log`), installation refaite sans.
- Assistant et modèles déclarés à la souris (chapitre 03) : Generic OpenAI `chat` (16384, Max Tokens 8192), transcription OpenAI Compatible `transcribe`, puis embedder Generic OpenAI `embed` après le banc de l'embedder intégré.

### 2026-11-12 14:00 — Bancs (6 réglages)

- `free -m` et `llm_central_sante.sh --essai` avant chaque banc (en tête des `banc-*.log`).
- Embedder intégré 25/34, 4/4 ; bge-m3 défaut 33/34, 3/4 ; tri intégré 34/34, 4/4 ; 8 passages 34/34, 4/4 ; 8 passages et tri 34/34, 4/4 (médiane 10,7 s) ; 2 passages 31/34, 4/4.
- Écart : des captures sans appel au modèle (chapitres 07, 08, 12, 10 en partie) ont été prises pendant un banc (RAM disponible 22 Go) ; les captures qui interrogent le modèle ont été faites hors banc.

### 2026-11-12 15:30 — Captures, chapitres, annexes, rapport

- Captures des chapitres 03 à 15 (133) et 35 captures de repérage ; masquage automatique des clés ajouté après une clé locale visible (jamais commitée).
- Essais : arrêt, redémarrage, sauvegarde, restauration (`exploitation-2026-11-12.log`) ; OCR français (`ocr-fra-2026-11-12.log`) ; dépassement de contexte (`contexte-2026-11-12.txt`) ; exemples d'API (7, code 0) ; passage en multi-utilisateur, comptes, invitation, widget.
- Jeu de démonstration rangé (`demo_ranger.py`) : « Démo Vélanor » avec trois conversations citées ; espace du banc et documents d'essai supprimés.
- Documentation committée chapitre par chapitre, `verifier_docs.py` à 0 point ; README, index de la série, `outils/README.md`, `RAPPORT-anythingllm.md`.
- Prochaine étape : relecture par un lecteur novice, corrections, commit final.

### 2026-11-12 18:30 — Phase H : relectures, clôture

- Relecture par lecteur novice (partie 1), treize passages avec un sous-agent neuf à chaque fois : 59, 34, 14, 15, 4, 3, 4, 2, 3, 3, 2, 2 remarques, puis « Aucune remarque » au treizième. Corrections commitées après chaque passage (renvois, étapes manquantes, prérequis LLM-Service, captures refaites dont 04/05, 04/14, 09/03, 10/01, 12/04, 12/14, 13/07, 13/12, 15/06, nouvelles 13/11b et 14/01b).
- Outil d'annotation corrigé (`outils/communs/captures/annoter.py`) : défilement seulement si l'élément est hors de la fenêtre, puis second calcul des positions (pastilles décalées dans les zones à défilement interne).
- Relecture adversariale des annexes : 45 écarts (aucun lien cassé) corrigés en requalifiant ([Source], [Estimation], [À tester]) et en rectifiant les chiffres ; relevé brut de fin de mission `outils/resultats/anythingllm/fin-de-mission-2026-11-12.log`.
- Masquage étendu aux codes d'invitation (`ui.py`), texte nettoyé.
- Jeu de démonstration rangé (`demo_ranger.py`) : « Démo Vélanor » avec ses trois conversations citées.
- État : AnythingLLM en marche sur `http://127.0.0.1:3001`, `verifier_docs.py` à 0 point, dépôt poussé.

### 2026-11-13 — Uniformisation de la série

- `docs/README.md` remplacé par l'index commun aux cinq dépôts (Open Notebook, RAGFlow, AnythingLLM, Kotaemon, Open WebUI) : modèles utilisés, services déportables (OCR, audio, reranker), comparatif à deux lignes par solution (défaut, meilleur réglage). Chiffres repris des résultats bruts du 12 et du 13 novembre, aucun nouveau banc.
- README : section « Résultats » au même format que les autres dépôts.
- `verifier_docs.py` : 0 point.

### 2026-11-13 — Index de la série : Docling déporté

- `docs/README.md` mis à jour : résultats des bancs Docling déporté de RAGFlow (34/34) et de Kotaemon (29/34).

### 2026-11-13 — Index de la série : procédures Docling déporté

- `docs/README.md` : colonne « Procédure dans le manuel » (Open WebUI chapitre 08, RAGFlow chapitre 06, Kotaemon chapitre 05).

### 2026-11-13 — Index de la série : comparatif complété

- Lignes « meilleur, Docling déporté » de RAGFlow et Kotaemon ajoutées au comparatif ; reranker de RAGFlow expliqué (essayé, sans gain) ; « Conventions » renommé « Étiquettes des annexes ».

### 2026-11-13 — Index de la série : contradictions levées

- Ligne « RAGFlow, meilleur, avec reranker » ajoutée au comparatif ; colonne « Effet du reranker mesuré au banc » ; résumé « En bref » et sens des colonnes ; Docling intégré possible seulement dans Kotaemon et Open Notebook (Open WebUI et RAGFlow : serveur à part uniquement, vérifié dans le code et les images).

### 2026-11-13 — Index de la série réécrit

- Solutions en colonnes, critères en lignes ; un tableau par sujet : PDF scanné (OCR et Docling), audio, reranker, résultats par cas, détail du meilleur réglage. Parcours de lecture et étiquettes retirés.

### 2026-11-13 — Index de la série : technologies et résultats séparés

- Tableaux OCR et Docling, audio, reranker : capacités seulement ; résultats déplacés dans « Résultats par cas » et « Détail du meilleur réglage » (scores par type de question). Cases vides quand la solution ne le fait pas.

### 2026-11-13 — Index de la série : tableaux de même largeur, ligne Docling

- Tableaux en HTML à largeurs fixes (200 px puis 5 × 150 px), tous de la même largeur. Lecture des PDF : une ligne « Docling » (conteneur, déporté) et une ligne « OCR intégré, autre que Docling » ; Docling expliqué ; ligne « OCR utilisé au banc » retirée (elle est dans le détail du meilleur réglage).

### 2026-11-14 — Clé propre au banc pour LLM-Service

- Fait : clé propre au banc créée dans LLM-Service (nom `anythingllm-test-bench`) et écrite dans `LLM_CENTRAL_KEY` du `.env` par `~/mes_projets/Projet-IA/LLM-Service/scripts/cle.sh creer anythingllm-test-bench --dans <dépôt>/.env --noms LLM_CENTRAL_URL,LLM_CENTRAL_KEY` (procédure : `docs/brancher-une-application.md` de LLM-Service). La clé maîtresse de LLM-Service n'est plus utilisée par ce banc.
- Essai : `outils/communs/llm_central_sante.sh --essai` avec la nouvelle clé : `models`, `chat`, `embed` (1024 dimensions), `rerank` et `transcribe` répondent ; 4 requêtes comptées sur la clé du banc (`cle.sh lister`).
- Documentation : `.env.example`, README et chapitre 02 du manuel donnent désormais la commande `cle.sh` au lieu de recopier `LITELLM_MASTER_KEY`.
- Conteneurs : aucun ne tournait, aucun relancé ; la nouvelle clé sera prise en compte au prochain lancement. La clé recopiée par l'application dans `donnees/anythingllm/storage/.env` (`GENERIC_OPEN_AI_API_KEY`, `GENERIC_OPEN_AI_EMBEDDING_API_KEY`, `WHISPER_GENERIC_OPEN_AI_API_KEY`) a été remplacée par la nouvelle clé.
