#!/usr/bin/env bash
# Sauvegarde d'AnythingLLM : arrêt bref du conteneur (base SQLite et LanceDB cohérentes), archive du dossier de données,
# redémarrage. L'archive contient la clé du service de modèles (.env de l'application) : à garder sur le poste.
# Usage : service/sauvegarder.sh [dossier de destination, défaut donnees/sauvegardes]
set -euo pipefail
cd "$(dirname "$0")/.."
dest="${1:-donnees/sauvegardes}"; mkdir -p "$dest"
archive="$dest/anythingllm-$(date +%Y%m%d-%H%M%S).tar.gz"
service/arreter.sh
tar -czf "$archive" -C donnees anythingllm
chmod 600 "$archive"
service/demarrer.sh
echo "Sauvegarde : $archive ($(du -h "$archive" | cut -f1))"
