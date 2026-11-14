# AnythingLLM

Interroger ses propres documents, faire travailler un agent et partager le tout avec une équipe, sur sa machine, sans service en ligne.

Ce dépôt contient le service (`service/`, pour lancer AnythingLLM sous Docker), le banc d'essai (`banc-essai/`, 38 questions) et la documentation avec le manuel utilisateur (`documentations/`).

```text
AnythingLLM-Test-Bench/
├── README.md
├── LICENSE
│
├── service/                 lancer AnythingLLM (Docker)
│   ├── installer.sh         première installation
│   ├── demarrer.sh
│   ├── arreter.sh
│   └── …                    état, sauvegarde, réglages
│
├── banc-essai/              rejouer les tests
│   ├── corpus/              9 documents et 38 questions
│   ├── anythingllm/         scripts du banc et des captures propres à AnythingLLM
│   ├── communs/             outils partagés par les cinq bancs
│   ├── exemples/            appels à l'API, avec leurs sorties vérifiées
│   └── resultats/           scores et preuves brutes
│
└── documentations/          lire
    ├── README.md            sommaire du manuel
    ├── manuel/              le guide, chapitre par chapitre
    ├── annexes/             évaluation, matériel, API, exploitation
    ├── img/                 captures d'écran
    ├── index-serie.md       comparaison des cinq solutions
    ├── fiche-technique.md   architecture, réglages, versions, licences
    ├── rapport.md           bilan
    └── journal.md           avancement
```

Les fichiers locaux, ignorés par git, restent à la racine : `donnees/` (volumes et identifiants), `sources/` le cas échéant.

## Lancer le service

Prérequis : Docker, le service de modèles LLM-Service en marche, sa clé dans `service/.env` (copie de `service/.env.example`).

```bash
cd service
./installer.sh     # première fois seulement
./demarrer.sh
./arreter.sh
```

## Rejouer le banc

Le service doit tourner.

```bash
python3 banc-essai/anythingllm/banc.py --etiquette essai --espace Banc-bge-m3
```

## Lire la documentation

| Besoin | Page |
|---|---|
| Utiliser AnythingLLM pas à pas | [Manuel](documentations/README.md) |
| Installer | [Chapitre 02](documentations/manuel/02-installer-anythingllm.md) |
| Résultats détaillés du banc | [Annexe A1](documentations/annexes/A1-evaluation-qualite-et-performances.md) |
| Comparer aux quatre autres solutions | [Index de la série](documentations/index-serie.md) |
| Architecture, réglages, versions, licences | [Fiche technique](documentations/fiche-technique.md) |
| Bilan | [Rapport](documentations/rapport.md) |

## Résultats

Banc de 38 questions (34 avec réponse, 4 pièges), modèles du service central : Qwen3.5-4B avec réflexion, bge-m3, bge-reranker-v2-m3.

| Réglage | OCR | Recherche | Passages | Reranker | Exactes /34 | Pièges refusés /4 | Médiane | Pic RAM de l'application |
|---|---|---|---|---|---|---|---|---|
| défaut | Tesseract | vecteurs | 4 |  | 33 | 3 | 14,3 s | 0,9 Go |
| meilleur | Tesseract | vecteurs | 8 | intégré (MiniLM) | 34 | 4 | 10,7 s | 1,6 Go |

AnythingLLM n'accepte pas le reranker bge-reranker-v2-m3 : seul son reranker intégré est utilisable. Avec son embedder intégré au lieu de bge-m3, le score tombe à 25/34.

Toutes les variantes : [annexe A1](documentations/annexes/A1-evaluation-qualite-et-performances.md). Méthode et preuves : [annexe A6](documentations/annexes/A6-rapport-d-essais.md). Bilan : [documentations/rapport.md](documentations/rapport.md). Comparaison avec les quatre autres solutions : [index de la série](documentations/index-serie.md).
