#!/usr/bin/env bash
# Vérifie que l'instance répond et que la clé de l'API développeur est acceptée.
set -euo pipefail
cd "$(dirname "$0")/../.."
CLE="${ANYTHINGLLM_API_KEY:-$(cat donnees/anythingllm/cle-api.txt)}"
echo "ping : $(curl -s http://127.0.0.1:3001/api/ping)"
echo "auth : $(curl -s -H "Authorization: Bearer $CLE" http://127.0.0.1:3001/api/v1/auth)"
echo "clé refusée (attendu 403) : $(curl -s -o /dev/null -w '%{http_code}' -H 'Authorization: Bearer cle-fausse' http://127.0.0.1:3001/api/v1/auth)"
