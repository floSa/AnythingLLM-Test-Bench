#!/usr/bin/env bash
# Restauration d'AnythingLLM depuis une archive de sauvegarder.sh : arrêt, remplacement du dossier de données
# (l'ancien est gardé à côté, suffixé .avant-restauration), redémarrage.
# Usage : service/restaurer.sh <archive .tar.gz>
set -euo pipefail
cd "$(dirname "$0")/.."
archive="${1:?usage : restaurer.sh <archive .tar.gz>}"
[ -f "$archive" ] || { echo "archive introuvable : $archive"; exit 1; }
service/arreter.sh
ancien="donnees/anythingllm.avant-restauration-$(date +%Y%m%d-%H%M%S)"
[ -d donnees/anythingllm ] && mv donnees/anythingllm "$ancien" && echo "ancien dossier gardé : $ancien"
tar -xzf "$archive" -C donnees
service/demarrer.sh
echo "Restauré depuis $archive"
