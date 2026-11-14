# Banc ragflow — agentic — 2026-11-09T18:10:07

| Mesure | Valeur |
|---|---|
| questions | 38 |
| exactes | 30 |
| sur | 34 |
| refus_corrects | 4 |
| pieges | 4 |
| citation_bon_document | 29 |
| citation_bonne_page | 21 |
| citations_avec_page | 21 |
| juge_llm_oui | 0 |
| juge_llm_sur | 0 |
| erreurs | 0 |
| latence_p50_s | 4.52 |
| latence_p95_s | 7.22 |
| par_type | {'tableau': '8/10', 'fait simple': '11/13', 'scan': '4/4', 'anglais': '2/2', 'multi-documents': '3/3', 'audio': '2/2', 'piège': '4/4'} |
| pic_ram_mo | {'rag-ragflow-server': 1903, 'rag-ragflow-es01': 2760, 'rag-ragflow-mysql': 532, 'rag-ragflow-minio': 103, 'rag-ragflow-kvrocks': 24, 'rag-ragflow-nats': 9, 'vllm-central': 6648, 'vllm-embed': 4173, 'rag-speaches': 1585} |
| pic_ram_application_mo | 5331 |
| vram | 15250 Mo / 16380 Mo (nvidia-smi, mesuré en fin de banc) |
| indexation_s | None |

| Id | Type | Exacte | Juge LLM | Doc. cité | Latence (s) | Réponse (début) |
|---|---|---|---|---|---|---|
| Q01 | tableau | oui | - | True | 8.85 | <think>Le chiffre d'affaires de Vélanor pour l'année 2025 s'établit à 48,6 M€ [I |
| Q02 | fait simple | oui | - | True | 6.46 | <think>Vélanor a été fondée en 2014 à Nantes [ID:0].The user is asking for the f |
| Q03 | fait simple | oui | - | True | 8.51 | <think>The user is asking for the president of "Vélanor" in French. The initial  |
| Q04 | fait simple | oui | - | True | 4.24 | <think>L'adresse du siège de Vélanor est située au 12 quai de la Fosse, à Nantes |
| Q05 | tableau | oui | - | True | 6.03 | <think>Vélanor comptait un total de 412 salariés au 31 décembre 2025, selon le r |
| Q06 | tableau | non | - | False | 1.2 | <think>Je n'ai pas accès à des informations sur les résultats financiers futurs, |
| Q07 | tableau | non | - | False | 0.6 | <think>Je ne dispose pas d'informations dans mon corpus concernant la production |
| Q08 | tableau | oui | - | True | 1.85 | <think>Le prix public du modèle Erdre Cargo est de 4 290 € TTC [ID:0].</think>   |
| Q09 | tableau | oui | - | True | 4.52 | <think>Le site de Cholet emploie 97 salariés pour l'activité de fabrication des  |
| Q10 | fait simple | oui | - | True | 4.26 | <think>Les cadres sont fabriqués à partir d'aluminium recyclé à 82 % [ID:0].</th |
| Q11 | fait simple | oui | - | True | 4.97 | <think>Le taux de recyclage des batteries usagées collectées atteint 96 %, grâce |
| Q12 | tableau | oui | - | True | 4.07 | <think>Le fournisseur qui livre les moteurs est Motodrive Co., et il est install |
| Q13 | tableau | oui | - | True | 5.43 | <think>Le résultat net dégagé par Vélanor en 2025 s'est établi à 3,1 M€, ce qui  |
| Q14 | fait simple | oui | - | True | 4.13 | <think>Le taux de retour sous garantie s'établit à 1,8 % des vélos vendus pour l |
| Q15 | scan | oui | - | True | 4.95 | <think>Le prix unitaire des batteries, référence BAT-48V-14Ah, prévue dans le co |
| Q16 | scan | oui | - | True | 4.65 | <think>Le fournisseur, Batterix, livre sous 21 jours après la commande, selon l' |
| Q17 | scan | oui | - | True | 4.68 | <think>Le plafond des pénalités de retard du contrat Batterix est fixé à 8% du m |
| Q18 | scan | oui | - | True | 4.46 | <think>Le contrat d'approvisionnement entre Velanor SAS et Batterix GmbH prévoit |
| Q19 | fait simple | oui | - | True | 5.13 | <think>Les batteries doivent être stockées entre 10 °C et 25 °C, dans le local B |
| Q20 | fait simple | oui | - | True | 4.52 | <think>La procédure de charge et de stockage des batteries est sous la responsab |
| Q21 | tableau | oui | - | True | 4.19 | <think>Le local B2 est inspecté le premier lundi de chaque mois, et cette inspec |
| Q22 | fait simple | oui | - | True | 1.89 | <think>Le prix public du Vilaine Compact, un vélo pliant électrique lancé en avr |
| Q23 | fait simple | oui | - | True | 4.63 | <think>L'usine de Saint-Nazaire, qui ouvrira en septembre 2026, aura une capacit |
| Q24 | tableau | oui | - | False | 5.84 | <think>Le stock de batteries BAT-48V-14Ah est de 1240 unités, et le seuil d'aler |
| Q25 | fait simple | oui | - | True | 2.91 | <think>Le cadre est garanti pendant 7 ans [ID:0]. Cependant, la batterie et le m |
| Q26 | fait simple | non | - | False | 0.95 | <think>Je suis désolé, mais je n'ai accès à aucun document ou base de données co |
| Q27 | fait simple | non | - | False | 0.97 | <think>Je n'ai pas trouvé d'informations dans ma base de données concernant le m |
| Q28 | anglais | oui | - | True | 1.77 | <think>The overall score Batterix obtained at the supplier audit was 87 out of 1 |
| Q29 | anglais | oui | - | True | 4.22 | <think>The taux de cellules défectueuses mesuré chez Batterix lors de l'audit ét |
| Q30 | multi-documents | oui | - | True | 5.62 | <think>Le délai de livraison contractuel de Batterix est de 21 jours après la co |
| Q31 | multi-documents | oui | - | True | 5.88 | <think>Le score de l'audit de Batterix n'est pas présent dans le contrat d'appro |
| Q32 | multi-documents | oui | - | True | 5.7 | <think>Vélanor vise un chiffre d'affaires de 55 millions d'euros en 2026 [ID:0]. |
| Q33 | audio | oui | - | True | 4.9 | <think>La ligne d'assemblage numéro 3 de Nantes sera arrêtée pour maintenance du |
| Q34 | audio | oui | - | True | 3.98 | <think>Julien Moreau est le directeur de production chez Vélanor [ID:0].</think> |
| Q35 | piège | oui | - | - | 7.22 | <think>Le corpus consulté concerne le rapport annuel de Vélanor pour l'année 202 |
| Q36 | piège | oui | - | - | 4.08 | <think>Le directeur de production de Vélanor est Julien Moreau, selon un message |
| Q37 | piège | oui | - | - | 0.63 | <think>Je n'ai trouvé aucune information sur les ventes de trottinettes électriq |
| Q38 | piège | oui | - | - | 5.23 | <think>Les documents consultés mentionnent Karim Benali dans le cadre de ses fon |
