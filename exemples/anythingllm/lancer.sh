#!/usr/bin/env bash
# Exécute chaque exemple dans l'ordre et enregistre la sortie réelle dans sorties_verifiees.txt.
set -uo pipefail
cd "$(dirname "$0")"
sortie=sorties_verifiees.txt
echo "# Sorties vérifiées des exemples AnythingLLM 1.19.0 — $(date -Iseconds)" > "$sortie"
for f in 01_sante.sh 02_lister_les_espaces.py 03_creer_et_alimenter.py 04_poser_une_question.py 05_recherche_seule.py 06_compatible_openai.py 07_nettoyer.py; do
  echo; echo "## $f" ; case "$f" in *.sh) bash "$f";; *.py) python3 "$f";; esac; echo "(code de sortie : $?)"
done 2>&1 | tee -a "$sortie"
