"""
Seed Mathématiques Première — 9 chapitres, leçons uniquement (sans quiz).
Usage : python manage.py seed_maths_premiere
"""

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from courses.models import Matiere, Chapitre, Lecon, Quiz, Question

CHAPITRES = [
    # ──────────────────────────────────────────────
    # CHAPITRE 1 — Second degré
    # ──────────────────────────────────────────────
    {
        'ordre': 1,
        'titre': 'Second degré',
        'description': "Trinôme du second degré, discriminant, factorisation, signe et représentation graphique.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Le trinôme du second degré',
                'duree': 35,
                'contenu': """# Le trinôme du second degré

## Introduction

Le **trinôme du second degré** est un pilier de l'algèbre au lycée. Il intervient aussi bien en mathématiques pures (factorisation, étude de signe) qu'en sciences physiques (trajectoire parabolique, énergie cinétique).

---

## Définition

On appelle **trinôme du second degré** toute expression de la forme :

$$f(x) = ax^2 + bx + c$$

où $a$, $b$, $c$ sont des réels avec $a \\neq 0$.

> Le coefficient $a$ est appelé **coefficient dominant**. Il détermine le sens d'ouverture de la parabole.

---

## Représentation graphique

La courbe représentative de $f$ est une **parabole** :

- Si $a > 0$ : parabole **tournée vers le haut** (forme de « U ») → la fonction admet un **minimum**.
- Si $a < 0$ : parabole **tournée vers le bas** (forme de « ∩ ») → la fonction admet un **maximum**.

---

## Forme canonique

Tout trinôme $f(x) = ax^2 + bx + c$ peut s'écrire sous sa **forme canonique** :

$$f(x) = a\\left(x + \\frac{b}{2a}\\right)^2 - \\frac{\\Delta}{4a}$$

où $\\Delta = b^2 - 4ac$ est le **discriminant** du trinôme.

### Démonstration

On factorise par $a$ :

$$f(x) = a\\left(x^2 + \\frac{b}{a}x\\right) + c$$

On complète le carré à l'intérieur de la parenthèse :

$$x^2 + \\frac{b}{a}x = \\left(x + \\frac{b}{2a}\\right)^2 - \\frac{b^2}{4a^2}$$

D'où :

$$f(x) = a\\left[\\left(x + \\frac{b}{2a}\\right)^2 - \\frac{b^2}{4a^2}\\right] + c = a\\left(x + \\frac{b}{2a}\\right)^2 - \\frac{b^2}{4a} + c$$

Comme $c = \\frac{4ac}{4a}$, on obtient :

$$f(x) = a\\left(x + \\frac{b}{2a}\\right)^2 - \\frac{b^2 - 4ac}{4a} = a\\left(x + \\frac{b}{2a}\\right)^2 - \\frac{\\Delta}{4a}$$

---

## Sommet de la parabole

Le **sommet** $S$ de la parabole est le point d'abscisse $\\alpha = -\\frac{b}{2a}$ et d'ordonnée $\\beta = f(\\alpha) = -\\frac{\\Delta}{4a}$ :

$$S\\left(-\\frac{b}{2a} \\;; -\\frac{\\Delta}{4a}\\right)$$

C'est le point **le plus bas** si $a > 0$, le point **le plus haut** si $a < 0$.

La droite $x = -\\frac{b}{2a}$ est l'**axe de symétrie** de la parabole.

---

## Le discriminant

Le **discriminant** est la quantité :

$$\\Delta = b^2 - 4ac$$

Il joue un rôle central car il détermine le nombre de racines réelles du trinôme.

| Signe de $\\Delta$ | Nombre de racines | Interprétation graphique |
|----|----|----|
| $\\Delta > 0$ | 2 racines distinctes $x_1$ et $x_2$ | La parabole coupe l'axe des abscisses en 2 points |
| $\\Delta = 0$ | 1 racine double $x_0$ | La parabole est tangente à l'axe des abscisses |
| $\\Delta < 0$ | Aucune racine réelle | La parabole ne coupe pas l'axe des abscisses |

---

## Exemple

Soit $f(x) = 2x^2 - 8x + 6$.

- $a = 2$, $b = -8$, $c = 6$
- $\\Delta = (-8)^2 - 4 \\times 2 \\times 6 = 64 - 48 = 16 > 0$

Le trinôme admet donc **deux racines réelles distinctes**.

- Sommet : $\\alpha = -\\frac{-8}{2 \\times 2} = 2$ et $\\beta = f(2) = 8 - 16 + 6 = -2$, d'où $S(2 ; -2)$.
- Forme canonique : $f(x) = 2(x-2)^2 - 2$.

---

## À retenir

- Un trinôme $ax^2 + bx + c$ avec $a \\neq 0$ a pour courbe une **parabole**.
- La **forme canonique** met en évidence le sommet de la parabole.
- Le **discriminant** $\\Delta = b^2 - 4ac$ détermine le nombre de racines.
- Le sommet a pour coordonnées $\\left(-\\frac{b}{2a} ; -\\frac{\\Delta}{4a}\\right)$.
""",
                'quiz': {
                    'titre': 'Quiz — Le trinôme du second degré',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quelle est la forme générale d'un trinôme du second degré ?",
                            'options': ["$ax^2 + bx + c$ avec $a \\\\neq 0$", "$ax + b$ avec $a \\\\neq 0$", "$ax^3 + bx^2 + cx + d$", "$a\\\\sqrt{x} + b$"],
                            'reponse_correcte': '0',
                            'explication': "Un trinôme du second degré est de la forme $ax^2 + bx + c$ avec $a \\neq 0$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quelle est la formule du discriminant $\\\\Delta$ du trinôme $ax^2 + bx + c$ ?",
                            'options': ["$b^2 + 4ac$", "$b^2 - 4ac$", "$4ac - b^2$", "$a^2 - 4bc$"],
                            'reponse_correcte': '1',
                            'explication': "Le discriminant est $\\Delta = b^2 - 4ac$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Si $a > 0$, dans quel sens s'ouvre la parabole ?",
                            'options': ["Vers le haut", "Vers le bas", "Vers la droite", "Vers la gauche"],
                            'reponse_correcte': '0',
                            'explication': "Si $a > 0$, la parabole est tournée vers le haut (forme de U) et admet un minimum.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quelle est l'abscisse du sommet de la parabole $f(x) = ax^2 + bx + c$ ?",
                            'options': ["$-\\\\frac{b}{a}$", "$\\\\frac{b}{2a}$", "$-\\\\frac{b}{2a}$", "$-\\\\frac{c}{a}$"],
                            'reponse_correcte': '2',
                            'explication': "L'abscisse du sommet est $\\alpha = -\\frac{b}{2a}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Si $\\\\Delta > 0$, combien de racines réelles possède le trinôme ?",
                            'options': ["Aucune", "Une racine double", "Deux racines distinctes", "Une infinité"],
                            'reponse_correcte': '2',
                            'explication': "Lorsque $\\Delta > 0$, le trinôme admet deux racines réelles distinctes.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quel est le discriminant du trinôme $x^2 - 6x + 9$ ?",
                            'options': ["$-12$", "$0$", "$36$", "$72$"],
                            'reponse_correcte': '1',
                            'explication': "$\\Delta = (-6)^2 - 4 \\times 1 \\times 9 = 36 - 36 = 0$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Quelle est la forme canonique de $f(x) = 2x^2 - 8x + 6$ ?",
                            'options': ["$2(x - 2)^2 + 2$", "$2(x - 2)^2 - 2$", "$2(x + 2)^2 - 2$", "$2(x - 4)^2 - 26$"],
                            'reponse_correcte': '1',
                            'explication': "$\\alpha = -\\frac{-8}{2 \\times 2} = 2$, $\\beta = f(2) = 8 - 16 + 6 = -2$, d'où $f(x) = 2(x - 2)^2 - 2$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Quelle quantité vaut l'ordonnée du sommet de la parabole ?",
                            'options': ["$-\\\\frac{b}{2a}$", "$-\\\\frac{\\\\Delta}{4a}$", "$\\\\frac{\\\\Delta}{4a}$", "$\\\\frac{b^2}{2a}$"],
                            'reponse_correcte': '1',
                            'explication': "L'ordonnée du sommet est $\\beta = -\\frac{\\Delta}{4a}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Le trinôme $3x^2 + 2x + 5$ a un discriminant $\\\\Delta = 4 - 60 = -56$. Que peut-on en conclure ?",
                            'options': ["Il admet deux racines distinctes", "Il admet une racine double", "Il n'admet aucune racine réelle", "Il est toujours négatif"],
                            'reponse_correcte': '2',
                            'explication': "$\\Delta < 0$ signifie que le trinôme n'admet aucune racine réelle.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quel est le sommet de la parabole $f(x) = -x^2 + 4x - 1$ ?",
                            'options': ["$S(2 ; 3)$", "$S(-2 ; -13)$", "$S(2 ; -3)$", "$S(4 ; -1)$"],
                            'reponse_correcte': '0',
                            'explication': "$\\alpha = -\\frac{4}{2(-1)} = 2$, $f(2) = -4 + 8 - 1 = 3$, donc $S(2 ; 3)$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Quelle est la forme canonique de $f(x) = x^2 + 6x + 5$ ?",
                            'options': ["$(x + 3)^2 - 4$", "$(x - 3)^2 + 4$", "$(x + 6)^2 - 31$", "$(x + 3)^2 + 5$"],
                            'reponse_correcte': '0',
                            'explication': "$\\alpha = -3$, $\\Delta = 36 - 20 = 16$, $\\beta = -\\frac{16}{4} = -4$. Donc $f(x) = (x+3)^2 - 4$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Le coefficient $a$ dans $f(x) = ax^2 + bx + c$ détermine :",
                            'options': ["La position du sommet sur l'axe des abscisses", "Le sens d'ouverture de la parabole", "Le nombre de racines", "La valeur du discriminant uniquement"],
                            'reponse_correcte': '1',
                            'explication': "Le signe de $a$ détermine le sens d'ouverture : vers le haut si $a > 0$, vers le bas si $a < 0$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Si $\\\\Delta = 0$ pour le trinôme $ax^2 + bx + c$, quelle est la forme factorisée ?",
                            'options': ["$a(x - x_1)(x - x_2)$", "$a(x - x_0)^2$", "Le trinôme ne se factorise pas", "$a(x + x_0)^2$"],
                            'reponse_correcte': '1',
                            'explication': "Avec une racine double $x_0 = -\\frac{b}{2a}$, la factorisation est $a(x - x_0)^2$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "La parabole représentant $f(x) = -2x^2 + x + 3$ s'ouvre vers le haut.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Comme $a = -2 < 0$, la parabole s'ouvre vers le bas.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Si le discriminant est négatif, le trinôme ne coupe jamais l'axe des abscisses.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$\\Delta < 0$ signifie qu'il n'y a aucune racine réelle : la parabole ne coupe pas l'axe des abscisses.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "L'axe de symétrie de la parabole $f(x) = ax^2 + bx + c$ a pour équation $x = -\\\\frac{b}{2a}$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "L'axe de symétrie passe par le sommet d'abscisse $-\\frac{b}{2a}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Calculer le discriminant du trinôme $2x^2 - 3x + 1$.",
                            'options': None,
                            'reponse_correcte': '1',
                            'tolerances': ['1.0', '1,0'],
                            'explication': "$\\Delta = (-3)^2 - 4 \\times 2 \\times 1 = 9 - 8 = 1$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Donner l'abscisse du sommet de la parabole $f(x) = x^2 - 4x + 7$.",
                            'options': None,
                            'reponse_correcte': '2',
                            'tolerances': ['2.0', '2,0'],
                            'explication': "$\\alpha = -\\frac{-4}{2 \\times 1} = 2$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Calculer le discriminant du trinôme $x^2 + 2x + 5$.",
                            'options': None,
                            'reponse_correcte': '-16',
                            'tolerances': ['-16.0', '-16,0'],
                            'explication': "$\\Delta = 2^2 - 4 \\times 1 \\times 5 = 4 - 20 = -16$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Déterminer la forme canonique de $f(x) = x^2 - 2x - 3$. Donner la réponse sous la forme $(x - a)^2 - b$ (avec a et b positifs).",
                            'options': None,
                            'reponse_correcte': '(x - 1)^2 - 4',
                            'tolerances': ['(x-1)^2 - 4', '(x-1)^2-4', '(x - 1)² - 4'],
                            'explication': "$\\alpha = 1$, $f(1) = 1 - 2 - 3 = -4$. Donc $f(x) = (x - 1)^2 - 4$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Résolution et factorisation',
                'duree': 35,
                'contenu': """# Résolution et factorisation du trinôme

## Résolution de $ax^2 + bx + c = 0$

La résolution de l'équation du second degré repose entièrement sur le signe du **discriminant** $\\Delta = b^2 - 4ac$.

---

### Cas $\\Delta > 0$ — Deux racines distinctes

L'équation admet deux solutions réelles :

$$x_1 = \\frac{-b - \\sqrt{\\Delta}}{2a} \\qquad \\text{et} \\qquad x_2 = \\frac{-b + \\sqrt{\\Delta}}{2a}$$

### Cas $\\Delta = 0$ — Racine double

L'équation admet une unique solution (racine double) :

$$x_0 = -\\frac{b}{2a}$$

### Cas $\\Delta < 0$ — Pas de racine réelle

L'équation n'a **aucune solution** dans $\\mathbb{R}$.

---

## Relations entre coefficients et racines

Lorsque le trinôme $ax^2 + bx + c$ admet deux racines $x_1$ et $x_2$ (éventuellement confondues), on a les **relations de Viète** :

$$x_1 + x_2 = -\\frac{b}{a}$$

$$x_1 \\cdot x_2 = \\frac{c}{a}$$

> **Application :** si on connaît la somme et le produit de deux nombres, on peut former l'équation du second degré dont ils sont racines : $x^2 - Sx + P = 0$, où $S$ est la somme et $P$ le produit.

---

## Factorisation du trinôme

### Si $\\Delta > 0$

Le trinôme se **factorise** :

$$ax^2 + bx + c = a(x - x_1)(x - x_2)$$

### Si $\\Delta = 0$

$$ax^2 + bx + c = a(x - x_0)^2$$

### Si $\\Delta < 0$

Le trinôme ne se factorise **pas** dans $\\mathbb{R}$.

---

## Exemples détaillés

### Exemple 1

Résoudre $x^2 - 5x + 6 = 0$.

- $a=1$, $b=-5$, $c=6$
- $\\Delta = 25 - 24 = 1 > 0$
- $x_1 = \\frac{5 - 1}{2} = 2$ et $x_2 = \\frac{5 + 1}{2} = 3$
- Factorisation : $x^2 - 5x + 6 = (x-2)(x-3)$

**Vérification par Viète :** $x_1 + x_2 = 5 = -\\frac{-5}{1}$ ✓ et $x_1 \\cdot x_2 = 6 = \\frac{6}{1}$ ✓

### Exemple 2

Résoudre $4x^2 - 12x + 9 = 0$.

- $\\Delta = 144 - 144 = 0$
- $x_0 = \\frac{12}{8} = \\frac{3}{2}$
- Factorisation : $4x^2 - 12x + 9 = 4\\left(x - \\frac{3}{2}\\right)^2 = (2x-3)^2$

### Exemple 3

Résoudre $x^2 + x + 1 = 0$.

- $\\Delta = 1 - 4 = -3 < 0$

Pas de solution réelle. Le trinôme reste strictement positif pour tout $x \\in \\mathbb{R}$ (car $a = 1 > 0$).

---

## Équations se ramenant au second degré

Certaines équations se ramènent au second degré par un changement de variable.

**Exemple :** Résoudre $x^4 - 5x^2 + 4 = 0$.

On pose $X = x^2$ : l'équation devient $X^2 - 5X + 4 = 0$.

- $\\Delta = 25 - 16 = 9$, $X_1 = 1$, $X_2 = 4$

Puis : $x^2 = 1 \\Rightarrow x = \\pm 1$ et $x^2 = 4 \\Rightarrow x = \\pm 2$.

L'ensemble des solutions est $\\{-2 ; -1 ; 1 ; 2\\}$.

---

## À retenir

- Les formules $x_{1,2} = \\frac{-b \\pm \\sqrt{\\Delta}}{2a}$ donnent les racines lorsque $\\Delta \\geq 0$.
- Un trinôme de discriminant positif se factorise : $a(x-x_1)(x-x_2)$.
- Les **relations de Viète** lient les racines aux coefficients : $x_1+x_2 = -\\frac{b}{a}$, $x_1 x_2 = \\frac{c}{a}$.
""",
                'quiz': {
                    'titre': 'Quiz — Résolution et factorisation',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quelles sont les racines de $x^2 - 5x + 6 = 0$ ?",
                            'options': ["$x = 1$ et $x = 6$", "$x = 2$ et $x = 3$", "$x = -2$ et $x = -3$", "$x = -1$ et $x = 6$"],
                            'reponse_correcte': '1',
                            'explication': "$\\Delta = 25 - 24 = 1$, $x_1 = \\frac{5-1}{2} = 2$ et $x_2 = \\frac{5+1}{2} = 3$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quelle est la formule donnant les racines lorsque $\\\\Delta > 0$ ?",
                            'options': ["$x = \\\\frac{b \\\\pm \\\\sqrt{\\\\Delta}}{2a}$", "$x = \\\\frac{-b \\\\pm \\\\sqrt{\\\\Delta}}{2a}$", "$x = \\\\frac{-b \\\\pm \\\\Delta}{2a}$", "$x = \\\\frac{b \\\\pm \\\\Delta}{a}$"],
                            'reponse_correcte': '1',
                            'explication': "Les racines sont $x_{1,2} = \\frac{-b \\pm \\sqrt{\\Delta}}{2a}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Lorsque $\\\\Delta = 0$, la racine double est :",
                            'options': ["$x_0 = \\\\frac{b}{2a}$", "$x_0 = -\\\\frac{b}{2a}$", "$x_0 = -\\\\frac{b}{a}$", "$x_0 = \\\\frac{c}{a}$"],
                            'reponse_correcte': '1',
                            'explication': "La racine double est $x_0 = -\\frac{b}{2a}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "La factorisation de $x^2 - 5x + 6$ est :",
                            'options': ["$(x - 1)(x - 6)$", "$(x + 2)(x + 3)$", "$(x - 2)(x - 3)$", "$(x - 2)(x + 3)$"],
                            'reponse_correcte': '2',
                            'explication': "Les racines sont 2 et 3, donc $x^2 - 5x + 6 = (x-2)(x-3)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "D'après les relations de Viète, $x_1 + x_2$ vaut :",
                            'options': ["$\\\\frac{b}{a}$", "$-\\\\frac{b}{a}$", "$\\\\frac{c}{a}$", "$-\\\\frac{c}{a}$"],
                            'reponse_correcte': '1',
                            'explication': "La somme des racines est $x_1 + x_2 = -\\frac{b}{a}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quelle est la factorisation de $4x^2 - 12x + 9$ ?",
                            'options': ["$(2x - 3)^2$", "$(4x - 3)(x - 3)$", "$(2x + 3)^2$", "$(2x - 9)(2x - 1)$"],
                            'reponse_correcte': '0',
                            'explication': "$\\Delta = 144 - 144 = 0$, racine double $x_0 = \\frac{3}{2}$. Donc $4(x - \\frac{3}{2})^2 = (2x - 3)^2$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "D'après les relations de Viète, $x_1 \\\\cdot x_2$ vaut :",
                            'options': ["$-\\\\frac{b}{a}$", "$\\\\frac{b}{a}$", "$\\\\frac{c}{a}$", "$-\\\\frac{c}{a}$"],
                            'reponse_correcte': '2',
                            'explication': "Le produit des racines est $x_1 \\cdot x_2 = \\frac{c}{a}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "L'équation $x^2 + x + 1 = 0$ a pour discriminant $\\\\Delta = -3$. Que peut-on dire ?",
                            'options': ["Elle a une racine double", "Elle a deux racines positives", "Elle n'a aucune solution réelle", "Elle a deux racines négatives"],
                            'reponse_correcte': '2',
                            'explication': "$\\Delta = -3 < 0$, donc l'équation n'a aucune solution dans $\\mathbb{R}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Résoudre $2x^2 - 3x + 1 = 0$. Les racines sont :",
                            'options': ["$x = \\\\frac{1}{2}$ et $x = 1$", "$x = -\\\\frac{1}{2}$ et $x = -1$", "$x = 1$ et $x = 2$", "$x = \\\\frac{3}{2}$ et $x = -1$"],
                            'reponse_correcte': '0',
                            'explication': "$\\Delta = 9 - 8 = 1$. $x_1 = \\frac{3-1}{4} = \\frac{1}{2}$, $x_2 = \\frac{3+1}{4} = 1$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "On sait que deux nombres ont pour somme 7 et pour produit 12. Quelle équation vérifient-ils ?",
                            'options': ["$x^2 + 7x + 12 = 0$", "$x^2 - 7x + 12 = 0$", "$x^2 - 7x - 12 = 0$", "$x^2 + 7x - 12 = 0$"],
                            'reponse_correcte': '1',
                            'explication': "Si $S = 7$ et $P = 12$, l'équation est $x^2 - Sx + P = 0$, soit $x^2 - 7x + 12 = 0$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Pour l'équation $x^4 - 5x^2 + 4 = 0$, quel changement de variable convient ?",
                            'options': ["$X = x + 1$", "$X = x^2$", "$X = \\\\sqrt{x}$", "$X = 2x$"],
                            'reponse_correcte': '1',
                            'explication': "On pose $X = x^2$ pour obtenir $X^2 - 5X + 4 = 0$, une équation du second degré en $X$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Combien de solutions réelles possède l'équation $x^4 - 5x^2 + 4 = 0$ ?",
                            'options': ["2", "3", "4", "0"],
                            'reponse_correcte': '2',
                            'explication': "$X = x^2$ donne $X = 1$ ou $X = 4$. Puis $x = \\pm 1$ et $x = \\pm 2$, soit 4 solutions.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Si le trinôme $ax^2 + bx + c$ ne se factorise pas dans $\\\\mathbb{R}$, alors :",
                            'options': ["$\\\\Delta > 0$", "$\\\\Delta = 0$", "$\\\\Delta < 0$", "$a = 0$"],
                            'reponse_correcte': '2',
                            'explication': "Le trinôme ne se factorise pas dans $\\mathbb{R}$ si et seulement si $\\Delta < 0$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Si $x_1$ et $x_2$ sont les racines de $x^2 - 4x + 3 = 0$, alors $x_1 + x_2 = 4$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Par Viète, $x_1 + x_2 = -\\frac{b}{a} = -\\frac{-4}{1} = 4$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "L'équation $3x^2 - 6x + 3 = 0$ admet deux racines distinctes.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "$\\Delta = 36 - 36 = 0$, donc l'équation a une racine double $x_0 = 1$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La factorisation de $2x^2 - 10x + 12$ est $2(x - 2)(x - 3)$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$\\Delta = 100 - 96 = 4$. Racines : $x_1 = \\frac{10-2}{4} = 2$ et $x_2 = 3$. Donc $2(x-2)(x-3)$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Résoudre $x^2 - 4x + 3 = 0$. Donner la plus petite racine.",
                            'options': None,
                            'reponse_correcte': '1',
                            'tolerances': ['1.0', '1,0'],
                            'explication': "$\\Delta = 16 - 12 = 4$. $x_1 = \\frac{4-2}{2} = 1$, $x_2 = 3$. La plus petite racine est 1.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer le produit des racines de $3x^2 + 6x - 9 = 0$ en utilisant les relations de Viète.",
                            'options': None,
                            'reponse_correcte': '-3',
                            'tolerances': ['-3.0', '-3,0'],
                            'explication': "Par Viète, $x_1 \\cdot x_2 = \\frac{c}{a} = \\frac{-9}{3} = -3$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Donner le nombre de solutions réelles de $x^4 - 10x^2 + 9 = 0$.",
                            'options': None,
                            'reponse_correcte': '4',
                            'tolerances': ['quatre'],
                            'explication': "Posons $X = x^2$ : $X^2 - 10X + 9 = 0$ donne $X = 1$ et $X = 9$, puis $x = \\pm 1$ et $x = \\pm 3$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Trouver deux nombres dont la somme est 10 et le produit est 21. Donner le plus grand.",
                            'options': None,
                            'reponse_correcte': '7',
                            'tolerances': ['7.0', '7,0'],
                            'explication': "On résout $x^2 - 10x + 21 = 0$ : $\\Delta = 100 - 84 = 16$, racines 3 et 7. Le plus grand est 7.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 3,
                'titre': 'Signe du trinôme',
                'duree': 30,
                'contenu': """# Signe du trinôme du second degré

## Problématique

Étudier le **signe** de $f(x) = ax^2 + bx + c$ revient à déterminer pour quelles valeurs de $x$ l'expression est positive, négative ou nulle. C'est essentiel pour résoudre des **inéquations** du second degré.

---

## Règle du signe

Le signe du trinôme dépend du **signe de $a$** et du **discriminant $\\Delta$**.

### Cas $\\Delta > 0$ (deux racines $x_1 < x_2$)

Le trinôme **s'annule** en $x_1$ et $x_2$ et est :

- **du signe de $a$** à l'**extérieur** des racines (pour $x < x_1$ et $x > x_2$) ;
- **du signe opposé à $a$** entre les racines (pour $x_1 < x < x_2$).

| $x$ | $-\\infty$ | | $x_1$ | | $x_2$ | | $+\\infty$ |
|---|---|---|---|---|---|---|---|
| signe de $f(x)$ | signe de $a$ | | $0$ | signe de $-a$ | $0$ | | signe de $a$ |

### Cas $\\Delta = 0$ (racine double $x_0$)

Le trinôme s'annule uniquement en $x_0$ et est **du signe de $a$** partout ailleurs :

$$f(x) = a(x - x_0)^2 \\geq 0 \\text{ si } a > 0, \\quad f(x) \\leq 0 \\text{ si } a < 0$$

### Cas $\\Delta < 0$ (pas de racine réelle)

Le trinôme ne s'annule jamais et est **du signe de $a$** pour tout $x \\in \\mathbb{R}$ :

$$\\text{Si } a > 0 \\text{ : } f(x) > 0 \\text{ pour tout } x \\in \\mathbb{R}$$
$$\\text{Si } a < 0 \\text{ : } f(x) < 0 \\text{ pour tout } x \\in \\mathbb{R}$$

---

## Méthode de résolution d'une inéquation

Pour résoudre $ax^2 + bx + c \\leq 0$ (ou $\\geq 0$, $< 0$, $> 0$) :

1. Calculer $\\Delta = b^2 - 4ac$.
2. Trouver les racines (si elles existent).
3. Dresser le **tableau de signes**.
4. Lire les intervalles solutions.

---

## Exemples

### Exemple 1

Résoudre $x^2 - 4x + 3 \\geq 0$.

- $\\Delta = 16 - 12 = 4 > 0$, racines $x_1 = 1$ et $x_2 = 3$
- $a = 1 > 0$, donc $f(x) \\geq 0$ à l'**extérieur** des racines

**Solution :** $x \\in ]-\\infty ; 1] \\cup [3 ; +\\infty[$

### Exemple 2

Résoudre $-2x^2 + 3x - 5 > 0$.

- $\\Delta = 9 - 40 = -31 < 0$
- $a = -2 < 0$, donc $f(x) < 0$ pour tout $x$

**Solution :** $\\emptyset$ (ensemble vide). L'inéquation n'a aucune solution.

### Exemple 3

Résoudre $x^2 - 6x + 9 < 0$.

- $\\Delta = 36 - 36 = 0$, racine double $x_0 = 3$
- $a = 1 > 0$, donc $f(x) = (x-3)^2 \\geq 0$ pour tout $x$

**Solution :** $\\emptyset$. Le trinôme ne prend jamais de valeur strictement négative.

---

## Application : position relative d'une parabole et d'une droite

Pour étudier la position de la parabole $y = ax^2 + bx + c$ par rapport à la droite $y = mx + p$, on étudie le signe de :

$$g(x) = ax^2 + (b - m)x + (c - p)$$

- Si $g(x) > 0$ : la parabole est **au-dessus** de la droite.
- Si $g(x) < 0$ : la parabole est **en dessous**.
- Si $g(x) = 0$ : il y a **intersection**.

---

## Résumé visuel

Le trinôme est **du signe de $a$ à l'extérieur des racines** (quand elles existent). C'est la règle fondamentale à retenir.

Moyen mnémotechnique :

> Si $a > 0$, la parabole « sourit » (U) → **positif** à l'extérieur.
> Si $a < 0$, la parabole « pleure » (∩) → **négatif** à l'extérieur.

---

## À retenir

- Le signe du trinôme dépend de $\\Delta$ et du signe de $a$.
- Si $\\Delta > 0$ : le trinôme est **du signe de $a$ à l'extérieur** des racines, **du signe de $-a$ entre** les racines.
- Si $\\Delta = 0$ : le trinôme est **du signe de $a$** partout (nul en $x_0$).
- Si $\\Delta < 0$ : le trinôme est **strictement du signe de $a$** pour tout réel.
""",
                'quiz': {
                    'titre': 'Quiz — Signe du trinôme',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Si $a > 0$ et $\\\\Delta > 0$, quel est le signe du trinôme entre ses deux racines ?",
                            'options': ["Positif", "Négatif", "Nul", "On ne peut pas savoir"],
                            'reponse_correcte': '1',
                            'explication': "Si $a > 0$ et $\\Delta > 0$, le trinôme est du signe de $-a$ (donc négatif) entre les racines.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Si $a > 0$ et $\\\\Delta < 0$, le trinôme est :",
                            'options': ["Toujours négatif", "Toujours positif", "Positif puis négatif", "Nul en un point"],
                            'reponse_correcte': '1',
                            'explication': "Avec $a > 0$ et $\\Delta < 0$, le trinôme n'a pas de racine et reste strictement positif.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "L'ensemble des solutions de $x^2 - 4x + 3 \\\\geq 0$ est :",
                            'options': ["$[1 ; 3]$", "$]-\\\\infty ; 1] \\\\cup [3 ; +\\\\infty[$", "$]-\\\\infty ; -1] \\\\cup [3 ; +\\\\infty[$", "$\\\\mathbb{R}$"],
                            'reponse_correcte': '1',
                            'explication': "Racines 1 et 3, $a = 1 > 0$ : le trinôme est $\\geq 0$ à l'extérieur des racines.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Le trinôme $-x^2 + 2x - 5$ a $\\\\Delta = 4 - 20 = -16$. Il est :",
                            'options': ["Toujours positif", "Positif sauf en un point", "Toujours négatif", "Positif entre les racines"],
                            'reponse_correcte': '2',
                            'explication': "$a = -1 < 0$ et $\\Delta < 0$ : le trinôme est strictement du signe de $a$, donc toujours négatif.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Le trinôme $x^2 - 6x + 9$ a pour discriminant $\\\\Delta = 0$. Son signe est :",
                            'options': ["Toujours strictement positif", "Positif ou nul pour tout $x$", "Négatif pour certains $x$", "Nul pour tout $x$"],
                            'reponse_correcte': '1',
                            'explication': "$a = 1 > 0$ et $\\Delta = 0$ : $f(x) = (x-3)^2 \\geq 0$ pour tout $x$, nul uniquement en $x = 3$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Pour résoudre une inéquation du second degré, la première étape est :",
                            'options': ["Factoriser directement", "Calculer le discriminant", "Dresser le tableau de variation", "Tracer la courbe"],
                            'reponse_correcte': '1',
                            'explication': "On commence par calculer $\\Delta = b^2 - 4ac$ pour déterminer les racines éventuelles.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Résoudre $-2x^2 + 3x - 5 > 0$. L'ensemble des solutions est :",
                            'options': ["$\\\\mathbb{R}$", "$]1 ; 5[$", "$\\\\emptyset$", "$]-\\\\infty ; 0[$"],
                            'reponse_correcte': '2',
                            'explication': "$\\Delta = 9 - 40 = -31 < 0$ et $a = -2 < 0$ : le trinôme est toujours négatif, aucune valeur ne le rend positif.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Si $a < 0$ et $\\\\Delta > 0$, le trinôme est positif :",
                            'options': ["À l'extérieur des racines", "Entre les racines", "Partout", "Nulle part"],
                            'reponse_correcte': '1',
                            'explication': "Si $a < 0$, le trinôme est du signe de $-a$ (positif) entre les racines et négatif à l'extérieur.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "L'ensemble des solutions de $x^2 + 2x - 8 < 0$ est :",
                            'options': ["$]-4 ; 2[$", "$]-\\\\infty ; -4[ \\\\cup ]2 ; +\\\\infty[$", "$]-2 ; 4[$", "$[- 4 ; 2]$"],
                            'reponse_correcte': '0',
                            'explication': "$\\Delta = 4 + 32 = 36$, racines $-4$ et $2$. $a > 0$ : le trinôme est négatif entre les racines, soit $]-4 ; 2[$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Pour étudier la position de la parabole $y = x^2$ par rapport à la droite $y = 2x + 3$, on étudie le signe de :",
                            'options': ["$x^2 + 2x + 3$", "$x^2 - 2x + 3$", "$x^2 - 2x - 3$", "$x^2 + 2x - 3$"],
                            'reponse_correcte': '2',
                            'explication': "On étudie $g(x) = x^2 - (2x + 3) = x^2 - 2x - 3$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "L'inéquation $x^2 - 6x + 9 < 0$ a pour ensemble de solutions :",
                            'options': ["$\\\\{3\\\\}$", "$]-\\\\infty ; 3[$", "$\\\\emptyset$", "$]3 ; +\\\\infty[$"],
                            'reponse_correcte': '2',
                            'explication': "$f(x) = (x-3)^2 \\geq 0$ pour tout $x$ : le trinôme n'est jamais strictement négatif.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "L'ensemble des solutions de $-x^2 + 4x - 3 \\\\geq 0$ est :",
                            'options': ["$[1 ; 3]$", "$]-\\\\infty ; 1] \\\\cup [3 ; +\\\\infty[$", "$\\\\mathbb{R}$", "$\\\\emptyset$"],
                            'reponse_correcte': '0',
                            'explication': "Racines 1 et 3, $a = -1 < 0$ : le trinôme est $\\geq 0$ entre les racines, soit $[1 ; 3]$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Le moyen mnémotechnique pour le signe du trinôme quand $a > 0$ est :",
                            'options': ["La parabole « pleure » → négatif dehors", "La parabole « sourit » → positif dehors", "La parabole « sourit » → négatif dehors", "La parabole « pleure » → positif dehors"],
                            'reponse_correcte': '1',
                            'explication': "Si $a > 0$, la parabole a la forme d'un U (« sourit ») : elle est positive à l'extérieur des racines.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Le trinôme $x^2 + 1$ est strictement positif pour tout réel $x$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$a = 1 > 0$, $\\Delta = 0 - 4 = -4 < 0$ : le trinôme est du signe de $a$, donc strictement positif.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Si $a < 0$ et $\\\\Delta = 0$, le trinôme est négatif ou nul pour tout $x$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$a < 0$ et $\\Delta = 0$ : $f(x) = a(x - x_0)^2 \\leq 0$ pour tout $x$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "L'inéquation $2x^2 + 3x + 5 > 0$ est vérifiée pour tout réel $x$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$\\Delta = 9 - 40 = -31 < 0$ et $a = 2 > 0$ : le trinôme est strictement positif partout.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Résoudre $x^2 - 9 \\\\leq 0$. Donner l'ensemble des solutions sous la forme $[a ; b]$.",
                            'options': None,
                            'reponse_correcte': '[-3 ; 3]',
                            'tolerances': ['[-3;3]', '[-3, 3]', '[-3 ;3]'],
                            'explication': "$x^2 - 9 = (x-3)(x+3)$. Racines $-3$ et $3$, $a > 0$ : négatif entre les racines. Solution : $[-3 ; 3]$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Le trinôme $-3x^2 + 12x - 12$ a $\\\\Delta = 0$. Pour quelle valeur de $x$ s'annule-t-il ?",
                            'options': None,
                            'reponse_correcte': '2',
                            'tolerances': ['2.0', '2,0'],
                            'explication': "$x_0 = -\\frac{12}{2(-3)} = 2$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Résoudre $x^2 - 2x - 8 > 0$. Donner la plus petite borne entière positive de l'ensemble des solutions.",
                            'options': None,
                            'reponse_correcte': '5',
                            'tolerances': [],
                            'explication': "Racines $-2$ et $4$. Solutions : $]-\\infty ; -2[ \\cup ]4 ; +\\infty[$. Le plus petit entier positif dans cet ensemble est 5.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Pour quelles valeurs de $x$ a-t-on $x^2 \\\\leq 4$ ? Donner la borne supérieure de l'intervalle solution.",
                            'options': None,
                            'reponse_correcte': '2',
                            'tolerances': ['2.0', '2,0'],
                            'explication': "$x^2 - 4 \\leq 0 \\Leftrightarrow (x-2)(x+2) \\leq 0$, soit $x \\in [-2 ; 2]$. La borne supérieure est 2.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },

    # ──────────────────────────────────────────────
    # CHAPITRE 2 — Suites numériques
    # ──────────────────────────────────────────────
    {
        'ordre': 2,
        'titre': 'Suites numériques',
        'description': "Définition, modes de génération, monotonie, suites arithmétiques, géométriques et récurrentes.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Définition, modes de génération et monotonie',
                'duree': 35,
                'contenu': """# Définition, modes de génération et monotonie des suites

## Qu'est-ce qu'une suite numérique ?

Une **suite numérique** est une fonction de $\\mathbb{N}$ (ou d'une partie de $\\mathbb{N}$) dans $\\mathbb{R}$. On note $(u_n)_{n \\in \\mathbb{N}}$ ou plus simplement $(u_n)$, et $u_n$ est appelé le **terme général** (ou terme de rang $n$).

**Exemples :**

- $u_n = 2n + 1$ : les termes sont $1, 3, 5, 7, \\ldots$ (nombres impairs)
- $u_n = \\frac{1}{n+1}$ : les termes sont $1, \\frac{1}{2}, \\frac{1}{3}, \\frac{1}{4}, \\ldots$

---

## Modes de génération

### Définition explicite

Le terme $u_n$ est donné **directement** en fonction de $n$ :

$$u_n = f(n)$$

**Exemple :** $u_n = n^2 - 3n + 2$. On peut calculer n'importe quel terme sans connaître les précédents : $u_{10} = 100 - 30 + 2 = 72$.

### Définition par récurrence

Le terme $u_{n+1}$ est exprimé en fonction du terme $u_n$ (et d'un ou plusieurs termes initiaux) :

$$\\begin{cases} u_0 = a \\text{ (terme initial)} \\\\ u_{n+1} = f(u_n) \\text{ pour tout } n \\in \\mathbb{N} \\end{cases}$$

**Exemple :** $u_0 = 3$ et $u_{n+1} = 2u_n - 1$.

- $u_0 = 3$
- $u_1 = 2 \\times 3 - 1 = 5$
- $u_2 = 2 \\times 5 - 1 = 9$
- $u_3 = 2 \\times 9 - 1 = 17$

> **Attention :** avec une définition par récurrence, pour calculer $u_{100}$, il faut calculer tous les termes intermédiaires.

---

## Représentation graphique

### Suite définie explicitement

On place les points de coordonnées $(n ; u_n)$ dans un repère. On obtient un **nuage de points** (pas une courbe continue, car $n$ est entier).

### Suite définie par récurrence (méthode de l'escalier / de la toile d'araignée)

Pour visualiser la suite $u_{n+1} = f(u_n)$ :

1. Tracer la courbe de $f$ et la droite $y = x$.
2. Partir du point $(u_0 ; 0)$, monter verticalement jusqu'à la courbe de $f$ → on lit $u_1 = f(u_0)$.
3. Aller horizontalement jusqu'à la droite $y = x$.
4. Recommencer : monter jusqu'à la courbe, aller jusqu'à la droite, etc.

---

## Monotonie d'une suite

### Définition

- $(u_n)$ est **croissante** si pour tout $n$ : $u_{n+1} \\geq u_n$.
- $(u_n)$ est **décroissante** si pour tout $n$ : $u_{n+1} \\leq u_n$.
- $(u_n)$ est **constante** si pour tout $n$ : $u_{n+1} = u_n$.
- $(u_n)$ est **monotone** si elle est croissante ou décroissante.

### Méthodes pour étudier la monotonie

**Méthode 1 — Signe de $u_{n+1} - u_n$ :**

Si $u_{n+1} - u_n > 0$ pour tout $n$, la suite est **strictement croissante**.

**Méthode 2 — Rapport $\\frac{u_{n+1}}{u_n}$ (si $u_n > 0$) :**

Si $\\frac{u_{n+1}}{u_n} > 1$ pour tout $n$, la suite est **strictement croissante**.

**Méthode 3 — Fonction associée :**

Si $u_n = f(n)$ et si $f$ est croissante sur $[0 ; +\\infty[$, alors la suite $(u_n)$ est croissante.

---

## Suites bornées

- $(u_n)$ est **majorée** s'il existe un réel $M$ tel que $u_n \\leq M$ pour tout $n$.
- $(u_n)$ est **minorée** s'il existe un réel $m$ tel que $u_n \\geq m$ pour tout $n$.
- $(u_n)$ est **bornée** si elle est à la fois majorée et minorée.

**Exemple :** $u_n = \\frac{n}{n+1}$

Pour tout $n \\geq 0$ : $0 \\leq u_n < 1$. La suite est bornée (minorée par 0, majorée par 1).

---

## À retenir

- Une suite peut être définie de manière **explicite** ($u_n = f(n)$) ou **par récurrence** ($u_{n+1} = g(u_n)$ avec $u_0$ donné).
- Pour la monotonie, on étudie le signe de $u_{n+1} - u_n$.
- Une suite est bornée si tous ses termes restent dans un intervalle $[m ; M]$.
""",
                'quiz': {
                    'titre': 'Quiz — Définition, modes de génération et monotonie',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Une suite numérique est une fonction de :",
                            'options': ["$\\\\mathbb{R}$ dans $\\\\mathbb{R}$", "$\\\\mathbb{N}$ dans $\\\\mathbb{R}$", "$\\\\mathbb{R}$ dans $\\\\mathbb{N}$", "$\\\\mathbb{Z}$ dans $\\\\mathbb{Z}$"],
                            'reponse_correcte': '1',
                            'explication': "Une suite est une fonction de $\\mathbb{N}$ (ou d'une partie) dans $\\mathbb{R}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "La suite $u_n = 2n + 1$ est définie de manière :",
                            'options': ["Récurrente", "Explicite", "Implicite", "Itérative"],
                            'reponse_correcte': '1',
                            'explication': "Le terme $u_n$ est donné directement en fonction de $n$ : c'est une définition explicite.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Si $u_0 = 3$ et $u_{n+1} = 2u_n - 1$, que vaut $u_1$ ?",
                            'options': ["$3$", "$5$", "$7$", "$4$"],
                            'reponse_correcte': '1',
                            'explication': "$u_1 = 2 \\times 3 - 1 = 5$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Pour montrer qu'une suite est strictement croissante, on montre que :",
                            'options': ["$u_{n+1} - u_n = 0$", "$u_{n+1} - u_n > 0$", "$u_{n+1} - u_n < 0$", "$u_{n+1} \\\\times u_n > 0$"],
                            'reponse_correcte': '1',
                            'explication': "Si $u_{n+1} - u_n > 0$ pour tout $n$, alors la suite est strictement croissante.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Si $u_n = n^2 - 3n + 2$, que vaut $u_0$ ?",
                            'options': ["$0$", "$2$", "$-1$", "$6$"],
                            'reponse_correcte': '1',
                            'explication': "$u_0 = 0 - 0 + 2 = 2$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "La suite $u_n = \\\\frac{n}{n+1}$ est majorée par :",
                            'options': ["$0$", "$1$", "$2$", "Elle n'est pas majorée"],
                            'reponse_correcte': '1',
                            'explication': "Pour tout $n \\geq 0$, $\\frac{n}{n+1} < 1$. La suite est majorée par 1.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "La représentation graphique d'une suite est :",
                            'options': ["Une courbe continue", "Un nuage de points", "Une droite", "Un histogramme"],
                            'reponse_correcte': '1',
                            'explication': "Comme $n$ est entier, on obtient un nuage de points $(n ; u_n)$ et non une courbe continue.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Avec la définition par récurrence $u_0 = 3$, $u_{n+1} = 2u_n - 1$, que vaut $u_2$ ?",
                            'options': ["$7$", "$9$", "$11$", "$5$"],
                            'reponse_correcte': '1',
                            'explication': "$u_1 = 5$, puis $u_2 = 2 \\times 5 - 1 = 9$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Si $u_n > 0$ pour tout $n$ et $\\\\frac{u_{n+1}}{u_n} > 1$, la suite est :",
                            'options': ["Décroissante", "Constante", "Strictement croissante", "Bornée"],
                            'reponse_correcte': '2',
                            'explication': "Si le rapport est $> 1$ avec des termes positifs, alors $u_{n+1} > u_n$ : la suite est strictement croissante.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "La suite $u_n = (-1)^n$ est :",
                            'options': ["Croissante", "Décroissante", "Monotone", "Ni croissante ni décroissante"],
                            'reponse_correcte': '3',
                            'explication': "$u_0 = 1, u_1 = -1, u_2 = 1, \\ldots$ Les termes alternent, la suite n'est pas monotone.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Si $f$ est décroissante sur $[0 ; +\\\\infty[$ et $u_n = f(n)$, alors $(u_n)$ est :",
                            'options': ["Croissante", "Décroissante", "Constante", "On ne peut pas conclure"],
                            'reponse_correcte': '1',
                            'explication': "Si la fonction associée est décroissante, la suite l'est aussi.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Quel inconvénient majeur a la définition par récurrence par rapport à la définition explicite ?",
                            'options': ["Elle est moins précise", "Elle nécessite de calculer tous les termes intermédiaires", "Elle ne permet pas de définir $u_0$", "Elle est toujours plus complexe à écrire"],
                            'reponse_correcte': '1',
                            'explication': "Pour calculer $u_{100}$ par récurrence, il faut calculer $u_1, u_2, \\ldots, u_{99}$ avant.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Une suite $(u_n)$ est bornée si :",
                            'options': ["Elle est croissante", "Elle est majorée et minorée", "Elle converge", "Elle est définie par récurrence"],
                            'reponse_correcte': '1',
                            'explication': "Une suite est bornée s'il existe $m$ et $M$ tels que $m \\leq u_n \\leq M$ pour tout $n$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "La suite $u_n = \\\\frac{1}{n+1}$ est décroissante.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$u_{n+1} - u_n = \\frac{1}{n+2} - \\frac{1}{n+1} = \\frac{-1}{(n+1)(n+2)} < 0$ : la suite est décroissante.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Une suite constante est à la fois croissante et décroissante.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Par définition, $u_{n+1} \\geq u_n$ et $u_{n+1} \\leq u_n$ si $u_{n+1} = u_n$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La suite $u_n = 2n + 1$ est bornée.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "$u_n = 2n + 1$ tend vers $+\\infty$ quand $n \\to +\\infty$ : elle n'est pas majorée, donc pas bornée.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Si $u_0 = 1$ et $u_{n+1} = u_n + 3$, que vaut $u_5$ ?",
                            'options': None,
                            'reponse_correcte': '16',
                            'tolerances': ['16.0', '16,0'],
                            'explication': "$u_1 = 4, u_2 = 7, u_3 = 10, u_4 = 13, u_5 = 16$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Si $u_n = n^2 - 3n + 2$, que vaut $u_{10}$ ?",
                            'options': None,
                            'reponse_correcte': '72',
                            'tolerances': ['72.0', '72,0'],
                            'explication': "$u_{10} = 100 - 30 + 2 = 72$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Calculer $u_3$ pour la suite définie par $u_0 = 3$ et $u_{n+1} = 2u_n - 1$.",
                            'options': None,
                            'reponse_correcte': '17',
                            'tolerances': ['17.0', '17,0'],
                            'explication': "$u_1 = 5, u_2 = 9, u_3 = 17$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "La suite $u_n = \\\\frac{n}{n+1}$ converge. Vers quelle valeur ? (nombre entier)",
                            'options': None,
                            'reponse_correcte': '1',
                            'tolerances': ['1.0', '1,0'],
                            'explication': "$\\lim_{n \\to +\\infty} \\frac{n}{n+1} = \\lim \\frac{1}{1 + 1/n} = 1$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Suites arithmétiques et géométriques',
                'duree': 40,
                'contenu': """# Suites arithmétiques et géométriques

## Les suites arithmétiques

### Définition

Une suite $(u_n)$ est **arithmétique** de raison $r$ si pour tout entier $n$ :

$$u_{n+1} = u_n + r$$

Chaque terme s'obtient en **ajoutant** la raison $r$ au terme précédent.

### Formule du terme général

$$u_n = u_0 + nr$$

Plus généralement, pour tout entier $p$ :

$$u_n = u_p + (n - p)r$$

### Sens de variation

- Si $r > 0$ : la suite est **strictement croissante**.
- Si $r < 0$ : la suite est **strictement décroissante**.
- Si $r = 0$ : la suite est **constante**.

### Somme des termes consécutifs

La somme des $(n+1)$ premiers termes (de $u_0$ à $u_n$) est :

$$S_n = u_0 + u_1 + \\cdots + u_n = (n+1) \\times \\frac{u_0 + u_n}{2}$$

> **Moyen mnémotechnique :** nombre de termes × moyenne du premier et du dernier terme.

**Cas particulier — Somme des $n$ premiers entiers :**

$$1 + 2 + 3 + \\cdots + n = \\frac{n(n+1)}{2}$$

---

### Exemple

Soit $(u_n)$ la suite arithmétique de premier terme $u_0 = 3$ et de raison $r = 4$.

- $u_n = 3 + 4n$
- $u_{10} = 3 + 40 = 43$
- $S_{10} = 11 \\times \\frac{3 + 43}{2} = 11 \\times 23 = 253$

---

## Les suites géométriques

### Définition

Une suite $(u_n)$ est **géométrique** de raison $q$ si pour tout entier $n$ :

$$u_{n+1} = q \\cdot u_n$$

Chaque terme s'obtient en **multipliant** le terme précédent par la raison $q$.

### Formule du terme général

$$u_n = u_0 \\cdot q^n$$

Plus généralement, pour tout entier $p$ :

$$u_n = u_p \\cdot q^{n-p}$$

### Sens de variation (pour $u_0 > 0$)

| Condition | Variation |
|---|---|
| $q > 1$ | Strictement croissante |
| $0 < q < 1$ | Strictement décroissante |
| $q = 1$ | Constante |
| $q < 0$ | Ni croissante ni décroissante (termes alternés) |

### Somme des termes consécutifs

Pour $q \\neq 1$, la somme des $(n+1)$ premiers termes est :

$$S_n = u_0 + u_1 + \\cdots + u_n = u_0 \\cdot \\frac{1 - q^{n+1}}{1 - q}$$

**Cas particulier :**

$$1 + q + q^2 + \\cdots + q^n = \\frac{1 - q^{n+1}}{1 - q}$$

---

### Exemple

Soit $(u_n)$ la suite géométrique de premier terme $u_0 = 5$ et de raison $q = 2$.

- $u_n = 5 \\times 2^n$
- $u_6 = 5 \\times 64 = 320$
- $S_6 = 5 \\times \\frac{1 - 2^7}{1 - 2} = 5 \\times \\frac{-127}{-1} = 635$

---

## Comment reconnaître le type d'une suite ?

| Test | Suite arithmétique | Suite géométrique |
|------|-------------------|-------------------|
| Critère | $u_{n+1} - u_n = r$ (constant) | $\\frac{u_{n+1}}{u_n} = q$ (constant, $u_n \\neq 0$) |
| Représentation | Points alignés | Croissance/décroissance exponentielle |
| Formule explicite | $u_n = u_0 + nr$ (linéaire en $n$) | $u_n = u_0 q^n$ (exponentielle en $n$) |

---

## Modélisation

- **Suite arithmétique** : situation d'augmentation (ou diminution) d'une quantité **fixe** à chaque étape. Exemples : salaire augmenté de 50 € par mois, nombre de pages lues chaque jour constant.

- **Suite géométrique** : situation de croissance (ou décroissance) **proportionnelle**. Exemples : population doublant chaque génération, capital augmentant d'un taux fixe, désintégration radioactive.

---

## À retenir

- **Arithmétique** : $u_{n+1} = u_n + r$, terme général $u_n = u_0 + nr$, somme $(n+1)\\frac{u_0+u_n}{2}$.
- **Géométrique** : $u_{n+1} = q \\cdot u_n$, terme général $u_n = u_0 q^n$, somme $u_0 \\frac{1 - q^{n+1}}{1-q}$.
- Les sommes de termes sont des formules à connaître par cœur.
""",
                'quiz': {
                    'titre': 'Quiz — Suites arithmétiques et géométriques',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Une suite arithmétique de raison $r$ vérifie pour tout $n$ :",
                            'options': ["$u_{n+1} = u_n \\\\times r$", "$u_{n+1} = u_n + r$", "$u_{n+1} = u_n - r$", "$u_{n+1} = r^n$"],
                            'reponse_correcte': '1',
                            'explication': "Par définition, une suite arithmétique vérifie $u_{n+1} = u_n + r$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Le terme général d'une suite arithmétique de premier terme $u_0$ et de raison $r$ est :",
                            'options': ["$u_n = u_0 \\\\cdot r^n$", "$u_n = u_0 + nr$", "$u_n = u_0 + r^n$", "$u_n = n \\\\cdot u_0 + r$"],
                            'reponse_correcte': '1',
                            'explication': "$u_n = u_0 + nr$ est la formule du terme général d'une suite arithmétique.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "La suite arithmétique $u_0 = 3$, $r = 4$ a pour $u_{10}$ :",
                            'options': ["$43$", "$40$", "$34$", "$47$"],
                            'reponse_correcte': '0',
                            'explication': "$u_{10} = 3 + 10 \\times 4 = 43$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Le terme général d'une suite géométrique de premier terme $u_0$ et de raison $q$ est :",
                            'options': ["$u_n = u_0 + nq$", "$u_n = u_0 \\\\cdot q^n$", "$u_n = n \\\\cdot q^{u_0}$", "$u_n = u_0^n \\\\cdot q$"],
                            'reponse_correcte': '1',
                            'explication': "$u_n = u_0 \\cdot q^n$ est la formule du terme général d'une suite géométrique.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Si $(u_n)$ est arithmétique avec $r > 0$, la suite est :",
                            'options': ["Décroissante", "Constante", "Strictement croissante", "Ni croissante ni décroissante"],
                            'reponse_correcte': '2',
                            'explication': "Si la raison $r$ est strictement positive, chaque terme est plus grand que le précédent.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "La somme $1 + 2 + 3 + \\\\cdots + n$ vaut :",
                            'options': ["$n^2$", "$\\\\frac{n(n-1)}{2}$", "$\\\\frac{n(n+1)}{2}$", "$n(n+1)$"],
                            'reponse_correcte': '2',
                            'explication': "C'est la formule classique : $\\sum_{k=1}^{n} k = \\frac{n(n+1)}{2}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "La suite géométrique $u_0 = 5$, $q = 2$ a pour $u_6$ :",
                            'options': ["$320$", "$640$", "$160$", "$64$"],
                            'reponse_correcte': '0',
                            'explication': "$u_6 = 5 \\times 2^6 = 5 \\times 64 = 320$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "La somme des $n+1$ premiers termes d'une suite géométrique de raison $q \\\\neq 1$ est :",
                            'options': ["$u_0 \\\\cdot \\\\frac{q^{n+1} - 1}{q - 1}$", "$u_0 \\\\cdot \\\\frac{1 - q^{n+1}}{1 - q}$", "$(n+1) \\\\cdot \\\\frac{u_0 + u_n}{2}$", "$u_0 \\\\cdot q^{n+1}$"],
                            'reponse_correcte': '1',
                            'explication': "La somme est $S_n = u_0 \\cdot \\frac{1 - q^{n+1}}{1 - q}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Pour reconnaître une suite arithmétique, on vérifie que :",
                            'options': ["$\\\\frac{u_{n+1}}{u_n}$ est constant", "$u_{n+1} - u_n$ est constant", "$u_n \\\\cdot u_{n+1}$ est constant", "$u_{n+1} + u_n$ est constant"],
                            'reponse_correcte': '1',
                            'explication': "La différence entre deux termes consécutifs est constante et vaut $r$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Si $(u_n)$ est géométrique avec $u_0 > 0$ et $0 < q < 1$, la suite est :",
                            'options': ["Strictement croissante", "Strictement décroissante", "Constante", "Alternée"],
                            'reponse_correcte': '1',
                            'explication': "Avec $u_0 > 0$ et $0 < q < 1$, chaque terme est multiplié par un facteur $<1$ : la suite décroît.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Un capital augmente de 5% par an. Son évolution est modélisée par une suite :",
                            'options': ["Arithmétique de raison 0,05", "Géométrique de raison 1,05", "Géométrique de raison 0,05", "Arithmétique de raison 1,05"],
                            'reponse_correcte': '1',
                            'explication': "Augmenter de 5% revient à multiplier par 1,05 à chaque étape : c'est une suite géométrique de raison 1,05.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "La somme $S_{10} = u_0 + u_1 + \\\\cdots + u_{10}$ pour la suite arithmétique $u_0 = 3$, $r = 4$ vaut :",
                            'options': ["$253$", "$230$", "$220$", "$260$"],
                            'reponse_correcte': '0',
                            'explication': "$u_{10} = 43$, $S_{10} = 11 \\times \\frac{3 + 43}{2} = 11 \\times 23 = 253$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "La formule de la somme d'une suite arithmétique $(n+1) \\\\times \\\\frac{u_0 + u_n}{2}$ correspond à :",
                            'options': ["Nombre de termes × premier terme", "Nombre de termes × moyenne du premier et du dernier", "$(n+1) \\\\times$ raison", "Premier terme × dernier terme"],
                            'reponse_correcte': '1',
                            'explication': "C'est le nombre de termes multiplié par la moyenne arithmétique du premier et du dernier terme.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "La suite $u_n = 3 \\\\times 2^n$ est une suite géométrique de raison 2.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$u_{n+1} = 3 \\times 2^{n+1} = 2 \\times (3 \\times 2^n) = 2u_n$. C'est géométrique de raison 2.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Si $q < 0$, une suite géométrique est alternée (termes positifs et négatifs).",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Un facteur $q < 0$ change le signe à chaque multiplication, d'où des termes alternés.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La suite $u_n = 5n + 2$ est géométrique.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "$u_n = 5n + 2$ est linéaire en $n$ : c'est une suite arithmétique de raison 5, pas géométrique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Calculer la somme $1 + 2 + 3 + \\\\cdots + 100$.",
                            'options': None,
                            'reponse_correcte': '5050',
                            'tolerances': ['5050.0', '5050,0'],
                            'explication': "$S = \\frac{100 \\times 101}{2} = 5050$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Soit $(u_n)$ arithmétique avec $u_0 = 7$ et $r = -3$. Que vaut $u_8$ ?",
                            'options': None,
                            'reponse_correcte': '-17',
                            'tolerances': ['-17.0', '-17,0'],
                            'explication': "$u_8 = 7 + 8 \\times (-3) = 7 - 24 = -17$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Soit $(u_n)$ géométrique avec $u_0 = 3$ et $q = 3$. Que vaut $u_4$ ?",
                            'options': None,
                            'reponse_correcte': '243',
                            'tolerances': ['243.0', '243,0'],
                            'explication': "$u_4 = 3 \\times 3^4 = 3 \\times 81 = 243$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Calculer la somme $S_6 = u_0 + u_1 + \\\\cdots + u_6$ pour la suite géométrique $u_0 = 5$, $q = 2$.",
                            'options': None,
                            'reponse_correcte': '635',
                            'tolerances': ['635.0', '635,0'],
                            'explication': "$S_6 = 5 \\times \\frac{1 - 2^7}{1 - 2} = 5 \\times \\frac{-127}{-1} = 635$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 3,
                'titre': 'Suites récurrentes et suite de Fibonacci',
                'duree': 35,
                'contenu': """# Suites récurrentes et suite de Fibonacci

## Suites arithmético-géométriques

### Définition

Une suite **arithmético-géométrique** est définie par une relation de la forme :

$$u_{n+1} = au_n + b \\qquad (a \\neq 0,\\; a \\neq 1,\\; b \\neq 0)$$

avec un terme initial $u_0$ donné.

> C'est un mélange de suite arithmétique (le « $+ b$ ») et géométrique (le « $a \\times$ »).

### Recherche du point fixe

On cherche la valeur $\\ell$ telle que $\\ell = a\\ell + b$, c'est-à-dire :

$$\\ell = \\frac{b}{1-a}$$

### Suite auxiliaire géométrique

On pose $v_n = u_n - \\ell$. Alors :

$$v_{n+1} = u_{n+1} - \\ell = (au_n + b) - \\ell = a(u_n - \\ell) = a \\cdot v_n$$

La suite $(v_n)$ est **géométrique** de raison $a$ et de premier terme $v_0 = u_0 - \\ell$.

Donc :

$$v_n = (u_0 - \\ell) \\cdot a^n$$

Et finalement :

$$u_n = \\ell + (u_0 - \\ell) \\cdot a^n$$

---

### Exemple

Soit $u_0 = 10$ et $u_{n+1} = 0{,}5 u_n + 3$.

- Point fixe : $\\ell = \\frac{3}{1-0{,}5} = 6$
- $v_n = u_n - 6$, $v_0 = 4$, $v_{n+1} = 0{,}5 v_n$ → suite géométrique de raison $0{,}5$
- $v_n = 4 \\times 0{,}5^n$
- $u_n = 6 + 4 \\times 0{,}5^n$

On vérifie : $u_0 = 6 + 4 = 10$ ✓, $u_1 = 6 + 2 = 8$ ✓ (car $0{,}5 \\times 10 + 3 = 8$).

Comme $0 < 0{,}5 < 1$, la suite $(u_n)$ **converge** vers $\\ell = 6$.

---

## La suite de Fibonacci

### Définition

La suite de Fibonacci $(F_n)$ est définie par :

$$\\begin{cases} F_0 = 1,\\; F_1 = 1 \\\\ F_{n+2} = F_{n+1} + F_n \\text{ pour tout } n \\geq 0 \\end{cases}$$

Les premiers termes sont :

$$1,\\; 1,\\; 2,\\; 3,\\; 5,\\; 8,\\; 13,\\; 21,\\; 34,\\; 55,\\; 89,\\; 144,\\; \\ldots$$

> Chaque terme est la **somme des deux précédents**.

### Le nombre d'or

En calculant les rapports successifs $\\frac{F_{n+1}}{F_n}$, on constate qu'ils se rapprochent d'une constante, le **nombre d'or** :

$$\\varphi = \\frac{1 + \\sqrt{5}}{2} \\approx 1{,}618$$

Le nombre d'or vérifie l'équation $\\varphi^2 = \\varphi + 1$, soit $\\varphi^2 - \\varphi - 1 = 0$.

### Formule de Binet

Il existe une formule explicite (admise en Première) :

$$F_n = \\frac{\\varphi^n - \\psi^n}{\\sqrt{5}}$$

où $\\psi = \\frac{1 - \\sqrt{5}}{2} \\approx -0{,}618$ est l'autre racine de $x^2 - x - 1 = 0$.

### Fibonacci dans la nature

La suite de Fibonacci apparaît dans de nombreux phénomènes naturels :

- Le nombre de pétales de certaines fleurs (3, 5, 8, 13, 21…)
- La disposition des graines dans un tournesol (spirales en nombres de Fibonacci)
- La croissance de la population de lapins (modèle idéalisé)
- La disposition des feuilles sur une tige (phyllotaxie)

---

## Calcul algorithmique des termes d'une suite récurrente

Pour calculer les termes d'une suite définie par récurrence, on utilise une **boucle** :

```
Algorithme : calcul de u_n
Entrée : u_0, n
u ← u_0
Pour k allant de 1 à n :
    u ← f(u)    // f est la relation de récurrence
Afficher u
```

**Remarque :** cet algorithme s'applique quelle que soit la relation de récurrence (arithmético-géométrique, Fibonacci en adaptant pour deux termes, etc.).

---

## À retenir

- Une suite arithmético-géométrique $u_{n+1} = au_n + b$ se résout en trouvant le **point fixe** $\\ell = \\frac{b}{1-a}$ et en posant $v_n = u_n - \\ell$.
- La **suite de Fibonacci** : $F_{n+2} = F_{n+1} + F_n$. Les rapports successifs tendent vers le **nombre d'or** $\\varphi \\approx 1{,}618$.
- Les suites récurrentes se calculent efficacement par **algorithme itératif**.
""",
                'quiz': {
                    'titre': 'Quiz — Suites récurrentes et suite de Fibonacci',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Une suite arithmético-géométrique est de la forme $u_{n+1} = au_n + b$. Quel est le point fixe $\\\\ell$ ?",
                            'options': ["$\\\\ell = \\\\frac{a}{1-b}$", "$\\\\ell = \\\\frac{b}{1-a}$", "$\\\\ell = \\\\frac{1-a}{b}$", "$\\\\ell = ab$"],
                            'reponse_correcte': '1',
                            'explication': "Le point fixe vérifie $\\ell = a\\ell + b$, d'où $\\ell(1-a) = b$ et $\\ell = \\frac{b}{1-a}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Si $u_{n+1} = 0{,}5 u_n + 3$, le point fixe est :",
                            'options': ["$3$", "$6$", "$1{,}5$", "$0{,}5$"],
                            'reponse_correcte': '1',
                            'explication': "$\\ell = \\frac{3}{1-0{,}5} = \\frac{3}{0{,}5} = 6$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Les deux premiers termes de la suite de Fibonacci sont :",
                            'options': ["$F_0 = 0$ et $F_1 = 1$", "$F_0 = 1$ et $F_1 = 1$", "$F_0 = 1$ et $F_1 = 2$", "$F_0 = 0$ et $F_1 = 0$"],
                            'reponse_correcte': '1',
                            'explication': "Dans le cours, $F_0 = 1$ et $F_1 = 1$ (convention utilisée ici).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "La relation de récurrence de la suite de Fibonacci est :",
                            'options': ["$F_{n+2} = F_{n+1} \\\\times F_n$", "$F_{n+2} = F_{n+1} + F_n$", "$F_{n+2} = 2F_{n+1} - F_n$", "$F_{n+2} = F_{n+1} - F_n$"],
                            'reponse_correcte': '1',
                            'explication': "Chaque terme de Fibonacci est la somme des deux précédents.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Le nombre d'or $\\\\varphi$ vaut approximativement :",
                            'options': ["$2{,}718$", "$3{,}14$", "$1{,}618$", "$1{,}414$"],
                            'reponse_correcte': '2',
                            'explication': "$\\varphi = \\frac{1 + \\sqrt{5}}{2} \\approx 1{,}618$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "L'équation vérifiée par le nombre d'or est :",
                            'options': ["$\\\\varphi^2 = 2\\\\varphi$", "$\\\\varphi^2 = \\\\varphi + 1$", "$\\\\varphi^2 = \\\\varphi - 1$", "$\\\\varphi^2 + \\\\varphi = 1$"],
                            'reponse_correcte': '1',
                            'explication': "Le nombre d'or vérifie $\\varphi^2 - \\varphi - 1 = 0$, soit $\\varphi^2 = \\varphi + 1$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Pour résoudre $u_{n+1} = au_n + b$, on pose $v_n = u_n - \\\\ell$. La suite $(v_n)$ est alors :",
                            'options': ["Arithmétique de raison $b$", "Géométrique de raison $a$", "Constante", "De Fibonacci"],
                            'reponse_correcte': '1',
                            'explication': "$v_{n+1} = a(u_n - \\ell) = a \\cdot v_n$ : la suite $(v_n)$ est géométrique de raison $a$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Le terme explicite d'une suite arithmético-géométrique est $u_n = \\\\ell + (u_0 - \\\\ell) \\\\cdot a^n$. Si $|a| < 1$, la suite :",
                            'options': ["Diverge vers $+\\\\infty$", "Diverge vers $-\\\\infty$", "Converge vers $\\\\ell$", "Oscille indéfiniment"],
                            'reponse_correcte': '2',
                            'explication': "Si $|a| < 1$, $a^n \\to 0$ et $u_n \\to \\ell$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Si $u_0 = 10$ et $u_{n+1} = 0{,}5u_n + 3$, alors $u_n = 6 + 4 \\\\times 0{,}5^n$. Que vaut $u_2$ ?",
                            'options': ["$7$", "$7{,}5$", "$8$", "$6{,}5$"],
                            'reponse_correcte': '0',
                            'explication': "$u_2 = 6 + 4 \\times 0{,}25 = 6 + 1 = 7$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Les rapports successifs $\\\\frac{F_{n+1}}{F_n}$ de la suite de Fibonacci tendent vers :",
                            'options': ["$1$", "$2$", "$\\\\varphi \\\\approx 1{,}618$", "$\\\\pi$"],
                            'reponse_correcte': '2',
                            'explication': "Les rapports convergent vers le nombre d'or $\\varphi = \\frac{1 + \\sqrt{5}}{2}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Quel est $F_7$ dans la suite de Fibonacci ($F_0 = F_1 = 1$) ?",
                            'options': ["$13$", "$21$", "$34$", "$8$"],
                            'reponse_correcte': '1',
                            'explication': "$F_2=2, F_3=3, F_4=5, F_5=8, F_6=13, F_7=21$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Pour calculer les termes d'une suite récurrente par algorithme, on utilise :",
                            'options': ["Une boucle for", "Un système d'équations", "Une intégrale", "Le théorème de Pythagore"],
                            'reponse_correcte': '0',
                            'explication': "On utilise une boucle itérative qui applique la relation de récurrence.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "La formule de Binet utilise deux racines de l'équation :",
                            'options': ["$x^2 + x - 1 = 0$", "$x^2 - x - 1 = 0$", "$x^2 - x + 1 = 0$", "$x^2 + x + 1 = 0$"],
                            'reponse_correcte': '1',
                            'explication': "Le nombre d'or $\\varphi$ et $\\psi$ sont les racines de $x^2 - x - 1 = 0$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "La suite de Fibonacci apparaît dans le nombre de pétales de certaines fleurs.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Lys (3 pétales), boutons d'or (5), marguerites (13 ou 21) : ce sont des nombres de Fibonacci.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Pour la suite $u_{n+1} = 3u_n + 6$, le point fixe est $\\\\ell = -3$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$\\ell = \\frac{6}{1-3} = \\frac{6}{-2} = -3$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Si $|a| > 1$ dans $u_{n+1} = au_n + b$, la suite converge toujours.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Si $|a| > 1$, $a^n$ diverge, donc $(u_n)$ diverge (sauf si $u_0 = \\ell$).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Calculer le point fixe de la suite $u_{n+1} = 0{,}8u_n + 4$.",
                            'options': None,
                            'reponse_correcte': '20',
                            'tolerances': ['20.0', '20,0'],
                            'explication': "$\\ell = \\frac{4}{1 - 0{,}8} = \\frac{4}{0{,}2} = 20$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quel est le 8e terme de la suite de Fibonacci ($F_0 = F_1 = 1$) ? Donner $F_8$.",
                            'options': None,
                            'reponse_correcte': '34',
                            'tolerances': ['34.0', '34,0'],
                            'explication': "$F_2=2, F_3=3, F_4=5, F_5=8, F_6=13, F_7=21, F_8=34$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Si $u_0 = 10$ et $u_{n+1} = 0{,}5u_n + 3$, vers quelle valeur la suite converge-t-elle ?",
                            'options': None,
                            'reponse_correcte': '6',
                            'tolerances': ['6.0', '6,0'],
                            'explication': "Le point fixe $\\ell = \\frac{3}{0{,}5} = 6$. Comme $|0{,}5| < 1$, la suite converge vers 6.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Pour $u_0 = 100$ et $u_{n+1} = 0{,}8u_n + 4$, donner l'expression de $u_n$ sous la forme $\\\\ell + c \\\\times a^n$. Quelle est la valeur de $c$ ?",
                            'options': None,
                            'reponse_correcte': '80',
                            'tolerances': ['80.0', '80,0'],
                            'explication': "$\\ell = 20$, $v_0 = u_0 - \\ell = 80$, $u_n = 20 + 80 \\times 0{,}8^n$. Donc $c = 80$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },

    # ──────────────────────────────────────────────
    # CHAPITRE 3 — Dérivation
    # ──────────────────────────────────────────────
    {
        'ordre': 3,
        'titre': 'Dérivation',
        'description': "Nombre dérivé, fonction dérivée, règles de dérivation et applications à l'étude de fonctions.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Nombre dérivé et tangente',
                'duree': 35,
                'contenu': """# Nombre dérivé et tangente

## Introduction — Le problème de la tangente

Comment mesurer la « vitesse de variation » d'une fonction en un point ? Comment tracer la **tangente** à une courbe ?

Ces deux questions fondamentales sont à l'origine du concept de **dérivée**, l'un des outils les plus puissants de l'analyse mathématique.

---

## Taux de variation

### Définition

Soit $f$ une fonction définie sur un intervalle $I$ et soient $a$ et $a+h$ deux points de $I$ (avec $h \\neq 0$).

Le **taux de variation** de $f$ entre $a$ et $a+h$ est :

$$\\tau(h) = \\frac{f(a+h) - f(a)}{h}$$

Géométriquement, c'est la **pente de la sécante** passant par les points $A(a ; f(a))$ et $B(a+h ; f(a+h))$.

---

## Nombre dérivé

### Définition

Si le taux de variation $\\frac{f(a+h)-f(a)}{h}$ admet une **limite finie** quand $h$ tend vers $0$, on dit que $f$ est **dérivable en $a$** et on note cette limite :

$$f'(a) = \\lim_{h \\to 0} \\frac{f(a+h) - f(a)}{h}$$

$f'(a)$ est le **nombre dérivé** de $f$ en $a$.

### Interprétation géométrique

$f'(a)$ est la **pente de la tangente** à la courbe de $f$ au point $A(a ; f(a))$.

Quand $h \\to 0$, la sécante « pivote » vers la tangente, et sa pente tend vers $f'(a)$.

### Interprétation cinématique

Si $f(t)$ représente la position d'un mobile à l'instant $t$, alors $f'(t)$ est sa **vitesse instantanée**.

---

## Équation de la tangente

L'équation de la **tangente** à la courbe de $f$ au point d'abscisse $a$ est :

$$\\boxed{y = f'(a)(x - a) + f(a)}$$

C'est l'équation d'une droite de pente $f'(a)$ passant par le point $(a ; f(a))$.

---

## Exemples de calcul du nombre dérivé

### Exemple 1 : $f(x) = x^2$ en $a = 3$

$$\\frac{f(3+h)-f(3)}{h} = \\frac{(3+h)^2 - 9}{h} = \\frac{9 + 6h + h^2 - 9}{h} = \\frac{6h + h^2}{h} = 6 + h$$

Pour $h \\to 0$ : $f'(3) = 6$.

La tangente en $(3 ; 9)$ a pour équation : $y = 6(x-3) + 9 = 6x - 9$.

### Exemple 2 : $f(x) = \\frac{1}{x}$ en $a = 2$

$$\\frac{f(2+h)-f(2)}{h} = \\frac{\\frac{1}{2+h} - \\frac{1}{2}}{h} = \\frac{2-(2+h)}{h \\cdot 2(2+h)} = \\frac{-1}{2(2+h)}$$

Pour $h \\to 0$ : $f'(2) = -\\frac{1}{4}$.

La tangente en $\\left(2 ; \\frac{1}{2}\\right)$ a pour équation : $y = -\\frac{1}{4}(x-2) + \\frac{1}{2} = -\\frac{1}{4}x + 1$.

---

## Dérivabilité et continuité

> **Propriété :** si $f$ est dérivable en $a$, alors $f$ est **continue** en $a$. La réciproque est fausse.

**Contre-exemple :** la fonction valeur absolue $f(x) = |x|$ est continue en $0$ mais **pas dérivable** en $0$ (la courbe présente un « angle »).

---

## À retenir

- Le **nombre dérivé** $f'(a) = \\lim_{h \\to 0} \\frac{f(a+h)-f(a)}{h}$ mesure la pente de la tangente.
- L'**équation de la tangente** en $a$ est $y = f'(a)(x-a)+f(a)$.
- Dérivable ⟹ continue, mais la réciproque est fausse.
""",
                'quiz': {
                    'titre': 'Quiz — Nombre dérivé et tangente',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quelle est la formule du taux de variation de $f$ entre $a$ et $a+h$ ?",
                            'options': ["$\\\\frac{f(a+h) + f(a)}{h}$", "$\\\\frac{f(a+h) - f(a)}{h}$", "$\\\\frac{f(a) - f(a+h)}{a}$", "$f(a+h) \\\\times h$"],
                            'reponse_correcte': '1',
                            'explication': "Le taux de variation est $\\frac{f(a+h)-f(a)}{h}$, pente de la sécante.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Le nombre dérivé $f'(a)$ est défini comme :",
                            'options': ["$\\\\lim_{h \\\\to 0} \\\\frac{f(a+h) - f(a)}{h}$", "$\\\\lim_{h \\\\to 0} \\\\frac{f(a) - f(h)}{a}$", "$\\\\frac{f(a+1) - f(a)}{1}$", "$f(a) \\\\times a$"],
                            'reponse_correcte': '0',
                            'explication': "Le nombre dérivé est la limite du taux de variation quand $h$ tend vers 0.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Géométriquement, $f'(a)$ représente :",
                            'options': ["L'aire sous la courbe en $a$", "La pente de la tangente à la courbe en $a$", "L'ordonnée du point d'abscisse $a$", "La distance entre deux points de la courbe"],
                            'reponse_correcte': '1',
                            'explication': "Le nombre dérivé $f'(a)$ est la pente de la tangente à la courbe au point d'abscisse $a$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "L'équation de la tangente à la courbe de $f$ au point d'abscisse $a$ est :",
                            'options': ["$y = f(a)(x - a) + f'(a)$", "$y = f'(a)(x - a) + f(a)$", "$y = f(a) \\\\cdot x + f'(a)$", "$y = f'(a) \\\\cdot x$"],
                            'reponse_correcte': '1',
                            'explication': "L'équation de la tangente est $y = f'(a)(x-a) + f(a)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'vrai_faux',
                            'texte': "Si $f$ est dérivable en $a$, alors $f$ est continue en $a$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "La dérivabilité en un point implique la continuité en ce point.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'vrai_faux',
                            'texte': "La fonction $f(x) = |x|$ est dérivable en $0$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La fonction valeur absolue présente un angle en 0 et n'y est pas dérivable.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Si $f(t)$ représente la position d'un mobile, que représente $f'(t)$ ?",
                            'options': ["L'accélération", "La vitesse instantanée", "La position moyenne", "La distance parcourue"],
                            'reponse_correcte': '1',
                            'explication': "Si $f(t)$ est la position, $f'(t)$ est la vitesse instantanée du mobile.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "La tangente à la courbe de $f$ en $(a ; f(a))$ passe par le point :",
                            'options': ["$(0 ; 0)$", "$(a ; f(a))$", "$(a ; 0)$", "$(0 ; f(a))$"],
                            'reponse_correcte': '1',
                            'explication': "La tangente passe toujours par le point de tangence $(a ; f(a))$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Soit $f(x) = x^2$. Que vaut $f'(3)$ ?",
                            'options': ["$3$", "$9$", "$6$", "$2$"],
                            'reponse_correcte': '2',
                            'explication': "Le taux de variation donne $\\frac{(3+h)^2 - 9}{h} = 6+h \\to 6$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quelle est l'équation de la tangente à $f(x) = x^2$ au point d'abscisse $3$ ?",
                            'options': ["$y = 6x - 9$", "$y = 6x + 9$", "$y = 3x - 9$", "$y = 9x - 6$"],
                            'reponse_correcte': '0',
                            'explication': "$f'(3)=6$ et $f(3)=9$, donc $y = 6(x-3)+9 = 6x-9$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Quel est le taux de variation de $f(x) = x^3$ entre $1$ et $1+h$ ?",
                            'options': ["$3 + 3h + h^2$", "$3h + h^2$", "$1 + 3h$", "$3 + h$"],
                            'reponse_correcte': '0',
                            'explication': "$\\frac{(1+h)^3 - 1}{h} = \\frac{3h+3h^2+h^3}{h} = 3+3h+h^2$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Soit $f(x) = \\\\frac{1}{x}$. Que vaut $f'(2)$ ?",
                            'options': ["$\\\\frac{1}{4}$", "$-\\\\frac{1}{2}$", "$-\\\\frac{1}{4}$", "$\\\\frac{1}{2}$"],
                            'reponse_correcte': '2',
                            'explication': "$\\frac{\\frac{1}{2+h}-\\frac{1}{2}}{h} = \\frac{-1}{2(2+h)} \\to -\\frac{1}{4}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'vrai_faux',
                            'texte': "Si $f$ est continue en $a$, alors $f$ est nécessairement dérivable en $a$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Continuité n'implique pas dérivabilité. Contre-exemple : $|x|$ en 0.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Soit $f(x) = x^2 - 3x + 2$. Quelle est l'équation de la tangente en $x = 1$ ?",
                            'options': ["$y = -x + 1$", "$y = -x$", "$y = x - 1$", "$y = -x + 2$"],
                            'reponse_correcte': '0',
                            'explication': "$f(1)=0$, $f'(x)=2x-3$ donc $f'(1)=-1$. Tangente : $y=-(x-1)+0=-x+1$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Le taux de variation de $f$ entre $a$ et $b$ est la pente de la sécante passant par $(a;f(a))$ et $(b;f(b))$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Le taux de variation $\\frac{f(b)-f(a)}{b-a}$ est bien la pente de la sécante.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'texte_libre',
                            'texte': "Calculer le nombre dérivé de $f(x) = 3x^2$ en $a = 2$.",
                            'options': None,
                            'reponse_correcte': '12',
                            'tolerances': ['12.0', '12,0'],
                            'explication': "$\\frac{3(2+h)^2 - 12}{h} = \\frac{12h+3h^2}{h} = 12+3h \\to 12$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Soit $f(x) = x^2 + 1$. Donner l'équation de la tangente en $x = 2$ sous la forme $y = ax + b$.",
                            'options': None,
                            'reponse_correcte': 'y = 4x - 3',
                            'tolerances': ['y=4x-3', 'y = 4x-3', 'y=4x - 3', '4x - 3', '4x-3'],
                            'explication': "$f(2)=5$, $f'(x)=2x$ donc $f'(2)=4$. Tangente : $y=4(x-2)+5=4x-3$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'qcm',
                            'texte': "Soit $f(x) = \\\\sqrt{x}$. Quelle est l'équation de la tangente en $x = 4$ ?",
                            'options': ["$y = \\\\frac{1}{4}x + 1$", "$y = \\\\frac{1}{2}x$", "$y = \\\\frac{1}{4}x + \\\\frac{3}{2}$", "$y = 4x - 14$"],
                            'reponse_correcte': '0',
                            'explication': "$f(4)=2$, $f'(x)=\\frac{1}{2\\sqrt{x}}$ donc $f'(4)=\\frac{1}{4}$. Tangente : $y=\\frac{1}{4}(x-4)+2=\\frac{1}{4}x+1$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'vrai_faux',
                            'texte': "Quand $h$ tend vers $0$, la sécante tend vers la tangente.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "La tangente est la position limite de la sécante quand $h \\to 0$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Calculer $f'(1)$ pour $f(x) = \\\\frac{1}{x}$ en utilisant la définition du nombre dérivé. Donner la réponse sous forme de fraction.",
                            'options': None,
                            'reponse_correcte': '-1',
                            'tolerances': ['-1.0', '-1,0'],
                            'explication': "$\\frac{\\frac{1}{1+h}-1}{h} = \\frac{1-(1+h)}{h(1+h)} = \\frac{-1}{1+h} \\to -1$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Dérivées usuelles et règles de dérivation',
                'duree': 40,
                'contenu': """# Dérivées usuelles et règles de dérivation

## Tableau des dérivées usuelles

Les résultats suivants sont à connaître **par cœur** :

| Fonction $f(x)$ | Ensemble de dérivabilité | Dérivée $f'(x)$ |
|---|---|---|
| $k$ (constante) | $\\mathbb{R}$ | $0$ |
| $x$ | $\\mathbb{R}$ | $1$ |
| $x^2$ | $\\mathbb{R}$ | $2x$ |
| $x^3$ | $\\mathbb{R}$ | $3x^2$ |
| $x^n$ ($n \\in \\mathbb{N}^*$) | $\\mathbb{R}$ | $nx^{n-1}$ |
| $\\frac{1}{x}$ | $\\mathbb{R}^*$ | $-\\frac{1}{x^2}$ |
| $\\sqrt{x}$ | $]0 ; +\\infty[$ | $\\frac{1}{2\\sqrt{x}}$ |

---

## Opérations sur les dérivées

### Somme

$$(u + v)' = u' + v'$$

### Multiplication par un scalaire

$$(ku)' = ku' \\qquad (k \\in \\mathbb{R})$$

### Produit

$$(uv)' = u'v + uv'$$

> **Moyen mnémotechnique :** « la dérivée du premier fois le second, plus le premier fois la dérivée du second ».

### Quotient

$$\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2} \\qquad (v \\neq 0)$$

---

## Exemples d'application

### Exemple 1 : dérivée d'un polynôme

Soit $f(x) = 3x^4 - 2x^3 + 5x - 7$.

$$f'(x) = 12x^3 - 6x^2 + 5$$

### Exemple 2 : dérivée d'un produit

Soit $f(x) = (2x+1)(x^2-3)$.

On pose $u(x) = 2x+1$ et $v(x) = x^2-3$.

- $u'(x) = 2$, $v'(x) = 2x$

$$f'(x) = 2(x^2-3) + (2x+1) \\cdot 2x = 2x^2 - 6 + 4x^2 + 2x = 6x^2 + 2x - 6$$

### Exemple 3 : dérivée d'un quotient

Soit $f(x) = \\frac{x+1}{x^2+1}$.

- $u(x) = x+1$, $u'(x) = 1$
- $v(x) = x^2+1$, $v'(x) = 2x$

$$f'(x) = \\frac{1 \\cdot (x^2+1) - (x+1) \\cdot 2x}{(x^2+1)^2} = \\frac{x^2+1-2x^2-2x}{(x^2+1)^2} = \\frac{-x^2-2x+1}{(x^2+1)^2}$$

---

## Dérivées composées

La dérivée de $g \\circ u$ (« $g$ de $u$ ») est :

$$(g \\circ u)'(x) = u'(x) \\cdot g'(u(x))$$

### Applications fréquentes

| Fonction | Dérivée |
|---|---|
| $u^n$ | $n \\cdot u' \\cdot u^{n-1}$ |
| $\\frac{1}{u}$ | $-\\frac{u'}{u^2}$ |
| $\\sqrt{u}$ | $\\frac{u'}{2\\sqrt{u}}$ |

### Exemple

Soit $f(x) = (3x+1)^4$.

On pose $u(x) = 3x+1$, donc $u'(x) = 3$.

$$f'(x) = 4 \\times 3 \\times (3x+1)^3 = 12(3x+1)^3$$

---

## Tableau récapitulatif des règles

| Opération | Formule |
|---|---|
| $(u+v)' $ | $u' + v'$ |
| $(ku)'$ | $ku'$ |
| $(uv)'$ | $u'v + uv'$ |
| $\\left(\\frac{u}{v}\\right)'$ | $\\frac{u'v-uv'}{v^2}$ |
| $(u^n)'$ | $nu'u^{n-1}$ |
| $(\\sqrt{u})'$ | $\\frac{u'}{2\\sqrt{u}}$ |

---

## À retenir

- Connaître le tableau des **dérivées usuelles** ($x^n$, $1/x$, $\\sqrt{x}$).
- Maîtriser les quatre opérations : **somme**, **produit**, **quotient**, **composée**.
- La formule du quotient nécessite que $v \\neq 0$ : $(u/v)' = (u'v - uv')/v^2$.
""",
                'quiz': {
                    'titre': 'Quiz — Dérivées usuelles et règles de dérivation',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quelle est la dérivée de $f(x) = x^3$ ?",
                            'options': ["$3x$", "$3x^2$", "$x^2$", "$3x^3$"],
                            'reponse_correcte': '1',
                            'explication': "$(x^n)' = nx^{n-1}$, donc $(x^3)' = 3x^2$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quelle est la dérivée de $f(x) = 5x^2 + 3x - 7$ ?",
                            'options': ["$10x + 3$", "$5x + 3$", "$10x - 7$", "$10x^2 + 3$"],
                            'reponse_correcte': '0',
                            'explication': "$f'(x) = 10x + 3$. La dérivée d'une constante est 0.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Quelle est la dérivée de $f(x) = \\\\frac{1}{x}$ ?",
                            'options': ["$\\\\frac{1}{x^2}$", "$-\\\\frac{1}{x^2}$", "$-\\\\frac{1}{x}$", "$\\\\frac{-2}{x^3}$"],
                            'reponse_correcte': '1',
                            'explication': "La dérivée de $\\frac{1}{x}$ est $-\\frac{1}{x^2}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quelle est la dérivée de $f(x) = \\\\sqrt{x}$ ?",
                            'options': ["$\\\\frac{1}{\\\\sqrt{x}}$", "$2\\\\sqrt{x}$", "$\\\\frac{1}{2\\\\sqrt{x}}$", "$\\\\frac{-1}{2\\\\sqrt{x}}$"],
                            'reponse_correcte': '2',
                            'explication': "$(\\sqrt{x})' = \\frac{1}{2\\sqrt{x}}$ sur $]0;+\\infty[$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'vrai_faux',
                            'texte': "La dérivée d'une constante est toujours égale à 0.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Si $f(x) = k$, alors $f'(x) = 0$ pour tout $x$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quelle est la formule de la dérivée d'un produit $(uv)'$ ?",
                            'options': ["$u'v'$", "$u'v + uv'$", "$u'v - uv'$", "$\\\\frac{u'}{v'}$"],
                            'reponse_correcte': '1',
                            'explication': "La formule du produit est $(uv)' = u'v + uv'$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Quelle est la formule de la dérivée d'un quotient $\\\\left(\\\\frac{u}{v}\\\\right)'$ ?",
                            'options': ["$\\\\frac{u'v + uv'}{v^2}$", "$\\\\frac{u'}{v'}$", "$\\\\frac{u'v - uv'}{v^2}$", "$\\\\frac{uv' - u'v}{v^2}$"],
                            'reponse_correcte': '2',
                            'explication': "La formule du quotient est $(u/v)' = \\frac{u'v - uv'}{v^2}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'vrai_faux',
                            'texte': "$(ku)' = ku'$ pour toute constante $k$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "La dérivée d'un scalaire fois une fonction est le scalaire fois la dérivée.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Soit $f(x) = (2x+1)(x^2-3)$. Que vaut $f'(x)$ ?",
                            'options': ["$2(x^2-3) + (2x+1)(2x)$", "$2 \\\\times 2x$", "$4x^2 + 2x - 6$", "$6x^2 + 2x - 6$"],
                            'reponse_correcte': '3',
                            'explication': "$f'(x) = 2(x^2-3)+(2x+1)(2x) = 2x^2 - 6 + 4x^2 + 2x = 6x^2+2x-6$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quelle est la dérivée de $f(x) = \\\\frac{x+1}{x^2+1}$ ? Quel est le numérateur de $f'(x)$ ?",
                            'options': ["$x^2 + 2x + 1$", "$-x^2 - 2x + 1$", "$x^2 - 2x - 1$", "$-x^2 + 2x - 1$"],
                            'reponse_correcte': '1',
                            'explication': "$f'(x) = \\frac{(x^2+1)-(x+1)(2x)}{(x^2+1)^2} = \\frac{-x^2-2x+1}{(x^2+1)^2}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Quelle est la dérivée de $f(x) = (3x+1)^4$ ?",
                            'options': ["$4(3x+1)^3$", "$12(3x+1)^3$", "$3(3x+1)^4$", "$12(3x+1)^4$"],
                            'reponse_correcte': '1',
                            'explication': "Par la formule $(u^n)'=nu'u^{n-1}$ : $f'(x) = 4 \\times 3 \\times (3x+1)^3 = 12(3x+1)^3$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Quelle est la dérivée de $f(x) = \\\\sqrt{2x+5}$ ?",
                            'options': ["$\\\\frac{1}{\\\\sqrt{2x+5}}$", "$\\\\frac{2}{\\\\sqrt{2x+5}}$", "$\\\\frac{1}{2\\\\sqrt{2x+5}}$", "$\\\\frac{2}{2\\\\sqrt{2x+5}}$"],
                            'reponse_correcte': '0',
                            'explication': "$(\\sqrt{u})' = \\frac{u'}{2\\sqrt{u}}$ avec $u=2x+5$, $u'=2$ : $f'(x) = \\frac{2}{2\\sqrt{2x+5}} = \\frac{1}{\\sqrt{2x+5}}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'vrai_faux',
                            'texte': "La dérivée de $(uv)$ est $u' \\\\times v'$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Non, $(uv)' = u'v + uv'$, pas $u' \\times v'$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'texte_libre',
                            'texte': "Calculer la dérivée de $f(x) = 4x^3 - 2x + 1$ et donner $f'(1)$.",
                            'options': None,
                            'reponse_correcte': '10',
                            'tolerances': ['10.0', '10,0'],
                            'explication': "$f'(x) = 12x^2 - 2$, donc $f'(1) = 12 - 2 = 10$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'texte_libre',
                            'texte': "Donner la dérivée de $f(x) = x^4$ sous la forme $ax^n$.",
                            'options': None,
                            'reponse_correcte': '4x^3',
                            'tolerances': ['4x³', '4*x^3'],
                            'explication': "$(x^4)' = 4x^3$ par la formule $(x^n)' = nx^{n-1}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La dérivée de $\\\\frac{1}{u}$ est $\\\\frac{u'}{u^2}$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La dérivée de $\\frac{1}{u}$ est $-\\frac{u'}{u^2}$ (signe négatif).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "Soit $f(x) = \\\\frac{2x}{x+1}$. Quel est le numérateur de $f'(x)$ ?",
                            'options': ["$2x + 2$", "$2$", "$-2x$", "$2x$"],
                            'reponse_correcte': '1',
                            'explication': "$f'(x) = \\frac{2(x+1)-2x}{(x+1)^2} = \\frac{2}{(x+1)^2}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer $f'(0)$ pour $f(x) = (x^2+1)^3$.",
                            'options': None,
                            'reponse_correcte': '0',
                            'tolerances': ['0.0', '0,0'],
                            'explication': "$f'(x) = 3 \\times 2x \\times (x^2+1)^2 = 6x(x^2+1)^2$. Donc $f'(0) = 0$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'qcm',
                            'texte': "Quelle est la dérivée de $f(x) = \\\\frac{x^2 - 1}{x^2 + 1}$ ? On demande le numérateur de $f'(x)$.",
                            'options': ["$4x$", "$2x$", "$-4x$", "$2x^2$"],
                            'reponse_correcte': '0',
                            'explication': "$f'(x)=\\frac{2x(x^2+1)-2x(x^2-1)}{(x^2+1)^2}=\\frac{4x}{(x^2+1)^2}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Calculer $f'(4)$ pour $f(x) = x\\\\sqrt{x}$ (écrire le résultat sous forme décimale).",
                            'options': None,
                            'reponse_correcte': '3',
                            'tolerances': ['3.0', '3,0'],
                            'explication': "$f(x)=x^{3/2}$, $f'(x)=\\frac{3}{2}x^{1/2}=\\frac{3}{2}\\sqrt{x}$. $f'(4)=\\frac{3}{2}\\times 2=3$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 3,
                'titre': 'Applications de la dérivation',
                'duree': 35,
                'contenu': """# Applications de la dérivation

## Lien entre signe de la dérivée et variations

C'est **le** résultat fondamental de ce chapitre :

> Soit $f$ une fonction dérivable sur un intervalle $I$.
> - Si $f'(x) > 0$ sur $I$, alors $f$ est **strictement croissante** sur $I$.
> - Si $f'(x) < 0$ sur $I$, alors $f$ est **strictement décroissante** sur $I$.
> - Si $f'(x) = 0$ sur $I$, alors $f$ est **constante** sur $I$.

### Comment dresser un tableau de variations

1. Calculer $f'(x)$.
2. Résoudre $f'(x) = 0$ pour trouver les valeurs critiques.
3. Étudier le **signe** de $f'(x)$ sur chaque intervalle.
4. En déduire les variations de $f$ et reporter dans un tableau.

---

## Extremums locaux

### Définition

- $f$ admet un **maximum local** en $c$ si $f(c) \\geq f(x)$ pour tout $x$ dans un voisinage de $c$.
- $f$ admet un **minimum local** en $c$ si $f(c) \\leq f(x)$ pour tout $x$ dans un voisinage de $c$.

### Condition nécessaire

> Si $f$ est dérivable en $c$ et admet un extremum local en $c$, alors $f'(c) = 0$.

**Attention :** la réciproque est fausse ! $f'(c) = 0$ ne garantit pas un extremum (exemple : $f(x) = x^3$ en $c = 0$).

### Condition suffisante

$f$ admet un **extremum local en $c$** si $f'$ **change de signe** en $c$ :

- $f'$ passe de $+$ à $-$ en $c$ → **maximum local**.
- $f'$ passe de $-$ à $+$ en $c$ → **minimum local**.

---

## Exemple complet : étude de $f(x) = x^3 - 3x + 1$

**Étape 1 — Ensemble de définition :** $D_f = \\mathbb{R}$.

**Étape 2 — Dérivée :**

$$f'(x) = 3x^2 - 3 = 3(x^2-1) = 3(x-1)(x+1)$$

**Étape 3 — Signe de $f'$ :**

$f'(x) = 0 \\Leftrightarrow x = -1$ ou $x = 1$.

| $x$ | $-\\infty$ | | $-1$ | | $1$ | | $+\\infty$ |
|---|---|---|---|---|---|---|---|
| $f'(x)$ | $+$ | | $0$ | $-$ | $0$ | | $+$ |
| $f$ | ↗ | | $3$ | ↘ | $-1$ | | ↗ |

**Étape 4 — Extremums :**

- **Maximum local** en $x = -1$ : $f(-1) = -1 + 3 + 1 = 3$
- **Minimum local** en $x = 1$ : $f(1) = 1 - 3 + 1 = -1$

---

## Problèmes d'optimisation

La dérivation permet de résoudre des problèmes concrets d'**optimisation** : trouver le maximum ou le minimum d'une grandeur.

### Méthode

1. **Modéliser** : exprimer la grandeur à optimiser comme une fonction $f(x)$.
2. **Dériver** et résoudre $f'(x) = 0$.
3. **Vérifier** que la valeur trouvée correspond à un extremum (changement de signe de $f'$).
4. **Conclure** en revenant au problème concret.

### Exemple : aire maximale d'un rectangle sous contrainte

On dispose d'une clôture de 20 m pour entourer un rectangle. Quelles dimensions maximisent l'aire ?

Si $x$ est la longueur, le périmètre impose $2x + 2y = 20$, soit $y = 10 - x$ avec $0 < x < 10$.

L'aire est $A(x) = x(10-x) = 10x - x^2$.

$$A'(x) = 10 - 2x$$

$A'(x) = 0 \\Leftrightarrow x = 5$.

Pour $x < 5$ : $A'(x) > 0$ (croissante). Pour $x > 5$ : $A'(x) < 0$ (décroissante).

**Maximum** en $x = 5$, $y = 5$ : c'est un **carré** de côté 5 m, d'aire $A = 25$ m².

---

## Tangente et position relative

L'équation de la tangente en $a$ étant $y = f'(a)(x-a) + f(a)$, on peut étudier la **position de la courbe par rapport à sa tangente** en calculant :

$$d(x) = f(x) - [f'(a)(x-a) + f(a)]$$

- Si $d(x) > 0$ au voisinage de $a$ : la courbe est **au-dessus** de sa tangente.
- Si $d(x) < 0$ : la courbe est **en dessous**.

---

## À retenir

- $f' > 0 \\Rightarrow f$ croissante ; $f' < 0 \\Rightarrow f$ décroissante.
- Pour un extremum : $f'(c) = 0$ **et** changement de signe de $f'$.
- La dérivation est l'outil central des **problèmes d'optimisation**.
- Dresser un tableau de variations : calculer $f'$, trouver ses zéros, signer, conclure.
""",
                'quiz': {
                    'titre': 'Quiz — Applications de la dérivation',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Si $f'(x) > 0$ sur un intervalle $I$, alors $f$ est :",
                            'options': ["Décroissante sur $I$", "Constante sur $I$", "Strictement croissante sur $I$", "Nulle sur $I$"],
                            'reponse_correcte': '2',
                            'explication': "Si $f'(x) > 0$ sur $I$, alors $f$ est strictement croissante sur $I$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Si $f'(x) < 0$ sur un intervalle $I$, alors $f$ est :",
                            'options': ["Strictement croissante", "Constante", "Strictement décroissante", "Positive"],
                            'reponse_correcte': '2',
                            'explication': "Dérivée négative implique fonction strictement décroissante.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'vrai_faux',
                            'texte': "Si $f'(c) = 0$, alors $f$ admet nécessairement un extremum local en $c$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Faux ! Contre-exemple : $f(x)=x^3$, $f'(0)=0$ mais pas d'extremum en 0.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quelle est la première étape pour dresser un tableau de variations ?",
                            'options': ["Calculer $f(0)$", "Calculer $f'(x)$", "Tracer la courbe", "Trouver l'ensemble de définition"],
                            'reponse_correcte': '1',
                            'explication': "On commence par calculer $f'(x)$ pour étudier son signe.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Si $f'$ passe du signe $+$ au signe $-$ en $c$, alors $f$ admet en $c$ un :",
                            'options': ["Minimum local", "Maximum local", "Point d'inflexion", "Aucun extremum"],
                            'reponse_correcte': '1',
                            'explication': "$f'$ passe de $+$ à $-$ : $f$ croît puis décroît, donc maximum local en $c$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'vrai_faux',
                            'texte': "Si $f'$ change de signe en $c$, alors $f$ admet un extremum local en $c$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Un changement de signe de $f'$ en $c$ garantit un extremum local.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Si $f'(x) = 0$ pour tout $x$ d'un intervalle $I$, alors $f$ est :",
                            'options': ["Croissante", "Décroissante", "Constante", "Nulle"],
                            'reponse_correcte': '2',
                            'explication': "Si la dérivée est identiquement nulle, la fonction est constante.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'vrai_faux',
                            'texte': "Un problème d'optimisation consiste à trouver le maximum ou le minimum d'une grandeur.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "L'optimisation cherche les valeurs extrêmes d'une fonction modélisant le problème.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Soit $f(x) = x^3 - 3x + 1$. Quelles sont les valeurs critiques (où $f'(x)=0$) ?",
                            'options': ["$x = 0$ et $x = 3$", "$x = 1$ et $x = -1$", "$x = -3$ et $x = 3$", "$x = 0$ uniquement"],
                            'reponse_correcte': '1',
                            'explication': "$f'(x)=3x^2-3=3(x-1)(x+1)=0$ donne $x=1$ et $x=-1$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Pour $f(x) = x^3 - 3x + 1$, quel est le maximum local ?",
                            'options': ["$f(1) = -1$", "$f(-1) = 3$", "$f(0) = 1$", "$f(3) = 19$"],
                            'reponse_correcte': '1',
                            'explication': "$f(-1) = -1+3+1 = 3$. En $x=-1$, $f'$ passe de $+$ à $-$ : maximum local.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Soit $f(x) = -x^2 + 4x - 1$. La fonction admet un maximum en :",
                            'options': ["$x = -2$", "$x = 4$", "$x = 2$", "$x = 1$"],
                            'reponse_correcte': '2',
                            'explication': "$f'(x) = -2x + 4 = 0 \\Leftrightarrow x = 2$. Comme $a=-1<0$, c'est un maximum.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "On entoure un rectangle de clôture (périmètre = 20 m). L'aire est maximale pour :",
                            'options': ["Un rectangle $8 \\\\times 2$", "Un rectangle $6 \\\\times 4$", "Un carré $5 \\\\times 5$", "Un rectangle $7 \\\\times 3$"],
                            'reponse_correcte': '2',
                            'explication': "$A(x)=x(10-x)$, $A'(x)=10-2x=0$ pour $x=5$. Maximum : carré $5\\times 5$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'vrai_faux',
                            'texte': "Pour $f(x) = x^3$, la dérivée s'annule en $x = 0$ et $f$ admet un extremum en $0$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "$f'(0)=0$ mais $f'$ ne change pas de signe (reste $\\geq 0$) : pas d'extremum.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'texte_libre',
                            'texte': "Soit $f(x) = x^2 - 6x + 5$. En quelle valeur de $x$ la fonction admet-elle un minimum ?",
                            'options': None,
                            'reponse_correcte': '3',
                            'tolerances': ['3.0', '3,0', 'x = 3', 'x=3'],
                            'explication': "$f'(x) = 2x - 6 = 0 \\Leftrightarrow x = 3$. Comme $a=1>0$, c'est un minimum.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'texte_libre',
                            'texte': "Calculer le minimum de $f(x) = x^2 - 6x + 5$.",
                            'options': None,
                            'reponse_correcte': '-4',
                            'tolerances': ['-4.0', '-4,0'],
                            'explication': "Le minimum est atteint en $x=3$ : $f(3) = 9 - 18 + 5 = -4$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'qcm',
                            'texte': "Comment vérifie-t-on qu'une valeur critique $c$ est bien un extremum ?",
                            'options': ["On vérifie que $f(c) = 0$", "On vérifie que $f'$ change de signe en $c$", "On vérifie que $f'(c) > 0$", "On vérifie que $f(c) > 0$"],
                            'reponse_correcte': '1',
                            'explication': "Un extremum nécessite un changement de signe de $f'$ en $c$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "Soit $f(x) = 2x^3 - 9x^2 + 12x$. En quelles valeurs $f'(x) = 0$ ?",
                            'options': ["$x = 0$ et $x = 3$", "$x = 1$ et $x = 2$", "$x = -1$ et $x = 2$", "$x = 2$ et $x = 3$"],
                            'reponse_correcte': '1',
                            'explication': "$f'(x)=6x^2-18x+12=6(x^2-3x+2)=6(x-1)(x-2)=0$ pour $x=1$ et $x=2$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer le maximum local de $f(x) = 2x^3 - 9x^2 + 12x$.",
                            'options': None,
                            'reponse_correcte': '5',
                            'tolerances': ['5.0', '5,0'],
                            'explication': "$f(1) = 2, - 9 + 12 = 5$. En $x=1$, $f'$ passe de $+$ à $-$ : maximum local.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'vrai_faux',
                            'texte': "La position de la courbe par rapport à sa tangente se détermine en étudiant le signe de $f(x) - [f'(a)(x-a)+f(a)]$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "On calcule $d(x) = f(x) - T(x)$ et on étudie son signe au voisinage de $a$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Calculer le minimum local de $f(x) = 2x^3 - 9x^2 + 12x$.",
                            'options': None,
                            'reponse_correcte': '4',
                            'tolerances': ['4.0', '4,0'],
                            'explication': "$f(2)=16-36+24=4$. En $x=2$, $f'$ passe de $-$ à $+$ : minimum local.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },

    # ──────────────────────────────────────────────
    # CHAPITRE 4 — Trigonométrie
    # ──────────────────────────────────────────────
    {
        'ordre': 4,
        'titre': 'Trigonométrie',
        'description': "Angles orientés, radian, cercle trigonométrique, cosinus et sinus, identités et équations.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Angles orientés et radian',
                'duree': 30,
                'contenu': """# Angles orientés et radian

## Le radian

### Pourquoi une nouvelle unité ?

Le degré (°) est pratique dans la vie courante, mais en mathématiques et en physique, le **radian** est l'unité naturelle pour mesurer les angles. Il simplifie de nombreuses formules (dérivation de sin et cos, longueur d'arc, etc.).

### Définition

Un **radian** est la mesure de l'angle au centre qui intercepte un arc de longueur égale au rayon du cercle.

Sur un cercle de rayon $r$, un angle de $\\theta$ radians intercepte un arc de longueur :

$$\\ell = r \\cdot \\theta$$

Pour un tour complet : $\\ell = 2\\pi r$, donc l'angle est $\\frac{2\\pi r}{r} = 2\\pi$ rad.

### Correspondance degrés ↔ radians

$$\\pi \\text{ rad} = 180°$$

Pour convertir :

- Degrés → radians : $\\theta_{\\text{rad}} = \\theta_{\\text{deg}} \\times \\frac{\\pi}{180}$
- Radians → degrés : $\\theta_{\\text{deg}} = \\theta_{\\text{rad}} \\times \\frac{180}{\\pi}$

### Valeurs à connaître

| Degrés | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $120°$ | $135°$ | $150°$ | $180°$ | $360°$ |
|--------|------|-------|-------|-------|-------|--------|--------|--------|--------|--------|
| Radians | $0$ | $\\frac{\\pi}{6}$ | $\\frac{\\pi}{4}$ | $\\frac{\\pi}{3}$ | $\\frac{\\pi}{2}$ | $\\frac{2\\pi}{3}$ | $\\frac{3\\pi}{4}$ | $\\frac{5\\pi}{6}$ | $\\pi$ | $2\\pi$ |

---

## Le cercle trigonométrique

### Définition

Le **cercle trigonométrique** est le cercle de centre $O$, de rayon $1$, muni d'un sens de parcours (le sens **trigonométrique** = sens inverse des aiguilles d'une montre).

### Enroulement de la droite des réels

À chaque nombre réel $\\theta$, on associe un unique point $M$ du cercle trigonométrique, obtenu en « enroulant » la droite des réels autour du cercle :

- On part du point $A(1 ; 0)$.
- On parcourt un arc de longueur $|\\theta|$ dans le sens direct si $\\theta > 0$, dans le sens indirect si $\\theta < 0$.
- On arrive au point $M$ associé à $\\theta$.

### Mesure principale

Tout réel $\\theta$ peut s'écrire sous la forme :

$$\\theta = \\theta_0 + 2k\\pi \\qquad \\text{avec } k \\in \\mathbb{Z} \\text{ et } \\theta_0 \\in ]-\\pi ; \\pi]$$

Le nombre $\\theta_0$ est la **mesure principale** de l'angle.

**Exemple :** $\\frac{13\\pi}{4} = \\frac{13\\pi}{4} - 2\\pi = \\frac{13\\pi - 8\\pi}{4} = \\frac{5\\pi}{4}$. Comme $\\frac{5\\pi}{4} > \\pi$, on soustrait encore $2\\pi$ : $\\frac{5\\pi}{4} - 2\\pi = -\\frac{3\\pi}{4}$.

Mesure principale : $-\\frac{3\\pi}{4}$.

---

## Angles orientés de vecteurs

### Définition

L'**angle orienté** de deux vecteurs non nuls $\\vec{u}$ et $\\vec{v}$ est la mesure (en radians) de la rotation qui amène la direction de $\\vec{u}$ sur celle de $\\vec{v}$.

On le note $(\\widehat{\\vec{u}, \\vec{v}})$ et il est défini **modulo $2\\pi$** :

$$(\\widehat{\\vec{u}, \\vec{v}}) = \\theta + 2k\\pi, \\quad k \\in \\mathbb{Z}$$

### Propriétés

- $(\\widehat{\\vec{u}, \\vec{v}}) = -(\\widehat{\\vec{v}, \\vec{u}}) \\pmod{2\\pi}$
- $(\\widehat{\\vec{u}, \\vec{w}}) = (\\widehat{\\vec{u}, \\vec{v}}) + (\\widehat{\\vec{v}, \\vec{w}}) \\pmod{2\\pi}$ (relation de Chasles)

---

## À retenir

- Le **radian** est défini par : un angle de 1 rad intercepte un arc de longueur égale au rayon.
- $\\pi$ rad $= 180°$. Conversion : multiplier par $\\frac{\\pi}{180}$ ou $\\frac{180}{\\pi}$.
- Le **cercle trigonométrique** est le cercle de centre $O$, rayon $1$, orienté dans le sens direct.
- Tout angle admet une unique **mesure principale** dans $]-\\pi ; \\pi]$.
""",
                'quiz': {
                    'titre': 'Quiz — Angles orientés et radian',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Combien vaut $\\\\pi$ radians en degrés ?",
                            'options': ["$90°$", "$180°$", "$360°$", "$270°$"],
                            'reponse_correcte': '1',
                            'explication': "$\\pi$ rad $= 180°$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Combien vaut un tour complet en radians ?",
                            'options': ["$\\\\pi$", "$\\\\frac{\\\\pi}{2}$", "$2\\\\pi$", "$4\\\\pi$"],
                            'reponse_correcte': '2',
                            'explication': "Un tour complet correspond à $2\\pi$ radians.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Quelle est la mesure en radians de $60°$ ?",
                            'options': ["$\\\\frac{\\\\pi}{6}$", "$\\\\frac{\\\\pi}{4}$", "$\\\\frac{\\\\pi}{3}$", "$\\\\frac{\\\\pi}{2}$"],
                            'reponse_correcte': '2',
                            'explication': "$60° = 60 \\times \\frac{\\pi}{180} = \\frac{\\pi}{3}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quelle est la mesure en radians de $45°$ ?",
                            'options': ["$\\\\frac{\\\\pi}{6}$", "$\\\\frac{\\\\pi}{4}$", "$\\\\frac{\\\\pi}{3}$", "$\\\\frac{\\\\pi}{2}$"],
                            'reponse_correcte': '1',
                            'explication': "$45° = 45 \\times \\frac{\\pi}{180} = \\frac{\\pi}{4}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'vrai_faux',
                            'texte': "Le cercle trigonométrique a un rayon de 1.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Le cercle trigonométrique est le cercle de centre $O$ et de rayon $1$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'vrai_faux',
                            'texte': "Le sens trigonométrique est le sens des aiguilles d'une montre.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le sens trigonométrique est le sens inverse des aiguilles d'une montre.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Quelle est la mesure en radians de $90°$ ?",
                            'options': ["$\\\\pi$", "$\\\\frac{\\\\pi}{2}$", "$\\\\frac{\\\\pi}{4}$", "$2\\\\pi$"],
                            'reponse_correcte': '1',
                            'explication': "$90° = \\frac{\\pi}{2}$ rad.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Pour convertir un angle de degrés en radians, on multiplie par :",
                            'options': ["$\\\\frac{180}{\\\\pi}$", "$\\\\frac{\\\\pi}{180}$", "$\\\\frac{\\\\pi}{360}$", "$\\\\frac{360}{\\\\pi}$"],
                            'reponse_correcte': '1',
                            'explication': "On multiplie par $\\frac{\\pi}{180}$ pour passer de degrés en radians.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Combien vaut $120°$ en radians ?",
                            'options': ["$\\\\frac{\\\\pi}{3}$", "$\\\\frac{2\\\\pi}{3}$", "$\\\\frac{3\\\\pi}{4}$", "$\\\\frac{5\\\\pi}{6}$"],
                            'reponse_correcte': '1',
                            'explication': "$120° = 120 \\times \\frac{\\pi}{180} = \\frac{2\\pi}{3}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quelle est la mesure en degrés de $\\\\frac{5\\\\pi}{6}$ rad ?",
                            'options': ["$120°$", "$150°$", "$135°$", "$100°$"],
                            'reponse_correcte': '1',
                            'explication': "$\\frac{5\\pi}{6} \\times \\frac{180}{\\pi} = 150°$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Sur un cercle de rayon $r$, un angle de $\\\\theta$ rad intercepte un arc de longueur :",
                            'options': ["$\\\\frac{r}{\\\\theta}$", "$r + \\\\theta$", "$r \\\\theta$", "$\\\\frac{\\\\theta}{r}$"],
                            'reponse_correcte': '2',
                            'explication': "La longueur de l'arc est $\\ell = r\\theta$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'vrai_faux',
                            'texte': "La mesure principale d'un angle appartient à l'intervalle $]-\\\\pi ; \\\\pi]$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Par convention, la mesure principale est dans $]-\\pi ; \\pi]$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'texte_libre',
                            'texte': "Convertir $30°$ en radians. Donner la réponse sous la forme $\\\\frac{\\\\pi}{n}$ (donner la valeur de $n$).",
                            'options': None,
                            'reponse_correcte': '6',
                            'tolerances': ['6.0', '6,0'],
                            'explication': "$30° = \\frac{\\pi}{6}$ rad, donc $n = 6$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "La relation de Chasles pour les angles orientés s'écrit :",
                            'options': ["$(\\\\widehat{\\\\vec{u},\\\\vec{w}}) = (\\\\widehat{\\\\vec{u},\\\\vec{v}}) \\\\times (\\\\widehat{\\\\vec{v},\\\\vec{w}})$", "$(\\\\widehat{\\\\vec{u},\\\\vec{w}}) = (\\\\widehat{\\\\vec{u},\\\\vec{v}}) + (\\\\widehat{\\\\vec{v},\\\\vec{w}})$", "$(\\\\widehat{\\\\vec{u},\\\\vec{w}}) = (\\\\widehat{\\\\vec{u},\\\\vec{v}}) - (\\\\widehat{\\\\vec{v},\\\\vec{w}})$", "Aucune de ces réponses"],
                            'reponse_correcte': '1',
                            'explication': "Relation de Chasles : $(\\widehat{\\vec{u},\\vec{w}}) = (\\widehat{\\vec{u},\\vec{v}}) + (\\widehat{\\vec{v},\\vec{w}})$ (mod $2\\pi$).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'texte_libre',
                            'texte': "Donner la mesure en degrés de $\\\\frac{3\\\\pi}{4}$ rad.",
                            'options': None,
                            'reponse_correcte': '135',
                            'tolerances': ['135°', '135.0', '135,0'],
                            'explication': "$\\frac{3\\pi}{4} \\times \\frac{180}{\\pi} = 135°$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Deux angles qui diffèrent de $2\\\\pi$ correspondent au même point sur le cercle trigonométrique.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Ajouter $2\\pi$ revient à faire un tour complet, on revient au même point.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Quelle est la mesure principale (en radians, sous forme de fraction de $\\\\pi$) de l'angle $\\\\frac{13\\\\pi}{4}$ ? Donner le numérateur de la fraction (le résultat est négatif).",
                            'options': None,
                            'reponse_correcte': '-3',
                            'tolerances': ['-3.0', '-3,0'],
                            'explication': "$\\frac{13\\pi}{4} - 2\\pi = \\frac{5\\pi}{4}$. Comme $\\frac{5\\pi}{4} > \\pi$, on soustrait $2\\pi$ : $\\frac{5\\pi}{4}-2\\pi = -\\frac{3\\pi}{4}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'qcm',
                            'texte': "Quelle est la mesure principale de $\\\\frac{7\\\\pi}{3}$ ?",
                            'options': ["$\\\\frac{\\\\pi}{3}$", "$-\\\\frac{\\\\pi}{3}$", "$\\\\frac{2\\\\pi}{3}$", "$\\\\frac{4\\\\pi}{3}$"],
                            'reponse_correcte': '0',
                            'explication': "$\\frac{7\\pi}{3} - 2\\pi = \\frac{7\\pi - 6\\pi}{3} = \\frac{\\pi}{3} \\in ]-\\pi;\\pi]$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'qcm',
                            'texte': "Quelle est la longueur d'un arc intercepté par un angle de $\\\\frac{\\\\pi}{3}$ rad sur un cercle de rayon $6$ cm ?",
                            'options': ["$2\\\\pi$ cm", "$6\\\\pi$ cm", "$\\\\pi$ cm", "$3\\\\pi$ cm"],
                            'reponse_correcte': '0',
                            'explication': "$\\ell = r\\theta = 6 \\times \\frac{\\pi}{3} = 2\\pi$ cm.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Convertir $\\\\frac{7\\\\pi}{6}$ rad en degrés.",
                            'options': None,
                            'reponse_correcte': '210',
                            'tolerances': ['210°', '210.0', '210,0'],
                            'explication': "$\\frac{7\\pi}{6} \\times \\frac{180}{\\pi} = \\frac{7 \\times 180}{6} = 210°$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Cosinus, sinus et valeurs remarquables',
                'duree': 35,
                'contenu': """# Cosinus, sinus et valeurs remarquables

## Définition sur le cercle trigonométrique

Soit $M$ le point du cercle trigonométrique associé à l'angle $\\theta$. Les coordonnées de $M$ sont :

$$M(\\cos\\theta \\;; \\sin\\theta)$$

- $\\cos\\theta$ est l'**abscisse** de $M$ (projection sur l'axe horizontal).
- $\\sin\\theta$ est l'**ordonnée** de $M$ (projection sur l'axe vertical).

---

## Valeurs remarquables

| $\\theta$ | $0$ | $\\frac{\\pi}{6}$ | $\\frac{\\pi}{4}$ | $\\frac{\\pi}{3}$ | $\\frac{\\pi}{2}$ | $\\pi$ |
|---|---|---|---|---|---|---|
| $\\cos\\theta$ | $1$ | $\\frac{\\sqrt{3}}{2}$ | $\\frac{\\sqrt{2}}{2}$ | $\\frac{1}{2}$ | $0$ | $-1$ |
| $\\sin\\theta$ | $0$ | $\\frac{1}{2}$ | $\\frac{\\sqrt{2}}{2}$ | $\\frac{\\sqrt{3}}{2}$ | $1$ | $0$ |

> **Astuce mnémotechnique :** pour le cosinus, on retient la séquence $\\frac{\\sqrt{4}}{2}, \\frac{\\sqrt{3}}{2}, \\frac{\\sqrt{2}}{2}, \\frac{\\sqrt{1}}{2}, \\frac{\\sqrt{0}}{2}$ — et pour le sinus, c'est la séquence dans l'ordre inverse.

---

## Identité fondamentale

Pour tout réel $\\theta$ :

$$\\boxed{\\cos^2\\theta + \\sin^2\\theta = 1}$$

C'est la conséquence directe du fait que $M$ est sur le cercle de rayon 1.

### Conséquences

- $-1 \\leq \\cos\\theta \\leq 1$ et $-1 \\leq \\sin\\theta \\leq 1$
- Si on connaît $\\cos\\theta$ et le quadrant, on peut en déduire $\\sin\\theta = \\pm\\sqrt{1-\\cos^2\\theta}$

---

## Relations de symétrie

Ces formules traduisent les **symétries du cercle trigonométrique** :

### Angle opposé ($-\\theta$) — Symétrie par rapport à l'axe $Ox$

$$\\cos(-\\theta) = \\cos\\theta \\qquad \\sin(-\\theta) = -\\sin\\theta$$

> Le cosinus est une fonction **paire**, le sinus est une fonction **impaire**.

### Angle supplémentaire ($\\pi - \\theta$) — Symétrie par rapport à l'axe $Oy$

$$\\cos(\\pi - \\theta) = -\\cos\\theta \\qquad \\sin(\\pi - \\theta) = \\sin\\theta$$

### Angle complémentaire à $\\pi$ ($\\pi + \\theta$) — Symétrie par rapport à $O$

$$\\cos(\\pi + \\theta) = -\\cos\\theta \\qquad \\sin(\\pi + \\theta) = -\\sin\\theta$$

### Angle complémentaire à $\\frac{\\pi}{2}$ ($\\frac{\\pi}{2} - \\theta$)

$$\\cos\\left(\\frac{\\pi}{2} - \\theta\\right) = \\sin\\theta \\qquad \\sin\\left(\\frac{\\pi}{2} - \\theta\\right) = \\cos\\theta$$

### Déphasage de $\\frac{\\pi}{2}$ ($\\theta + \\frac{\\pi}{2}$)

$$\\cos\\left(\\theta + \\frac{\\pi}{2}\\right) = -\\sin\\theta \\qquad \\sin\\left(\\theta + \\frac{\\pi}{2}\\right) = \\cos\\theta$$

---

## Tableau récapitulatif

| Transformation | $\\cos$ | $\\sin$ |
|---|---|---|
| $-\\theta$ | $\\cos\\theta$ | $-\\sin\\theta$ |
| $\\pi - \\theta$ | $-\\cos\\theta$ | $\\sin\\theta$ |
| $\\pi + \\theta$ | $-\\cos\\theta$ | $-\\sin\\theta$ |
| $\\frac{\\pi}{2} - \\theta$ | $\\sin\\theta$ | $\\cos\\theta$ |
| $\\frac{\\pi}{2} + \\theta$ | $-\\sin\\theta$ | $\\cos\\theta$ |

---

## Exemple d'utilisation

Calculer $\\cos\\left(\\frac{5\\pi}{6}\\right)$ et $\\sin\\left(\\frac{5\\pi}{6}\\right)$.

On écrit $\\frac{5\\pi}{6} = \\pi - \\frac{\\pi}{6}$.

D'après les formules de l'angle supplémentaire :

$$\\cos\\left(\\frac{5\\pi}{6}\\right) = -\\cos\\left(\\frac{\\pi}{6}\\right) = -\\frac{\\sqrt{3}}{2}$$

$$\\sin\\left(\\frac{5\\pi}{6}\\right) = \\sin\\left(\\frac{\\pi}{6}\\right) = \\frac{1}{2}$$

---

## À retenir

- $\\cos\\theta$ = abscisse, $\\sin\\theta$ = ordonnée du point $M$ sur le cercle trigonométrique.
- **Identité fondamentale :** $\\cos^2\\theta + \\sin^2\\theta = 1$.
- Connaître les **valeurs remarquables** pour $0$, $\\frac{\\pi}{6}$, $\\frac{\\pi}{4}$, $\\frac{\\pi}{3}$, $\\frac{\\pi}{2}$.
- Maîtriser les **formules de symétrie** pour se ramener aux angles du premier quadrant.
""",
                'quiz': {
                    'titre': 'Quiz — Cosinus, sinus et valeurs remarquables',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Sur le cercle trigonométrique, $\\\\cos\\\\theta$ est :",
                            'options': ["L'ordonnée du point $M$", "L'abscisse du point $M$", "La distance $OM$", "La pente de $OM$"],
                            'reponse_correcte': '1',
                            'explication': "$\\cos\\theta$ est l'abscisse du point $M$ sur le cercle trigonométrique.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\cos(0)$ ?",
                            'options': ["$0$", "$1$", "$-1$", "$\\\\frac{1}{2}$"],
                            'reponse_correcte': '1',
                            'explication': "$\\cos(0) = 1$ (point $(1;0)$ sur le cercle).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\sin\\\\left(\\\\frac{\\\\pi}{2}\\\\right)$ ?",
                            'options': ["$0$", "$\\\\frac{1}{2}$", "$1$", "$-1$"],
                            'reponse_correcte': '2',
                            'explication': "$\\sin\\left(\\frac{\\pi}{2}\\right) = 1$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\cos\\\\left(\\\\frac{\\\\pi}{3}\\\\right)$ ?",
                            'options': ["$\\\\frac{\\\\sqrt{3}}{2}$", "$\\\\frac{\\\\sqrt{2}}{2}$", "$\\\\frac{1}{2}$", "$0$"],
                            'reponse_correcte': '2',
                            'explication': "$\\cos\\left(\\frac{\\pi}{3}\\right) = \\frac{1}{2}$ (valeur remarquable).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'vrai_faux',
                            'texte': "L'identité fondamentale est $\\\\cos^2\\\\theta + \\\\sin^2\\\\theta = 1$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est la conséquence directe du fait que $M$ est sur le cercle de rayon 1.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'vrai_faux',
                            'texte': "Le cosinus est une fonction impaire.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le cosinus est une fonction paire : $\\cos(-\\theta) = \\cos\\theta$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\sin\\\\left(\\\\frac{\\\\pi}{6}\\\\right)$ ?",
                            'options': ["$\\\\frac{\\\\sqrt{3}}{2}$", "$\\\\frac{\\\\sqrt{2}}{2}$", "$\\\\frac{1}{2}$", "$1$"],
                            'reponse_correcte': '2',
                            'explication': "$\\sin\\left(\\frac{\\pi}{6}\\right) = \\frac{1}{2}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\cos\\\\left(\\\\frac{\\\\pi}{4}\\\\right)$ ?",
                            'options': ["$\\\\frac{1}{2}$", "$\\\\frac{\\\\sqrt{3}}{2}$", "$\\\\frac{\\\\sqrt{2}}{2}$", "$0$"],
                            'reponse_correcte': '2',
                            'explication': "$\\cos\\left(\\frac{\\pi}{4}\\right) = \\frac{\\sqrt{2}}{2}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\cos(\\\\pi)$ ?",
                            'options': ["$0$", "$1$", "$-1$", "$\\\\frac{1}{2}$"],
                            'reponse_correcte': '2',
                            'explication': "$\\cos(\\pi) = -1$ (point $(-1;0)$ sur le cercle).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\sin(-\\\\theta)$ ?",
                            'options': ["$\\\\sin\\\\theta$", "$-\\\\sin\\\\theta$", "$\\\\cos\\\\theta$", "$-\\\\cos\\\\theta$"],
                            'reponse_correcte': '1',
                            'explication': "Le sinus est impair : $\\sin(-\\theta) = -\\sin\\theta$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\cos(\\\\pi - \\\\theta)$ ?",
                            'options': ["$\\\\cos\\\\theta$", "$-\\\\cos\\\\theta$", "$\\\\sin\\\\theta$", "$-\\\\sin\\\\theta$"],
                            'reponse_correcte': '1',
                            'explication': "Formule de l'angle supplémentaire : $\\cos(\\pi-\\theta) = -\\cos\\theta$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'vrai_faux',
                            'texte': "Le sinus est une fonction paire.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le sinus est impair ($\\sin(-\\theta)=-\\sin\\theta$), pas pair.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\sin(\\\\pi - \\\\theta)$ ?",
                            'options': ["$-\\\\sin\\\\theta$", "$\\\\sin\\\\theta$", "$\\\\cos\\\\theta$", "$-\\\\cos\\\\theta$"],
                            'reponse_correcte': '1',
                            'explication': "$\\sin(\\pi - \\theta) = \\sin\\theta$ (symétrie par rapport à $Oy$).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'texte_libre',
                            'texte': "Que vaut $\\\\cos\\\\left(\\\\frac{\\\\pi}{6}\\\\right)$ ? Donner la réponse exacte simplifiée (sans les parenthèses).",
                            'options': None,
                            'reponse_correcte': 'sqrt(3)/2',
                            'tolerances': ['racine(3)/2', 'racine de 3 sur 2', 'V3/2'],
                            'explication': "$\\cos\\left(\\frac{\\pi}{6}\\right) = \\frac{\\sqrt{3}}{2}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'texte_libre',
                            'texte': "Que vaut $\\\\sin\\\\left(\\\\frac{\\\\pi}{4}\\\\right)$ ? Donner la réponse exacte simplifiée.",
                            'options': None,
                            'reponse_correcte': 'sqrt(2)/2',
                            'tolerances': ['racine(2)/2', 'racine de 2 sur 2', 'V2/2'],
                            'explication': "$\\sin\\left(\\frac{\\pi}{4}\\right) = \\frac{\\sqrt{2}}{2}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\cos\\\\left(\\\\frac{5\\\\pi}{6}\\\\right)$ ?",
                            'options': ["$\\\\frac{\\\\sqrt{3}}{2}$", "$-\\\\frac{\\\\sqrt{3}}{2}$", "$\\\\frac{1}{2}$", "$-\\\\frac{1}{2}$"],
                            'reponse_correcte': '1',
                            'explication': "$\\frac{5\\pi}{6} = \\pi - \\frac{\\pi}{6}$, donc $\\cos\\left(\\frac{5\\pi}{6}\\right) = -\\cos\\left(\\frac{\\pi}{6}\\right) = -\\frac{\\sqrt{3}}{2}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\cos\\\\left(\\\\theta + \\\\frac{\\\\pi}{2}\\\\right)$ ?",
                            'options': ["$\\\\cos\\\\theta$", "$\\\\sin\\\\theta$", "$-\\\\sin\\\\theta$", "$-\\\\cos\\\\theta$"],
                            'reponse_correcte': '2',
                            'explication': "$\\cos\\left(\\theta + \\frac{\\pi}{2}\\right) = -\\sin\\theta$ (déphasage de $\\frac{\\pi}{2}$).",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Sachant que $\\\\cos\\\\theta = \\\\frac{3}{5}$ et $\\\\theta \\\\in \\\\left]0;\\\\frac{\\\\pi}{2}\\\\right[$, calculer $\\\\sin\\\\theta$. Donner la réponse sous forme de fraction.",
                            'options': None,
                            'reponse_correcte': '4/5',
                            'tolerances': ['0.8', '0,8'],
                            'explication': "$\\sin^2\\theta = 1 - \\cos^2\\theta = 1 - \\frac{9}{25} = \\frac{16}{25}$. Comme $\\theta \\in ]0;\\frac{\\pi}{2}[$, $\\sin\\theta = \\frac{4}{5}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'vrai_faux',
                            'texte': "$\\\\cos(\\\\pi + \\\\theta) = \\\\cos\\\\theta$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "$\\cos(\\pi+\\theta) = -\\cos\\theta$ (symétrie par rapport à $O$).",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Calculer $\\\\sin\\\\left(\\\\frac{5\\\\pi}{6}\\\\right)$. Donner la réponse sous forme de fraction.",
                            'options': None,
                            'reponse_correcte': '1/2',
                            'tolerances': ['0.5', '0,5'],
                            'explication': "$\\frac{5\\pi}{6} = \\pi - \\frac{\\pi}{6}$, donc $\\sin\\left(\\frac{5\\pi}{6}\\right) = \\sin\\left(\\frac{\\pi}{6}\\right) = \\frac{1}{2}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 3,
                'titre': 'Équations trigonométriques',
                'duree': 35,
                'contenu': """# Équations trigonométriques

## Résolution de $\\cos x = \\cos \\alpha$

L'équation $\\cos x = \\cos\\alpha$ a pour solutions :

$$\\boxed{x = \\alpha + 2k\\pi \\quad \\text{ou} \\quad x = -\\alpha + 2k\\pi, \\quad k \\in \\mathbb{Z}}$$

### Interprétation géométrique

Deux points du cercle trigonométrique ont la même abscisse (même cosinus) s'ils sont **symétriques par rapport à l'axe $Ox$**. Leurs angles sont $\\alpha$ et $-\\alpha$ (modulo $2\\pi$).

### Exemple

Résoudre $\\cos x = \\frac{1}{2}$.

On reconnaît $\\cos\\left(\\frac{\\pi}{3}\\right) = \\frac{1}{2}$, donc $\\alpha = \\frac{\\pi}{3}$.

$$x = \\frac{\\pi}{3} + 2k\\pi \\quad \\text{ou} \\quad x = -\\frac{\\pi}{3} + 2k\\pi, \\quad k \\in \\mathbb{Z}$$

---

## Résolution de $\\sin x = \\sin \\alpha$

L'équation $\\sin x = \\sin\\alpha$ a pour solutions :

$$\\boxed{x = \\alpha + 2k\\pi \\quad \\text{ou} \\quad x = \\pi - \\alpha + 2k\\pi, \\quad k \\in \\mathbb{Z}}$$

### Interprétation géométrique

Deux points du cercle trigonométrique ont la même ordonnée (même sinus) s'ils sont **symétriques par rapport à l'axe $Oy$**. Leurs angles sont $\\alpha$ et $\\pi - \\alpha$ (modulo $2\\pi$).

### Exemple

Résoudre $\\sin x = \\frac{\\sqrt{2}}{2}$.

On reconnaît $\\sin\\left(\\frac{\\pi}{4}\\right) = \\frac{\\sqrt{2}}{2}$, donc $\\alpha = \\frac{\\pi}{4}$.

$$x = \\frac{\\pi}{4} + 2k\\pi \\quad \\text{ou} \\quad x = \\frac{3\\pi}{4} + 2k\\pi, \\quad k \\in \\mathbb{Z}$$

---

## Résolution sur un intervalle donné

En pratique, on demande souvent les solutions dans un intervalle, typiquement $[0 ; 2\\pi[$ ou $]-\\pi ; \\pi]$.

### Méthode

1. Trouver les solutions **générales** (avec le paramètre $k \\in \\mathbb{Z}$).
2. Substituer les valeurs de $k$ ($0, 1, -1, 2, \\ldots$) pour trouver celles qui tombent dans l'intervalle demandé.

### Exemple

Résoudre $\\cos x = -\\frac{\\sqrt{3}}{2}$ sur $[0 ; 2\\pi[$.

On reconnaît $\\cos\\left(\\frac{\\pi}{6}\\right) = \\frac{\\sqrt{3}}{2}$, donc $\\cos\\left(\\frac{5\\pi}{6}\\right) = -\\frac{\\sqrt{3}}{2}$ et $\\alpha = \\frac{5\\pi}{6}$.

Solutions générales : $x = \\frac{5\\pi}{6} + 2k\\pi$ ou $x = -\\frac{5\\pi}{6} + 2k\\pi$.

Sur $[0 ; 2\\pi[$ :

- $k=0$ : $x = \\frac{5\\pi}{6}$ ✓ et $x = -\\frac{5\\pi}{6} \\notin [0;2\\pi[$ ✗
- $k=1$ pour la seconde : $x = -\\frac{5\\pi}{6} + 2\\pi = \\frac{7\\pi}{6}$ ✓

**Solutions :** $x \\in \\left\\{\\frac{5\\pi}{6} ; \\frac{7\\pi}{6}\\right\\}$.

---

## Inéquations trigonométriques

Pour résoudre des inéquations comme $\\cos x \\geq \\frac{1}{2}$ ou $\\sin x < 0$, on s'aide du **cercle trigonométrique** :

1. Repérer les angles où l'égalité est atteinte.
2. Identifier l'arc du cercle vérifiant l'inégalité.
3. Écrire l'ensemble solution avec le paramètre $k$.

### Exemple

Résoudre $\\sin x \\geq \\frac{1}{2}$ sur $[0 ; 2\\pi[$.

$\\sin x = \\frac{1}{2}$ pour $x = \\frac{\\pi}{6}$ et $x = \\frac{5\\pi}{6}$.

Sur le cercle, $\\sin x \\geq \\frac{1}{2}$ pour les points situés au-dessus de la droite horizontale $y = \\frac{1}{2}$, c'est-à-dire pour :

$$x \\in \\left[\\frac{\\pi}{6} ; \\frac{5\\pi}{6}\\right]$$

---

## Formules d'addition (complément)

Même si elles sont surtout développées en Terminale, les formules d'addition peuvent apparaître en exercice :

$$\\cos(a+b) = \\cos a \\cos b - \\sin a \\sin b$$
$$\\sin(a+b) = \\sin a \\cos b + \\cos a \\sin b$$

**Application :** $\\cos\\left(\\frac{\\pi}{3} + \\frac{\\pi}{4}\\right) = \\cos\\frac{\\pi}{3}\\cos\\frac{\\pi}{4} - \\sin\\frac{\\pi}{3}\\sin\\frac{\\pi}{4}$

$$= \\frac{1}{2} \\cdot \\frac{\\sqrt{2}}{2} - \\frac{\\sqrt{3}}{2} \\cdot \\frac{\\sqrt{2}}{2} = \\frac{\\sqrt{2} - \\sqrt{6}}{4}$$

---

## À retenir

- **$\\cos x = \\cos\\alpha$** : $x = \\pm \\alpha + 2k\\pi$.
- **$\\sin x = \\sin\\alpha$** : $x = \\alpha + 2k\\pi$ ou $x = \\pi - \\alpha + 2k\\pi$.
- Pour les solutions sur un intervalle, on fixe les valeurs de $k$.
- Pour les **inéquations**, on raisonne sur le cercle trigonométrique.
""",
                'quiz': {
                    'titre': 'Quiz — Équations trigonométriques',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Les solutions de $\\\\cos x = \\\\cos\\\\alpha$ sont :",
                            'options': ["$x = \\\\alpha + 2k\\\\pi$ uniquement", "$x = \\\\alpha + k\\\\pi$ ou $x = -\\\\alpha + k\\\\pi$", "$x = \\\\alpha + 2k\\\\pi$ ou $x = -\\\\alpha + 2k\\\\pi$", "$x = \\\\alpha + 2k\\\\pi$ ou $x = \\\\pi - \\\\alpha + 2k\\\\pi$"],
                            'reponse_correcte': '2',
                            'explication': "$\\cos x = \\cos\\alpha \\Leftrightarrow x = \\alpha + 2k\\pi$ ou $x = -\\alpha + 2k\\pi$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Les solutions de $\\\\sin x = \\\\sin\\\\alpha$ sont :",
                            'options': ["$x = \\\\alpha + 2k\\\\pi$ ou $x = \\\\pi - \\\\alpha + 2k\\\\pi$", "$x = \\\\alpha + 2k\\\\pi$ ou $x = -\\\\alpha + 2k\\\\pi$", "$x = \\\\alpha + k\\\\pi$", "$x = \\\\alpha + 2k\\\\pi$ uniquement"],
                            'reponse_correcte': '0',
                            'explication': "$\\sin x = \\sin\\alpha \\Leftrightarrow x = \\alpha + 2k\\pi$ ou $x = \\pi-\\alpha + 2k\\pi$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Résoudre $\\\\cos x = 1$. Les solutions sont :",
                            'options': ["$x = \\\\frac{\\\\pi}{2} + 2k\\\\pi$", "$x = 2k\\\\pi$", "$x = \\\\pi + 2k\\\\pi$", "$x = k\\\\pi$"],
                            'reponse_correcte': '1',
                            'explication': "$\\cos x = 1 = \\cos 0 \\Rightarrow x = 0 + 2k\\pi = 2k\\pi$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Résoudre $\\\\sin x = 0$. Les solutions sont :",
                            'options': ["$x = 2k\\\\pi$", "$x = k\\\\pi$", "$x = \\\\frac{\\\\pi}{2} + k\\\\pi$", "$x = \\\\frac{\\\\pi}{2} + 2k\\\\pi$"],
                            'reponse_correcte': '1',
                            'explication': "$\\sin x = 0 = \\sin 0 \\Rightarrow x = 2k\\pi$ ou $x = \\pi + 2k\\pi$, soit $x = k\\pi$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'vrai_faux',
                            'texte': "L'équation $\\\\cos x = \\\\frac{1}{2}$ admet une infinité de solutions.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Les solutions sont $x = \\frac{\\pi}{3} + 2k\\pi$ et $x = -\\frac{\\pi}{3} + 2k\\pi$ pour tout $k\\in\\mathbb{Z}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'vrai_faux',
                            'texte': "L'équation $\\\\cos x = 2$ admet des solutions.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "$-1 \\leq \\cos x \\leq 1$, donc $\\cos x = 2$ n'a aucune solution.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "L'équation $\\\\cos x = \\\\frac{1}{2}$ a pour solutions :",
                            'options': ["$x = \\\\frac{\\\\pi}{6} + 2k\\\\pi$ ou $x = -\\\\frac{\\\\pi}{6} + 2k\\\\pi$", "$x = \\\\frac{\\\\pi}{3} + 2k\\\\pi$ ou $x = -\\\\frac{\\\\pi}{3} + 2k\\\\pi$", "$x = \\\\frac{\\\\pi}{4} + 2k\\\\pi$ ou $x = -\\\\frac{\\\\pi}{4} + 2k\\\\pi$", "$x = \\\\frac{\\\\pi}{3} + k\\\\pi$"],
                            'reponse_correcte': '1',
                            'explication': "$\\cos\\left(\\frac{\\pi}{3}\\right) = \\frac{1}{2}$, donc $x = \\pm\\frac{\\pi}{3} + 2k\\pi$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "L'équation $\\\\sin x = \\\\frac{\\\\sqrt{2}}{2}$ a pour solutions :",
                            'options': ["$x = \\\\frac{\\\\pi}{4} + 2k\\\\pi$ ou $x = \\\\frac{3\\\\pi}{4} + 2k\\\\pi$", "$x = \\\\frac{\\\\pi}{3} + 2k\\\\pi$ ou $x = \\\\frac{2\\\\pi}{3} + 2k\\\\pi$", "$x = \\\\frac{\\\\pi}{6} + 2k\\\\pi$ ou $x = \\\\frac{5\\\\pi}{6} + 2k\\\\pi$", "$x = \\\\frac{\\\\pi}{4} + k\\\\pi$"],
                            'reponse_correcte': '0',
                            'explication': "$\\sin\\left(\\frac{\\pi}{4}\\right)=\\frac{\\sqrt{2}}{2}$, donc $x=\\frac{\\pi}{4}+2k\\pi$ ou $x=\\pi-\\frac{\\pi}{4}+2k\\pi=\\frac{3\\pi}{4}+2k\\pi$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Sur $[0 ; 2\\\\pi[$, combien de solutions a l'équation $\\\\cos x = \\\\frac{1}{2}$ ?",
                            'options': ["$1$", "$2$", "$3$", "$4$"],
                            'reponse_correcte': '1',
                            'explication': "Sur $[0;2\\pi[$ : $x = \\frac{\\pi}{3}$ et $x = \\frac{5\\pi}{3}$, soit 2 solutions.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Résoudre $\\\\cos x = -\\\\frac{\\\\sqrt{3}}{2}$ sur $[0 ; 2\\\\pi[$. Les solutions sont :",
                            'options': ["$\\\\frac{\\\\pi}{6}$ et $\\\\frac{11\\\\pi}{6}$", "$\\\\frac{5\\\\pi}{6}$ et $\\\\frac{7\\\\pi}{6}$", "$\\\\frac{2\\\\pi}{3}$ et $\\\\frac{4\\\\pi}{3}$", "$\\\\frac{\\\\pi}{3}$ et $\\\\frac{5\\\\pi}{3}$"],
                            'reponse_correcte': '1',
                            'explication': "$\\cos x = -\\frac{\\sqrt{3}}{2} = \\cos\\frac{5\\pi}{6}$, donc $x = \\frac{5\\pi}{6}$ ou $x = -\\frac{5\\pi}{6}+2\\pi = \\frac{7\\pi}{6}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "L'ensemble des solutions de $\\\\sin x \\\\geq \\\\frac{1}{2}$ sur $[0 ; 2\\\\pi[$ est :",
                            'options': ["$\\\\left[\\\\frac{\\\\pi}{6} ; \\\\frac{5\\\\pi}{6}\\\\right]$", "$\\\\left[0 ; \\\\frac{\\\\pi}{6}\\\\right]$", "$\\\\left[\\\\frac{\\\\pi}{6} ; \\\\pi\\\\right]$", "$\\\\left[\\\\frac{\\\\pi}{3} ; \\\\frac{2\\\\pi}{3}\\\\right]$"],
                            'reponse_correcte': '0',
                            'explication': "$\\sin x = \\frac{1}{2}$ pour $x=\\frac{\\pi}{6}$ et $x=\\frac{5\\pi}{6}$. Entre ces deux valeurs, $\\sin x \\geq \\frac{1}{2}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'vrai_faux',
                            'texte': "L'équation $\\\\sin x = \\\\sin\\\\alpha$ admet exactement deux familles de solutions.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Les deux familles sont $x = \\alpha + 2k\\pi$ et $x = \\pi - \\alpha + 2k\\pi$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'texte_libre',
                            'texte': "Combien de solutions l'équation $\\\\sin x = \\\\frac{1}{2}$ admet-elle sur $[0 ; 2\\\\pi[$ ?",
                            'options': None,
                            'reponse_correcte': '2',
                            'tolerances': ['deux'],
                            'explication': "$x = \\frac{\\pi}{6}$ et $x = \\frac{5\\pi}{6}$, soit 2 solutions.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Résoudre $\\\\sin x = -1$ sur $[0 ; 2\\\\pi[$.",
                            'options': ["$x = 0$", "$x = \\\\pi$", "$x = \\\\frac{3\\\\pi}{2}$", "$x = 2\\\\pi$"],
                            'reponse_correcte': '2',
                            'explication': "$\\sin x = -1$ pour $x = \\frac{3\\pi}{2}$ (point le plus bas du cercle).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Pour résoudre une inéquation trigonométrique, on peut s'aider du cercle trigonométrique.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Le cercle trigonométrique permet de visualiser les arcs vérifiant l'inégalité.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'texte_libre',
                            'texte': "Donner une solution dans $]0 ; \\\\pi[$ de l'équation $\\\\cos x = 0$. Répondre sous la forme d'une fraction de $\\\\pi$ (par exemple pi/4).",
                            'options': None,
                            'reponse_correcte': 'pi/2',
                            'tolerances': ['π/2', 'Pi/2'],
                            'explication': "$\\cos x = 0 \\Rightarrow x = \\frac{\\pi}{2}$ sur $]0;\\pi[$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "Résoudre $\\\\cos x = -\\\\frac{1}{2}$ sur $[0 ; 2\\\\pi[$. Les solutions sont :",
                            'options': ["$\\\\frac{\\\\pi}{3}$ et $\\\\frac{5\\\\pi}{3}$", "$\\\\frac{2\\\\pi}{3}$ et $\\\\frac{4\\\\pi}{3}$", "$\\\\frac{\\\\pi}{6}$ et $\\\\frac{11\\\\pi}{6}$", "$\\\\frac{5\\\\pi}{6}$ et $\\\\frac{7\\\\pi}{6}$"],
                            'reponse_correcte': '1',
                            'explication': "$\\cos x = -\\frac{1}{2} = \\cos\\frac{2\\pi}{3}$, donc $x=\\frac{2\\pi}{3}$ ou $x=2\\pi-\\frac{2\\pi}{3}=\\frac{4\\pi}{3}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Résoudre $\\\\sin x = \\\\frac{\\\\sqrt{3}}{2}$ sur $[0 ; 2\\\\pi[$. Donner la plus grande solution sous forme de fraction de $\\\\pi$ (par exemple 5pi/6).",
                            'options': None,
                            'reponse_correcte': '2pi/3',
                            'tolerances': ['2π/3', '2Pi/3', '2*pi/3'],
                            'explication': "$\\sin\\left(\\frac{\\pi}{3}\\right)=\\frac{\\sqrt{3}}{2}$. Solutions : $x=\\frac{\\pi}{3}$ et $x=\\pi-\\frac{\\pi}{3}=\\frac{2\\pi}{3}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'qcm',
                            'texte': "La formule $\\\\cos(a+b)$ vaut :",
                            'options': ["$\\\\cos a \\\\cos b + \\\\sin a \\\\sin b$", "$\\\\cos a \\\\cos b - \\\\sin a \\\\sin b$", "$\\\\sin a \\\\cos b + \\\\cos a \\\\sin b$", "$\\\\sin a \\\\cos b - \\\\cos a \\\\sin b$"],
                            'reponse_correcte': '1',
                            'explication': "$\\cos(a+b) = \\cos a \\cos b - \\sin a \\sin b$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Combien de solutions l'équation $\\\\cos x = -1$ admet-elle sur $[0 ; 2\\\\pi[$ ?",
                            'options': None,
                            'reponse_correcte': '1',
                            'tolerances': ['une'],
                            'explication': "La seule solution est $x = \\pi$ ($\\cos\\pi = -1$).",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 5 — Fonction exponentielle
    # ──────────────────────────────────────────────
    {
        'ordre': 5,
        'titre': 'Fonction exponentielle',
        'description': "Définition, propriétés algébriques, dérivation, variations, croissances comparées et modèles exponentiels.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Définition et propriétés algébriques',
                'duree': 35,
                'contenu': """# Définition et propriétés algébriques de la fonction exponentielle

## Introduction

La fonction exponentielle est l'une des fonctions les plus importantes en mathématiques et en sciences. Elle modélise des phénomènes de croissance (population, capital placé) et de décroissance (radioactivité, refroidissement). Ce chapitre introduit sa définition rigoureuse et ses propriétés fondamentales.

---

## Définition

La **fonction exponentielle** est l'unique fonction $f$ définie et dérivable sur $\\mathbb{R}$ telle que :

$$f'(x) = f(x) \\quad \\text{et} \\quad f(0) = 1$$

On la note $\\exp$ et on écrit $\\exp(x) = e^x$.

> **Remarque :** La lettre $e$ désigne le nombre d'Euler, un nombre irrationnel dont la valeur approchée est $e \\approx 2{,}718\\,28$.

### Conséquence immédiate

Puisque $f'(x) = f(x)$ et que le carré d'un nombre réel non nul est strictement positif, on peut montrer que :

$$\\forall x \\in \\mathbb{R}, \\quad e^x > 0$$

La fonction exponentielle est **strictement positive** sur $\\mathbb{R}$.

---

## Propriétés algébriques

Les propriétés algébriques de l'exponentielle traduisent celles des puissances.

### Propriété fondamentale

Pour tous réels $a$ et $b$ :

$$e^{a+b} = e^a \\cdot e^b$$

> **Démonstration (idée) :** On considère la fonction $g(x) = e^{a+x} \\cdot e^{-x}$. Sa dérivée vaut $g'(x) = 0$, donc $g$ est constante. En évaluant en $x = 0$, on obtient $g(0) = e^a$, d'où $e^{a+b} \\cdot e^{-b} = e^a$ et finalement $e^{a+b} = e^a \\cdot e^b$.

### Propriétés déduites

Pour tous réels $a$ et $b$, et tout entier $n$ :

| Propriété | Formule |
|-----------|---------|
| Produit | $e^{a+b} = e^a \\cdot e^b$ |
| Quotient | $e^{a-b} = \\dfrac{e^a}{e^b}$ |
| Inverse | $e^{-a} = \\dfrac{1}{e^a}$ |
| Puissance | $(e^a)^n = e^{na}$ |
| Valeur en 0 | $e^0 = 1$ |
| Valeur en 1 | $e^1 = e$ |

### Exemples de simplification

**Exemple 1 :** Simplifier $A = e^3 \\cdot e^{-5} \\cdot e^2$.

$$A = e^{3 + (-5) + 2} = e^{0} = 1$$

**Exemple 2 :** Simplifier $B = \\dfrac{e^{2x+1}}{e^{x-3}}$.

$$B = e^{(2x+1)-(x-3)} = e^{x+4}$$

**Exemple 3 :** Développer $C = (e^x - 1)(e^x + 1)$.

$$C = (e^x)^2 - 1^2 = e^{2x} - 1$$

---

## Équations et inéquations avec l'exponentielle

### Unicité de l'exponentielle

Pour tous réels $a$ et $b$ :

$$e^a = e^b \\iff a = b$$

L'exponentielle est une fonction **injective** (ou « strictement monotone »), ce qui permet de résoudre des équations.

### Résolution d'équations

**Exemple :** Résoudre $e^{2x-1} = e^{x+3}$.

$$e^{2x-1} = e^{x+3} \\iff 2x - 1 = x + 3 \\iff x = 4$$

**Exemple :** Résoudre $e^{x^2} = e^{4}$.

$$e^{x^2} = e^{4} \\iff x^2 = 4 \\iff x = 2 \\text{ ou } x = -2$$

### Signe de l'exponentielle

Comme $e^x > 0$ pour tout $x$ :

$$e^a > e^b \\iff a > b$$

**Exemple :** Résoudre $e^{3x-2} > e^{x+1}$.

$$3x - 2 > x + 1 \\iff 2x > 3 \\iff x > \\frac{3}{2}$$

L'ensemble des solutions est $\\left]\\frac{3}{2} ; +\\infty\\right[$.

---

## Tableau de valeurs remarquables

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|-----|------|------|-----|-----|-----|-----|
| $e^x$ | $\\approx 0{,}14$ | $\\approx 0{,}37$ | $1$ | $\\approx 2{,}72$ | $\\approx 7{,}39$ | $\\approx 20{,}09$ |

---

## À retenir

- La fonction exponentielle est l'**unique** fonction égale à sa propre dérivée et valant 1 en 0.
- $e^x > 0$ pour tout réel $x$.
- Les règles de calcul sur les exposants se transposent directement.
- $e^a = e^b \\iff a = b$ et $e^a > e^b \\iff a > b$.
""",
                'quiz': {
                    'titre': 'Quiz — Définition et propriétés algébriques de l\'exponentielle',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "La fonction exponentielle est l'unique fonction $f$ dérivable sur $\\\\mathbb{R}$ telle que :",
                            'options': ["$f' = 2f$ et $f(0) = 1$", "$f' = f$ et $f(0) = 1$", "$f' = f$ et $f(1) = 0$", "$f' = f^2$ et $f(0) = 1$"],
                            'reponse_correcte': '1',
                            'explication': "La fonction exponentielle vérifie $f' = f$ et $f(0) = 1$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Que vaut $e^0$ ?",
                            'options': ["$0$", "$1$", "$e$", "$-1$"],
                            'reponse_correcte': '1',
                            'explication': "$e^0 = 1$ est une propriété fondamentale.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Simplifier $e^3 \\\\cdot e^{-5} \\\\cdot e^2$ :",
                            'options': ["$e^{10}$", "$e^{-4}$", "$e^0 = 1$", "$e^{30}$"],
                            'reponse_correcte': '2',
                            'explication': "$e^{3+(-5)+2} = e^{0} = 1$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Simplifier $\\\\frac{e^{2x+1}}{e^{x-3}}$ :",
                            'options': ["$e^{x+4}$", "$e^{x-2}$", "$e^{3x-2}$", "$e^{x-4}$"],
                            'reponse_correcte': '0',
                            'explication': "$\\frac{e^{2x+1}}{e^{x-3}} = e^{(2x+1)-(x-3)} = e^{x+4}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Que vaut $e^{-a}$ ?",
                            'options': ["$-e^a$", "$\\\\frac{1}{e^a}$", "$e^a - 1$", "$\\\\frac{e^a}{a}$"],
                            'reponse_correcte': '1',
                            'explication': "$e^{-a} = \\frac{1}{e^a}$ est une propriété algébrique fondamentale.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Développer $(e^x - 1)(e^x + 1)$ :",
                            'options': ["$e^{2x}$", "$e^{2x} + 1$", "$e^{2x} - 1$", "$e^{x^2} - 1$"],
                            'reponse_correcte': '2',
                            'explication': "$(e^x)^2 - 1^2 = e^{2x} - 1$ (identité remarquable $a^2 - b^2$).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "La valeur approchée de $e$ est :",
                            'options': ["$3{,}14$", "$2{,}718$", "$1{,}618$", "$2{,}236$"],
                            'reponse_correcte': '1',
                            'explication': "$e \\approx 2{,}718$ (nombre d'Euler).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Pour tout réel $x$, $e^x$ est :",
                            'options': ["Toujours négatif", "Toujours nul", "Strictement positif", "Positif ou nul"],
                            'reponse_correcte': '2',
                            'explication': "$e^x > 0$ pour tout $x \\in \\mathbb{R}$. L'exponentielle ne s'annule jamais.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Résoudre $e^{2x-1} = e^{x+3}$ :",
                            'options': ["$x = 2$", "$x = 4$", "$x = -4$", "$x = 1$"],
                            'reponse_correcte': '1',
                            'explication': "$e^{2x-1} = e^{x+3} \\Leftrightarrow 2x - 1 = x + 3 \\Leftrightarrow x = 4$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Résoudre $e^{x^2} = e^{4}$ :",
                            'options': ["$x = 2$ uniquement", "$x = -2$ uniquement", "$x = 2$ ou $x = -2$", "$x = 4$"],
                            'reponse_correcte': '2',
                            'explication': "$x^2 = 4 \\Leftrightarrow x = 2$ ou $x = -2$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "L'ensemble des solutions de $e^{3x-2} > e^{x+1}$ est :",
                            'options': ["$\\\\left]-\\\\infty ; \\\\frac{3}{2}\\\\right[$", "$\\\\left]\\\\frac{3}{2} ; +\\\\infty\\\\right[$", "$\\\\left]0 ; +\\\\infty\\\\right[$", "$\\\\left]-\\\\infty ; 3\\\\right[$"],
                            'reponse_correcte': '1',
                            'explication': "$3x - 2 > x + 1 \\Rightarrow 2x > 3 \\Rightarrow x > \\frac{3}{2}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Que vaut $(e^a)^n$ ?",
                            'options': ["$e^{a+n}$", "$e^{a/n}$", "$e^{na}$", "$n \\\\cdot e^a$"],
                            'reponse_correcte': '2',
                            'explication': "$(e^a)^n = e^{na}$ est la propriété de puissance.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Simplifier $\\\\frac{(e^x)^3 \\\\cdot e^{-x}}{e^{2x}}$ :",
                            'options': ["$1$", "$e^x$", "$e^{-x}$", "$e^{2x}$"],
                            'reponse_correcte': '0',
                            'explication': "$\\frac{e^{3x} \\cdot e^{-x}}{e^{2x}} = \\frac{e^{2x}}{e^{2x}} = e^0 = 1$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Résoudre $e^{2x} - 3e^x + 2 = 0$ (poser $X = e^x$) :",
                            'options': ["$x = 0$ ou $x = \\\\ln 2$", "$x = 1$ ou $x = 2$", "$x = \\\\ln 3$", "$x = 0$ uniquement"],
                            'reponse_correcte': '0',
                            'explication': "$X^2 - 3X + 2 = 0 \\Rightarrow (X-1)(X-2) = 0 \\Rightarrow X = 1$ ou $X = 2$. Donc $e^x = 1 \\Rightarrow x = 0$ ou $e^x = 2 \\Rightarrow x = \\ln 2$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "$e^{a+b} = e^a + e^b$.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "$e^{a+b} = e^a \\cdot e^b$ (produit, pas somme).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "L'exponentielle est une fonction injective : $e^a = e^b \\\\Leftrightarrow a = b$.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "L'exponentielle est strictement monotone (croissante), donc injective.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Il existe un réel $x$ tel que $e^x = 0$.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "$e^x > 0$ pour tout $x \\in \\mathbb{R}$, l'exponentielle ne s'annule jamais.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Simplifier $e^5 \\\\cdot e^{-3}$ sous la forme $e^n$. Quelle est la valeur de $n$ ?",
                            'options': None,
                            'reponse_correcte': '2',
                            'tolerances': [],
                            'explication': "$e^5 \\cdot e^{-3} = e^{5+(-3)} = e^2$, donc $n = 2$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Résoudre $e^{3x} = e^{12}$. Donner la valeur de $x$.",
                            'options': None,
                            'reponse_correcte': '4',
                            'tolerances': ['x = 4', 'x=4'],
                            'explication': "$3x = 12 \\Rightarrow x = 4$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Que vaut $e^1$ arrondi au centième ?",
                            'options': None,
                            'reponse_correcte': '2.72',
                            'tolerances': ['2,72', '2.718', '2,718', '2.71', '2,71'],
                            'explication': "$e^1 = e \\approx 2{,}718 \\approx 2{,}72$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Dérivation et variations',
                'duree': 35,
                'contenu': """# Dérivation et variations de la fonction exponentielle

## Introduction

La fonction exponentielle possède des propriétés de dérivation remarquablement simples : elle est sa propre dérivée. Cette propriété fondatrice entraîne des conséquences importantes sur ses variations et ses limites, que nous étudions dans cette leçon.

---

## Dérivée de la fonction exponentielle

### Dérivée de $e^x$

$$\\left(e^x\\right)' = e^x$$

C'est la **seule** fonction (à une constante multiplicative près) égale à sa propre dérivée.

### Dérivée de $e^{u(x)}$ (dérivée composée)

Si $u$ est une fonction dérivable sur un intervalle $I$, alors la fonction $x \\mapsto e^{u(x)}$ est dérivable sur $I$ et :

$$\\left(e^{u(x)}\\right)' = u'(x) \\cdot e^{u(x)}$$

### Exemples

**Exemple 1 :** Dériver $f(x) = e^{3x+2}$.

Ici $u(x) = 3x + 2$, donc $u'(x) = 3$.

$$f'(x) = 3e^{3x+2}$$

**Exemple 2 :** Dériver $g(x) = e^{x^2 - 1}$.

Ici $u(x) = x^2-1$, donc $u'(x) = 2x$.

$$g'(x) = 2x \\cdot e^{x^2-1}$$

**Exemple 3 :** Dériver $h(x) = x \\cdot e^x$.

On utilise la formule du produit $(uv)' = u'v + uv'$ :

$$h'(x) = 1 \\cdot e^x + x \\cdot e^x = (1+x)e^x$$

**Exemple 4 :** Dériver $k(x) = \\dfrac{e^x}{x}$ pour $x \\neq 0$.

$$k'(x) = \\frac{e^x \\cdot x - e^x \\cdot 1}{x^2} = \\frac{(x-1)e^x}{x^2}$$

---

## Variations de la fonction exponentielle

Puisque $e^x > 0$ pour tout $x \\in \\mathbb{R}$, et que $(e^x)' = e^x > 0$, la fonction exponentielle est **strictement croissante** sur $\\mathbb{R}$.

### Tableau de variations

| $x$ | $-\\infty$ | | $+\\infty$ |
|-----|----------|--------|---------|
| $e^x$ | $0^+$ | $\\nearrow$ | $+\\infty$ |

### Limites aux bornes

$$\\lim_{x \\to -\\infty} e^x = 0 \\qquad \\text{et} \\qquad \\lim_{x \\to +\\infty} e^x = +\\infty$$

> **Interprétation graphique :** L'axe des abscisses ($y = 0$) est **asymptote horizontale** à la courbe de $e^x$ en $-\\infty$.

---

## Croissances comparées

Les résultats de **croissances comparées** affirment que l'exponentielle « l'emporte » sur toute puissance de $x$.

### En $+\\infty$

Pour tout entier naturel $n \\geq 1$ :

$$\\lim_{x \\to +\\infty} \\frac{e^x}{x^n} = +\\infty$$

> L'exponentielle croît plus vite que n'importe quel polynôme.

### En $-\\infty$

Pour tout entier naturel $n \\geq 1$ :

$$\\lim_{x \\to -\\infty} x^n \\cdot e^x = 0$$

> Le facteur $e^x$ force le produit vers 0 malgré la divergence de $x^n$.

### Applications

**Exemple 1 :** Calculer $\\displaystyle\\lim_{x \\to +\\infty} (x^2 - 3x) e^{-x}$.

On écrit : $(x^2 - 3x)e^{-x} = \\dfrac{x^2 - 3x}{e^x}$. Par croissance comparée, $\\dfrac{x^2}{e^x} \\to 0$ et $\\dfrac{x}{e^x} \\to 0$, donc :

$$\\lim_{x \\to +\\infty} (x^2 - 3x)e^{-x} = 0$$

**Exemple 2 :** Calculer $\\displaystyle\\lim_{x \\to +\\infty} e^x - x$.

On factorise : $e^x - x = e^x\\left(1 - \\dfrac{x}{e^x}\\right)$. Comme $\\dfrac{x}{e^x} \\to 0$, la parenthèse tend vers 1, et $e^x \\to +\\infty$, donc :

$$\\lim_{x \\to +\\infty} (e^x - x) = +\\infty$$

---

## Étude complète d'une fonction

**Exemple :** Étudier $f(x) = (2x-1)e^x$ sur $\\mathbb{R}$.

**1. Dérivée :**

$$f'(x) = 2e^x + (2x-1)e^x = (2x+1)e^x$$

**2. Signe de $f'(x)$ :**

Comme $e^x > 0$, le signe de $f'(x)$ est celui de $2x+1$.

- $f'(x) = 0 \\iff x = -\\frac{1}{2}$
- $f'(x) > 0 \\iff x > -\\frac{1}{2}$
- $f'(x) < 0 \\iff x < -\\frac{1}{2}$

**3. Tableau de variations :**

| $x$ | $-\\infty$ | | $-\\frac{1}{2}$ | | $+\\infty$ |
|-----|----------|---|-----------|---|---------|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | $0$ | $\\searrow$ | $-2e^{-1/2}$ | $\\nearrow$ | $+\\infty$ |

Le minimum est $f\\left(-\\frac{1}{2}\\right) = (2 \\cdot (-\\frac{1}{2})-1)e^{-1/2} = -2e^{-1/2} \\approx -1{,}21$.

---

## À retenir

- $(e^x)' = e^x$ et $(e^{u})' = u' \\cdot e^{u}$.
- $e^x$ est strictement croissante sur $\\mathbb{R}$, avec $\\lim_{-\\infty} e^x = 0$ et $\\lim_{+\\infty} e^x = +\\infty$.
- **Croissances comparées** : l'exponentielle domine toute puissance de $x$.
- Pour étudier le signe de $f'(x)$ quand elle contient $e^x$, on utilise $e^x > 0$.
""",
                'quiz': {
                    'titre': 'Quiz — Dérivation et variations de l\'exponentielle',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Que vaut $(e^x)'$ ?",
                            'options': ["$x e^{x-1}$", "$e^x$", "$\\\\frac{1}{e^x}$", "$e^{x-1}$"],
                            'reponse_correcte': '1',
                            'explication': "La dérivée de $e^x$ est $e^x$ elle-même.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Que vaut $(e^{3x+2})'$ ?",
                            'options': ["$e^{3x+2}$", "$3e^{3x+2}$", "$(3x+2)e^{3x+2}$", "$3e^{3x}$"],
                            'reponse_correcte': '1',
                            'explication': "$(e^{u})' = u' \\cdot e^{u}$, avec $u = 3x+2$, $u' = 3$, d'où $3e^{3x+2}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "La fonction exponentielle est :",
                            'options': ["Strictement décroissante sur $\\\\mathbb{R}$", "Strictement croissante sur $\\\\mathbb{R}$", "Croissante puis décroissante", "Constante"],
                            'reponse_correcte': '1',
                            'explication': "$(e^x)' = e^x > 0$ pour tout $x$, donc $e^x$ est strictement croissante sur $\\mathbb{R}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\lim_{x \\\\to -\\\\infty} e^x$ ?",
                            'options': ["$+\\\\infty$", "$1$", "$0$", "$-\\\\infty$"],
                            'reponse_correcte': '2',
                            'explication': "$\\lim_{x \\to -\\infty} e^x = 0$ (l'axe des abscisses est asymptote horizontale en $-\\infty$).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\lim_{x \\\\to +\\\\infty} \\\\frac{e^x}{x^2}$ ?",
                            'options': ["$0$", "$1$", "$+\\\\infty$", "$e$"],
                            'reponse_correcte': '2',
                            'explication': "Par croissance comparée, l'exponentielle l'emporte sur toute puissance : $\\lim_{x \\to +\\infty} \\frac{e^x}{x^n} = +\\infty$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\lim_{x \\\\to -\\\\infty} x^3 e^x$ ?",
                            'options': ["$+\\\\infty$", "$-\\\\infty$", "$0$", "$1$"],
                            'reponse_correcte': '2',
                            'explication': "Par croissances comparées en $-\\infty$ : $\\lim_{x \\to -\\infty} x^n e^x = 0$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Que vaut $(e^{x^2 - 1})'$ ?",
                            'options': ["$(x^2-1)e^{x^2-1}$", "$2x e^{x^2-1}$", "$e^{2x}$", "$2e^{x^2-1}$"],
                            'reponse_correcte': '1',
                            'explication': "$u = x^2 - 1$, $u' = 2x$, donc $(e^{u})' = 2x \\cdot e^{x^2-1}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Si $h(x) = x \\\\cdot e^x$, que vaut $h'(x)$ ?",
                            'options': ["$e^x$", "$x e^x$", "$(1+x)e^x$", "$(x-1)e^x$"],
                            'reponse_correcte': '2',
                            'explication': "$(uv)' = u'v + uv' = 1 \\cdot e^x + x \\cdot e^x = (1+x)e^x$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Si $k(x) = \\\\frac{e^x}{x}$, le signe de $k'(x)$ dépend de :",
                            'options': ["$e^x$ uniquement", "$x - 1$", "$x + 1$", "$x^2$"],
                            'reponse_correcte': '1',
                            'explication': "$k'(x) = \\frac{(x-1)e^x}{x^2}$, et comme $e^x > 0$ et $x^2 > 0$, le signe dépend de $x - 1$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "L'axe des abscisses est asymptote à $e^x$ en :",
                            'options': ["$+\\\\infty$", "$-\\\\infty$", "$0$", "Il n'y a pas d'asymptote horizontale"],
                            'reponse_correcte': '1',
                            'explication': "$\\lim_{x \\to -\\infty} e^x = 0$, donc $y = 0$ est asymptote horizontale en $-\\infty$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Pour $f(x) = (2x-1)e^x$, $f'(x)$ vaut :",
                            'options': ["$2e^x$", "$(2x-1)e^x$", "$(2x+1)e^x$", "$(2x+3)e^x$"],
                            'reponse_correcte': '2',
                            'explication': "$f'(x) = 2e^x + (2x-1)e^x = (2x+1)e^x$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Pour $f(x) = (2x-1)e^x$, le minimum est atteint en $x = $ :",
                            'options': ["$0$", "$\\\\frac{1}{2}$", "$-\\\\frac{1}{2}$", "$-1$"],
                            'reponse_correcte': '2',
                            'explication': "$f'(x) = (2x+1)e^x = 0 \\Rightarrow x = -\\frac{1}{2}$. Le signe de $f'$ change de $-$ à $+$, c'est un minimum.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Pour étudier le signe de $f'(x) = (3-x)e^x$, on utilise le fait que :",
                            'options': ["$e^x$ peut être négatif", "$e^x > 0$ donc le signe dépend de $3-x$", "$e^x = 0$ pour $x = 0$", "Il faut dériver une seconde fois"],
                            'reponse_correcte': '1',
                            'explication': "Comme $e^x > 0$ pour tout $x$, le signe de $f'(x)$ est celui de $3 - x$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\lim_{x \\\\to +\\\\infty} (e^x - x)$ ?",
                            'options': ["$0$", "$-\\\\infty$", "$+\\\\infty$", "$1$"],
                            'reponse_correcte': '2',
                            'explication': "$e^x - x = e^x(1 - xe^{-x})$. Comme $xe^{-x} \\to 0$, on a $e^x - x \\to +\\infty$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "La fonction $e^x$ admet un maximum sur $\\\\mathbb{R}$.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "$e^x$ est strictement croissante et $\\lim_{+\\infty} e^x = +\\infty$ : elle n'admet pas de maximum.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "$(e^{2x})' = 2e^{2x}$.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "$u = 2x$, $u' = 2$, donc $(e^{2x})' = 2e^{2x}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "$\\\\lim_{x \\\\to +\\\\infty} \\\\frac{x^{100}}{e^x} = +\\\\infty$.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "Par croissances comparées, $\\lim_{x \\to +\\infty} \\frac{x^n}{e^x} = 0$ pour tout $n$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer $(e^{-5x})'$.",
                            'options': None,
                            'reponse_correcte': '-5e^(-5x)',
                            'tolerances': ['-5e^{-5x}', '-5*e^(-5x)', '-5exp(-5x)'],
                            'explication': "$u = -5x$, $u' = -5$, donc $(e^{-5x})' = -5e^{-5x}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Donner $\\\\lim_{x \\\\to +\\\\infty} e^x$.",
                            'options': None,
                            'reponse_correcte': '+infini',
                            'tolerances': ['+inf', 'infini', '+∞', '∞', 'infinity'],
                            'explication': "$\\lim_{x \\to +\\infty} e^x = +\\infty$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Si $f(x) = (x+2)e^x$, en quelle valeur de $x$ la fonction admet-elle un extremum ?",
                            'options': None,
                            'reponse_correcte': '-3',
                            'tolerances': ['x = -3', 'x=-3'],
                            'explication': "$f'(x) = e^x + (x+2)e^x = (x+3)e^x$. $f'(x) = 0 \\Rightarrow x = -3$. C'est un minimum car $f'$ change de signe de $-$ à $+$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 3,
                'titre': 'Modèles exponentiels et équations différentielles',
                'duree': 30,
                'contenu': """# Modèles exponentiels et équations différentielles

## Introduction

La fonction exponentielle n'est pas qu'un objet mathématique abstrait : elle modélise de nombreux phénomènes concrets en physique, biologie et économie. Dans cette leçon, nous explorons les **équations différentielles** du premier ordre et les modèles de **croissance** et **décroissance** exponentielles.

---

## Équation différentielle $y' = ay$

### Définition

Une **équation différentielle** est une équation dont l'inconnue est une fonction et qui fait intervenir sa dérivée.

L'équation différentielle la plus simple est :

$$y' = ay$$

où $a$ est une constante réelle.

### Théorème

Les solutions de l'équation $y' = ay$ sont les fonctions de la forme :

$$y(x) = C \\cdot e^{ax}$$

où $C$ est une constante réelle.

> **Démonstration (vérification) :** Si $y(x) = Ce^{ax}$, alors $y'(x) = Cae^{ax} = a \\cdot Ce^{ax} = a \\cdot y(x)$. ✓

### Condition initiale

Si on impose $y(0) = y_0$, alors $C = y_0$ et la solution unique est :

$$y(x) = y_0 \\cdot e^{ax}$$

**Exemple :** Trouver la fonction $f$ telle que $f' = 3f$ et $f(0) = 5$.

$$f(x) = 5 \\cdot e^{3x}$$

---

## Modèle de croissance exponentielle

### Croissance d'une population

Lorsqu'une population croît de manière proportionnelle à son effectif, son évolution suit le modèle :

$$N(t) = N_0 \\cdot e^{kt}$$

où :
- $N_0$ est l'effectif initial (à $t = 0$),
- $k > 0$ est le **taux de croissance**,
- $t$ est le temps.

**Exemple :** Une colonie de bactéries double toutes les 2 heures. Si l'effectif initial est $N_0 = 1000$ :

On cherche $k$ tel que $N(2) = 2N_0$, soit $e^{2k} = 2$, d'où $k = \\dfrac{\\ln 2}{2} \\approx 0{,}347$.

$$N(t) = 1000 \\cdot e^{0{,}347\\,t}$$

Après 6 heures : $N(6) = 1000 \\cdot e^{0{,}347 \\times 6} \\approx 1000 \\times 8 = 8000$ bactéries.

---

## Modèle de décroissance exponentielle

### Décroissance radioactive

Un noyau radioactif se désintègre selon la loi :

$$N(t) = N_0 \\cdot e^{-\\lambda t}$$

où $\\lambda > 0$ est la **constante de désintégration**.

### Temps de demi-vie

Le **temps de demi-vie** $t_{1/2}$ est le temps au bout duquel la moitié des noyaux se sont désintégrés :

$$N(t_{1/2}) = \\frac{N_0}{2} \\implies e^{-\\lambda t_{1/2}} = \\frac{1}{2} \\implies t_{1/2} = \\frac{\\ln 2}{\\lambda}$$

**Exemple :** Le carbone 14 a une demi-vie de $t_{1/2} = 5730$ ans.

$$\\lambda = \\frac{\\ln 2}{5730} \\approx 1{,}21 \\times 10^{-4} \\text{ an}^{-1}$$

Si un échantillon contient 75 % de carbone 14 par rapport à l'original :

$$0{,}75 = e^{-\\lambda t} \\implies t = \\frac{-\\ln(0{,}75)}{\\lambda} \\approx \\frac{0{,}288}{1{,}21 \\times 10^{-4}} \\approx 2380 \\text{ ans}$$

---

## Autres modèles

### Refroidissement de Newton

La température d'un corps dans un milieu ambiant de température $T_a$ vérifie :

$$T(t) = T_a + (T_0 - T_a) \\cdot e^{-kt}$$

où $T_0$ est la température initiale et $k > 0$.

**Exemple :** Un café à $90°C$ refroidit dans une pièce à $20°C$ avec $k = 0{,}05$.

$$T(t) = 20 + 70 \\cdot e^{-0{,}05t}$$

Au bout de 10 minutes : $T(10) = 20 + 70 \\cdot e^{-0{,}5} \\approx 20 + 42{,}4 \\approx 62{,}4°C$.

### Capitalisation continue

Un capital $C_0$ placé à un taux annuel $r$ en capitalisation continue vaut :

$$C(t) = C_0 \\cdot e^{rt}$$

**Exemple :** $1000$ € placés à $3\\%$ continu :

$$C(10) = 1000 \\cdot e^{0{,}03 \\times 10} = 1000 \\cdot e^{0{,}3} \\approx 1349{,}86 \\text{ €}$$

---

## Résumé des modèles

| Phénomène | Équation | Paramètre |
|-----------|----------|-----------|
| Croissance bactérienne | $N(t) = N_0 e^{kt}$ | $k > 0$ |
| Décroissance radioactive | $N(t) = N_0 e^{-\\lambda t}$ | $\\lambda > 0$ |
| Refroidissement | $T(t) = T_a + (T_0-T_a)e^{-kt}$ | $k > 0$ |
| Capitalisation continue | $C(t) = C_0 e^{rt}$ | $r > 0$ |

---

## À retenir

- L'équation $y' = ay$ a pour solutions $y = Ce^{ax}$.
- Avec $y(0) = y_0$, la solution unique est $y = y_0 e^{ax}$.
- Si $a > 0$ : croissance exponentielle ; si $a < 0$ : décroissance exponentielle.
- Le temps de demi-vie est $t_{1/2} = \\dfrac{\\ln 2}{\\lambda}$.
""",
                'quiz': {
                    'titre': 'Quiz — Modèles exponentiels et équations différentielles',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Les solutions de l'équation différentielle $y' = ay$ sont de la forme :",
                            'options': ["$y = ax + C$", "$y = Ce^{ax}$", "$y = Ca^x$", "$y = e^{Cx}$"],
                            'reponse_correcte': '1',
                            'explication': "Les solutions de $y' = ay$ sont les fonctions $y(x) = Ce^{ax}$ où $C$ est une constante réelle.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Si $y' = 3y$ et $y(0) = 5$, quelle est la solution ?",
                            'options': ["$y = 3e^{5x}$", "$y = 5e^{3x}$", "$y = 15e^x$", "$y = e^{15x}$"],
                            'reponse_correcte': '1',
                            'explication': "Avec la condition initiale $y(0) = 5$, on a $C = 5$ et $a = 3$, d'où $y = 5e^{3x}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Un modèle de croissance exponentielle correspond à $a$ :",
                            'options': ["Nul", "Strictement positif", "Strictement négatif", "Quelconque"],
                            'reponse_correcte': '1',
                            'explication': "Si $a > 0$, $y = Ce^{ax}$ croît exponentiellement avec $x$ (si $C > 0$).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "La formule du temps de demi-vie $t_{1/2}$ est :",
                            'options': ["$\\\\frac{\\\\lambda}{\\\\ln 2}$", "$\\\\frac{\\\\ln 2}{\\\\lambda}$", "$\\\\frac{1}{\\\\lambda}$", "$\\\\frac{2}{\\\\lambda}$"],
                            'reponse_correcte': '1',
                            'explication': "Le temps de demi-vie est $t_{1/2} = \\frac{\\ln 2}{\\lambda}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La décroissance radioactive suit le modèle :",
                            'options': ["$N(t) = N_0 \\\\cdot e^{\\\\lambda t}$", "$N(t) = N_0 \\\\cdot e^{-\\\\lambda t}$", "$N(t) = N_0 - \\\\lambda t$", "$N(t) = N_0 / (1 + \\\\lambda t)$"],
                            'reponse_correcte': '1',
                            'explication': "La décroissance radioactive suit $N(t) = N_0 e^{-\\lambda t}$ avec $\\lambda > 0$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Dans le modèle de refroidissement de Newton, la température limite quand $t \\\\to +\\\\infty$ est :",
                            'options': ["$T_0$", "$T_a$", "$0$", "$T_0 - T_a$"],
                            'reponse_correcte': '1',
                            'explication': "$T(t) = T_a + (T_0 - T_a)e^{-kt}$, et $\\lim_{t \\to +\\infty} e^{-kt} = 0$, donc $T \\to T_a$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Si $N(t) = 1000 e^{-0{,}1 t}$, quelle est la valeur de $N(0)$ ?",
                            'options': ["$0$", "$100$", "$1000$", "$e^{-0{,}1}$"],
                            'reponse_correcte': '2',
                            'explication': "$N(0) = 1000 e^{0} = 1000$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Un capital $C_0$ placé en capitalisation continue à taux $r$ vaut après $t$ années :",
                            'options': ["$C_0(1 + r)^t$", "$C_0 e^{rt}$", "$C_0 + rt$", "$C_0 \\\\cdot r^t$"],
                            'reponse_correcte': '1',
                            'explication': "En capitalisation continue, $C(t) = C_0 e^{rt}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Si une population double toutes les 3 heures, quelle est la constante $k$ (en $h^{-1}$) ?",
                            'options': ["$\\\\frac{\\\\ln 2}{3}$", "$\\\\frac{3}{\\\\ln 2}$", "$\\\\frac{2}{3}$", "$3 \\\\ln 2$"],
                            'reponse_correcte': '0',
                            'explication': "$e^{3k} = 2 \\Rightarrow k = \\frac{\\ln 2}{3}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "1000 € placés à 5 % en capitalisation continue valent après 10 ans :",
                            'options': ["$1000 \\\\cdot e^{5}$", "$1000 \\\\cdot e^{0{,}5}$", "$1000 \\\\cdot (1{,}05)^{10}$", "$1050$"],
                            'reponse_correcte': '1',
                            'explication': "$C(10) = 1000 e^{0{,}05 \\times 10} = 1000 e^{0{,}5} \\approx 1648{,}72$ €.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Si $N(t) = 500 e^{-0{,}2t}$, au bout de combien de temps (approx.) la valeur a-t-elle diminué de moitié ?",
                            'options': ["$\\\\frac{\\\\ln 2}{0{,}2} \\\\approx 3{,}47$", "$\\\\frac{0{,}2}{\\\\ln 2} \\\\approx 0{,}29$", "$5$", "$10$"],
                            'reponse_correcte': '0',
                            'explication': "$t_{1/2} = \\frac{\\ln 2}{0{,}2} = \\frac{0{,}693}{0{,}2} \\approx 3{,}47$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Le carbone 14 a $t_{1/2} = 5730$ ans. Sa constante de désintégration $\\\\lambda$ vaut environ :",
                            'options': ["$0{,}693$", "$1{,}21 \\\\times 10^{-4}$ an$^{-1}$", "$5730 / \\\\ln 2$", "$\\\\ln(5730)$"],
                            'reponse_correcte': '1',
                            'explication': "$\\lambda = \\frac{\\ln 2}{5730} \\approx \\frac{0{,}693}{5730} \\approx 1{,}21 \\times 10^{-4}$ an$^{-1}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Un café à 90°C refroidit dans une pièce à 20°C avec $k = 0{,}05$. Après 10 min, $T$ vaut environ :",
                            'options': ["$55°C$", "$62{,}4°C$", "$70°C$", "$45°C$"],
                            'reponse_correcte': '1',
                            'explication': "$T(10) = 20 + 70 e^{-0{,}5} \\approx 20 + 70 \\times 0{,}607 \\approx 62{,}4°C$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Pour vérifier que $y = Ce^{ax}$ est solution de $y' = ay$, on calcule :",
                            'options': ["$y' = Ce^{ax}$ et on compare à $y$", "$y' = Cae^{ax}$ et on compare à $ay = Cae^{ax}$", "$y' = Ce^{x}$ et $ay = aCe^{ax}$", "$y' = ae^{x}$"],
                            'reponse_correcte': '1',
                            'explication': "$y' = Cae^{ax} = a \\cdot Ce^{ax} = ay$. ✓",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Si $a < 0$, la solution de $y' = ay$ décrit une décroissance exponentielle.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "$a < 0$ implique que $e^{ax} \\to 0$ quand $x \\to +\\infty$, soit une décroissance.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Le temps de demi-vie dépend de la quantité initiale $N_0$.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "$t_{1/2} = \\frac{\\ln 2}{\\lambda}$ ne dépend que de $\\lambda$, pas de $N_0$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "La solution de $y' = -2y$ avec $y(0) = 3$ est $y = 3e^{-2x}$.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "$a = -2$, $C = y(0) = 3$, donc $y = 3e^{-2x}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Donner la solution de $y' = 4y$ avec $y(0) = 2$ sous la forme $y = ...$.",
                            'options': None,
                            'reponse_correcte': '2e^(4x)',
                            'tolerances': ['2*e^(4x)', '2exp(4x)', '2e^{4x}'],
                            'explication': "$y = 2e^{4x}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Si $\\\\lambda = 0{,}1$ an$^{-1}$, calculer $t_{1/2}$ en années (arrondi à l'entier).",
                            'options': None,
                            'reponse_correcte': '7',
                            'tolerances': ['7 ans', '6.93', '6,93'],
                            'explication': "$t_{1/2} = \\frac{\\ln 2}{0{,}1} = \\frac{0{,}693}{0{,}1} \\approx 6{,}93 \\approx 7$ ans.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Combien vaut $N(t_{1/2})$ si $N_0 = 800$ ? (nombre entier)",
                            'options': None,
                            'reponse_correcte': '400',
                            'tolerances': [],
                            'explication': "Par définition, $N(t_{1/2}) = \\frac{N_0}{2} = \\frac{800}{2} = 400$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 6 — Probabilités conditionnelles
    # ──────────────────────────────────────────────
    {
        'ordre': 6,
        'titre': 'Probabilités conditionnelles',
        'description': "Probabilités conditionnelles, indépendance, formule des probabilités totales, variables aléatoires et loi binomiale.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Probabilités conditionnelles et indépendance',
                'duree': 35,
                'contenu': """# Probabilités conditionnelles et indépendance

## Introduction

En classe de Seconde, vous avez étudié les probabilités d'événements simples. En Première, on enrichit ce cadre en introduisant la **probabilité conditionnelle** : la probabilité qu'un événement se réalise **sachant** qu'un autre événement a eu lieu. Cette notion est essentielle en statistiques, en médecine (tests de dépistage) et en sciences de l'information.

---

## Probabilité conditionnelle

### Définition

Soit $B$ un événement de probabilité non nulle ($P(B) > 0$). La **probabilité conditionnelle de $A$ sachant $B$** est :

$$P(A|B) = \\frac{P(A \\cap B)}{P(B)}$$

> **Interprétation :** $P(A|B)$ mesure la probabilité de $A$ lorsqu'on sait que $B$ est réalisé. L'univers « se réduit » à $B$.

### Exemple fondateur

On lance un dé équilibré. Soit $A$ = « obtenir 6 » et $B$ = « obtenir un nombre pair ».

$$P(A|B) = \\frac{P(A \\cap B)}{P(B)} = \\frac{P(\\{6\\})}{P(\\{2,4,6\\})} = \\frac{1/6}{3/6} = \\frac{1}{3}$$

Sachant que le résultat est pair, il y a une chance sur trois d'avoir obtenu 6.

### Propriété multiplicative

De la définition, on déduit immédiatement :

$$P(A \\cap B) = P(A|B) \\cdot P(B) = P(B|A) \\cdot P(A)$$

Cette formule est très utile pour calculer $P(A \\cap B)$ à partir d'un arbre pondéré.

---

## Arbres pondérés

Un **arbre pondéré** (ou arbre de probabilité) est un outil graphique permettant de représenter et calculer des probabilités conditionnelles.

### Règles de construction

1. Chaque branche porte la probabilité de l'événement **sachant** le nœud parent.
2. La somme des probabilités issues d'un même nœud vaut **1**.
3. La probabilité d'un chemin est le **produit** des probabilités le long des branches.
4. $P(A)$ est la **somme** des probabilités des chemins menant à $A$.

### Exemple

Un sac contient 3 boules rouges et 2 boules vertes. On tire deux boules successivement **sans remise**.

**Premier tirage :** $P(R_1) = \\frac{3}{5}$, $P(V_1) = \\frac{2}{5}$.

**Deuxième tirage sachant $R_1$ :** $P(R_2|R_1) = \\frac{2}{4} = \\frac{1}{2}$, $P(V_2|R_1) = \\frac{2}{4} = \\frac{1}{2}$.

**Deuxième tirage sachant $V_1$ :** $P(R_2|V_1) = \\frac{3}{4}$, $P(V_2|V_1) = \\frac{1}{4}$.

Ainsi :

$$P(R_1 \\cap R_2) = \\frac{3}{5} \\times \\frac{1}{2} = \\frac{3}{10}$$

$$P(\\text{deux boules de même couleur}) = P(R_1 \\cap R_2) + P(V_1 \\cap V_2) = \\frac{3}{10} + \\frac{2}{5} \\times \\frac{1}{4} = \\frac{3}{10} + \\frac{1}{10} = \\frac{4}{10} = \\frac{2}{5}$$

---

## Formule des probabilités totales

### Théorème

Si $B_1, B_2, \\ldots, B_n$ forment une **partition** de l'univers $\\Omega$ (événements incompatibles dont la réunion est $\\Omega$, chacun de probabilité non nulle), alors pour tout événement $A$ :

$$P(A) = \\sum_{i=1}^{n} P(A|B_i) \\cdot P(B_i)$$

### Cas usuel : partition en deux

$$P(A) = P(A|B) \\cdot P(B) + P(A|\\overline{B}) \\cdot P(\\overline{B})$$

### Exemple

Un test de dépistage a les caractéristiques suivantes :
- Prévalence de la maladie : $P(M) = 0{,}02$.
- Le test est positif chez un malade : $P(T^+|M) = 0{,}95$.
- Le test est positif chez un non-malade : $P(T^+|\\overline{M}) = 0{,}03$.

Quelle est la probabilité d'avoir un test positif ?

$$P(T^+) = P(T^+|M) \\cdot P(M) + P(T^+|\\overline{M}) \\cdot P(\\overline{M})$$
$$= 0{,}95 \\times 0{,}02 + 0{,}03 \\times 0{,}98 = 0{,}019 + 0{,}0294 = 0{,}0484$$

---

## Indépendance

### Définition

Deux événements $A$ et $B$ sont **indépendants** si et seulement si :

$$P(A \\cap B) = P(A) \\cdot P(B)$$

> L'indépendance signifie que la réalisation de $B$ ne modifie pas la probabilité de $A$ : $P(A|B) = P(A)$.

### Vérification

**Exemple :** On lance deux dés. Soit $A$ = « le premier dé donne 6 » et $B$ = « le deuxième dé donne un nombre pair ».

$$P(A) = \\frac{1}{6}, \\quad P(B) = \\frac{1}{2}, \\quad P(A \\cap B) = \\frac{1}{6} \\times \\frac{1}{2} = \\frac{1}{12}$$

Comme $P(A \\cap B) = P(A) \\cdot P(B)$, les événements $A$ et $B$ sont **indépendants**. ✓

### Propriété

Si $A$ et $B$ sont indépendants, alors $A$ et $\\overline{B}$ sont aussi indépendants (de même $\\overline{A}$ et $B$, et $\\overline{A}$ et $\\overline{B}$).

### Attention

> L'indépendance **n'est pas** l'incompatibilité ! Deux événements incompatibles ($A \\cap B = \\emptyset$) de probabilités non nulles ne sont **jamais** indépendants.

---

## À retenir

- $P(A|B) = \\dfrac{P(A \\cap B)}{P(B)}$ (avec $P(B) > 0$).
- $P(A \\cap B) = P(A|B) \\cdot P(B)$.
- **Probabilités totales** : $P(A) = P(A|B)P(B) + P(A|\\overline{B})P(\\overline{B})$.
- **Indépendance** : $P(A \\cap B) = P(A) \\cdot P(B)$.
- Incompatibilité $\\neq$ indépendance.
""",
                'quiz': {
                    'titre': 'Quiz — Probabilités conditionnelles et indépendance',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "La probabilité conditionnelle $P(A|B)$ se calcule par :",
                            'options': ["$\\\\frac{P(B)}{P(A \\\\cap B)}$", "$\\\\frac{P(A \\\\cap B)}{P(B)}$", "$P(A) \\\\cdot P(B)$", "$\\\\frac{P(A \\\\cup B)}{P(B)}$"],
                            'reponse_correcte': '1',
                            'explication': "Par définition, $P(A|B) = \\frac{P(A \\cap B)}{P(B)}$ lorsque $P(B) > 0$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Dans un arbre pondéré, la probabilité d'un chemin se calcule en :",
                            'options': ["Additionnant les probabilités des branches", "Multipliant les probabilités des branches", "Prenant la plus grande probabilité", "Divisant les probabilités des branches"],
                            'reponse_correcte': '1',
                            'explication': "La probabilité d'un chemin est le produit des probabilités le long des branches successives.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Deux événements $A$ et $B$ sont indépendants si et seulement si :",
                            'options': ["$P(A \\\\cap B) = 0$", "$P(A \\\\cup B) = P(A) + P(B)$", "$P(A \\\\cap B) = P(A) \\\\cdot P(B)$", "$P(A|B) = P(B)$"],
                            'reponse_correcte': '2',
                            'explication': "L'indépendance signifie que $P(A \\cap B) = P(A) \\cdot P(B)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Si $A$ et $B$ sont indépendants, que vaut $P(A|B)$ ?",
                            'options': ["$P(B)$", "$P(A)$", "$P(A) + P(B)$", "$0$"],
                            'reponse_correcte': '1',
                            'explication': "Si $A$ et $B$ sont indépendants, $P(A|B) = \\frac{P(A) \\cdot P(B)}{P(B)} = P(A)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La formule des probabilités totales avec la partition $\\\\{B, \\\\overline{B}\\\\}$ donne :",
                            'options': ["$P(A) = P(A|B) + P(A|\\\\overline{B})$", "$P(A) = P(A|B) \\\\cdot P(B) + P(A|\\\\overline{B}) \\\\cdot P(\\\\overline{B})$", "$P(A) = P(A \\\\cap B) + P(A \\\\cap \\\\overline{B}) - P(B)$", "$P(A) = P(B|A) + P(\\\\overline{B}|A)$"],
                            'reponse_correcte': '1',
                            'explication': "La formule des probabilités totales : $P(A) = P(A|B)P(B) + P(A|\\overline{B})P(\\overline{B})$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "On lance un dé. $A$ = « obtenir 6 », $B$ = « obtenir un pair ». Que vaut $P(A|B)$ ?",
                            'options': ["$\\\\frac{1}{6}$", "$\\\\frac{1}{2}$", "$\\\\frac{1}{3}$", "$\\\\frac{2}{3}$"],
                            'reponse_correcte': '2',
                            'explication': "$P(A|B) = \\frac{P(\\{6\\})}{P(\\{2,4,6\\})} = \\frac{1/6}{3/6} = \\frac{1}{3}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Si $P(A) = 0{,}4$, $P(B) = 0{,}5$ et $P(A \\\\cap B) = 0{,}2$, $A$ et $B$ sont-ils indépendants ?",
                            'options': ["Oui", "Non", "On ne peut pas savoir", "Seulement si $P(A \\\\cup B) = 1$"],
                            'reponse_correcte': '0',
                            'explication': "$P(A) \\cdot P(B) = 0{,}4 \\times 0{,}5 = 0{,}2 = P(A \\cap B)$, donc $A$ et $B$ sont indépendants.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "La somme des probabilités issues d'un même nœud dans un arbre pondéré vaut :",
                            'options': ["$0$", "$0{,}5$", "$1$", "Cela dépend du contexte"],
                            'reponse_correcte': '2',
                            'explication': "Les branches issues d'un même nœud forment un système complet, donc la somme vaut 1.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Si $P(A \\\\cap B) = P(A|B) \\\\cdot P(B)$, on peut aussi écrire $P(A \\\\cap B) = $ :",
                            'options': ["$P(B|A) \\\\cdot P(B)$", "$P(A|B) \\\\cdot P(A)$", "$P(B|A) \\\\cdot P(A)$", "$P(A) + P(B) - 1$"],
                            'reponse_correcte': '2',
                            'explication': "Par symétrie de la formule multiplicative : $P(A \\cap B) = P(B|A) \\cdot P(A)$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Un test a $P(T^+|M) = 0{,}95$, $P(T^+|\\\\overline{M}) = 0{,}03$, $P(M) = 0{,}02$. Que vaut $P(T^+)$ ?",
                            'options': ["$0{,}019$", "$0{,}98$", "$0{,}0484$", "$0{,}95$"],
                            'reponse_correcte': '2',
                            'explication': "$P(T^+) = 0{,}95 \\times 0{,}02 + 0{,}03 \\times 0{,}98 = 0{,}019 + 0{,}0294 = 0{,}0484$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Si $P(A) = 0{,}6$ et $P(B|A) = 0{,}3$, que vaut $P(A \\\\cap B)$ ?",
                            'options': ["$0{,}9$", "$0{,}18$", "$0{,}5$", "$0{,}2$"],
                            'reponse_correcte': '1',
                            'explication': "$P(A \\cap B) = P(B|A) \\cdot P(A) = 0{,}3 \\times 0{,}6 = 0{,}18$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Deux événements incompatibles de probabilités non nulles sont-ils indépendants ?",
                            'options': ["Toujours", "Jamais", "Parfois", "Seulement si $P(A) = P(B)$"],
                            'reponse_correcte': '1',
                            'explication': "Si $A \\cap B = \\emptyset$, alors $P(A \\cap B) = 0 \\neq P(A) \\cdot P(B)$ (car $P(A) > 0$ et $P(B) > 0$).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Un sac contient 3 rouges et 2 vertes. On tire deux boules sans remise. Que vaut $P(R_2|R_1)$ ?",
                            'options': ["$\\\\frac{3}{5}$", "$\\\\frac{2}{5}$", "$\\\\frac{1}{2}$", "$\\\\frac{2}{4}$"],
                            'reponse_correcte': '2',
                            'explication': "Après avoir tiré une rouge, il reste 2 rouges sur 4 boules : $P(R_2|R_1) = \\frac{2}{4} = \\frac{1}{2}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Si $A$ et $B$ sont indépendants, alors $A$ et $\\\\overline{B}$ sont :",
                            'options': ["Incompatibles", "Indépendants", "De même probabilité", "Complémentaires"],
                            'reponse_correcte': '1',
                            'explication': "Si $A$ et $B$ sont indépendants, alors $A$ et $\\overline{B}$ le sont aussi (propriété classique).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "$P(A|B)$ est définie uniquement si $P(B) > 0$.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "La formule $P(A|B) = \\frac{P(A \\cap B)}{P(B)}$ n'a de sens que si $P(B) \\neq 0$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Si $P(A|B) = P(A)$, alors $A$ et $B$ sont indépendants.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "$P(A|B) = P(A) \\Leftrightarrow P(A \\cap B) = P(A) \\cdot P(B)$, ce qui est la définition de l'indépendance.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Deux événements incompatibles sont toujours indépendants.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "C'est le contraire : si $A \\cap B = \\emptyset$ avec $P(A) > 0$ et $P(B) > 0$, ils ne sont jamais indépendants.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Si $P(A) = 0{,}3$ et $P(B) = 0{,}5$, et $A$ et $B$ sont indépendants, que vaut $P(A \\\\cap B)$ ? (répondre sous forme décimale)",
                            'options': None,
                            'reponse_correcte': '0.15',
                            'tolerances': ['0,15'],
                            'explication': "$P(A \\cap B) = P(A) \\cdot P(B) = 0{,}3 \\times 0{,}5 = 0{,}15$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Si $P(A \\\\cap B) = 0{,}12$ et $P(B) = 0{,}4$, que vaut $P(A|B)$ ? (répondre sous forme décimale)",
                            'options': None,
                            'reponse_correcte': '0.3',
                            'tolerances': ['0,3', '0,30', '0.30'],
                            'explication': "$P(A|B) = \\frac{0{,}12}{0{,}4} = 0{,}3$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "On tire une carte dans un jeu de 32. $A$ = « obtenir un as » ($P = \\\\frac{4}{32}$), $B$ = « obtenir un cœur » ($P = \\\\frac{8}{32}$). Que vaut $P(A \\\\cap B)$ sachant que $A$ et $B$ sont indépendants ? (répondre sous forme de fraction simplifiée)",
                            'options': None,
                            'reponse_correcte': '1/32',
                            'tolerances': ['1/32'],
                            'explication': "$P(A \\cap B) = \\frac{4}{32} \\times \\frac{8}{32} = \\frac{32}{1024} = \\frac{1}{32}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Variables aléatoires discrètes',
                'duree': 35,
                'contenu': """# Variables aléatoires discrètes

## Introduction

Jusqu'ici, nous avons travaillé avec des événements (« obtenir un 6 », « le test est positif »). Une **variable aléatoire** permet de passer du qualitatif au quantitatif : on associe un nombre réel à chaque issue d'une expérience aléatoire. Cela ouvre la porte au calcul d'espérance, de variance et à la modélisation statistique.

---

## Définition

### Variable aléatoire

Soit $\\Omega$ l'univers d'une expérience aléatoire. Une **variable aléatoire discrète** $X$ est une fonction :

$$X : \\Omega \\to \\mathbb{R}$$

qui associe un nombre réel à chaque issue.

### Loi de probabilité

La **loi de probabilité** de $X$ est la donnée de chaque valeur $x_i$ prise par $X$ et de la probabilité correspondante $P(X = x_i) = p_i$.

On la présente souvent sous forme de tableau :

| $x_i$ | $x_1$ | $x_2$ | $\\cdots$ | $x_n$ |
|--------|--------|--------|----------|--------|
| $P(X=x_i)$ | $p_1$ | $p_2$ | $\\cdots$ | $p_n$ |

Avec la condition : $\\displaystyle\\sum_{i=1}^n p_i = 1$.

### Exemple

On lance deux dés et on note $X$ la somme des résultats. $X$ prend les valeurs $2, 3, 4, \\ldots, 12$.

Par exemple : $P(X=7) = \\dfrac{6}{36} = \\dfrac{1}{6}$ (les couples $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$).

---

## Espérance

### Définition

L'**espérance** de $X$ est la moyenne pondérée de ses valeurs par leurs probabilités :

$$E(X) = \\sum_{i=1}^n x_i \\cdot p_i = x_1 p_1 + x_2 p_2 + \\cdots + x_n p_n$$

> L'espérance représente la **valeur moyenne** que prendrait $X$ si on répétait l'expérience un très grand nombre de fois.

### Exemple

Un jeu consiste à lancer un dé équilibré. Si on obtient 6, on gagne 10 €. Sinon, on perd 2 €. Soit $X$ le gain.

| $x_i$ | $10$ | $-2$ |
|--------|------|------|
| $P(X=x_i)$ | $\\frac{1}{6}$ | $\\frac{5}{6}$ |

$$E(X) = 10 \\times \\frac{1}{6} + (-2) \\times \\frac{5}{6} = \\frac{10}{6} - \\frac{10}{6} = 0$$

Le jeu est **équitable** : en moyenne, on ne gagne ni ne perd.

### Propriété de linéarité

Pour tous réels $a$ et $b$ :

$$E(aX + b) = aE(X) + b$$

---

## Variance et écart-type

### Variance

La **variance** mesure la dispersion des valeurs de $X$ autour de son espérance :

$$V(X) = E\\left[(X - E(X))^2\\right] = \\sum_{i=1}^n (x_i - E(X))^2 \\cdot p_i$$

### Formule de König-Huygens

En pratique, on utilise souvent la formule équivalente :

$$V(X) = E(X^2) - [E(X)]^2$$

où $E(X^2) = \\displaystyle\\sum_{i=1}^n x_i^2 \\cdot p_i$.

### Écart-type

L'**écart-type** est la racine carrée de la variance :

$$\\sigma(X) = \\sqrt{V(X)}$$

Il s'exprime dans la **même unité** que $X$.

### Exemple

Reprenons le jeu précédent ($E(X) = 0$).

$$E(X^2) = 10^2 \\times \\frac{1}{6} + (-2)^2 \\times \\frac{5}{6} = \\frac{100}{6} + \\frac{20}{6} = 20$$

$$V(X) = 20 - 0^2 = 20$$

$$\\sigma(X) = \\sqrt{20} = 2\\sqrt{5} \\approx 4{,}47 \\text{ €}$$

### Propriété

$$V(aX + b) = a^2 V(X) \\qquad \\text{et} \\qquad \\sigma(aX+b) = |a| \\sigma(X)$$

---

## Applications

### Espérance d'un gain

Dans un jeu de hasard, l'espérance du gain permet de déterminer si le jeu est :
- **Favorable** au joueur si $E(X) > 0$.
- **Équitable** si $E(X) = 0$.
- **Défavorable** au joueur si $E(X) < 0$.

### Exemple complet

Une urne contient 4 boules blanches et 6 boules noires. On tire une boule. Si elle est blanche, on gagne 5 €. Si elle est noire, on perd 3 €. On paie 1 € pour jouer.

Soit $X$ le gain net.

| Issue | Blanche | Noire |
|-------|---------|-------|
| Gain brut | $5$ | $-3$ |
| Gain net $X$ | $4$ | $-4$ |
| Probabilité | $\\frac{4}{10} = 0{,}4$ | $\\frac{6}{10} = 0{,}6$ |

$$E(X) = 4 \\times 0{,}4 + (-4) \\times 0{,}6 = 1{,}6 - 2{,}4 = -0{,}8$$

Le jeu est **défavorable** : en moyenne, on perd 0,80 € par partie.

---

## À retenir

- $E(X) = \\sum x_i p_i$ : « valeur moyenne » de $X$.
- $V(X) = E(X^2) - [E(X)]^2$ (formule de König-Huygens).
- $\\sigma(X) = \\sqrt{V(X)}$ : dispersion dans la même unité que $X$.
- Linéarité : $E(aX+b) = aE(X)+b$ ; $V(aX+b) = a^2 V(X)$.
""",
                'quiz': {
                    'titre': 'Quiz — Variables aléatoires discrètes',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Une variable aléatoire discrète est une fonction de :",
                            'options': ["$\\\\mathbb{R}$ dans $\\\\Omega$", "$\\\\Omega$ dans $\\\\mathbb{R}$", "$\\\\mathbb{N}$ dans $\\\\mathbb{N}$", "$\\\\mathbb{R}$ dans $\\\\mathbb{R}$"],
                            'reponse_correcte': '1',
                            'explication': "Une variable aléatoire discrète $X$ est une fonction de l'univers $\\Omega$ dans $\\mathbb{R}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Pour une loi de probabilité, la somme des probabilités $\\\\sum p_i$ vaut :",
                            'options': ["$0$", "$0{,}5$", "$1$", "Cela dépend de la variable"],
                            'reponse_correcte': '2',
                            'explication': "Par définition d'une loi de probabilité, $\\sum_{i} p_i = 1$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "L'espérance $E(X)$ se calcule par :",
                            'options': ["$\\\\sum x_i^2 p_i$", "$\\\\sum x_i p_i$", "$\\\\sum p_i / x_i$", "$\\\\max(x_i) - \\\\min(x_i)$"],
                            'reponse_correcte': '1',
                            'explication': "$E(X) = \\sum x_i p_i$ est la moyenne pondérée des valeurs par leurs probabilités.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Un jeu est dit équitable lorsque :",
                            'options': ["$E(X) > 0$", "$E(X) < 0$", "$E(X) = 0$", "$V(X) = 0$"],
                            'reponse_correcte': '2',
                            'explication': "Un jeu est équitable quand l'espérance du gain est nulle : ni gain ni perte en moyenne.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La formule de König-Huygens donne :",
                            'options': ["$V(X) = E(X)^2 - E(X^2)$", "$V(X) = E(X^2) - [E(X)]^2$", "$V(X) = [E(X)]^2$", "$V(X) = \\\\sqrt{E(X^2)}$"],
                            'reponse_correcte': '1',
                            'explication': "La formule de König-Huygens est $V(X) = E(X^2) - [E(X)]^2$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "L'écart-type $\\\\sigma(X)$ est :",
                            'options': ["$V(X)^2$", "$\\\\sqrt{V(X)}$", "$V(X) / 2$", "$E(X) - V(X)$"],
                            'reponse_correcte': '1',
                            'explication': "$\\sigma(X) = \\sqrt{V(X)}$, il mesure la dispersion dans la même unité que $X$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Si $E(X) = 5$, que vaut $E(3X + 2)$ ?",
                            'options': ["$15$", "$17$", "$13$", "$10$"],
                            'reponse_correcte': '1',
                            'explication': "Par linéarité : $E(3X+2) = 3 \\times 5 + 2 = 17$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Si $V(X) = 4$, que vaut $V(2X + 5)$ ?",
                            'options': ["$8$", "$13$", "$16$", "$9$"],
                            'reponse_correcte': '2',
                            'explication': "$V(aX + b) = a^2 V(X)$, donc $V(2X + 5) = 4 \\times 4 = 16$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "On lance un dé, $X$ = résultat. Que vaut $E(X)$ ?",
                            'options': ["$3$", "$3{,}5$", "$4$", "$6$"],
                            'reponse_correcte': '1',
                            'explication': "$E(X) = \\frac{1}{6}(1+2+3+4+5+6) = \\frac{21}{6} = 3{,}5$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Si $X$ vaut 10 avec probabilité $\\\\frac{1}{4}$ et $-2$ avec probabilité $\\\\frac{3}{4}$, que vaut $E(X)$ ?",
                            'options': ["$4$", "$1$", "$2{,}5$", "$8$"],
                            'reponse_correcte': '1',
                            'explication': "$E(X) = 10 \\times \\frac{1}{4} + (-2) \\times \\frac{3}{4} = 2{,}5 - 1{,}5 = 1$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Si $X$ prend les valeurs 0, 1, 2 avec probabilités $0{,}3$, $0{,}5$, $0{,}2$, que vaut $E(X)$ ?",
                            'options': ["$0{,}9$", "$0{,}5$", "$1$", "$1{,}2$"],
                            'reponse_correcte': '0',
                            'explication': "$E(X) = 0 \\times 0{,}3 + 1 \\times 0{,}5 + 2 \\times 0{,}2 = 0 + 0{,}5 + 0{,}4 = 0{,}9$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Si $E(X) = 3$ et $E(X^2) = 11$, que vaut $V(X)$ ?",
                            'options': ["$8$", "$2$", "$\\\\sqrt{2}$", "$14$"],
                            'reponse_correcte': '1',
                            'explication': "$V(X) = E(X^2) - [E(X)]^2 = 11 - 9 = 2$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Un jeu coûte 2 € et rapporte 10 € avec probabilité $\\\\frac{1}{6}$. Quel est le gain net espéré ?",
                            'options': ["$-\\\\frac{1}{3}$", "$0$", "$\\\\frac{2}{3}$", "$-\\\\frac{2}{3}$"],
                            'reponse_correcte': '3',
                            'explication': "Gain net = $8 \\times \\frac{1}{6} + (-2) \\times \\frac{5}{6} = \\frac{8-10}{6} = -\\frac{2}{6} = -\\frac{1}{3}$. Correction : gain brut 10 − coût 2 = 8 si succès, et −2 si échec, $E = \\frac{8}{6} - \\frac{10}{6} = -\\frac{2}{6} \\approx -0{,}33$. L'option la plus proche est $-\\frac{1}{3}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Si $\\\\sigma(X) = 3$, que vaut $\\\\sigma(4X)$ ?",
                            'options': ["$3$", "$7$", "$12$", "$9$"],
                            'reponse_correcte': '2',
                            'explication': "$\\sigma(aX+b) = |a|\\sigma(X) = 4 \\times 3 = 12$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "L'espérance d'une variable aléatoire est toujours une valeur que $X$ peut prendre.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "L'espérance est une moyenne pondérée ; elle peut ne correspondre à aucune valeur prise par $X$ (ex : $E = 3{,}5$ pour un dé).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La variance d'une variable aléatoire est toujours positive ou nulle.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "$V(X) = E[(X - E(X))^2]$ est une somme de carrés pondérés, donc $V(X) \\geq 0$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Si $V(X) = 0$, alors $X$ est une variable certaine (constante).",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "$V(X) = 0$ signifie que $X$ ne s'écarte jamais de son espérance, donc $X$ est constante.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer $E(X)$ si $X$ prend les valeurs 1, 2, 3 chacune avec probabilité $\\\\frac{1}{3}$.",
                            'options': None,
                            'reponse_correcte': '2',
                            'tolerances': [],
                            'explication': "$E(X) = 1 \\times \\frac{1}{3} + 2 \\times \\frac{1}{3} + 3 \\times \\frac{1}{3} = \\frac{6}{3} = 2$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Si $E(X) = 4$ et $E(X^2) = 20$, calculer $V(X)$.",
                            'options': None,
                            'reponse_correcte': '4',
                            'tolerances': [],
                            'explication': "$V(X) = E(X^2) - [E(X)]^2 = 20 - 16 = 4$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Si $E(X) = 7$ et $V(X) = 9$, que vaut $\\\\sigma(X)$ ?",
                            'options': None,
                            'reponse_correcte': '3',
                            'tolerances': [],
                            'explication': "$\\sigma(X) = \\sqrt{V(X)} = \\sqrt{9} = 3$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 3,
                'titre': 'Loi binomiale',
                'duree': 35,
                'contenu': """# Loi binomiale

## Introduction

La loi binomiale est la loi de probabilité la plus courante en classe de Première. Elle modélise le nombre de succès dans une **répétition d'épreuves indépendantes** à deux issues. On la retrouve dans de nombreuses situations : contrôle qualité, sondages, tests médicaux, jeux de hasard.

---

## Épreuve de Bernoulli

### Définition

Une **épreuve de Bernoulli** de paramètre $p$ est une expérience aléatoire à exactement **deux issues** :
- **Succès** (S) de probabilité $p$.
- **Échec** (E) de probabilité $q = 1 - p$.

### Variable de Bernoulli

On associe à cette épreuve la variable aléatoire $X$ :

$$X = \\begin{cases} 1 & \\text{si succès} \\\\ 0 & \\text{si échec} \\end{cases}$$

Sa loi : $P(X=1) = p$ et $P(X=0) = 1-p$.

$$E(X) = p \\qquad V(X) = p(1-p)$$

---

## Schéma de Bernoulli

Un **schéma de Bernoulli** consiste en la **répétition de $n$ épreuves de Bernoulli identiques et indépendantes**.

On note $X$ le **nombre de succès** obtenus au cours des $n$ épreuves.

$X$ peut prendre les valeurs $0, 1, 2, \\ldots, n$.

---

## Coefficients binomiaux

### Définition

Le nombre de façons de choisir $k$ éléments parmi $n$ est le **coefficient binomial** :

$$\\binom{n}{k} = \\frac{n!}{k!(n-k)!}$$

où $n! = n \\times (n-1) \\times \\cdots \\times 2 \\times 1$ (factorielle de $n$), avec $0! = 1$.

### Exemples

$$\\binom{5}{2} = \\frac{5!}{2! \\cdot 3!} = \\frac{120}{2 \\times 6} = 10$$

$$\\binom{6}{0} = 1 \\qquad \\binom{6}{6} = 1 \\qquad \\binom{6}{1} = 6$$

### Propriétés

- $\\binom{n}{0} = \\binom{n}{n} = 1$
- $\\binom{n}{k} = \\binom{n}{n-k}$ (symétrie)
- **Triangle de Pascal** : $\\binom{n+1}{k+1} = \\binom{n}{k} + \\binom{n}{k+1}$

---

## Loi binomiale $\\mathcal{B}(n, p)$

### Théorème

Si $X$ suit la loi binomiale de paramètres $n$ et $p$, notée $X \\sim \\mathcal{B}(n, p)$, alors :

$$P(X = k) = \\binom{n}{k} p^k (1-p)^{n-k} \\qquad \\text{pour } k = 0, 1, \\ldots, n$$

### Interprétation

$\\binom{n}{k}$ compte le nombre de chemins ayant exactement $k$ succès parmi $n$ épreuves.

$p^k$ est la probabilité des $k$ succès.

$(1-p)^{n-k}$ est la probabilité des $n-k$ échecs.

### Exemple

On lance 5 fois une pièce équilibrée ($p = 0{,}5$). Soit $X$ le nombre de « pile ».

$X \\sim \\mathcal{B}(5 \\;; 0{,}5)$.

$$P(X = 3) = \\binom{5}{3} \\cdot (0{,}5)^3 \\cdot (0{,}5)^2 = 10 \\times 0{,}125 \\times 0{,}25 = 0{,}3125$$

$$P(X = 0) = \\binom{5}{0} \\cdot (0{,}5)^0 \\cdot (0{,}5)^5 = 1 \\times 1 \\times 0{,}03125 = 0{,}03125$$

---

## Espérance, variance, écart-type

Si $X \\sim \\mathcal{B}(n, p)$ :

$$E(X) = np$$

$$V(X) = np(1-p)$$

$$\\sigma(X) = \\sqrt{np(1-p)}$$

### Exemple

Un QCM de 20 questions a 4 réponses possibles par question. Un élève répond au hasard. Soit $X$ le nombre de bonnes réponses.

$X \\sim \\mathcal{B}\\left(20 \\;; \\frac{1}{4}\\right)$.

$$E(X) = 20 \\times \\frac{1}{4} = 5$$

$$V(X) = 20 \\times \\frac{1}{4} \\times \\frac{3}{4} = \\frac{15}{4} = 3{,}75$$

$$\\sigma(X) = \\sqrt{3{,}75} \\approx 1{,}94$$

En moyenne, l'élève obtient 5 bonnes réponses.

---

## Calculer $P(X \\leq k)$ et $P(X \\geq k)$

### Probabilité cumulée

$$P(X \\leq k) = \\sum_{i=0}^{k} \\binom{n}{i} p^i (1-p)^{n-i}$$

### Complément

$$P(X \\geq k) = 1 - P(X \\leq k-1)$$

### Exemple

Avec $X \\sim \\mathcal{B}(5 \\;; 0{,}5)$, calculons $P(X \\geq 3)$ :

$$P(X \\geq 3) = 1 - P(X \\leq 2) = 1 - [P(X=0) + P(X=1) + P(X=2)]$$

$$= 1 - \\left[\\frac{1}{32} + \\frac{5}{32} + \\frac{10}{32}\\right] = 1 - \\frac{16}{32} = \\frac{1}{2}$$

---

## Application : contrôle qualité

Une usine produit des pièces dont 5 % sont défectueuses. On prélève un échantillon de 10 pièces. Soit $X$ le nombre de pièces défectueuses.

$X \\sim \\mathcal{B}(10 \\;; 0{,}05)$.

$$P(X = 0) = \\binom{10}{0} (0{,}05)^0 (0{,}95)^{10} = (0{,}95)^{10} \\approx 0{,}599$$

$$P(X \\geq 1) = 1 - P(X=0) \\approx 1 - 0{,}599 = 0{,}401$$

Il y a environ 40 % de chances de trouver au moins une pièce défectueuse dans l'échantillon.

---

## À retenir

- **Épreuve de Bernoulli** : deux issues, succès ($p$) et échec ($1-p$).
- **Loi binomiale** $\\mathcal{B}(n,p)$ : $P(X=k) = \\binom{n}{k}p^k(1-p)^{n-k}$.
- $E(X) = np$, $V(X) = np(1-p)$, $\\sigma(X) = \\sqrt{np(1-p)}$.
- $\\binom{n}{k} = \\dfrac{n!}{k!(n-k)!}$.
""",
                'quiz': {
                    'titre': 'Quiz — Loi binomiale',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Une épreuve de Bernoulli possède exactement :",
                            'options': ["Une seule issue", "Deux issues", "Trois issues", "Un nombre variable d'issues"],
                            'reponse_correcte': '1',
                            'explication': "Une épreuve de Bernoulli a exactement deux issues : succès (probabilité $p$) et échec (probabilité $1-p$).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Si $X$ suit une loi de Bernoulli de paramètre $p$, quelle est $E(X)$ ?",
                            'options': ["$p^2$", "$1 - p$", "$p$", "$p(1-p)$"],
                            'reponse_correcte': '2',
                            'explication': "Pour une variable de Bernoulli, $E(X) = 1 \\times p + 0 \\times (1-p) = p$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\binom{5}{2}$ ?",
                            'options': ["$5$", "$10$", "$20$", "$25$"],
                            'reponse_correcte': '1',
                            'explication': "$\\binom{5}{2} = \\frac{5!}{2! \\times 3!} = \\frac{120}{2 \\times 6} = 10$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Si $X \\\\sim \\\\mathcal{B}(10, 0{,}3)$, quelle est $E(X)$ ?",
                            'options': ["$0{,}3$", "$3$", "$7$", "$10$"],
                            'reponse_correcte': '1',
                            'explication': "Pour une loi binomiale, $E(X) = np = 10 \\times 0{,}3 = 3$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\binom{n}{0}$ pour tout entier $n$ ?",
                            'options': ["$0$", "$1$", "$n$", "$n!$"],
                            'reponse_correcte': '1',
                            'explication': "$\\binom{n}{0} = \\frac{n!}{0! \\times n!} = 1$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quelle formule donne $P(X = k)$ pour $X \\\\sim \\\\mathcal{B}(n, p)$ ?",
                            'options': ["$\\\\binom{n}{k} p^k (1-p)^{n-k}$", "$\\\\frac{n!}{k!} p^k$", "$n p^k (1-p)^{n-k}$", "$\\\\binom{n}{k} p^n$"],
                            'reponse_correcte': '0',
                            'explication': "La loi binomiale donne $P(X=k) = \\binom{n}{k} p^k (1-p)^{n-k}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Un schéma de Bernoulli nécessite que les épreuves soient :",
                            'options': ["Identiques mais pas forcément indépendantes", "Indépendantes mais pas forcément identiques", "Identiques et indépendantes", "Ni identiques ni indépendantes"],
                            'reponse_correcte': '2',
                            'explication': "Un schéma de Bernoulli est la répétition de $n$ épreuves de Bernoulli identiques et indépendantes.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\binom{6}{3}$ ?",
                            'options': ["$6$", "$18$", "$20$", "$36$"],
                            'reponse_correcte': '2',
                            'explication': "$\\binom{6}{3} = \\frac{6!}{3! \\times 3!} = \\frac{720}{6 \\times 6} = 20$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Si $X \\\\sim \\\\mathcal{B}(20, 0{,}25)$, que vaut $V(X)$ ?",
                            'options': ["$5$", "$3{,}75$", "$15$", "$1{,}25$"],
                            'reponse_correcte': '1',
                            'explication': "$V(X) = np(1-p) = 20 \\times 0{,}25 \\times 0{,}75 = 3{,}75$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "On lance 5 fois une pièce équilibrée. Quelle est $P(X = 3)$ où $X$ est le nombre de pile ?",
                            'options': ["$\\\\frac{5}{16}$", "$\\\\frac{10}{32}$", "$\\\\frac{1}{5}$", "$\\\\frac{3}{8}$"],
                            'reponse_correcte': '1',
                            'explication': "$P(X=3) = \\binom{5}{3}(0{,}5)^3(0{,}5)^2 = 10 \\times \\frac{1}{32} = \\frac{10}{32} = \\frac{5}{16}$. Les options 0 et 1 sont la même valeur, mais $\\frac{10}{32}$ est la forme directe du calcul.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "La relation $\\\\binom{n}{k} = \\\\binom{n}{n-k}$ s'appelle la propriété de :",
                            'options': ["Linéarité", "Triangle de Pascal", "Symétrie des coefficients binomiaux", "Formule de Vandermonde"],
                            'reponse_correcte': '2',
                            'explication': "C'est la propriété de symétrie : choisir $k$ éléments parmi $n$ revient à en exclure $n-k$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Si $X \\\\sim \\\\mathcal{B}(8, 0{,}4)$, quelle est $P(X = 0)$ ?",
                            'options': ["$0{,}4^8$", "$(0{,}6)^8$", "$0$", "$1 - 0{,}4^8$"],
                            'reponse_correcte': '1',
                            'explication': "$P(X=0) = \\binom{8}{0}(0{,}4)^0(0{,}6)^8 = (0{,}6)^8 \\approx 0{,}0168$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "$P(X \\\\geq 1)$ s'exprime en fonction de $P(X = 0)$ par :",
                            'options': ["$P(X = 0)$", "$1 + P(X = 0)$", "$1 - P(X = 0)$", "$P(X = 0)^2$"],
                            'reponse_correcte': '2',
                            'explication': "$P(X \\geq 1) = 1 - P(X = 0)$ par passage au complémentaire.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Dans le triangle de Pascal, la relation $\\\\binom{n+1}{k+1} = \\\\binom{n}{k} + \\\\binom{n}{k+1}$ permet de calculer :",
                            'options': ["Les coefficients ligne par ligne", "Uniquement les termes centraux", "Seulement $\\\\binom{n}{0}$", "Les factorielles directement"],
                            'reponse_correcte': '0',
                            'explication': "Le triangle de Pascal construit chaque coefficient comme somme des deux coefficients de la ligne précédente.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'qcm',
                            'texte': "Si $X \\\\sim \\\\mathcal{B}(12, 0{,}5)$, que vaut $\\\\sigma(X)$ ?",
                            'options': ["$6$", "$3$", "$\\\\sqrt{3}$", "$\\\\sqrt{6}$"],
                            'reponse_correcte': '2',
                            'explication': "$V(X) = 12 \\times 0{,}5 \\times 0{,}5 = 3$, donc $\\sigma(X) = \\sqrt{3}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'qcm',
                            'texte': "5 % des pièces d'une usine sont défectueuses. On en prélève 10. La probabilité qu'aucune ne soit défectueuse est :",
                            'options': ["$(0{,}05)^{10}$", "$(0{,}95)^{10}$", "$1 - (0{,}05)^{10}$", "$\\\\binom{10}{5} (0{,}05)^5$"],
                            'reponse_correcte': '1',
                            'explication': "$P(X=0) = \\binom{10}{0}(0{,}05)^0(0{,}95)^{10} = (0{,}95)^{10} \\approx 0{,}599$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Si $X \\\\sim \\\\mathcal{B}(n, p)$, alors $P(X = n) = p^n$.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "$P(X=n) = \\binom{n}{n}p^n(1-p)^0 = 1 \\times p^n \\times 1 = p^n$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'vrai_faux',
                            'texte': "Le coefficient $\\\\binom{7}{3}$ est égal à $\\\\binom{7}{4}$.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "Par la propriété de symétrie : $\\binom{7}{3} = \\binom{7}{7-3} = \\binom{7}{4} = 35$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Calculer $\\\\binom{4}{2}$.",
                            'options': None,
                            'reponse_correcte': '6',
                            'tolerances': [],
                            'explication': "$\\binom{4}{2} = \\frac{4!}{2! \\times 2!} = \\frac{24}{4} = 6$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Si $X \\\\sim \\\\mathcal{B}(50, 0{,}2)$, calculer $E(X)$.",
                            'options': None,
                            'reponse_correcte': '10',
                            'tolerances': [],
                            'explication': "$E(X) = np = 50 \\times 0{,}2 = 10$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 7 — Produit scalaire
    # ──────────────────────────────────────────────
    {
        'ordre': 7,
        'titre': 'Produit scalaire',
        'description': "Produit scalaire dans le plan : définitions géométrique et analytique, propriétés, orthogonalité et applications.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Définitions et propriétés du produit scalaire',
                'duree': 35,
                'contenu': """# Définitions et propriétés du produit scalaire

## Introduction

Le **produit scalaire** est un outil fondamental de la géométrie. Il associe à deux vecteurs un **nombre réel** qui encode leur relation angulaire et leurs longueurs. Il permet de calculer des distances, des angles, de prouver l'orthogonalité, et constitue le pont entre géométrie synthétique et géométrie analytique.

---

## Norme d'un vecteur

### Définition

La **norme** (ou longueur) d'un vecteur $\\vec{u}$ est notée $\\|\\vec{u}\\|$ ou $|\\vec{u}|$.

Si $\\vec{u}$ a pour coordonnées $(x ; y)$ dans un repère orthonormé :

$$\\|\\vec{u}\\| = \\sqrt{x^2 + y^2}$$

### Distance entre deux points

Si $A(x_A ; y_A)$ et $B(x_B ; y_B)$ :

$$AB = \\|\\overrightarrow{AB}\\| = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$$

---

## Définitions du produit scalaire

Il existe **plusieurs définitions équivalentes** du produit scalaire.

### Définition 1 : avec l'angle

Pour deux vecteurs $\\vec{u}$ et $\\vec{v}$ non nuls, avec $\\theta = (\\widehat{\\vec{u}, \\vec{v}})$ l'angle entre eux :

$$\\vec{u} \\cdot \\vec{v} = \\|\\vec{u}\\| \\times \\|\\vec{v}\\| \\times \\cos\\theta$$

Si l'un des vecteurs est nul : $\\vec{u} \\cdot \\vec{v} = 0$.

### Définition 2 : avec les coordonnées (analytique)

Si $\\vec{u}(x ; y)$ et $\\vec{v}(x' ; y')$ dans un repère **orthonormé** :

$$\\vec{u} \\cdot \\vec{v} = xx' + yy'$$

### Définition 3 : avec les normes (polarisation)

$$\\vec{u} \\cdot \\vec{v} = \\frac{1}{2}\\left(\\|\\vec{u} + \\vec{v}\\|^2 - \\|\\vec{u}\\|^2 - \\|\\vec{v}\\|^2\\right)$$

ou de manière équivalente :

$$\\vec{u} \\cdot \\vec{v} = \\frac{1}{2}\\left(\\|\\vec{u}\\|^2 + \\|\\vec{v}\\|^2 - \\|\\vec{u} - \\vec{v}\\|^2\\right)$$

### Définition 4 : avec le projeté orthogonal

Si $H$ est le projeté orthogonal de $\\vec{v}$ sur la droite dirigée par $\\vec{u}$ :

$$\\vec{u} \\cdot \\vec{v} = \\|\\vec{u}\\| \\times \\overline{OH}$$

où $\\overline{OH}$ est la mesure algébrique du projeté.

---

## Exemples de calcul

### Avec les coordonnées

$\\vec{u}(3 ; -1)$ et $\\vec{v}(2 ; 5)$ :

$$\\vec{u} \\cdot \\vec{v} = 3 \\times 2 + (-1) \\times 5 = 6 - 5 = 1$$

### Avec l'angle

$\\|\\vec{u}\\| = 4$, $\\|\\vec{v}\\| = 3$ et $\\theta = 60°$ :

$$\\vec{u} \\cdot \\vec{v} = 4 \\times 3 \\times \\cos 60° = 12 \\times \\frac{1}{2} = 6$$

### Cas particuliers

- Si $\\theta = 0°$ (même direction, même sens) : $\\vec{u} \\cdot \\vec{v} = \\|\\vec{u}\\| \\cdot \\|\\vec{v}\\|$.
- Si $\\theta = 90°$ (vecteurs perpendiculaires) : $\\vec{u} \\cdot \\vec{v} = 0$.
- Si $\\theta = 180°$ (même direction, sens opposés) : $\\vec{u} \\cdot \\vec{v} = -\\|\\vec{u}\\| \\cdot \\|\\vec{v}\\|$.
- $\\vec{u} \\cdot \\vec{u} = \\|\\vec{u}\\|^2$ (le produit scalaire d'un vecteur par lui-même donne le carré de sa norme).

---

## Propriétés

Le produit scalaire vérifie les propriétés suivantes, pour tous vecteurs $\\vec{u}$, $\\vec{v}$, $\\vec{w}$ et tout réel $\\lambda$ :

| Propriété | Formule |
|-----------|---------|
| **Symétrie** | $\\vec{u} \\cdot \\vec{v} = \\vec{v} \\cdot \\vec{u}$ |
| **Bilinéarité** | $\\vec{u} \\cdot (\\vec{v} + \\vec{w}) = \\vec{u} \\cdot \\vec{v} + \\vec{u} \\cdot \\vec{w}$ |
| **Homogénéité** | $(\\lambda\\vec{u}) \\cdot \\vec{v} = \\lambda(\\vec{u} \\cdot \\vec{v})$ |
| **Positivité** | $\\vec{u} \\cdot \\vec{u} \\geq 0$, et $\\vec{u} \\cdot \\vec{u} = 0 \\iff \\vec{u} = \\vec{0}$ |

### Identités remarquables

$$\\|\\vec{u} + \\vec{v}\\|^2 = \\|\\vec{u}\\|^2 + 2\\vec{u}\\cdot\\vec{v} + \\|\\vec{v}\\|^2$$

$$\\|\\vec{u} - \\vec{v}\\|^2 = \\|\\vec{u}\\|^2 - 2\\vec{u}\\cdot\\vec{v} + \\|\\vec{v}\\|^2$$

$$(\\vec{u}+\\vec{v})\\cdot(\\vec{u}-\\vec{v}) = \\|\\vec{u}\\|^2 - \\|\\vec{v}\\|^2$$

---

## Orthogonalité

### Critère

Deux vecteurs $\\vec{u}$ et $\\vec{v}$ sont **orthogonaux** si et seulement si :

$$\\vec{u} \\cdot \\vec{v} = 0$$

### Exemple

$\\vec{u}(2 ; 3)$ et $\\vec{v}(3 ; -2)$ :

$$\\vec{u} \\cdot \\vec{v} = 2 \\times 3 + 3 \\times (-2) = 6 - 6 = 0$$

Les vecteurs sont **orthogonaux**. ✓

---

## Calcul d'un angle

À partir de la définition avec l'angle, on déduit :

$$\\cos\\theta = \\frac{\\vec{u} \\cdot \\vec{v}}{\\|\\vec{u}\\| \\times \\|\\vec{v}\\|}$$

**Exemple :** $\\vec{u}(1 ; 2)$ et $\\vec{v}(3 ; 1)$ :

$$\\vec{u} \\cdot \\vec{v} = 3 + 2 = 5, \\quad \\|\\vec{u}\\| = \\sqrt{5}, \\quad \\|\\vec{v}\\| = \\sqrt{10}$$

$$\\cos\\theta = \\frac{5}{\\sqrt{5} \\cdot \\sqrt{10}} = \\frac{5}{\\sqrt{50}} = \\frac{5}{5\\sqrt{2}} = \\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2}$$

Donc $\\theta = \\frac{\\pi}{4}$ (soit 45°).

---

## À retenir

- $\\vec{u} \\cdot \\vec{v} = xx' + yy'$ (en repère orthonormé).
- $\\vec{u} \\cdot \\vec{v} = \\|\\vec{u}\\| \\|\\vec{v}\\| \\cos\\theta$.
- $\\vec{u} \\perp \\vec{v} \\iff \\vec{u} \\cdot \\vec{v} = 0$.
- $\\vec{u} \\cdot \\vec{u} = \\|\\vec{u}\\|^2$.
- Le produit scalaire est **symétrique**, **bilinéaire** et **positif**.
""",
                'quiz': {
                    'titre': 'Quiz — Définitions et propriétés du produit scalaire',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quelle est la norme du vecteur $\\\\vec{u}(x ; y)$ dans un repère orthonormé ?",
                            'options': ["$x + y$", "$\\\\sqrt{x^2 + y^2}$", "$x^2 + y^2$", "$|x| + |y|$"],
                            'reponse_correcte': '1',
                            'explication': "La norme est $\\|\\vec{u}\\| = \\sqrt{x^2 + y^2}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Que vaut le produit scalaire $\\\\vec{u} \\\\cdot \\\\vec{v}$ si $\\\\vec{u}(x ; y)$ et $\\\\vec{v}(x' ; y')$ dans un repère orthonormé ?",
                            'options': ["$xx' - yy'$", "$xy' + x'y$", "$xx' + yy'$", "$xy' - x'y$"],
                            'reponse_correcte': '2',
                            'explication': "Dans un repère orthonormé, $\\vec{u} \\cdot \\vec{v} = xx' + yy'$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Si $\\\\vec{u} \\\\cdot \\\\vec{v} = 0$ et les deux vecteurs sont non nuls, alors ils sont :",
                            'options': ["Colinéaires", "Orthogonaux", "De même norme", "Opposés"],
                            'reponse_correcte': '1',
                            'explication': "Un produit scalaire nul entre deux vecteurs non nuls signifie qu'ils sont orthogonaux.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Que vaut $\\\\vec{u} \\\\cdot \\\\vec{u}$ ?",
                            'options': ["$0$", "$\\\\|\\\\vec{u}\\\\|$", "$\\\\|\\\\vec{u}\\\\|^2$", "$2\\\\|\\\\vec{u}\\\\|$"],
                            'reponse_correcte': '2',
                            'explication': "$\\vec{u} \\cdot \\vec{u} = \\|\\vec{u}\\|^2$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Calculer $\\\\vec{u} \\\\cdot \\\\vec{v}$ avec $\\\\vec{u}(3 ; -1)$ et $\\\\vec{v}(2 ; 5)$.",
                            'options': ["$11$", "$1$", "$-1$", "$7$"],
                            'reponse_correcte': '1',
                            'explication': "$3 \\times 2 + (-1) \\times 5 = 6 - 5 = 1$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Le produit scalaire est symétrique, c'est-à-dire que :",
                            'options': ["$\\\\vec{u} \\\\cdot \\\\vec{v} = -\\\\vec{v} \\\\cdot \\\\vec{u}$", "$\\\\vec{u} \\\\cdot \\\\vec{v} = \\\\vec{v} \\\\cdot \\\\vec{u}$", "$\\\\vec{u} \\\\cdot \\\\vec{v} = \\\\|\\\\vec{u}\\\\| \\\\cdot \\\\|\\\\vec{v}\\\\|$", "$\\\\vec{u} \\\\cdot \\\\vec{v} = 0$ toujours"],
                            'reponse_correcte': '1',
                            'explication': "La symétrie du produit scalaire signifie que $\\vec{u} \\cdot \\vec{v} = \\vec{v} \\cdot \\vec{u}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Si $\\\\|\\\\vec{u}\\\\| = 4$, $\\\\|\\\\vec{v}\\\\| = 3$ et l'angle entre eux est $60°$, combien vaut $\\\\vec{u} \\\\cdot \\\\vec{v}$ ?",
                            'options': ["$12$", "$6\\\\sqrt{3}$", "$6$", "$3$"],
                            'reponse_correcte': '2',
                            'explication': "$\\vec{u} \\cdot \\vec{v} = 4 \\times 3 \\times \\cos 60° = 12 \\times \\frac{1}{2} = 6$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Les vecteurs $\\\\vec{u}(2 ; 3)$ et $\\\\vec{v}(3 ; -2)$ sont-ils orthogonaux ?",
                            'options': ["Oui, car $\\\\vec{u} \\\\cdot \\\\vec{v} = 0$", "Non, car $\\\\vec{u} \\\\cdot \\\\vec{v} = 12$", "Oui, car $\\\\vec{u} \\\\cdot \\\\vec{v} = 1$", "Non, car $\\\\vec{u} \\\\cdot \\\\vec{v} = -1$"],
                            'reponse_correcte': '0',
                            'explication': "$2 \\times 3 + 3 \\times (-2) = 6 - 6 = 0$, donc ils sont orthogonaux.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Quelle formule permet de calculer le cosinus de l'angle $\\\\theta$ entre $\\\\vec{u}$ et $\\\\vec{v}$ ?",
                            'options': ["$\\\\cos\\\\theta = \\\\|\\\\vec{u}\\\\| \\\\times \\\\|\\\\vec{v}\\\\|$", "$\\\\cos\\\\theta = \\\\frac{\\\\vec{u} \\\\cdot \\\\vec{v}}{\\\\|\\\\vec{u}\\\\| + \\\\|\\\\vec{v}\\\\|}$", "$\\\\cos\\\\theta = \\\\frac{\\\\vec{u} \\\\cdot \\\\vec{v}}{\\\\|\\\\vec{u}\\\\| \\\\times \\\\|\\\\vec{v}\\\\|}$", "$\\\\cos\\\\theta = \\\\vec{u} \\\\cdot \\\\vec{v}$"],
                            'reponse_correcte': '2',
                            'explication': "$\\cos\\theta = \\frac{\\vec{u} \\cdot \\vec{v}}{\\|\\vec{u}\\| \\times \\|\\vec{v}\\|}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quelle identité remarquable est correcte ?",
                            'options': ["$\\\\|\\\\vec{u} + \\\\vec{v}\\\\|^2 = \\\\|\\\\vec{u}\\\\|^2 + \\\\|\\\\vec{v}\\\\|^2$", "$\\\\|\\\\vec{u} + \\\\vec{v}\\\\|^2 = \\\\|\\\\vec{u}\\\\|^2 + 2\\\\vec{u} \\\\cdot \\\\vec{v} + \\\\|\\\\vec{v}\\\\|^2$", "$\\\\|\\\\vec{u} + \\\\vec{v}\\\\| = \\\\|\\\\vec{u}\\\\| + \\\\|\\\\vec{v}\\\\|$", "$\\\\|\\\\vec{u} + \\\\vec{v}\\\\|^2 = (\\\\vec{u} \\\\cdot \\\\vec{v})^2$"],
                            'reponse_correcte': '1',
                            'explication': "$\\|\\vec{u} + \\vec{v}\\|^2 = \\|\\vec{u}\\|^2 + 2\\vec{u} \\cdot \\vec{v} + \\|\\vec{v}\\|^2$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Si $\\\\|\\\\vec{u}\\\\| = 2$, $\\\\|\\\\vec{v}\\\\| = 3$ et l'angle est $120°$, combien vaut $\\\\vec{u} \\\\cdot \\\\vec{v}$ ?",
                            'options': ["$3$", "$-6$", "$-3$", "$6$"],
                            'reponse_correcte': '2',
                            'explication': "$\\vec{u} \\cdot \\vec{v} = 2 \\times 3 \\times \\cos 120° = 6 \\times (-\\frac{1}{2}) = -3$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Calculer l'angle entre $\\\\vec{u}(1 ; 1)$ et $\\\\vec{v}(0 ; 2)$.",
                            'options': ["$30°$", "$45°$", "$60°$", "$90°$"],
                            'reponse_correcte': '1',
                            'explication': "$\\vec{u} \\cdot \\vec{v} = 2$, $\\|\\vec{u}\\| = \\sqrt{2}$, $\\|\\vec{v}\\| = 2$. $\\cos\\theta = \\frac{2}{2\\sqrt{2}} = \\frac{\\sqrt{2}}{2}$, donc $\\theta = 45°$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Soient $\\\\vec{u}(1 ; 2)$ et $\\\\vec{v}(3 ; 1)$. Les expressions $\\\\frac{5}{\\\\sqrt{50}}$, $\\\\frac{5}{\\\\sqrt{5}\\\\sqrt{10}}$ et $\\\\frac{\\\\sqrt{2}}{2}$ pour $\\\\cos\\\\theta$ sont :",
                            'options': ["Toutes différentes", "Seules les deux premières sont égales", "Seules la première et la troisième sont égales", "Toutes équivalentes"],
                            'reponse_correcte': '3',
                            'explication': "$\\vec{u} \\cdot \\vec{v} = 5$, $\\|\\vec{u}\\| = \\sqrt{5}$, $\\|\\vec{v}\\| = \\sqrt{10}$. $\\cos\\theta = \\frac{5}{\\sqrt{50}} = \\frac{5}{5\\sqrt{2}} = \\frac{\\sqrt{2}}{2}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Le produit scalaire de deux vecteurs est toujours positif ou nul.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le produit scalaire peut être négatif lorsque l'angle entre les vecteurs est obtus (supérieur à $90°$).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Pour tout vecteur $\\\\vec{u}$, on a $\\\\vec{u} \\\\cdot \\\\vec{u} \\\\geq 0$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$\\vec{u} \\cdot \\vec{u} = \\|\\vec{u}\\|^2 \\geq 0$ car c'est un carré.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Le produit scalaire vérifie $(\\\\lambda\\\\vec{u}) \\\\cdot \\\\vec{v} = \\\\lambda(\\\\vec{u} \\\\cdot \\\\vec{v})$ pour tout réel $\\\\lambda$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est la propriété d'homogénéité (ou compatibilité avec la multiplication par un scalaire) du produit scalaire.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Calculer $\\\\vec{u} \\\\cdot \\\\vec{v}$ avec $\\\\vec{u}(4 ; -2)$ et $\\\\vec{v}(1 ; 3)$.",
                            'options': None,
                            'reponse_correcte': '-2',
                            'tolerances': ['-2,0', '-2.0'],
                            'explication': "$4 \\times 1 + (-2) \\times 3 = 4 - 6 = -2$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer la norme $\\\\|\\\\vec{u}\\\\|$ pour $\\\\vec{u}(5 ; 12)$.",
                            'options': None,
                            'reponse_correcte': '13',
                            'tolerances': ['13,0', '13.0'],
                            'explication': "$\\|\\vec{u}\\| = \\sqrt{25 + 144} = \\sqrt{169} = 13$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Calculer $\\\\vec{u} \\\\cdot \\\\vec{v}$ avec $\\\\vec{u}(-3 ; 4)$ et $\\\\vec{v}(8 ; 6)$.",
                            'options': None,
                            'reponse_correcte': '0',
                            'tolerances': ['0,0', '0.0'],
                            'explication': "$(-3) \\times 8 + 4 \\times 6 = -24 + 24 = 0$. Les vecteurs sont orthogonaux.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Soit $\\\\vec{u}(1 ; 0)$ et $\\\\vec{v}(1 ; \\\\sqrt{3})$. Donner l'angle entre ces vecteurs en degrés.",
                            'options': None,
                            'reponse_correcte': '60',
                            'tolerances': ['60°', '60,0', '60.0'],
                            'explication': "$\\vec{u} \\cdot \\vec{v} = 1$, $\\|\\vec{u}\\| = 1$, $\\|\\vec{v}\\| = 2$. $\\cos\\theta = \\frac{1}{2}$, donc $\\theta = 60°$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Applications du produit scalaire',
                'duree': 35,
                'contenu': """# Applications du produit scalaire

## Introduction

Le produit scalaire est bien plus qu'une formule de calcul : c'est un outil puissant qui permet de démontrer des propriétés géométriques, d'appliquer la formule d'Al-Kashi, et de résoudre des problèmes de distances et d'angles dans le plan.

---

## Formule d'Al-Kashi (loi des cosinus)

### Théorème

Dans un triangle $ABC$ quelconque, avec les notations $a = BC$, $b = AC$, $c = AB$ :

$$a^2 = b^2 + c^2 - 2bc \\cos(\\widehat{A})$$

> C'est la généralisation du théorème de Pythagore au cas des triangles non rectangles. Quand $\\widehat{A} = 90°$, on retrouve $a^2 = b^2 + c^2$.

### Démonstration par le produit scalaire

$$a^2 = BC^2 = \\|\\overrightarrow{BC}\\|^2 = \\|\\overrightarrow{AC} - \\overrightarrow{AB}\\|^2$$

$$= \\|\\overrightarrow{AC}\\|^2 - 2\\overrightarrow{AC} \\cdot \\overrightarrow{AB} + \\|\\overrightarrow{AB}\\|^2$$

$$= b^2 + c^2 - 2\\overrightarrow{AC} \\cdot \\overrightarrow{AB}$$

Or $\\overrightarrow{AC} \\cdot \\overrightarrow{AB} = bc\\cos(\\widehat{A})$, d'où le résultat.

### Exemple

Dans un triangle $ABC$ avec $AB = 5$, $AC = 7$ et $\\widehat{A} = 60°$ :

$$BC^2 = 5^2 + 7^2 - 2 \\times 5 \\times 7 \\times \\cos 60° = 25 + 49 - 70 \\times \\frac{1}{2} = 74 - 35 = 39$$

$$BC = \\sqrt{39} \\approx 6{,}24$$

### Réciproque : calculer un angle

On peut aussi utiliser Al-Kashi pour trouver un angle :

$$\\cos(\\widehat{A}) = \\frac{b^2 + c^2 - a^2}{2bc}$$

**Exemple :** Triangle avec $a = 8$, $b = 5$, $c = 7$.

$$\\cos(\\widehat{A}) = \\frac{25 + 49 - 64}{2 \\times 5 \\times 7} = \\frac{10}{70} = \\frac{1}{7} \\approx 0{,}143$$

$$\\widehat{A} = \\arccos\\left(\\frac{1}{7}\\right) \\approx 81{,}8°$$

---

## Formule des médianes

### Théorème

Si $M$ est le milieu de $[BC]$ dans le triangle $ABC$, alors :

$$\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = AM^2 - \\frac{BC^2}{4}$$

### Démonstration

$$\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = (\\overrightarrow{AM} + \\overrightarrow{MB}) \\cdot (\\overrightarrow{AM} + \\overrightarrow{MC})$$

Comme $\\overrightarrow{MC} = -\\overrightarrow{MB}$ :

$$= (\\overrightarrow{AM} + \\overrightarrow{MB}) \\cdot (\\overrightarrow{AM} - \\overrightarrow{MB}) = \\|\\overrightarrow{AM}\\|^2 - \\|\\overrightarrow{MB}\\|^2 = AM^2 - \\frac{BC^2}{4}$$

---

## Démonstrations géométriques avec le produit scalaire

### Exemple 1 : Diagonales d'un losange

**Propriété :** Les diagonales d'un losange sont perpendiculaires.

**Preuve :** Soit $ABCD$ un losange ($AB = BC = CD = DA$). On montre que $\\overrightarrow{AC} \\cdot \\overrightarrow{BD} = 0$.

$$\\overrightarrow{AC} \\cdot \\overrightarrow{BD} = (\\overrightarrow{AB} + \\overrightarrow{BC}) \\cdot (\\overrightarrow{BA} + \\overrightarrow{AD})$$

$$= (\\overrightarrow{AB} + \\overrightarrow{BC}) \\cdot (-\\overrightarrow{AB} + \\overrightarrow{BC})$$

car $\\overrightarrow{AD} = \\overrightarrow{BC}$ (parallélogramme).

$$= -\\|\\overrightarrow{AB}\\|^2 + \\|\\overrightarrow{BC}\\|^2 = -AB^2 + BC^2 = 0$$

car $AB = BC$ (losange). Donc $\\overrightarrow{AC} \\perp \\overrightarrow{BD}$. ■

### Exemple 2 : Théorème de Pythagore

Si $\\widehat{A} = 90°$ dans le triangle $ABC$, alors $\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = 0$.

$$BC^2 = \\|\\overrightarrow{AC} - \\overrightarrow{AB}\\|^2 = AC^2 + AB^2 - 2\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = AC^2 + AB^2$$

On retrouve le théorème de Pythagore. ✓

---

## Projeté orthogonal

### Définition

Le **projeté orthogonal** d'un point $M$ sur une droite $(d)$ est le point $H$ de $(d)$ tel que $\\overrightarrow{MH} \\perp (d)$.

### Produit scalaire et projection

Si $H$ est le projeté orthogonal de $C$ sur la droite $(AB)$, alors :

$$\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = \\overrightarrow{AB} \\cdot \\overrightarrow{AH} = AB \\times AH \\times \\cos 0° = AB \\times AH$$

si $H$ est du même côté que $B$ par rapport à $A$ (sinon le signe change).

Cette formule est utile pour calculer des longueurs de projections.

---

## Inégalité de Cauchy-Schwarz

Pour tous vecteurs $\\vec{u}$ et $\\vec{v}$ :

$$|\\vec{u} \\cdot \\vec{v}| \\leq \\|\\vec{u}\\| \\times \\|\\vec{v}\\|$$

avec égalité si et seulement si $\\vec{u}$ et $\\vec{v}$ sont **colinéaires**.

> Cette inégalité découle de $|\\cos\\theta| \\leq 1$.

---

## À retenir

- **Al-Kashi** : $a^2 = b^2 + c^2 - 2bc\\cos(\\widehat{A})$.
- Pour prouver l'orthogonalité : montrer que le produit scalaire est nul.
- Le produit scalaire se développe avec les **identités remarquables** vectorielles.
- **Cauchy-Schwarz** : $|\\vec{u} \\cdot \\vec{v}| \\leq \\|\\vec{u}\\| \\cdot \\|\\vec{v}\\|$.
""",
                'quiz': {
                    'titre': 'Quiz — Applications du produit scalaire',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Dans un triangle $ABC$, la formule d'Al-Kashi s'écrit :",
                            'options': ["$a^2 = b^2 + c^2$", "$a^2 = b^2 + c^2 - 2bc\\\\cos(\\\\widehat{A})$", "$a^2 = b^2 - c^2 + 2bc$", "$a = b + c - 2bc\\\\cos(\\\\widehat{A})$"],
                            'reponse_correcte': '1',
                            'explication': "La formule d'Al-Kashi est $a^2 = b^2 + c^2 - 2bc\\cos(\\widehat{A})$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Si $\\\\widehat{A} = 90°$ dans la formule d'Al-Kashi, on retrouve :",
                            'options': ["La formule de la médiane", "Le théorème de Thalès", "Le théorème de Pythagore", "L'inégalité triangulaire"],
                            'reponse_correcte': '2',
                            'explication': "Avec $\\cos 90° = 0$, on obtient $a^2 = b^2 + c^2$, le théorème de Pythagore.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Le projeté orthogonal de $M$ sur une droite $(d)$ est le point $H$ tel que :",
                            'options': ["$MH$ est parallèle à $(d)$", "$MH$ est perpendiculaire à $(d)$", "$MH = 0$", "$H$ est le milieu de $M$"],
                            'reponse_correcte': '1',
                            'explication': "Le projeté orthogonal $H$ est le pied de la perpendiculaire abaissée de $M$ sur $(d)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "L'inégalité de Cauchy-Schwarz affirme que :",
                            'options': ["$\\\\vec{u} \\\\cdot \\\\vec{v} \\\\leq \\\\|\\\\vec{u}\\\\| + \\\\|\\\\vec{v}\\\\|$", "$|\\\\vec{u} \\\\cdot \\\\vec{v}| \\\\leq \\\\|\\\\vec{u}\\\\| \\\\times \\\\|\\\\vec{v}\\\\|$", "$\\\\vec{u} \\\\cdot \\\\vec{v} = \\\\|\\\\vec{u}\\\\| \\\\times \\\\|\\\\vec{v}\\\\|$", "$|\\\\vec{u} \\\\cdot \\\\vec{v}| \\\\geq \\\\|\\\\vec{u}\\\\| \\\\times \\\\|\\\\vec{v}\\\\|$"],
                            'reponse_correcte': '1',
                            'explication': "L'inégalité de Cauchy-Schwarz est $|\\vec{u} \\cdot \\vec{v}| \\leq \\|\\vec{u}\\| \\times \\|\\vec{v}\\|$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Pour montrer que les diagonales d'un losange sont perpendiculaires, on montre que :",
                            'options': ["Leurs normes sont égales", "Leur produit scalaire est nul", "Elles ont même direction", "Leurs milieux coïncident"],
                            'reponse_correcte': '1',
                            'explication': "On montre $\\overrightarrow{AC} \\cdot \\overrightarrow{BD} = 0$, ce qui prouve la perpendicularité.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Dans un triangle avec $AB = 5$, $AC = 7$ et $\\\\widehat{A} = 60°$, la formule d'Al-Kashi donne $BC^2 =$ :",
                            'options': ["$25 + 49 - 70$", "$25 + 49 - 35$", "$25 + 49 + 35$", "$74$"],
                            'reponse_correcte': '1',
                            'explication': "$BC^2 = 25 + 49 - 2 \\times 5 \\times 7 \\times \\cos 60° = 74 - 70 \\times \\frac{1}{2} = 74 - 35 = 39$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Si $BC^2 = 39$, alors $BC$ vaut :",
                            'options': ["$\\\\sqrt{39}$", "$39$", "$\\\\sqrt{74}$", "$6$"],
                            'reponse_correcte': '0',
                            'explication': "$BC = \\sqrt{39} \\approx 6{,}24$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Si $M$ est le milieu de $[BC]$, la formule de la médiane donne :",
                            'options': ["$\\\\overrightarrow{AB} \\\\cdot \\\\overrightarrow{AC} = AM^2 + \\\\frac{BC^2}{4}$", "$\\\\overrightarrow{AB} \\\\cdot \\\\overrightarrow{AC} = AM^2 - \\\\frac{BC^2}{4}$", "$\\\\overrightarrow{AB} \\\\cdot \\\\overrightarrow{AC} = AM - BC$", "$\\\\overrightarrow{AB} \\\\cdot \\\\overrightarrow{AC} = \\\\frac{AM^2}{BC^2}$"],
                            'reponse_correcte': '1',
                            'explication': "La formule de la médiane est $\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = AM^2 - \\frac{BC^2}{4}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "À partir d'Al-Kashi, $\\\\cos(\\\\widehat{A})$ s'exprime par :",
                            'options': ["$\\\\frac{a^2 + b^2 - c^2}{2ab}$", "$\\\\frac{b^2 + c^2 - a^2}{2bc}$", "$\\\\frac{a^2 - b^2 - c^2}{2bc}$", "$\\\\frac{b^2 + c^2 + a^2}{2bc}$"],
                            'reponse_correcte': '1',
                            'explication': "On isole : $\\cos(\\widehat{A}) = \\frac{b^2 + c^2 - a^2}{2bc}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "L'égalité dans Cauchy-Schwarz est atteinte lorsque les vecteurs sont :",
                            'options': ["Orthogonaux", "Colinéaires", "De même norme", "Unitaires"],
                            'reponse_correcte': '1',
                            'explication': "L'égalité $|\\vec{u} \\cdot \\vec{v}| = \\|\\vec{u}\\| \\times \\|\\vec{v}\\|$ signifie $|\\cos\\theta| = 1$, donc $\\theta = 0°$ ou $180°$ (colinéarité).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Triangle avec $a = 8$, $b = 5$, $c = 7$. Quelle est la valeur de $\\\\cos(\\\\widehat{A})$ ?",
                            'options': ["$\\\\frac{10}{70}$", "$\\\\frac{38}{80}$", "$\\\\frac{-14}{70}$", "$\\\\frac{74}{70}$"],
                            'reponse_correcte': '0',
                            'explication': "$\\cos(\\widehat{A}) = \\frac{25 + 49 - 64}{2 \\times 5 \\times 7} = \\frac{10}{70} = \\frac{1}{7}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Soit $ABCD$ un parallélogramme tel que $\\\\overrightarrow{AC} \\\\cdot \\\\overrightarrow{BD} = 0$. Que peut-on en déduire ?",
                            'options': ["$ABCD$ est un rectangle", "$ABCD$ est un losange", "$ABCD$ est un carré", "On ne peut rien conclure"],
                            'reponse_correcte': '1',
                            'explication': "Des diagonales perpendiculaires dans un parallélogramme caractérisent un losange.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Triangle $ABC$ isocèle avec $AB = AC = 6$ et $\\\\overrightarrow{AB} \\\\cdot \\\\overrightarrow{AC} = 18$. Quel est l'angle $\\\\widehat{BAC}$ ?",
                            'options': ["$30°$", "$45°$", "$60°$", "$90°$"],
                            'reponse_correcte': '2',
                            'explication': "$\\cos(\\widehat{A}) = \\frac{18}{6 \\times 6} = \\frac{1}{2}$, donc $\\widehat{A} = 60°$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "La formule d'Al-Kashi est une généralisation du théorème de Pythagore.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Quand l'angle vaut $90°$, $\\cos 90° = 0$ et on retrouve $a^2 = b^2 + c^2$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Pour prouver que deux droites sont perpendiculaires, on peut montrer que le produit scalaire de leurs vecteurs directeurs est nul.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Si les vecteurs directeurs sont orthogonaux ($\\vec{u} \\cdot \\vec{v} = 0$), les droites sont perpendiculaires.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Dans un triangle isocèle en $A$ avec $AB = AC = 5$ et $BC = 6$, la formule de la médiane donne $\\\\overrightarrow{AB} \\\\cdot \\\\overrightarrow{AC} = AM^2 - 9$ où $M$ est le milieu de $[BC]$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = AM^2 - \\frac{BC^2}{4} = AM^2 - \\frac{36}{4} = AM^2 - 9$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Triangle avec $b = 5$, $c = 7$ et $\\\\widehat{A} = 60°$. Calculer $BC^2$ avec Al-Kashi.",
                            'options': None,
                            'reponse_correcte': '39',
                            'tolerances': ['39,0', '39.0'],
                            'explication': "$BC^2 = 25 + 49 - 2 \\times 5 \\times 7 \\times \\frac{1}{2} = 74 - 35 = 39$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer $\\\\overrightarrow{AB} \\\\cdot \\\\overrightarrow{AC}$ sachant que $AB = 6$, $AC = 4$ et $\\\\widehat{A} = 120°$.",
                            'options': None,
                            'reponse_correcte': '-12',
                            'tolerances': ['-12,0', '-12.0'],
                            'explication': "$6 \\times 4 \\times \\cos 120° = 24 \\times (-\\frac{1}{2}) = -12$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Triangle $ABC$ avec $a = 7$, $b = 5$, $c = 3$. Calculer $\\\\cos(\\\\widehat{A})$ (donner une fraction irréductible).",
                            'options': None,
                            'reponse_correcte': '-1/2',
                            'tolerances': ['-0.5', '-0,5'],
                            'explication': "$\\cos(\\widehat{A}) = \\frac{25 + 9 - 49}{2 \\times 5 \\times 3} = \\frac{-15}{30} = -\\frac{1}{2}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Triangle $ABC$ avec $AB = 5$, $AC = 8$ et $\\\\overrightarrow{AB} \\\\cdot \\\\overrightarrow{AC} = 20$. Calculer $\\\\cos(\\\\widehat{BAC})$ (donner une fraction irréductible).",
                            'options': None,
                            'reponse_correcte': '1/2',
                            'tolerances': ['0.5', '0,5'],
                            'explication': "$\\cos(\\widehat{A}) = \\frac{20}{5 \\times 8} = \\frac{20}{40} = \\frac{1}{2}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 8 — Géométrie repérée
    # ──────────────────────────────────────────────
    {
        'ordre': 8,
        'titre': 'Géométrie repérée',
        'description': "Équation de droite, vecteur normal, équation de cercle, positions relatives et problèmes de géométrie analytique.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Équation de droite et vecteur normal',
                'duree': 35,
                'contenu': """# Équation de droite et vecteur normal

## Introduction

La **géométrie repérée** (ou analytique) consiste à étudier les figures géométriques à l'aide de coordonnées dans un repère. Dans cette leçon, nous reprenons les équations de droites et introduisons la notion de **vecteur normal**, qui fait le lien avec le produit scalaire.

---

## Rappels sur l'équation de droite

### Équation réduite

Une droite non verticale admet une équation de la forme :

$$y = mx + p$$

où $m$ est le **coefficient directeur** (pente) et $p$ l'**ordonnée à l'origine**.

### Équation cartésienne

Toute droite du plan admet une équation de la forme :

$$ax + by + c = 0$$

où $a$, $b$, $c$ sont des réels avec $(a, b) \\neq (0, 0)$.

> Les droites verticales ($x = k$) s'expriment sous la forme $1 \\cdot x + 0 \\cdot y - k = 0$.

### Passage d'une forme à l'autre

Si $b \\neq 0$ : $ax + by + c = 0 \\iff y = -\\dfrac{a}{b}x - \\dfrac{c}{b}$, donc $m = -\\dfrac{a}{b}$ et $p = -\\dfrac{c}{b}$.

---

## Vecteur directeur et vecteur normal

### Vecteur directeur

Un vecteur $\\vec{u}$ est **directeur** de la droite $(d)$ s'il est parallèle à $(d)$.

Si $(d)$ a pour équation $ax + by + c = 0$, alors $\\vec{u}(-b ; a)$ est un vecteur directeur de $(d)$.

### Vecteur normal

Un vecteur $\\vec{n}$ est **normal** à la droite $(d)$ s'il est **perpendiculaire** à tout vecteur directeur de $(d)$.

Si $(d)$ a pour équation $ax + by + c = 0$, alors $\\vec{n}(a ; b)$ est un vecteur normal de $(d)$.

> **Remarque :** Le vecteur normal se lit directement sur les coefficients de l'équation cartésienne.

### Vérification par le produit scalaire

$\\vec{u}(-b ; a)$ et $\\vec{n}(a ; b)$ :

$$\\vec{u} \\cdot \\vec{n} = (-b) \\times a + a \\times b = -ab + ab = 0 \\quad \\checkmark$$

---

## Déterminer une équation de droite

### Méthode 1 : Avec un point et un vecteur normal

La droite passant par $A(x_0 ; y_0)$ de vecteur normal $\\vec{n}(a ; b)$ a pour équation :

$$a(x - x_0) + b(y - y_0) = 0$$

soit :

$$ax + by + c = 0 \\quad \\text{avec } c = -ax_0 - by_0$$

**Exemple :** Droite passant par $A(1 ; 3)$ de vecteur normal $\\vec{n}(2 ; -5)$ :

$$2(x - 1) + (-5)(y - 3) = 0 \\iff 2x - 5y + 13 = 0$$

### Méthode 2 : Avec un point et un vecteur directeur

La droite passant par $A(x_0 ; y_0)$ de vecteur directeur $\\vec{u}(\\alpha ; \\beta)$ a pour équation :

$$\\beta(x - x_0) - \\alpha(y - y_0) = 0$$

**Exemple :** Droite passant par $B(2 ; -1)$ de vecteur directeur $\\vec{u}(3 ; 4)$ :

$$4(x - 2) - 3(y + 1) = 0 \\iff 4x - 3y - 11 = 0$$

### Méthode 3 : Avec deux points

La droite passant par $A(x_A ; y_A)$ et $B(x_B ; y_B)$ a pour vecteur directeur $\\overrightarrow{AB}(x_B - x_A ; y_B - y_A)$.

**Exemple :** Droite $(AB)$ avec $A(1 ; 2)$ et $B(4 ; -1)$ :

$\\overrightarrow{AB}(3 ; -3)$, d'où $\\vec{n}(3 ; 3)$ (ou simplifié $\\vec{n}(1 ; 1)$).

$$1(x - 1) + 1(y - 2) = 0 \\iff x + y - 3 = 0$$

---

## Distance d'un point à une droite

### Formule

La distance du point $M(x_M ; y_M)$ à la droite $(d) : ax + by + c = 0$ est :

$$d(M, (d)) = \\frac{|ax_M + by_M + c|}{\\sqrt{a^2 + b^2}}$$

### Démonstration (esquisse)

Si $H$ est le projeté orthogonal de $M$ sur $(d)$, alors $d(M, (d)) = MH$. On montre que $\\overrightarrow{MH} = t \\cdot \\vec{n}$ où $t = -\\dfrac{ax_M + by_M + c}{a^2 + b^2}$, et donc $MH = |t| \\cdot \\|\\vec{n}\\|$.

### Exemple

Distance de $P(3 ; 1)$ à la droite $2x - y + 4 = 0$ :

$$d = \\frac{|2 \\times 3 + (-1) \\times 1 + 4|}{\\sqrt{4 + 1}} = \\frac{|6 - 1 + 4|}{\\sqrt{5}} = \\frac{9}{\\sqrt{5}} = \\frac{9\\sqrt{5}}{5}$$

---

## Positions relatives de deux droites

Soient $(d_1) : a_1x + b_1y + c_1 = 0$ et $(d_2) : a_2x + b_2y + c_2 = 0$.

| Relation | Condition |
|----------|-----------|
| Sécantes | $\\vec{n_1}$ et $\\vec{n_2}$ non colinéaires |
| Parallèles | $\\vec{n_1}$ et $\\vec{n_2}$ colinéaires ($a_1 b_2 = a_2 b_1$) |
| Confondues | Parallèles et un point commun |
| Perpendiculaires | $\\vec{n_1} \\cdot \\vec{n_2} = 0$ (soit $a_1 a_2 + b_1 b_2 = 0$) |

### Exemple

$(d_1) : 2x + 3y - 1 = 0$ et $(d_2) : 3x - 2y + 5 = 0$.

$\\vec{n_1}(2 ; 3)$ et $\\vec{n_2}(3 ; -2)$ : $\\vec{n_1} \\cdot \\vec{n_2} = 6 - 6 = 0$.

Les droites sont **perpendiculaires**.

---

## À retenir

- Droite $ax + by + c = 0$ : vecteur normal $\\vec{n}(a ; b)$, vecteur directeur $\\vec{u}(-b ; a)$.
- Droite par $A(x_0 ; y_0)$ de vecteur normal $\\vec{n}(a ; b)$ : $a(x-x_0) + b(y-y_0) = 0$.
- Distance point-droite : $d = \\dfrac{|ax_M + by_M + c|}{\\sqrt{a^2 + b^2}}$.
- Perpendiculaires $\\iff$ $a_1a_2 + b_1b_2 = 0$.
""",
                'quiz': {
                    'titre': 'Quiz — Équation de droite et vecteur normal',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quelle est l'équation réduite d'une droite non verticale ?",
                            'options': ["$ax + by + c = 0$", "$y = mx + p$", "$x = k$", "$y = ax^2 + bx + c$"],
                            'reponse_correcte': '1',
                            'explication': "L'équation réduite est $y = mx + p$ avec $m$ le coefficient directeur et $p$ l'ordonnée à l'origine.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Si la droite $(d)$ a pour équation $ax + by + c = 0$, un vecteur normal à $(d)$ est :",
                            'options': ["$\\\\vec{n}(-b ; a)$", "$\\\\vec{n}(a ; b)$", "$\\\\vec{n}(c ; a)$", "$\\\\vec{n}(b ; -a)$"],
                            'reponse_correcte': '1',
                            'explication': "Le vecteur normal se lit directement sur les coefficients : $\\vec{n}(a ; b)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Si $(d) : ax + by + c = 0$, un vecteur directeur de $(d)$ est :",
                            'options': ["$\\\\vec{u}(a ; b)$", "$\\\\vec{u}(b ; a)$", "$\\\\vec{u}(-b ; a)$", "$\\\\vec{u}(a ; -b)$"],
                            'reponse_correcte': '2',
                            'explication': "Un vecteur directeur est $\\vec{u}(-b ; a)$, perpendiculaire au vecteur normal $\\vec{n}(a ; b)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Le coefficient directeur de la droite $3x + 2y - 6 = 0$ est :",
                            'options': ["$\\\\frac{3}{2}$", "$-\\\\frac{3}{2}$", "$\\\\frac{2}{3}$", "$-\\\\frac{2}{3}$"],
                            'reponse_correcte': '1',
                            'explication': "$m = -\\frac{a}{b} = -\\frac{3}{2}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La droite passant par $A(1 ; 3)$ de vecteur normal $\\\\vec{n}(2 ; -5)$ a pour équation :",
                            'options': ["$2x - 5y + 13 = 0$", "$2x - 5y - 13 = 0$", "$5x + 2y - 11 = 0$", "$-5x + 2y + 3 = 0$"],
                            'reponse_correcte': '0',
                            'explication': "$2(x - 1) + (-5)(y - 3) = 0 \\iff 2x - 5y + 13 = 0$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Deux droites sont perpendiculaires si et seulement si :",
                            'options': ["Leurs vecteurs normaux sont colinéaires", "$a_1a_2 + b_1b_2 = 0$", "$a_1b_2 - a_2b_1 = 0$", "Leurs coefficients directeurs sont égaux"],
                            'reponse_correcte': '1',
                            'explication': "Perpendiculaires $\\iff$ vecteurs normaux orthogonaux $\\iff$ $a_1a_2 + b_1b_2 = 0$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Quelle est la formule de la distance du point $M(x_M ; y_M)$ à la droite $ax + by + c = 0$ ?",
                            'options': ["$\\\\frac{ax_M + by_M + c}{a^2 + b^2}$", "$\\\\frac{|ax_M + by_M + c|}{\\\\sqrt{a^2 + b^2}}$", "$\\\\frac{|ax_M + by_M + c|}{a + b}$", "$\\\\sqrt{(ax_M)^2 + (by_M)^2}$"],
                            'reponse_correcte': '1',
                            'explication': "$d(M, (d)) = \\frac{|ax_M + by_M + c|}{\\sqrt{a^2 + b^2}}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "La droite passant par $A(2 ; -1)$ et $B(5 ; 3)$ a pour vecteur directeur :",
                            'options': ["$\\\\vec{u}(3 ; 4)$", "$\\\\vec{u}(7 ; 2)$", "$\\\\vec{u}(4 ; 3)$", "$\\\\vec{u}(5 ; -1)$"],
                            'reponse_correcte': '0',
                            'explication': "$\\overrightarrow{AB}(5-2 ; 3-(-1)) = (3 ; 4)$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Les droites $2x + 3y - 1 = 0$ et $3x - 2y + 5 = 0$ sont :",
                            'options': ["Parallèles", "Perpendiculaires", "Confondues", "Sécantes non perpendiculaires"],
                            'reponse_correcte': '1',
                            'explication': "$\\vec{n_1} \\cdot \\vec{n_2} = 2 \\times 3 + 3 \\times (-2) = 0$, donc perpendiculaires.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Si $b \\\\neq 0$, l'ordonnée à l'origine $p$ de la droite $ax + by + c = 0$ vaut :",
                            'options': ["$-\\\\frac{a}{b}$", "$\\\\frac{c}{b}$", "$-\\\\frac{c}{b}$", "$\\\\frac{a}{c}$"],
                            'reponse_correcte': '2',
                            'explication': "$y = -\\frac{a}{b}x - \\frac{c}{b}$, donc $p = -\\frac{c}{b}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Calculer la distance du point $P(3 ; 1)$ à la droite $2x - y + 4 = 0$.",
                            'options': ["$\\\\frac{9}{\\\\sqrt{5}}$", "$\\\\frac{3}{\\\\sqrt{5}}$", "$\\\\frac{9}{5}$", "$\\\\frac{5}{\\\\sqrt{9}}$"],
                            'reponse_correcte': '0',
                            'explication': "$d = \\frac{|6 - 1 + 4|}{\\sqrt{4+1}} = \\frac{9}{\\sqrt{5}}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "La droite passant par $B(2 ; -1)$ de vecteur directeur $\\\\vec{u}(3 ; 4)$ a pour équation :",
                            'options': ["$3x + 4y - 2 = 0$", "$4x - 3y - 11 = 0$", "$4x + 3y - 5 = 0$", "$3x - 4y - 10 = 0$"],
                            'reponse_correcte': '1',
                            'explication': "Vecteur normal $\\vec{n}(4 ; -3)$. $4(x-2) - 3(y+1) = 0 \\iff 4x - 3y - 11 = 0$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Les droites $(d_1) : x + 2y - 3 = 0$ et $(d_2) : 2x + 4y + 1 = 0$ sont :",
                            'options': ["Perpendiculaires", "Sécantes", "Confondues", "Strictement parallèles"],
                            'reponse_correcte': '3',
                            'explication': "$\\vec{n_1}(1;2)$ et $\\vec{n_2}(2;4) = 2\\vec{n_1}$ sont colinéaires, mais les droites ne passent pas par les mêmes points.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Le vecteur normal d'une droite est parallèle à cette droite.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le vecteur normal est perpendiculaire à la droite, pas parallèle.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Toute droite du plan admet une équation cartésienne de la forme $ax + by + c = 0$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Oui, y compris les droites verticales ($b = 0$).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Si deux droites ont des vecteurs normaux colinéaires, elles sont nécessairement confondues.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Elles sont parallèles, mais pas forcément confondues (elles peuvent être parallèles distinctes).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Donner le coefficient directeur de la droite $5x - 2y + 7 = 0$ (sous forme de fraction).",
                            'options': None,
                            'reponse_correcte': '5/2',
                            'tolerances': ['2.5', '2,5'],
                            'explication': "$m = -\\frac{a}{b} = -\\frac{5}{-2} = \\frac{5}{2}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer la distance du point $A(1 ; 0)$ à la droite $3x + 4y - 7 = 0$ (donner une fraction).",
                            'options': None,
                            'reponse_correcte': '4/5',
                            'tolerances': ['0.8', '0,8'],
                            'explication': "$d = \\frac{|3 + 0 - 7|}{\\sqrt{9+16}} = \\frac{4}{5}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Donner l'équation cartésienne de la droite passant par $A(3 ; -2)$ et $B(1 ; 4)$ sous la forme $ax + by + c = 0$ (avec $a > 0$, entiers).",
                            'options': None,
                            'reponse_correcte': '3x + y - 7 = 0',
                            'tolerances': ['3x+y-7=0'],
                            'explication': "$\\overrightarrow{AB}(-2 ; 6)$, $\\vec{n}(6 ; 2)$ simplifié $(3 ; 1)$. $3(x-3) + 1(y+2) = 0 \\iff 3x + y - 7 = 0$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Donner les coordonnées d'un vecteur normal à la droite $y = -\\\\frac{3}{4}x + 2$ sous la forme $(a ; b)$ avec $a$ et $b$ entiers positifs.",
                            'options': None,
                            'reponse_correcte': '(3 ; 4)',
                            'tolerances': ['(3;4)', '3 ; 4', '3;4'],
                            'explication': "$y = -\\frac{3}{4}x + 2 \\iff 3x + 4y - 8 = 0$. Le vecteur normal est $\\vec{n}(3 ; 4)$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Équation de cercle',
                'duree': 35,
                'contenu': """# Équation de cercle

## Introduction

Après les droites, le **cercle** est la deuxième figure fondamentale de la géométrie repérée. Son équation cartésienne permet de résoudre de nombreux problèmes : appartenance d'un point, intersection cercle-droite, tangente, etc.

---

## Équation cartésienne d'un cercle

### Définition

Le **cercle** de centre $\\Omega(a ; b)$ et de rayon $r > 0$ est l'ensemble des points $M(x ; y)$ tels que $\\Omega M = r$, soit :

$$(x - a)^2 + (y - b)^2 = r^2$$

C'est l'**équation cartésienne** du cercle.

### Exemples

- Cercle de centre $O(0 ; 0)$ et de rayon 1 (cercle unité) : $x^2 + y^2 = 1$.
- Cercle de centre $A(2 ; -3)$ et de rayon 5 : $(x-2)^2 + (y+3)^2 = 25$.

### Vérifier qu'un point appartient à un cercle

Le point $M(5 ; 1)$ appartient-il au cercle $(x-2)^2 + (y+3)^2 = 25$ ?

$$(5-2)^2 + (1+3)^2 = 9 + 16 = 25 \\quad \\checkmark$$

Oui, $M$ appartient au cercle.

---

## Forme développée

En développant l'équation $(x-a)^2 + (y-b)^2 = r^2$ :

$$x^2 - 2ax + a^2 + y^2 - 2by + b^2 = r^2$$

$$x^2 + y^2 - 2ax - 2by + (a^2 + b^2 - r^2) = 0$$

On obtient la **forme développée** :

$$x^2 + y^2 + Dx + Ey + F = 0$$

avec $D = -2a$, $E = -2b$, $F = a^2 + b^2 - r^2$.

### Réciproquement

À partir de $x^2 + y^2 + Dx + Ey + F = 0$, on retrouve le centre et le rayon en **complétant le carré** :

$$\\left(x + \\frac{D}{2}\\right)^2 + \\left(y + \\frac{E}{2}\\right)^2 = \\frac{D^2 + E^2 - 4F}{4}$$

- **Centre** : $\\Omega\\left(-\\frac{D}{2} ; -\\frac{E}{2}\\right)$.
- **Rayon** : $r = \\frac{\\sqrt{D^2 + E^2 - 4F}}{2}$ (à condition que $D^2 + E^2 - 4F > 0$).

### Exemple complet

Identifier le cercle $x^2 + y^2 - 6x + 4y - 12 = 0$.

$$\\left(x^2 - 6x + 9\\right) + \\left(y^2 + 4y + 4\\right) = 12 + 9 + 4$$

$$(x - 3)^2 + (y + 2)^2 = 25$$

Centre $\\Omega(3 ; -2)$, rayon $r = 5$.

---

## Cercle de diamètre $[AB]$

### Théorème

Le cercle de diamètre $[AB]$ est l'ensemble des points $M$ tels que $\\overrightarrow{MA} \\cdot \\overrightarrow{MB} = 0$.

> C'est une conséquence directe du **théorème de Thalès dans le cercle** : l'angle inscrit dans un demi-cercle est droit.

### Démonstration

$M$ est sur le cercle de diamètre $[AB]$ $\\iff$ $\\widehat{AMB} = 90°$ $\\iff$ $\\overrightarrow{MA} \\perp \\overrightarrow{MB}$ $\\iff$ $\\overrightarrow{MA} \\cdot \\overrightarrow{MB} = 0$.

### Équation

Si $A(x_A ; y_A)$ et $B(x_B ; y_B)$, le cercle de diamètre $[AB]$ a pour équation :

$$(x - x_A)(x - x_B) + (y - y_A)(y - y_B) = 0$$

**Exemple :** Cercle de diamètre $[AB]$ avec $A(1 ; 3)$ et $B(5 ; -1)$ :

$$(x-1)(x-5) + (y-3)(y+1) = 0$$

$$x^2 - 6x + 5 + y^2 - 2y - 3 = 0$$

$$x^2 + y^2 - 6x - 2y + 2 = 0$$

Centre : milieu de $[AB]$ soit $(3 ; 1)$, rayon : $\\frac{AB}{2} = \\frac{\\sqrt{16+16}}{2} = \\frac{4\\sqrt{2}}{2} = 2\\sqrt{2}$.

---

## Tangente à un cercle

### Propriété

La tangente au cercle $\\mathcal{C}$ de centre $\\Omega$ en un point $M_0$ du cercle est la droite passant par $M_0$ et **perpendiculaire** au rayon $[\\Omega M_0]$.

### Vecteur normal de la tangente

Le vecteur $\\overrightarrow{\\Omega M_0}$ est un **vecteur normal** à la tangente en $M_0$.

Si $\\Omega(a ; b)$ et $M_0(x_0 ; y_0)$, alors $\\overrightarrow{\\Omega M_0}(x_0 - a ; y_0 - b)$ et la tangente a pour équation :

$$(x_0 - a)(x - x_0) + (y_0 - b)(y - y_0) = 0$$

### Exemple

Tangente au cercle $(x-2)^2 + (y-1)^2 = 10$ au point $M_0(5 ; 2)$.

$\\overrightarrow{\\Omega M_0}(3 ; 1)$, donc la tangente est :

$$3(x - 5) + 1(y - 2) = 0 \\iff 3x + y - 17 = 0$$

---

## Intersection cercle-droite

Pour trouver les points d'intersection d'un cercle et d'une droite :

1. Exprimer $y$ en fonction de $x$ (ou $x$ en fonction de $y$) à partir de l'équation de la droite.
2. Substituer dans l'équation du cercle pour obtenir une **équation du second degré**.
3. Analyser le discriminant :
   - $\\Delta > 0$ : deux points d'intersection (la droite est **sécante**).
   - $\\Delta = 0$ : un point d'intersection (la droite est **tangente**).
   - $\\Delta < 0$ : aucune intersection (la droite est **extérieure**).

### Exemple

Cercle $x^2 + y^2 = 25$ et droite $y = x + 1$.

$$x^2 + (x+1)^2 = 25 \\iff 2x^2 + 2x + 1 - 25 = 0 \\iff 2x^2 + 2x - 24 = 0 \\iff x^2 + x - 12 = 0$$

$$\\Delta = 1 + 48 = 49 > 0$$

$$x_1 = \\frac{-1 + 7}{2} = 3, \\qquad x_2 = \\frac{-1 - 7}{2} = -4$$

Points d'intersection : $(3 ; 4)$ et $(-4 ; -3)$.

---

## À retenir

- Cercle de centre $\\Omega(a;b)$, rayon $r$ : $(x-a)^2 + (y-b)^2 = r^2$.
- Forme développée : $x^2 + y^2 + Dx + Ey + F = 0$ → compléter le carré.
- Cercle de diamètre $[AB]$ : $(x-x_A)(x-x_B) + (y-y_A)(y-y_B) = 0$.
- Tangente en $M_0$ : perpendiculaire au rayon, vecteur normal $\\overrightarrow{\\Omega M_0}$.
- Intersection cercle-droite : substitution → second degré → discriminant.
""",
                'quiz': {
                    'titre': 'Quiz — Équation de cercle',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "L'équation du cercle de centre $\\\\Omega(a ; b)$ et de rayon $r$ est :",
                            'options': ["$(x + a)^2 + (y + b)^2 = r$", "$(x - a)^2 + (y - b)^2 = r^2$", "$x^2 + y^2 = r^2$", "$(x - a) + (y - b) = r$"],
                            'reponse_correcte': '1',
                            'explication': "L'équation cartésienne est $(x - a)^2 + (y - b)^2 = r^2$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "L'équation du cercle unité (centre $O$, rayon $1$) est :",
                            'options': ["$x + y = 1$", "$x^2 + y^2 = 1$", "$(x - 1)^2 + (y - 1)^2 = 1$", "$|x| + |y| = 1$"],
                            'reponse_correcte': '1',
                            'explication': "Le cercle unité a pour centre l'origine et rayon 1 : $x^2 + y^2 = 1$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Le point $M(3 ; 4)$ appartient-il au cercle $x^2 + y^2 = 25$ ?",
                            'options': ["Oui", "Non", "On ne peut pas savoir", "Seulement si $M$ est sur un axe"],
                            'reponse_correcte': '0',
                            'explication': "$3^2 + 4^2 = 9 + 16 = 25$ ✓.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Le cercle $(x - 2)^2 + (y + 3)^2 = 16$ a pour centre et rayon :",
                            'options': ["Centre $(2 ; -3)$, rayon $4$", "Centre $(-2 ; 3)$, rayon $16$", "Centre $(2 ; 3)$, rayon $4$", "Centre $(2 ; -3)$, rayon $16$"],
                            'reponse_correcte': '0',
                            'explication': "Centre $(2 ; -3)$ et $r = \\sqrt{16} = 4$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La tangente à un cercle en un point $M_0$ est perpendiculaire :",
                            'options': ["À une corde passant par $M_0$", "Au diamètre quelconque", "Au rayon $[\\\\Omega M_0]$", "À l'axe des abscisses"],
                            'reponse_correcte': '2',
                            'explication': "La tangente en $M_0$ est perpendiculaire au rayon $[\\Omega M_0]$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Le cercle de diamètre $[AB]$ est l'ensemble des points $M$ vérifiant :",
                            'options': ["$MA + MB = AB$", "$\\\\overrightarrow{MA} \\\\cdot \\\\overrightarrow{MB} = 0$", "$MA = MB$", "$\\\\overrightarrow{MA} + \\\\overrightarrow{MB} = \\\\vec{0}$"],
                            'reponse_correcte': '1',
                            'explication': "L'angle inscrit dans un demi-cercle est droit, donc $\\overrightarrow{MA} \\cdot \\overrightarrow{MB} = 0$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Identifier le cercle $x^2 + y^2 - 6x + 4y - 12 = 0$.",
                            'options': ["Centre $(3 ; -2)$, rayon $5$", "Centre $(-3 ; 2)$, rayon $5$", "Centre $(3 ; -2)$, rayon $25$", "Centre $(6 ; -4)$, rayon $\\\\sqrt{12}$"],
                            'reponse_correcte': '0',
                            'explication': "$(x-3)^2 + (y+2)^2 = 9 + 4 + 12 = 25$, donc centre $(3 ; -2)$ et rayon $5$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Dans la forme développée $x^2 + y^2 + Dx + Ey + F = 0$, le rayon vaut :",
                            'options': ["$\\\\frac{D^2 + E^2 - 4F}{4}$", "$\\\\frac{\\\\sqrt{D^2 + E^2 - 4F}}{2}$", "$D^2 + E^2 + F$", "$\\\\frac{D + E}{2}$"],
                            'reponse_correcte': '1',
                            'explication': "$r = \\frac{\\sqrt{D^2 + E^2 - 4F}}{2}$, à condition que $D^2 + E^2 - 4F > 0$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Combien de points d'intersection a une droite sécante avec un cercle ?",
                            'options': ["$0$", "$1$", "$2$", "$3$"],
                            'reponse_correcte': '2',
                            'explication': "Une droite sécante coupe le cercle en exactement 2 points.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "En substituant l'équation de la droite dans celle du cercle, on obtient :",
                            'options': ["Une équation du premier degré", "Une équation du second degré", "Un système de deux équations", "Une inéquation"],
                            'reponse_correcte': '1',
                            'explication': "La substitution conduit à une équation du second degré dont le discriminant détermine le nombre d'intersections.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Si le discriminant est nul lors de l'intersection cercle-droite, la droite est :",
                            'options': ["Extérieure au cercle", "Sécante", "Tangente", "Confondue avec le cercle"],
                            'reponse_correcte': '2',
                            'explication': "$\\Delta = 0$ : un seul point d'intersection, la droite est tangente au cercle.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "L'équation du cercle de diamètre $[A(1;3), B(5;-1)]$ peut s'écrire :",
                            'options': ["$(x-1)(x-5) + (y-3)(y+1) = 0$", "$(x-3)^2 + (y-1)^2 = 8$", "Les deux sont correctes", "Aucune de ces réponses"],
                            'reponse_correcte': '2',
                            'explication': "La première traduit $\\overrightarrow{MA} \\cdot \\overrightarrow{MB} = 0$, et en développant on retrouve la seconde.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Les points d'intersection du cercle $x^2 + y^2 = 25$ et de la droite $y = x + 1$ sont :",
                            'options': ["$(3 ; 4)$ et $(-4 ; -3)$", "$(4 ; 3)$ et $(-3 ; -4)$", "$(5 ; 0)$ et $(0 ; 5)$", "Il n'y a pas d'intersection"],
                            'reponse_correcte': '0',
                            'explication': "$x^2 + (x+1)^2 = 25 \\iff x^2 + x - 12 = 0$, $x = 3$ ou $x = -4$, d'où $(3;4)$ et $(-4;-3)$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Un cercle de rayon $r$ a une équation de la forme $(x - a)^2 + (y - b)^2 = r^2$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est la définition même de l'équation cartésienne du cercle.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "L'équation $x^2 + y^2 + Dx + Ey + F = 0$ représente toujours un cercle.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Seulement si $D^2 + E^2 - 4F > 0$. Sinon, c'est un point ou l'ensemble vide.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La tangente au cercle en un point $M_0$ a pour vecteur normal $\\\\overrightarrow{\\\\Omega M_0}$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Le rayon $\\overrightarrow{\\Omega M_0}$ est perpendiculaire à la tangente, donc c'est un vecteur normal.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Donner le rayon du cercle $(x - 1)^2 + (y + 4)^2 = 49$.",
                            'options': None,
                            'reponse_correcte': '7',
                            'tolerances': ['7,0', '7.0'],
                            'explication': "$r = \\sqrt{49} = 7$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Donner les coordonnées du centre du cercle $x^2 + y^2 - 4x + 6y - 3 = 0$ sous la forme $(a ; b)$.",
                            'options': None,
                            'reponse_correcte': '(2 ; -3)',
                            'tolerances': ['(2;-3)', '(2 ; -3)', '2 ; -3', '2;-3'],
                            'explication': "$(x-2)^2 + (y+3)^2 = 4 + 9 + 3 = 16$. Centre $(2 ; -3)$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Calculer le rayon du cercle $x^2 + y^2 - 4x + 6y - 3 = 0$.",
                            'options': None,
                            'reponse_correcte': '4',
                            'tolerances': ['4,0', '4.0'],
                            'explication': "$(x-2)^2 + (y+3)^2 = 16$, donc $r = 4$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Donner l'équation de la tangente au cercle $(x-1)^2 + (y-2)^2 = 5$ au point $M_0(3 ; 3)$ sous la forme $ax + by + c = 0$ (avec $a > 0$, entiers).",
                            'options': None,
                            'reponse_correcte': '2x + y - 9 = 0',
                            'tolerances': ['2x+y-9=0'],
                            'explication': "$\\overrightarrow{\\Omega M_0}(2 ; 1)$. Tangente : $2(x-3) + 1(y-3) = 0 \\iff 2x + y - 9 = 0$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 3,
                'titre': 'Problèmes de géométrie analytique',
                'duree': 30,
                'contenu': """# Problèmes de géométrie analytique

## Introduction

La géométrie analytique combine les outils algébriques (équations, coordonnées, produit scalaire) avec le raisonnement géométrique. Cette leçon propose des **méthodes de résolution** systématiques et des exemples de problèmes types rencontrés en Première.

---

## Méthode générale

Face à un problème de géométrie analytique, on suit souvent ces étapes :

1. **Placer un repère** (souvent orthonormé, parfois donné).
2. **Traduire** les données géométriques en coordonnées.
3. **Calculer** (distances, produits scalaires, équations).
4. **Conclure** en revenant à l'interprétation géométrique.

---

## Problème 1 : Nature d'un quadrilatère

**Énoncé :** Soit $A(1 ; 2)$, $B(4 ; 6)$, $C(8 ; 3)$ et $D(5 ; -1)$. Déterminer la nature du quadrilatère $ABCD$.

**Étape 1 : Vecteurs côtés**

$$\\overrightarrow{AB}(3 ; 4) \\qquad \\overrightarrow{DC}(3 ; 4)$$

$$\\overrightarrow{AB} = \\overrightarrow{DC}$$, donc $ABCD$ est un **parallélogramme**.

**Étape 2 : Est-ce un rectangle ?**

$$\\overrightarrow{AB} \\cdot \\overrightarrow{AD} = (3)(4) + (4)(-3) = 12 - 12 = 0$$

avec $\\overrightarrow{AD}(4 ; -3)$.

$\\overrightarrow{AB} \\perp \\overrightarrow{AD}$, donc $ABCD$ est un **rectangle**.

**Étape 3 : Est-ce un carré ?**

$$AB = \\sqrt{9 + 16} = 5 \\qquad AD = \\sqrt{16 + 9} = 5$$

$AB = AD$, donc $ABCD$ est un **carré**. ■

---

## Problème 2 : Ensemble de points

**Énoncé :** On considère $A(1 ; 0)$ et $B(3 ; 0)$. Déterminer l'ensemble des points $M(x ; y)$ tels que $MA^2 - MB^2 = 8$.

**Calcul :**

$$MA^2 = (x-1)^2 + y^2 = x^2 - 2x + 1 + y^2$$

$$MB^2 = (x-3)^2 + y^2 = x^2 - 6x + 9 + y^2$$

$$MA^2 - MB^2 = (x^2 - 2x + 1 + y^2) - (x^2 - 6x + 9 + y^2) = 4x - 8$$

$$4x - 8 = 8 \\iff x = 4$$

L'ensemble cherché est la **droite verticale** d'équation $x = 4$.

> **Remarque :** On pouvait utiliser la formule $MA^2 - MB^2 = 2\\overrightarrow{BA} \\cdot \\overrightarrow{BI}$ où $I$ est le milieu de $[AB]$, mais le calcul direct est ici plus rapide.

---

## Problème 3 : Intersection de droites et cercle

**Énoncé :** Soit le cercle $\\mathcal{C}$ d'équation $(x-1)^2 + (y-2)^2 = 20$ et la droite $(d)$ d'équation $2x + y - 7 = 0$.

**a) Vérifier que la droite est sécante au cercle.**

Distance du centre $\\Omega(1 ; 2)$ à $(d)$ :

$$d(\\Omega, (d)) = \\frac{|2 \\times 1 + 1 \\times 2 - 7|}{\\sqrt{4 + 1}} = \\frac{|-3|}{\\sqrt{5}} = \\frac{3}{\\sqrt{5}} = \\frac{3\\sqrt{5}}{5} \\approx 1{,}34$$

Comme $r = \\sqrt{20} = 2\\sqrt{5} \\approx 4{,}47 > 1{,}34$, la droite est bien **sécante** au cercle.

**b) Trouver les points d'intersection.**

De $(d)$ : $y = 7 - 2x$. On substitue :

$$(x-1)^2 + (7-2x-2)^2 = 20$$

$$(x-1)^2 + (5-2x)^2 = 20$$

$$x^2 - 2x + 1 + 25 - 20x + 4x^2 = 20$$

$$5x^2 - 22x + 6 = 0$$

$$\\Delta = 484 - 120 = 364$$

$$x = \\frac{22 \\pm \\sqrt{364}}{10} = \\frac{22 \\pm 2\\sqrt{91}}{10} = \\frac{11 \\pm \\sqrt{91}}{5}$$

---

## Problème 4 : Médiatrice et cercle circonscrit

**Énoncé :** Trouver le cercle circonscrit au triangle $A(0 ; 0)$, $B(6 ; 0)$, $C(2 ; 4)$.

**Méthode :** Le centre du cercle circonscrit est l'intersection des médiatrices.

**Médiatrice de $[AB]$ :** Milieu $I(3 ; 0)$, vecteur directeur de $AB$ : $\\vec{u}(6 ; 0)$, donc la médiatrice est perpendiculaire avec vecteur normal $(6 ; 0)$ :

$$6(x - 3) + 0(y - 0) = 0 \\iff x = 3$$

**Médiatrice de $[AC]$ :** Milieu $J(1 ; 2)$, $\\overrightarrow{AC}(2 ; 4)$ est vecteur normal :

$$2(x - 1) + 4(y - 2) = 0 \\iff 2x + 4y - 10 = 0 \\iff x + 2y = 5$$

**Intersection :** $x = 3$ et $x + 2y = 5 \\implies 3 + 2y = 5 \\implies y = 1$.

Centre $\\Omega(3 ; 1)$, rayon $r = \\Omega A = \\sqrt{9 + 1} = \\sqrt{10}$.

**Équation :** $(x-3)^2 + (y-1)^2 = 10$.

**Vérification :** $\\Omega B = \\sqrt{9 + 1} = \\sqrt{10}$ ✓ et $\\Omega C = \\sqrt{1 + 9} = \\sqrt{10}$ ✓.

---

## Problème 5 : Lieu géométrique avec produit scalaire

**Énoncé :** Soit $A(0 ; 0)$ et $B(4 ; 0)$. Déterminer l'ensemble des points $M$ tels que $\\overrightarrow{MA} \\cdot \\overrightarrow{MB} = 0$.

Avec $M(x ; y)$ :

$$\\overrightarrow{MA}(-x ; -y) \\qquad \\overrightarrow{MB}(4-x ; -y)$$

$$\\overrightarrow{MA} \\cdot \\overrightarrow{MB} = (-x)(4-x) + (-y)(-y) = -4x + x^2 + y^2 = 0$$

$$x^2 + y^2 - 4x = 0 \\iff (x - 2)^2 + y^2 = 4$$

C'est le **cercle de diamètre $[AB]$**, de centre $(2 ; 0)$ et de rayon 2. ✓

---

## Résumé des méthodes

| Objectif | Outil principal |
|----------|----------------|
| Nature d'un quadrilatère | Vecteurs côtés, produit scalaire, normes |
| Ensemble de points ($MA^2 + MB^2 = k$, etc.) | Calcul direct en coordonnées |
| Intersection droite-cercle | Substitution → second degré |
| Cercle circonscrit | Intersection de deux médiatrices |
| Lieu géométrique ($\\overrightarrow{MA} \\cdot \\overrightarrow{MB} = 0$) | Produit scalaire en coordonnées |

---

## À retenir

- En géométrie analytique, on **traduit** le problème en coordonnées, on **calcule**, puis on **interprète**.
- Le produit scalaire, les distances et les équations de droites/cercles sont les outils centraux.
- Pour un cercle de diamètre $[AB]$ : $\\overrightarrow{MA} \\cdot \\overrightarrow{MB} = 0$.
- Le cercle circonscrit a son centre à l'intersection des médiatrices.
""",
                'quiz': {
                    'titre': 'Quiz — Problèmes de géométrie analytique',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "La première étape pour résoudre un problème de géométrie analytique est généralement de :",
                            'options': ["Calculer des aires", "Placer un repère et traduire les données en coordonnées", "Utiliser le théorème de Thalès", "Tracer les médiatrices"],
                            'reponse_correcte': '1',
                            'explication': "On commence par placer un repère, traduire en coordonnées, calculer, puis interpréter géométriquement.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Pour montrer qu'un quadrilatère $ABCD$ est un parallélogramme, on vérifie que :",
                            'options': ["Les 4 côtés sont égaux", "$\\\\overrightarrow{AB} = \\\\overrightarrow{DC}$", "Les diagonales sont perpendiculaires", "Tous les angles sont droits"],
                            'reponse_correcte': '1',
                            'explication': "Deux vecteurs côtés opposés égaux caractérisent un parallélogramme.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Le centre du cercle circonscrit à un triangle se trouve à l'intersection :",
                            'options': ["Des médianes", "Des hauteurs", "Des médiatrices", "Des bissectrices"],
                            'reponse_correcte': '2',
                            'explication': "Le centre du cercle circonscrit est le point équidistant des trois sommets, intersection des médiatrices.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "$\\\\overrightarrow{MA} \\\\cdot \\\\overrightarrow{MB} = 0$ signifie que le point $M$ est sur :",
                            'options': ["La médiatrice de $[AB]$", "Le cercle de diamètre $[AB]$", "La droite $(AB)$", "Le milieu de $[AB]$"],
                            'reponse_correcte': '1',
                            'explication': "$\\overrightarrow{MA} \\cdot \\overrightarrow{MB} = 0$ signifie que l'angle $\\widehat{AMB} = 90°$, donc $M$ est sur le cercle de diamètre $[AB]$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Si $\\\\overrightarrow{AB} = \\\\overrightarrow{DC}$, alors $ABCD$ est :",
                            'options': ["Un rectangle", "Un losange", "Un parallélogramme", "Un trapèze"],
                            'reponse_correcte': '2',
                            'explication': "L'égalité de deux vecteurs côtés opposés est la définition du parallélogramme.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Pour prouver qu'un parallélogramme est un rectangle, on montre que :",
                            'options': ["Ses diagonales sont perpendiculaires", "Deux côtés consécutifs sont perpendiculaires", "Ses 4 côtés sont égaux", "Ses diagonales sont de même longueur uniquement"],
                            'reponse_correcte': '1',
                            'explication': "Un parallélogramme ayant un angle droit (côtés consécutifs orthogonaux) est un rectangle.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "$A(1;2)$, $B(4;6)$, $C(8;3)$, $D(5;-1)$. $\\\\overrightarrow{AB}(3;4)$ et $\\\\overrightarrow{DC}(3;4)$. $ABCD$ est :",
                            'options': ["Un trapèze", "Un parallélogramme", "Un losange", "On ne peut pas conclure"],
                            'reponse_correcte': '1',
                            'explication': "$\\overrightarrow{AB} = \\overrightarrow{DC}$, donc $ABCD$ est un parallélogramme.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "La médiatrice d'un segment $[AB]$ est l'ensemble des points :",
                            'options': ["Équidistants de $A$ et $B$", "Situés sur la droite $(AB)$", "Tels que $\\\\overrightarrow{MA} \\\\cdot \\\\overrightarrow{MB} = 0$", "Situés au milieu du segment"],
                            'reponse_correcte': '0',
                            'explication': "La médiatrice est l'ensemble des points $M$ tels que $MA = MB$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "$A(0;0)$ et $B(6;0)$. La médiatrice de $[AB]$ a pour équation :",
                            'options': ["$y = 0$", "$x = 3$", "$y = 3$", "$x = 6$"],
                            'reponse_correcte': '1',
                            'explication': "Le milieu de $[AB]$ est $(3;0)$ et $\\overrightarrow{AB}(6;0)$ est horizontal. La médiatrice est la verticale $x = 3$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "L'ensemble des points $M$ tels que $MA^2 - MB^2 = k$ ($A$, $B$ fixés, $k$ constante) est :",
                            'options': ["Un cercle", "Une droite perpendiculaire à $(AB)$", "Une parabole", "Un segment"],
                            'reponse_correcte': '1',
                            'explication': "En développant, les termes $x^2$ et $y^2$ se simplifient, et il reste une équation du premier degré.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "$A(1;0)$, $B(3;0)$. L'ensemble des $M(x;y)$ tels que $MA^2 - MB^2 = 8$ est la droite :",
                            'options': ["$x = 4$", "$x = 2$", "$y = 4$", "$x = -4$"],
                            'reponse_correcte': '0',
                            'explication': "$MA^2 - MB^2 = 4x - 8 = 8 \\iff x = 4$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "$A(1;2)$, $B(4;6)$, $\\\\overrightarrow{AD}(4;-3)$. On a $\\\\overrightarrow{AB} \\\\cdot \\\\overrightarrow{AD} = 0$. Que peut-on en déduire ?",
                            'options': ["L'angle en $A$ est droit", "$AB$ et $AD$ sont parallèles", "$ABCD$ est un losange", "On ne peut rien conclure"],
                            'reponse_correcte': '0',
                            'explication': "Le produit scalaire nul entre deux côtés consécutifs signifie que l'angle en $A$ est droit.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Le cercle circonscrit au triangle rectangle $A(0;0)$, $B(6;0)$, $C(0;8)$ a pour centre :",
                            'options': ["$(3 ; 4)$", "$(2 ; 3)$", "$(0 ; 0)$", "$(3 ; 0)$"],
                            'reponse_correcte': '0',
                            'explication': "Triangle rectangle en $A$, le centre est le milieu de l'hypoténuse $[BC]$ : $\\left(\\frac{6}{2};\\frac{8}{2}\\right) = (3;4)$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Si $ABCD$ est un parallélogramme et $AB = AD$, alors c'est un losange.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Un parallélogramme ayant deux côtés consécutifs égaux est un losange.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Le milieu de $[AB]$ avec $A(x_A ; y_A)$ et $B(x_B ; y_B)$ a pour coordonnées $\\\\left(\\\\frac{x_A + x_B}{2} ; \\\\frac{y_A + y_B}{2}\\\\right)$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est la formule classique du milieu d'un segment.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Pour prouver qu'un quadrilatère est un carré, il suffit de montrer que c'est un parallélogramme à diagonales perpendiculaires.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Cela prouve seulement que c'est un losange. Pour un carré, il faut en plus un angle droit (ou des diagonales de même longueur).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Calculer $AB$ avec $A(1 ; 2)$ et $B(4 ; 6)$.",
                            'options': None,
                            'reponse_correcte': '5',
                            'tolerances': ['5,0', '5.0'],
                            'explication': "$AB = \\sqrt{(4-1)^2 + (6-2)^2} = \\sqrt{9+16} = 5$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Donner les coordonnées du milieu de $[AC]$ avec $A(2 ; 4)$ et $C(6 ; 0)$ sous la forme $(a ; b)$.",
                            'options': None,
                            'reponse_correcte': '(4 ; 2)',
                            'tolerances': ['(4;2)', '(4 ; 2)', '4 ; 2', '4;2'],
                            'explication': "Milieu : $\\left(\\frac{2+6}{2} ; \\frac{4+0}{2}\\right) = (4 ; 2)$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Donner l'équation du cercle de diamètre $[AB]$ avec $A(0;0)$ et $B(4;0)$ sous la forme $(x-a)^2 + (y-b)^2 = r^2$.",
                            'options': None,
                            'reponse_correcte': '(x - 2)^2 + y^2 = 4',
                            'tolerances': ['(x-2)^2+y^2=4', '(x-2)²+y²=4'],
                            'explication': "Centre $(2;0)$, rayon $2$. $(x-2)^2 + y^2 = 4$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Triangle $A(0;0)$, $B(6;0)$, $C(2;4)$. Le cercle circonscrit a pour centre $\\\\Omega(3;1)$. Donner son rayon sous forme simplifiée.",
                            'options': None,
                            'reponse_correcte': 'sqrt(10)',
                            'tolerances': ['√10', 'racine(10)', 'racine de 10'],
                            'explication': "$r = \\Omega A = \\sqrt{9 + 1} = \\sqrt{10}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 9 — Généralités sur les fonctions
    # ──────────────────────────────────────────────
    {
        'ordre': 9,
        'titre': 'Généralités sur les fonctions',
        'description': "Ensemble de définition, parité, monotonie, composition de fonctions et valeur absolue.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Ensemble de définition, parité et monotonie',
                'duree': 30,
                'contenu': """# Ensemble de définition, parité et monotonie

## Introduction

Avant d'étudier une fonction en détail (dérivation, limites…), il est essentiel de connaître ses **propriétés générales** : sur quel ensemble est-elle définie ? Présente-t-elle des symétries ? Comment varie-t-elle ? Ce chapitre pose les bases de l'analyse de fonctions en classe de Première.

---

## 1. Ensemble de définition

### Définition

L'**ensemble de définition** d'une fonction $f$, noté $D_f$, est l'ensemble de toutes les valeurs de $x$ pour lesquelles $f(x)$ existe.

> Autrement dit, $D_f = \\{x \\in \\mathbb{R} \\mid f(x) \\text{ est défini}\\}$.

### Cas classiques

| Expression | Condition d'existence | Ensemble de définition |
|------------|----------------------|-----------------------|
| $\\frac{1}{g(x)}$ | $g(x) \\neq 0$ | $\\mathbb{R} \\setminus \\{x \\mid g(x) = 0\\}$ |
| $\\sqrt{g(x)}$ | $g(x) \\geq 0$ | $\\{x \\mid g(x) \\geq 0\\}$ |
| $\\ln(g(x))$ | $g(x) > 0$ | $\\{x \\mid g(x) > 0\\}$ |

### Exemple

Soit $f(x) = \\frac{1}{x^2 - 4}$.

Le dénominateur s'annule lorsque $x^2 - 4 = 0$, soit $x = -2$ ou $x = 2$.

Donc $D_f = \\mathbb{R} \\setminus \\{-2 ; 2\\}$.

---

## 2. Image et antécédent

### Définitions

- L'**image** de $x$ par $f$ est le nombre $f(x)$.
- Un **antécédent** de $y$ par $f$ est tout nombre $x$ tel que $f(x) = y$.

> Un nombre peut avoir **zéro, un ou plusieurs antécédents**, mais chaque $x$ de $D_f$ a **exactement une image**.

### Exemple

Soit $f(x) = x^2$.

- L'image de $3$ est $f(3) = 9$.
- Les antécédents de $4$ sont $x = 2$ et $x = -2$ car $f(2) = f(-2) = 4$.
- Le nombre $-1$ n'a **aucun antécédent** car $x^2 \\geq 0$ pour tout $x$.

---

## 3. Courbe représentative

La **courbe représentative** de $f$, notée $\\mathcal{C}_f$, est l'ensemble des points $M(x ; f(x))$ pour $x \\in D_f$.

- Dire que $M(a ; b) \\in \\mathcal{C}_f$ signifie que $b = f(a)$.
- Lire l'image de $a$ revient à lire l'ordonnée du point d'abscisse $a$ sur $\\mathcal{C}_f$.
- Trouver les antécédents de $b$ revient à tracer la droite $y = b$ et lire les abscisses des points d'intersection.

---

## 4. Parité d'une fonction

### Prérequis

Pour étudier la parité, il faut d'abord que $D_f$ soit **symétrique par rapport à $0$** : pour tout $x \\in D_f$, on a aussi $-x \\in D_f$.

### Définitions

- $f$ est **paire** si pour tout $x \\in D_f$ : $f(-x) = f(x)$.
- $f$ est **impaire** si pour tout $x \\in D_f$ : $f(-x) = -f(x)$.

### Interprétation graphique

| Propriété | Symétrie de $\\mathcal{C}_f$ |
|-----------|-----------------------------|
| $f$ paire | Symétrie par rapport à l'**axe des ordonnées** $(Oy)$ |
| $f$ impaire | Symétrie par rapport à l'**origine** $O$ |

### Exemples

**Fonction paire :** $f(x) = x^2$

$f(-x) = (-x)^2 = x^2 = f(x)$ pour tout $x \\in \\mathbb{R}$.

La parabole est bien symétrique par rapport à l'axe $(Oy)$.

**Fonction impaire :** $g(x) = x^3$

$g(-x) = (-x)^3 = -x^3 = -g(x)$ pour tout $x \\in \\mathbb{R}$.

La courbe est symétrique par rapport à l'origine.

**Ni paire, ni impaire :** $h(x) = x^2 + x$

$h(-x) = x^2 - x \\neq h(x)$ et $h(-x) \\neq -h(x)$.

### Méthode : étudier la parité

1. Vérifier que $D_f$ est symétrique par rapport à $0$.
2. Calculer $f(-x)$.
3. Comparer $f(-x)$ avec $f(x)$ et $-f(x)$.

---

## 5. Monotonie

### Définitions

Soit $f$ définie sur un intervalle $I$ :

- $f$ est **croissante** sur $I$ si pour tous $x_1, x_2 \\in I$ : $x_1 < x_2 \\Rightarrow f(x_1) \\leq f(x_2)$.
- $f$ est **strictement croissante** sur $I$ si : $x_1 < x_2 \\Rightarrow f(x_1) < f(x_2)$.
- $f$ est **décroissante** sur $I$ si : $x_1 < x_2 \\Rightarrow f(x_1) \\geq f(x_2)$.
- $f$ est **strictement décroissante** sur $I$ si : $x_1 < x_2 \\Rightarrow f(x_1) > f(x_2)$.

> Une fonction croissante **conserve l'ordre**, une fonction décroissante **renverse l'ordre**.

### Tableau de variations

On résume la monotonie d'une fonction dans un **tableau de variations** :

- On indique les valeurs remarquables de $x$ (bornes, extremums).
- Des flèches montantes ($\\nearrow$) indiquent une croissance.
- Des flèches descendantes ($\\searrow$) indiquent une décroissance.

### Exemple

Soit $f(x) = x^2$ sur $\\mathbb{R}$.

- $f$ est **strictement décroissante** sur $]-\\infty ; 0]$.
- $f$ est **strictement croissante** sur $[0 ; +\\infty[$.
- Le **minimum** de $f$ est atteint en $x = 0$ et vaut $f(0) = 0$.

---

## 6. Extremum local

### Définition

- $f$ admet un **maximum local** en $a$ s'il existe un intervalle ouvert $I$ contenant $a$ tel que $f(x) \\leq f(a)$ pour tout $x \\in I \\cap D_f$.
- $f$ admet un **minimum local** en $a$ s'il existe un intervalle ouvert $I$ contenant $a$ tel que $f(x) \\geq f(a)$ pour tout $x \\in I \\cap D_f$.

> Un extremum local correspond à un « sommet » ou un « creux » de la courbe.

### Lien avec la monotonie

Si $f$ est croissante puis décroissante autour de $a$, alors $f$ admet un **maximum local** en $a$.

Si $f$ est décroissante puis croissante autour de $a$, alors $f$ admet un **minimum local** en $a$.

### Exemple

Soit $f(x) = -x^2 + 4x - 1$ sur $\\mathbb{R}$.

$f$ est croissante sur $]-\\infty ; 2]$ et décroissante sur $[2 ; +\\infty[$.

$f$ admet donc un **maximum local** (et global) en $x = 2$, avec $f(2) = -4 + 8 - 1 = 3$.

---

## À retenir

- L'ensemble de définition $D_f$ détermine les valeurs de $x$ pour lesquelles $f(x)$ est calculable.
- La **parité** (paire ou impaire) traduit une symétrie de la courbe.
- La **monotonie** décrit le sens de variation de la fonction sur un intervalle.
- Un **extremum local** est un maximum ou minimum atteint localement.
- Ces propriétés permettent de dresser un premier portrait de la fonction avant toute étude approfondie.
""",
                'quiz': {
                    'titre': "Quiz — Ensemble de définition, parité et monotonie",
                    'questions': [
                        # ── 8 QCM facile ──────────────────────────────
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quel est l'ensemble de définition de $f(x) = \\\\frac{1}{x - 3}$ ?",
                            'options': ["$\\\\mathbb{R}$", "$\\\\mathbb{R} \\\\setminus \\\\{3\\\\}$", "$\\\\mathbb{R} \\\\setminus \\\\{-3\\\\}$", "$]3 ; +\\\\infty[$"],
                            'reponse_correcte': '1',
                            'explication': "Le dénominateur s'annule pour $x = 3$, donc $D_f = \\mathbb{R} \\setminus \\{3\\}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quel est l'ensemble de définition de $g(x) = \\\\sqrt{x - 2}$ ?",
                            'options': ["$\\\\mathbb{R}$", "$]-\\\\infty ; 2]$", "$[2 ; +\\\\infty[$", "$]2 ; +\\\\infty[$"],
                            'reponse_correcte': '2',
                            'explication': "Il faut $x - 2 \\geq 0$, soit $x \\geq 2$, donc $D_g = [2 ; +\\infty[$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "La fonction $f(x) = x^2$ est :",
                            'options': ["Paire", "Impaire", "Ni paire ni impaire", "Paire et impaire"],
                            'reponse_correcte': '0',
                            'explication': "$f(-x) = (-x)^2 = x^2 = f(x)$ pour tout $x$. La fonction est paire.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "La fonction $g(x) = x^3$ est :",
                            'options': ["Paire", "Impaire", "Ni paire ni impaire", "Constante"],
                            'reponse_correcte': '1',
                            'explication': "$g(-x) = (-x)^3 = -x^3 = -g(x)$. La fonction est impaire.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Si $f$ est paire, sa courbe admet une symétrie par rapport :",
                            'options': ["À l'axe des abscisses", "À l'axe des ordonnées", "À l'origine $O$", "À la droite $y = x$"],
                            'reponse_correcte': '1',
                            'explication': "Une fonction paire vérifie $f(-x) = f(x)$, ce qui correspond à une symétrie par rapport à l'axe $(Oy)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Dire que $f$ est strictement croissante sur $I$ signifie :",
                            'options': [
                                "Pour tous $x_1 < x_2$ dans $I$, $f(x_1) < f(x_2)$",
                                "Pour tous $x_1 < x_2$ dans $I$, $f(x_1) > f(x_2)$",
                                "Pour tous $x_1 < x_2$ dans $I$, $f(x_1) = f(x_2)$",
                                "La courbe est une droite ascendante",
                            ],
                            'reponse_correcte': '0',
                            'explication': "Strictement croissante signifie que l'ordre est strictement conservé : $x_1 < x_2 \\Rightarrow f(x_1) < f(x_2)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "La fonction $f(x) = x^2$ est strictement décroissante sur :",
                            'options': ["$\\\\mathbb{R}$", "$[0 ; +\\\\infty[$", "$]-\\\\infty ; 0]$", "$[-1 ; 1]$"],
                            'reponse_correcte': '2',
                            'explication': "La fonction carré est strictement décroissante sur $]-\\infty ; 0]$ et strictement croissante sur $[0 ; +\\infty[$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "L'image de $-3$ par la fonction $f(x) = x^2 + 1$ est :",
                            'options': ["$-8$", "$8$", "$10$", "$-10$"],
                            'reponse_correcte': '2',
                            'explication': "$f(-3) = (-3)^2 + 1 = 9 + 1 = 10$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        # ── 6 QCM moyen ───────────────────────────────
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Quel est l'ensemble de définition de $h(x) = \\\\frac{\\\\sqrt{x}}{x^2 - 1}$ ?",
                            'options': [
                                "$[0 ; +\\\\infty[$",
                                "$[0 ; +\\\\infty[ \\\\setminus \\\\{1\\\\}$",
                                "$\\\\mathbb{R} \\\\setminus \\\\{-1 ; 1\\\\}$",
                                "$]0 ; +\\\\infty[ \\\\setminus \\\\{1\\\\}$",
                            ],
                            'reponse_correcte': '1',
                            'explication': "Il faut $x \\geq 0$ (racine) et $x^2 - 1 \\neq 0$ (dénominateur), soit $x \\neq \\pm 1$. Comme $x \\geq 0$, seul $x = 1$ est exclu.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "La fonction $f(x) = x^2 + x$ est :",
                            'options': ["Paire", "Impaire", "Ni paire ni impaire", "Paire et impaire"],
                            'reponse_correcte': '2',
                            'explication': "$f(-x) = x^2 - x$. On a $f(-x) \\neq f(x)$ et $f(-x) \\neq -f(x)$, donc $f$ n'est ni paire ni impaire.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Soit $f(x) = \\\\frac{x}{x^2 + 1}$. Quelle est la parité de $f$ ?",
                            'options': ["Paire", "Impaire", "Ni paire ni impaire", "On ne peut pas conclure"],
                            'reponse_correcte': '1',
                            'explication': "$f(-x) = \\frac{-x}{(-x)^2 + 1} = \\frac{-x}{x^2 + 1} = -f(x)$. La fonction est impaire.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Soit $f$ définie sur $\\\\mathbb{R}$ avec le tableau de variations : $f$ décroissante sur $]-\\\\infty ; 1]$ et croissante sur $[1 ; +\\\\infty[$. Quel est l'extremum en $x = 1$ ?",
                            'options': ["Maximum local", "Minimum local", "Point d'inflexion", "Aucun extremum"],
                            'reponse_correcte': '1',
                            'explication': "Si $f$ est décroissante puis croissante autour de $a$, alors $f$ admet un minimum local en $a$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Quel est l'ensemble de définition de $f(x) = \\\\ln(4 - x^2)$ ?",
                            'options': ["$]-2 ; 2[$", "$[-2 ; 2]$", "$\\\\mathbb{R} \\\\setminus \\\\{-2 ; 2\\\\}$", "$]0 ; 2[$"],
                            'reponse_correcte': '0',
                            'explication': "Il faut $4 - x^2 > 0$, soit $x^2 < 4$, c'est-à-dire $-2 < x < 2$. Donc $D_f = ]-2 ; 2[$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Soit $f(x) = -x^2 + 4x - 1$. Sur quel intervalle $f$ est-elle croissante ?",
                            'options': ["$]-\\\\infty ; 2]$", "$[2 ; +\\\\infty[$", "$]-\\\\infty ; -2]$", "$\\\\mathbb{R}$"],
                            'reponse_correcte': '0',
                            'explication': "Le sommet est en $x = -\\frac{4}{2 \\times (-1)} = 2$. Comme $a < 0$, $f$ est croissante sur $]-\\infty ; 2]$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        # ── 3 Vrai/Faux moyen ────────────────────────
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Pour étudier la parité d'une fonction, il faut d'abord vérifier que son ensemble de définition est symétrique par rapport à 0.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est un prérequis indispensable : $D_f$ doit être symétrique par rapport à $0$ avant de comparer $f(-x)$ et $f(x)$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Un nombre réel possède toujours exactement un antécédent par une fonction $f$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Un nombre peut avoir zéro, un ou plusieurs antécédents. Par exemple, $4$ a deux antécédents par $f(x) = x^2$ : $2$ et $-2$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Une fonction strictement croissante sur $\\\\mathbb{R}$ ne peut pas admettre de maximum local.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Si $f$ est strictement croissante sur $\\mathbb{R}$, elle augmente toujours : elle ne peut pas atteindre de maximum local.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        # ── 3 Texte libre difficile ───────────────────
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Déterminer l'ensemble de définition de $f(x) = \\\\frac{1}{x^2 - 4}$. Donner la réponse sous la forme R\\\\{a ; b} avec a < b.",
                            'options': None,
                            'reponse_correcte': 'R\\{-2 ; 2}',
                            'tolerances': ["R\\\\{-2 ; 2}", "R\\{-2;2}", "R \\ {-2 ; 2}", "ℝ\\{-2 ; 2}"],
                            'explication': "$x^2 - 4 = 0 \\Leftrightarrow x = -2$ ou $x = 2$. Donc $D_f = \\mathbb{R} \\setminus \\{-2 ; 2\\}$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Soit $f(x) = \\\\frac{x^3}{x^2 + 1}$. Calculer $f(-x)$ et indiquer si la fonction est paire, impaire, ou ni l'un ni l'autre.",
                            'options': None,
                            'reponse_correcte': 'impaire',
                            'tolerances': ["Impaire", "IMPAIRE", "f est impaire"],
                            'explication': "$f(-x) = \\frac{(-x)^3}{(-x)^2 + 1} = \\frac{-x^3}{x^2 + 1} = -f(x)$. La fonction est impaire.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Soit $f(x) = -x^2 + 6x - 5$. Donner la valeur du maximum de $f$ (nombre entier).",
                            'options': None,
                            'reponse_correcte': '4',
                            'tolerances': ["4.0", "4,0"],
                            'explication': "Le sommet est en $x = -\\frac{6}{2 \\times (-1)} = 3$. $f(3) = -9 + 18 - 5 = 4$. Comme $a < 0$, c'est un maximum.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Composition et valeur absolue',
                'duree': 30,
                'contenu': """# Composition de fonctions et valeur absolue

## Introduction

La **composition de fonctions** est une opération fondamentale qui permet de construire de nouvelles fonctions à partir de fonctions connues. La **valeur absolue**, quant à elle, est un outil algébrique et géométrique incontournable. Ce cours couvre ces deux notions au programme de Première.

---

## 1. Composition de fonctions

### Définition

Soient deux fonctions $f$ et $g$. La **composée** de $f$ par $g$, notée $g \\circ f$ (lire « $g$ rond $f$ »), est la fonction définie par :

$$(g \\circ f)(x) = g\\big(f(x)\\big)$$

L'ordre est important : on applique **d'abord** $f$, **puis** $g$.

> **Attention :** en général, $g \\circ f \\neq f \\circ g$.

### Ensemble de définition de la composée

$g \\circ f$ est définie pour les $x \\in D_f$ tels que $f(x) \\in D_g$.

### Exemple

Soient $f(x) = 2x + 1$ et $g(x) = x^2$.

$$(g \\circ f)(x) = g(f(x)) = g(2x + 1) = (2x + 1)^2$$

$$(f \\circ g)(x) = f(g(x)) = f(x^2) = 2x^2 + 1$$

On vérifie que $g \\circ f \\neq f \\circ g$ : pour $x = 1$, $(g \\circ f)(1) = 9$ tandis que $(f \\circ g)(1) = 3$.

---

## 2. Sens de variation d'une composée

C'est un résultat essentiel pour l'étude de fonctions :

### Théorème

| Variations de $f$ | Variations de $g$ | Variations de $g \\circ f$ |
|---|---|---|
| Croissante ($\\nearrow$) | Croissante ($\\nearrow$) | **Croissante** ($\\nearrow$) |
| Croissante ($\\nearrow$) | Décroissante ($\\searrow$) | **Décroissante** ($\\searrow$) |
| Décroissante ($\\searrow$) | Croissante ($\\nearrow$) | **Décroissante** ($\\searrow$) |
| Décroissante ($\\searrow$) | Décroissante ($\\searrow$) | **Croissante** ($\\nearrow$) |

> **Règle mnémotechnique :** même sens → croissante ; sens contraires → décroissante. C'est la **règle des signes** appliquée aux variations.

### Exemple

Soit $h(x) = (2x - 3)^2$.

On décompose : $h = g \\circ f$ avec $f(x) = 2x - 3$ (affine, croissante) et $g(t) = t^2$.

- $g$ est décroissante sur $]-\\infty ; 0]$ et croissante sur $[0 ; +\\infty[$.
- $f(x) = 0 \\Leftrightarrow x = \\frac{3}{2}$.

Donc :
- Sur $\\left]-\\infty ; \\frac{3}{2}\\right]$ : $f$ croissante et $g$ décroissante → $h$ **décroissante**.
- Sur $\\left[\\frac{3}{2} ; +\\infty\\right[$ : $f$ croissante et $g$ croissante → $h$ **croissante**.

Le minimum de $h$ est atteint en $x = \\frac{3}{2}$ et vaut $h\\left(\\frac{3}{2}\\right) = 0$.

---

## 3. La fonction valeur absolue

### Définition

La **valeur absolue** d'un nombre réel $x$, notée $|x|$, est définie par :

$$|x| = \\begin{cases} x & \\text{si } x \\geq 0 \\\\ -x & \\text{si } x < 0 \\end{cases}$$

> $|x|$ représente la **distance** de $x$ à l'origine sur la droite des réels.

### Courbe représentative

La courbe de la fonction $x \\mapsto |x|$ a la forme d'un **V** pointant vers le haut, avec un sommet en $O(0 ; 0)$.

- Sur $]-\\infty ; 0]$ : la courbe est la droite $y = -x$ (pente $-1$).
- Sur $[0 ; +\\infty[$ : la courbe est la droite $y = x$ (pente $+1$).

La fonction valeur absolue est **paire** : $|-x| = |x|$ pour tout $x$, ce qui se traduit par la symétrie de la courbe par rapport à l'axe des ordonnées.

---

## 4. Propriétés de la valeur absolue

### Propriétés fondamentales

Pour tous réels $a$ et $b$ :

1. $|a| \\geq 0$ et $|a| = 0 \\Leftrightarrow a = 0$
2. $|-a| = |a|$
3. $|ab| = |a| \\cdot |b|$ (multiplicativité)
4. $\\left|\\frac{a}{b}\\right| = \\frac{|a|}{|b|}$ pour $b \\neq 0$
5. $|a|^2 = a^2$

### Inégalité triangulaire

Pour tous réels $a$ et $b$ :

$$|a + b| \\leq |a| + |b|$$

C'est l'une des inégalités les plus importantes en mathématiques. L'égalité a lieu si et seulement si $a$ et $b$ sont de **même signe** (ou l'un des deux est nul).

### Exemple

Avec $a = 3$ et $b = -5$ :

$|a + b| = |3 + (-5)| = |-2| = 2$

$|a| + |b| = 3 + 5 = 8$

On vérifie bien $2 \\leq 8$.

---

## 5. Résolution d'équations avec valeur absolue

### Équation $|X| = k$

- Si $k > 0$ : deux solutions, $X = k$ ou $X = -k$.
- Si $k = 0$ : une solution, $X = 0$.
- Si $k < 0$ : **aucune solution** (la valeur absolue est toujours positive).

### Exemple

Résoudre $|2x - 5| = 3$.

$$2x - 5 = 3 \\quad \\text{ou} \\quad 2x - 5 = -3$$
$$2x = 8 \\quad \\text{ou} \\quad 2x = 2$$
$$x = 4 \\quad \\text{ou} \\quad x = 1$$

L'ensemble des solutions est $S = \\{1 ; 4\\}$.

**Vérification :** $|2(4) - 5| = |3| = 3$ ✓ et $|2(1) - 5| = |-3| = 3$ ✓

---

## 6. Résolution d'inéquations avec valeur absolue

### Inéquation $|X| \\leq k$ (avec $k \\geq 0$)

$$|X| \\leq k \\iff -k \\leq X \\leq k$$

### Inéquation $|X| \\geq k$ (avec $k \\geq 0$)

$$|X| \\geq k \\iff X \\leq -k \\quad \\text{ou} \\quad X \\geq k$$

### Exemple

Résoudre $|x - 3| < 2$.

$$-2 < x - 3 < 2$$
$$1 < x < 5$$

L'ensemble des solutions est l'intervalle ouvert $]1 ; 5[$.

**Interprétation géométrique :** les réels dont la **distance à $3$** est strictement inférieure à $2$.

---

## 7. Interprétation géométrique de la valeur absolue

La valeur absolue a une signification géométrique très naturelle :

$$|a - b| = \\text{distance entre les points d'abscisses } a \\text{ et } b \\text{ sur la droite des réels}$$

Cette interprétation est très utile pour résoudre des inéquations :

- $|x - 3| < 2$ : les points à distance inférieure à $2$ du point $3$, soit $]1 ; 5[$.
- $|x + 1| \\geq 4$ : les points à distance supérieure ou égale à $4$ du point $-1$, soit $]-\\infty ; -5] \\cup [3 ; +\\infty[$.

### Exemple : encadrement avec la valeur absolue

Si $|x - 2| \\leq 0{,}5$, alors $1{,}5 \\leq x \\leq 2{,}5$.

Cela signifie que $x$ est une **approximation** de $2$ à $0{,}5$ près.

---

## À retenir

- La composée $g \\circ f$ s'obtient en appliquant $f$ puis $g$ : $(g \\circ f)(x) = g(f(x))$.
- Le sens de variation d'une composée suit la **règle des signes** : même sens → croissante, sens contraires → décroissante.
- La valeur absolue $|x|$ mesure la **distance à zéro** : $|x| \\geq 0$ et $|x| = 0 \\iff x = 0$.
- **Inégalité triangulaire** : $|a + b| \\leq |a| + |b|$.
- $|X| = k$ donne deux solutions (si $k > 0$), $|X| \\leq k$ donne un intervalle $[-k ; k]$.
- $|a - b|$ est la distance entre $a$ et $b$ sur la droite réelle.
""",
                'quiz': {
                    'titre': "Quiz — Composition de fonctions et valeur absolue",
                    'questions': [
                        # ── 8 QCM facile ──────────────────────────────
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Que signifie $(g \\\\circ f)(x)$ ?",
                            'options': ["$f(g(x))$", "$g(f(x))$", "$f(x) \\\\times g(x)$", "$f(x) + g(x)$"],
                            'reponse_correcte': '1',
                            'explication': "$(g \\circ f)(x) = g(f(x))$ : on applique d'abord $f$, puis $g$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quelle est la valeur de $|-7|$ ?",
                            'options': ["$-7$", "$7$", "$0$", "$49$"],
                            'reponse_correcte': '1',
                            'explication': "$|-7| = 7$ car la valeur absolue donne la distance à zéro, toujours positive.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Soient $f(x) = x + 2$ et $g(x) = 3x$. Que vaut $(g \\\\circ f)(1)$ ?",
                            'options': ["$5$", "$7$", "$9$", "$6$"],
                            'reponse_correcte': '2',
                            'explication': "$f(1) = 3$, puis $g(3) = 9$. Donc $(g \\circ f)(1) = 9$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "L'équation $|x| = 5$ admet :",
                            'options': ["Aucune solution", "Une solution", "Deux solutions", "Une infinité de solutions"],
                            'reponse_correcte': '2',
                            'explication': "$|x| = 5 \\Leftrightarrow x = 5$ ou $x = -5$. Il y a deux solutions.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Que représente $|a - b|$ géométriquement ?",
                            'options': [
                                "La somme de $a$ et $b$",
                                "Le produit de $a$ et $b$",
                                "La distance entre $a$ et $b$ sur la droite réelle",
                                "La moyenne de $a$ et $b$",
                            ],
                            'reponse_correcte': '2',
                            'explication': "$|a - b|$ mesure la distance entre les points d'abscisses $a$ et $b$ sur la droite des réels.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "L'équation $|x| = -3$ admet :",
                            'options': ["Aucune solution", "Une solution", "Deux solutions", "Une infinité de solutions"],
                            'reponse_correcte': '0',
                            'explication': "La valeur absolue est toujours positive ou nulle, donc $|x| = -3$ n'a aucune solution.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "La fonction valeur absolue $x \\\\mapsto |x|$ est :",
                            'options': ["Paire", "Impaire", "Ni paire ni impaire", "Constante"],
                            'reponse_correcte': '0',
                            'explication': "$|-x| = |x|$ pour tout $x$, donc la fonction valeur absolue est paire.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Soient $f(x) = x^2$ et $g(x) = x + 1$. Que vaut $(f \\\\circ g)(x)$ ?",
                            'options': ["$x^2 + 1$", "$(x + 1)^2$", "$x^2 + x$", "$x^2 + 2x$"],
                            'reponse_correcte': '1',
                            'explication': "$(f \\circ g)(x) = f(g(x)) = f(x + 1) = (x + 1)^2$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        # ── 6 QCM moyen ───────────────────────────────
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Si $f$ est croissante et $g$ est décroissante, alors $g \\\\circ f$ est :",
                            'options': ["Croissante", "Décroissante", "Constante", "On ne peut pas conclure"],
                            'reponse_correcte': '1',
                            'explication': "Croissante $\\circ$ Décroissante (sens contraires) $\\Rightarrow$ la composée est décroissante.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Résoudre $|2x - 1| = 5$. L'ensemble des solutions est :",
                            'options': ["$\\\\{3\\\\}$", "$\\\\{-2 ; 3\\\\}$", "$\\\\{-3 ; 2\\\\}$", "$\\\\{-2 ; -3\\\\}$"],
                            'reponse_correcte': '1',
                            'explication': "$2x - 1 = 5 \\Rightarrow x = 3$ ou $2x - 1 = -5 \\Rightarrow x = -2$. Donc $S = \\{-2 ; 3\\}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "L'inéquation $|x - 4| < 3$ a pour ensemble de solutions :",
                            'options': ["$]1 ; 7[$", "$[-1 ; 7]$", "$]4 ; 7[$", "$]-3 ; 3[$"],
                            'reponse_correcte': '0',
                            'explication': "$|x - 4| < 3 \\Leftrightarrow -3 < x - 4 < 3 \\Leftrightarrow 1 < x < 7$. Donc $S = ]1 ; 7[$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Soient $f(x) = 2x - 3$ et $g(x) = x^2$. Quelle est l'expression de $(g \\\\circ f)(x)$ ?",
                            'options': ["$4x^2 - 12x + 9$", "$2x^2 - 3$", "$4x^2 - 9$", "$4x^2 + 12x + 9$"],
                            'reponse_correcte': '0',
                            'explication': "$(g \\circ f)(x) = (2x - 3)^2 = 4x^2 - 12x + 9$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Laquelle de ces propriétés est l'inégalité triangulaire ?",
                            'options': [
                                "$|a \\\\cdot b| = |a| \\\\cdot |b|$",
                                "$|a + b| \\\\leq |a| + |b|$",
                                "$|a - b| = |b - a|$",
                                "$|a|^2 = a^2$",
                            ],
                            'reponse_correcte': '1',
                            'explication': "L'inégalité triangulaire s'écrit $|a + b| \\leq |a| + |b|$ pour tous réels $a$ et $b$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Soit $h(x) = (3x + 1)^2$. On pose $f(x) = 3x + 1$ et $g(t) = t^2$. Quel est le minimum de $h$ ?",
                            'options': ["$h(-\\\\frac{1}{3}) = 0$", "$h(0) = 1$", "$h(1) = 16$", "$h(-1) = 4$"],
                            'reponse_correcte': '0',
                            'explication': "$f(x) = 0 \\Leftrightarrow x = -\\frac{1}{3}$. Le minimum de $g(t) = t^2$ est $0$ en $t = 0$, donc $h\\left(-\\frac{1}{3}\\right) = 0$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        # ── 3 Vrai/Faux moyen ────────────────────────
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "En général, la composition de fonctions est commutative : $g \\\\circ f = f \\\\circ g$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "En général $g \\circ f \\neq f \\circ g$. Par exemple, avec $f(x) = x + 1$ et $g(x) = x^2$ : $(g \\circ f)(x) = (x+1)^2$ mais $(f \\circ g)(x) = x^2 + 1$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Si $|x - 2| \\\\leq 0{,}1$, alors $1{,}9 \\\\leq x \\\\leq 2{,}1$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$|x - 2| \\leq 0{,}1 \\Leftrightarrow -0{,}1 \\leq x - 2 \\leq 0{,}1 \\Leftrightarrow 1{,}9 \\leq x \\leq 2{,}1$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Si $f$ est décroissante et $g$ est décroissante, alors $g \\\\circ f$ est décroissante.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Décroissante composée avec décroissante donne une fonction croissante (règle des signes : $(-) \\times (-) = (+)$).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        # ── 3 Texte libre difficile ───────────────────
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Résoudre $|3x - 6| = 12$. Donner l'ensemble des solutions sous la forme {a ; b} avec a < b.",
                            'options': None,
                            'reponse_correcte': '{-2 ; 6}',
                            'tolerances': ["{-2;6}", "{-2 ; 6}", "{ -2 ; 6 }"],
                            'explication': "$3x - 6 = 12 \\Rightarrow x = 6$ ou $3x - 6 = -12 \\Rightarrow x = -2$. Donc $S = \\{-2 ; 6\\}$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Résoudre $|x + 1| \\\\leq 3$. Donner la solution sous la forme [a ; b].",
                            'options': None,
                            'reponse_correcte': '[-4 ; 2]',
                            'tolerances': ["[-4;2]", "[-4 ; 2]", "[ -4 ; 2 ]"],
                            'explication': "$|x + 1| \\leq 3 \\Leftrightarrow -3 \\leq x + 1 \\leq 3 \\Leftrightarrow -4 \\leq x \\leq 2$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Soient $f(x) = 2x + 3$ et $g(x) = x^2 - 1$. Calculer $(g \\\\circ f)(0)$.",
                            'options': None,
                            'reponse_correcte': '8',
                            'tolerances': ["8.0", "8,0"],
                            'explication': "$f(0) = 3$, puis $g(3) = 9 - 1 = 8$. Donc $(g \\circ f)(0) = 8$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Seed Mathématiques Première — chapitres 1 à 9, leçons (sans quiz)."

    def handle(self, *args, **options):
        matiere, created = Matiere.objects.get_or_create(
            nom='mathematiques',
            defaults={
                'description': "Les mathématiques au lycée : algèbre, analyse, géométrie, probabilités et algorithmique.",
            },
        )
        if created:
            self.stdout.write(f"  ✔ Matière « {matiere} » créée")
        else:
            self.stdout.write(f"  … Matière « {matiere} » existante")

        total_lecons = 0
        total_quizzes = 0

        for chap_data in CHAPITRES:
            chapitre, ch_created = Chapitre.objects.update_or_create(
                matiere=matiere,
                niveau='premiere',
                ordre=chap_data['ordre'],
                defaults={
                    'titre': chap_data['titre'],
                    'slug': slugify(chap_data['titre']),
                    'description': chap_data['description'],
                    'score_minimum_deblocage': chap_data['score_minimum'],
                },
            )
            status = "créé" if ch_created else "mis à jour"
            self.stdout.write(f"  {'✔' if ch_created else '…'} Ch.{chap_data['ordre']} — {chap_data['titre']} ({status})")

            for lecon_data in chap_data['lecons']:
                lecon, lec_created = Lecon.objects.update_or_create(
                    chapitre=chapitre,
                    ordre=lecon_data['ordre'],
                    defaults={
                        'titre': lecon_data['titre'],
                        'slug': slugify(lecon_data['titre']),
                        'duree_estimee': lecon_data['duree'],
                        'contenu': lecon_data['contenu'],
                    },
                )
                total_lecons += 1
                status = "créée" if lec_created else "mise à jour"
                self.stdout.write(f"      L{lecon_data['ordre']} — {lecon_data['titre']} ({status})")

                if 'quiz' in lecon_data:
                    qdata = lecon_data['quiz']
                    quiz, _ = Quiz.objects.update_or_create(
                        lecon=lecon,
                        defaults={
                            'titre': qdata['titre'],
                            'score_minimum': qdata.get('score_minimum', 60.0),
                        },
                    )
                    for q in qdata['questions']:
                        Question.objects.update_or_create(
                            quiz=quiz,
                            ordre=q['ordre'],
                            defaults={
                                'texte': q['texte'],
                                'type': q.get('type', 'qcm'),
                                'options': q.get('options'),
                                'reponse_correcte': str(q['reponse_correcte']),
                                'tolerances': q.get('tolerances'),
                                'explication': q.get('explication', ''),
                                'difficulte': q.get('difficulte', 'moyen'),
                                'points': q.get('points', 1),
                            },
                        )
                    total_quizzes += 1

        self.stdout.write(self.style.SUCCESS(
            f"\n✅ Mathématiques Première — {len(CHAPITRES)} chapitres, {total_lecons} leçons, {total_quizzes} quiz traités."
        ))
