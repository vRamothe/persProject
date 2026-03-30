# ScienceLycée - Plateforme d'Apprentissage Scientifique

ScienceLycée est une application web éducative complète (e-learning) destinée aux élèves de lycée (de la Seconde à la Terminale). Elle a pour objectif d'accompagner les lycéens dans leur apprentissage des matières scientifiques fondamentales : **Mathématiques, Physique et Chimie**.

Le projet se démarque par la richesse de son contenu, généré via des scripts de « seeding » exhaustifs, et par l'intégration d'outils interactifs comme des quiz d'évaluation et un système de révision personnalisé.

---

## 🚀 Fonctionnalités Principales

### 1. Contenu Pédagogique Structuré
- **Organisation hiérarchique** : Le contenu est découpé logiquement en `Matière > Chapitre > Leçon`.
- **Contenu riche** : Support du format Markdown avec intégration native de **LaTeX** pour l'affichage de formules mathématiques, physiques et chimiques complexes.
- **Ségrégation par niveau** : Un élève de Seconde n'accède qu'aux contenus de Seconde (contrôle d'accès strict).
- **Multimédia** : Intégration sécurisée de vidéos explicatives (via des iframes YouTube).

### 2. Évaluation et Quiz
- **Quiz par Leçon** : Chaque leçon peut être accompagnée d'un quiz pour valider les acquis.
- **Types de questions variés** : QCM, Vrai/Faux, et questions à Texte libre avec un système de tolérance de réponses (acceptation de différentes graphies ou formats numériques).
- **Explications détaillées** : Chaque réponse est accompagnée d'une explication pédagogique pour aider l'élève à comprendre ses erreurs.
- **Score minimum de déblocage** : Les chapitres et/ou quiz peuvent requérir un score minimum (ex: 60%) pour valider la progression.

### 3. Fonctionnalités Avancées
- **Système de Révisions personnalisé** : Suivi de l'historique des utilisateurs (`UserQuestionHistorique`) pour proposer des files de révisions adaptées aux besoins de l'élève.
- **Génération de PDF** : Possibilité de convertir et de télécharger les leçons au format PDF (via `WeasyPrint`).
- **Recherche Full-Text** : Moteur de recherche performant utilisant les capacités de recherche vectorielle de la base de données.
- **Leçons Publiques** : Gestion de contenus gratuits/freemium accessibles sans authentification pour découvrir la plateforme.

---

## 🛠 Technologies Utilisées

### Backend & Architecture
- **Langage** : Python
- **Framework** : Django
- **Base de données** : PostgreSQL (exploité notamment pour ses fonctionnalités avancées de recherche textuelle : `SearchQuery` et `SearchVector`).
- **ORM** : Django ORM pour la modélisation des données.

### Rendu et Contenu
- **Markdown & LaTeX** : Parsing du Markdown et compilation des équations LaTeX pour le rendu des cours.
- **WeasyPrint** : Génération de documents PDF à partir du HTML/Markdown des leçons.

---

## 🏗 Architecture des Données

L'application s'articule autour des modèles principaux suivants (définis dans l'application `courses`) :

1. **Matiere** : Catégorie principale (Physique, Chimie, Mathématiques).
2. **Chapitre** : Associé à une matière et à un niveau scolaire (Seconde, Première, Terminale). Possède une condition de déblocage (score minimum).
3. **Lecon** : Contenu textuel, durée estimée, rendu Markdown/LaTeX.
4. **Quiz** : Associé à une leçon, sert d'évaluation.
5. **Question** : Appartient à un quiz. Possède des options, un niveau de difficulté, des points, et une correction explicative.
6. **UserQuestionHistorique** : Stocke l'historique de l'élève pour le système de révision intelligente.

L'initialisation de la base de données (leçons et quiz inclus) se fait via de puissantes commandes de *seed* (ex: `seed_maths_seconde.py`, `seed_chimie_premiere.py`, etc.).

---

## 🔒 Sécurité et Qualité du Code

L'application a fait l'objet d'un audit de sécurité (basé sur le référentiel **OWASP Top 10**) :

- **Authentification & Autorisation (A01)** : Les vues sensibles (`matieres_view`, `lecon_view`, `quiz_view`, etc.) sont protégées par `@login_required`. Les requêtes vérifient que les utilisateurs accèdent uniquement à leur propre niveau scolaire.
- **Protection contre les IDOR (A01)** : La soumission des révisions (`soumettre_revisions`) vérifie de manière cryptographique et logique que les identifiants de questions soumis appartiennent bien au niveau de l'utilisateur.
- **Injections SQL (A03)** : L'utilisation de l'ORM Django et de `SearchVector` immunise l'application contre les injections SQL classiques.
- **SSRF & XSS (A10)** : Les IDs YouTube insérés dans les iframes sont filtrés par une expression régulière stricte (`[a-zA-Z0-9_-]{11}`).
- **Rate Limiting** : Un système de limitation de requêtes (`_check_quiz_rate_limit`) prévient les abus ou les attaques par force brute sur la soumission des quiz.

---

## 🚀 Améliorations Prévues (Roadmap)

L'application suit une feuille de route ambitieuse visant à la transformer en un véritable produit SaaS éducatif, en adressant à la fois les élèves en autonomie et les **enseignants à domicile** souhaitant un outil de suivi pour leurs propres élèves.

### 1. Écosystème Multi-Rôles (Élèves, Enseignants, Parents)

L'objectif est de créer un écosystème où chaque acteur trouve une valeur ajoutée :

- **Comptes Enseignants** :
  - **Tableau de bord dédié** : Vue d'ensemble de tous les élèves suivis, avec progression globale, scores moyens, et temps passé.
  - **Fiche élève détaillée** : Analyse fine du parcours d'un élève (points forts/faibles par chapitre, historique des quiz) pour préparer les cours particuliers.
  - **Système de liaison sécurisé** : Les enseignants peuvent lier leurs élèves via un code unique, garantissant la confidentialité des données.
  - **Messagerie interne** : Faciliter la communication entre l'enseignant, l'élève et ses parents.

- **Comptes Parents** :
  - **Suivi simplifié** : Vue sur l'activité de l'enfant (leçons complétées, résultats aux quiz).
  - **Rapports hebdomadaires** : Boucle de rétention par e-mail pour maintenir l'engagement parental.

### 2. Monétisation et Business (SaaS)

- **Abonnements multiples** :
  - *Formule Élève* : Accès individuel à la plateforme.
  - *Formule Enseignant* : Accès pour le tuteur + un certain nombre de "sièges" pour ses élèves, avec un tarif dégressif.
- **Intégration Stripe** : Gestion des abonnements (mensuels/annuels) et mise en place d'un Paywall visuel pour bloquer le contenu premium et les fonctionnalités de suivi.
- **Plateforme de Tutorat & Réservation** : Planification de cours particuliers avec un système de double-validation (enseignant + élève ou parent).
- **Paiements sécurisés (Stripe)** : Prise d'empreinte bancaire à la demande, débit uniquement lors de la validation mutuelle du cours.
- **Facturation "Service à la Personne" (SAP)** : Génération automatique de factures éligibles au crédit d'impôt (50%), envoyées simultanément à l'élève, aux parents et à l'enseignant.
- **Synchronisation Calendrier** : Intégration fluide avec Google Agenda, Outlook et Apple Calendrier pour ajouter automatiquement les cours validés.
- **Upsell & Services** : Formules hybrides incluant du tutorat vidéo en plus de l'accès à la plateforme pour les élèves autonomes.

### 3. Expérience Pédagogique et Gamification

- **Exercices interactifs** : Ajout de nouveaux formats (glisser-déposer, textes à trous) en utilisant `Alpine.js`.
- **Évaluations avancées** : Quiz chronométrés pour simuler les conditions d'examen, et retours/corrections immédiats pour chaque question.
- **Gamification** : Système de badges (ex: "Série de 10 jours"), succès et classements (Leaderboards) anonymisés par classe ou niveau.
- **Génération de fiches** : Création automatique d'un glossaire et de fiches de formules par matière.

### 4. Dette Technique, Optimisations et Sécurité

- **Optimisation des performances** : Élimination des requêtes N+1 (via `select_related`/`prefetch_related` de l'ORM Django) et remplacement de `random.shuffle()` par un échantillonnage SQL optimisé pour les quiz.
- **Extraction de la logique LaTeX/Markdown** : Déplacer les méthodes de traitement de texte (`_proteger_latex`, `_restaurer_latex`, `_compiler_equations_latex`) depuis `views.py` vers un module utilitaire dédié (ex: `backend/courses/utils/latex_parser.py`).
- **Centralisation de l'intégration vidéo** : Créer un helper `_generer_video_html(lecon)` pour éviter la duplication du code de l'iframe YouTube entre les vues privées et publiques.
- **Assainissement du code HTML (Sanitization)** : Intégration de la librairie `bleach`. Actuellement, les données Markdown proviennent d'un "seed" sécurisé (administrateur). L'intégration de `bleach` préparera le terrain pour de futures interfaces permettant aux professeurs ou utilisateurs moins privilégiés de créer/modifier du contenu, éliminant ainsi les risques de failles XSS.
- **Accessibilité (a11y) & Mobile** : Audit poussé du responsive design (mobile-first pour les quiz) et intégration de balises ARIA et gestion du focus après requêtes HTMX.
