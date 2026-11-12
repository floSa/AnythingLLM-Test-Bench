#!/usr/bin/env bash
# Lance un script de captures Playwright dans le conteneur officiel (rien à installer dans WSL).
# Le conteneur est branché sur le réseau rag-local : les applications s'ouvrent par leur nom de conteneur.
# Le paquet Python playwright (même version que l'image) est installé une fois dans donnees/playwright/site.
# Usage : outils/communs/captures/lancer.sh <script.py relatif au dépôt> [arguments]
set -euo pipefail
cd "$(dirname "$0")/../../.."
IMAGE="mcr.microsoft.com/playwright/python:v1.65.1-noble@sha256:0ab41a37431309d72b7a26f40ef1fdb464a62740196b2143965a2f59dc090409"
mkdir -p donnees/playwright
if [ ! -d donnees/playwright/site/playwright ]; then
  docker run --rm --user "$(id -u):$(id -g)" -e HOME=/tmp -v "$PWD/donnees/playwright:/pw" "$IMAGE" \
    pip install -q --target /pw/site playwright==1.65.1
fi
ENVF=(); [ -f .env ] && ENVF=(--env-file .env)  # clé du service central : transmise au scénario, jamais affichée
docker run --rm --name rag-captures --network rag-local "${ENVF[@]}" --user "$(id -u):$(id -g)" -e HOME=/tmp \
  -e PYTHONPATH=/pw/site:/depot/outils/communs/captures -v "$PWD/donnees/playwright:/pw" -v "$PWD:/depot" -w /depot \
  "$IMAGE" python "$@"
