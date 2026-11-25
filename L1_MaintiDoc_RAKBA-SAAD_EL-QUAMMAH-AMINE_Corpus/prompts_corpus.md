# Prompts et règles du corpus MAINTiDOC

## Règle générale

Construire des documents techniques français sur les pneus de moto et les chaînes de transmission. Chaque document traite une problématique distincte et doit rester exploitable par un RAG multimodal.

## Prompt d’annotation visuelle

Décrire uniquement ce qui est directement visible sur l’image. Identifier l’équipement, le composant, la zone observée et les signes visuels. Ne pas transformer une cause hypothétique en diagnostic certain.

## Prompt d’interprétation technique

Formuler les explications et causes possibles à partir de sources constructeurs ou fabricants. Séparer clairement l’observation, l’interprétation, le contrôle physique requis et la recommandation.

## Prompt de contrôle qualité

Vérifier l’identifiant, le titre, la famille, les photographies, les légendes, les références, les licences, la lisibilité, l’extraction textuelle et l’absence de répétition artificielle.

## Règle de sécurité

Une photographie ne confirme pas seule la pression, la tension, l’alignement, l’allongement, l’état interne ou la tolérance de remplacement. Lorsque l’image est ambiguë, demander une clarification ou recommander une inspection qualifiée.
