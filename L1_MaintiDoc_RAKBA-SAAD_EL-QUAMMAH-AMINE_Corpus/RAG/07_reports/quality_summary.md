# Qualité du pipeline RAG multimodal MAINTiDOC

- Documents ingérés : 45
- Fragments texte : 135
- Pages visuelles : 135
- Images intégrées extraites : 366
- Dimensions CLIP texte/image : 512
- Collections ChromaDB : `mainti_doc_text`, `mainti_doc_page_visual`, `mainti_doc_extracted_images`
- Tests de recherche : 5 requêtes multimodales

## Critères de qualité appliqués

Traçabilité par document et page, conservation des textes et images sources, normalisation L2 des vecteurs, séparation des modalités, provenance SHA-256, détection des pages sans texte et tests de récupération sur les familles pneus/chaînes.
