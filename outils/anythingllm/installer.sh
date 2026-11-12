#!/usr/bin/env bash
# Installation rejouable et idempotente d'AnythingLLM v1.19.0 (édition Docker), branchée au service LLM central.
#  1. image officielle à la version figée (étiquette et empreinte) ;
#  2. réglages et secrets générés localement (donnees/anythingllm/storage/.env, ignoré par git) ; télémétrie coupée ;
#  3. démarrage du projet compose rag-anythingllm (outils/anythingllm/compose.yml) et attente de /api/ping ;
#  4. vérification des ports (127.0.0.1 seulement).
# Le compte, la langue et le branchement des modèles se font ensuite dans l'interface (manuel, chapitre 03)
# ou par outils/anythingllm/configurer.py (même résultat, par l'API interne de l'interface).
# Usage : outils/anythingllm/installer.sh   (journal : outils/resultats/anythingllm/installation-<date>.log)
set -euo pipefail
RACINE="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$RACINE"
IMAGE="mintplexlabs/anythingllm:1.19.0@sha256:daf5a6ae9d363ed578e7d41e2d0668c7eaa604bd90b0ff27435f893b0906833e"
DONNEES="$RACINE/donnees/anythingllm"
ENVF="$DONNEES/storage/.env"
JOURNAL="outils/resultats/anythingllm/installation-$(date +%F).log"
mkdir -p "$(dirname "$JOURNAL")"
exec > >(tee -a "$JOURNAL") 2>&1
echo "== installer.sh $(date -Iseconds)"
debut=$(date +%s)

# 0. prérequis
outils/anythingllm/compose.sh version >/dev/null || { echo "docker compose indisponible"; exit 1; }
docker network inspect llm-net >/dev/null 2>&1 || { echo "réseau llm-net absent : démarrer LLM-Service (~/mes_projets/Projet-IA/LLM-Service/scripts/demarrer.sh)"; exit 1; }
docker network inspect rag-local >/dev/null 2>&1 || docker network create rag-local
free -m | awk '/Mem:/{print "RAM disponible avant installation : " $7 " Mo"}'

# 1. image figée
docker image inspect "$IMAGE" >/dev/null 2>&1 || docker pull "$IMAGE"
docker image inspect --format 'image : {{index .RepoTags 0}} {{index .RepoDigests 0}} {{.Size}} octets' "$IMAGE"

# 2. réglages : secrets générés une seule fois (l'application complète ce fichier quand les réglages changent).
#    Pas de JWT_SECRET ici : sa présence fait marquer l'accueil comme déjà fait (server/utils/boot/markOnboarded.js),
#    l'assistant de premier lancement disparaît ; l'application le génère elle-même à l'activation du mot de passe.
mkdir -p "$DONNEES/storage"
if [ ! -f "$ENVF" ]; then
  secret() { openssl rand -hex 32; }
  umask 077
  cat > "$ENVF" <<ENV
SERVER_PORT=3001
STORAGE_DIR="/app/server/storage"
SIG_KEY="$(secret)"
SIG_SALT="$(secret)"
DISABLE_TELEMETRY="true"
ENV
  echo "réglages générés : $ENVF (secrets locaux, jamais affichés)"
else
  echo "réglages existants conservés : $ENVF"
fi
grep -q '^DISABLE_TELEMETRY="true"' "$ENVF" || echo 'DISABLE_TELEMETRY="true"' >> "$ENVF"

# 3. démarrage
outils/anythingllm/demarrer.sh

# 4. ports liés à 127.0.0.1 seulement
docker ps --filter name=rag-anythingllm --format '{{.Names}} {{.Ports}}' | tee /dev/stderr | grep -v '127.0.0.1:' && { echo "port publié hors de 127.0.0.1"; exit 1; } || true
echo "durée : $(( $(date +%s) - debut )) s"
docker stats --no-stream --format 'RAM au repos : {{.Name}} {{.MemUsage}}' rag-anythingllm
du -sh "$DONNEES" | sed 's/^/disque des données : /'
