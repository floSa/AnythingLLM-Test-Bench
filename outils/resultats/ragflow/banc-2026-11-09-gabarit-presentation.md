# Banc ragflow — gabarit-presentation — 2026-11-09T18:15:33

| Mesure | Valeur |
|---|---|
| questions | 38 |
| exactes | 32 |
| sur | 34 |
| refus_corrects | 4 |
| pieges | 4 |
| citation_bon_document | 33 |
| citation_bonne_page | 23 |
| citations_avec_page | 23 |
| juge_llm_oui | 0 |
| juge_llm_sur | 0 |
| erreurs | 0 |
| latence_p50_s | 1.18 |
| latence_p95_s | 1.86 |
| par_type | {'tableau': '10/10', 'fait simple': '13/13', 'scan': '4/4', 'anglais': '1/2', 'multi-documents': '2/3', 'audio': '2/2', 'piège': '4/4'} |
| pic_ram_mo | {'rag-ragflow-server': 2061, 'rag-ragflow-es01': 2770, 'rag-ragflow-mysql': 535, 'rag-ragflow-minio': 102, 'rag-ragflow-kvrocks': 26, 'rag-ragflow-nats': 9, 'vllm-central': 6647, 'vllm-embed': 4171, 'rag-speaches': 1479} |
| pic_ram_application_mo | 5503 |
| vram | 15242 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | 53.0 |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | - | True | 1.42 | Le chiffre d'affaires de Vélanor pour 2025 s'élève à 48,6 M€ [ID:3][ID:5]. |
| Q02 | fait simple | oui | - | True | 0.99 | Vélanor a été fondée en 2014 à Nantes [ID:0]. |
| Q03 | fait simple | oui | - | True | 1.18 | La présidente de Vélanor est Hélène Marchais [ID:0]. Elle dirige l'entreprise de |
| Q04 | fait simple | oui | - | True | 1.08 | Le siège de Vélanor est situé au 12 quai de la Fosse, à Nantes [ID:0]. |
| Q05 | tableau | oui | - | True | 2.86 | Vélanor comptait 412 salariés au 31/12/2025 [ID:1].  Voici la répartition des ef |
| Q06 | tableau | oui | - | True | 1.63 | Le chiffre d'affaires du troisième trimestre 2025 était de 14,2 M€ [ID:0]. Ce tr |
| Q07 | tableau | oui | - | True | 1.29 | Le nombre d'unités produites du modèle Sèvre Trail en 2025 était de 15 400 [ID:0 |
| Q08 | tableau | oui | - | True | 1.46 | Le prix public TTC du modèle Erdre Cargo est de 4 290 € [ID:0]. De plus, il est  |
| Q09 | tableau | oui | - | True | 1.11 | Le nombre de salariés travaillant sur le site de Cholet est de 97 [ID:0]. |
| Q10 | fait simple | oui | - | True | 1.19 | Les cadres sont fabriqués à partir d'aluminium recyclé à 82 % [ID:0]. |
| Q11 | fait simple | oui | - | True | 1.27 | Le taux de recyclage des batteries usagées collectées atteint 96 % grâce au part |
| Q12 | tableau | oui | - | True | 1.2 | Le fournisseur qui livre les moteurs est Motodrive Co. et il est installé en Taï |
| Q13 | tableau | oui | - | True | 1.17 | Le résultat net de Vélanor s'est établi à 3,1 M€ en 2025 [ID:5]. |
| Q14 | fait simple | oui | - | True | 1.24 | Le taux de retour sous garantie s'établit à 1,8 % des vélos vendus [ID:0]. |
| Q15 | scan | oui | - | True | 1.21 | Le prix unitaire prévu dans le contrat avec Batterix est de 212 euros HT, avec u |
| Q16 | scan | oui | - | True | 1.13 | Le fournisseur livre sous 21 jours après la commande, conformément à l'Article 5 |
| Q17 | scan | oui | - | True | 1.13 | Le plafond des pénalités de retard dans le contrat Batterix est fixé à 8% du mon |
| Q18 | scan | oui | - | True | 1.07 | Le contrat avec Batterix prévoit un volume minimal annuel de 40 000 batteries [I |
| Q19 | fait simple | oui | - | True | 1.8 | Les batteries doivent être stockées entre 10 °C et 25 °C dans le local B2 équipé |
| Q20 | fait simple | oui | - | True | 1.08 | Le responsable de la procédure de charge et de stockage des batteries est Karim  |
| Q21 | tableau | oui | - | True | 1.02 | Le local B2 est inspecté le premier lundi de chaque mois [ID:0]. |
| Q22 | fait simple | oui | - | True | 1.06 | Le prix public du Vilaine Compact est de 2 490 € TTC [ID:0]. |
| Q23 | fait simple | oui | - | True | 1.31 | La capacité prévue de l'usine de Saint-Nazaire est de 25 000 vélos par an [ID:0] |
| Q24 | tableau | oui | - | True | 4.51 | Le stock restant pour la référence BAT-48V-14Ah est de 1240 unités [ID:0], et ce |
| Q25 | fait simple | oui | - | True | 0.92 | La garantie du cadre est de 7 ans [ID:0]. |
| Q26 | fait simple | oui | - | True | 1.61 | Le service après-vente peut être joint par téléphone au 02 40 00 12 34, du lundi |
| Q27 | fait simple | oui | - | True | 1.44 | La prime d'intéressement 2025 est de 1 150 euros par salarié et sera versée en a |
| Q28 | anglais | oui | - | True | 1.04 | The overall score obtained by the supplier during the audit was 87 out of 100 [I |
| Q29 | anglais | non | - | False | 0.98 | The answer you are looking for is not found in the dataset! [ID:1] |
| Q30 | multi-documents | non | - | True | 1.86 | Le contrat d'approvisionnement en batteries avec Batterix a été renouvelé en mar |
| Q31 | multi-documents | oui | - | True | 1.86 | Le score global obtenu par Batterix lors de l'audit est de 87 sur 100, ce qui a  |
| Q32 | multi-documents | oui | - | True | 1.85 | Vélanor vise un chiffre d'affaires de 55 M€ en 2026 [ID:0][ID:1]. De plus, une s |
| Q33 | audio | oui | - | True | 1.21 | La ligne d'assemblage numéro 3 de Nantes sera arrêtée pour maintenance du 2 au 6 |
| Q34 | audio | oui | - | True | 0.96 | Le directeur de production chez Vélanor est Julien Moreau [ID:0]. |
| Q35 | piège | oui | - | - | 0.94 | The answer you are looking for is not found in the dataset! [ID:4] |
| Q36 | piège | oui | - | - | 0.91 | The answer you are looking for is not found in the dataset! [ID:5] |
| Q37 | piège | oui | - | - | 0.9 | The answer you are looking for is not found in the dataset! [ID:4] |
| Q38 | piège | oui | - | - | 0.96 | The answer you are looking for is not found in the dataset! [ID:3] |
