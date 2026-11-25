"""Pipeline RAG portable. Exécuter depuis n’importe quel dossier : python 08_scripts/run_rag_pipeline.py"""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
RAG=HERE.parent
CORPUS=RAG.parent
PROJECT=CORPUS.parent
CONFIG=json.loads((RAG/"00_config/paths.json").read_text(encoding="utf-8"))
print("Projet:", PROJECT)
print("Corpus:", CORPUS)
print("PDF famille_1:", len(list((CORPUS/"documents"/"famille_1").glob("*.pdf"))))
print("PDF famille_2:", len(list((CORPUS/"documents"/"famille_2").glob("*.pdf"))))
print("Configuration chargée depuis:", RAG/"00_config")
print("Pour reconstruire l’index complet, utiliser le notebook ou adapter le pipeline d’ingestion avec ces chemins relatifs.")
