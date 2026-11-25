# RAG_UNIFIED — Arborescence RAG portable

Cette arborescence est indépendante du système d’exploitation. Les chemins sont relatifs ; aucun chemin `/home/ubuntu` ou `C:\Users\...` n’est requis.

## Organisation

- `00_config/` : paramètres, chemins relatifs et dépendances.
- `01_sources/` : points d’entrée des documents et registre des images sources.
- `02_ingestion/` : textes extraits, images extraites et pages rendues.
- `03_chunks/` : unités documentaires sans vecteurs.
- `04_embeddings/` : vecteurs CLIP texte/image séparés.
- `05_vector_store/` : base ChromaDB persistante.
- `06_evaluation/` : manifest, tests de recherche et évaluation.
- `07_reports/` : rapport qualité RAG et synthèses.
- `08_scripts/` : scripts portables.
- `09_notebooks/` : notebooks d’expérimentation.
- `10_logs/` : journaux d’exécution.

Les dossiers vides sont conservés volontairement pour rendre l’architecture complète et faciliter les prochaines étapes du projet.
