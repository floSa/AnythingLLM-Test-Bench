# Banc ragflow — defaut — 2026-11-12T08:20:11

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
| latence_p50_s | 7.8 |
| latence_p95_s | 50.03 |
| par_type | {'tableau': '10/10', 'fait simple': '13/13', 'scan': '4/4', 'anglais': '2/2', 'multi-documents': '2/3', 'audio': '2/2', 'piège': '4/4'} |
| pic_ram_mo | {'rag-ragflow-server': 1765, 'rag-ragflow-es01': 2861, 'rag-ragflow-mysql': 547, 'rag-ragflow-minio': 159, 'rag-ragflow-kvrocks': 53, 'rag-ragflow-nats': 22, 'llm-central': 699, 'llm-swap': 6511, 'llm-speaches': 1452} |
| pic_ram_application_mo | 5407 |
| vram | 8238 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | 64.0 |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | - | True | 8.5 | Le chiffre d'affaires de Vélanor en 2025 s'élève à **48,6 M€**. [ID:1][ID:3] Cet |
| Q02 | fait simple | oui | - | True | 50.03 | Voici les données pertinentes extraites du dataset concernant la fondation de l' |
| Q03 | fait simple | oui | - | True | 50.29 | La présidente de Vélanor est Hélène Marchais [ID:0]. Elle dirige l'entreprise de |
| Q04 | fait simple | oui | - | True | 6.12 | L'adresse du siège de Vélanor est située au 12 quai de la Fosse, à Nantes [ID:0] |
| Q05 | tableau | oui | - | True | 8.84 | Vélanor compte **412 salariés** au 31 décembre 2025. Cette information apparaît  |
| Q06 | tableau | oui | - | True | 6.34 | Le chiffre d'affaires du troisième trimestre de l'année 2025 a été de **14,2 M€* |
| Q07 | tableau | oui | - | True | 48.37 | En 2025, **15 400 unités** du modèle Sèvre Trail ont été produites par l'entrepr |
| Q08 | tableau | oui | - | True | 5.5 | Selon le rapport annuel 2025 de Vélanor SAS, le prix public du modèle **Erdre Ca |
| Q09 | tableau | oui | - | True | 6.04 | Le site de **Cholet** compte **97 salariés** au 31 décembre 2025, qui y travaill |
| Q10 | fait simple | oui | - | True | 6.96 | Selon le document, les cadres sont fabriqués à partir d'aluminium recyclé à 82 % |
| Q11 | fait simple | oui | - | True | 43.62 | Selon le rapport annuel 2025, le taux de recyclage des batteries usagées collect |
| Q12 | tableau | oui | - | True | 4.41 | Le fournisseur qui livre les moteurs est **Motodrive Co.**, et il est installé e |
| Q13 | tableau | oui | - | True | 5.86 | Vélanor a dégagé un résultat net de 3,1 M€ en 2025 [ID:2]. Cela représente une a |
| Q14 | fait simple | oui | - | True | 9.01 | Selon les documents du rapport annuel 2025, le taux de retour sous garantie s'ét |
| Q15 | scan | oui | - | True | 5.66 | Selon le contrat d'approvisionnement avec Batterix, le prix unitaire des batteri |
| Q16 | scan | oui | - | True | 10.74 | Based on the provided dataset, I found relevant information in the Batterix supp |
| Q17 | scan | oui | - | True | 36.01 | Le contrat d'approvisionnement avec Batterix spécifie un plafond de pénalités po |
| Q18 | scan | oui | - | True | 10.94 | Le volume minimal annuel prévu par le contrat Batterix est de **40 000 batteries |
| Q19 | fait simple | oui | - | True | 5.33 | Selon la procédure de stockage des batteries, les batteries doivent être stockée |
| Q20 | fait simple | oui | - | True | 3.99 | La procédure de charge et de stockage des batteries est assurée par **Karim Bena |
| Q21 | tableau | oui | - | True | 46.36 | Selon le document procedure-batteries.docx, la fréquence de l'inspection du loca |
| Q22 | fait simple | oui | - | True | 7.03 | Le prix du Vilaine Compact est de **2 490 € TTC** selon les documents disponible |
| Q23 | fait simple | oui | - | True | 88.25 | D'après les documents fournis, la capacité prévue de l'usine de Saint-Nazaire es |
| Q24 | tableau | oui | - | True | 8.12 | Il reste **1240 unités** de batteries BAT-48V-14Ah (référence exacte : Batterie  |
| Q25 | fait simple | oui | - | True | 5.21 | La durée de garantie du cadre est de **7 ans**. Cette information provient du do |
| Q26 | fait simple | oui | - | True | 5.36 | Le numéro de téléphone du service après-vente est le **02 40 00 12 34** [ID:0].  |
| Q27 | fait simple | oui | - | True | 4.46 | Selon les décisions documentées, le montant de la prime d'intéressement 2025 est |
| Q28 | anglais | oui | - | True | 4.31 | Batterix obtained an overall score of 87 out of 100 at the supplier audit conduc |
| Q29 | anglais | oui | - | True | 3.67 | Selon l'audit qualité du fournisseur Batterix GmbH à Bremen, le taux de cellules |
| Q30 | multi-documents | non | - | True | 12.84 | # Réponse sur les délais de livraison de Batterix GmbH  ## Délai moyen réellemen |
| Q31 | multi-documents | oui | - | True | 6.42 | Batterix a obtenu un score de **87 sur 100** à l'audit de qualité, ce qui lui a  |
| Q32 | multi-documents | oui | - | True | 7.8 | Vélanor vise un chiffre d'affaires de 55 M€ en 2026 [ID:0][ID:2]. La société pré |
| Q33 | audio | oui | - | True | 12.53 | Voici la réponse basée sur les données du dataset :  ## Information trouvée dans |
| Q34 | audio | oui | - | True | 36.72 | D'après les documents disponibles, **Julien Moreau** est le responsable de la pr |
| Q35 | piège | oui | - | - | 13.36 | Le chiffre d'affaires de Vélanor en 2022 n'est pas mentionné dans les documents  |
| Q36 | piège | oui | - | - | 32.14 | Après avoir examiné les documents fournis concernant Vélanor SAS, aucun nom de d |
| Q37 | piège | oui | - | - | 13.44 | Based on the provided knowledge base, I've searched through all the documents to |
| Q38 | piège | oui | - | - | 6.67 | D'après les documents disponibles dans la base de connaissances, il n'y a **aucu |
