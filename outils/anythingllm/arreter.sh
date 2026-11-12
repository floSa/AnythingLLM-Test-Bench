#!/usr/bin/env bash
# Arrête AnythingLLM (données conservées dans donnees/anythingllm). LLM-Service n'est jamais arrêté ici : il est partagé.
set -euo pipefail
cd "$(dirname "$0")/../.."
outils/anythingllm/compose.sh stop
echo "AnythingLLM arrêté."
