---
description: "Use when editing or creating Django models in ScienceLycée. Covers naming conventions, field patterns, slug auto-population, and migration workflow."
applyTo: "**/models.py"
---
# Django Models — ScienceLycée Conventions

- French naming for models, fields, and Meta options
- Model hierarchy: `Matiere → Chapitre → Lecon → Quiz → Question`
- Slug fields: auto-populated in `save()` via `slugify()`, unique per parent scope (e.g. `unique_together` with parent FK)
- `Lecon.gratuit` BooleanField — marks free public lessons
- `Question.type`: choices from `TypeQuestionChoices` (qcm, vrai_faux, texte_libre)
- `Question.difficulte`: choices from `DifficulteChoices` (FACILE, MOYEN, DIFFICILE), default MOYEN
- `Question.tolerances`: JSONField for alternative answers (texte_libre only)
- Progress models in `progress/models.py`: `UserProgression`, `UserQuizResultat`, `UserChapitreQuizResultat`, `ChapitreDebloque`, `UserQuestionHistorique`, `UserNote`
- `UserNote`: `unique_together = [("user", "lecon")]`, max 2000 chars
- Leitner system: `UserQuestionHistorique` with `boite` (1–5), `prochaine_revision`, intervals `{1: 1d, 2: 3d, 3: 7d, 4: 14d, 5: 30d}`
- After ANY model change: signal `⚠️ Migration requise → migration-writer`
- Never edit migration files manually
