#!/usr/bin/env bash
# Installe le serveur MCP fictif « velanor-outils » dans le dossier des greffons d'AnythingLLM :
# copie du script dans donnees/anythingllm/storage/plugins/mcp/ et déclaration dans anythingllm_mcp_servers.json
# (format { "mcpServers": { nom: { command, args } } }). La commande tourne dans le conteneur (node y est présent).
set -euo pipefail
cd "$(dirname "$0")/../../.."
P=donnees/anythingllm/storage/plugins
mkdir -p "$P/mcp"
cp outils/anythingllm/mcp/serveur-velanor.js "$P/mcp/"
cat > "$P/anythingllm_mcp_servers.json" <<JSON
{
  "mcpServers": {
    "velanor-outils": {
      "command": "node",
      "args": ["/app/server/storage/plugins/mcp/serveur-velanor.js"]
    }
  }
}
JSON
echo "serveur MCP déclaré dans $P/anythingllm_mcp_servers.json"
printf '%s\n' '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18"}}' '{"jsonrpc":"2.0","id":2,"method":"tools/list"}' '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"stock_piece","arguments":{"reference":"BAT-500"}}}' \
  | docker exec -i rag-anythingllm node /app/server/storage/plugins/mcp/serveur-velanor.js
