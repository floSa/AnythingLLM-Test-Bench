# Banc ragflow — hybride-vecteurs07-top8 — 2026-11-09T18:12:52

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
| latence_p50_s | 1.36 |
| latence_p95_s | 1.83 |
| par_type | {'tableau': '10/10', 'fait simple': '13/13', 'scan': '4/4', 'anglais': '2/2', 'multi-documents': '3/3', 'audio': '2/2', 'piège': '4/4'} |
| pic_ram_mo | {'rag-ragflow-server': 1625, 'rag-ragflow-es01': 2760, 'rag-ragflow-mysql': 531, 'rag-ragflow-minio': 93, 'rag-ragflow-kvrocks': 24, 'rag-ragflow-nats': 8, 'vllm-central': 6647, 'vllm-embed': 4172, 'rag-speaches': 897} |
| pic_ram_application_mo | 5041 |
| vram | 15254 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | None |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | - | True | 1.96 | Le chiffre d'affaires de Vélanor pour l'exercice 2025 s'est établi à 48,6 M€ [ID |
| Q02 | fait simple | oui | - | True | 1.21 | Vélanor a été fondée en 2014 [ID:0]. |
| Q03 | fait simple | oui | - | True | 1.31 | La présidente de Vélanor est Hélène Marchais, et elle dirige l'entreprise depuis |
| Q04 | fait simple | oui | - | True | 1.13 | Le siège de Vélanor est situé au 12 quai de la Fosse, à Nantes [ID:0]. |
| Q05 | tableau | oui | - | True | 1.39 | Vélanor comptait 412 salariés au 31 décembre 2025 [ID:4][ID:3]. |
| Q06 | tableau | oui | - | True | 1.61 | Le chiffre d'affaires pour le troisième trimestre (T3) 2025 s'est établi à 14,2  |
| Q07 | tableau | oui | - | True | 1.37 | Le modèle Sèvre Trail a produit 15 400 unités en 2025 [ID:0]. |
| Q08 | tableau | oui | - | True | 1.32 | Le prix public TTC du modèle Erdre Cargo est de 4 290 € [ID:0]. |
| Q09 | tableau | oui | - | True | 1.37 | Il y a 97 salariés travaillant sur le site de Cholet, où se déroule la fabricati |
| Q10 | fait simple | oui | - | True | 1.34 | Les cadres sont fabriqués à partir d'aluminium recyclé à 82 % [ID:0]. |
| Q11 | fait simple | oui | - | True | 1.53 | Le taux de recyclage des batteries usagées collectées atteint 96 %, grâce au par |
| Q12 | tableau | oui | - | True | 1.48 | Le fournisseur qui livre les moteurs est Motodrive Co., et il est installé au Ta |
| Q13 | tableau | oui | - | True | 1.21 | Vélanor a dégagé un résultat net de 3,1 M€ en 2025 [ID:3]. |
| Q14 | fait simple | oui | - | True | 1.35 | Le taux de retour sous garantie s'établit à 1,8 % des vélos vendus [ID:0]. |
| Q15 | scan | oui | - | True | 1.53 | Le prix unitaire des batteries prévu dans le contrat avec Batterix est de 212 eu |
| Q16 | scan | oui | - | True | 1.38 | Le fournisseur livre sous 21 jours après la commande dans le cadre du contrat d' |
| Q17 | scan | oui | - | True | 1.37 | Le plafond des pénalités de retard dans le contrat avec Batterix est fixé à 8 %  |
| Q18 | scan | oui | - | True | 1.35 | Le volume minimal annuel de batteries prévu dans le contrat avec Batterix est de |
| Q19 | fait simple | oui | - | True | 1.56 | Les batteries doivent être stockées entre 10 °C et 25 °C, dans le local B2 équip |
| Q20 | fait simple | oui | - | True | 1.37 | Karim Benali, responsable HSE, est le responsable de la procédure de charge et d |
| Q21 | tableau | oui | - | True | 1.14 | Le local B2 est inspecté le premier lundi de chaque mois [ID:0]. |
| Q22 | fait simple | oui | - | True | 1.23 | Le prix public du Vilaine Compact est de 2 490 € TTC [ID:0]. |
| Q23 | fait simple | oui | - | True | 1.36 | L'usine de Saint-Nazaire a une capacité prévue de 25 000 vélos par an [ID:0]. |
| Q24 | tableau | oui | - | True | 1.66 | Il reste 1240 unités de la référence BAT-48V-14Ah, ce qui est en dessous du seui |
| Q25 | fait simple | oui | - | True | 1.15 | Le cadre est garanti 7 ans [ID:0]. |
| Q26 | fait simple | oui | - | True | 1.67 | Le service après-vente peut être joint par téléphone au 02 40 00 12 34, du lundi |
| Q27 | fait simple | oui | - | True | 1.65 | La prime d'intéressement 2025 est de 1 150 euros par salarié, et elle sera versé |
| Q28 | anglais | oui | - | True | 1.18 | The overall score Batterix obtained at the supplier audit was 87 out of 100 [ID: |
| Q29 | anglais | oui | - | True | 1.31 | Le taux de défaut des cellules mesuré est de 0,3 % [ID:0]. |
| Q30 | multi-documents | oui | - | True | 1.74 | Le délai de livraison contractuel de Batterix GmbH est de 21 jours après la comm |
| Q31 | multi-documents | oui | - | True | 1.83 | Batterix a obtenu un score de 87 sur 100 lors de l'audit du fournisseur [ID:1].  |
| Q32 | multi-documents | oui | - | True | 2.05 | Vélanor vise un chiffre d'affaires de 55 M€ en 2026 [ID:0][ID:4][ID:4]. De plus, |
| Q33 | audio | oui | - | True | 1.42 | La ligne d'assoblage numéro 3 de Nantes sera arrêtée pour maintenance [ID:0] du  |
| Q34 | audio | oui | - | True | 1.19 | Julien Moreau est le directeur de production chez Vélanor [ID:1]. |
| Q35 | piège | oui | - | - | 1.12 | The answer you are looking for is not found in the dataset! [ID:5] |
| Q36 | piège | oui | - | - | 1.09 | The answer you are looking for is not found in the dataset! [ID:4] |
| Q37 | piège | oui | - | - | 1.1 | The answer you are looking for is not found in the dataset! [ID:4] |
| Q38 | piège | oui | - | - | 1.08 | The answer you are looking for is not found in the dataset! [ID:4] |
