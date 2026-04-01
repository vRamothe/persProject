# 04 — Beta Test avec Élèves Actuels

| Champ | Valeur |
|-------|--------|
| **Source** | ROADMAP.md #7 |
| **Phase** | 2 — Acquisition & First Revenue |
| **Type** | Business (non-technique) |
| **LLM recommandé** | Aucun (tâche humaine) |
| **Statut** | ✅ Terminé (support technique) |
| **Priorité** | 4 |
| **Dépendances** | #02 Paywall, #03 Stripe (optionnel — possible sans paiement) |

---

## Description

Créer des comptes gratuits (avec abonnement offert ou flag `beta`) pour les élèves actuels en cours particuliers. Embarquer les parents dans le processus pour récolter du feedback structuré (bugs, UX, contenu) et obtenir les premiers témoignages utilisables pour la landing page (#05).

## Critères d'acceptation

- 5-10 comptes beta créés et actifs avec des élèves réels (niveaux seconde/première/terminale)
- Chaque beta testeur a complété au moins 3 leçons et 2 quiz
- Un formulaire de feedback structuré est distribué (Google Forms ou équivalent) couvrant : navigation, compréhension des leçons, difficulté des quiz, bugs rencontrés
- Au moins 3 retours écrits exploitables (parents ou élèves) collectés
- Les bugs critiques identifiés sont triés et priorisés dans le backlog

## Definition of Done

- Comptes beta créés et documentés (emails, niveaux)
- Feedback collecté et synthétisé dans un document récapitulatif
- Bugs critiques enregistrés comme issues
- Au moins 2 témoignages exploitables pour la landing page (#05)

## Implémentation technique

- `CustomUser.is_beta` — BooleanField (default=False), flag pour accorder l'accès premium gratuit aux bêta-testeurs
- `_user_has_active_subscription(user)` — retourne `True` si `user.is_beta` est `True`, avant même de vérifier l'abonnement Stripe
- Management command `create_beta_accounts` — création de comptes beta en batch via arguments positionnels (`email:niveau`) ou fichier CSV (`--csv`). Flags : `--dry-run`, `--no-email`
- Badge admin "Beta" (amber) affiché dans le panneau utilisateurs pour les comptes `is_beta=True`
- 13 tests ajoutés dans `users/tests.py` couvrant le flag beta, la commande de création et le bypass d'abonnement
