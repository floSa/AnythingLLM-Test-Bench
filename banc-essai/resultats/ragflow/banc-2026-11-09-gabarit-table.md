# Banc ragflow — gabarit-table — 2026-11-09T18:17:18

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
| latence_p50_s | 1.26 |
| latence_p95_s | 2.16 |
| par_type | {'tableau': '10/10', 'fait simple': '13/13', 'scan': '4/4', 'anglais': '2/2', 'multi-documents': '2/3', 'audio': '2/2', 'piège': '4/4'} |
| pic_ram_mo | {'rag-ragflow-server': 2185, 'rag-ragflow-es01': 2779, 'rag-ragflow-mysql': 537, 'rag-ragflow-minio': 109, 'rag-ragflow-kvrocks': 27, 'rag-ragflow-nats': 9, 'vllm-central': 6646, 'vllm-embed': 4171, 'rag-speaches': 1480} |
| pic_ram_application_mo | 5646 |
| vram | 15241 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | 53.0 |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | - | True | 2.3 | Le chiffre d'affaires de Vélanor en 2025 s'établit à 48,6 M€ [ID:1]. Ce total re |
| Q02 | fait simple | oui | - | True | 1.11 | Vélanor a été fondée en 2014 à Nantes [ID:0]. |
| Q03 | fait simple | oui | - | True | 1.19 | La présidente de Vélanor est Hélène Marchais, qui dirige l'entreprise depuis 201 |
| Q04 | fait simple | oui | - | True | 1.15 | Le siège de Vélanor est situé au 12 quai de la Fosse, à Nantes [ID:0]. |
| Q05 | tableau | oui | - | True | 4.04 | Vélanor comptait 412 salariés au 31/12/2025 [ID:0][ID:3].  Voici une répartition |
| Q06 | tableau | oui | - | True | 1.78 | Le chiffre d'affaires du troisième trimestre (T3) 2025 a été de 14,2 M€ [ID:0].  |
| Q07 | tableau | oui | - | True | 1.26 | Le modèle Sèvre Trail a produit 15 400 unités en 2025 [ID:0]. |
| Q08 | tableau | oui | - | True | 1.14 | Le prix public TTC du modèle Erdre Cargo est de 4 290 € [ID:0]. |
| Q09 | tableau | oui | - | True | 1.26 | Il y a 97 salariés qui travaillent sur le site de Cholet, où se situe la fabrica |
| Q10 | fait simple | oui | - | True | 1.18 | Les cadres sont fabriqués à partir d'aluminium recyclé à 82 % [ID:0]. |
| Q11 | fait simple | oui | - | True | 1.39 | Le taux de recyclage des batteries usagées collectées atteint 96 % grâce au part |
| Q12 | tableau | oui | - | True | 1.37 | Le fournisseur qui livre les moteurs est Motodrive Co. [ID:2][ID:1], et il est i |
| Q13 | tableau | oui | - | True | 1.2 | Vélanor a dégagé un résultat net de 3,1 M€ en 2025 [ID:2]. |
| Q14 | fait simple | oui | - | True | 1.31 | Le taux de retour sous garantie s'établit à 1,8 % des vélos vendus [ID:0]. |
| Q15 | scan | oui | - | True | 1.71 | Le prix unitaire pour la fourniture de batteries 48V 14 Ah, référence BAT-48V-14 |
| Q16 | scan | oui | - | True | 1.23 | Le Fournisseur livre sous 21 jours après la commande dans le cadre du contrat d' |
| Q17 | scan | oui | - | True | 1.19 | Le plafond des pénalités de retard est fixé à 8% du montant de la commande [ID:0 |
| Q18 | scan | oui | - | True | 1.27 | Le volume minimal annuel de batteries prévu par le contrat avec Batterix est de  |
| Q19 | fait simple | oui | - | True | 1.45 | Les batteries doivent être stockées entre 10 °C et 25 °C, dans le local B2 qui e |
| Q20 | fait simple | oui | - | True | 1.35 | Karim Benali, responsable HSE, est le responsable de la procédure PR-SEC-04 conc |
| Q21 | tableau | oui | - | True | 1.09 | Le local B2 est inspecté le premier lundi de chaque mois [ID:0]. |
| Q22 | fait simple | oui | - | True | 1.13 | Le prix public du Vilaine Compact est de 2 490 € TTC [ID:0]. |
| Q23 | fait simple | oui | - | True | 1.3 | La capacité prévue pour l'usine de Saint-Nazaire est de 25 000 vélos par an [ID: |
| Q24 | tableau | oui | - | True | 2.16 | Le stock restant pour la référence BAT-48V-14Ah est de 1240 unités [ID:0], et le |
| Q25 | fait simple | oui | - | True | 0.95 | Le cadre est garanti 7 ans [ID:0]. |
| Q26 | fait simple | oui | - | True | 1.67 | Le service après-vente peut être joint par téléphone au 02 40 00 12 34, du lundi |
| Q27 | fait simple | oui | - | True | 1.58 | La prime d'intéressement pour 2025 est de 1 150 euros par salarié, et elle sera  |
| Q28 | anglais | oui | - | True | 1.17 | Batterix GmbH obtained an overall score of 87 out of 100 during the Supplier Qua |
| Q29 | anglais | oui | - | True | 1.12 | Le taux de défaut des cellules mesuré est de 0,3 % [ID:0]. |
| Q30 | multi-documents | non | - | True | 1.35 | Le délai de livraison contractuel n'est pas spécifié dans les documents, mais le |
| Q31 | multi-documents | oui | - | True | 1.69 | Batterix a obtenu un score global de 87 sur 100 lors de l'audit de fournisseur [ |
| Q32 | multi-documents | oui | - | True | 1.94 | Vélanor vise un chiffre d'affaires de 55 M€ en 2026 [ID:0][ID:2]. De plus, une s |
| Q33 | audio | oui | - | True | 1.3 | La ligne d'assoblage numéro 3 de Nantes sera arrêtée pour maintenance du 2 au 6  |
| Q34 | audio | oui | - | True | 1.04 | Le directeur de production chez Vélanor est Julien Moreau [ID:1]. |
| Q35 | piège | oui | - | - | 1.03 | The answer you are looking for is not found in the dataset! [ID:5] |
| Q36 | piège | oui | - | - | 0.43 | The answer you are looking for is not found in the dataset! [ID:2] |
| Q37 | piège | oui | - | - | 1.04 | The answer you are looking for is not found in the dataset! [ID:2] |
| Q38 | piège | oui | - | - | 1.0 | The answer you are looking for is not found in the dataset! [ID:2] |
