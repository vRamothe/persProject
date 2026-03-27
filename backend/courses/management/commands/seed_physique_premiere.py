"""
Seed Physique Première — 9 chapitres, leçons uniquement (sans quiz).
Usage : python manage.py seed_physique_premiere
"""

from django.core.management.base import BaseCommand
from courses.models import Matiere, Chapitre, Lecon, Quiz, Question

CHAPITRES = [
    # ──────────────────────────────────────────────
    # CHAPITRE 1 — Interactions et champs
    # ──────────────────────────────────────────────
    {
        'ordre': 1,
        'titre': 'Interactions et champs',
        'description': "Comprendre les interactions fondamentales et la notion de champ en physique.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Les interactions fondamentales',
                'duree': 35,
                'contenu': """# Les interactions fondamentales

## Introduction

En physique, toute action d'un objet sur un autre est modélisée par une **force**. Ces forces trouvent leur origine dans quatre interactions fondamentales.

---

## Les quatre interactions fondamentales

| Interaction | Portée | Intensité relative | Particules concernées |
|---|---|---|---|
| **Gravitationnelle** | Infinie | $10^{-39}$ | Toute masse |
| **Électromagnétique** | Infinie | $10^{-2}$ | Charges électriques |
| **Nucléaire forte** | $\\approx 10^{-15}$ m | $1$ | Quarks, nucléons |
| **Nucléaire faible** | $\\approx 10^{-18}$ m | $10^{-5}$ | Toutes les particules |

---

## Interaction gravitationnelle

Deux corps de masses $m_A$ et $m_B$, séparés par une distance $d$, exercent l'un sur l'autre une force d'attraction :

$$
F = G \\frac{m_A \\cdot m_B}{d^2}
$$

avec $G = 6{,}674 \\times 10^{-11}$ N·m²·kg⁻².

### Caractéristiques

- Toujours **attractive**
- Proportionnelle au produit des masses
- Inversement proportionnelle au carré de la distance

---

## Interaction électromagnétique

### Loi de Coulomb

Deux charges ponctuelles $q_A$ et $q_B$ séparées par une distance $d$ :

$$
F = k \\frac{|q_A| \\cdot |q_B|}{d^2}
$$

avec $k = 8{,}99 \\times 10^9$ N·m²·C⁻².

### Caractéristiques

- **Attractive** si les charges sont de signes opposés
- **Répulsive** si les charges sont de même signe
- Beaucoup plus intense que la gravitation à l'échelle atomique

---

## Interactions nucléaires

- **Interaction forte** : assure la cohésion du noyau (lie les nucléons entre eux malgré la répulsion entre protons)
- **Interaction faible** : responsable de certaines désintégrations radioactives (radioactivité $\\beta$)

---

## Bilan

À notre échelle, seules les interactions **gravitationnelle** et **électromagnétique** ont des effets observables. Les interactions nucléaires n'agissent qu'à l'échelle du noyau.

---
""",
                'quiz': {
                    'titre': 'Quiz — Les interactions fondamentales',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Combien existe-t-il d'interactions fondamentales en physique ?", 'options': ["4", "2", "3", "6"], 'reponse_correcte': '0', 'explication': "Il existe quatre interactions fondamentales : gravitationnelle, électromagnétique, nucléaire forte et nucléaire faible.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "L'interaction gravitationnelle est toujours :", 'options': ["Attractive", "Répulsive", "Nulle", "Variable selon les masses"], 'reponse_correcte': '0', 'explication': "La gravitation est toujours attractive.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Quelle est l'unité de la force dans le Système International ?", 'options': ["Le newton (N)", "Le joule (J)", "Le watt (W)", "Le pascal (Pa)"], 'reponse_correcte': '0', 'explication': "La force se mesure en newtons.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "La constante de gravitation universelle est notée :", 'options': ["G", "g", "k", "F"], 'reponse_correcte': '0', 'explication': "La constante de gravitation universelle est notée $G$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "L'interaction électromagnétique concerne :", 'options': ["Les charges électriques", "Toute masse", "Les neutrons uniquement", "Les photons uniquement"], 'reponse_correcte': '0', 'explication': "L'interaction électromagnétique agit entre les charges électriques.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "L'interaction nucléaire forte assure :", 'options': ["La cohésion du noyau", "La gravité terrestre", "Le magnétisme", "La radioactivité β"], 'reponse_correcte': '0', 'explication': "L'interaction forte lie les nucléons au sein du noyau.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "La portée de l'interaction gravitationnelle est :", 'options': ["Infinie", "10⁻¹⁵ m", "10⁻¹⁸ m", "1 m"], 'reponse_correcte': '0', 'explication': "La gravitation a une portée infinie.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "La loi de Coulomb décrit l'interaction :", 'options': ["Électrostatique", "Gravitationnelle", "Nucléaire forte", "Nucléaire faible"], 'reponse_correcte': '0', 'explication': "La loi de Coulomb régit l'interaction entre charges électriques.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "La force gravitationnelle entre deux masses est proportionnelle à :", 'options': ["Le produit des masses", "La somme des masses", "La différence des masses", "Le carré des masses"], 'reponse_correcte': '0', 'explication': "$F = G \\cdot m_A \\cdot m_B / d^2$ : proportionnelle au produit des masses.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "La constante $k$ dans la loi de Coulomb vaut environ :", 'options': ["9 × 10⁹ N·m²·C⁻²", "6,67 × 10⁻¹¹ N·m²·kg⁻²", "3 × 10⁸ m·s⁻¹", "1,6 × 10⁻¹⁹ C"], 'reponse_correcte': '0', 'explication': "$k \\approx 8{,}99 \\times 10^9$ N·m²·C⁻².", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Si la distance entre deux charges double, la force électrostatique est :", 'options': ["Divisée par 4", "Divisée par 2", "Multipliée par 2", "Multipliée par 4"], 'reponse_correcte': '0', 'explication': "La force varie en $1/d^2$ : si $d$ double, $F$ est divisée par 4.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Deux charges de même signe exercent l'une sur l'autre une force :", 'options': ["Répulsive", "Attractive", "Nulle", "Alternée"], 'reponse_correcte': '0', 'explication': "Des charges de même signe se repoussent.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "L'interaction nucléaire faible est responsable de :", 'options': ["La radioactivité β", "La cohésion du noyau", "La gravité", "Le magnétisme"], 'reponse_correcte': '0', 'explication': "La radioactivité β est due à l'interaction faible.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "À l'échelle atomique, quelle interaction domine entre un proton et un électron ?", 'options': ["Électromagnétique", "Gravitationnelle", "Nucléaire faible", "Nucléaire forte"], 'reponse_correcte': '0', 'explication': "L'interaction électromagnétique est bien plus intense que la gravitation à l'échelle atomique.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "La force gravitationnelle peut être répulsive.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "La gravitation est toujours attractive.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "La force électrostatique varie en $1/d^2$.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "La loi de Coulomb montre que $F \\propto 1/d^2$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "L'interaction nucléaire forte a une portée infinie.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "L'interaction forte a une portée de l'ordre de $10^{-15}$ m.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner l'expression littérale de la force gravitationnelle entre deux masses $m_A$ et $m_B$ séparées par une distance $d$.", 'reponse_correcte': "F = G × mA × mB / d²", 'tolerances': ["G*mA*mB/d²", "F=GmAmB/d2", "G·mA·mB/d²"], 'explication': "$F = G \\frac{m_A m_B}{d^2}$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Quelle est la valeur de la constante de gravitation universelle $G$ (avec son unité) ?", 'reponse_correcte': "6,674 × 10⁻¹¹ N·m²·kg⁻²", 'tolerances': ["6.674e-11", "6,67 × 10⁻¹¹", "6,674 × 10^-11"], 'explication': "$G = 6{,}674 \\times 10^{-11}$ N·m²·kg⁻².", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Quelle interaction fondamentale est responsable de la cohésion des noyaux atomiques ?", 'reponse_correcte': "interaction nucléaire forte", 'tolerances': ["nucléaire forte", "force forte", "interaction forte"], 'explication': "L'interaction nucléaire forte lie les nucléons malgré la répulsion électrostatique entre protons.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Notion de champ',
                'duree': 35,
                'contenu': """# Notion de champ

## Qu'est-ce qu'un champ ?

Un **champ** est une grandeur physique (scalaire ou vectorielle) définie en tout point de l'espace. Il permet de décrire l'influence d'un objet sur son environnement sans contact direct.

---

## Champ scalaire et champ vectoriel

- **Champ scalaire** : défini par un nombre en chaque point (température, pression, altitude)
- **Champ vectoriel** : défini par un vecteur (direction, sens, norme) en chaque point (champ de gravitation, champ électrique, champ de vitesse)

---

## Champ de gravitation

Le champ de gravitation $\\vec{g}$ créé par un corps de masse $M$ en un point situé à la distance $r$ du centre :

$$
\\vec{g} = -G \\frac{M}{r^2} \\vec{u_r}
$$

- Dirigé vers le centre du corps qui le crée
- À la surface de la Terre : $g \\approx 9{,}81$ N·kg⁻¹

Le **poids** d'un objet de masse $m$ est :
$$
\\vec{P} = m \\vec{g}
$$

---

## Champ électrique

Le champ électrique $\\vec{E}$ créé par une charge ponctuelle $Q$ :

$$
\\vec{E} = k \\frac{Q}{r^2} \\vec{u_r}
$$

La **force électrique** subie par une charge $q$ placée dans ce champ :
$$
\\vec{F} = q \\vec{E}
$$

---

## Lignes de champ

Les **lignes de champ** sont des courbes tangentes en chaque point au vecteur champ. Elles permettent de visualiser la structure du champ.

### Propriétés

- Plus les lignes sont resserrées, plus le champ est intense
- Les lignes de champ ne se croisent jamais
- Pour un champ **uniforme**, les lignes sont parallèles et équidistantes

### Exemples

- **Charge ponctuelle positive** : lignes radiales dirigées vers l'extérieur
- **Charge ponctuelle négative** : lignes radiales dirigées vers la charge
- **Condensateur plan** : lignes parallèles entre les plaques → champ uniforme

---

## Champ uniforme

Un champ est dit **uniforme** dans une région de l'espace s'il a la même valeur (direction, sens, norme) en tout point de cette région.

**Exemples :**
- Le champ de pesanteur $\\vec{g}$ est considéré uniforme au voisinage de la surface terrestre
- Le champ électrique entre les plaques d'un condensateur plan

---
""",
                'quiz': {
                    'titre': 'Quiz — Notion de champ',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Un champ vectoriel est défini en chaque point par :", 'options': ["Un vecteur", "Un nombre", "Une couleur", "Une fréquence"], 'reponse_correcte': '0', 'explication': "Un champ vectoriel associe un vecteur à chaque point de l'espace.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Le champ de pesanteur à la surface de la Terre vaut environ :", 'options': ["9,81 N·kg⁻¹", "6,67 N·kg⁻¹", "3,0 N·kg⁻¹", "1,0 N·kg⁻¹"], 'reponse_correcte': '0', 'explication': "$g \\approx 9{,}81$ N·kg⁻¹ à la surface de la Terre.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "La température est un exemple de :", 'options': ["Champ scalaire", "Champ vectoriel", "Force", "Énergie"], 'reponse_correcte': '0', 'explication': "La température associe un nombre à chaque point : c'est un champ scalaire.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Le poids d'un objet de masse $m$ est donné par :", 'options': ["P = mg", "P = mv", "P = mv²", "P = mgh"], 'reponse_correcte': '0', 'explication': "Le poids est $\\vec{P} = m\\vec{g}$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Les lignes de champ d'une charge ponctuelle positive sont :", 'options': ["Dirigées vers l'extérieur", "Dirigées vers la charge", "Circulaires", "Parallèles"], 'reponse_correcte': '0', 'explication': "Les lignes de champ d'une charge positive s'éloignent de la charge.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Un champ uniforme a des lignes de champ :", 'options': ["Parallèles et équidistantes", "Convergentes", "Divergentes", "Circulaires"], 'reponse_correcte': '0', 'explication': "Dans un champ uniforme, les lignes sont parallèles et régulièrement espacées.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Quelle est l'unité du champ électrique ?", 'options': ["V·m⁻¹ (ou N·C⁻¹)", "N·kg⁻¹", "Pa", "J"], 'reponse_correcte': '0', 'explication': "Le champ électrique s'exprime en V·m⁻¹ ou N·C⁻¹.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Le champ de gravitation est créé par :", 'options': ["Une masse", "Une charge électrique", "Un aimant", "Un courant"], 'reponse_correcte': '0', 'explication': "Toute masse crée un champ de gravitation dans l'espace environnant.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Le champ de gravitation créé par une masse $M$ à la distance $r$ est proportionnel à :", 'options': ["M/r²", "M/r", "M·r²", "M·r"], 'reponse_correcte': '0', 'explication': "$g = G \\frac{M}{r^2}$ : proportionnel à $M/r^2$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "La force subie par une charge $q$ dans un champ électrique $\\vec{E}$ est :", 'options': ["F = qE", "F = qE²", "F = q/E", "F = E/q"], 'reponse_correcte': '0', 'explication': "$\\vec{F} = q\\vec{E}$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Le champ de pesanteur est considéré uniforme :", 'options': ["Au voisinage de la surface terrestre", "Partout dans l'univers", "Uniquement au centre de la Terre", "Uniquement en haute altitude"], 'reponse_correcte': '0', 'explication': "Au voisinage de la surface terrestre, $\\vec{g}$ est quasiment constant.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Plus les lignes de champ sont resserrées :", 'options': ["Plus le champ est intense", "Plus le champ est faible", "Plus le champ est uniforme", "Cela n'a pas de lien avec l'intensité"], 'reponse_correcte': '0', 'explication': "La densité des lignes de champ traduit l'intensité du champ.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Le champ électrique entre les plaques d'un condensateur plan est :", 'options': ["Uniforme", "Nul", "Radial", "Variable"], 'reponse_correcte': '0', 'explication': "Entre les plaques d'un condensateur plan, le champ est uniforme.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Les lignes de champ d'une charge ponctuelle négative sont :", 'options': ["Dirigées vers la charge", "Dirigées vers l'extérieur", "Parallèles", "Circulaires"], 'reponse_correcte': '0', 'explication': "Les lignes de champ convergent vers une charge négative.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Les lignes de champ peuvent se croiser.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Les lignes de champ ne se croisent jamais.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Le champ de gravitation est un champ vectoriel.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "Le champ de gravitation est défini par un vecteur en chaque point.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Le champ électrique créé par une charge ponctuelle est uniforme.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Le champ d'une charge ponctuelle varie en $1/r^2$ : il n'est pas uniforme.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner l'expression du poids d'un objet de masse $m$ dans un champ de pesanteur $g$.", 'reponse_correcte': "P = mg", 'tolerances': ["P = m × g", "P=m·g", "P = m.g"], 'explication': "$\\vec{P} = m\\vec{g}$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Donner l'expression du champ électrique créé par une charge $Q$ à la distance $r$.", 'reponse_correcte': "E = kQ/r²", 'tolerances': ["E = k × Q / r²", "kQ/r2", "E=kQ/r²"], 'explication': "$E = k \\frac{Q}{r^2}$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Comment appelle-t-on un champ qui a la même valeur (direction, sens, norme) en tout point d'une région ?", 'reponse_correcte': "champ uniforme", 'tolerances': ["uniforme", "un champ uniforme", "champ constant"], 'explication': "Un champ uniforme est identique en tout point de la région considérée.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 2 — Statique des fluides
    # ──────────────────────────────────────────────
    {
        'ordre': 2,
        'titre': 'Statique des fluides',
        'description': "Étudier la pression dans les fluides au repos et la poussée d'Archimède.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Pression dans un fluide',
                'duree': 35,
                'contenu': """# Pression dans un fluide

## Notion de pression

La **pression** $P$ est le rapport de la force $F$ exercée perpendiculairement à une surface $S$ :

$$
P = \\frac{F}{S}
$$

- Unité SI : le **pascal** (Pa) — 1 Pa = 1 N·m⁻²
- Autres unités : 1 bar = $10^5$ Pa ; 1 atm = $1{,}013 \\times 10^5$ Pa

---

## Propriétés de la pression dans un fluide au repos

### Principe de Pascal

La pression exercée sur un fluide incompressible en équilibre se transmet intégralement dans toutes les directions.

### Pression dans un fluide au repos

Dans un fluide homogène incompressible de masse volumique $\\rho$, soumis à la gravité :

$$
P = P_0 + \\rho g h
$$

- $P_0$ : pression à la surface libre (souvent la pression atmosphérique)
- $\\rho$ : masse volumique du fluide (kg·m⁻³)
- $g$ : accélération de la pesanteur (m·s⁻²)
- $h$ : profondeur sous la surface libre (m)

### Conséquences

- La pression augmente avec la profondeur
- Tous les points situés à la même profondeur dans un même fluide au repos sont à la même pression (**surfaces isobares horizontales**)

---

## Exemples

**Pression au fond d'une piscine de 3 m de profondeur :**

$P_0 = 1{,}013 \\times 10^5$ Pa, $\\rho_{eau} = 1000$ kg·m⁻³, $g = 9{,}81$ m·s⁻²

$$
P = 1{,}013 \\times 10^5 + 1000 \\times 9{,}81 \\times 3 = 1{,}31 \\times 10^5 \\text{ Pa}
$$

---

## Mesure de la pression

- **Manomètre** : mesure la pression relative (par rapport à $P_0$)
- **Baromètre** : mesure la pression atmosphérique

---
""",
                'quiz': {
                    'titre': 'Quiz — Pression dans un fluide',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "L'unité SI de la pression est :", 'options': ["Le pascal (Pa)", "Le bar", "L'atmosphère (atm)", "Le newton (N)"], 'reponse_correcte': '0', 'explication': "L'unité SI de la pression est le pascal (Pa).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "La pression est définie comme le rapport :", 'options': ["F/S", "F × S", "F + S", "S/F"], 'reponse_correcte': '0', 'explication': "$P = F/S$ : force par unité de surface.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "1 bar est égal à :", 'options': ["10⁵ Pa", "10³ Pa", "10⁶ Pa", "10² Pa"], 'reponse_correcte': '0', 'explication': "1 bar = $10^5$ Pa.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Dans un fluide au repos, la pression augmente avec :", 'options': ["La profondeur", "L'altitude", "La température", "La vitesse"], 'reponse_correcte': '0', 'explication': "Plus on descend, plus la pression augmente.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Un manomètre mesure :", 'options': ["La pression relative", "La température", "La vitesse", "La masse volumique"], 'reponse_correcte': '0', 'explication': "Le manomètre mesure la pression relative (par rapport à la pression atmosphérique).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Un baromètre mesure :", 'options': ["La pression atmosphérique", "La pression relative", "La profondeur", "La densité"], 'reponse_correcte': '0', 'explication': "Le baromètre mesure la pression atmosphérique.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "La pression atmosphérique standard vaut environ :", 'options': ["1,013 × 10⁵ Pa", "1 × 10³ Pa", "9,81 Pa", "1,5 × 10⁵ Pa"], 'reponse_correcte': '0', 'explication': "$P_{atm} \\approx 1{,}013 \\times 10^5$ Pa.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "La relation $P = P_0 + \\rho g h$ s'applique à un fluide :", 'options': ["Homogène et au repos", "En mouvement rapide", "Compressible", "Turbulent"], 'reponse_correcte': '0', 'explication': "Cette loi s'applique aux fluides homogènes, incompressibles et au repos.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "La pression au fond d'un lac de 10 m de profondeur ($\\rho_{eau}$ = 1000 kg·m⁻³) est environ :", 'options': ["2 × 10⁵ Pa", "1 × 10⁵ Pa", "3 × 10⁵ Pa", "10 Pa"], 'reponse_correcte': '0', 'explication': "$P = 10^5 + 1000 \\times 9{,}81 \\times 10 \\approx 2 \\times 10^5$ Pa.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Le principe de Pascal affirme que la pression se transmet :", 'options': ["Intégralement dans toutes les directions", "Uniquement vers le bas", "Uniquement vers le haut", "Uniquement horizontalement"], 'reponse_correcte': '0', 'explication': "La pression se transmet intégralement et dans toutes les directions dans un fluide incompressible.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Si la profondeur dans un fluide double, la surpression $\\rho g h$ :", 'options': ["Double", "Quadruple", "Reste constante", "Est divisée par 2"], 'reponse_correcte': '0', 'explication': "La surpression est proportionnelle à $h$ : si $h$ double, $\\rho g h$ double.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Des points situés à la même profondeur dans un fluide au repos ont :", 'options': ["La même pression", "Des pressions différentes", "Une pression nulle", "Une pression variable"], 'reponse_correcte': '0', 'explication': "Les surfaces isobares sont horizontales dans un fluide au repos.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "La masse volumique de l'eau est environ :", 'options': ["1000 kg·m⁻³", "100 kg·m⁻³", "10 000 kg·m⁻³", "1 kg·m⁻³"], 'reponse_correcte': '0', 'explication': "$\\rho_{eau} \\approx 1000$ kg·m⁻³.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "1 atm est approximativement égale à :", 'options': ["1,013 bar", "10 bar", "0,1 bar", "100 bar"], 'reponse_correcte': '0', 'explication': "1 atm $\\approx$ 1,013 bar.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "La pression dans un fluide au repos ne dépend pas de la forme du récipient.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "La pression ne dépend que de la profondeur, de la masse volumique et de $g$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "La pression atmosphérique est identique à toutes les altitudes.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "La pression atmosphérique diminue avec l'altitude.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "1 Pa = 1 N·m⁻².", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "Par définition, 1 pascal = 1 newton par mètre carré.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner l'expression de la pression dans un fluide en fonction de la profondeur $h$.", 'reponse_correcte': "P = P₀ + ρgh", 'tolerances': ["P=P0+ρgh", "P = P0 + rho × g × h", "P0 + ρgh"], 'explication': "$P = P_0 + \\rho g h$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Quelle est la valeur de la pression atmosphérique standard en pascal ?", 'reponse_correcte': "1,013 × 10⁵ Pa", 'tolerances': ["101300 Pa", "101325 Pa", "1.013 × 10^5 Pa"], 'explication': "$P_{atm} = 1{,}013 \\times 10^5$ Pa.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Comment appelle-t-on les surfaces de même pression dans un fluide au repos ?", 'reponse_correcte': "surfaces isobares", 'tolerances': ["isobares", "des surfaces isobares", "surfaces isobares horizontales"], 'explication': "Les surfaces isobares sont horizontales dans un fluide homogène au repos.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': "Poussée d'Archimède",
                'duree': 35,
                'contenu': """# Poussée d'Archimède

## Énoncé du principe

Tout corps immergé (partiellement ou totalement) dans un fluide au repos subit de la part de ce fluide une force verticale, dirigée vers le haut, appelée **poussée d'Archimède** :

$$
\\vec{\\Pi} = -\\rho_{fluide} \\cdot V_{immergé} \\cdot \\vec{g}
$$

En norme :
$$
\\Pi = \\rho_{fluide} \\cdot V_{immergé} \\cdot g
$$

- $\\rho_{fluide}$ : masse volumique du fluide (kg·m⁻³)
- $V_{immergé}$ : volume de la partie immergée du corps (m³)
- $g$ : accélération de la pesanteur (m·s⁻²)

---

## Origine de la poussée d'Archimède

La poussée d'Archimède résulte de la **différence de pression** entre le bas et le haut du corps immergé. La pression étant plus forte en bas (car $P$ augmente avec la profondeur), la résultante des forces de pression est dirigée vers le haut.

---

## Conditions d'équilibre d'un corps dans un fluide

Un corps de masse volumique $\\rho_{corps}$ dans un fluide de masse volumique $\\rho_{fluide}$ :

| Condition | Comportement |
|---|---|
| $\\rho_{corps} < \\rho_{fluide}$ | Le corps **flotte** |
| $\\rho_{corps} = \\rho_{fluide}$ | Le corps est en **équilibre indifférent** |
| $\\rho_{corps} > \\rho_{fluide}$ | Le corps **coule** |

---

## Exemple

**Un bloc d'aluminium** ($\\rho = 2700$ kg·m⁻³, volume $V = 0{,}001$ m³) immergé dans l'eau :

- Poids : $P = m \\cdot g = \\rho \\cdot V \\cdot g = 2700 \\times 0{,}001 \\times 9{,}81 = 26{,}5$ N
- Poussée d'Archimède : $\\Pi = 1000 \\times 0{,}001 \\times 9{,}81 = 9{,}81$ N
- Le bloc coule car $P > \\Pi$
- Le **poids apparent** vaut : $P - \\Pi = 26{,}5 - 9{,}81 = 16{,}7$ N

---
""",
                'quiz': {
                    'titre': "Quiz — Poussée d'Archimède",
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "La poussée d'Archimède est dirigée vers :", 'options': ["Le haut", "Le bas", "La droite", "La gauche"], 'reponse_correcte': '0', 'explication': "La poussée d'Archimède est toujours verticale, dirigée vers le haut.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "La poussée d'Archimède s'applique à un corps :", 'options': ["Immergé dans un fluide", "Posé sur un sol sec", "En chute libre dans le vide", "En orbite spatiale"], 'reponse_correcte': '0', 'explication': "La poussée d'Archimède s'exerce sur tout corps immergé dans un fluide.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Un corps flotte si sa masse volumique est :", 'options': ["Inférieure à celle du fluide", "Supérieure à celle du fluide", "Égale à la pression atmosphérique", "Nulle"], 'reponse_correcte': '0', 'explication': "Un corps flotte lorsque $\\rho_{corps} < \\rho_{fluide}$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "La poussée d'Archimède est due à :", 'options': ["La différence de pression entre le bas et le haut du corps", "La température du fluide", "Le vent", "La viscosité du fluide"], 'reponse_correcte': '0', 'explication': "Elle résulte de la différence de pression hydrostatique.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "L'unité de la poussée d'Archimède est :", 'options': ["Le newton (N)", "Le pascal (Pa)", "Le joule (J)", "Le watt (W)"], 'reponse_correcte': '0', 'explication': "La poussée d'Archimède est une force, mesurée en newtons.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Un corps coule dans un fluide si :", 'options': ["ρ_corps > ρ_fluide", "ρ_corps < ρ_fluide", "ρ_corps = 0", "ρ_corps = ρ_fluide"], 'reponse_correcte': '0', 'explication': "Si la masse volumique du corps dépasse celle du fluide, il coule.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "La poussée d'Archimède dépend du volume :", 'options': ["Immergé du corps", "Total du récipient", "De la Terre", "Du fluide entier"], 'reponse_correcte': '0', 'explication': "Seul le volume de la partie immergée intervient.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Le poids apparent d'un corps immergé vaut :", 'options': ["P − Π", "P + Π", "P × Π", "P / Π"], 'reponse_correcte': '0', 'explication': "Le poids apparent est la différence entre le poids et la poussée d'Archimède.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "L'expression de la norme de la poussée d'Archimède est :", 'options': ["Π = ρ_fluide × V_immergé × g", "Π = m × g", "Π = ρ × V × v", "Π = F / S"], 'reponse_correcte': '0', 'explication': "$\\Pi = \\rho_{fluide} \\cdot V_{immergé} \\cdot g$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Un bloc de bois ($\\rho$ = 600 kg·m⁻³) placé dans l'eau ($\\rho$ = 1000 kg·m⁻³) :", 'options': ["Flotte", "Coule", "Est en équilibre indifférent", "Se dissout"], 'reponse_correcte': '0', 'explication': "$\\rho_{bois} < \\rho_{eau}$ donc le bois flotte.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "La poussée d'Archimède ne dépend pas de :", 'options': ["La masse du corps immergé", "La masse volumique du fluide", "Le volume immergé", "L'accélération de la pesanteur"], 'reponse_correcte': '0', 'explication': "La formule $\\Pi = \\rho_{fluide} V g$ ne fait pas intervenir la masse du corps.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Un corps en équilibre indifférent dans un fluide vérifie :", 'options': ["ρ_corps = ρ_fluide", "ρ_corps > ρ_fluide", "ρ_corps < ρ_fluide", "ρ_corps = 0"], 'reponse_correcte': '0', 'explication': "L'équilibre indifférent correspond à l'égalité des masses volumiques.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Si on double le volume immergé, la poussée d'Archimède :", 'options': ["Double", "Quadruple", "Reste constante", "Est divisée par 2"], 'reponse_correcte': '0', 'explication': "$\\Pi \\propto V_{immergé}$ : doubler $V$ double $\\Pi$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "La poussée d'Archimède dans le mercure ($\\rho$ = 13600 kg·m⁻³) est plus grande que dans l'eau car :", 'options': ["ρ_mercure est plus grand que ρ_eau", "Le mercure est un métal", "Le volume change", "La gravité est différente"], 'reponse_correcte': '0', 'explication': "$\\Pi = \\rho_{fluide} V g$ : plus $\\rho$ est grand, plus $\\Pi$ est grande.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "La poussée d'Archimède dépend de la profondeur à laquelle le corps est totalement immergé.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Pour un corps totalement immergé, $\\Pi$ ne dépend pas de la profondeur (seul $V$ et $\\rho_{fluide}$ comptent).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Un objet totalement immergé subit une poussée d'Archimède égale au poids du fluide déplacé.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "C'est la formulation classique du principe d'Archimède.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Un sous-marin modifie sa masse volumique moyenne pour plonger ou remonter.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "En remplissant ou vidant ses ballasts, le sous-marin change sa masse volumique moyenne.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner l'expression de la norme de la poussée d'Archimède.", 'reponse_correcte': "Π = ρ_fluide × V_immergé × g", 'tolerances': ["ρVg", "rho × V × g", "Π=ρfluide·Vimmergé·g"], 'explication': "$\\Pi = \\rho_{fluide} \\cdot V_{immergé} \\cdot g$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Un bloc de volume 0,002 m³ est totalement immergé dans l'eau. Calculer la poussée d'Archimède ($g$ = 9,81 m·s⁻²).", 'reponse_correcte': "19,62 N", 'tolerances': ["19,6 N", "19.62 N", "environ 20 N"], 'explication': "$\\Pi = 1000 \\times 0{,}002 \\times 9{,}81 = 19{,}62$ N.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Quelle condition sur les masses volumiques permet à un corps de flotter dans un fluide ?", 'reponse_correcte': "ρ_corps < ρ_fluide", 'tolerances': ["masse volumique du corps inférieure à celle du fluide", "densité inférieure", "ρcorps < ρfluide"], 'explication': "Un corps flotte si $\\rho_{corps} < \\rho_{fluide}$.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 3 — Mouvements et forces
    # ──────────────────────────────────────────────
    {
        'ordre': 3,
        'titre': 'Mouvements et forces',
        'description': "Appliquer les lois de Newton pour décrire et prévoir le mouvement d'un système.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Les lois de Newton',
                'duree': 35,
                'contenu': """# Les lois de Newton

## Première loi de Newton — Principe d'inertie

Dans un **référentiel galiléen**, si la somme des forces extérieures appliquées à un système est nulle, alors le centre de masse du système est soit au repos, soit en mouvement rectiligne uniforme :

$$
\\sum \\vec{F}_{ext} = \\vec{0} \\implies \\vec{v} = \\text{constante}
$$

---

## Deuxième loi de Newton — Principe fondamental de la dynamique

Dans un référentiel galiléen, la somme des forces extérieures est égale au produit de la masse par l'accélération :

$$
\\sum \\vec{F}_{ext} = m \\vec{a}
$$

- $m$ : masse du système (kg)
- $\\vec{a}$ : vecteur accélération (m·s⁻²)

### Conséquences

- Si $\\sum \\vec{F}_{ext} \\neq \\vec{0}$, le système est **accéléré** (la vitesse change en norme et/ou en direction)
- L'accélération a la **même direction et le même sens** que la résultante des forces
- Plus la masse est grande, plus l'accélération est faible pour une même force

---

## Troisième loi de Newton — Principe des actions réciproques

Si un corps A exerce une force $\\vec{F}_{A/B}$ sur un corps B, alors B exerce sur A une force $\\vec{F}_{B/A}$ telle que :

$$
\\vec{F}_{A/B} = -\\vec{F}_{B/A}
$$

Les deux forces sont de même direction, de même norme, mais de sens opposés.

---

## Bilan des forces

Pour étudier le mouvement d'un système :
1. **Définir le système** et le référentiel
2. **Recenser les forces** extérieures (poids, réaction du support, tension, frottements, poussée d'Archimède…)
3. **Appliquer** la 2ᵉ loi de Newton

---
""",
                'quiz': {
                    'titre': 'Quiz — Les lois de Newton',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "La première loi de Newton s'appelle :", 'options': ["Le principe d'inertie", "Le principe fondamental de la dynamique", "Le principe des actions réciproques", "Le principe de conservation"], 'reponse_correcte': '0', 'explication': "La 1ʳᵉ loi est le principe d'inertie.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "La deuxième loi de Newton s'écrit :", 'options': ["ΣF = ma", "F = mv", "E = mc²", "P = mg"], 'reponse_correcte': '0', 'explication': "$\\sum \\vec{F} = m\\vec{a}$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "L'unité de la force dans le SI est :", 'options': ["Le newton (N)", "Le kilogramme (kg)", "Le joule (J)", "Le pascal (Pa)"], 'reponse_correcte': '0', 'explication': "La force se mesure en newtons.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Un objet au repos dans un référentiel galiléen vérifie :", 'options': ["ΣF = 0", "ΣF > 0", "ΣF < 0", "F = ma avec a ≠ 0"], 'reponse_correcte': '0', 'explication': "Au repos, la somme des forces est nulle (1ʳᵉ loi de Newton).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "L'accélération a la même direction que :", 'options': ["La résultante des forces", "La vitesse", "La position", "Le déplacement"], 'reponse_correcte': '0', 'explication': "$\\vec{a}$ est colinéaire à $\\sum \\vec{F}$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "La troisième loi de Newton concerne :", 'options': ["Les actions réciproques", "L'inertie", "L'accélération", "L'énergie cinétique"], 'reponse_correcte': '0', 'explication': "La 3ᵉ loi est le principe des actions réciproques.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Dans $\\sum \\vec{F} = m\\vec{a}$, $m$ représente :", 'options': ["La masse du système", "Le poids", "L'énergie", "La vitesse"], 'reponse_correcte': '0', 'explication': "$m$ est la masse du système étudié.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Un référentiel galiléen est un référentiel :", 'options': ["En translation rectiligne uniforme", "En rotation uniforme", "Accéléré", "Quelconque"], 'reponse_correcte': '0', 'explication': "Un référentiel galiléen est en mouvement de translation rectiligne uniforme (ou au repos) par rapport à un autre référentiel galiléen.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Si la somme des forces extérieures est nulle, le mouvement est :", 'options': ["Rectiligne uniforme ou immobile", "Toujours accéléré", "Circulaire uniforme", "Impossible"], 'reponse_correcte': '0', 'explication': "D'après le principe d'inertie : $\\sum\\vec{F}=\\vec{0} \\Rightarrow \\vec{v} = \\text{cte}$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Une force de 10 N est appliquée à un objet de 2 kg. L'accélération vaut :", 'options': ["5 m·s⁻²", "20 m·s⁻²", "0,2 m·s⁻²", "12 m·s⁻²"], 'reponse_correcte': '0', 'explication': "$a = F/m = 10/2 = 5$ m·s⁻².", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Selon la 3ᵉ loi de Newton, $\\vec{F}_{A/B}$ et $\\vec{F}_{B/A}$ ont :", 'options': ["La même norme et des sens opposés", "La même norme et le même sens", "Des normes différentes", "Aucun lien entre elles"], 'reponse_correcte': '0', 'explication': "$\\vec{F}_{A/B} = -\\vec{F}_{B/A}$ : même norme, sens opposés.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Si la masse double et la force reste constante, l'accélération :", 'options': ["Est divisée par 2", "Double", "Reste constante", "Quadruple"], 'reponse_correcte': '0', 'explication': "$a = F/m$ : si $m$ double, $a$ est divisée par 2.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Le bilan des forces sur un objet posé en équilibre sur un plan horizontal comprend :", 'options': ["Le poids et la réaction du support", "Uniquement le poids", "Uniquement la réaction du support", "Aucune force"], 'reponse_correcte': '0', 'explication': "En équilibre : poids $\\vec{P}$ et réaction normale $\\vec{R}_N$ se compensent.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Quelle condition est nécessaire pour appliquer les lois de Newton ?", 'options': ["Se placer dans un référentiel galiléen", "Avoir une vitesse nulle", "Être dans le vide", "Avoir une masse nulle"], 'reponse_correcte': '0', 'explication': "Les lois de Newton ne sont valables que dans un référentiel galiléen.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Si un objet est en mouvement rectiligne uniforme, la somme des forces qui s'exercent sur lui est nulle.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "C'est la première loi de Newton : MRU ⟹ $\\sum\\vec{F}=\\vec{0}$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Les forces d'action et de réaction s'appliquent sur le même corps.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Elles s'appliquent sur deux corps différents.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "L'accélération est toujours dans le sens du mouvement.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "L'accélération peut être opposée au mouvement (freinage).", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Énoncer la deuxième loi de Newton sous forme mathématique.", 'reponse_correcte': "ΣF = ma", 'tolerances': ["somme des F = ma", "F = m × a", "somme des forces = m·a"], 'explication': "$\\sum \\vec{F}_{ext} = m\\vec{a}$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Un objet de 5 kg est soumis à une force résultante de 15 N. Calculer son accélération.", 'reponse_correcte': "3 m·s⁻²", 'tolerances': ["3 m/s²", "3", "3 m.s-2"], 'explication': "$a = F/m = 15/5 = 3$ m·s⁻².", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Comment appelle-t-on le principe selon lequel $\\vec{F}_{A/B} = -\\vec{F}_{B/A}$ ?", 'reponse_correcte': "principe des actions réciproques", 'tolerances': ["actions réciproques", "troisième loi de Newton", "3ème loi de Newton"], 'explication': "C'est le principe des actions réciproques (3ᵉ loi de Newton).", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Mouvement rectiligne et chute libre',
                'duree': 35,
                'contenu': """# Mouvement rectiligne et chute libre

## Vecteur vitesse et vecteur accélération

### Vecteur vitesse

$$
\\vec{v} = \\frac{d\\vec{OM}}{dt}
$$

Dans un repère cartésien : $\\vec{v} = \\dot{x}\\vec{i} + \\dot{y}\\vec{j}$

### Vecteur accélération

$$
\\vec{a} = \\frac{d\\vec{v}}{dt}
$$

---

## Mouvement rectiligne uniforme (MRU)

- $\\vec{a} = \\vec{0}$, donc $\\vec{v} = \\text{constante}$
- Position : $x(t) = x_0 + v \\cdot t$

---

## Mouvement rectiligne uniformément accéléré (MRUA)

- $\\vec{a} = \\text{constante}$
- Vitesse : $v(t) = v_0 + a \\cdot t$
- Position : $x(t) = x_0 + v_0 t + \\frac{1}{2} a t^2$

---

## Chute libre

On appelle **chute libre** le mouvement d'un objet soumis **uniquement à son poids** (on néglige les frottements).

### Équations du mouvement

En prenant l'axe $y$ vertical dirigé vers le haut, origine au point de lancement :

$$
a_x = 0 \\quad ; \\quad a_y = -g
$$

$$
v_x(t) = v_{0x} \\quad ; \\quad v_y(t) = v_{0y} - g t
$$

$$
x(t) = v_{0x} t \\quad ; \\quad y(t) = v_{0y} t - \\frac{1}{2} g t^2
$$

### Chute libre verticale sans vitesse initiale

Si l'objet est lâché sans vitesse initiale ($v_0 = 0$) :
- $v(t) = g t$
- $y(t) = \\frac{1}{2} g t^2$ (distance parcourue vers le bas)

**Exemple :** temps de chute d'un objet lâché de $h = 20$ m :
$$
t = \\sqrt{\\frac{2h}{g}} = \\sqrt{\\frac{2 \\times 20}{9{,}81}} \\approx 2{,}0 \\text{ s}
$$

---
""",
                'quiz': {
                    'titre': 'Quiz — Mouvement rectiligne et chute libre',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Un mouvement rectiligne uniforme a une accélération :", 'options': ["Nulle", "Constante non nulle", "Variable", "Infinie"], 'reponse_correcte': '0', 'explication': "En MRU, $\\vec{a} = \\vec{0}$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "En chute libre, on néglige :", 'options': ["Les frottements de l'air", "La gravité", "La masse de l'objet", "Le temps de chute"], 'reponse_correcte': '0', 'explication': "En chute libre, seul le poids agit ; les frottements sont négligés.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "L'accélération de la pesanteur $g$ vaut environ :", 'options': ["9,81 m·s⁻²", "6,67 m·s⁻²", "3,0 m·s⁻²", "1,0 m·s⁻²"], 'reponse_correcte': '0', 'explication': "$g \\approx 9{,}81$ m·s⁻².", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "En mouvement rectiligne uniforme, la vitesse est :", 'options': ["Constante", "Croissante", "Décroissante", "Nulle"], 'reponse_correcte': '0', 'explication': "Par définition, la vitesse est constante en MRU.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "En chute libre verticale, l'objet est soumis uniquement à :", 'options': ["Son poids", "La poussée d'Archimède", "Les frottements", "La tension d'un fil"], 'reponse_correcte': '0', 'explication': "Par définition, en chute libre seule la gravité agit.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "La position en MRU s'écrit :", 'options': ["x = x₀ + vt", "x = ½at²", "x = v²/(2a)", "x = mg"], 'reponse_correcte': '0', 'explication': "En MRU : $x(t) = x_0 + vt$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Le vecteur accélération est la dérivée temporelle du vecteur :", 'options': ["Vitesse", "Position", "Force", "Masse"], 'reponse_correcte': '0', 'explication': "$\\vec{a} = d\\vec{v}/dt$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "En MRUA, la vitesse varie :", 'options': ["Linéairement avec le temps", "Avec le carré du temps", "De façon exponentielle", "Elle reste constante"], 'reponse_correcte': '0', 'explication': "En MRUA : $v(t) = v_0 + at$, variation linéaire.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "En chute libre sans vitesse initiale, $v(t)$ = :", 'options': ["gt", "½gt²", "g/t", "g + t"], 'reponse_correcte': '0', 'explication': "$v(t) = gt$ pour un objet lâché sans vitesse initiale.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "La distance parcourue en chute libre sans vitesse initiale est :", 'options': ["½gt²", "gt", "g²t", "2gt"], 'reponse_correcte': '0', 'explication': "$y(t) = \\frac{1}{2}gt^2$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Un objet est lâché sans vitesse initiale de 45 m de haut. Le temps de chute est environ :", 'options': ["3,0 s", "4,5 s", "2,0 s", "9,0 s"], 'reponse_correcte': '0', 'explication': "$t = \\sqrt{2h/g} = \\sqrt{2 \\times 45/9{,}81} \\approx 3{,}0$ s.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "En MRUA, la position s'écrit :", 'options': ["x₀ + v₀t + ½at²", "v₀ + at", "½mv²", "F × t"], 'reponse_correcte': '0', 'explication': "$x(t) = x_0 + v_0 t + \\frac{1}{2}at^2$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "En chute libre, l'accélération est :", 'options': ["Indépendante de la masse", "Proportionnelle à la masse", "Inversement proportionnelle à la masse", "Nulle"], 'reponse_correcte': '0', 'explication': "Tous les corps chutent avec la même accélération $g$, quelle que soit leur masse.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Le vecteur vitesse est tangent à :", 'options': ["La trajectoire", "Le vecteur accélération", "Le vecteur force", "Le vecteur position"], 'reponse_correcte': '0', 'explication': "Le vecteur vitesse est toujours tangent à la trajectoire.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "En chute libre, tous les objets tombent avec la même accélération quelle que soit leur masse.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "En l'absence de frottements, l'accélération est $g$ pour tous les corps.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Le vecteur accélération en chute libre est dirigé vers le haut.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "$\\vec{a} = \\vec{g}$ est dirigé vers le bas.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "En MRU, la distance parcourue est proportionnelle au temps.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "$d = v \\times t$ : proportionnalité directe.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner l'expression de la vitesse en fonction du temps en MRUA.", 'reponse_correcte': "v = v₀ + at", 'tolerances': ["v(t) = v0 + at", "v = v₀ + a×t", "v0 + at"], 'explication': "$v(t) = v_0 + at$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Un objet est lâché sans vitesse initiale de 20 m de hauteur. Calculer le temps de chute ($g$ = 9,81 m·s⁻²).", 'reponse_correcte': "2,0 s", 'tolerances': ["2 s", "2.0 s", "environ 2 secondes"], 'explication': "$t = \\sqrt{2h/g} = \\sqrt{2 \\times 20/9{,}81} \\approx 2{,}0$ s.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Donner l'expression de la distance parcourue en chute libre sans vitesse initiale.", 'reponse_correcte': "y = ½gt²", 'tolerances': ["½gt²", "0.5gt²", "gt²/2"], 'explication': "$y(t) = \\frac{1}{2}gt^2$.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 4 — Travail et énergie cinétique
    # ──────────────────────────────────────────────
    {
        'ordre': 4,
        'titre': 'Travail et énergie cinétique',
        'description': "Calculer le travail d'une force et appliquer le théorème de l'énergie cinétique.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Travail d'une force",
                'duree': 35,
                'contenu': """# Travail d'une force

## Définition

Le **travail** d'une force constante $\\vec{F}$ lors d'un déplacement rectiligne $\\vec{AB}$ est :

$$
W_{AB}(\\vec{F}) = \\vec{F} \\cdot \\vec{AB} = F \\cdot AB \\cdot \\cos(\\alpha)
$$

- $F$ : norme de la force (N)
- $AB$ : distance parcourue (m)
- $\\alpha$ : angle entre $\\vec{F}$ et $\\vec{AB}$
- Unité : le **joule** (J)

---

## Cas particuliers

| Situation | Angle $\\alpha$ | Travail |
|---|---|---|
| Force dans le sens du déplacement | $0°$ | $W = F \\cdot d > 0$ (moteur) |
| Force perpendiculaire au déplacement | $90°$ | $W = 0$ |
| Force opposée au déplacement | $180°$ | $W = -F \\cdot d < 0$ (résistant) |

---

## Travail du poids

Le travail du poids ne dépend que de la **différence d'altitude** :

$$
W_{AB}(\\vec{P}) = m g (z_A - z_B) = m g \\Delta z
$$

- Si le corps **descend** ($z_A > z_B$) : $W > 0$ (moteur)
- Si le corps **monte** ($z_A < z_B$) : $W < 0$ (résistant)
- Le travail du poids ne dépend pas du chemin suivi → le poids est une **force conservative**

---

## Puissance

La **puissance** est le travail par unité de temps :

$$
P = \\frac{W}{\\Delta t} = \\vec{F} \\cdot \\vec{v}
$$

Unité : le **watt** (W) — 1 W = 1 J·s⁻¹

---
""",
                'quiz': {
                    'titre': "Quiz — Travail d'une force",
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "L'unité du travail dans le Système International est :", 'options': ["Le joule (J)", "Le newton (N)", "Le watt (W)", "Le pascal (Pa)"], 'reponse_correcte': '0', 'explication': "Le travail s'exprime en joules (J).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Le travail d'une force perpendiculaire au déplacement est :", 'options': ["Nul", "Positif", "Négatif", "Maximal"], 'reponse_correcte': '0', 'explication': "Si $\\alpha = 90°$, $\\cos(90°) = 0$ donc $W = 0$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Un travail moteur est un travail :", 'options': ["Positif", "Négatif", "Nul", "Infini"], 'reponse_correcte': '0', 'explication': "Un travail moteur favorise le déplacement, il est positif.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "La puissance est définie comme :", 'options': ["Le travail par unité de temps", "La force par unité de surface", "L'énergie par unité de masse", "La vitesse par unité de temps"], 'reponse_correcte': '0', 'explication': "$P = W / \\Delta t$ : la puissance est le travail par unité de temps.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "L'unité de la puissance est :", 'options': ["Le watt (W)", "Le joule (J)", "Le newton (N)", "Le pascal (Pa)"], 'reponse_correcte': '0', 'explication': "La puissance s'exprime en watts (W).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Le travail du poids dépend de :", 'options': ["La différence d'altitude", "La distance horizontale parcourue", "La vitesse de l'objet", "La forme du chemin suivi"], 'reponse_correcte': '0', 'explication': "$W(\\vec{P}) = mg(z_A - z_B)$ : seule la différence d'altitude compte.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Quand un objet monte, le travail du poids est :", 'options': ["Résistant (négatif)", "Moteur (positif)", "Nul", "Variable"], 'reponse_correcte': '0', 'explication': "Quand l'objet monte, $z_A < z_B$ donc $W < 0$ : le poids est résistant.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Le poids est une force conservative car :", 'options': ["Son travail ne dépend pas du chemin suivi", "Il est toujours nul", "Il dépend de la vitesse", "Il dépend du temps"], 'reponse_correcte': '0', 'explication': "Le travail du poids ne dépend que des positions initiale et finale.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Une force de 50 N déplace un objet de 10 m dans la direction de la force. Le travail vaut :", 'options': ["500 J", "50 J", "5 J", "5000 J"], 'reponse_correcte': '0', 'explication': "$W = F \\times d = 50 \\times 10 = 500$ J.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Une force de 100 N fait un angle de 60° avec le déplacement de 5 m. Le travail vaut :", 'options': ["250 J", "500 J", "100 J", "433 J"], 'reponse_correcte': '0', 'explication': "$W = 100 \\times 5 \\times \\cos(60°) = 500 \\times 0{,}5 = 250$ J.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Un objet de 2 kg descend de 5 m. Le travail du poids vaut ($g = 10$ m·s⁻²) :", 'options': ["100 J", "−100 J", "10 J", "50 J"], 'reponse_correcte': '0', 'explication': "$W = mgh = 2 \\times 10 \\times 5 = 100$ J (moteur en descente).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Un frottement de 20 N agit sur un objet se déplaçant de 8 m. Le travail du frottement vaut :", 'options': ["−160 J", "160 J", "−80 J", "80 J"], 'reponse_correcte': '0', 'explication': "Les frottements sont opposés au déplacement : $W = -20 \\times 8 = -160$ J.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Une machine fournit un travail de 6000 J en 2 minutes. Sa puissance est :", 'options': ["50 W", "3000 W", "6000 W", "100 W"], 'reponse_correcte': '0', 'explication': "$P = W / \\Delta t = 6000 / 120 = 50$ W.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Un travail résistant correspond à un angle $\\alpha$ entre la force et le déplacement de :", 'options': ["180°", "0°", "90°", "45°"], 'reponse_correcte': '0', 'explication': "À 180°, $\\cos(180°) = -1$, le travail est négatif (résistant).", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Le travail du poids dépend du chemin suivi entre deux points.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Le poids est une force conservative : son travail ne dépend que des altitudes initiale et finale.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "1 watt correspond à 1 joule par seconde.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "Par définition, 1 W = 1 J·s⁻¹.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Une force qui ne travaille pas ne modifie pas la vitesse du système.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Une force perpendiculaire au déplacement ne travaille pas mais peut modifier la direction de la vitesse (ex : force centripète).", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner l'expression du travail d'une force constante $\\vec{F}$ lors d'un déplacement rectiligne $AB$ avec un angle $\\alpha$ entre la force et le déplacement.", 'reponse_correcte': "W = F × AB × cos(α)", 'tolerances': ["F·AB·cos(alpha)", "W=F.d.cos(a)", "F × d × cos(α)"], 'explication': "$W_{AB}(\\vec{F}) = F \\cdot AB \\cdot \\cos(\\alpha)$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Donner l'expression du travail du poids entre deux points A et B d'altitudes $z_A$ et $z_B$.", 'reponse_correcte': "W = mg(zA − zB)", 'tolerances': ["mg(zA-zB)", "W = m × g × (zA − zB)", "mgh"], 'explication': "$W_{AB}(\\vec{P}) = mg(z_A - z_B)$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Donner l'expression de la puissance en fonction de la force $\\vec{F}$ et de la vitesse $\\vec{v}$.", 'reponse_correcte': "P = F × v", 'tolerances': ["P = F·v", "P=Fv", "F.v", "P = F × v × cos(α)"], 'explication': "$P = \\vec{F} \\cdot \\vec{v}$.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': "Énergie cinétique et théorème de l'énergie cinétique",
                'duree': 35,
                'contenu': """# Énergie cinétique et théorème de l'énergie cinétique

## Énergie cinétique

L'**énergie cinétique** d'un objet de masse $m$ se déplaçant à la vitesse $v$ :

$$
E_c = \\frac{1}{2} m v^2
$$

- $m$ en kg, $v$ en m·s⁻¹, $E_c$ en J

---

## Théorème de l'énergie cinétique

La **variation d'énergie cinétique** d'un système entre deux points A et B est égale à la **somme des travaux** de toutes les forces extérieures :

$$
\\Delta E_c = E_c(B) - E_c(A) = \\sum W_{AB}(\\vec{F}_{ext})
$$

Soit :
$$
\\frac{1}{2} m v_B^2 - \\frac{1}{2} m v_A^2 = \\sum W_{AB}
$$

---

## Application : freinage d'une voiture

**Données :** $m = 1200$ kg, $v_A = 90$ km·h⁻¹ $= 25$ m·s⁻¹, $v_B = 0$

$$
\\Delta E_c = 0 - \\frac{1}{2} \\times 1200 \\times 25^2 = -375\\,000 \\text{ J} = -375 \\text{ kJ}
$$

La force de frottement doit effectuer un travail de $-375$ kJ pour stopper le véhicule.

Si $F_{frot} = 7500$ N :
$$
d = \\frac{|\\Delta E_c|}{F_{frot}} = \\frac{375\\,000}{7500} = 50 \\text{ m}
$$

---

## Lien avec les forces

| Si $\\sum W > 0$ | $E_c$ augmente | Le système **accélère** |
|---|---|---|
| Si $\\sum W = 0$ | $E_c$ constante | Vitesse **constante** |
| Si $\\sum W < 0$ | $E_c$ diminue | Le système **ralentit** |

---
""",
                'quiz': {
                    'titre': "Quiz — Énergie cinétique et théorème de l'énergie cinétique",
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "L'énergie cinétique d'un objet dépend de :", 'options': ["Sa masse et sa vitesse", "Sa masse et son altitude", "Sa vitesse et son altitude", "Sa masse uniquement"], 'reponse_correcte': '0', 'explication': "$E_c = \\frac{1}{2}mv^2$ dépend de la masse et de la vitesse.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "L'unité de l'énergie cinétique est :", 'options': ["Le joule (J)", "Le watt (W)", "Le newton (N)", "Le kilogramme (kg)"], 'reponse_correcte': '0', 'explication': "L'énergie cinétique s'exprime en joules.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Si la vitesse d'un objet double, son énergie cinétique est :", 'options': ["Multipliée par 4", "Multipliée par 2", "Inchangée", "Divisée par 2"], 'reponse_correcte': '0', 'explication': "$E_c \\propto v^2$ : si $v$ double, $E_c$ est multipliée par $2^2 = 4$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "L'énergie cinétique d'un objet immobile est :", 'options': ["Nulle", "Positive", "Négative", "Infinie"], 'reponse_correcte': '0', 'explication': "Si $v = 0$, $E_c = \\frac{1}{2}m \\times 0^2 = 0$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "L'énergie cinétique est toujours :", 'options': ["Positive ou nulle", "Négative", "Constante", "Nulle"], 'reponse_correcte': '0', 'explication': "$E_c = \\frac{1}{2}mv^2 \\geq 0$ car $m > 0$ et $v^2 \\geq 0$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Le théorème de l'énergie cinétique relie la variation d'énergie cinétique à :", 'options': ["La somme des travaux des forces extérieures", "La masse du système", "L'altitude du système", "La puissance fournie"], 'reponse_correcte': '0', 'explication': "$\\Delta E_c = \\sum W_{AB}(\\vec{F}_{ext})$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Si la somme des travaux des forces est positive, le système :", 'options': ["Accélère", "Ralentit", "Reste à vitesse constante", "S'arrête"], 'reponse_correcte': '0', 'explication': "$\\sum W > 0 \\Rightarrow \\Delta E_c > 0$ : le système accélère.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Pour convertir 90 km·h⁻¹ en m·s⁻¹, on divise par :", 'options': ["3,6", "10", "60", "100"], 'reponse_correcte': '0', 'explication': "$90 \\div 3{,}6 = 25$ m·s⁻¹.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "L'énergie cinétique d'une voiture de 1000 kg roulant à 20 m·s⁻¹ vaut :", 'options': ["200 000 J", "100 000 J", "20 000 J", "400 000 J"], 'reponse_correcte': '0', 'explication': "$E_c = \\frac{1}{2} \\times 1000 \\times 20^2 = 200\\,000$ J.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Un objet de 5 kg passe de 4 m·s⁻¹ à 10 m·s⁻¹. La variation d'énergie cinétique vaut :", 'options': ["210 J", "150 J", "250 J", "130 J"], 'reponse_correcte': '0', 'explication': "$\\Delta E_c = \\frac{1}{2} \\times 5 \\times (10^2 - 4^2) = \\frac{1}{2} \\times 5 \\times 84 = 210$ J.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Une voiture de 1200 kg roule à 25 m·s⁻¹ et freine jusqu'à l'arrêt. Le travail des forces de freinage vaut :", 'options': ["−375 000 J", "375 000 J", "−187 500 J", "187 500 J"], 'reponse_correcte': '0', 'explication': "$\\Delta E_c = 0 - \\frac{1}{2} \\times 1200 \\times 25^2 = -375\\,000$ J.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Si on triple la masse d'un objet sans changer sa vitesse, son énergie cinétique est :", 'options': ["Triplée", "Multipliée par 9", "Inchangée", "Divisée par 3"], 'reponse_correcte': '0', 'explication': "$E_c \\propto m$ : tripler la masse triple l'énergie cinétique.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "La distance de freinage est proportionnelle à :", 'options': ["Le carré de la vitesse initiale", "La vitesse initiale", "La masse du véhicule", "La force de freinage"], 'reponse_correcte': '0', 'explication': "$d = \\frac{\\frac{1}{2}mv^2}{F} \\propto v^2$ : la distance de freinage est proportionnelle à $v^2$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Un cycliste (80 kg) passe de 0 à 6 m·s⁻¹. Le travail total des forces vaut :", 'options': ["1440 J", "480 J", "2880 J", "720 J"], 'reponse_correcte': '0', 'explication': "$\\Delta E_c = \\frac{1}{2} \\times 80 \\times 6^2 - 0 = 1440$ J.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "L'énergie cinétique peut être négative.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "$E_c = \\frac{1}{2}mv^2 \\geq 0$ : elle est toujours positive ou nulle.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Le théorème de l'énergie cinétique s'applique uniquement en l'absence de frottements.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Le TEC s'applique dans tous les cas : $\\Delta E_c = \\sum W$ inclut le travail de toutes les forces, y compris les frottements.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Si la somme des travaux des forces est nulle, la vitesse du système reste constante.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "$\\sum W = 0 \\Rightarrow \\Delta E_c = 0$ : la vitesse ne change pas.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner l'expression de l'énergie cinétique d'un objet de masse $m$ et de vitesse $v$.", 'reponse_correcte': "Ec = ½mv²", 'tolerances': ["Ec = (1/2)mv²", "½mv²", "Ec = 0.5 × m × v²", "1/2 mv2"], 'explication': "$E_c = \\frac{1}{2}mv^2$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Énoncer le théorème de l'énergie cinétique en une phrase.", 'reponse_correcte': "La variation d'énergie cinétique est égale à la somme des travaux des forces extérieures", 'tolerances': ["ΔEc = somme des travaux", "delta Ec = somme W", "variation Ec = travail total"], 'explication': "$\\Delta E_c = E_c(B) - E_c(A) = \\sum W_{AB}(\\vec{F}_{ext})$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Calculer l'énergie cinétique d'un objet de 3 kg se déplaçant à 4 m·s⁻¹.", 'reponse_correcte': "24 J", 'tolerances': ["24", "24 joules", "24,0 J"], 'explication': "$E_c = \\frac{1}{2} \\times 3 \\times 4^2 = 24$ J.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 5 — Énergie potentielle et énergie mécanique
    # ──────────────────────────────────────────────
    {
        'ordre': 5,
        'titre': 'Énergie potentielle et énergie mécanique',
        'description': "Comprendre l'énergie potentielle de pesanteur, l'énergie mécanique et sa conservation.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Énergie potentielle de pesanteur',
                'duree': 35,
                'contenu': """# Énergie potentielle de pesanteur

## Définition

L'**énergie potentielle de pesanteur** est l'énergie que possède un objet du fait de sa position dans le champ de gravitation :

$$
E_{pp} = m g z
$$

- $m$ : masse de l'objet (kg)
- $g$ : accélération de la pesanteur (m·s⁻²)
- $z$ : altitude par rapport à une référence choisie (m)

---

## Choix de la référence

L'énergie potentielle est définie **à une constante près**. Il faut choisir un niveau de référence où $E_{pp} = 0$.

> **Convention usuelle :** on choisit le sol comme référence ($z = 0$).

---

## Lien avec le travail du poids

Le travail du poids est lié à la variation d'énergie potentielle :

$$
W_{AB}(\\vec{P}) = -(E_{pp}(B) - E_{pp}(A)) = -\\Delta E_{pp}
$$

- Si l'objet descend : $\\Delta E_{pp} < 0$ et $W > 0$ (le poids est moteur)
- Si l'objet monte : $\\Delta E_{pp} > 0$ et $W < 0$ (le poids est résistant)

---

## Force conservative

Le poids est une **force conservative** car son travail ne dépend que des positions initiale et finale, pas du chemin suivi. L'énergie potentielle de pesanteur est l'énergie potentielle associée au poids.

---
""",
                'quiz': {
                    'titre': 'Quiz — Énergie potentielle de pesanteur',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "L'énergie potentielle de pesanteur dépend de :", 'options': ["La masse, g et l'altitude", "La masse et la vitesse", "La vitesse et l'altitude", "La masse uniquement"], 'reponse_correcte': '0', 'explication': "$E_{pp} = mgz$ dépend de $m$, $g$ et $z$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "L'unité de l'énergie potentielle de pesanteur est :", 'options': ["Le joule (J)", "Le newton (N)", "Le watt (W)", "Le mètre (m)"], 'reponse_correcte': '0', 'explication': "L'énergie potentielle s'exprime en joules.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "L'énergie potentielle de pesanteur est définie :", 'options': ["À une constante près", "De manière absolue", "Uniquement au sol", "Uniquement en altitude"], 'reponse_correcte': '0', 'explication': "$E_{pp}$ dépend du choix du niveau de référence, donc elle est définie à une constante près.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Si on choisit le sol comme référence, l'énergie potentielle au sol vaut :", 'options': ["Zéro", "mgh", "mg", "Infini"], 'reponse_correcte': '0', 'explication': "Au sol, $z = 0$ donc $E_{pp} = mg \\times 0 = 0$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Quand un objet monte, son énergie potentielle de pesanteur :", 'options': ["Augmente", "Diminue", "Reste constante", "S'annule"], 'reponse_correcte': '0', 'explication': "$z$ augmente, donc $E_{pp} = mgz$ augmente.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Le travail du poids est lié à la variation d'énergie potentielle par :", 'options': ["W = −ΔEpp", "W = ΔEpp", "W = Epp", "W = −Epp"], 'reponse_correcte': '0', 'explication': "$W(\\vec{P}) = -(E_{pp}(B) - E_{pp}(A)) = -\\Delta E_{pp}$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Plus l'altitude d'un objet est grande, plus son énergie potentielle est :", 'options': ["Élevée", "Faible", "Nulle", "Négative"], 'reponse_correcte': '0', 'explication': "$E_{pp} = mgz$ : proportionnelle à l'altitude $z$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "La force de pesanteur est qualifiée de force conservative car :", 'options': ["Son travail ne dépend pas du chemin suivi", "Elle est toujours nulle", "Son travail est toujours positif", "Elle ne fait jamais de travail"], 'reponse_correcte': '0', 'explication': "Le travail du poids ne dépend que de la différence d'altitude.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Un objet de 5 kg est situé à 10 m du sol ($g = 10$ m·s⁻²). Son énergie potentielle vaut :", 'options': ["500 J", "50 J", "100 J", "250 J"], 'reponse_correcte': '0', 'explication': "$E_{pp} = 5 \\times 10 \\times 10 = 500$ J.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Un objet de 2 kg descend de 15 m à 5 m. La variation d'énergie potentielle vaut ($g = 10$ m·s⁻²) :", 'options': ["−200 J", "200 J", "−100 J", "100 J"], 'reponse_correcte': '0', 'explication': "$\\Delta E_{pp} = mg(z_B - z_A) = 2 \\times 10 \\times (5-15) = -200$ J.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Le travail du poids quand un objet de 3 kg descend de 8 m vaut ($g = 10$ m·s⁻²) :", 'options': ["240 J", "−240 J", "24 J", "−24 J"], 'reponse_correcte': '0', 'explication': "$W = mg \\Delta z = 3 \\times 10 \\times 8 = 240$ J (positif en descente).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Si le niveau de référence est changé mais pas la situation physique, la variation d'énergie potentielle entre deux points :", 'options': ["Reste la même", "Change de signe", "Double", "S'annule"], 'reponse_correcte': '0', 'explication': "$\\Delta E_{pp}$ ne dépend pas du choix de la référence car la constante s'élimine.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Sur la Lune ($g_{Lune} \\approx 1{,}6$ m·s⁻²), l'énergie potentielle d'un objet de 10 kg à 5 m de hauteur vaut :", 'options': ["80 J", "500 J", "490 J", "16 J"], 'reponse_correcte': '0', 'explication': "$E_{pp} = 10 \\times 1{,}6 \\times 5 = 80$ J.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Un objet monte de 4 m. Le travail du poids est :", 'options': ["Négatif", "Positif", "Nul", "Variable"], 'reponse_correcte': '0', 'explication': "En montée $z_B > z_A$ : $W = mg(z_A - z_B) < 0$ (résistant).", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "L'énergie potentielle de pesanteur peut être négative si l'objet est en dessous du niveau de référence.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "Si $z < 0$ (sous le niveau de référence), $E_{pp} = mgz < 0$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "La variation d'énergie potentielle entre deux points est indépendante du choix de la référence.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "$\\Delta E_{pp} = mg(z_B - z_A)$ : les constantes s'annulent.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Les frottements sont des forces conservatives.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Les frottements sont des forces non conservatives : leur travail dépend du chemin suivi.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner l'expression de l'énergie potentielle de pesanteur d'un objet de masse $m$ à l'altitude $z$.", 'reponse_correcte': "Epp = mgz", 'tolerances': ["mgh", "Epp = m × g × z", "m·g·z", "mgz"], 'explication': "$E_{pp} = mgz$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Quelle est la relation entre le travail du poids et la variation d'énergie potentielle ?", 'reponse_correcte': "W = −ΔEpp", 'tolerances': ["W = -delta Epp", "W(P) = -ΔEpp", "W = -(Epp(B) - Epp(A))"], 'explication': "$W(\\vec{P}) = -\\Delta E_{pp}$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Un objet de 4 kg est à 20 m du sol ($g = 10$ m·s⁻²). Calculer son énergie potentielle de pesanteur.", 'reponse_correcte': "800 J", 'tolerances': ["800", "800 joules", "800,0 J"], 'explication': "$E_{pp} = 4 \\times 10 \\times 20 = 800$ J.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Énergie mécanique et conservation',
                'duree': 35,
                'contenu': """# Énergie mécanique et conservation

## Définition

L'**énergie mécanique** d'un système est la somme de son énergie cinétique et de son énergie potentielle de pesanteur :

$$
E_m = E_c + E_{pp} = \\frac{1}{2} m v^2 + m g z
$$

---

## Conservation de l'énergie mécanique

Si un système n'est soumis qu'à des **forces conservatives** (poids) et à des forces qui ne travaillent pas (réaction normale) :

$$
E_m = \\text{constante} \\quad \\Leftrightarrow \\quad \\Delta E_m = 0
$$

### En chute libre

$$
\\frac{1}{2} m v_A^2 + m g z_A = \\frac{1}{2} m v_B^2 + m g z_B
$$

**Exemple :** Un objet lâché sans vitesse initiale de $h = 10$ m. Quelle est sa vitesse au sol ?

$$
m g h = \\frac{1}{2} m v^2 \\implies v = \\sqrt{2gh} = \\sqrt{2 \\times 9{,}81 \\times 10} \\approx 14 \\text{ m·s}^{-1}
$$

---

## Non-conservation de l'énergie mécanique

En présence de forces **non conservatives** (frottements) :

$$
\\Delta E_m = W_{nc}
$$

où $W_{nc}$ est le travail des forces non conservatives.

- Les frottements dissipent de l'énergie mécanique sous forme de **chaleur** (énergie thermique)
- $\\Delta E_m < 0$ : l'énergie mécanique diminue

---

## Diagramme d'énergie

Un diagramme représentant $E_c$, $E_{pp}$ et $E_m$ en fonction de la position ou du temps permet de visualiser les transferts d'énergie.

- En chute libre : quand $E_{pp}$ diminue, $E_c$ augmente d'autant
- Avec frottements : $E_m$ diminue progressivement

---
""",
                'quiz': {
                    'titre': 'Quiz — Énergie mécanique et conservation',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "L'énergie mécanique est la somme de :", 'options': ["L'énergie cinétique et l'énergie potentielle", "La masse et la vitesse", "La force et le déplacement", "La puissance et le temps"], 'reponse_correcte': '0', 'explication': "$E_m = E_c + E_{pp}$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "L'énergie mécanique se conserve quand le système est soumis uniquement à :", 'options': ["Des forces conservatives", "Des frottements", "Des forces quelconques", "Aucune force"], 'reponse_correcte': '0', 'explication': "$E_m$ se conserve si seules des forces conservatives travaillent.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "En chute libre, quand l'énergie potentielle diminue, l'énergie cinétique :", 'options': ["Augmente", "Diminue", "Reste constante", "S'annule"], 'reponse_correcte': '0', 'explication': "Conservation : $\\Delta E_c = -\\Delta E_{pp}$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Les frottements sont des forces :", 'options': ["Non conservatives", "Conservatives", "Nulles", "Gravitationnelles"], 'reponse_correcte': '0', 'explication': "Le travail des frottements dépend du chemin suivi : ce sont des forces non conservatives.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "En présence de frottements, l'énergie mécanique du système :", 'options': ["Diminue", "Augmente", "Reste constante", "S'annule instantanément"], 'reponse_correcte': '0', 'explication': "Les frottements dissipent de l'énergie mécanique sous forme de chaleur.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "L'énergie dissipée par les frottements se transforme en :", 'options': ["Énergie thermique (chaleur)", "Énergie potentielle", "Énergie cinétique", "Énergie nucléaire"], 'reponse_correcte': '0', 'explication': "Les frottements convertissent l'énergie mécanique en énergie thermique.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "L'unité de l'énergie mécanique est :", 'options': ["Le joule (J)", "Le watt (W)", "Le newton (N)", "Le mètre par seconde (m·s⁻¹)"], 'reponse_correcte': '0', 'explication': "Comme toute énergie, $E_m$ s'exprime en joules.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Au point le plus bas d'une chute libre (sol), l'énergie mécanique est :", 'options': ["Entièrement cinétique", "Entièrement potentielle", "Nulle", "Entièrement thermique"], 'reponse_correcte': '0', 'explication': "Au sol ($z=0$, référence), $E_{pp} = 0$ donc $E_m = E_c$.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Un objet de 2 kg est lâché sans vitesse de 20 m de haut. Sa vitesse au sol vaut ($g = 10$ m·s⁻²) :", 'options': ["20 m·s⁻¹", "10 m·s⁻¹", "14 m·s⁻¹", "40 m·s⁻¹"], 'reponse_correcte': '0', 'explication': "$v = \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 20} = 20$ m·s⁻¹.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "L'énergie mécanique d'un objet de 1 kg à 5 m du sol se déplaçant à 6 m·s⁻¹ vaut ($g = 10$ m·s⁻²) :", 'options': ["68 J", "50 J", "18 J", "56 J"], 'reponse_correcte': '0', 'explication': "$E_m = \\frac{1}{2} \\times 1 \\times 36 + 1 \\times 10 \\times 5 = 18 + 50 = 68$ J.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Un pendule oscille sans frottement. À la position la plus haute :", 'options': ["L'énergie potentielle est maximale et l'énergie cinétique est nulle", "L'énergie cinétique est maximale", "L'énergie mécanique est nulle", "Les deux énergies sont égales"], 'reponse_correcte': '0', 'explication': "En haut, la vitesse est nulle ($E_c = 0$) et $E_{pp}$ est maximale.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Avec des frottements, la variation d'énergie mécanique est égale à :", 'options': ["Le travail des forces non conservatives", "Zéro", "Le travail du poids", "L'énergie cinétique finale"], 'reponse_correcte': '0', 'explication': "$\\Delta E_m = W_{nc}$ : la variation est due aux forces non conservatives.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Un objet glisse sur un plan incliné avec frottements. Par rapport à la chute libre, sa vitesse au bas est :", 'options': ["Plus faible", "Plus grande", "Identique", "Nulle"], 'reponse_correcte': '0', 'explication': "Les frottements dissipent de l'énergie : la vitesse finale est plus faible qu'en chute libre.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Un objet lâché de 5 m atteint le sol à 8 m·s⁻¹ au lieu de 10 m·s⁻¹ (chute libre). L'énergie dissipée par les frottements vaut ($m = 1$ kg, $g = 10$ m·s⁻²) :", 'options': ["18 J", "50 J", "32 J", "10 J"], 'reponse_correcte': '0', 'explication': "$E_{dissipée} = mgh - \\frac{1}{2}mv^2 = 50 - 32 = 18$ J.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "L'énergie mécanique se conserve toujours.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Elle ne se conserve que si les forces non conservatives ne travaillent pas.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "En chute libre, la somme $E_c + E_{pp}$ reste constante.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "En chute libre, seul le poids (force conservative) travaille : $E_m$ est conservée.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Un diagramme d'énergie permet de visualiser les transferts entre énergie cinétique et potentielle.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "Le diagramme montre comment $E_c$ et $E_{pp}$ évoluent en fonction de la position.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner l'expression de l'énergie mécanique d'un système de masse $m$, de vitesse $v$ et à l'altitude $z$.", 'reponse_correcte': "Em = ½mv² + mgz", 'tolerances': ["Ec + Epp", "Em = (1/2)mv² + mgz", "½mv² + mgz", "Em = 0.5mv² + mgz"], 'explication': "$E_m = \\frac{1}{2}mv^2 + mgz$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Un objet est lâché sans vitesse initiale d'une hauteur $h$. Exprimer sa vitesse $v$ au sol en fonction de $g$ et $h$ (conservation de l'énergie mécanique).", 'reponse_correcte': "v = √(2gh)", 'tolerances': ["v = racine(2gh)", "sqrt(2gh)", "v = (2gh)^(1/2)"], 'explication': "Conservation : $mgh = \\frac{1}{2}mv^2 \\Rightarrow v = \\sqrt{2gh}$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "En présence de frottements, quelle relation relie la variation d'énergie mécanique au travail des forces non conservatives ?", 'reponse_correcte': "ΔEm = Wnc", 'tolerances': ["delta Em = Wnc", "ΔEm = travail des forces non conservatives", "Em(B) - Em(A) = Wnc"], 'explication': "$\\Delta E_m = W_{nc}$.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 6 — Aspects énergétiques de l'électricité
    # ──────────────────────────────────────────────
    {
        'ordre': 6,
        'titre': "Aspects énergétiques de l'électricité",
        'description': "Comprendre la puissance et l'énergie électriques, la loi de Joule et le bilan énergétique d'un circuit.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Puissance et énergie électrique',
                'duree': 35,
                'contenu': """# Puissance et énergie électrique

## Tension et intensité

- **Tension** $U$ (en volts, V) : différence de potentiel entre deux points d'un circuit
- **Intensité** $I$ (en ampères, A) : débit de charges électriques

---

## Puissance électrique

La **puissance** reçue par un dipôle parcouru par un courant $I$ sous une tension $U$ :

$$
P = U \\times I
$$

- $P$ en watts (W)
- $U$ en volts (V)
- $I$ en ampères (A)

---

## Énergie électrique

L'**énergie** consommée par un dipôle pendant une durée $\\Delta t$ :

$$
E = P \\times \\Delta t = U \\times I \\times \\Delta t
$$

- $E$ en joules (J) si $\\Delta t$ en secondes
- En pratique, on utilise le **kilowattheure** : 1 kWh = $3{,}6 \\times 10^6$ J

---

## Loi d'Ohm

Pour un conducteur ohmique (résistance $R$) :

$$
U = R \\times I
$$

La puissance dissipée par effet Joule :
$$
P = R I^2 = \\frac{U^2}{R}
$$

---

## Applications numériques

**Ampoule :** $P = 60$ W, $U = 230$ V

$$
I = \\frac{P}{U} = \\frac{60}{230} \\approx 0{,}26 \\text{ A}
$$

**Énergie consommée en 5 h :**
$$
E = 60 \\times 5 = 300 \\text{ Wh} = 0{,}3 \\text{ kWh}
$$

---
""",
                'quiz': {
                    'titre': 'Quiz — Puissance et énergie électrique',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "La puissance électrique est donnée par la relation :", 'options': ["P = U × I", "P = U / I", "P = U + I", "P = U − I"], 'reponse_correcte': '0', 'explication': "$P = U \\times I$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "L'unité de la puissance électrique est :", 'options': ["Le watt (W)", "Le joule (J)", "Le volt (V)", "L'ampère (A)"], 'reponse_correcte': '0', 'explication': "La puissance s'exprime en watts.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "La tension électrique se mesure en :", 'options': ["Volts (V)", "Ampères (A)", "Watts (W)", "Ohms (Ω)"], 'reponse_correcte': '0', 'explication': "La tension se mesure en volts.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "La loi d'Ohm s'écrit :", 'options': ["U = R × I", "U = R / I", "U = R + I", "U = R − I"], 'reponse_correcte': '0', 'explication': "La loi d'Ohm : $U = RI$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "1 kilowattheure (kWh) est égal à :", 'options': ["3,6 × 10⁶ J", "3600 J", "1000 J", "10⁶ J"], 'reponse_correcte': '0', 'explication': "1 kWh = $1000 \\times 3600 = 3{,}6 \\times 10^6$ J.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "L'énergie électrique consommée est donnée par :", 'options': ["E = P × Δt", "E = P / Δt", "E = P + Δt", "E = P − Δt"], 'reponse_correcte': '0', 'explication': "$E = P \\times \\Delta t = U \\times I \\times \\Delta t$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "L'intensité du courant se mesure en :", 'options': ["Ampères (A)", "Volts (V)", "Watts (W)", "Joules (J)"], 'reponse_correcte': '0', 'explication': "L'intensité se mesure en ampères.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "La résistance électrique se mesure en :", 'options': ["Ohms (Ω)", "Volts (V)", "Watts (W)", "Ampères (A)"], 'reponse_correcte': '0', 'explication': "La résistance se mesure en ohms (Ω).", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "La puissance dissipée par une résistance de 100 Ω traversée par un courant de 2 A vaut :", 'options': ["400 W", "200 W", "50 W", "800 W"], 'reponse_correcte': '0', 'explication': "$P = RI^2 = 100 \\times 4 = 400$ W.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Une ampoule de 60 W fonctionne sous 230 V. L'intensité du courant vaut environ :", 'options': ["0,26 A", "2,6 A", "26 A", "0,026 A"], 'reponse_correcte': '0', 'explication': "$I = P/U = 60/230 \\approx 0{,}26$ A.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Un appareil de 2000 W fonctionne pendant 3 heures. L'énergie consommée est :", 'options': ["6 kWh", "6000 kWh", "2 kWh", "3 kWh"], 'reponse_correcte': '0', 'explication': "$E = 2000 \\times 3 = 6000$ Wh $= 6$ kWh.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "La puissance dissipée par une résistance de 50 Ω sous une tension de 100 V vaut :", 'options': ["200 W", "5000 W", "50 W", "100 W"], 'reponse_correcte': '0', 'explication': "$P = U^2/R = 10000/50 = 200$ W.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Si on double la résistance d'un conducteur ohmique à tension constante, la puissance dissipée est :", 'options': ["Divisée par 2", "Multipliée par 2", "Multipliée par 4", "Inchangée"], 'reponse_correcte': '0', 'explication': "$P = U^2/R$ : si $R$ double, $P$ est divisée par 2.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Si on double l'intensité dans une résistance, la puissance dissipée par effet Joule est :", 'options': ["Multipliée par 4", "Multipliée par 2", "Inchangée", "Divisée par 2"], 'reponse_correcte': '0', 'explication': "$P = RI^2$ : si $I$ double, $P$ est multipliée par $2^2 = 4$.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Le kilowattheure est une unité de puissance.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Le kWh est une unité d'énergie (puissance × temps).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "La loi d'Ohm ne s'applique qu'aux conducteurs ohmiques.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "$U = RI$ n'est valable que pour les conducteurs ohmiques (résistances).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "La puissance consommée par un appareil dépend uniquement de la tension.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "$P = UI$ : la puissance dépend à la fois de la tension et de l'intensité.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner les deux expressions de la puissance dissipée par effet Joule dans une résistance $R$.", 'reponse_correcte': "P = RI² et P = U²/R", 'tolerances': ["RI² et U²/R", "P=RI2 et P=U2/R", "RI^2 et U^2/R"], 'explication': "$P = RI^2 = U^2/R$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Convertir 5 kWh en joules.", 'reponse_correcte': "18 × 10⁶ J", 'tolerances': ["18000000 J", "1,8 × 10⁷ J", "18 000 000 J", "18 MJ"], 'explication': "$5 \\times 3{,}6 \\times 10^6 = 18 \\times 10^6$ J.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Quelle est la loi d'Ohm pour un conducteur ohmique de résistance $R$ ?", 'reponse_correcte': "U = RI", 'tolerances': ["U = R × I", "U=R·I", "U = R.I"], 'explication': "$U = R \\times I$.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Bilan énergétique et rendement',
                'duree': 35,
                'contenu': """# Bilan énergétique et rendement d'un circuit

## Effet Joule

Tout conducteur ohmique transforme l'énergie électrique en **énergie thermique** (chaleur). C'est l'**effet Joule**.

$$
Q = R I^2 \\Delta t
$$

### Applications utiles

- Chauffage électrique, grille-pain, sèche-cheveux
- Lampes à incandescence

### Applications indésirables

- Échauffement des câbles électriques → pertes d'énergie
- Nécessité de refroidir les composants électroniques

---

## Bilan énergétique d'un circuit

### Générateur

Un générateur fournit de l'énergie au circuit. Sa puissance utile :

$$
P_{utile} = U_{borne} \\times I
$$

Sa puissance totale inclut les pertes internes :

$$
P_{totale} = (U_{borne} + r \\times I) \\times I = \\varepsilon \\times I
$$

où $\\varepsilon$ est la force électromotrice et $r$ la résistance interne.

### Récepteur

Un récepteur reçoit l'énergie du circuit et la convertit (mouvement, lumière, chaleur…).

---

## Rendement

Le **rendement** $\\eta$ d'un convertisseur d'énergie :

$$
\\eta = \\frac{P_{utile}}{P_{totale}} = \\frac{E_{utile}}{E_{totale}}
$$

- $0 \\leq \\eta \\leq 1$ (souvent exprimé en %)
- $\\eta = 1$ : conversion idéale (impossible en pratique)

**Exemple :** un moteur électrique reçoit $P = 500$ W et fournit $P_{utile} = 400$ W :
$$
\\eta = \\frac{400}{500} = 0{,}80 = 80\\%
$$

Les $100$ W de pertes sont dissipés par effet Joule.

---
""",
                'quiz': {
                    'titre': 'Quiz — Bilan énergétique et rendement',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "L'effet Joule est la transformation d'énergie électrique en :", 'options': ["Énergie thermique", "Énergie cinétique", "Énergie potentielle", "Énergie nucléaire"], 'reponse_correcte': '0', 'explication': "L'effet Joule convertit l'énergie électrique en chaleur.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Le rendement d'un convertisseur est toujours :", 'options': ["Inférieur ou égal à 1", "Supérieur à 1", "Égal à 1", "Négatif"], 'reponse_correcte': '0', 'explication': "$\\eta = P_{utile}/P_{totale} \\leq 1$ car on ne peut pas créer d'énergie.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Le rendement est le rapport :", 'options': ["Puissance utile / Puissance totale", "Puissance totale / Puissance utile", "Énergie − pertes", "Force × vitesse"], 'reponse_correcte': '0', 'explication': "$\\eta = P_{utile} / P_{totale}$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "L'énergie dissipée par effet Joule dans une résistance $R$ pendant $\\Delta t$ est :", 'options': ["Q = RI²Δt", "Q = RIΔt", "Q = RI²", "Q = R/I²Δt"], 'reponse_correcte': '0', 'explication': "$Q = RI^2\\Delta t$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Un générateur fournit de l'énergie au circuit grâce à sa :", 'options': ["Force électromotrice (f.é.m.)", "Résistance interne", "Puissance dissipée", "Tension de seuil"], 'reponse_correcte': '0', 'explication': "La f.é.m. $\\varepsilon$ caractérise la capacité du générateur à fournir de l'énergie.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Un rendement de 80 % signifie que :", 'options': ["80 % de l'énergie reçue est convertie utilement", "20 % de l'énergie est utile", "L'appareil ne consomme que 80 J", "80 W sont dissipés"], 'reponse_correcte': '0', 'explication': "$\\eta = 80\\%$ : 80 % de l'énergie consommée est utile.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "La résistance interne d'un générateur provoque :", 'options': ["Des pertes par effet Joule", "Une augmentation de la tension", "Une diminution du courant à zéro", "Une conversion en énergie potentielle"], 'reponse_correcte': '0', 'explication': "La résistance interne $r$ entraîne des pertes $rI^2$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Le chauffage électrique est un exemple d'effet Joule :", 'options': ["Utile", "Indésirable", "Nul", "Impossible"], 'reponse_correcte': '0', 'explication': "Dans un radiateur, l'effet Joule est volontairement utilisé pour chauffer.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Un moteur reçoit 600 W et fournit 450 W utiles. Son rendement est :", 'options': ["75 %", "133 %", "25 %", "50 %"], 'reponse_correcte': '0', 'explication': "$\\eta = 450/600 = 0{,}75 = 75\\%$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Un générateur de f.é.m. $\\varepsilon = 12$ V et de résistance interne $r = 1$ Ω débite $I = 2$ A. La tension aux bornes vaut :", 'options': ["10 V", "12 V", "14 V", "8 V"], 'reponse_correcte': '0', 'explication': "$U = \\varepsilon - rI = 12 - 1 \\times 2 = 10$ V.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Les pertes par effet Joule dans un câble de résistance 0,5 Ω traversé par 10 A pendant 1 h valent :", 'options': ["180 000 J", "50 J", "5 000 J", "500 J"], 'reponse_correcte': '0', 'explication': "$Q = RI^2\\Delta t = 0{,}5 \\times 100 \\times 3600 = 180\\,000$ J.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Pour transporter la même puissance avec moins de pertes, on augmente :", 'options': ["La tension", "L'intensité", "La résistance du câble", "La longueur du câble"], 'reponse_correcte': '0', 'explication': "$P_{pertes} = RI^2$ : augmenter $U$ permet de diminuer $I$ à puissance constante ($P=UI$).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Un appareil de rendement 90 % consomme 1000 W. La puissance perdue vaut :", 'options': ["100 W", "900 W", "1000 W", "10 W"], 'reponse_correcte': '0', 'explication': "$P_{perdue} = P_{totale} - P_{utile} = 1000 - 900 = 100$ W.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "La puissance totale fournie par un générateur de f.é.m. $\\varepsilon$ débitant un courant $I$ est :", 'options': ["εI", "εI²", "ε/I", "ε²I"], 'reponse_correcte': '0', 'explication': "$P_{totale} = \\varepsilon \\times I$.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Un rendement de 100 % est réalisable en pratique.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "En pratique, il y a toujours des pertes (effet Joule, frottements, etc.).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "L'effet Joule est toujours indésirable.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "L'effet Joule est utile dans les appareils de chauffage.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Augmenter la tension de transport de l'électricité permet de réduire les pertes en ligne.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "À puissance constante, augmenter $U$ diminue $I$, donc $P_{pertes} = RI^2$ diminue.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner l'expression du rendement $\\eta$ d'un convertisseur d'énergie.", 'reponse_correcte': "η = Putile / Ptotale", 'tolerances': ["η = Pu/Pt", "rendement = puissance utile / puissance totale", "η = Eu/Et", "Putile/Ptotale"], 'explication': "$\\eta = \\frac{P_{utile}}{P_{totale}}$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Donner l'expression de la tension aux bornes d'un générateur de f.é.m. $\\varepsilon$ et de résistance interne $r$ débitant un courant $I$.", 'reponse_correcte': "U = ε − rI", 'tolerances': ["U = ε - rI", "U = E - rI", "U = fem - rI", "ε − rI"], 'explication': "$U = \\varepsilon - rI$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Un moteur de rendement 75 % reçoit 800 W. Quelle est sa puissance utile ?", 'reponse_correcte': "600 W", 'tolerances': ["600", "600 watts", "600,0 W"], 'explication': "$P_{utile} = \\eta \\times P_{totale} = 0{,}75 \\times 800 = 600$ W.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 7 — Ondes mécaniques
    # ──────────────────────────────────────────────
    {
        'ordre': 7,
        'titre': 'Ondes mécaniques',
        'description': "Comprendre la propagation des ondes mécaniques, leur célérité et leurs propriétés.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Propagation des ondes mécaniques',
                'duree': 35,
                'contenu': """# Propagation des ondes mécaniques

## Définition

Une **onde mécanique** est la propagation d'une perturbation dans un milieu matériel, **sans transport de matière**, mais avec transport d'énergie.

---

## Conditions de propagation

- Nécessite un **milieu matériel** (solide, liquide ou gaz)
- Ne se propage **pas dans le vide**
- La matière oscille autour de sa position d'équilibre puis y revient

---

## Types d'ondes

### Onde transversale

La perturbation est **perpendiculaire** à la direction de propagation.

> **Exemples :** vagues à la surface de l'eau, onde le long d'une corde

### Onde longitudinale

La perturbation est **parallèle** à la direction de propagation.

> **Exemples :** ondes sonores, ondes de compression dans un ressort

---

## Célérité

La **célérité** $v$ est la vitesse de propagation de l'onde :

$$
v = \\frac{d}{\\tau}
$$

- $d$ : distance parcourue par l'onde (m)
- $\\tau$ : durée (retard) de propagation (s)
- $v$ en m·s⁻¹

### Facteurs influençant la célérité

La célérité dépend du **milieu** et de ses propriétés (élasticité, densité, température).

| Milieu | Célérité du son |
|---|---|
| Air (20°C) | $\\approx 340$ m·s⁻¹ |
| Eau | $\\approx 1500$ m·s⁻¹ |
| Acier | $\\approx 5000$ m·s⁻¹ |

---

## Retard

Le **retard** $\\tau$ est le temps mis par la perturbation pour atteindre un point situé à la distance $d$ :

$$
\\tau = \\frac{d}{v}
$$

---
""",
                'quiz': {
                    'titre': 'Quiz — Propagation des ondes mécaniques',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Une onde mécanique nécessite pour se propager :", 'options': ["Un milieu matériel", "Le vide", "De la lumière", "Un champ magnétique"], 'reponse_correcte': '0', 'explication': "Une onde mécanique ne se propage que dans un milieu matériel (solide, liquide ou gaz).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Une onde mécanique transporte :", 'options': ["De l'énergie sans matière", "De la matière", "Du vide", "Des particules chargées"], 'reponse_correcte': '0', 'explication': "Une onde mécanique transporte de l'énergie sans transport de matière.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Une onde transversale se caractérise par une perturbation :", 'options': ["Perpendiculaire à la direction de propagation", "Parallèle à la direction de propagation", "Circulaire", "Nulle"], 'reponse_correcte': '0', 'explication': "Dans une onde transversale, la perturbation est perpendiculaire à la direction de propagation.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Les ondes sonores sont des ondes :", 'options': ["Longitudinales", "Transversales", "Électromagnétiques", "Lumineuses"], 'reponse_correcte': '0', 'explication': "Le son est une onde longitudinale : la perturbation est parallèle à la propagation.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "La célérité d'une onde se mesure en :", 'options': ["m·s⁻¹", "kg", "Hz", "N"], 'reponse_correcte': '0', 'explication': "La célérité est une vitesse et s'exprime en mètres par seconde.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "La célérité du son dans l'air à 20 °C est environ :", 'options': ["340 m·s⁻¹", "1500 m·s⁻¹", "5000 m·s⁻¹", "3 × 10⁸ m·s⁻¹"], 'reponse_correcte': '0', 'explication': "La vitesse du son dans l'air à 20 °C vaut environ 340 m·s⁻¹.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Une vague à la surface de l'eau est une onde :", 'options': ["Transversale", "Longitudinale", "Électromagnétique", "Stationnaire"], 'reponse_correcte': '0', 'explication': "Les vagues sont des ondes transversales : la surface oscille verticalement tandis que l'onde se propage horizontalement.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Le retard τ correspond au temps mis par la perturbation pour :", 'options': ["Atteindre un point donné", "Revenir à sa source", "Disparaître", "Changer de fréquence"], 'reponse_correcte': '0', 'explication': "Le retard est le temps de propagation entre la source et un point donné.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "La célérité du son est la plus grande dans :", 'options': ["L'acier", "L'eau", "L'air", "Le vide"], 'reponse_correcte': '0', 'explication': "Le son se propage plus vite dans les solides rigides : environ 5000 m·s⁻¹ dans l'acier.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Un séisme arrive à une station à 340 km avec un retard de 100 s. La célérité vaut :", 'options': ["3400 m·s⁻¹", "340 m·s⁻¹", "34 000 m·s⁻¹", "34 m·s⁻¹"], 'reponse_correcte': '0', 'explication': "$v = d/\\tau = 340\\,000 / 100 = 3400$ m·s⁻¹.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "La célérité d'une onde mécanique dépend principalement :", 'options': ["Du milieu de propagation", "De l'amplitude de l'onde", "De la couleur de l'onde", "De la fréquence uniquement"], 'reponse_correcte': '0', 'explication': "La célérité dépend des propriétés du milieu (élasticité, densité, température).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Deux microphones distants de 1,70 m captent un son avec un retard de 5,0 ms. La célérité est :", 'options': ["340 m·s⁻¹", "170 m·s⁻¹", "1500 m·s⁻¹", "34 m·s⁻¹"], 'reponse_correcte': '0', 'explication': "$v = d/\\tau = 1{,}70 / 0{,}005 = 340$ m·s⁻¹.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Le son ne se propage pas dans :", 'options': ["Le vide", "L'eau", "L'acier", "Le béton"], 'reponse_correcte': '0', 'explication': "Le son est une onde mécanique : il nécessite un milieu matériel et ne se propage pas dans le vide.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Dans un milieu plus dense et plus rigide, la célérité du son est généralement :", 'options': ["Plus grande", "Plus petite", "Identique", "Nulle"], 'reponse_correcte': '0', 'explication': "La rigidité favorise la transmission rapide des vibrations : la célérité augmente.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Une onde mécanique peut se propager dans le vide.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Une onde mécanique nécessite un milieu matériel ; elle ne se propage pas dans le vide.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Lors de la propagation d'une onde sonore, les molécules d'air se déplacent de la source au récepteur.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Les molécules oscillent autour de leur position d'équilibre : il n'y a pas de transport de matière.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "La célérité du son dans l'eau est supérieure à celle dans l'air.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "Le son se propage à environ 1500 m·s⁻¹ dans l'eau contre 340 m·s⁻¹ dans l'air.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner l'expression du retard τ en fonction de la distance d et de la célérité v.", 'reponse_correcte': 'τ = d/v', 'tolerances': ['τ=d/v', 't = d/v', 'tau = d/v'], 'explication': "$\\tau = d / v$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Donner l'expression de la célérité v en fonction de la distance d et du retard τ.", 'reponse_correcte': 'v = d/τ', 'tolerances': ['v=d/τ', 'v = d/t', 'v=d/t'], 'explication': "$v = d / \\tau$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Comment appelle-t-on une onde dont la perturbation est parallèle à la direction de propagation ?", 'reponse_correcte': 'onde longitudinale', 'tolerances': ['longitudinale', 'une onde longitudinale'], 'explication': "Une onde longitudinale a une perturbation parallèle à sa direction de propagation.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': "Ondes périodiques et longueur d'onde",
                'duree': 35,
                'contenu': """# Ondes périodiques et longueur d'onde

## Onde progressive périodique

Une onde est **périodique** si la source vibre de façon répétitive. Si la vibration est sinusoïdale, l'onde est dite **sinusoïdale** ou **harmonique**.

---

## Période et fréquence

- **Période** $T$ : durée d'un cycle complet (s)
- **Fréquence** $f$ : nombre de cycles par seconde (Hz)

$$
f = \\frac{1}{T}
$$

---

## Longueur d'onde

La **longueur d'onde** $\\lambda$ est la distance parcourue par l'onde pendant une période :

$$
\\lambda = v \\times T = \\frac{v}{f}
$$

- $\\lambda$ en mètres (m)
- C'est aussi la distance entre deux points consécutifs en phase

---

## Double périodicité

Une onde sinusoïdale présente une **double périodicité** :
- **Temporelle** : à un point fixe, le mouvement se répète avec la période $T$
- **Spatiale** : à un instant donné, le motif se répète avec la longueur d'onde $\\lambda$

---

## Exemples

**Onde sonore :** fréquence $f = 440$ Hz (La₃), célérité $v = 340$ m·s⁻¹

$$
\\lambda = \\frac{340}{440} = 0{,}77 \\text{ m}
$$

**Onde à la surface de l'eau :** $T = 0{,}5$ s, $v = 2$ m·s⁻¹

$$
\\lambda = 2 \\times 0{,}5 = 1{,}0 \\text{ m}
$$

---

## Phénomène de diffraction (introduction)

Lorsqu'une onde rencontre un obstacle ou une ouverture de dimension comparable à sa longueur d'onde, elle se **diffracte** : la direction de propagation est modifiée.

- Plus l'ouverture est petite par rapport à $\\lambda$, plus la diffraction est marquée
- Ce phénomène prouve la nature ondulatoire

---
""",
                'quiz': {
                    'titre': "Quiz — Ondes périodiques et longueur d'onde",
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "La période T d'une onde périodique est :", 'options': ["La durée d'un cycle complet", "La distance entre deux crêtes", "La vitesse de l'onde", "Le nombre de cycles par seconde"], 'reponse_correcte': '0', 'explication': "La période est la durée d'un cycle complet de la vibration.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "La fréquence f se mesure en :", 'options': ["Hertz (Hz)", "Mètres (m)", "Secondes (s)", "Newtons (N)"], 'reponse_correcte': '0', 'explication': "La fréquence s'exprime en hertz (Hz).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "La longueur d'onde λ représente :", 'options': ["La distance parcourue par l'onde pendant une période", "La durée d'un cycle", "La vitesse de l'onde", "Le nombre de cycles"], 'reponse_correcte': '0', 'explication': "La longueur d'onde est la distance parcourue pendant une période $T$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "La relation entre fréquence et période est :", 'options': ["f = 1/T", "f = T", "f = T²", "f = 2T"], 'reponse_correcte': '0', 'explication': "$f = 1/T$ : la fréquence est l'inverse de la période.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Une onde sinusoïdale est une onde :", 'options': ["Périodique à vibration sinusoïdale", "Non périodique", "Qui ne se propage pas", "Toujours amortie"], 'reponse_correcte': '0', 'explication': "Une onde sinusoïdale (ou harmonique) est périodique avec une vibration en sinus.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "La longueur d'onde s'exprime en :", 'options': ["Mètres (m)", "Hertz (Hz)", "Secondes (s)", "Watts (W)"], 'reponse_correcte': '0', 'explication': "La longueur d'onde est une distance et s'exprime en mètres.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Deux points séparés d'une longueur d'onde λ sont :", 'options': ["En phase", "En opposition de phase", "Au repos", "Immobiles"], 'reponse_correcte': '0', 'explication': "Deux points distants de λ vibrent exactement de la même façon : ils sont en phase.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "La double périodicité d'une onde signifie qu'elle est périodique :", 'options': ["Dans le temps et dans l'espace", "Uniquement dans le temps", "Uniquement dans l'espace", "Ni dans le temps ni dans l'espace"], 'reponse_correcte': '0', 'explication': "L'onde est périodique temporellement (période $T$) et spatialement (longueur d'onde $\\lambda$).", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Une onde sonore de fréquence 440 Hz se propage à 340 m·s⁻¹. Sa longueur d'onde vaut environ :", 'options': ["0,77 m", "7,7 m", "0,077 m", "77 m"], 'reponse_correcte': '0', 'explication': "$\\lambda = v/f = 340/440 \\approx 0{,}77$ m.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "La longueur d'onde λ est donnée par :", 'options': ["λ = v/f", "λ = f/v", "λ = v × f", "λ = v + f"], 'reponse_correcte': '0', 'explication': "$\\lambda = v / f = v \\times T$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Si la fréquence d'une onde double et la célérité reste constante, la longueur d'onde :", 'options': ["Est divisée par 2", "Est multipliée par 2", "Reste la même", "Est divisée par 4"], 'reponse_correcte': '0', 'explication': "$\\lambda = v/f$ : si $f$ double, $\\lambda$ est divisée par 2.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Une onde a une période T = 0,5 s et une célérité v = 2 m·s⁻¹. Sa longueur d'onde vaut :", 'options': ["1,0 m", "0,25 m", "4,0 m", "0,5 m"], 'reponse_correcte': '0', 'explication': "$\\lambda = v \\times T = 2 \\times 0{,}5 = 1{,}0$ m.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Le phénomène de diffraction est d'autant plus marqué que :", 'options': ["L'ouverture est petite par rapport à λ", "L'ouverture est grande par rapport à λ", "La fréquence est très faible", "La célérité augmente"], 'reponse_correcte': '0', 'explication': "La diffraction est maximale quand la dimension de l'ouverture est de l'ordre de λ ou plus petite.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "La fréquence d'une onde de période T = 2 ms est :", 'options': ["500 Hz", "2000 Hz", "50 Hz", "200 Hz"], 'reponse_correcte': '0', 'explication': "$f = 1/T = 1/0{,}002 = 500$ Hz.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "La fréquence d'une onde dépend du milieu de propagation.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "La fréquence est fixée par la source ; elle ne dépend pas du milieu.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "La longueur d'onde dépend à la fois de la célérité et de la fréquence.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "$\\lambda = v / f$ : elle dépend de la célérité et de la fréquence.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "La diffraction prouve la nature ondulatoire d'un phénomène.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "Seules les ondes peuvent être diffractées : c'est une preuve de la nature ondulatoire.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner l'expression de la longueur d'onde λ en fonction de la célérité v et de la période T.", 'reponse_correcte': 'λ = v × T', 'tolerances': ['λ = vT', 'λ=v×T', 'lambda = v × T'], 'explication': "$\\lambda = v \\times T$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Donner l'expression de la longueur d'onde λ en fonction de la célérité v et de la fréquence f.", 'reponse_correcte': 'λ = v/f', 'tolerances': ['λ=v/f', 'lambda = v/f', 'lambda=v/f'], 'explication': "$\\lambda = v / f$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Comment appelle-t-on la périodicité spatiale d'une onde sinusoïdale ?", 'reponse_correcte': "longueur d'onde", 'tolerances': ["la longueur d'onde", 'λ', 'longueur donde'], 'explication': "La longueur d'onde $\\lambda$ est la période spatiale de l'onde.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 8 — Modèles de la lumière
    # ──────────────────────────────────────────────
    {
        'ordre': 8,
        'titre': 'Modèles de la lumière',
        'description': "Comprendre la dualité onde-corpuscule de la lumière, le modèle ondulatoire et le photon.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Modèle ondulatoire de la lumière',
                'duree': 35,
                'contenu': """# Modèle ondulatoire de la lumière

## La lumière est une onde électromagnétique

Contrairement aux ondes mécaniques, la lumière se propage **dans le vide** et dans les milieux transparents. C'est une **onde électromagnétique** : oscillation couplée d'un champ électrique et d'un champ magnétique.

---

## Vitesse de la lumière

Dans le vide :
$$
c = 3{,}00 \\times 10^8 \\text{ m·s}^{-1}
$$

Dans un milieu transparent d'indice de réfraction $n$ :
$$
v = \\frac{c}{n}
$$

| Milieu | Indice $n$ |
|---|---|
| Vide | $1{,}000$ |
| Air | $\\approx 1{,}000$ |
| Eau | $1{,}33$ |
| Verre | $1{,}5$ à $1{,}9$ |

---

## Spectre électromagnétique

La lumière visible n'est qu'une petite partie du spectre électromagnétique :

| Domaine | Longueur d'onde |
|---|---|
| Rayons gamma | $< 10^{-12}$ m |
| Rayons X | $10^{-12}$ à $10^{-8}$ m |
| Ultraviolets | $10^{-8}$ à $4 \\times 10^{-7}$ m |
| **Visible** | $400$ nm (violet) à $800$ nm (rouge) |
| Infrarouge | $8 \\times 10^{-7}$ à $10^{-3}$ m |
| Micro-ondes | $10^{-3}$ à $1$ m |
| Ondes radio | $> 1$ m |

---

## Relation fondamentale

Pour toute onde électromagnétique :

$$
\\lambda = \\frac{c}{f}
$$

ou dans un milieu d'indice $n$ :

$$
\\lambda_{milieu} = \\frac{\\lambda_0}{n}
$$

---

## Diffraction de la lumière

La lumière peut être **diffractée** par une fente ou un obstacle de dimensions comparables à sa longueur d'onde. Ce phénomène prouve sa nature ondulatoire.

L'angle de diffraction pour une fente de largeur $a$ :
$$
\\theta \\approx \\frac{\\lambda}{a}
$$

---
""",
                'quiz': {
                    'titre': 'Quiz — Modèle ondulatoire de la lumière',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "La lumière est une onde :", 'options': ["Électromagnétique", "Mécanique", "Sonore", "Sismique"], 'reponse_correcte': '0', 'explication': "La lumière est une onde électromagnétique : elle n'a pas besoin de milieu matériel.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "La vitesse de la lumière dans le vide vaut environ :", 'options': ["3 × 10⁸ m·s⁻¹", "340 m·s⁻¹", "1500 m·s⁻¹", "3 × 10⁶ m·s⁻¹"], 'reponse_correcte': '0', 'explication': "$c = 3{,}00 \\times 10^8$ m·s⁻¹ dans le vide.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Le domaine visible du spectre électromagnétique va de :", 'options': ["400 à 800 nm", "100 à 200 nm", "1 à 10 mm", "10 à 100 m"], 'reponse_correcte': '0', 'explication': "La lumière visible s'étend d'environ 400 nm (violet) à 800 nm (rouge).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "L'indice de réfraction du vide vaut :", 'options': ["1", "0", "1,33", "1,5"], 'reponse_correcte': '0', 'explication': "Par définition, l'indice de réfraction du vide est 1.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Contrairement au son, la lumière peut se propager :", 'options': ["Dans le vide", "Uniquement dans l'eau", "Uniquement dans les solides", "Jamais dans les gaz"], 'reponse_correcte': '0', 'explication': "La lumière est une onde électromagnétique qui se propage dans le vide.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "L'indice de réfraction de l'eau est environ :", 'options': ["1,33", "1,00", "2,00", "0,75"], 'reponse_correcte': '0', 'explication': "L'indice de réfraction de l'eau vaut environ 1,33.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Les ultraviolets ont des longueurs d'onde :", 'options': ["Plus courtes que le visible", "Plus longues que le visible", "Identiques au visible", "Nulles"], 'reponse_correcte': '0', 'explication': "Les UV ont des longueurs d'onde inférieures à 400 nm, plus courtes que le visible.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Un prisme permet de réaliser :", 'options': ["La dispersion de la lumière blanche", "La compression de la lumière", "L'amplification de la lumière", "L'absorption totale"], 'reponse_correcte': '0', 'explication': "Un prisme sépare les différentes longueurs d'onde : c'est la dispersion.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "La relation entre longueur d'onde λ et fréquence f dans le vide est :", 'options': ["λ = c/f", "λ = c × f", "λ = f/c", "λ = c + f"], 'reponse_correcte': '0', 'explication': "$\\lambda = c / f$ dans le vide.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "La vitesse de la lumière dans un milieu d'indice n = 1,5 vaut :", 'options': ["2,0 × 10⁸ m·s⁻¹", "4,5 × 10⁸ m·s⁻¹", "3,0 × 10⁸ m·s⁻¹", "1,5 × 10⁸ m·s⁻¹"], 'reponse_correcte': '0', 'explication': "$v = c/n = 3{,}0 \\times 10^8 / 1{,}5 = 2{,}0 \\times 10^8$ m·s⁻¹.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "La longueur d'onde dans un milieu d'indice n par rapport au vide est :", 'options': ["λ_milieu = λ₀/n", "λ_milieu = λ₀ × n", "λ_milieu = λ₀", "λ_milieu = λ₀ + n"], 'reponse_correcte': '0', 'explication': "$\\lambda_{milieu} = \\lambda_0 / n$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "L'angle de diffraction θ par une fente de largeur a est donné par :", 'options': ["θ ≈ λ/a", "θ ≈ a/λ", "θ ≈ λ × a", "θ ≈ a²/λ"], 'reponse_correcte': '0', 'explication': "$\\theta \\approx \\lambda / a$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Une lumière de 600 nm dans le vide a dans le verre (n = 1,5) une longueur d'onde de :", 'options': ["400 nm", "900 nm", "600 nm", "300 nm"], 'reponse_correcte': '0', 'explication': "$\\lambda = 600/1{,}5 = 400$ nm.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Les micro-ondes ont des longueurs d'onde de l'ordre de :", 'options': ["10⁻³ à 1 m", "10⁻¹² à 10⁻⁸ m", "400 à 800 nm", "Supérieures à 1 m"], 'reponse_correcte': '0', 'explication': "Les micro-ondes couvrent le domaine de 10⁻³ m à 1 m environ.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "La fréquence de la lumière change quand elle passe d'un milieu à un autre.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Lors d'un changement de milieu, c'est la longueur d'onde qui varie, pas la fréquence.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "La diffraction de la lumière prouve sa nature ondulatoire.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "La diffraction est un phénomène typiquement ondulatoire.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Les ondes radio ont des longueurs d'onde plus courtes que la lumière visible.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Les ondes radio ont des longueurs d'onde bien plus longues (> 1 m) que le visible (400–800 nm).", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner la relation entre la vitesse de la lumière dans un milieu, la vitesse dans le vide et l'indice de réfraction.", 'reponse_correcte': 'v = c/n', 'tolerances': ['v=c/n', 'c/n', 'v = c / n'], 'explication': "$v = c / n$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Donner la relation entre la longueur d'onde λ, la fréquence f et la vitesse c dans le vide.", 'reponse_correcte': 'λ = c/f', 'tolerances': ['c = λf', 'c = λ × f', 'λ=c/f'], 'explication': "$\\lambda = c / f$ ou $c = \\lambda f$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Quel est le domaine de longueur d'onde de la lumière visible (en nm) ?", 'reponse_correcte': '400 à 800 nm', 'tolerances': ['400-800 nm', '400 nm à 800 nm', 'de 400 à 800 nm'], 'explication': "Le visible s'étend d'environ 400 nm (violet) à 800 nm (rouge).", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Le photon et la dualité onde-corpuscule',
                'duree': 35,
                'contenu': """# Le photon et la dualité onde-corpuscule

## Le photon

La lumière peut aussi être décrite comme un flux de particules appelées **photons**. Chaque photon transporte une énergie :

$$
E = h \\nu = \\frac{hc}{\\lambda}
$$

- $h = 6{,}63 \\times 10^{-34}$ J·s (constante de Planck)
- $\\nu$ : fréquence de la lumière (Hz)
- $\\lambda$ : longueur d'onde (m)

---

## Énergie en électron-volt

L'**électron-volt** (eV) est une unité d'énergie adaptée à l'échelle atomique :

$$
1 \\text{ eV} = 1{,}6 \\times 10^{-19} \\text{ J}
$$

**Exemple :** Lumière verte ($\\lambda = 550$ nm) :
$$
E = \\frac{6{,}63 \\times 10^{-34} \\times 3{,}00 \\times 10^8}{550 \\times 10^{-9}} = 3{,}62 \\times 10^{-19} \\text{ J} \\approx 2{,}26 \\text{ eV}
$$

---

## Effet photoélectrique

L'**effet photoélectrique** est l'éjection d'électrons d'une surface métallique éclairée par de la lumière.

### Observations

- L'effet ne se produit que si la fréquence $\\nu$ dépasse un seuil $\\nu_0$ (indépendant de l'intensité)
- Au-dessus du seuil, le nombre d'électrons éjectés est proportionnel à l'intensité lumineuse

### Explication par le modèle corpusculaire

Chaque photon cède son énergie $E = h\\nu$ à un électron. L'éjection n'est possible que si $E \\geq W$ (travail d'extraction).

$$
E_c = h\\nu - W
$$

Ce phénomène ne peut **pas** être expliqué par le modèle ondulatoire seul.

---

## Dualité onde-corpuscule

La lumière possède à la fois des propriétés **ondulatoires** (diffraction, interférences) et **corpusculaires** (effet photoélectrique).

| Phénomène | Modèle |
|---|---|
| Propagation, diffraction, interférences | Ondulatoire |
| Effet photoélectrique, émission/absorption | Corpusculaire |

> **Conclusion :** la lumière n'est ni une onde classique, ni un flux de particules classiques. Elle possède les deux aspects selon l'expérience réalisée.

---
""",
                'quiz': {
                    'titre': 'Quiz — Le photon et la dualité onde-corpuscule',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Le photon est :", 'options': ["Une particule de lumière", "Un atome", "Un électron", "Un proton"], 'reponse_correcte': '0', 'explication': "Le photon est le quantum d'énergie lumineuse, la particule associée à la lumière.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "La constante de Planck h vaut environ :", 'options': ["6,63 × 10⁻³⁴ J·s", "3,00 × 10⁸ J·s", "1,6 × 10⁻¹⁹ J·s", "9,81 J·s"], 'reponse_correcte': '0', 'explication': "$h = 6{,}63 \\times 10^{-34}$ J·s.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "L'énergie d'un photon est donnée par :", 'options': ["E = hν", "E = mc²", "E = mv²/2", "E = mgh"], 'reponse_correcte': '0', 'explication': "$E = h\\nu$ où $h$ est la constante de Planck et $\\nu$ la fréquence.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Un électron-volt (eV) vaut :", 'options': ["1,6 × 10⁻¹⁹ J", "6,63 × 10⁻³⁴ J", "3,0 × 10⁸ J", "9,81 J"], 'reponse_correcte': '0', 'explication': "$1$ eV $= 1{,}6 \\times 10^{-19}$ J.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "L'effet photoélectrique est :", 'options': ["L'éjection d'électrons d'un métal par la lumière", "La déviation de la lumière par un prisme", "La réflexion de la lumière", "L'absorption de chaleur"], 'reponse_correcte': '0', 'explication': "L'effet photoélectrique est l'émission d'électrons par un matériau sous l'action de la lumière.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "La dualité onde-corpuscule signifie que la lumière possède des propriétés :", 'options': ["Ondulatoires et corpusculaires", "Uniquement ondulatoires", "Uniquement corpusculaires", "Ni ondulatoires ni corpusculaires"], 'reponse_correcte': '0', 'explication': "La lumière manifeste à la fois des propriétés d'onde et de particule.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "La diffraction est expliquée par le modèle :", 'options': ["Ondulatoire", "Corpusculaire", "Thermique", "Mécanique"], 'reponse_correcte': '0', 'explication': "La diffraction est un phénomène purement ondulatoire.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "L'effet photoélectrique est expliqué par le modèle :", 'options': ["Corpusculaire", "Ondulatoire", "Mécanique", "Thermique"], 'reponse_correcte': '0', 'explication': "L'effet photoélectrique ne peut être expliqué que par le modèle corpusculaire (photon).", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "L'énergie d'un photon de lumière verte (λ = 550 nm) est environ :", 'options': ["3,6 × 10⁻¹⁹ J", "3,6 × 10⁻³⁴ J", "5,5 × 10⁻⁷ J", "1,8 × 10⁻¹⁹ J"], 'reponse_correcte': '0', 'explication': "$E = hc/\\lambda = 6{,}63 \\times 10^{-34} \\times 3 \\times 10^8 / 550 \\times 10^{-9} \\approx 3{,}6 \\times 10^{-19}$ J.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Pour qu'il y ait effet photoélectrique, il faut que :", 'options': ["L'énergie du photon soit supérieure au travail d'extraction", "L'intensité lumineuse soit grande", "La lumière soit blanche", "La surface soit en verre"], 'reponse_correcte': '0', 'explication': "L'effet photoélectrique nécessite $E = h\\nu \\geq W$ (travail d'extraction).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Le travail d'extraction W d'un métal est l'énergie minimale pour :", 'options': ["Arracher un électron de la surface", "Chauffer le métal", "Fondre le métal", "Réfléchir la lumière"], 'reponse_correcte': '0', 'explication': "$W$ est l'énergie minimale nécessaire pour extraire un électron du métal.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "L'énergie cinétique d'un électron éjecté par effet photoélectrique est :", 'options': ["Ec = hν − W", "Ec = hν + W", "Ec = hν × W", "Ec = W/hν"], 'reponse_correcte': '0', 'explication': "$E_c = h\\nu - W$ : l'énergie du photon moins le travail d'extraction.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Si la fréquence de la lumière augmente, l'énergie du photon :", 'options': ["Augmente", "Diminue", "Reste constante", "Devient nulle"], 'reponse_correcte': '0', 'explication': "$E = h\\nu$ : l'énergie est proportionnelle à la fréquence.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Un photon UV possède plus d'énergie qu'un photon rouge car :", 'options': ["Sa fréquence est plus grande", "Sa longueur d'onde est plus grande", "Sa vitesse est plus grande", "Sa masse est plus grande"], 'reponse_correcte': '0', 'explication': "L'UV a une fréquence plus élevée (et une longueur d'onde plus courte), donc $E = h\\nu$ est plus grand.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "L'effet photoélectrique se produit quelle que soit la fréquence de la lumière.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Il existe une fréquence seuil $\\nu_0$ en dessous de laquelle l'effet ne se produit pas.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "L'énergie d'un photon est proportionnelle à sa fréquence.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "$E = h\\nu$ : relation linéaire entre énergie et fréquence.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Augmenter l'intensité lumineuse augmente l'énergie de chaque photon.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "L'intensité augmente le nombre de photons, pas l'énergie individuelle de chacun.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner l'expression de l'énergie d'un photon en fonction de h et λ.", 'reponse_correcte': 'E = hc/λ', 'tolerances': ['E=hc/λ', 'hc/λ', 'E = h × c / λ'], 'explication': "$E = hc / \\lambda$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Donner la valeur de la constante de Planck h avec son unité.", 'reponse_correcte': '6,63 × 10⁻³⁴ J·s', 'tolerances': ['6.63e-34 J·s', '6,63 × 10^-34 J.s', '6,63 × 10⁻³⁴'], 'explication': "$h = 6{,}63 \\times 10^{-34}$ J·s.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Comment s'appelle le phénomène d'éjection d'électrons d'un métal par la lumière ?", 'reponse_correcte': 'effet photoélectrique', 'tolerances': ["l'effet photoélectrique", 'photoélectrique', 'photo-électrique'], 'explication': "L'effet photoélectrique est l'émission d'électrons sous l'action de la lumière.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 9 — Images et couleurs
    # ──────────────────────────────────────────────
    {
        'ordre': 9,
        'titre': 'Images et couleurs',
        'description': "Comprendre la formation des images par les lentilles et la perception des couleurs.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Lentilles convergentes et formation des images',
                'duree': 35,
                'contenu': """# Lentilles convergentes et formation des images

## Lentille mince convergente

Une **lentille convergente** (bords minces) fait converger les rayons lumineux vers un point appelé **foyer image** $F'$.

### Éléments caractéristiques

- **Centre optique** $O$ : les rayons passant par $O$ ne sont pas déviés
- **Foyer objet** $F$ : un rayon passant par $F$ ressort parallèle à l'axe
- **Foyer image** $F'$ : un rayon parallèle à l'axe converge vers $F'$
- **Distance focale** $f' = \\overline{OF'}$ (en mètres)
- **Vergence** $V = \\frac{1}{f'}$ (en dioptries, $\\delta$)

---

## Construction géométrique d'une image

Pour construire l'image $A'B'$ d'un objet $AB$, on utilise **trois rayons** passant par le point $B$ :

1. Rayon parallèle à l'axe → passe par $F'$ après la lentille
2. Rayon passant par le centre $O$ → non dévié
3. Rayon passant par $F$ → ressort parallèle à l'axe

L'image $B'$ est à l'intersection de deux de ces rayons.

---

## Relation de conjugaison

Pour une lentille mince de distance focale $f'$ :

$$
\\frac{1}{\\overline{OA'}} - \\frac{1}{\\overline{OA}} = \\frac{1}{f'}
$$

avec la convention algébrique (distances orientées sur l'axe optique).

---

## Grandissement

Le **grandissement** $\\gamma$ caractérise le rapport de taille entre l'image et l'objet :

$$
\\gamma = \\frac{\\overline{A'B'}}{\\overline{AB}} = \\frac{\\overline{OA'}}{\\overline{OA}}
$$

- $|\\gamma| > 1$ : image agrandie
- $|\\gamma| < 1$ : image réduite
- $\\gamma > 0$ : image droite
- $\\gamma < 0$ : image renversée

---

## Types d'images

| Position de l'objet | Image |
|---|---|
| Objet au-delà de $2F$ | Réelle, renversée, réduite |
| Objet à $2F$ | Réelle, renversée, même taille |
| Objet entre $F$ et $2F$ | Réelle, renversée, agrandie |
| Objet au foyer $F$ | Pas d'image (rayons parallèles) |
| Objet entre $O$ et $F$ | Virtuelle, droite, agrandie (loupe) |

---
""",
                'quiz': {
                    'titre': 'Quiz — Lentilles convergentes et formation des images',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Une lentille convergente a des bords :", 'options': ["Minces", "Épais", "Plats", "Ondulés"], 'reponse_correcte': '0', 'explication': "Une lentille convergente est plus épaisse au centre qu'aux bords : ses bords sont minces.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Le centre optique O d'une lentille est le point par lequel :", 'options': ["Les rayons ne sont pas déviés", "Tous les rayons convergent", "L'image se forme toujours", "Aucun rayon ne passe"], 'reponse_correcte': '0', 'explication': "Un rayon passant par le centre optique n'est pas dévié.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Le foyer image F' est le point où convergent les rayons :", 'options': ["Parallèles à l'axe optique après la lentille", "Passant par le centre optique", "Venant du foyer objet", "Quelconques"], 'reponse_correcte': '0', 'explication': "Les rayons parallèles à l'axe convergent au foyer image $F'$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "La distance focale f' est la distance entre :", 'options': ["O et F'", "F et F'", "L'objet et l'image", "La lentille et l'objet"], 'reponse_correcte': '0', 'explication': "$f' = \\overline{OF'}$ : distance entre le centre optique et le foyer image.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "La vergence V d'une lentille s'exprime en :", 'options': ["Dioptries (δ)", "Mètres (m)", "Newtons (N)", "Hertz (Hz)"], 'reponse_correcte': '0', 'explication': "La vergence s'exprime en dioptries ($\\delta$).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Un rayon passant par le centre optique O :", 'options': ["N'est pas dévié", "Est réfléchi", "Converge vers F'", "Diverge toujours"], 'reponse_correcte': '0', 'explication': "Le centre optique est le point de non-déviation.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Une image réelle se forme :", 'options': ["Du côté opposé à l'objet par rapport à la lentille", "Du même côté que l'objet", "Au foyer objet", "Au centre optique"], 'reponse_correcte': '0', 'explication': "Une image réelle se forme en aval de la lentille, du côté opposé à l'objet.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Le grandissement γ compare :", 'options': ["La taille de l'image et celle de l'objet", "La distance focale et la vergence", "Deux lentilles différentes", "La luminosité de l'image"], 'reponse_correcte': '0', 'explication': "$\\gamma = \\overline{A'B'} / \\overline{AB}$ : rapport de la taille de l'image à celle de l'objet.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "La vergence d'une lentille de distance focale f' = 0,20 m est :", 'options': ["5 δ", "0,2 δ", "20 δ", "2 δ"], 'reponse_correcte': '0', 'explication': "$V = 1/f' = 1/0{,}20 = 5$ δ.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "La relation de conjugaison pour une lentille mince est :", 'options': ["1/OA' − 1/OA = 1/f'", "1/OA' + 1/OA = 1/f'", "OA' × OA = f'²", "OA' + OA = f'"], 'reponse_correcte': '0', 'explication': "$1/\\overline{OA'} - 1/\\overline{OA} = 1/f'$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Si |γ| > 1, l'image est :", 'options': ["Agrandie", "Réduite", "De même taille", "Inexistante"], 'reponse_correcte': '0', 'explication': "$|\\gamma| > 1$ signifie que l'image est plus grande que l'objet.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Un objet placé entre O et F donne une image :", 'options': ["Virtuelle, droite et agrandie", "Réelle, renversée et réduite", "Réelle, droite et agrandie", "Aucune image"], 'reponse_correcte': '0', 'explication': "Entre O et F, la lentille convergente agit comme une loupe : image virtuelle, droite, agrandie.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Si γ < 0, l'image est :", 'options': ["Renversée", "Droite", "Virtuelle", "De même taille"], 'reponse_correcte': '0', 'explication': "Un grandissement négatif indique que l'image est renversée par rapport à l'objet.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Un objet placé au foyer objet F produit :", 'options': ["Des rayons parallèles (pas d'image à distance finie)", "Une image au foyer image", "Une image au centre optique", "Une image agrandie"], 'reponse_correcte': '0', 'explication': "Un objet au foyer objet donne des rayons parallèles après la lentille : l'image est rejetée à l'infini.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Une lentille convergente peut produire une image virtuelle.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "Oui, quand l'objet est placé entre O et F (effet loupe).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "La vergence d'une lentille divergente est positive.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "La vergence d'une lentille divergente est négative ($f' < 0$).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Le grandissement γ est toujours positif.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "$\\gamma$ est négatif quand l'image est renversée.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner l'expression de la vergence V en fonction de la distance focale f'.", 'reponse_correcte': "V = 1/f'", 'tolerances': ["V=1/f'", "1/f'", "V = 1 / f'"], 'explication': "$V = 1 / f'$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Donner l'expression du grandissement γ en fonction de OA' et OA.", 'reponse_correcte': "γ = OA'/OA", 'tolerances': ["γ=OA'/OA", "gamma = OA'/OA", "OA'/OA"], 'explication': "$\\gamma = \\overline{OA'} / \\overline{OA}$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Comment appelle-t-on une image que l'on peut recueillir sur un écran ?", 'reponse_correcte': 'image réelle', 'tolerances': ['réelle', 'une image réelle', 'image reelle'], 'explication': "Une image réelle peut être projetée sur un écran, contrairement à une image virtuelle.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Couleurs et synthèse',
                'duree': 35,
                'contenu': """# Couleurs et synthèse

## Lumière blanche et couleurs

La lumière blanche est un mélange de toutes les radiations visibles (du violet au rouge).

Un **prisme** ou un **réseau** décompose la lumière blanche en ses composantes : c'est la **dispersion**.

---

## Synthèse additive

La **synthèse additive** combine des lumières colorées. Les trois couleurs primaires sont :
- **Rouge** (R)
- **Vert** (V)
- **Bleu** (B)

| Mélange | Résultat |
|---|---|
| R + V | Jaune |
| R + B | Magenta |
| V + B | Cyan |
| R + V + B | Blanc |

> **Application :** écrans (TV, téléphone, ordinateur) — chaque pixel est composé de sous-pixels R, V, B.

---

## Synthèse soustractive

La **synthèse soustractive** utilise des filtres ou des pigments qui **absorbent** certaines longueurs d'onde. Les trois couleurs primaires soustractives sont :
- **Cyan** (C)
- **Magenta** (M)
- **Jaune** (J)

| Mélange | Résultat |
|---|---|
| C + M | Bleu |
| C + J | Vert |
| M + J | Rouge |
| C + M + J | Noir |

> **Application :** imprimantes (encres CMJ + noir), peinture.

---

## Couleur perçue d'un objet

La couleur d'un objet dépend de :
1. La lumière qui l'éclaire
2. Les propriétés d'absorption/diffusion de la surface

Un objet paraît de la couleur qu'il **diffuse** (renvoie). Il **absorbe** les autres couleurs.

**Exemple :** une pomme éclairée en lumière blanche paraît rouge car elle absorbe le vert et le bleu et diffuse le rouge.

---

## Vision des couleurs

L'œil humain possède trois types de **cônes** sensibles à :
- Rouge ($\\lambda \\approx 570$ nm)
- Vert ($\\lambda \\approx 540$ nm)
- Bleu ($\\lambda \\approx 420$ nm)

La sensation de couleur résulte de la combinaison des signaux envoyés par ces trois types de cônes au cerveau.

---
""",
                'quiz': {
                    'titre': 'Quiz — Couleurs et synthèse',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Les trois couleurs primaires en synthèse additive sont :", 'options': ["Rouge, vert, bleu", "Cyan, magenta, jaune", "Rouge, jaune, bleu", "Blanc, noir, gris"], 'reponse_correcte': '0', 'explication': "En synthèse additive, les primaires sont rouge (R), vert (V) et bleu (B).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Les trois couleurs primaires en synthèse soustractive sont :", 'options': ["Cyan, magenta, jaune", "Rouge, vert, bleu", "Rouge, jaune, bleu", "Orange, violet, vert"], 'reponse_correcte': '0', 'explication': "En synthèse soustractive (encres, filtres), les primaires sont cyan, magenta et jaune.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "La synthèse additive est utilisée dans :", 'options': ["Les écrans (TV, téléphone)", "Les imprimantes", "La peinture", "Les filtres photographiques"], 'reponse_correcte': '0', 'explication': "Les écrans superposent des lumières RVB : c'est de la synthèse additive.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "La lumière blanche est un mélange de :", 'options': ["Toutes les radiations visibles", "Rouge et bleu uniquement", "Uniquement du jaune", "Aucune radiation"], 'reponse_correcte': '0', 'explication': "La lumière blanche contient toutes les longueurs d'onde du spectre visible.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Un prisme décompose la lumière blanche par :", 'options': ["Dispersion", "Absorption", "Réflexion totale", "Diffusion"], 'reponse_correcte': '0', 'explication': "Le prisme sépare les composantes de la lumière blanche : c'est la dispersion.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "En synthèse additive, rouge + vert donne du :", 'options': ["Jaune", "Cyan", "Magenta", "Blanc"], 'reponse_correcte': '0', 'explication': "Rouge + vert = jaune en synthèse additive.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "En synthèse additive, rouge + vert + bleu donne du :", 'options': ["Blanc", "Noir", "Gris", "Jaune"], 'reponse_correcte': '0', 'explication': "La superposition des trois primaires additives donne du blanc.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "L'œil humain possède des cellules sensibles aux couleurs appelées :", 'options': ["Cônes", "Bâtonnets", "Iris", "Pupilles"], 'reponse_correcte': '0', 'explication': "Les cônes sont les cellules de la rétine responsables de la vision des couleurs.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "En synthèse soustractive, cyan + magenta donne du :", 'options': ["Bleu", "Rouge", "Vert", "Blanc"], 'reponse_correcte': '0', 'explication': "Cyan absorbe le rouge, magenta absorbe le vert : il ne reste que le bleu.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Un objet rouge éclairé en lumière blanche :", 'options': ["Diffuse le rouge et absorbe les autres couleurs", "Absorbe le rouge", "Diffuse toutes les couleurs", "N'absorbe aucune couleur"], 'reponse_correcte': '0', 'explication': "L'objet rouge absorbe le vert et le bleu et diffuse (renvoie) le rouge.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Un filtre cyan laisse passer :", 'options': ["Le vert et le bleu", "Uniquement le rouge", "Uniquement le cyan", "Toutes les couleurs"], 'reponse_correcte': '0', 'explication': "Le filtre cyan absorbe le rouge et transmet le vert et le bleu (vert + bleu = cyan).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "En synthèse soustractive, cyan + magenta + jaune donne du :", 'options': ["Noir", "Blanc", "Gris", "Rouge"], 'reponse_correcte': '0', 'explication': "Chaque filtre absorbe une primaire additive : ensemble, tout est absorbé → noir.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Un objet vert éclairé uniquement en lumière rouge apparaît :", 'options': ["Noir", "Vert", "Rouge", "Jaune"], 'reponse_correcte': '0', 'explication': "L'objet vert absorbe le rouge et ne reçoit pas de vert à diffuser : il apparaît noir.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "En synthèse additive, vert + bleu donne du :", 'options': ["Cyan", "Jaune", "Magenta", "Blanc"], 'reponse_correcte': '0', 'explication': "Vert + bleu = cyan en synthèse additive.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "La couleur perçue d'un objet dépend uniquement de la lumière qui l'éclaire.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Elle dépend aussi des propriétés d'absorption et de diffusion de la surface de l'objet.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "En synthèse soustractive, cyan + jaune donne du vert.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "Cyan absorbe le rouge, jaune absorbe le bleu : il reste le vert.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Les cônes de l'œil sont sensibles au rouge, au vert et au bleu.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "L'œil possède trois types de cônes sensibles respectivement au rouge, au vert et au bleu.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Quel résultat obtient-on en mélangeant du rouge et du bleu en synthèse additive ?", 'reponse_correcte': 'magenta', 'tolerances': ['du magenta', 'Magenta', 'le magenta'], 'explication': "Rouge + bleu = magenta en synthèse additive.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Quel est le rôle d'un filtre coloré en synthèse soustractive ?", 'reponse_correcte': 'absorber certaines longueurs d\'onde', 'tolerances': ["absorber des longueurs d'onde", 'absorber certaines couleurs', "il absorbe certaines longueurs d'onde"], 'explication': "Un filtre absorbe certaines longueurs d'onde et en transmet d'autres.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Combien de types de cônes possède l'œil humain ?", 'reponse_correcte': '3', 'tolerances': ['trois', '3 types', 'trois types'], 'explication': "L'œil possède 3 types de cônes (rouge, vert, bleu).", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Seed Physique Première — 9 chapitres, leçons uniquement (sans quiz)."

    def handle(self, *args, **options):
        matiere, created = Matiere.objects.get_or_create(
            nom='physique',
            defaults={
                'description': "La physique au lycée : mécanique, énergie, ondes, lumière et électricité.",
            },
        )
        if created:
            self.stdout.write(f"  ✔ Matière « {matiere} » créée")
        else:
            self.stdout.write(f"  … Matière « {matiere} » existante")

        total_lecons = 0

        for chap_data in CHAPITRES:
            chapitre, ch_created = Chapitre.objects.get_or_create(
                matiere=matiere,
                niveau='premiere',
                ordre=chap_data['ordre'],
                defaults={
                    'titre': chap_data['titre'],
                    'description': chap_data['description'],
                    'score_minimum_deblocage': chap_data.get('score_minimum', 60.0),
                },
            )
            status = "créé" if ch_created else "existant"
            self.stdout.write(f"  {'✔' if ch_created else '…'} Ch.{chap_data['ordre']} — {chap_data['titre']} ({status})")

            for lecon_data in chap_data['lecons']:
                lecon, lec_created = Lecon.objects.update_or_create(
                    chapitre=chapitre,
                    ordre=lecon_data['ordre'],
                    defaults={
                        'titre': lecon_data['titre'],
                        'duree_estimee': lecon_data.get('duree', 30),
                        'contenu': lecon_data['contenu'],
                    },
                )
                total_lecons += 1
                status = "créée" if lec_created else "mise à jour"
                self.stdout.write(f"      L{lecon_data['ordre']} — {lecon_data['titre']} ({status})")

                # Quiz et questions
                if 'quiz' in lecon_data:
                    quiz_data = lecon_data['quiz']
                    Quiz.objects.filter(lecon=lecon).delete()
                    quiz = Quiz.objects.create(
                        lecon=lecon,
                        titre=quiz_data.get('titre', f"Quiz — {lecon.titre}"),
                        score_minimum=quiz_data.get('score_minimum', 60.0),
                    )
                    for q in quiz_data['questions']:
                        Question.objects.create(
                            quiz=quiz,
                            ordre=q['ordre'],
                            texte=q['texte'],
                            type=q.get('type', 'qcm'),
                            options=q.get('options'),
                            reponse_correcte=str(q['reponse_correcte']),
                            tolerances=q.get('tolerances'),
                            explication=q.get('explication', ''),
                            difficulte=q.get('difficulte', 'moyen'),
                            points=q.get('points', 1),
                        )
                    self.stdout.write(f"        📝 Quiz créé ({len(quiz_data['questions'])} questions)")

        self.stdout.write(self.style.SUCCESS(
            f"\n✅ Physique Première — {len(CHAPITRES)} chapitres, {total_lecons} leçons traités."
        ))
