#!/usr/bin/env bash
# Série de bancs sur le même espace « Banc-bge-m3 » (même corpus, mêmes questions) : seuls les réglages changent.
# free -m et santé du service central relevés avant chaque banc (kit/PROMPT.md §2).
set -uo pipefail
cd "$(dirname "$0")/../.."
lancer() { etiq="$1"; shift
  log="outils/resultats/anythingllm/banc-$(date +%F)-$etiq.log"
  { free -m | head -2; outils/communs/llm_central_sante.sh --essai 2>&1 | tail -12; } > "$log" 2>&1
  python3 outils/anythingllm/banc.py --etiquette "$etiq" --espace Banc-bge-m3 "$@" >> "$log" 2>&1
  tail -1 "$log"; }
lancer rerank-natif --rerank
lancer top8 --top-n 8
lancer top8-rerank-natif --top-n 8 --rerank
lancer serre-top2 --top-n 2
