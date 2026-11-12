#!/usr/bin/env bash
# Démarre AnythingLLM (données conservées) et attend /api/ping. LLM-Service n'est pas démarré ici : il est géré à part.
set -euo pipefail
cd "$(dirname "$0")/../.."
docker network inspect llm-net >/dev/null 2>&1 || { echo "réseau llm-net absent : démarrer LLM-Service (~/mes_projets/Projet-IA/LLM-Service/scripts/demarrer.sh)"; exit 1; }
docker network inspect rag-local >/dev/null 2>&1 || docker network create rag-local >/dev/null
outils/anythingllm/compose.sh up -d
for i in $(seq 1 90); do
  [ "$(curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:3001/api/ping)" = 200 ] && { echo "AnythingLLM prêt : http://127.0.0.1:3001 ($((i*2)) s)"; exit 0; }
  sleep 2
done
echo "AnythingLLM ne répond pas après 180 s : docker logs rag-anythingllm"; exit 1
