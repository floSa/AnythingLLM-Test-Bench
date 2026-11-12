#!/usr/bin/env bash
# docker compose du projet rag-anythingllm (repli sur le greffon système si « docker compose » est cassé, kit/PROMPT.md §2).
set -euo pipefail
cd "$(dirname "$0")"
if docker compose version >/dev/null 2>&1; then DC=(docker compose); else DC=(/usr/libexec/docker/cli-plugins/docker-compose); fi
exec "${DC[@]}" -f compose.yml "$@"
