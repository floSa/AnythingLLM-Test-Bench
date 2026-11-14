# Banc ragflow — essai-adaptateur — 2026-11-09T17:39:09

| Mesure | Valeur |
|---|---|
| questions | 3 |
| exactes | 3 |
| sur | 3 |
| refus_corrects | 0 |
| pieges | 0 |
| citation_bon_document | 3 |
| citation_bonne_page | 1 |
| citations_avec_page | 3 |
| juge_llm_oui | 0 |
| juge_llm_sur | 0 |
| erreurs | 0 |
| latence_p50_s | 1.43 |
| latence_p95_s | 2.66 |
| par_type | {'tableau': '1/1', 'fait simple': '2/2'} |
| pic_ram_mo | {'rag-ragflow-server': 1910, 'rag-ragflow-es01': 2570, 'rag-ragflow-mysql': 520, 'rag-ragflow-minio': 95, 'rag-ragflow-kvrocks': 22, 'rag-ragflow-nats': 9, 'vllm-central': 6686, 'vllm-embed': 4183, 'rag-speaches': 1343} |
| pic_ram_application_mo | 5126 |
| vram | 15247 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | 71.2 |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | - | True | 2.66 | Le chiffre d'affaires de Vélanor pour 2025 était de 48,6 M€ [ID:1][ID:3]. Ce chi |
| Q02 | fait simple | oui | - | True | 1.15 | Vélanor a été fondée en 2014 [ID:0]. |
| Q03 | fait simple | oui | - | True | 1.43 | La présidente de Vélanor s'appelle Hélène Marchais [ID:0]. Elle dirige l'entrepr |
