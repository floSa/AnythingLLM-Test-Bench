# Banc AnythingLLM — defaut-sans-rerank — 2026-11-12T13:45:49

| Mesure | Valeur |
|---|---|
| questions | 38 |
| exactes | 33 |
| sur | 34 |
| refus_corrects | 3 |
| pieges | 4 |
| citation_bon_document | 33 |
| citation_bonne_page | 0 |
| citations_avec_page | 0 |
| juge_llm_oui | 35 |
| juge_llm_sur | 38 |
| erreurs | 0 |
| latence_p50_s | 14.25 |
| latence_p95_s | 27.78 |
| par_type | {'tableau': '10/10', 'fait simple': '13/13', 'scan': '4/4', 'anglais': '2/2', 'multi-documents': '3/3', 'audio': '1/2', 'piège': '3/4'} |
| pic_ram_mo | {'rag-anythingllm': 887, 'llm-central': 681, 'llm-swap': 5721, 'llm-speaches': 1336} |
| pic_ram_application_mo | 887 |
| vram | 8116 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | 8.5 |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | True | True | 3.59 | Le chiffre d'affaires de Vélanor en 2025 s'élève à **48,6 millions d'euros** (+1 |
| Q02 | fait simple | oui | True | True | 10.96 | Vélanor a été fondée en 2014. |
| Q03 | fait simple | oui | True | True | 6.15 | La présidente de Vélanor SAS est Hélène Marchais. |
| Q04 | fait simple | oui | True | True | 13.11 | Selon le rapport annuel 2025, l'adresse du siège de Vélanor est située au 12 qua |
| Q05 | tableau | oui | True | True | 14.86 | Vélanor compte 412 salariés au 31 décembre 2025. |
| Q06 | tableau | oui | True | True | 4.48 | Le chiffre d'affaires du troisième trimestre 2025 a été de **14,2 M€**. |
| Q07 | tableau | oui | True | True | 17.48 | 15 400 unités. |
| Q08 | tableau | oui | True | True | 15.54 | Le prix public TTC du modèle Erdre Cargo est de 4 290 €. |
| Q09 | tableau | oui | True | True | 23.5 | Selon le rapport annuel 2025, il y a **97 salariés** sur le site de Cholet (au 3 |
| Q10 | fait simple | oui | True | True | 14.25 | La part d'aluminium recyclé dans les cadres est de 82 %. |
| Q11 | fait simple | oui | True | True | 15.2 | Selon le rapport annuel 2025 mentionné dans le contexte, le taux de recyclage de |
| Q12 | tableau | oui | True | True | 14.16 | Le fournisseur qui livre les moteurs est **Motodrive Co.**, et il est installé e |
| Q13 | tableau | oui | True | True | 15.54 | Selon les chiffres clés de l'année 2025 figurant dans le rapport annuel, Vélanor |
| Q14 | fait simple | oui | True | True | 15.89 | Selon le rapport annuel 2025 disponible dans le contexte, le taux de retour sous |
| Q15 | scan | oui | True | True | 15.97 | Le prix unitaire prévu par le contrat avec Batterix est de 212 euros HT, comme i |
| Q16 | scan | oui | True | True | 17.19 | Selon l'article 5 du contrat d'approvisionnement (Contrat d'Approvisionnement N° |
| Q17 | scan | oui | True | True | 3.28 | Selon l'article 6 du contrat d'approvisionnement avec Batterix, le plafond des p |
| Q18 | scan | oui | True | True | 12.14 | Le contrat prévoit un volume minimal annuel de 40 000 batteries. |
| Q19 | fait simple | oui | True | True | 8.41 | Selon la procédure PR-SEC-04, les batteries doivent être stockées entre 10 °C et |
| Q20 | fait simple | oui | True | True | 13.45 | Selon la procédure PR-SEC-04 — Charge et stockage des batteries, le responsable  |
| Q21 | tableau | oui | True | True | 10.26 | Le local B2 est inspecté le premier lundi de chaque mois. |
| Q22 | fait simple | oui | True | True | 11.18 | Le prix public du modèle Vilaine Compact est de 2 490 € TTC. |
| Q23 | fait simple | oui | True | True | 11.61 | La capacité prévue de l'usine de Saint-Nazaire est de 25 000 vélos par an. |
| Q24 | tableau | oui | True | True | 20.03 | Il reste **1240** batteries BAT-48V-14Ah. Oui, ce stock est bien **sous le seuil |
| Q25 | fait simple | oui | True | True | 12.22 | Selon le document FAQ du service après-vente, le cadre est garanti 7 ans. |
| Q26 | fait simple | oui | True | True | 14.22 | Le numéro de téléphone du service après-vente est le 02 40 00 12 34. |
| Q27 | fait simple | oui | True | True | 10.38 | Le montant de la prime d'intéressement 2025 est de 1 150 euros par salarié. |
| Q28 | anglais | oui | True | True | 9.61 | Batterix obtained an overall score of 87 out of 100 at the supplier audit. |
| Q29 | anglais | oui | True | True | 16.85 | Le taux de cellules défectueuses mesuré chez Batterix lors de l'audit est de 0,3 |
| Q30 | multi-documents | oui | True | True | 14.47 | D'après le contrat d'approvisionnement (Article 5), le délai de livraison contra |
| Q31 | multi-documents | oui | True | True | 17.22 | Batterix a obtenu un score de 87 sur 100 à l'audit, et le contrat fixe un prix u |
| Q32 | multi-documents | oui | True | True | 14.51 | Vélanor vise un chiffre d'affaires de 55 M€ en 2026 et prévoit 70 embauches à Sa |
| Q33 | audio | oui | True | True | 26.0 | La ligne d'assemblage numéro 3 de Nantes sera arrêtée pour maintenance du 2 au 6 |
| Q34 | audio | non | False | False | 57.8 | Le document rapporté annuel 2025 ne mentionne pas le nom du directeur de product |
| Q35 | piège | oui | True | - | 9.83 | Je ne trouve pas dans les documents fournis aucune mention du chiffre d'affaires |
| Q36 | piège | oui | True | - | 27.78 | Les documents fournis dans le contexte (le rapport annuel 2025 de Vélanor SAS) n |
| Q37 | piège | oui | False | - | 39.79 | Selon les documents fournis, il n'existe aucune information sur le nombre de tro |
| Q38 | piège | non | False | - | 23.49 |  |
