# Journal — AnythingLLM

Mission : `kit/PROMPT.md` pour la fiche `kit/fiches/04-anythingllm.md`. Une entrée par étape (date, phase, fait, résultat, fichiers, prochaine étape).

## Décisions en attente

(aucune pour l'instant)

### 2026-11-12 12:55 — Phase A : diagnostic de la machine et santé du service central

- Fait : `outils/communs/llm_central_sante.sh --essai` en début de session : modèles listés (`chat`, `embed`, `rerank`, `transcribe` et alias), une requête réussie par usage (sortie : `outils/resultats/anythingllm/sante-2026-11-12-debut.txt`, code 0).
- `outils/communs/diagnostic.sh` adapté au service central (conteneurs `llm-*`, profil, réseau `llm-net`, santé ; essai GPU dans un conteneur éphémère de l'image de `llm-swap`, sans toucher au service) ; sortie `outils/resultats/machine/diagnostic-2026-11-12.json`.
- Résultat : machine du profil B (Ryzen 5 9600X, 32 Go visibles dans WSL, RTX 4060 Ti 16 Go, pilote 616.92), Docker 29.9.3, Compose 5.7.0 (greffon sain), 536 Go libres, `vm.max_map_count` 1 048 576, port `127.0.0.1` joignable depuis WSL, service central en profil `gpu` (LiteLLM v1.109.0, llama-swap v272 cuda b12282, speaches 0.8.3-cpu).
- Juge du banc (`outils/communs/banc/commun.py`) adapté au service central : `/v1/chat/completions`, modèle `chat`, réflexion coupée, clé lue dans `.env` ; essai : OUI pour « Paris », NON pour « Lyon ».
- Version retenue : AnythingLLM v1.19.0 (26 octobre 2026), image `mintplexlabs/anythingllm:1.19.0@sha256:daf5a6ae9d363ed578e7d41e2d0668c7eaa604bd90b0ff27435f893b0906833e` (3,39 Go), sources au tag dans `sources/anythingllm` (commit 9b1fcab, ignoré par git).
- Prochaine étape : cadrage (lecture du code par sous-agents), versions, relecture, installation.
