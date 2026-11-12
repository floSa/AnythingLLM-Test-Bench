#!/usr/bin/env python3
"""Vérifie que chaque route déclarée par l'interface (frontend/src/main.jsx au tag v1.19.0) a sa ligne dans
docs/anythingllm/annexes/carte-interface.md. Sortie : outils/resultats/anythingllm/carte-couverture-<date>.txt"""
import datetime, re
from pathlib import Path

R = Path(__file__).resolve().parents[2]
routes = sorted(set(re.findall(r'path:\s*"([^"]+)"', (R / "sources/anythingllm/frontend/src/main.jsx").read_text())))
carte = (R / "docs/anythingllm/annexes/carte-interface.md").read_text()
lignes = {l.split("|")[1].strip(): l for l in carte.splitlines() if l.startswith("| ") and not l.startswith("| Page ou menu")}
CORRESPONDANCE = {
    "/": "Écran principal", "/login": "Connexion", "/onboarding": "Assistant de premier lancement",
    "/onboarding/:step": "Assistant de premier lancement", "/accept-invite/:code": "Acceptation d'une invitation",
    "/sso/simple": "Connexion unique (SSO)", "*": "Page introuvable",
    "/workspace/:slug": "Discussion d'un espace", "t/:threadSlug": "Discussion d'un espace",
    "/workspace/:slug/settings/:tab": "Paramètres généraux",
    "/settings/llm-preference": "Préférence LLM", "/settings/vector-database": "Base de données vectorielle",
    "/settings/embedding-preference": "Préférences d'intégration", "/settings/text-splitter-preference": "Diviseur de texte et découpage",
    "/settings/image-generation-preference": "Génération d'images", "/settings/audio-preference": "Voix et Parole",
    "/settings/transcription-preference": "Modèle de transcription", "/settings/model-routers": "Routeur modèle",
    "/settings/model-routers/:id": "Règles d'un routeur", "/settings/users": "Utilisateurs", "/settings/workspaces": "Espaces de travail",
    "/settings/workspace-chats": "Chat de l'espace de travail", "/settings/invites": "Invitation",
    "/settings/default-system-prompt": "Default System Prompt", "/settings/agents": "Compétences de l'agent",
    "/settings/agents/builder": "Éditeur d'agent flow", "/settings/agents/builder/:flowId": "Éditeur d'agent flow",
    "/settings/community-hub/trending": "Centre communautaire", "/settings/community-hub/authentication": "Centre communautaire",
    "/settings/community-hub/import-item": "Centre communautaire", "/settings/interface": "Interface",
    "/settings/branding": "Personnalisation", "/settings/chat": "Chat (apparence)",
    "/settings/external-connections/telegram": "Canaux, Telegram", "/settings/embed-chat-widgets": "Widgets de chat intégrés",
    "/settings/event-logs": "Journaux d'événements", "/settings/scheduled-jobs": "Tâches planifiées",
    "/settings/scheduled-jobs/:id/runs": "Exécutions d'une tâche planifiée", "/settings/scheduled-jobs/:id/runs/:runId": "Exécutions d'une tâche planifiée",
    "/settings/api-keys": "Clés API", "/settings/system-prompt-variables": "Variables de prompt système",
    "/settings/browser-extension": "Extension de navigateur", "/settings/mobile-connections": "AnythingLLM Mobile",
    "/settings/security": "Sécurité", "/settings/privacy": "Confidentialité et données",
    "/settings/beta-features": "Fonctionnalités expérimentales",
    "/settings/beta-features/live-document-sync/manage": "Gestion des documents surveillés",
}
sortie, manquantes = [], 0
for r in routes:
    nom = CORRESPONDANCE.get(r)
    ligne = lignes.get(nom) if nom else None
    couvre = ligne.split("|")[4].strip() if ligne else ""
    ok = bool(ligne) and bool(couvre)
    manquantes += not ok
    sortie.append(f"{'OK ' if ok else 'MANQUE'} {r:52} -> {nom or '?'} : {couvre[:90]}")
sortie.append(f"{len(routes)} routes, {manquantes} sans ligne de carte ou sans manuel ; {len(lignes)} lignes dans la carte")
out = R / f"outils/resultats/anythingllm/carte-couverture-{datetime.date.today()}.txt"
out.write_text("\n".join(sortie) + "\n")
print("\n".join(sortie))
