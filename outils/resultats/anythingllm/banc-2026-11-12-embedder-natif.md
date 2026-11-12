# Banc AnythingLLM — embedder-natif — 2026-11-12T13:07:04

| Mesure | Valeur |
|---|---|
| questions | 38 |
| exactes | 25 |
| sur | 34 |
| refus_corrects | 4 |
| pieges | 4 |
| citation_bon_document | 32 |
| citation_bonne_page | 0 |
| citations_avec_page | 0 |
| juge_llm_oui | 27 |
| juge_llm_sur | 38 |
| erreurs | 0 |
| latence_p50_s | 11.97 |
| latence_p95_s | 45.18 |
| par_type | {'tableau': '5/10', 'fait simple': '12/13', 'scan': '3/4', 'anglais': '2/2', 'multi-documents': '1/3', 'audio': '2/2', 'piège': '4/4'} |
| pic_ram_mo | {'rag-anythingllm': 617, 'llm-central': 676, 'llm-swap': 5678, 'llm-speaches': 1339} |
| pic_ram_application_mo | 617 |
| vram | 8101 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | 0.0 |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | non | False | True | 83.66 | D'après les documents fournis, le chiffre d'affaires exact de Vélanor pour l'ann |
| Q02 | fait simple | oui | True | True | 11.11 | Vélanor a été fondée en 2014. |
| Q03 | fait simple | oui | True | True | 10.64 | D'après les documents fournis, la présidente de Vélanor est Hélène Marchais. Ell |
| Q04 | fait simple | oui | True | True | 8.91 | L'adresse du siège de Vélanor est au 12 quai de la Fosse, à Nantes. |
| Q05 | tableau | oui | True | True | 3.33 | Vélanor compte **412 salariés** au 31 décembre 2025. |
| Q06 | tableau | oui | False | True | 14.8 | Selon le rapport annuel 2025 mentionné dans les documents, le chiffre d'affaires |
| Q07 | tableau | oui | True | True | 19.09 | 15 400 unités ont été produites en 2025. |
| Q08 | tableau | non | False | True | 25.16 | D’après les documents fournis, le prix public du modèle Erdre Cargo n’est pas me |
| Q09 | tableau | non | False | True | 52.27 | Les documents fournis ne précisent pas le nombre de salariés travaillant spécifi |
| Q10 | fait simple | oui | True | True | 11.98 | La part d'aluminium recyclé dans les cadres est de 82 %. |
| Q11 | fait simple | oui | True | True | 12.44 | Le taux de recyclage des batteries usagées collectées atteint 96 %, grâce au par |
| Q12 | tableau | non | False | True | 6.08 | Je n'ai pas d'informations dans les documents fournis concernant le fournisseur  |
| Q13 | tableau | non | False | True | 9.3 | D'après les documents fournis, Vélanor n'a pas de résultat net précis mentionné  |
| Q14 | fait simple | non | False | True | 8.03 | Les documents fournis ne contiennent pas d'information sur le taux de retour sou |
| Q15 | scan | oui | True | True | 19.43 | Selon l'Article 4 du contrat d'approvisionnement (Contexte 1), le prix unitaire  |
| Q16 | scan | non | False | False | 8.36 | Je ne trouve aucune information concernant un contrat Batterix ou son délai de l |
| Q17 | scan | oui | True | True | 12.13 | Le plafond des pénalités de retard est de 8 % du montant de la commande (Article |
| Q18 | scan | oui | True | True | 12.05 | Selon le contrat d'approvisionnement (Article 3), le volume minimal annuel prévu |
| Q19 | fait simple | oui | True | True | 11.88 | Selon la procédure PR-SEC-04 (Contexte 0), les batteries doivent être stockées e |
| Q20 | fait simple | oui | True | True | 11.56 | Karim Benali est responsable de la procédure de charge et de stockage des batter |
| Q21 | tableau | oui | True | True | 7.93 | Le local B2 est inspecté le premier lundi de chaque mois. |
| Q22 | fait simple | oui | True | True | 11.97 | Le prix public du Vilaine Compact est de 2 490 € TTC. |
| Q23 | fait simple | oui | True | True | 4.31 | La capacité prévue de l'usine de Saint-Nazaire est de **25 000 vélos par an**, s |
| Q24 | tableau | oui | True | True | 18.21 | Il reste un stock de 1240 batteries BAT-48V-14Ah. Oui, ce stock est sous le seui |
| Q25 | fait simple | oui | True | True | 9.96 | Selon le document de FAQ du service après-vente, le cadre est garanti **7 ans**. |
| Q26 | fait simple | oui | True | True | 10.63 | Le numéro de téléphone du service après-vente est le 02 40 00 12 34. |
| Q27 | fait simple | oui | True | True | 11.38 | Le montant de la prime d'intéressement 2025 est de 1 150 euros par salarié. |
| Q28 | anglais | oui | True | True | 11.47 | Batterix obtained an overall score of 87 out of 100. |
| Q29 | anglais | oui | True | True | 16.1 | Le taux de cellules défectueuses mesuré chez Batterix lors de l'audit est de 0,3 |
| Q30 | multi-documents | non | False | True | 35.24 | D'après le contrat d'approvisionnement n° BX-2025-117 (Contexte 3), le délai de  |
| Q31 | multi-documents | non | False | False | 29.41 | Les documents fournis ne contiennent aucune information concernant l'entreprise  |
| Q32 | multi-documents | oui | True | True | 12.02 | Vélanor vise un chiffre d'affaires de 55 M€ en 2026 et prévoit 70 embauches pour |
| Q33 | audio | oui | True | True | 30.7 | La ligne d'assemblage numéro 3 de Nantes sera arrêtée pour maintenance du 2 au 6 |
| Q34 | audio | oui | True | True | 9.4 | Le directeur de production de Vélanor est Julien Moreau. |
| Q35 | piège | oui | True | - | 7.41 | D'après les documents fournis, aucun chiffre d'affaires spécifique pour l'exerci |
| Q36 | piège | oui | True | - | 45.18 | D'après les documents fournis, le nom du directeur financier de Vélanor n'est pa |
| Q37 | piège | oui | False | - | 40.39 | D'après les documents fournis, il n'est pas indiqué combien de trottinettes élec |
| Q38 | piège | oui | True | - | 16.7 | Les documents fournis ne contiennent aucune information sur le salaire de Karim  |
