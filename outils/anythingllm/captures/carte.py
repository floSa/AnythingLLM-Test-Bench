"""Captures de repérage de la carte de l'interface (docs/anythingllm/img/carte/), une par page, compte administrateur
(multi-utilisateur). Usage : lancer.sh outils/anythingllm/captures/carte.py"""
from ui import Scenario

PAGES = [("accueil", "/"), ("discussion", "/workspace/demo-velanor"),
         ("espace-general", "/workspace/demo-velanor/settings/general-appearance"),
         ("espace-chat", "/workspace/demo-velanor/settings/chat-settings"),
         ("espace-vecteurs", "/workspace/demo-velanor/settings/vector-database"),
         ("espace-membres", "/workspace/demo-velanor/settings/members"),
         ("espace-agent", "/workspace/demo-velanor/settings/agent-config"),
         ("preference-llm", "/settings/llm-preference"), ("base-vectorielle", "/settings/vector-database"),
         ("embedding", "/settings/embedding-preference"), ("decoupage", "/settings/text-splitter-preference"),
         ("images", "/settings/image-generation-preference"), ("voix", "/settings/audio-preference"),
         ("transcription", "/settings/transcription-preference"), ("routeurs", "/settings/model-routers"),
         ("utilisateurs", "/settings/users"), ("espaces", "/settings/workspaces"), ("conversations", "/settings/workspace-chats"),
         ("invitations", "/settings/invites"), ("consigne-par-defaut", "/settings/default-system-prompt"),
         ("competences", "/settings/agents"), ("centre-communautaire", "/settings/community-hub/trending"),
         ("interface", "/settings/interface"), ("personnalisation", "/settings/branding"), ("apparence-chat", "/settings/chat"),
         ("widgets", "/settings/embed-chat-widgets"), ("journaux", "/settings/event-logs"), ("cles-api", "/settings/api-keys"),
         ("variables", "/settings/system-prompt-variables"), ("extension", "/settings/browser-extension"),
         ("mobile", "/settings/mobile-connections"), ("securite", "/settings/security"), ("confidentialite", "/settings/privacy"),
         ("experimental", "/settings/beta-features"), ("documentation-api", "/api/docs")]

s = Scenario("carte")
try:
    s.page.evaluate("localStorage.setItem('anythingllm_experimental_feature_preview_unlocked','enabled')")
    for nom, chemin in PAGES:
        s.aller(chemin); s.page.wait_for_timeout(1500)
        s.cap(nom, [], note="repérage " + chemin)
finally:
    s.fermer()
