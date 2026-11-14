# Banc AnythingLLM — serre-top2 — 2026-11-12T14:36:24

| Mesure | Valeur |
|---|---|
| questions | 38 |
| exactes | 31 |
| sur | 34 |
| refus_corrects | 4 |
| pieges | 4 |
| citation_bon_document | 32 |
| citation_bonne_page | 0 |
| citations_avec_page | 0 |
| juge_llm_oui | 35 |
| juge_llm_sur | 38 |
| erreurs | 0 |
| latence_p50_s | 13.43 |
| latence_p95_s | 34.71 |
| par_type | {'tableau': '9/10', 'fait simple': '13/13', 'scan': '4/4', 'anglais': '2/2', 'multi-documents': '2/3', 'audio': '1/2', 'piège': '4/4'} |
| pic_ram_mo | {'rag-anythingllm': 1568, 'llm-central': 716, 'llm-swap': 5734, 'llm-speaches': 1336} |
| pic_ram_application_mo | 1568 |
| vram | 8408 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | 0.2 |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | True | True | 13.0 | Le chiffre d'affaires de Vélanor en 2025 est de 48,6 M€. |
| Q02 | fait simple | oui | True | True | 8.54 | Vélanor a été fondée en 2014. |
| Q03 | fait simple | oui | True | True | 8.73 | La présidente de Vélanor est Hélène Marchais. |
| Q04 | fait simple | oui | True | True | 10.05 | L'adresse du siège de Vélanor est au 12 quai de la Fosse, à Nantes. |
| Q05 | tableau | oui | True | True | 13.37 | Vélanor compte 412 salariés au 31 décembre 2025. |
| Q06 | tableau | oui | True | True | 17.07 | Selon le rapport annuel 2025, le chiffre d'affaires du troisième trimestre 2025  |
| Q07 | tableau | oui | True | True | 15.8 | Selon le rapport annuel 2025, **15 400 unités** du modèle Sèvre Trail ont été pr |
| Q08 | tableau | oui | True | True | 14.63 | Le prix public TTC du modèle Erdre Cargo est de 4 290 €. |
| Q09 | tableau | oui | True | True | 21.19 | Selon le rapport annuel 2025, il y avait 97 salariés sur le site de Cholet au 31 |
| Q10 | fait simple | oui | True | True | 13.12 | D'après le contexte fourni, la part d'aluminium recyclé dans les cadres est de * |
| Q11 | fait simple | oui | True | True | 11.16 | Le taux de recyclage des batteries usagées collectées atteint 96 %. |
| Q12 | tableau | non | False | False | 103.55 | D'après les documents fournis, le fournisseur qui livre les moteurs est **Motodr |
| Q13 | tableau | oui | True | True | 13.51 | Selon le document fourni (page 3), Vélanor a dégagé un résultat net de **3,1 M€* |
| Q14 | fait simple | oui | True | True | 12.26 | Le taux de retour sous garantie s'établit à 1,8 % des vélos vendus. |
| Q15 | scan | oui | True | True | 19.18 | Le prix unitaire des batteries prévu par le contrat est de 212 euros HT (Article |
| Q16 | scan | oui | True | True | 19.86 | Selon l'article 5 du contrat d'approvisionnement, le délai de livraison est de * |
| Q17 | scan | oui | True | True | 15.96 | Le plafond des pénalités de retard est de 8 % du montant de la commande, conform |
| Q18 | scan | oui | True | True | 10.66 | Le contrat prévoit un volume minimal annuel de 40 000 batteries. |
| Q19 | fait simple | oui | True | True | 13.43 | Selon la procédure PR-SEC-04, les batteries doivent être stockées entre 10 °C et |
| Q20 | fait simple | oui | True | True | 17.15 | Le responsable de la procédure de charge et de stockage des batteries est Karim  |
| Q21 | tableau | oui | True | True | 9.14 | Le local B2 est inspecté le premier lundi de chaque mois. |
| Q22 | fait simple | oui | True | True | 11.71 | Le prix public du Vilaine Compact est de 2 490 € TTC. |
| Q23 | fait simple | oui | True | True | 8.82 | La capacité prévue de l'usine de Saint-Nazaire est de 25 000 vélos par an. |
| Q24 | tableau | oui | True | True | 19.78 | Le stock de batteries BAT-48V-14Ah restant s'élève à **1240 unités**, ce qui est |
| Q25 | fait simple | oui | True | True | 12.07 | Selon le document FAQ du service après-vente, la durée de garantie du cadre est  |
| Q26 | fait simple | oui | True | True | 11.96 | Le numéro de téléphone du service après-vente est le 02 40 00 12 34. |
| Q27 | fait simple | oui | True | True | 4.63 | Le montant de la prime d'intéressement 2025 est de **1 150 euros par salarié**. |
| Q28 | anglais | oui | True | True | 12.79 | Batterix obtained an overall score of 87 out of 100 at the supplier audit. |
| Q29 | anglais | oui | True | True | 14.2 | Le taux de cellules défectueuses mesuré chez Batterix lors de l'audit est de 0,3 |
| Q30 | multi-documents | non | False | True | 20.3 | Selon l'article 5 du contrat d'approvisionnement (Contexte 0), le délai de livra |
| Q31 | multi-documents | oui | True | True | 13.1 | Batterix a obtenu un score de 87 sur 100 à l'audit, et le contrat fixe un prix u |
| Q32 | multi-documents | oui | True | True | 9.36 | Vélanor vise un chiffre d'affaires de 55 M€ en 2026 et prévoit 70 embauches à Sa |
| Q33 | audio | oui | True | True | 25.71 | La ligne d'assemblage numéro 3 de Nantes sera arrêtée pour maintenance du 2 au 6 |
| Q34 | audio | non | False | False | 45.02 |  |
| Q35 | piège | oui | True | - | 32.16 | D'après les documents fournis, il n'est pas possible de connaître le chiffre d'a |
| Q36 | piège | oui | True | - | 26.24 | D'après les documents fournis, le nom du directeur financier de Vélanor n'est pa |
| Q37 | piège | oui | True | - | 34.71 | D'après les documents fournis, il n'est pas possible de répondre à cette questio |
| Q38 | piège | oui | True | - | 19.12 | Les documents fournis (rapport annuel 2025 de Vélanor SAS) ne contiennent aucune |
