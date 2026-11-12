# 16. Glossaire

> Ce chapitre rassemble les mots employés dans le manuel, avec leur sens simple.
> **Point de départ** : n'importe quel chapitre, quand un mot n'est pas clair.
> **Durée** : à la demande. **Avant** : aucun.

## Ce qu'il faut savoir

Les termes communs à toute la série de manuels (RAG, embedding, jeton, reranker…) sont définis dans le [glossaire de la série](../../glossaire.md). Le tableau ci-dessous reprend ceux qui reviennent le plus dans ce manuel, avec le libellé affiché par AnythingLLM quand il existe.

## Mots du manuel

| Mot | Libellé dans l'interface | Sens |
|---|---|---|
| Espace de travail | « Espace de travail », « workspace » | dossier cloisonné qui réunit des documents, des conversations et des réglages ; une question ne voit que les documents de son espace |
| Fil | « Thread », « New Thread » | conversation séparée dans un espace, avec son propre historique |
| Document | « Mes documents » | fichier téléversé (PDF, Word, Excel, PowerPoint, page web, audio…), lu et transformé en texte par AnythingLLM |
| Intégrer | « Sauvegarder et intégrer » | découper un document en passages et calculer leur représentation numérique, pour qu'il puisse être retrouvé |
| Passage | « contexte », « extrait » | morceau de document (1 000 caractères au plus) retrouvé pour répondre |
| Source, citation | « Sources » | document dont viennent les passages utilisés pour la réponse, affiché sous la réponse |
| Épingler | « Pin to workspace » | faire lire un document en entier à chaque question, au lieu de ses seuls passages retrouvés |
| Modèle de réponse | « Préférence LLM » | modèle d'IA qui rédige les réponses ; ici `chat` |
| Modèle d'embedding | « Préférences d'intégration » | modèle qui transforme un texte en nombres représentant son sens ; ici `embed` |
| Transcription | « Modèle de transcription » | conversion d'un audio en texte ; ici `transcribe` |
| Mode Chat | « Chat » | le modèle répond avec les documents et ses connaissances générales |
| Mode Requête | « Requête » | le modèle ne répond qu'à partir des documents ; sans passage trouvé, il renvoie la réponse de refus |
| Mode Agent | « Agent » | le modèle peut utiliser des outils (recherche dans les documents, site web, fichiers) avant de répondre ; mode par défaut d'un nouvel espace |
| Agent | `@agent` | assistant qui enchaîne des actions avec des outils (compétences) |
| Compétence | « Compétences de l'agent » | outil que l'agent peut utiliser : lire un site, chercher dans les documents, créer un fichier… |
| Agent flow | « Agent Flows » | suite d'étapes construite sans code, utilisable par l'agent |
| Serveur MCP | « MCP Servers » | petit programme qui ajoute des outils à l'agent selon un protocole standard |
| Souvenir | « Souvenirs » | information retenue par l'application et rappelée au modèle dans les conversations suivantes |
| Tâche planifiée | « Tâches planifiées » | question ou action lancée automatiquement à heure fixe |
| Routeur de modèles | « Routeur modèle » | règles qui envoient chaque question au modèle le plus adapté |
| Tri de précision | « Accuracy Optimized » | second tri des passages retrouvés par un petit modèle intégré, pour garder les plus pertinents |
| Seuil de similarité | « Seuil de similarité des documents » | score minimal qu'un passage doit atteindre pour être retenu |
| Nombre de contextes | « Nombre maximum de contextes » | nombre de passages transmis au modèle pour chaque question (4 par défaut) |
| Réflexion | bloc replié au-dessus de la réponse | raisonnement que le modèle `chat` écrit avant sa réponse |
| Jeton | « Max Tokens », « context window » | unité de texte pour un modèle, environ trois quarts de mot en français |
| Clé d'API | « Clés API » | code secret qui permet à un programme d'utiliser AnythingLLM sans l'interface |
| Widget | « Widgets de chat intégrés » | fenêtre de discussion à insérer dans une page web |
| Multi-utilisateur | « Mon équipe », « Mode multi-utilisateurs » | plusieurs comptes, chacun avec un rôle : administrateur, gestionnaire (« Manager ») ou utilisateur (« Default ») |

## Résultat

Le sens de chaque mot du manuel est disponible ici ou dans le glossaire de la série.

---
*Version décrite : AnythingLLM 1.19.0, essais du 12 novembre 2026. Détails et preuves : [rapport d'essais](../annexes/A6-rapport-d-essais.md).*
