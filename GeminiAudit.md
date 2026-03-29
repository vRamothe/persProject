# Audit de Sécurité et Qualité du Code - ScienceLycée

**Date de l'audit :** (Date courante)
**Fichiers analysés :** `backend/courses/views.py`, configurations des agents et seeds.
**Référentiel :** OWASP Top 10

---

## 1. Points Positifs (✅)

*   **Contrôle d'accès (A01)** : Les vues sensibles (`matieres_view`, `chapitre_view`, `lecon_view`, `quiz_view`, `quiz_chapitre_view`, `revisions_view`) sont toutes correctement protégées par le décorateur `@login_required`. De plus, une vérification systématique est faite pour s'assurer qu'un élève ne peut accéder qu'aux contenus de son niveau (`chapitre.niveau == user.niveau`).
*   **Injections SQL (A03)** : L'utilisation de `SearchQuery` et `SearchVector` pour la recherche `recherche_view` est une excellente pratique. Elle tire parti de l'ORM Django et des fonctionnalités PostgreSQL pour éviter les injections SQL liées aux requêtes de recherche textuelles.
*   **SSRF et Intégration Vidéo (A10)** : La fonction `_extraire_youtube_id` utilise des expressions régulières restrictives (`[a-zA-Z0-9_-]{11}`) pour s'assurer que seuls les IDs valides sont extraits. L'intégration se fait de manière sécurisée côté client via un tag `<iframe>`.
*   **Rate Limiting** : La protection contre les abus de soumission de formulaires est présente grâce à l'appel de `_check_quiz_rate_limit(user.id)` dans la vue `soumettre_revisions`.
*   **Vues Publiques** : La vue `lecon_publique_view` gère correctement l'exposition du contenu en vérifiant explicitement `lecon.gratuit` avant d'afficher quoi que ce soit.

---

## 2. Vulnérabilités et Risques Identifiés (Mise à jour suite aux corrections)

### ✅ Vulnérabilité IDOR (Insecure Direct Object Reference) - A01 [CORRIGÉ]
**Emplacement :** `courses/views.py` -> `soumettre_revisions()`
**Ancienne Description :** 
La fonction récupère les ID des questions soumises directement depuis la requête POST : 
`question_ids_raw = request.POST.get("question_ids", "")`
Ensuite, elle interroge la base de données avec ces IDs sans vérifier s'ils appartiennent effectivement à l'utilisateur ou s'ils font partie de sa file de révision actuelle :
`Question.objects.filter(id__in=question_ids)`
**Exploitation :** Un élève de Seconde pourrait forger une requête POST contenant les IDs de questions d'un quiz de Terminale. L'application créerait ou mettrait à jour un objet `UserQuestionHistorique` pour ces questions.
**Recommandation de correction :** 
Avant d'évaluer les réponses, il faut s'assurer que les questions soumises appartiennent à un chapitre dont le niveau correspond à l'utilisateur (ou que le chapitre est débloqué pour lui).
```python
# Correction implémentée :
if user.is_admin:
    questions = list(Question.objects.filter(id__in=question_ids).select_related("quiz__lecon__chapitre__matiere"))
else:
    questions = list(Question.objects.filter(id__in=question_ids, quiz__lecon__chapitre__niveau=user.niveau).select_related("quiz__lecon__chapitre__matiere"))
```

### ⚠️ Risque de XSS / Exécution de code via WeasyPrint (A03)
**Emplacement :** `courses/views.py` -> Rendu Markdown / PDF
**Description :** 
Les fonctions générant le HTML depuis le Markdown (`lecon_view`, `lecon_pdf_view`) n'utilisent pas de mécanisme de nettoyage HTML (comme `bleach`). 
Actuellement, c'est acceptable car le contenu Markdown provient exclusivement des commandes `seed_*.py` contrôlées par l'administrateur.
**Recommandation :** Si, à l'avenir, une interface d'administration permet la saisie ou la modification de leçons par des utilisateurs moins privilégiés (professeurs), il sera indispensable d'assainir le HTML généré par la librairie `markdown` avant de le restituer aux clients ou à WeasyPrint.

---

## 3. Recommandations Qualité du Code (Refactoring)

1.  **Extraction de la logique LaTeX / Markdown :**
    Les fonctions privées `_proteger_latex`, `_restaurer_latex`, `_restaurer_latex_svg` et `_compiler_equations_latex` occupent une grande place dans `views.py`. Il est recommandé de les extraire dans un fichier dédié (par exemple `backend/courses/utils/latex_parser.py`) pour alléger les vues et respecter le principe de séparation des responsabilités.

2.  **Duplication de code (DRY) :**
    La logique de gestion de l'embed vidéo YouTube (création du HTML `<iframe>`) est dupliquée à l'identique entre `lecon_view` et `lecon_publique_view`. Il serait judicieux de l'isoler dans une fonction helper : `_generer_video_html(lecon)`.

3.  **Appels de Randomisation :**
    Dans `_selectionner_questions_chapitre`, l'utilisation intensive de `random.shuffle()` est correcte pour de petites collections, mais pourrait s'avérer lente si la banque de questions devient énorme. Pour le moment, l'implémentation est largement suffisante.

---
**Fin de l'audit**
