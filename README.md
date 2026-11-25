<<<<<<< HEAD
# MAINTiDOC — Équipe RAKBA SAAD / EL QUAMMAH AMINE

## Projet

Assistant documentaire multimodal et agentique pour la maintenance des motos.

## Équipe

- RAKBA SAAD
- EL QUAMMAH AMINE

## Contenu du dépôt

- `L1_MaintiDoc_RAKBA-SAAD_EL-QUAMMAH-AMINE_Rapport.pdf` : rapport nominatif de 13 pages.
- `L1_MaintiDoc_RAKBA-SAAD_EL-QUAMMAH-AMINE_LienGitHub.txt` : emplacement du lien GitHub.
- `L1_MaintiDoc_RAKBA-SAAD_EL-QUAMMAH-AMINE_Corpus/inventaire.csv` : inventaire des 45 documents.
- `L1_MaintiDoc_RAKBA-SAAD_EL-QUAMMAH-AMINE_Corpus/prompts_corpus.md` : prompts et règles d’annotation.
- `L1_MaintiDoc_RAKBA-SAAD_EL-QUAMMAH-AMINE_Corpus/documents/famille_1/` : 22 PDF pneus.
- `L1_MaintiDoc_RAKBA-SAAD_EL-QUAMMAH-AMINE_Corpus/documents/famille_2/` : 23 PDF chaînes.
- `L1_MaintiDoc_RAKBA-SAAD_EL-QUAMMAH-AMINE_Corpus/images/` : images sources et registre.
- `L1_MaintiDoc_RAKBA-SAAD_EL-QUAMMAH-AMINE_Corpus/RAG/` : extraction, embeddings CLIP, index ChromaDB, manifest et évaluation.

## Pipeline RAG appliqué

Le pipeline suit le notebook fourni : extraction PyMuPDF page par page, extraction des images intégrées, rendu visuel des pages, embeddings CLIP `ViT-B-32 / laion2b_s34b_b79k` normalisés sur 512 dimensions, puis indexation persistante dans trois collections ChromaDB : texte, page visuelle et image extraite.

Le dossier `RAG/` contient 135 fragments texte, 135 pages visuelles, 366 images extraites, les vecteurs et manifest, les tests de récupération et le rapport de qualité RAG. Chaque résultat conserve son `document_id`, sa page, sa famille et son chemin source.

## Contrôles et limites

Chaque PDF spécialisé est au format A4 et contient exactement trois pages. Les tests de récupération ont obtenu la bonne famille en première position pour 5 requêtes représentatives. La précision moyenne de famille dans les cinq premiers résultats est conservée dans `RAG/retrieval_evaluation.csv`.

Les images TyreNet doivent encore être filtrées par type de véhicule avant redistribution finale, car le dataset comprend aussi des pneus automobiles. Une réponse de production doit citer le document et la page, distinguer observation et hypothèse et rappeler qu’une image ne confirme pas seule un défaut interne ou une tolérance mécanique.

## Arborescence RAG unifiée

Le dossier `Corpus/RAG/` suit une structure portable en dix niveaux : `00_config`, `01_sources`, `02_ingestion`, `03_chunks`, `04_embeddings`, `05_vector_store`, `06_evaluation`, `07_reports`, `08_scripts`, `09_notebooks` et `10_logs`. Les chemins sont relatifs et fonctionnent sous Windows, Linux et macOS. Le détail est dans `Corpus/RAG/ARBORESCENCE.md`.
=======
# MAINTiDOC-RAG
>>>>>>> 7e4b3f4b5b1c95add07b76f09f95a93c3225f09e
