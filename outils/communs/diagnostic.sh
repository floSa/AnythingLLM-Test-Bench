#!/usr/bin/env bash
# Diagnostic de la machine : écrit outils/resultats/machine/diagnostic-<date>.json
set -u
cd "$(dirname "$0")/../.."
sortie="outils/resultats/machine/diagnostic-$(date +%F).json"
mkdir -p "$(dirname "$sortie")"

essai() { timeout "${2:-20}" bash -c "$1" 2>&1 | head -c 4000; }

wsl_version=$(essai 'wsl.exe --version 2>/dev/null | tr -d "\000\r"')
windows=$(essai 'cmd.exe /c ver 2>/dev/null | tr -d "\r"')
distrib=$(essai '. /etc/os-release; echo "$PRETTY_NAME"')
noyau=$(uname -r)
cpu=$(grep -m1 "model name" /proc/cpuinfo | cut -d: -f2- | sed 's/^ //')
coeurs=$(nproc)
ram_mo=$(free -m | awk '/Mem:/{print $2}')
swap_mo=$(free -m | awk '/Swap:/{print $2}')
disque_depot=$(df -BG --output=avail . | tail -1 | tr -d ' G')
docker_root=$(docker info --format '{{.DockerRootDir}}' 2>/dev/null)
docker_df=$(essai 'docker system df --format "{{.Type}}={{.Size}}" | paste -sd";"')
nvsmi=$(essai 'nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader')
# GPU visible dans un conteneur : nouvel essai éphémère avec l'image déjà présente de llm-swap (le service n'est pas touché)
img_swap=$(docker inspect --format '{{.Config.Image}}' llm-swap 2>/dev/null)
gpu_conteneur=$( [ -n "$img_swap" ] && essai "docker run --rm --gpus all --entrypoint nvidia-smi $img_swap -L" 120 || echo "sans objet (llm-swap absent : profil cpu ou service arrêté)")
gpu_windows=$(essai 'powershell.exe -NoProfile -Command "Get-CimInstance Win32_VideoController | ForEach-Object { \$_.Name }" | tr -d "\r" | paste -sd";"' 60)
docker_v=$(docker version --format '{{.Server.Version}}' 2>/dev/null)
compose_v=$(docker compose version --short 2>/dev/null)

code() { curl -s -o /dev/null -m 15 -w '%{http_code}' "$1"; }
hub=$(code https://registry-1.docker.io/v2/)
ghcr=$(code https://ghcr.io/v2/)
pypi=$(code https://pypi.org/simple/pip/)
hf=$(code https://huggingface.co/api/models/BAAI/bge-m3)

# Port publié sur 127.0.0.1 joignable depuis WSL
docker rm -f rag-diag-port >/dev/null 2>&1
docker run -d --name rag-diag-port -p 127.0.0.1:18999:80 nginx:alpine >/dev/null 2>&1
sleep 3
port_local=$(code http://127.0.0.1:18999/)
docker rm -f rag-diag-port >/dev/null 2>&1

# vm.max_map_count de la VM de Docker (lecture seule ; Elasticsearch exige 262144 ou plus)
max_map=$(essai 'docker run --rm --entrypoint cat nginx:alpine /proc/sys/vm/max_map_count' 60)

# Service LLM central (LLM-Service, géré à part) : branche, conteneurs llm-*, profil, réseau, modèles, santé
LLMDIR="${LLM_SERVICE_DIR:-$HOME/mes_projets/Projet-IA/LLM-Service}"
llm_branche=$(essai "git -C '$LLMDIR' branch --show-current")
llm_conteneurs=$(essai 'docker ps --format "{{.Names}}={{.Image}}" | grep -E "^llm-" | paste -sd";"')
if docker ps --format '{{.Names}}' | grep -qx llm-swap; then llm_profil=gpu; elif docker ps --format '{{.Names}}' | grep -qx llm-swap-cpu; then llm_profil=cpu; else llm_profil=inconnu; fi
llm_net=$(docker network inspect llm-net >/dev/null 2>&1 && echo present || echo absent)
llm_modeles=$(essai 'outils/communs/llm_central_sante.sh | grep "^  " | sed "s/^ *//" | paste -sd";"' 30)
llm_sante=$(essai 'outils/communs/llm_central_sante.sh --essai >/dev/null 2>&1 && echo OK || echo ECHEC' 600)

python3 - "$sortie" <<EOF
import json, sys
d = {
  "date": "$(date -Iseconds)",
  "windows": """$windows""".strip(),
  "wsl_version": """$wsl_version""".strip(),
  "distribution": "$distrib", "noyau": "$noyau",
  "cpu": "$cpu", "coeurs_logiques": $coeurs,
  "ram_wsl_mo": $ram_mo, "swap_wsl_mo": $swap_mo,
  "disque_libre_depot_go": $disque_depot,
  "docker_root": "$docker_root", "docker_df": "$docker_df",
  "nvidia_smi_wsl": """$nvsmi""".strip(),
  "gpu_dans_conteneur": """$gpu_conteneur""".strip(),
  "cartes_video_windows": """$gpu_windows""".strip(),
  "docker": "$docker_v", "compose": "$compose_v",
  "acces_http": {"docker_hub": "$hub", "ghcr": "$ghcr", "pypi": "$pypi", "huggingface": "$hf"},
  "port_127_0_0_1_depuis_wsl": "$port_local",
  "vm_max_map_count_docker": """$max_map""".strip(),
  "llm_service": {"dossier": "$LLMDIR", "branche": """$llm_branche""".strip(), "conteneurs": """$llm_conteneurs""".strip(), "profil": "$llm_profil", "reseau_llm_net": "$llm_net", "modeles": """$llm_modeles""".strip(), "sante_essai": """$llm_sante""".strip()},
}
json.dump(d, open(sys.argv[1], "w"), ensure_ascii=False, indent=2)
print(json.dumps(d, ensure_ascii=False, indent=2))
EOF
