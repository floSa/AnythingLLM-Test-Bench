# Banc ragflow — gabarit-paper — 2026-11-09T18:13:46

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
| latence_p50_s | 1.19 |
| latence_p95_s | 2.31 |
| par_type | {'tableau': '10/10', 'fait simple': '13/13', 'scan': '4/4', 'anglais': '2/2', 'multi-documents': '2/3', 'audio': '2/2', 'piège': '4/4'} |
| pic_ram_mo | {'rag-ragflow-server': 2145, 'rag-ragflow-es01': 2766, 'rag-ragflow-mysql': 532, 'rag-ragflow-minio': 98, 'rag-ragflow-kvrocks': 25, 'rag-ragflow-nats': 9, 'vllm-central': 6647, 'vllm-embed': 4172, 'rag-speaches': 1527} |
| pic_ram_application_mo | 5575 |
| vram | 15241 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | 55.9 |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | - | True | 2.31 | Le chiffre d'affaires de Vélanor pour 2025 s'est établi à 48,6 M€ [ID:2]. Les do |
| Q02 | fait simple | oui | - | True | 0.99 | Vélanor a été fondée en 2014 [ID:0]. |
| Q03 | fait simple | oui | - | True | 1.0 | La présidente de Vélanor est Hélène Marchais [ID:0]. |
| Q04 | fait simple | oui | - | True | 1.12 | Le siège de Vélanor est situé au 12 quai de la Fosse, à Nantes [ID:0]. |
| Q05 | tableau | oui | - | True | 2.48 | L'effectif total de Vélanor au 31/12/2025 était de 412 salariés [ID:1]. Ce nombr |
| Q06 | tableau | oui | - | True | 1.59 | Le chiffre d'affaires du troisième trimestre (T3) 2025 a été de 14,2 M€, ce trim |
| Q07 | tableau | oui | - | True | 1.19 | Le modèle Sèvre Trail a produit 15 400 unités en 2025 [ID:0]. |
| Q08 | tableau | oui | - | True | 1.09 | Le prix public TTC du modèle Erdre Cargo est de 4 290 € [ID:0]. |
| Q09 | tableau | oui | - | True | 1.13 | 97 salariés travaillent sur le site de Cholet pour l'activité de fabrication des |
| Q10 | fait simple | oui | - | True | 1.19 | Les cadres sont fabriqués à partir d'aluminium recyclé à 82 % [ID:0]. |
| Q11 | fait simple | oui | - | True | 1.36 | Le taux de recyclage des batteries usagées collectées atteint 96 % grâce au part |
| Q12 | tableau | oui | - | True | 1.24 | Le fournisseur des moteurs est Motodrive Co., et il est installé au Taïwan [ID:1 |
| Q13 | tableau | oui | - | True | 1.2 | Vélanor a dégagé un résultat net de 3,1 M€ en 2025 [ID:3]. |
| Q14 | fait simple | oui | - | True | 1.29 | Le taux de retour sous garantie s'établit à 1,8 % des vélos vendus [ID:0]. |
| Q15 | scan | oui | - | True | 1.47 | Le prix unitaire des batteries dans le contrat d'approvisionnement avec Batterix |
| Q16 | scan | oui | - | True | 1.08 | Le Fournisseur livre sous 21 jours après la commande [ID:1]. |
| Q17 | scan | oui | - | True | 1.32 | Le plafond des pénalités de retard pour le contrat Batterix est fixé à 8 % du mo |
| Q18 | scan | oui | - | True | 1.32 | Le volume minimal annuel de batteries prévu dans le contrat Batterix est de 40 0 |
| Q19 | fait simple | oui | - | True | 1.43 | Les batteries doivent être stockées entre 10 °C et 25 °C, dans le local B2 équip |
| Q20 | fait simple | oui | - | True | 1.22 | Le responsable de la procédure de charge et de stockage des batteries est Karim  |
| Q21 | tableau | oui | - | True | 1.09 | Le local B2 est inspecté le premier lundi de chaque mois [ID:0]. |
| Q22 | fait simple | oui | - | True | 1.12 | Le prix public du Vilaine Compact est de 2 490 € TTC [ID:0]. |
| Q23 | fait simple | oui | - | True | 1.34 | La capacité prévue de l'usine de Saint-Nazaire est de 25 000 vélos par an [ID:0] |
| Q24 | tableau | oui | - | True | 1.71 | Le stock actuel pour la batterie BAT-48V-14Ah est de 1240 unités [ID:0]. Ce stoc |
| Q25 | fait simple | oui | - | True | 1.02 | La durée de garantie pour le cadre est de 7 ans [ID:0]. |
| Q26 | fait simple | oui | - | True | 1.68 | Le numéro de téléphone pour joindre le service après-vente est le 02 40 00 12 34 |
| Q27 | fait simple | oui | - | True | 1.57 | Le montant de la prime d'intéressement pour 2025 est de 1 150 euros par salarié, |
| Q28 | anglais | oui | - | True | 1.17 | Batterix GmbH obtained an overall score of 87 out of 100 during the Supplier Qua |
| Q29 | anglais | oui | - | True | 1.14 | Le taux de défaut des cellules mesuré chez Batterix est de 0,3 % [ID:1]. |
| Q30 | multi-documents | non | - | True | 2.98 | The dataset provides information regarding the average delivery time for compone |
| Q31 | multi-documents | oui | - | True | 1.74 | Batterix a obtenu un score de 87 sur 100 lors de l'audit fournisseur [ID:2]. Le  |
| Q32 | multi-documents | oui | - | True | 1.6 | Vélanor vise un chiffre d'affaires de 55 M€ en 2026 [ID:0][ID:2]. Pour l'usine d |
| Q33 | audio | oui | - | True | 1.18 | La ligne d'assoblage numéro 3 de Nantes sera arrêtée pour maintenance du 2 au 6  |
| Q34 | audio | oui | - | True | 1.01 | Le directeur de production chez Vélanor est Julien Moreau [ID:0]. |
| Q35 | piège | oui | - | - | 0.98 | The answer you are looking for is not found in the dataset! [ID:5] |
| Q36 | piège | oui | - | - | 0.99 | The answer you are looking for is not found in the dataset! [ID:3] |
| Q37 | piège | oui | - | - | 0.96 | The answer you are looking for is not found in the dataset! [ID:3] |
| Q38 | piège | oui | - | - | 0.98 | The answer you are looking for is not found in the dataset! [ID:3] |
