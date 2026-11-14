# Banc ragflow — defaut — 2026-11-09T18:07:29

| Mesure | Valeur |
|---|---|
| questions | 38 |
| exactes | 33 |
| sur | 34 |
| refus_corrects | 4 |
| pieges | 4 |
| citation_bon_document | 34 |
| citation_bonne_page | 24 |
| citations_avec_page | 24 |
| juge_llm_oui | 0 |
| juge_llm_sur | 0 |
| erreurs | 0 |
| latence_p50_s | 1.28 |
| latence_p95_s | 1.88 |
| par_type | {'tableau': '10/10', 'fait simple': '13/13', 'scan': '4/4', 'anglais': '2/2', 'multi-documents': '2/3', 'audio': '2/2', 'piège': '4/4'} |
| pic_ram_mo | {'rag-ragflow-server': 1980, 'rag-ragflow-es01': 2749, 'rag-ragflow-mysql': 529, 'rag-ragflow-minio': 103, 'rag-ragflow-kvrocks': 24, 'rag-ragflow-nats': 9, 'vllm-central': 6647, 'vllm-embed': 4172, 'rag-speaches': 1649} |
| pic_ram_application_mo | 5394 |
| vram | 15260 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | 53.0 |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | - | True | 1.88 | Le chiffre d'affaires de Vélanor en 2025 s'est établi à 48,6 M€ [ID:1][ID:3]. |
| Q02 | fait simple | oui | - | True | 1.05 | Vélanor a été fondée en 2014 [ID:0]. |
| Q03 | fait simple | oui | - | True | 1.21 | La présidente de Vélanor est Hélène Marchais, qui dirige l'entreprise depuis 201 |
| Q04 | fait simple | oui | - | True | 1.18 | Le siège de Vélanor est situé au 12 quai de la Fosse, à Nantes [ID:0]. |
| Q05 | tableau | oui | - | True | 1.42 | Vélanor comptait un effectif de 412 salariés au 31/12/2025 [ID:3][ID:0]. |
| Q06 | tableau | oui | - | True | 1.71 | Le chiffre d'affaires du troisième trimestre 2025 était de 14,2 M€ [ID:0]. Ce tr |
| Q07 | tableau | oui | - | True | 1.28 | Le modèle Sèvre Trail a produit 15 400 unités en 2025 [ID:0]. |
| Q08 | tableau | oui | - | True | 1.14 | Le prix public du modèle Erdre Cargo est de 4 290 € [ID:0]. |
| Q09 | tableau | oui | - | True | 1.21 | Le site de Cholet emploie 97 salariés pour l'activité de fabrication des cadres  |
| Q10 | fait simple | oui | - | True | 1.25 | Les cadres sont fabriqués à partir d'aluminium recyclé à 82 % [ID:0]. |
| Q11 | fait simple | oui | - | True | 1.39 | Le taux de recyclage des batteries usagées collectées atteint 96 % grâce au part |
| Q12 | tableau | oui | - | True | 1.32 | Le fournisseur qui livre les moteurs est Motodrive Co. et il est installé en Taï |
| Q13 | tableau | oui | - | True | 1.26 | Le résultat net de Vélanor s'est établi à 3,1 M€ en 2025 [ID:2]. |
| Q14 | fait simple | oui | - | True | 1.31 | Le taux de retour sous garantie s'établit à 1,8 % des vélos vendus [ID:0]. |
| Q15 | scan | oui | - | True | 1.41 | Le prix unitaire des batteries dans le contrat avec Batterix est de 212 euros HT |
| Q16 | scan | oui | - | True | 1.31 | Le Fournisseur livre les batteries sous 21 jours après la commande dans le contr |
| Q17 | scan | oui | - | True | 1.3 | Le plafond des pénalités de retard dans le contrat avec Batterix est fixé à 8 %  |
| Q18 | scan | oui | - | True | 1.31 | Le volume minimal annuel de batteries prévu par le contrat Batterix est de 40 00 |
| Q19 | fait simple | oui | - | True | 2.05 | Les batteries doivent être stockées entre 10 °C et 25 °C, dans le local B2 qui e |
| Q20 | fait simple | oui | - | True | 1.27 | Responsable de la procédure de charge et de stockage des batteries est Karim Ben |
| Q21 | tableau | oui | - | True | 1.09 | Le local B2 est inspecté le premier lundi de chaque mois [ID:0]. |
| Q22 | fait simple | oui | - | True | 1.15 | Le prix public du Vilaine Compact est de 2 490 € TTC [ID:0]. |
| Q23 | fait simple | oui | - | True | 1.35 | La capacité prévue de l'usine de Saint-Nazaire est de 25 000 vélos par an [ID:0] |
| Q24 | tableau | oui | - | True | 1.66 | Le stock de la batterie BAT-48V-14Ah est de 1240 unités, ce qui est en dessous d |
| Q25 | fait simple | oui | - | True | 0.95 | Le cadre est garanti 7 ans [ID:0]. |
| Q26 | fait simple | oui | - | True | 1.63 | Le service après-vente peut être joint par téléphone au 02 40 00 12 34, du lundi |
| Q27 | fait simple | oui | - | True | 1.6 | Le montant de la prime d'intéressement 2025 est de 1 150 euros par salarié, et e |
| Q28 | anglais | oui | - | True | 1.2 | Batterix obtained an overall score of 87 out of 100 during the Supplier Quality  |
| Q29 | anglais | oui | - | True | 1.14 | Le taux de défaut des cellules mesuré est de 0,3 % [ID:0]. |
| Q30 | multi-documents | non | - | True | 1.47 | Le délai contractuel de livraison de Batterix n'est pas mentionné dans les docum |
| Q31 | multi-documents | oui | - | True | 1.62 | Batterix a obtenu un score de 87 sur 100 lors de l'audit [ID:2]. Le prix unitair |
| Q32 | multi-documents | oui | - | True | 1.94 | Vélanor vise un chiffre d'affaires de 55 M€ en 2026 [ID:0][ID:2]. De plus, une s |
| Q33 | audio | oui | - | True | 1.3 | La ligne d'assoblage numéro 3 de Nantes sera arrêtée pour maintenance du 2 au 6  |
| Q34 | audio | oui | - | True | 1.05 | Le directeur de production chez Vélanor est Julien Moreau [ID:1]. |
| Q35 | piège | oui | - | - | 1.02 | The answer you are looking for is not found in the dataset! [ID:5] |
| Q36 | piège | oui | - | - | 0.42 | The answer you are looking for is not found in the dataset! [ID:2] |
| Q37 | piège | oui | - | - | 1.04 | The answer you are looking for is not found in the dataset! [ID:2] |
| Q38 | piège | oui | - | - | 1.0 | The answer you are looking for is not found in the dataset! [ID:2] |
