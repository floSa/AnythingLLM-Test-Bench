# Banc AnythingLLM — top8-rerank-natif — 2026-11-12T14:26:29

| Mesure | Valeur |
|---|---|
| questions | 38 |
| exactes | 34 |
| sur | 34 |
| refus_corrects | 4 |
| pieges | 4 |
| citation_bon_document | 34 |
| citation_bonne_page | 0 |
| citations_avec_page | 0 |
| juge_llm_oui | 37 |
| juge_llm_sur | 38 |
| erreurs | 0 |
| latence_p50_s | 10.69 |
| latence_p95_s | 37.64 |
| par_type | {'tableau': '10/10', 'fait simple': '13/13', 'scan': '4/4', 'anglais': '2/2', 'multi-documents': '3/3', 'audio': '2/2', 'piège': '4/4'} |
| pic_ram_mo | {'rag-anythingllm': 1573, 'llm-central': 718, 'llm-swap': 5725, 'llm-speaches': 1336} |
| pic_ram_application_mo | 1573 |
| vram | 8357 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | 0.0 |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | True | True | 6.06 | Le chiffre d'affaires 2025 de Vélanor s'élève à **48,6 millions d'euros**, soit  |
| Q02 | fait simple | oui | True | True | 9.37 | Vélanor a été fondée en 2014. |
| Q03 | fait simple | oui | True | True | 3.67 | La présidente de Vélanor est **Hélène Marchais**. Elle dirige l'entreprise depui |
| Q04 | fait simple | oui | True | True | 31.96 | L'adresse du siège de Vélanor est au 12 quai de la Fosse, 44000 Nantes. |
| Q05 | tableau | oui | True | True | 15.08 | Vélanor compte 412 salariés au 31 décembre 2025. |
| Q06 | tableau | oui | True | True | 5.27 | Le chiffre d'affaires du troisième trimestre 2025 a été de **14,2 M€** (selon le |
| Q07 | tableau | oui | True | True | 20.75 | Selon le rapport annuel 2025, **15 400 unités** du modèle Sèvre Trail ont été pr |
| Q08 | tableau | oui | True | True | 14.31 | Le prix public du modèle Erdre Cargo est de 4 290 € TTC. |
| Q09 | tableau | oui | True | True | 5.3 | D'après le rapport annuel de Vélanor SAS (page 6 du document), **97 salariés** t |
| Q10 | fait simple | oui | True | True | 15.84 | La part d'aluminium recyclé dans les cadres est de 82 %. |
| Q11 | fait simple | oui | True | True | 5.53 | Le taux de recyclage des batteries usagées collectées est de **96 %**, grâce au  |
| Q12 | tableau | oui | True | True | 6.04 | Le fournisseur des moteurs est **Motodrive Co.** et il est installé en **Taïwan* |
| Q13 | tableau | oui | True | True | 4.17 | 3,1 millions d'euros (3,1 M€). |
| Q14 | fait simple | oui | True | True | 5.92 | Le taux de retour sous garantie est de **1,8 %** des vélos vendus. Cette informa |
| Q15 | scan | oui | True | True | 3.35 | Le prix unitaire des batteries prévu par le contrat avec Batterix est de **212 e |
| Q16 | scan | oui | True | True | 3.9 | Selon le contrat d'approvisionnement n° BX-2025-117 (Article 5), le délai de liv |
| Q17 | scan | oui | True | True | 4.04 | Selon l'article 6 du contrat d'approvisionnement Batterix, le plafond des pénali |
| Q18 | scan | oui | True | True | 9.27 | Le contrat d'approvisionnement prévoit un volume minimal annuel de 40 000 batter |
| Q19 | fait simple | oui | True | True | 15.25 | Selon la procédure PR-SEC-04, les batteries doivent être stockées entre **10 °C  |
| Q20 | fait simple | oui | True | True | 3.52 | Karim Benali est responsable de la procédure de charge et de stockage des batter |
| Q21 | tableau | oui | True | True | 4.11 | Le local B2 est inspecté le premier lundi de chaque mois (selon la procédure PR- |
| Q22 | fait simple | oui | True | True | 4.64 | Le Vilaine Compact a un prix public de 2 490 € TTC. |
| Q23 | fait simple | oui | True | True | 5.33 | La capacité prévue de l'usine de Saint-Nazaire est de **25 000 vélos par an**, a |
| Q24 | tableau | oui | True | True | 13.47 | Il reste **1 240** batteries BAT-48V-14Ah dans le stock. Oui, ce niveau est bien |
| Q25 | fait simple | oui | True | True | 10.69 | Le cadre est garanti 7 ans. |
| Q26 | fait simple | oui | True | True | 13.56 | Le numéro de téléphone du service après-vente est le 02 40 00 12 34 (appelable d |
| Q27 | fait simple | oui | True | True | 13.61 | Le montant de la prime d'intéressement 2025 est de 1 150 euros par salarié. |
| Q28 | anglais | oui | True | True | 11.16 | Batterix obtained an overall score of 87 out of 100 at the supplier audit. |
| Q29 | anglais | oui | True | True | 30.09 | Le taux de cellules défectueuses mesuré chez Batterix lors de l'audit est de 0,3 |
| Q30 | multi-documents | oui | True | True | 25.78 | Selon le contrat d'approvisionnement n° BX-2025-117 (Article 5), le délai de liv |
| Q31 | multi-documents | oui | True | True | 15.63 | Batterix a obtenu un score de 87 sur 100 à l'audit, et le contrat fixe un prix u |
| Q32 | multi-documents | oui | True | True | 6.67 | Vélanor vise un chiffre d'affaires de **55 M€** en 2026, et **70 embauches** son |
| Q33 | audio | oui | True | True | 68.8 | La ligne d'assemblage numéro 3 de Nantes sera arrêtée du 2 au 6 mars pour mainte |
| Q34 | audio | oui | True | True | 12.28 | Le directeur de production de Vélanor est Julien Moreau. |
| Q35 | piège | oui | False | - | 29.7 | Les documents fournis ne contiennent pas d'informations sur le chiffre d'affaire |
| Q36 | piège | oui | True | - | 58.4 | D'après les documents fournis, l'identité du directeur financier de Vélanor n'es |
| Q37 | piège | oui | True | - | 37.64 | D'après les documents fournis, il n'existe aucune information concernant les ven |
| Q38 | piège | oui | True | - | 27.61 | D'après les documents fournis, il n'est pas possible de déterminer le salaire de |
