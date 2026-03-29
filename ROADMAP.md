# Roadmap & Suivi des tâches

## Sécurité
- [x] Corriger la vulnérabilité IDOR dans `soumettre_revisions` (`courses/views.py`)
- [ ] Implémenter le nettoyage XSS (`bleach`) sur le rendu Markdown (dès que l'édition côté client sera envisagée)

## Qualité de code (Refactoring)
- [x] Appliquer le principe DRY sur l'intégration vidéo HTML (`_generer_video_html`)
- [x] Extraire la logique de compilation LaTeX / rendu Markdown dans `courses/utils/latex_parser.py`
- [ ] Optimiser les appels `random.shuffle()` si la volumétrie des questions augmente