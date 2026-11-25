# Arborescence RAG unifiée et portable

```text
RAG/
├── 00_config/
│   ├── paths.json
│   ├── settings.json
│   └── requirements_rag.txt
├── 01_sources/
│   ├── documents/
│   │   ├── famille_1/       # point d’entrée optionnel ; sources canoniques dans ../documents/
│   │   └── famille_2/
│   ├── images/              # registre des images sources
│   └── README.md
├── 02_ingestion/
│   ├── textes/              # texte par document et par page
│   ├── images_extraites/    # images intégrées extraites des PDF
│   └── pages_rendues/       # rendu complet des pages pour le multimodal
├── 03_chunks/               # unités documentaires sans vecteurs
│   ├── text_chunks.jsonl
│   ├── page_visual_chunks.jsonl
│   └── image_chunks.jsonl
├── 04_embeddings/           # vecteurs CLIP normalisés, dimension 512
│   ├── text_embeddings.jsonl
│   ├── page_visual_embeddings.jsonl
│   └── image_embeddings.jsonl
├── 05_vector_store/
│   └── chroma/              # index persistant ChromaDB
├── 06_evaluation/
│   ├── documents_manifest.csv
│   ├── manifest.json
│   ├── retrieval_evaluation.csv
│   └── retrieval_smoke_tests.json
├── 07_reports/
│   ├── RAG_quality_report.md
│   ├── RAG_quality_report.pdf
│   └── quality_summary.md
├── 08_scripts/
│   └── run_rag_pipeline.py  # chemins relatifs, portable Windows/Linux/macOS
├── 09_notebooks/            # notebooks d’expérimentation, dossier extensible
├── 10_logs/                 # journaux d’exécution, dossier extensible
├── ARBORESCENCE.md
└── README.md
```

Les dossiers `01_sources/documents`, `09_notebooks` et `10_logs` peuvent rester vides. Ils sont conservés pour imposer une structure stable à toutes les équipes et faciliter les prochaines étapes.
