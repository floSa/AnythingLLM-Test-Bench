#!/usr/bin/env bash
# Site web local de test (fictif) pour le connecteur « site web » : nginx sur le réseau rag-local, sans port publié.
# AnythingLLM le lit à l'adresse http://rag-anythingllm-site/. Usage : site.sh start|stop
set -euo pipefail
cd "$(dirname "$0")"
case "${1:-start}" in
  start) docker rm -f rag-anythingllm-site >/dev/null 2>&1 || true
         docker run -d --name rag-anythingllm-site --network rag-local -v "$PWD/site:/usr/share/nginx/html:ro" nginx:alpine >/dev/null
         echo "site de test : http://rag-anythingllm-site/ (réseau rag-local)";;
  stop)  docker rm -f rag-anythingllm-site >/dev/null && echo "site de test arrêté";;
esac
