# Banc ragflow — defaut-reranker — 2026-11-12T08:32:43

| Mesure | Valeur |
|---|---|
| questions | 38 |
| exactes | 34 |
| sur | 34 |
| refus_corrects | 4 |
| pieges | 4 |
| citation_bon_document | 33 |
| citation_bonne_page | 23 |
| citations_avec_page | 23 |
| juge_llm_oui | 0 |
| juge_llm_sur | 0 |
| erreurs | 0 |
| latence_p50_s | 8.31 |
| latence_p95_s | 58.31 |
| par_type | {'tableau': '10/10', 'fait simple': '13/13', 'scan': '4/4', 'anglais': '2/2', 'multi-documents': '3/3', 'audio': '2/2', 'piège': '4/4'} |
| pic_ram_mo | {'rag-ragflow-server': 1456, 'rag-ragflow-es01': 2858, 'rag-ragflow-mysql': 552, 'rag-ragflow-minio': 159, 'rag-ragflow-kvrocks': 56, 'rag-ragflow-nats': 23, 'llm-central': 704, 'llm-swap': 6762, 'llm-speaches': 1386} |
| pic_ram_application_mo | 5104 |
| vram | 8256 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | None |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | - | True | 43.44 | Le chiffre d'affaires de Vélanor pour l'année 2025 s'est élevé à 48,6 millions d |
| Q02 | fait simple | oui | - | True | 4.17 | Vélanor a été fondée en 2014.  Selon le rapport annuel 2025, Vélanor conçoit et  |
| Q03 | fait simple | oui | - | False | 11.21 | Based on the provided knowledge base, here are the details about the president o |
| Q04 | fait simple | oui | - | True | 64.97 | L'adresse du siège de Vélanor est indiquée comme étant au 12 quai de la Fosse, à |
| Q05 | tableau | oui | - | True | 9.96 | Vélanor compte **412 salariés** au 31 décembre 2025 [ID:0][ID:2].  Cette informa |
| Q06 | tableau | oui | - | True | 58.31 | D'après le rapport annuel de Vélanor SAS, le chiffre d'affaires du troisième tri |
| Q07 | tableau | oui | - | True | 5.11 | En 2025, **15 400** unités du modèle Sèvre Trail ont été produites par Vélanor S |
| Q08 | tableau | oui | - | True | 17.15 | Le prix public TTC du modèle Erdre Cargo est de 4 290 € [ID:0]. Il s'agit égalem |
| Q09 | tableau | oui | - | True | 18.89 | D'après les données du rapport annuel 2025, le site de Cholet emploie 97 salarié |
| Q10 | fait simple | oui | - | True | 6.24 | La part d'aluminium recyclé dans les cadres est de **82 %**.  This information c |
| Q11 | fait simple | oui | - | True | 5.19 | Le taux de recyclage des batteries usagées collectées atteint 96 %, grâce au par |
| Q12 | tableau | oui | - | True | 4.55 | Based on the provided knowledge base, I can answer your question about the motor |
| Q13 | tableau | oui | - | True | 36.72 | Selon les chiffres clés publiés dans le rapport annuel 2025 de Vélanor SAS, l'en |
| Q14 | fait simple | oui | - | True | 42.29 | Le taux de retour sous garantie s'établit à 1,8 % des vélos vendus selon les don |
| Q15 | scan | oui | - | True | 7.12 | Selon le contrat d'approvisionnement (Contrat n°BX-2025-117) signé entre Velanor |
| Q16 | scan | oui | - | True | 6.97 | Selon le contrat d'approvisionnement avec Batterix GmbH :  Le délai de livraison |
| Q17 | scan | oui | - | True | 8.71 | Selon le contrat d'approvisionnement n°BX-2025-117 signé avec Batterix GmbH, le  |
| Q18 | scan | oui | - | True | 48.97 | Le contrat d'approvisionnement avec Batterix GmbH spécifie clairement le volume  |
| Q19 | fait simple | oui | - | True | 5.2 | Les batteries doivent être stockées entre **10 °C et 25 °C** selon la procédure  |
| Q20 | fait simple | oui | - | True | 6.2 | Selon le document concernant la **Procédure PR-SEC-04 — Charge et stockage des b |
| Q21 | tableau | oui | - | True | 5.22 | Based on the provided document, here is the information about the inspection fre |
| Q22 | fait simple | oui | - | True | 8.06 | Le prix public du vélo Vilaine Compact est de **2 490 € TTC**.  Voici les détail |
| Q23 | fait simple | oui | - | True | 6.46 | La capacité prévue de l'usine de Saint-Nazaire est de **25 000 vélos par an** [I |
| Q24 | tableau | oui | - | True | 7.11 | D'après les données disponibles dans le fichier stocks-octobre-2025.xlsx :  Le s |
| Q25 | fait simple | oui | - | True | 6.57 | D'après les documents fournis, voici la durée de garantie du cadre :  **Le cadre |
| Q26 | fait simple | oui | - | True | 66.16 | Selon le document FAQ du service après-vente [ID:0], le numéro de téléphone pour |
| Q27 | fait simple | oui | - | True | 4.6 | Le montant de la prime d'intéressement 2025 est de **1 150 euros par salarié**,  |
| Q28 | anglais | oui | - | True | 4.56 | Batterix GmbH received an overall score of **87 out of 100** at their supplier a |
| Q29 | anglais | oui | - | True | 8.99 | Le taux de cellules défectueuses mesuré chez Batterix lors de l'audit est de 0,3 |
| Q30 | multi-documents | oui | - | True | 38.06 | Le délai contractuel d'approvisionnement avec le fournisseur Batterix GmbH est c |
| Q31 | multi-documents | oui | - | True | 10.51 | Selon les documents fournis dans la base de connaissances :  **Score audit Batte |
| Q32 | multi-documents | oui | - | True | 8.23 | Vélanor vise un chiffre d'affaires de **55 M€ en 2026** et prévoit **70 embauche |
| Q33 | audio | oui | - | True | 17.69 | Basé sur les documents de la base de connaissances, voici les informations dispo |
| Q34 | audio | oui | - | True | 8.31 | Selon le dossier du message vocal enregistré le 3 novembre VVTSEC, le directeur  |
| Q35 | piège | oui | - | - | 15.08 | Il n'y a aucune information sur le chiffre d'affaires de Vélanor en 2022 dans le |
| Q36 | piège | oui | - | - | 9.24 | Le nom du directeur financier de Vélanor n'est pas mentionné dans les documents  |
| Q37 | piège | oui | - | - | 11.93 | D'après les documents fournis, je ne trouve pas d'informations sur le nombre de  |
| Q38 | piège | oui | - | - | 6.45 | Based on the provided dataset, there is no information about Karim Benali's sala |
