# Banc AnythingLLM — rerank-natif — 2026-11-12T14:06:19

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
| juge_llm_oui | 36 |
| juge_llm_sur | 38 |
| erreurs | 0 |
| latence_p50_s | 13.54 |
| latence_p95_s | 50.17 |
| par_type | {'tableau': '10/10', 'fait simple': '13/13', 'scan': '4/4', 'anglais': '2/2', 'multi-documents': '3/3', 'audio': '2/2', 'piège': '4/4'} |
| pic_ram_mo | {'rag-anythingllm': 1560, 'llm-central': 719, 'llm-swap': 5726, 'llm-speaches': 1338} |
| pic_ram_application_mo | 1560 |
| vram | 8407 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | 0.0 |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | True | True | 4.93 | Le chiffre d'affaires de Vélanor en 2025 s'établit à **48,6 M€**, soit une augme |
| Q02 | fait simple | oui | True | True | 9.94 | Vélanor a été fondée en 2014. |
| Q03 | fait simple | oui | True | True | 11.62 | La présidente de Vélanor est Hélène Marchais. |
| Q04 | fait simple | oui | True | True | 12.64 | L'adresse du siège de Vélanor est le 12 quai de la Fosse, à Nantes. |
| Q05 | tableau | oui | True | True | 12.47 | Vélanor compte **412 salariés** au 31 décembre 2025. |
| Q06 | tableau | oui | True | True | 4.35 | Le chiffre d'affaires du troisième trimestre 2025 a été de **14,2 M€**. |
| Q07 | tableau | oui | True | True | 32.03 | Selon le rapport annuel 2025, 15 400 unités du modèle Sèvre Trail ont été produi |
| Q08 | tableau | oui | True | True | 18.12 | Le prix public TTC du modèle Erdre Cargo est de 4 290 €. |
| Q09 | tableau | oui | True | True | 3.87 | 97 salariés |
| Q10 | fait simple | oui | True | True | 13.54 | La part d'aluminium recyclé dans les cadres est de 82 %. |
| Q11 | fait simple | oui | True | True | 18.22 | Le taux de recyclage des batteries usagées collectées atteint 96 %. |
| Q12 | tableau | oui | True | True | 14.99 | Le fournisseur des moteurs est Motodrive Co., qui est installé en Taïwan. |
| Q13 | tableau | oui | True | True | 11.4 | Vélanor a dégagé un résultat net de 3,1 M€ en 2025. |
| Q14 | fait simple | oui | True | True | 4.41 | Le taux de retour sous garantie s'établit à 1,8 % des vélos vendus, selon le rap |
| Q15 | scan | oui | True | True | 12.99 | Selon l'article 4 du contrat d'approvisionnement, le prix unitaire des batteries |
| Q16 | scan | oui | True | True | 23.11 | Le délai de livraison prévu par le contrat Batterix est de **21 jours après la c |
| Q17 | scan | oui | True | True | 14.84 | Selon l'article 6 du contrat d'approvisionnement (N° BX-2025-117), le montant de |
| Q18 | scan | oui | True | True | 13.42 | Selon l'Article 3 du contrat d'approvisionnement n° BX-2025-117, le volume minim |
| Q19 | fait simple | oui | True | True | 10.79 | Selon la procédure PR-SEC-04, les batteries doivent être stockées entre 10 °C et |
| Q20 | fait simple | oui | True | True | 5.26 | Karim Benali, responsable HSE. |
| Q21 | tableau | oui | True | True | 3.53 | Le local B2 est inspecté le premier lundi de chaque mois, selon la procédure PR- |
| Q22 | fait simple | oui | True | True | 20.91 | Le prix public du Vilaine Compact est de 2 490 € TTC. |
| Q23 | fait simple | oui | True | True | 14.72 | La capacité prévue de l'usine de Saint-Nazaire est de 25 000 vélos par an. |
| Q24 | tableau | oui | True | True | 23.18 | Selon le fichier stocks-octobre-2025.xlsx disponible dans le contexte :  Il rest |
| Q25 | fait simple | oui | True | True | 3.35 | Le cadre est garanti pendant 7 ans. |
| Q26 | fait simple | oui | True | True | 14.1 | Le numéro de téléphone du service après-vente est le 02 40 00 12 34. |
| Q27 | fait simple | oui | True | True | 12.77 | Le montant de la prime d'intéressement 2025 est de 1 150 euros par salarié. |
| Q28 | anglais | oui | True | True | 11.7 | Batterix obtained an overall score of 87 out of 100 at the supplier audit. |
| Q29 | anglais | oui | True | True | 16.88 | Le taux de cellules défectueuses mesuré chez Batterix lors de l'audit est de 0,3 |
| Q30 | multi-documents | oui | True | True | 25.92 | Le délai de livraison contractuel stipulé par le contrat d'approvisionnement (Ar |
| Q31 | multi-documents | oui | True | True | 19.19 | Batterix a obtenu un score de 87 sur 100 à l'audit. Le contrat fixe un prix unit |
| Q32 | multi-documents | oui | True | True | 20.32 | Vélanor vise un chiffre d'affaires de 55 M€ en 2026, et il est prévu 70 embauche |
| Q33 | audio | oui | True | True | 53.15 | La ligne d'assemblage numéro 3 de Nantes sera arrêtée pour maintenance du 2 au 6 |
| Q34 | audio | oui | True | True | 10.67 | Le directeur de production de Vélanor est Julien Moreau, comme indiqué dans le m |
| Q35 | piège | oui | False | - | 48.62 | Les documents fournis ne contiennent pas d'informations sur le chiffre d'affaire |
| Q36 | piège | oui | True | - | 57.02 | D'après les documents fournis, l'identité du directeur financier de Vélanor n'es |
| Q37 | piège | oui | False | - | 50.17 | D'après les documents fournis, Vélanor SAS n'a vendu aucune trottinette électriq |
| Q38 | piège | oui | True | - | 19.72 | Les documents fournis ne contiennent aucune information sur le salaire de Karim  |
