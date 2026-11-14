# Banc ragflow — hybride-vecteurs07-top8-reranker — 2026-11-12T08:54:24

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
| latence_p50_s | 8.78 |
| latence_p95_s | 55.04 |
| par_type | {'tableau': '10/10', 'fait simple': '13/13', 'scan': '4/4', 'anglais': '2/2', 'multi-documents': '3/3', 'audio': '2/2', 'piège': '4/4'} |
| pic_ram_mo | {'rag-ragflow-server': 1425, 'rag-ragflow-es01': 2851, 'rag-ragflow-mysql': 554, 'rag-ragflow-minio': 160, 'rag-ragflow-kvrocks': 55, 'rag-ragflow-nats': 27, 'llm-central': 694, 'llm-swap': 6630, 'llm-speaches': 1378} |
| pic_ram_application_mo | 5072 |
| vram | 8440 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | None |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | - | True | 12.55 | Le chiffre d'affaires de Vélanor en 2025 s'élève à **48,6 millions d'euros** [+1 |
| Q02 | fait simple | oui | - | True | 6.6 | Vélanor a été fondée en **2014**.   Cette information provient du rapport annuel |
| Q03 | fait simple | oui | - | True | 52.82 | D'après les documents disponibles dans la base de connaissances, plusieurs sourc |
| Q04 | fait simple | oui | - | True | 5.84 | L'adresse du siège de Vélanor est située au 12 quai de la Fosse à Nantes. Cet ét |
| Q05 | tableau | oui | - | True | 9.13 | Vélanor compte **412 salariés** au 31 décembre 2025.  Cette information est conf |
| Q06 | tableau | oui | - | True | 55.04 | D'après le rapport annuel 2025, le chiffre d'affaires du troisième trimestre a é |
| Q07 | tableau | oui | - | True | 8.98 | En 2025, **15 400 unités** du modèle Sèvre Trail ont été produites par Vélanor.  |
| Q08 | tableau | oui | - | True | 5.11 | Le prix public TTC du modèle Erdre Cargo s'établit à **4 290 €**. [ID:0]  Ce mod |
| Q09 | tableau | oui | - | True | 5.55 | Selon les informations contenues dans le document du rapport annuel 2025, il y a |
| Q10 | fait simple | oui | - | True | 5.25 | La part d'aluminium recyclé dans les cadres de Vélanor est de **82 %**.  Cette i |
| Q11 | fait simple | oui | - | True | 18.29 | Selon le rapport annuel 2025 publié par Vélanor, le taux de recyclage des batter |
| Q12 | tableau | oui | - | True | 43.48 | Le fournisseur qui livre les moteurs est Motodrive Co., installé à Taïwan [ID:0] |
| Q13 | tableau | oui | - | True | 5.74 | Vélanor a dégagé un résultat net de **3,1 M€** en 2025 [ID:1]. Cela représente u |
| Q14 | fait simple | oui | - | True | 5.85 | Le taux de retour sous garantie est de 1,8 % des vélos vendus [ID:0]. |
| Q15 | scan | oui | - | True | 9.66 | Le prix unitaire des batteries prévu par le contrat avec Batterix est de **212 e |
| Q16 | scan | oui | - | True | 8.92 | Le délai de livraison prévu par le contrat Batterix est fixé à **21 jours** aprè |
| Q17 | scan | oui | - | True | 60.59 | Le plafond des pénalités de retard est fixé à 8% du montant de la commande. [ID: |
| Q18 | scan | oui | - | True | 8.7 | Le contrat d'approvisionnement avec Batterix prévoit un volume minimal annuel de |
| Q19 | fait simple | oui | - | True | 4.53 | Les batteries doivent être stockées entre **10 °C et 25 °C**, dans le local B2 é |
| Q20 | fait simple | oui | - | True | 7.09 | Karim Benali est le responsable de la procédure de charge et de stockage des bat |
| Q21 | tableau | oui | - | True | 5.2 | Le local B2 est inspecté **le premier lundi de chaque mois** [ID:0]. Cette inspe |
| Q22 | fait simple | oui | - | True | 5.71 | Le prix public du modèle Vilaine Compact est de **2 490 € TTC** [ID:0].  Ce vélo |
| Q23 | fait simple | oui | - | True | 71.66 | Voici les données extraites des documents concernant l'usine de Saint-Nazaire :  |
| Q24 | tableau | oui | - | True | 8.58 | Le stock de batteries BAT-48V-14Ah reste à **1 240 unités** selon les données du |
| Q25 | fait simple | oui | - | True | 7.18 | Selon la FAQ du service après-vente disponible dans les documents fournis :  **L |
| Q26 | fait simple | oui | - | True | 5.33 | Le numéro de téléphone du service après-vente est le 02 40 00 12 34 [ID:0]. Vous |
| Q27 | fait simple | oui | - | True | 8.78 | Le montant de la prime d'intéressement 2025 est fixé à **1 150 euros par salarié |
| Q28 | anglais | oui | - | True | 4.36 | Based on the provided knowledge base, I found the audit results for Batterix Gmb |
| Q29 | anglais | oui | - | True | 4.29 | Le taux de cellules défectueuses mesuré chez Batterix lors de l'audit est de 0,3 |
| Q30 | multi-documents | oui | - | True | 9.11 | Selon les documents fournis, voici les délais concernant Batterix GmbH :  **Déla |
| Q31 | multi-documents | oui | - | True | 12.58 | Selon les documents fournis :  **Score de l'audit :** Batterix GmbH a obtenu un  |
| Q32 | multi-documents | oui | - | True | 9.74 | Vélanor vise un chiffre d'affaires de **55 M€ en 2026** [ID:0]. Cette prévision  |
| Q33 | audio | oui | - | True | 12.08 | Based on the dataset content:  **Réponse :** La ligne d'assemblage numéro 3 de N |
| Q34 | audio | oui | - | True | 16.51 | Selon le contenu du fichier « message-vocal-production.mp3 », Julien Moreau est  |
| Q35 | piège | oui | - | - | 8.16 | Le chiffre d'affaires de Vélanor en 2022 n'est pas trouvé dans les documents du  |
| Q36 | piège | oui | - | - | 9.94 | Je n'ai pas trouvé d'information sur le directeur financier de Vélanor dans les  |
| Q37 | piège | oui | - | - | 15.48 | Looking at the provided knowledge base, I found information about Vélanor SAS's  |
| Q38 | piège | oui | - | - | 9.47 | Je ne trouve pas d'information sur le salaire de Karim Benali dans les documents |
