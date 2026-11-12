# Outils

Principe : rien n'est écrit de mémoire. Chaque affirmation des manuels vient d'un script de ce dossier et d'un résultat brut rangé dans `outils/resultats/`. Les actions de la partie 1 du manuel sont faites à la souris par des scénarios Playwright, exécutés dans le conteneur officiel `mcr.microsoft.com/playwright/python` (rien à installer dans WSL).

## Communs (`outils/communs/`)

| Fichier | Rôle |
|---|---|
| `diagnostic.sh` | relevé de la machine et du service LLM central → `resultats/machine/diagnostic-<date>.json` |
| `llm_central_sante.sh` | santé du service central (liste des modèles, puis un essai par usage avec `--essai`) ; lecture seule |
| `versions.py` | dernière version stable de chaque composant (GitHub) → `resultats/<solution>/versions-<date>.json` |
| `identite_github.py` | étoiles, activité, licence du projet → `resultats/<solution>/identite-github-<date>.json` |
| `banc/commun.py` | banc commun : notation, juge LLM (`chat` du service central, réflexion coupée), mémoire, sorties JSON et Markdown |
| `banc/tableau.py` | tableau Markdown des bancs (comparatif de `docs/README.md`) |
| `banc/renoter.py` | renotation d'un banc enregistré |
| `captures/annoter.py` | rectangle rouge, pastille numérotée, masquage des secrets, capture |
| `captures/lancer.sh` | lance un scénario dans le conteneur Playwright (réseau `rag-local`, clé du service transmise sans affichage) |
| `verifier_docs.py` | vérification de la documentation (liens, ton, captures, carte) ; 0 point avant chaque commit |
| `nettoyer.sh` | suppression d'une solution (ressources `rag-<solution>` et `donnees/<solution>/`), sur confirmation |
| `nouvelle_solution.sh` | prépare le dépôt de la solution suivante |
| `generer_corpus.py`, `generer_audio.py` | corpus fictif (graine fixe) |
| `inventaire_modeles.py`, `llm_service.sh`, `llm_service_vllm.sh`, `voix.sh`, `mesure_modeles.py` | ancienne pile (Ollama, vLLM, speaches local), plus lancés ; gardés pour l'historique |

## AnythingLLM (`outils/anythingllm/`)

| Fichier | Rôle |
|---|---|
| `compose.yml`, `compose.sh` | projet compose `rag-anythingllm` (image figée, `127.0.0.1:3001`, réseaux `llm-net` et `rag-local`, options facultatives `donnees/anythingllm/options.env`) |
| `installer.sh` | installation rejouable (image, secrets, télémétrie coupée, démarrage, contrôle des ports) |
| `demarrer.sh`, `arreter.sh`, `etat.sh` | exploitation courante |
| `sauvegarder.sh`, `restaurer.sh` | sauvegarde et restauration du dossier de données |
| `client.py` | client de l'API (session, clé d'API, envoi de fichiers, retrait de la réflexion) |
| `banc.py`, `serie_banc.sh` | adaptateur du banc et série de réglages |
| `essai_contexte.py` | dépassement volontaire du contexte |
| `nettoyer_documents.py` | retrait des documents d'essai (garde les espaces listés) |
| `demo_ranger.py` | rangement du jeu de démonstration |
| `mcp/serveur-velanor.js`, `mcp/installer-mcp.sh` | serveur MCP fictif d'exemple et sa déclaration |
| `essais/site/`, `essais/site.sh` | site web local de test et page de test du widget |
| `captures/ui.py` | socle des scénarios (connexion, captures annotées, masquage automatique des clés) |
| `captures/c03_…` à `c15_…`, `carte.py` | un scénario par chapitre du manuel, et les captures de repérage de la carte |

## Résultats (`outils/resultats/`)

| Dossier | Contenu |
|---|---|
| `machine/` | diagnostics de la machine |
| `socle/` | mesures de l'ancienne pile (historique) |
| `anythingllm/` | versions, relecture, cadrage, installation, bancs, exploitation, captures (texte des pages et libellés des pastilles) |
| `open-notebook/`, `ragflow/` | bancs des solutions précédentes, pour le comparatif |
