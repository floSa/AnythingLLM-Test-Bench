# Banc ragflow — hybride-vecteurs07-top8 — 2026-11-12T08:43:41

| Mesure | Valeur |
|---|---|
| questions | 38 |
| exactes | 34 |
| sur | 34 |
| refus_corrects | 4 |
| pieges | 4 |
| citation_bon_document | 34 |
| citation_bonne_page | 24 |
| citations_avec_page | 24 |
| juge_llm_oui | 0 |
| juge_llm_sur | 0 |
| erreurs | 0 |
| latence_p50_s | 7.76 |
| latence_p95_s | 56.92 |
| par_type | {'tableau': '10/10', 'fait simple': '13/13', 'scan': '4/4', 'anglais': '2/2', 'multi-documents': '3/3', 'audio': '2/2', 'piège': '4/4'} |
| pic_ram_mo | {'rag-ragflow-server': 1424, 'rag-ragflow-es01': 2859, 'rag-ragflow-mysql': 554, 'rag-ragflow-minio': 159, 'rag-ragflow-kvrocks': 55, 'rag-ragflow-nats': 25, 'llm-central': 705, 'llm-swap': 6796, 'llm-speaches': 1386} |
| pic_ram_application_mo | 5076 |
| vram | 8245 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | None |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | - | True | 11.74 | Le chiffre d'affaires de Vélanor en 2025 s'élève à **48,6 M€**, avec une évoluti |
| Q02 | fait simple | oui | - | True | 4.13 | Vélanor a été fondée en **2014**.  Cette information est disponible dans le rapp |
| Q03 | fait simple | oui | - | True | 5.64 | La présidente de Vélanor est **Hélène Marchais**. Elle dirige l'entreprise depui |
| Q04 | fait simple | oui | - | True | 50.92 | D'après le rapport annuel 2025 et les documents contractuels fournis, voici les  |
| Q05 | tableau | oui | - | True | 7.04 | Vélanor compte au total **412 salariés** au 31 décembre 2025.  Cet effectif glob |
| Q06 | tableau | oui | - | True | 7.76 | Le chiffre d'affaires du troisième trimestre 2025 était de 14,2 [ID:0] M€. Ce ré |
| Q07 | tableau | oui | - | True | 7.92 | En 2025, **15 400 unités** du modèle Sèvre Trail ont été produites [ID:0].  Ce m |
| Q08 | tableau | oui | - | True | 6.39 | Le prix public TTC du modèle Erdre Cargo est de 4 290 €.  Cette information prov |
| Q09 | tableau | oui | - | True | 4.43 | D'après les documents du rapport annuel 2025, il y a **97 salariés** au site de  |
| Q10 | fait simple | oui | - | True | 7.05 | La part d'aluminium recyclé dans les cadres de Vélanor est de **82 %**.   Cette  |
| Q11 | fait simple | oui | - | True | 64.09 | Le taux de recyclage des batteries usagées collectées atteint 96 %[ID:0], grâce  |
| Q12 | tableau | oui | - | True | 6.95 | Basé sur les documents fournis, je peux répondre à votre question concernant le  |
| Q13 | tableau | oui | - | True | 59.93 | Selon les documents analysés, Vélanor a dégagé un **résultat net de 3,1 M€** pou |
| Q14 | fait simple | oui | - | True | 9.33 | Le taux de retour sous garantie est de **1,8 % des vélos vendus**.  [ID:0] |
| Q15 | scan | oui | - | True | 12.73 | Based on the dataset content, here is the information about the unit price for b |
| Q16 | scan | oui | - | True | 11.6 | Le contrat d'approvisionnement avec Batterix prévoit un délai de livraison de 21 |
| Q17 | scan | oui | - | True | 6.69 | Le plafond des pénalités de retard du contrat Batterix est de **8 % du montant d |
| Q18 | scan | oui | - | True | 6.62 | Le contrat d'approvisionnement avec Batterix prévoit un **volume minimal annuel  |
| Q19 | fait simple | oui | - | True | 8.93 | Les batteries doivent être stockées entre **10 °C et 25 °C** selon la procédure  |
| Q20 | fait simple | oui | - | True | 7.63 | Selon les documents de la base de connaissances, la procédure de charge et de st |
| Q21 | tableau | oui | - | True | 4.98 | Le local B2 est inspecté au premier lundi de chaque mois [ID:0]. |
| Q22 | fait simple | oui | - | True | 7.21 | Le prix du Vilaine Compact est de **2 490 € TTC** [ID:0].  Ce vélo électrique pl |
| Q23 | fait simple | oui | - | True | 53.4 | Voici les données extraites du jeu de connaissances pertinentes pour votre quest |
| Q24 | tableau | oui | - | True | 55.01 | D'après le fichier `stocks-octobre-2025.xlsx`, la référence BAT-48V-14Ah présent |
| Q25 | fait simple | oui | - | True | 56.92 | Selon le document FAQ du service après-vente, la durée de garantie pour le cadre |
| Q26 | fait simple | oui | - | True | 50.68 | Le numéro de téléphone du service après-vente est le 02 40 00 12 34 [ID:0]. Il e |
| Q27 | fait simple | oui | - | True | 4.84 | Le montant de la prime d'intéressement 2025 s'élève à **1 150 euros par salarié* |
| Q28 | anglais | oui | - | True | 6.05 | Based on the provided document, the supplier audit results for Batterix GmbH sho |
| Q29 | anglais | oui | - | True | 7.14 | According to the supplier quality audit document, the measured cell defect rate  |
| Q30 | multi-documents | oui | - | True | 8.19 | Selon le contrat d'approvisionnement avec Batterix GmbH, le délai contractuel de |
| Q31 | multi-documents | oui | - | True | 7.15 | Le contrat d'approvisionnement fixe un prix unitaire de 212 euros HT pour les ba |
| Q32 | multi-documents | oui | - | True | 7.46 | Vélanor vise un chiffre d'affaires de **55 millions d'euros (M€)** en 2026, et * |
| Q33 | audio | oui | - | True | 13.86 | Pour répondre à votre question concernant l'arrêt de ligne d'assemblage pour mai |
| Q34 | audio | oui | - | True | 6.63 | Selon les documents disponibles, le directeur de production de Vélanor est **Jul |
| Q35 | piège | oui | - | - | 9.52 | Based on my analysis of the knowledge base documents, there is **no information  |
| Q36 | piège | oui | - | - | 9.63 | Le document fourni ne contient pas d'information sur le directeur financier de V |
| Q37 | piège | oui | - | - | 15.38 | Based on the provided documents, Vélanor SAS (a French company) produces and ass |
| Q38 | piège | oui | - | - | 9.25 | Basé sur les documents fournis dans la base de connaissances, il n'y a **aucune  |
