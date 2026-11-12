#!/usr/bin/env bash
# État d'AnythingLLM : conteneur, ports (liés à 127.0.0.1), santé, mémoire, disque ; santé du service LLM central (lecture seule).
set -uo pipefail
cd "$(dirname "$0")/../.."
echo "== conteneur";  docker ps -a --filter name=rag-anythingllm --format '{{.Names}} {{.Status}} {{.Ports}}'
echo "== /api/ping";  curl -s -m 5 http://127.0.0.1:3001/api/ping; echo
echo "== mémoire";    docker stats --no-stream --format '{{.Name}} {{.MemUsage}} {{.CPUPerc}}' rag-anythingllm 2>/dev/null
echo "== disque";     du -sh donnees/anythingllm 2>/dev/null
echo "== service LLM central"; outils/communs/llm_central_sante.sh 2>&1 | head -6
