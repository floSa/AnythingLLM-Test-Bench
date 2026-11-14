#!/usr/bin/env node
// Serveur MCP minimal et fictif (stdio, JSON-RPC 2.0, un message JSON par ligne), sans dépendance, écrit pour le manuel.
// Un seul outil : « stock_piece », qui renvoie un stock fictif de pièces Vélanor. Aucun accès réseau ni fichier.
const readline = require("readline");
const STOCKS = { "BAT-500": 184, "MOT-250": 62, "CADRE-URB": 35, "FREIN-HYD": 410 };
const rl = readline.createInterface({ input: process.stdin });
const envoyer = (m) => process.stdout.write(JSON.stringify(m) + "\n");
rl.on("line", (ligne) => {
  let m; try { m = JSON.parse(ligne); } catch { return; }
  if (m.id === undefined) return; // notifications (ex. notifications/initialized) : pas de réponse
  const ok = (result) => envoyer({ jsonrpc: "2.0", id: m.id, result });
  switch (m.method) {
    case "initialize":
      return ok({ protocolVersion: (m.params && m.params.protocolVersion) || "2025-06-18",
                  capabilities: { tools: {} }, serverInfo: { name: "velanor-outils", version: "1.0.0" } });
    case "ping": return ok({});
    case "tools/list":
      return ok({ tools: [{ name: "stock_piece", description: "Donne le stock (fictif) d'une pièce détachée Vélanor à partir de sa référence, par exemple BAT-500.",
                            inputSchema: { type: "object", properties: { reference: { type: "string", description: "référence de la pièce" } }, required: ["reference"] } }] });
    case "tools/call": {
      const ref = String((m.params && m.params.arguments && m.params.arguments.reference) || "").toUpperCase();
      const n = STOCKS[ref];
      return ok({ content: [{ type: "text", text: n === undefined ? `Référence ${ref} inconnue. Références connues : ${Object.keys(STOCKS).join(", ")}.` : `Stock de ${ref} : ${n} unités (entrepôt de Nantes, données fictives).` }] });
    }
    default:
      return envoyer({ jsonrpc: "2.0", id: m.id, error: { code: -32601, message: "méthode inconnue" } });
  }
});
