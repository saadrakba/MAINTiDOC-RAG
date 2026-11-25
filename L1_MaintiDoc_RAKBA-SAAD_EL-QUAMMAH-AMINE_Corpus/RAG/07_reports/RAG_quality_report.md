# Rapport de qualité RAG multimodal — MAINTiDOC

## Périmètre

Le pipeline a été appliqué aux 45 PDF du corpus de l’équipe RAKBA SAAD et EL QUAMMAH AMINE : 22 documents pneus et 23 documents chaînes. Il suit le notebook fourni : extraction PyMuPDF, encodage CLIP texte/image normalisé, puis indexation persistante ChromaDB.

## Artefacts produits

- 45 documents ingérés ;
- 135 fragments texte, un par page ;
- 135 rendus visuels de pages ;
- 366 images intégrées extraites ;
- vecteurs texte et image de dimension 512 ;
- trois collections ChromaDB séparées : texte, page visuelle, image extraite ;
- manifest avec SHA-256, famille, page, chemin et compte d’images ;
- extraction page par page et fichier texte global pour chaque document.

## Évaluation smoke test

Cinq requêtes représentatives ont été testées. La précision de famille en première position est de **5/5 (100%)**. La précision moyenne de famille dans les cinq premiers résultats textuels est de **84%**. Le détail se trouve dans `retrieval_evaluation.csv` et les résultats bruts dans `retrieval_smoke_tests.json`.

## Critères d’arborescence de qualité

1. Chaque résultat conserve un `document_id` et un numéro de page.
2. Le texte source, le rendu visuel et l’image extraite sont stockés séparément.
3. Les vecteurs sont normalisés L2, conformément au notebook, afin que le produit scalaire corresponde à la similarité cosinus.
4. Les modalités sont indexées dans des collections séparées afin d’éviter de mélanger des distances non comparables sans fusion contrôlée.
5. Les PDF sources et les images conservent une trace SHA-256 ou un chemin d’origine.
6. Les pages sans texte détectable sont signalées dans le manifest ; dans ce corpus, aucune page n’est restée sans texte.
7. La réponse finale d’un assistant devra citer le document et la page récupérés, et rappeler les limites d’un diagnostic visuel.

## Limites et prochaines améliorations

CLIP fournit une représentation commune texte/image, mais le notebook ne définit pas encore de reranking ni de génération de réponse. Pour une version de production, il faudra ajouter un reranker texte, une fusion calibrée des trois collections, un jeu de questions-réponses annoté avec réponses attendues et des mesures Recall@k, MRR et nDCG. Il faudra également contrôler que les images TyreNet utilisées correspondent bien à des pneus de moto, car le dataset contient aussi des pneus automobiles.
