"""
Seed Physique Seconde — 7 chapitres, leçons uniquement (sans quiz).
Usage : python manage.py seed_physique_seconde
"""

from django.core.management.base import BaseCommand
from courses.models import Matiere, Chapitre, Lecon, Quiz, Question

CHAPITRES = [
    # ──────────────────────────────────────────────
    # CHAPITRE 1 — Description d'un mouvement
    # ──────────────────────────────────────────────
    {
        'ordre': 1,
        'titre': "Description d'un mouvement",
        'description': "Décrire le mouvement d'un objet : système, référentiel, trajectoire, vitesse moyenne et instantanée.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Système, référentiel et relativité du mouvement',
                'duree': 35,
                'contenu': """# Système, référentiel et relativité du mouvement

## Introduction

En physique, **décrire un mouvement** est l'une des premières compétences à acquérir. Mais avant de parler de vitesse ou de trajectoire, il faut préciser **quel objet** on étudie et **par rapport à quoi** on décrit son mouvement. C'est tout l'enjeu de cette leçon.

---

## Le système

### Définition

On appelle **système** l'objet ou l'ensemble d'objets dont on étudie le mouvement. Pour simplifier l'étude, on modélise souvent le système par un **point matériel** : un point géométrique auquel on attribue toute la masse du système.

> **Exemple :** pour étudier le mouvement d'une voiture sur une autoroute, on peut assimiler la voiture à un point situé en son centre de gravité.

### Quand utiliser le modèle du point matériel ?

Ce modèle est valable lorsque les **dimensions du système** sont **négligeables** devant les distances parcourues. Une voiture de 4 m qui parcourt 100 km peut être assimilée à un point ; un ballon de football que l'on étudie lors d'un tir à 20 m aussi.

---

## Le référentiel

### Définition

Un **référentiel** est un solide de référence, muni d'un repère d'espace et d'une horloge, par rapport auquel on décrit le mouvement du système.

Le choix du référentiel est **fondamental** : un même objet peut être immobile dans un référentiel et en mouvement dans un autre.

### Les référentiels courants

| Référentiel | Solide de référence | Utilisation typique |
|---|---|---|
| **Terrestre** (ou du laboratoire) | Le sol, un bâtiment, la salle de classe | Mouvements à la surface de la Terre |
| **Géocentrique** | Le centre de la Terre | Mouvement de la Lune, des satellites |
| **Héliocentrique** | Le centre du Soleil | Mouvement des planètes |

---

## La relativité du mouvement

### Principe

Le mouvement d'un objet **dépend du référentiel** dans lequel on l'observe. On dit que **le mouvement est relatif**.

### Exemple concret

Imaginons un passager assis dans un train en marche :

- **Dans le référentiel du train** : le passager est **immobile** (il ne bouge pas par rapport au wagon).
- **Dans le référentiel terrestre** : le passager est **en mouvement** (il se déplace avec le train par rapport au sol).

### Autre exemple

Un cycliste pédale sur une route droite. Sa main droite :

- est en mouvement **circulaire** dans le référentiel du vélo (elle tourne avec le guidon ou la pédale) ;
- décrit une trajectoire **plus complexe** (cycloïde) dans le référentiel terrestre.

> **Conclusion essentielle :** il n'y a pas de mouvement « absolu ». Tout mouvement est décrit **par rapport à un référentiel choisi**. Préciser le référentiel est **obligatoire** pour toute description de mouvement.

---

## Le repère d'espace et le repère de temps

Pour repérer la position d'un point dans un référentiel, on utilise un **repère d'espace** :

- **Repère à une dimension** (axe $Ox$) : suffisant pour un mouvement rectiligne.
- **Repère à deux dimensions** (axes $Ox$ et $Oy$) : pour un mouvement plan (ex : trajectoire parabolique).
- **Repère à trois dimensions** (axes $Ox$, $Oy$ et $Oz$) : pour un mouvement quelconque dans l'espace.

On associe au repère une **horloge** (origine des temps $t = 0$) pour mesurer les instants successifs. La position du système est alors une fonction du temps : $M(t)$.

---

## Enregistrement d'un mouvement

### Chronophotographie

La **chronophotographie** consiste à photographier un objet en mouvement à intervalles de temps **égaux** $\\Delta t$. On obtient une série de positions $M_0, M_1, M_2, \\ldots$ qui permettent de reconstituer la trajectoire et d'estimer les vitesses.

### Pointage vidéo

Avec un logiciel de pointage (ex : Aviméca, Tracker), on relève les coordonnées $(x, y)$ du système image par image. Cela fournit un tableau de valeurs $x(t)$ et $y(t)$.

---

## À retenir

- Le **système** est l'objet étudié, modélisé par un point matériel si ses dimensions sont négligeables.
- Le **référentiel** est le solide de référence + repère + horloge.
- Le mouvement est **relatif** : sa description dépend du référentiel choisi.
- Préciser le référentiel est **indispensable** avant toute description cinématique.
""",
                'quiz': {
                    'titre': "Quiz — Système, référentiel et relativité du mouvement",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Qu'appelle-t-on un « système » en mécanique ?",
                            'options': ["L'objet dont on étudie le mouvement", "Le référentiel choisi", "L'ensemble des forces appliquées", "L'horloge utilisée pour mesurer le temps"],
                            'reponse_correcte': '0',
                            'explication': "Le système est l'objet ou l'ensemble d'objets dont on étudie le mouvement.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quand peut-on modéliser un système par un point matériel ?",
                            'options': ["Quand ses dimensions sont négligeables devant les distances parcourues", "Quand il est immobile", "Quand il a une masse très faible", "Quand il se déplace en ligne droite"],
                            'reponse_correcte': '0',
                            'explication': "Le modèle du point matériel est valable lorsque les dimensions du système sont négligeables par rapport aux distances parcourues.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "De quoi est composé un référentiel ?",
                            'options': ["Un solide de référence, un repère d'espace et une horloge", "Uniquement un solide de référence", "Un repère d'espace et une trajectoire", "Une horloge et un dynamomètre"],
                            'reponse_correcte': '0',
                            'explication': "Un référentiel est constitué d'un solide de référence auquel on associe un repère d'espace et une horloge.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quel référentiel utilise-t-on habituellement pour décrire le mouvement des planètes autour du Soleil ?",
                            'options': ["Le référentiel héliocentrique", "Le référentiel terrestre", "Le référentiel géocentrique", "Le référentiel du laboratoire"],
                            'reponse_correcte': '0',
                            'explication': "Le référentiel héliocentrique, centré sur le Soleil, est utilisé pour décrire le mouvement des planètes.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Un passager est assis dans un train en marche. Dans le référentiel du train, le passager est :",
                            'options': ["Immobile", "En mouvement rectiligne uniforme", "En mouvement circulaire", "En mouvement accéléré"],
                            'reponse_correcte': '0',
                            'explication': "Dans le référentiel du train, le passager ne bouge pas par rapport au wagon : il est immobile.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Le référentiel géocentrique est centré sur :",
                            'options': ["Le centre de la Terre", "Le centre du Soleil", "La surface de la Terre", "La Lune"],
                            'reponse_correcte': '0',
                            'explication': "Le référentiel géocentrique a pour centre le centre de la Terre.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "La description du mouvement d'un objet dépend du référentiel choisi. Ce principe s'appelle :",
                            'options': ["La relativité du mouvement", "Le principe d'inertie", "Le principe d'action-réaction", "La loi de gravitation"],
                            'reponse_correcte': '0',
                            'explication': "Le mouvement est relatif : sa description change selon le référentiel d'observation.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "La chronophotographie consiste à photographier un objet en mouvement :",
                            'options': ["À intervalles de temps égaux", "À vitesse variable", "Uniquement quand il est immobile", "Une seule fois au début du mouvement"],
                            'reponse_correcte': '0',
                            'explication': "La chronophotographie prend des photos à intervalles de temps réguliers pour reconstituer le mouvement.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Un vélo roule sur une route rectiligne. Dans le référentiel terrestre, un point de la roue décrit une trajectoire :",
                            'options': ["Cycloïde", "Rectiligne", "Circulaire", "Immobile"],
                            'reponse_correcte': '0',
                            'explication': "Dans le référentiel terrestre, un point de la roue décrit une cycloïde (combinaison de rotation et de translation).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quel référentiel est le mieux adapté pour étudier le mouvement de la Lune autour de la Terre ?",
                            'options': ["Le référentiel géocentrique", "Le référentiel terrestre", "Le référentiel héliocentrique", "Le référentiel du laboratoire"],
                            'reponse_correcte': '0',
                            'explication': "Le référentiel géocentrique est centré sur la Terre, ce qui est le plus adapté pour étudier le mouvement de la Lune.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Un repère à deux dimensions est suffisant pour décrire un mouvement :",
                            'options': ["Plan (ex : trajectoire parabolique)", "Rectiligne uniquement", "Quelconque dans l'espace", "Circulaire uniquement"],
                            'reponse_correcte': '0',
                            'explication': "Un repère 2D (Ox, Oy) suffit pour un mouvement plan, comme une trajectoire parabolique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Un objet lâché dans un train en MRU a, dans le référentiel terrestre, une trajectoire :",
                            'options': ["Parabolique", "Rectiligne verticale", "Circulaire", "Rectiligne horizontale"],
                            'reponse_correcte': '0',
                            'explication': "Dans le référentiel du train, la trajectoire est rectiligne verticale, mais dans le référentiel terrestre, elle est parabolique car le train avance.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Pour étudier le mouvement d'un satellite artificiel autour de la Terre, le référentiel terrestre est-il adapté ?",
                            'options': ["Non, il faut utiliser le référentiel géocentrique", "Oui, le référentiel terrestre convient toujours", "Oui, si la durée est courte", "Non, il faut le référentiel héliocentrique"],
                            'reponse_correcte': '0',
                            'explication': "Pour un satellite en orbite autour de la Terre, le référentiel géocentrique est le plus approprié car la Terre tourne sur elle-même.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Le mouvement d'un objet est absolu : il ne dépend pas du référentiel choisi.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le mouvement est relatif : sa description dépend toujours du référentiel choisi.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Un objet peut être en mouvement dans un référentiel et immobile dans un autre.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est exactement le principe de la relativité du mouvement.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Le référentiel terrestre est considéré comme galiléen pour des expériences de courte durée.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Pour des durées courtes et des distances faibles, le référentiel terrestre est une bonne approximation d'un référentiel galiléen.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Le référentiel héliocentrique est centré sur la Terre.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le référentiel héliocentrique est centré sur le Soleil (hélios = soleil en grec).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on le solide de référence par rapport auquel on décrit un mouvement ?",
                            'options': None,
                            'reponse_correcte': 'référentiel',
                            'tolerances': ["referentiel", "le référentiel", "le referentiel", "un référentiel"],
                            'explication': "Le référentiel est le solide de référence (muni d'un repère et d'une horloge) par rapport auquel on décrit le mouvement.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on la technique qui consiste à photographier un objet en mouvement à intervalles de temps réguliers ?",
                            'options': None,
                            'reponse_correcte': 'chronophotographie',
                            'tolerances': ["la chronophotographie", "chrono-photographie"],
                            'explication': "La chronophotographie consiste à prendre des photos à intervalles de temps égaux pour analyser un mouvement.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Dans quel référentiel étudie-t-on le mouvement des planètes du système solaire ?",
                            'options': None,
                            'reponse_correcte': 'héliocentrique',
                            'tolerances': ["heliocentrique", "référentiel héliocentrique", "referentiel heliocentrique", "le référentiel héliocentrique"],
                            'explication': "Le référentiel héliocentrique (centré sur le Soleil) est utilisé pour décrire le mouvement des planètes.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Trajectoire, vecteur déplacement et vitesse',
                'duree': 40,
                'contenu': """# Trajectoire, vecteur déplacement et vitesse

## Introduction

Une fois le système et le référentiel définis, on peut caractériser le mouvement de façon précise. Cette leçon introduit trois notions fondamentales : la **trajectoire**, le **vecteur déplacement** et la **vitesse**.

---

## La trajectoire

### Définition

La **trajectoire** d'un point matériel dans un référentiel donné est l'ensemble des positions successives occupées par ce point au cours du temps. C'est la « trace » laissée par le mouvement.

### Types de trajectoires

| Trajectoire | Forme | Exemple |
|---|---|---|
| **Rectiligne** | Ligne droite | Voiture sur une route droite |
| **Circulaire** | Cercle ou arc de cercle | Nacelle de grande roue, satellite en orbite circulaire |
| **Parabolique** | Parabole | Balle lancée en l'air |
| **Quelconque** | Courbe irrégulière | Mouche en vol |

> La trajectoire dépend du **référentiel**. Une balle lâchée dans un train a une trajectoire rectiligne verticale dans le référentiel du train, mais parabolique dans le référentiel terrestre.

---

## Le vecteur déplacement

### Définition

Soit un point matériel occupant la position $M$ à l'instant $t$ et la position $M'$ à l'instant $t' = t + \\Delta t$. Le **vecteur déplacement** est :

$$\\vec{MM'} = \\overrightarrow{OM'} - \\overrightarrow{OM}$$

où $O$ est l'**origine** du repère.

### Propriétés du vecteur déplacement

- **Direction** : de $M$ vers $M'$.
- **Sens** : de la position initiale vers la position finale.
- **Norme** : $\\|\\vec{MM'}\\|$ est la distance en ligne droite entre $M$ et $M'$ (ce n'est **pas** la distance parcourue le long de la trajectoire, sauf si celle-ci est rectiligne).

### Distinction importante

La **distance parcourue** $d$ le long de la trajectoire est en général **supérieure ou égale** à la norme du vecteur déplacement :

$$d \\geq \\|\\vec{MM'}\\|$$

L'égalité n'est vérifiée que pour un mouvement **rectiligne** entre $M$ et $M'$.

---

## La vitesse moyenne

### Définition scalaire

La **vitesse moyenne** $v_m$ d'un objet entre deux instants est le rapport de la **distance parcourue** $d$ sur la **durée** $\\Delta t$ :

$$v_m = \\frac{d}{\\Delta t}$$

- $v_m$ s'exprime en **mètres par seconde** (m/s) dans le Système International.
- $d$ est la distance parcourue le long de la trajectoire (en m).
- $\\Delta t = t' - t$ est la durée du parcours (en s).

### Conversion km/h ↔ m/s

$$1 \\text{ km/h} = \\frac{1000}{3600} \\text{ m/s} \\approx 0{,}278 \\text{ m/s}$$

> **Astuce :** pour convertir de km/h en m/s, on **divise par 3,6**. Pour convertir de m/s en km/h, on **multiplie par 3,6**.

| Vitesse en km/h | Vitesse en m/s |
|---|---|
| 36 | 10 |
| 90 | 25 |
| 130 | 36,1 |

### Définition vectorielle

Le **vecteur vitesse moyenne** est défini par :

$$\\vec{v}_m = \\frac{\\vec{MM'}}{\\Delta t}$$

Il a la même direction et le même sens que le vecteur déplacement $\\vec{MM'}$.

---

## La vitesse instantanée

### Définition

La **vitesse instantanée** est la vitesse à un instant $t$ précis. Elle est obtenue en considérant la vitesse moyenne sur un intervalle de temps $\\Delta t$ **de plus en plus petit** :

$$\\vec{v}(t) = \\lim_{\\Delta t \\to 0} \\frac{\\vec{MM'}}{\\Delta t}$$

En pratique, sur une chronophotographie, on approxime la vitesse instantanée au point $M_i$ par :

$$v_i \\approx \\frac{M_{i-1}M_{i+1}}{t_{i+1} - t_{i-1}} = \\frac{M_{i-1}M_{i+1}}{2\\Delta t}$$

### Le vecteur vitesse instantanée

Le vecteur vitesse instantanée $\\vec{v}(t)$ est **tangent à la trajectoire** au point considéré. Il est orienté dans le **sens du mouvement**.

- Sa **norme** est la valeur de la vitesse (en m/s).
- Sa **direction** est la tangente à la trajectoire.
- Son **sens** est celui du mouvement.

---

## Classification des mouvements

Le mouvement d'un objet se classe selon l'évolution de sa vitesse et de sa trajectoire.

### Selon la trajectoire

| Trajectoire | Nom du mouvement |
|---|---|
| Ligne droite | Mouvement **rectiligne** |
| Cercle | Mouvement **circulaire** |
| Autre courbe | Mouvement **curviligne** |

### Selon la vitesse

| Évolution de $v$ | Nom du mouvement |
|---|---|
| $v$ constante | Mouvement **uniforme** |
| $v$ augmente | Mouvement **accéléré** |
| $v$ diminue | Mouvement **décéléré** (ou ralenti) |

### Combinaisons courantes

- **Mouvement rectiligne uniforme (MRU)** : trajectoire droite et vitesse constante.
- **Mouvement rectiligne uniformément accéléré** : trajectoire droite et vitesse qui augmente régulièrement.
- **Mouvement circulaire uniforme (MCU)** : trajectoire circulaire et norme de la vitesse constante (mais la direction change !).

---

## Interpréter une chronophotographie

Sur une chronophotographie (intervalle de temps $\\Delta t$ constant) :

- Si les points sont **régulièrement espacés** → mouvement **uniforme**.
- Si les points se **rapprochent** → mouvement **décéléré**.
- Si les points s'**éloignent** → mouvement **accéléré**.

---

## Exemple de calcul

Une voiture parcourt 150 km en 1h30.

$$v_m = \\frac{d}{\\Delta t} = \\frac{150 \\times 10^3}{1{,}5 \\times 3600} = \\frac{150\\,000}{5\\,400} \\approx 27{,}8 \\text{ m/s}$$

En km/h : $v_m = \\frac{150}{1{,}5} = 100$ km/h.

---

## À retenir

- La **trajectoire** est l'ensemble des positions successives du système dans le référentiel choisi.
- Le **vecteur déplacement** $\\vec{MM'}$ relie deux positions ; sa norme ≠ distance parcourue (sauf mouvement rectiligne).
- La **vitesse moyenne** : $v_m = \\frac{d}{\\Delta t}$ (scalaire) ; **vecteur vitesse moyenne** : $\\vec{v}_m = \\frac{\\vec{MM'}}{\\Delta t}$.
- La **vitesse instantanée** est la limite de la vitesse moyenne quand $\\Delta t \\to 0$ ; son vecteur est **tangent** à la trajectoire.
- Un mouvement est **uniforme** si $v = \\text{cte}$, **accéléré** si $v$ augmente, **décéléré** si $v$ diminue.
""",
                'quiz': {
                    'titre': "Quiz — Trajectoire, vecteur déplacement et vitesse",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "La trajectoire d'un point matériel est :",
                            'options': ["L'ensemble des positions successives du point dans un référentiel", "La vitesse du point à chaque instant", "La force appliquée au point", "La masse du point matériel"],
                            'reponse_correcte': '0',
                            'explication': "La trajectoire est l'ensemble des positions successives occupées par le point matériel au cours du temps.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quelle est l'unité de la vitesse dans le Système International ?",
                            'options': ["m/s", "km/h", "m/s²", "N"],
                            'reponse_correcte': '0',
                            'explication': "Dans le Système International, la vitesse s'exprime en mètres par seconde (m/s).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Pour convertir une vitesse de km/h en m/s, il faut :",
                            'options': ["Diviser par 3,6", "Multiplier par 3,6", "Diviser par 60", "Multiplier par 1000"],
                            'reponse_correcte': '0',
                            'explication': "1 km/h = 1000 m / 3600 s ≈ 0,278 m/s. On divise donc par 3,6.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "La formule de la vitesse moyenne est :",
                            'options': ["v = d / Δt", "v = Δt / d", "v = d × Δt", "v = d² / Δt"],
                            'reponse_correcte': '0',
                            'explication': "La vitesse moyenne est le rapport de la distance parcourue d sur la durée Δt.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Un mouvement rectiligne uniforme (MRU) est un mouvement où :",
                            'options': ["La trajectoire est droite et la vitesse constante", "La trajectoire est courbe et la vitesse constante", "La trajectoire est droite et la vitesse augmente", "La trajectoire est circulaire et la vitesse constante"],
                            'reponse_correcte': '0',
                            'explication': "Un MRU combine une trajectoire rectiligne et une vitesse de norme constante.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quelle est la vitesse en m/s d'une voiture roulant à 90 km/h ?",
                            'options': ["25 m/s", "90 m/s", "9 m/s", "250 m/s"],
                            'reponse_correcte': '0',
                            'explication': "90 ÷ 3,6 = 25 m/s.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Le vecteur vitesse instantanée est toujours :",
                            'options': ["Tangent à la trajectoire dans le sens du mouvement", "Perpendiculaire à la trajectoire", "Dirigé vers le centre de la trajectoire", "Vertical et vers le bas"],
                            'reponse_correcte': '0',
                            'explication': "Le vecteur vitesse instantanée est tangent à la trajectoire au point considéré et orienté dans le sens du mouvement.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "La nacelle d'une grande roue tournant à vitesse constante décrit un mouvement :",
                            'options': ["Circulaire uniforme", "Rectiligne uniforme", "Rectiligne accéléré", "Parabolique"],
                            'reponse_correcte': '0',
                            'explication': "La nacelle se déplace sur un cercle à vitesse constante : c'est un mouvement circulaire uniforme.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Sur une chronophotographie à intervalles de temps égaux, si les points s'éloignent les uns des autres, le mouvement est :",
                            'options': ["Accéléré", "Uniforme", "Décéléré", "Immobile"],
                            'reponse_correcte': '0',
                            'explication': "Des points qui s'éloignent signifient que l'objet parcourt des distances de plus en plus grandes dans le même intervalle de temps : il accélère.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "La norme du vecteur déplacement entre deux points M et M' est :",
                            'options': ["La distance en ligne droite entre M et M'", "La distance parcourue le long de la trajectoire", "La vitesse moyenne entre M et M'", "La durée du parcours de M à M'"],
                            'reponse_correcte': '0',
                            'explication': "La norme du vecteur déplacement est la distance à vol d'oiseau entre les deux positions, pas la distance parcourue le long de la trajectoire.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Une voiture parcourt 150 km en 1h30. Sa vitesse moyenne est :",
                            'options': ["100 km/h", "150 km/h", "75 km/h", "225 km/h"],
                            'reponse_correcte': '0',
                            'explication': "v = d / Δt = 150 / 1,5 = 100 km/h.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Sur une chronophotographie, on approxime la vitesse instantanée au point Mᵢ par :",
                            'options': ["vᵢ ≈ Mᵢ₋₁Mᵢ₊₁ / (2Δt)", "vᵢ ≈ Mᵢ₋₁Mᵢ / Δt", "vᵢ ≈ MᵢMᵢ₊₁ × Δt", "vᵢ ≈ Mᵢ₋₁Mᵢ₊₁ × Δt"],
                            'reponse_correcte': '0',
                            'explication': "On encadre le point Mᵢ par ses voisins et on divise la distance Mᵢ₋₁Mᵢ₊₁ par l'intervalle de temps 2Δt.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Un objet décrit un mouvement circulaire uniforme. Comment évolue son vecteur vitesse ?",
                            'options': ["Sa norme est constante mais sa direction change", "Sa norme et sa direction sont constantes", "Sa norme change mais sa direction est fixe", "Sa norme et sa direction changent"],
                            'reponse_correcte': '0',
                            'explication': "En MCU, la norme de la vitesse est constante mais la direction change à chaque instant (tangente au cercle).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "La distance parcourue le long de la trajectoire est toujours égale à la norme du vecteur déplacement.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La distance parcourue est supérieure ou égale à la norme du vecteur déplacement. L'égalité n'est vérifiée que pour un mouvement rectiligne.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Un mouvement circulaire uniforme est un mouvement où la vitesse (le vecteur) est constante.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "En MCU, la norme de la vitesse est constante, mais la direction du vecteur vitesse change : le vecteur vitesse n'est donc pas constant.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Sur une chronophotographie à intervalles réguliers, des points régulièrement espacés indiquent un mouvement uniforme.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Des écarts constants entre les positions successives, à intervalles de temps égaux, signifient une vitesse constante.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "La vitesse instantanée est obtenue en faisant tendre l'intervalle de temps Δt vers zéro.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "La vitesse instantanée est la limite de la vitesse moyenne lorsque Δt tend vers 0.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Convertir 36 km/h en m/s. Donner la valeur numérique.",
                            'options': None,
                            'reponse_correcte': '10',
                            'tolerances': ["10 m/s", "10,0", "10.0"],
                            'explication': "36 ÷ 3,6 = 10 m/s.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment qualifie-t-on un mouvement dont la trajectoire est une droite et la vitesse constante ? (3 mots)",
                            'options': None,
                            'reponse_correcte': 'mouvement rectiligne uniforme',
                            'tolerances': ["rectiligne uniforme", "MRU", "mru"],
                            'explication': "Un mouvement de trajectoire rectiligne et de vitesse constante est un mouvement rectiligne uniforme (MRU).",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Comment qualifie-t-on un mouvement dont la vitesse diminue au cours du temps ?",
                            'options': None,
                            'reponse_correcte': 'décéléré',
                            'tolerances': ["decelere", "ralenti", "mouvement décéléré", "mouvement decelere"],
                            'explication': "Un mouvement dont la vitesse diminue est dit décéléré (ou ralenti).",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 2 — Les forces et les interactions
    # ──────────────────────────────────────────────
    {
        'ordre': 2,
        'titre': 'Les forces et les interactions',
        'description': "Modéliser une action mécanique par une force, distinguer forces de contact et forces à distance, et étudier la gravitation et le poids.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Généralités sur les forces',
                'duree': 35,
                'contenu': """# Généralités sur les forces

## Introduction

Quand on pousse un chariot, quand la Terre attire une pomme, quand un ressort se détend… on parle d'**actions mécaniques**. Ces actions sont modélisées en physique par des **forces**. Comprendre ce qu'est une force et comment on la représente est essentiel pour analyser le mouvement des objets.

---

## Action mécanique et force

### Définition

Une **action mécanique** est toute cause capable de :

- **mettre en mouvement** un objet au repos ;
- **modifier** le mouvement d'un objet (changer sa vitesse ou sa direction) ;
- **déformer** un objet.

On modélise chaque action mécanique par une **force**, notée $\\vec{F}$.

### Notation

La force exercée par l'objet $A$ sur l'objet $B$ se note :

$$\\vec{F}_{A/B}$$

> On lit « force exercée par $A$ sur $B$ ».

---

## Caractéristiques d'une force

Une force est un **vecteur**. Elle est entièrement définie par quatre caractéristiques :

| Caractéristique | Description |
|---|---|
| **Point d'application** | Point où s'exerce la force |
| **Direction** | Droite d'action (horizontale, verticale, oblique…) |
| **Sens** | Vers le haut, vers la droite, etc. |
| **Norme (intensité)** | Valeur exprimée en **newtons** (N) |

### Représentation graphique

On représente une force par une **flèche** :

- L'**origine** de la flèche est le point d'application.
- La **direction** de la flèche est celle de la force.
- Le **sens** de la flèche indique le sens de la force.
- La **longueur** de la flèche est proportionnelle à l'intensité (on choisit une échelle, par ex. 1 cm ↔ 2 N).

---

## Forces de contact et forces à distance

### Forces de contact

Elles nécessitent un **contact physique** entre les deux objets. Exemples :

- **Réaction d'un support** : force exercée par une table sur un livre posé dessus.
- **Force de frottement** : résistance au glissement entre deux surfaces.
- **Tension d'un fil** : force exercée par un fil tendu sur l'objet accroché.
- **Poussée** : action de la main sur un ballon.

### Forces à distance

Elles s'exercent **sans contact** entre les objets. Exemples :

- **Force gravitationnelle** : attraction entre deux masses.
- **Force électrostatique** : attraction ou répulsion entre charges électriques.
- **Force magnétique** : action d'un aimant sur un clou en fer.

---

## Inventaire des forces — le diagramme objet-interactions (DOI)

Avant de résoudre un problème de mécanique, on réalise un **inventaire des forces** (ou analyse des actions mécaniques) en suivant ces étapes :

1. **Définir le système** étudié.
2. **Identifier tous les objets** qui agissent sur le système.
3. Pour chaque objet, déterminer si l'interaction est **de contact** ou **à distance**.
4. Représenter ces interactions dans un **diagramme objet-interactions** (DOI).

### Exemple : un livre posé sur une table

- Système : le livre.
- Objets agissant sur le livre :
  - La **Terre** → force gravitationnelle (à distance) → poids $\\vec{P}$
  - La **table** → force de contact → réaction normale $\\vec{R}$

---

## Mesure d'une force : le dynamomètre

Un **dynamomètre** est un instrument qui mesure l'intensité d'une force grâce à l'allongement d'un ressort. Il est gradué en **newtons** (N).

> L'unité de force dans le Système International est le **newton** (N), en hommage au physicien Isaac Newton (1642–1727).

---

## Le principe des actions réciproques

### Énoncé (3ᵉ loi de Newton)

Si un objet $A$ exerce une force $\\vec{F}_{A/B}$ sur un objet $B$, alors $B$ exerce sur $A$ une force $\\vec{F}_{B/A}$ telle que :

$$\\vec{F}_{B/A} = -\\vec{F}_{A/B}$$

Ces deux forces :

- ont la **même direction** (même droite d'action) ;
- ont la **même norme** (même intensité) ;
- sont de **sens opposés** ;
- s'exercent sur **deux objets différents**.

### Exemple

Quand vous poussez un mur avec une force de 50 N, le mur vous repousse avec une force de 50 N en sens opposé. C'est pour cela que vous sentez une résistance.

> ⚠️ **Attention :** les deux forces réciproques s'exercent sur des objets *différents*. Elles ne s'annulent **pas** entre elles car elles ne s'appliquent pas au même système !

---

## Résultante des forces

Lorsque plusieurs forces s'exercent sur un même système, on peut les combiner en une **résultante** :

$$\\sum \\vec{F} = \\vec{F}_1 + \\vec{F}_2 + \\vec{F}_3 + \\cdots$$

La résultante se calcule par **addition vectorielle**. Si $\\sum \\vec{F} = \\vec{0}$, on dit que les forces se **compensent**.

---

## À retenir

- Une **force** modélise une action mécanique ; c'est un vecteur (point d'application, direction, sens, norme en N).
- On distingue les forces **de contact** (réaction, frottement, tension) et les forces **à distance** (gravitation, électrostatique, magnétique).
- Le **principe des actions réciproques** : $\\vec{F}_{A/B} = -\\vec{F}_{B/A}$.
- Toujours commencer par un **inventaire des forces** (DOI) avant d'analyser un mouvement.
""",
                'quiz': {
                    'titre': "Quiz — Généralités sur les forces",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Une force est modélisée par :",
                            'options': ["Un vecteur", "Un scalaire", "Une trajectoire", "Un référentiel"],
                            'reponse_correcte': '0',
                            'explication': "Une force est un vecteur, caractérisé par un point d'application, une direction, un sens et une norme.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "L'unité de la force dans le Système International est :",
                            'options': ["Le newton (N)", "Le kilogramme (kg)", "Le joule (J)", "Le mètre par seconde (m/s)"],
                            'reponse_correcte': '0',
                            'explication': "L'unité de force dans le SI est le newton (N).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Parmi ces forces, laquelle est une force à distance ?",
                            'options': ["La force gravitationnelle", "La tension d'un fil", "La réaction du support", "La force de frottement"],
                            'reponse_correcte': '0',
                            'explication': "La force gravitationnelle s'exerce entre deux masses sans contact physique.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Une action mécanique peut :",
                            'options': ["Mettre en mouvement, modifier le mouvement ou déformer un objet", "Uniquement mettre un objet en mouvement", "Uniquement déformer un objet", "Modifier la masse d'un objet"],
                            'reponse_correcte': '0',
                            'explication': "Une action mécanique peut mettre en mouvement, modifier le mouvement ou déformer un objet.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La force exercée par A sur B se note :",
                            'options': ["F(A/B)", "F(B/A)", "F(A+B)", "F(A×B)"],
                            'reponse_correcte': '0',
                            'explication': "La notation F(A/B) se lit « force exercée par A sur B ».",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quel instrument permet de mesurer l'intensité d'une force ?",
                            'options': ["Un dynamomètre", "Une balance", "Un thermomètre", "Un voltmètre"],
                            'reponse_correcte': '0',
                            'explication': "Le dynamomètre mesure l'intensité d'une force grâce à l'allongement d'un ressort, gradué en newtons.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "La tension d'un fil est une force :",
                            'options': ["De contact", "À distance", "Gravitationnelle", "Électrostatique"],
                            'reponse_correcte': '0',
                            'explication': "La tension d'un fil nécessite un contact physique entre le fil et l'objet accroché.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Selon le principe des actions réciproques, si A exerce une force de 50 N sur B, alors B exerce sur A une force de :",
                            'options': ["50 N en sens opposé", "50 N dans le même sens", "25 N en sens opposé", "100 N en sens opposé"],
                            'reponse_correcte': '0',
                            'explication': "D'après la 3ème loi de Newton, B exerce sur A une force de même norme (50 N) mais de sens opposé.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Quelles sont les quatre caractéristiques d'une force ?",
                            'options': ["Point d'application, direction, sens, norme", "Masse, direction, sens, norme", "Point d'application, trajectoire, vitesse, norme", "Direction, sens, norme, énergie"],
                            'reponse_correcte': '0',
                            'explication': "Une force est définie par son point d'application, sa direction, son sens et sa norme (en newtons).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Dans un diagramme objet-interactions (DOI), on identifie pour chaque interaction :",
                            'options': ["Si elle est de contact ou à distance", "Uniquement la masse des objets", "La trajectoire du système", "La vitesse du système"],
                            'reponse_correcte': '0',
                            'explication': "Le DOI recense toutes les interactions et précise leur nature : contact ou distance.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Les deux forces réciproques (3ème loi de Newton) ont la même droite d'action. Elles :",
                            'options': ["S'exercent sur deux objets différents", "S'exercent sur le même objet", "S'annulent toujours", "Ont des normes différentes"],
                            'reponse_correcte': '0',
                            'explication': "Les forces réciproques s'exercent sur deux objets différents (A sur B et B sur A), elles ne s'annulent donc pas.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "On dit que les forces se compensent sur un système lorsque :",
                            'options': ["La résultante des forces est nulle", "Une seule force s'exerce sur le système", "Toutes les forces sont de contact", "Le système est en mouvement accéléré"],
                            'reponse_correcte': '0',
                            'explication': "Les forces se compensent quand leur somme vectorielle (résultante) est le vecteur nul.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Parmi ces forces, laquelle est une force de contact ?",
                            'options': ["La force de frottement", "La force gravitationnelle", "La force électrostatique", "La force magnétique"],
                            'reponse_correcte': '0',
                            'explication': "Le frottement nécessite un contact entre les surfaces : c'est une force de contact.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Les deux forces du principe des actions réciproques s'exercent sur le même objet et s'annulent.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Les deux forces réciproques s'exercent sur deux objets différents. Elles ne s'annulent pas.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "La force magnétique exercée par un aimant sur un clou en fer est une force à distance.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "La force magnétique s'exerce sans contact physique direct entre l'aimant et le clou.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Sur un schéma, la longueur de la flèche représentant une force est proportionnelle à son intensité.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "On choisit une échelle (ex : 1 cm pour 2 N) et la longueur de la flèche est proportionnelle à la norme de la force.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "La résultante des forces est la somme algébrique des normes de toutes les forces.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La résultante est la somme vectorielle des forces, pas la somme de leurs normes.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quel est le nom de la troisième loi de Newton ?",
                            'options': None,
                            'reponse_correcte': "principe des actions réciproques",
                            'tolerances': ["actions réciproques", "actions reciproques", "principe des actions reciproques", "action-réaction", "action réaction", "action reaction"],
                            'explication': "La 3ème loi de Newton est le principe des actions réciproques (ou loi d'action-réaction).",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on l'instrument qui mesure l'intensité d'une force ?",
                            'options': None,
                            'reponse_correcte': 'dynamomètre',
                            'tolerances': ["dynamometre", "un dynamomètre", "un dynamometre", "le dynamomètre"],
                            'explication': "Le dynamomètre est l'instrument qui mesure l'intensité d'une force, gradué en newtons.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quelle est l'unité de la force dans le Système International ? (symbole)",
                            'options': None,
                            'reponse_correcte': 'N',
                            'tolerances': ["newton", "Newton", "le newton", "newtons"],
                            'explication': "L'unité de force est le newton, de symbole N.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Gravitation, poids et réaction du support',
                'duree': 40,
                'contenu': """# Gravitation, poids et réaction du support

## Introduction

Parmi toutes les forces, trois sont particulièrement importantes en mécanique de Seconde : la **force gravitationnelle**, le **poids** et la **réaction du support**. Cette leçon les détaille et montre comment les calculer.

---

## L'interaction gravitationnelle

### La loi de la gravitation universelle

Deux corps de masses $m_1$ et $m_2$, séparés par une distance $d$ (mesurée entre leurs centres), exercent l'un sur l'autre des forces attractives dont la norme est :

$$F = G \\frac{m_1 \\cdot m_2}{d^2}$$

| Grandeur | Symbole | Unité |
|---|---|---|
| Force gravitationnelle | $F$ | newton (N) |
| Constante de gravitation universelle | $G$ | N·m²·kg⁻² |
| Masses des corps | $m_1$, $m_2$ | kilogramme (kg) |
| Distance entre les centres | $d$ | mètre (m) |

La valeur de la constante de gravitation est :

$$G = 6{,}674 \\times 10^{-11} \\text{ N·m}^2\\text{·kg}^{-2}$$

### Propriétés

- La force gravitationnelle est **toujours attractive**.
- Elle s'exerce entre **toutes les masses** de l'Univers.
- Elle diminue quand la distance augmente (en $\\frac{1}{d^2}$).
- Elle est réciproque : $A$ attire $B$ autant que $B$ attire $A$ (3ᵉ loi de Newton).

### Exemple numérique

Calculons la force gravitationnelle entre la Terre ($m_T = 5{,}97 \\times 10^{24}$ kg) et la Lune ($m_L = 7{,}35 \\times 10^{22}$ kg), distantes de $d = 3{,}84 \\times 10^8$ m :

$$F = G \\frac{m_T \\cdot m_L}{d^2} = 6{,}674 \\times 10^{-11} \\times \\frac{5{,}97 \\times 10^{24} \\times 7{,}35 \\times 10^{22}}{(3{,}84 \\times 10^8)^2}$$

$$F \\approx 1{,}98 \\times 10^{20} \\text{ N}$$

C'est cette force qui maintient la Lune en orbite autour de la Terre.

---

## Le poids

### Définition

Le **poids** $\\vec{P}$ d'un corps est la force d'attraction gravitationnelle exercée par la Terre (ou tout autre astre) sur ce corps, à proximité de sa surface. Il est donné par :

$$\\vec{P} = m\\vec{g}$$

| Grandeur | Symbole | Unité |
|---|---|---|
| Poids | $P$ | newton (N) |
| Masse | $m$ | kilogramme (kg) |
| Intensité de pesanteur | $g$ | m/s² (ou N/kg) |

### L'intensité de pesanteur $g$

À la surface de la Terre : $g \\approx 9{,}81$ m/s² (souvent arrondi à $9{,}8$ ou $10$ m/s²).

Le poids dérive de la loi de gravitation. En assimilant le corps à une masse ponctuelle à la distance $R_T$ (rayon de la Terre) du centre de la Terre :

$$P = G \\frac{m_T \\cdot m}{R_T^2} = m \\cdot \\underbrace{G \\frac{m_T}{R_T^2}}_{= g}$$

Donc :

$$g = G \\frac{m_T}{R_T^2}$$

### Caractéristiques du vecteur poids

- **Point d'application** : centre de gravité du corps.
- **Direction** : verticale (la droite passant par le centre de la Terre et le corps).
- **Sens** : vers le bas (vers le centre de la Terre).
- **Norme** : $P = mg$ en newtons.

### Variation de $g$

La valeur de $g$ varie selon :

- l'**altitude** : plus on s'élève, plus $g$ diminue ;
- la **latitude** : $g$ est légèrement plus fort aux pôles ($g \\approx 9{,}83$ m/s²) qu'à l'équateur ($g \\approx 9{,}78$ m/s²) ;
- l'**astre** : sur la Lune, $g_L \\approx 1{,}62$ m/s² ; sur Mars, $g_M \\approx 3{,}72$ m/s².

| Lieu | $g$ (m/s²) |
|---|---|
| Terre (surface) | 9,81 |
| Lune | 1,62 |
| Mars | 3,72 |
| Jupiter | 24,8 |

---

## Poids et masse : ne pas confondre !

| | **Masse** | **Poids** |
|---|---|---|
| Nature | Quantité de matière | Force |
| Unité | kilogramme (kg) | newton (N) |
| Instrument | Balance | Dynamomètre |
| Dépend du lieu ? | Non (invariante) | Oui (dépend de $g$) |

> Un astronaute de 80 kg a une masse de 80 kg sur la Terre **et** sur la Lune. Mais son poids passe de $80 \\times 9{,}81 = 785$ N sur Terre à $80 \\times 1{,}62 = 130$ N sur la Lune.

---

## La réaction du support

### Définition

Lorsqu'un objet est posé sur un support (table, sol, plan incliné…), le support exerce sur l'objet une force de contact appelée **réaction du support**, notée $\\vec{R}$.

### Décomposition de la réaction

La réaction se décompose en deux composantes :

- La **réaction normale** $\\vec{R}_N$ : perpendiculaire à la surface de contact. Elle empêche l'objet de « traverser » le support.
- La **force de frottement** $\\vec{f}$ : parallèle à la surface de contact. Elle s'oppose au glissement (ou à la tendance au glissement).

$$\\vec{R} = \\vec{R}_N + \\vec{f}$$

### Cas d'un plan horizontal sans frottement

Si la surface est horizontale et qu'il n'y a pas de frottement, la réaction est purement **normale** et **verticale** :

$$\\vec{R} = \\vec{R}_N$$

Pour un objet en **équilibre** sur un plan horizontal :

$$\\vec{P} + \\vec{R} = \\vec{0}$$

Donc $\\vec{R} = -\\vec{P}$, ce qui signifie que la réaction a la même norme que le poids ($R = P = mg$) mais est dirigée vers le haut.

---

## Exemple complet : objet posé sur une table

Un livre de masse $m = 0{,}8$ kg est posé sur une table. On prend $g = 9{,}8$ m/s².

**Inventaire des forces :**

1. Poids : $\\vec{P}$ (vertical, vers le bas)
   - $P = mg = 0{,}8 \\times 9{,}8 = 7{,}84$ N
2. Réaction de la table : $\\vec{R}$ (vertical, vers le haut)

**Condition d'équilibre :** $\\vec{P} + \\vec{R} = \\vec{0}$, donc $R = P = 7{,}84$ N.

---

## Application : calculer une force gravitationnelle

Deux boules de bowling identiques de masse $m = 7{,}0$ kg sont posées à $d = 0{,}50$ m l'une de l'autre. Calculons la force gravitationnelle entre elles :

$$F = G \\frac{m^2}{d^2} = 6{,}674 \\times 10^{-11} \\times \\frac{7{,}0^2}{0{,}50^2}$$

$$F = 6{,}674 \\times 10^{-11} \\times \\frac{49}{0{,}25} = 6{,}674 \\times 10^{-11} \\times 196$$

$$F \\approx 1{,}3 \\times 10^{-8} \\text{ N}$$

Cette force est **extrêmement faible** et imperceptible au quotidien. La gravitation ne devient significative qu'avec des masses très grandes (planètes, étoiles…).

---

## À retenir

- **Gravitation universelle** : $F = G \\frac{m_1 m_2}{d^2}$, toujours attractive.
- **Poids** : $\\vec{P} = m\\vec{g}$, force verticale vers le bas, $g \\approx 9{,}81$ m/s² sur Terre.
- **Masse** (kg) ≠ **Poids** (N) : la masse est invariante, le poids dépend du lieu.
- **Réaction du support** $\\vec{R}$ : perpendiculaire au support (+ frottement si glissement).
- À l'**équilibre** sur un plan horizontal : $\\vec{P} + \\vec{R} = \\vec{0}$.
""",
                'quiz': {
                    'titre': "Quiz — Gravitation, poids et réaction du support",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "La force gravitationnelle entre deux corps est :",
                            'options': ["Toujours attractive", "Toujours répulsive", "Attractive ou répulsive selon les masses", "Nulle si les masses sont égales"],
                            'reponse_correcte': '0',
                            'explication': "La force gravitationnelle est toujours attractive : deux masses s'attirent mutuellement.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "La formule de la loi de gravitation universelle est :",
                            'options': ["F = G × m₁ × m₂ / d²", "F = G × m₁ × m₂ × d²", "F = G × (m₁ + m₂) / d", "F = m₁ × m₂ / G"],
                            'reponse_correcte': '0',
                            'explication': "La loi de la gravitation universelle s'écrit F = G × m₁ × m₂ / d².",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Le poids d'un objet se calcule avec la formule :",
                            'options': ["P = m × g", "P = m / g", "P = m × g²", "P = m + g"],
                            'reponse_correcte': '0',
                            'explication': "Le poids est le produit de la masse par l'intensité de pesanteur : P = m × g.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "L'unité du poids est :",
                            'options': ["Le newton (N)", "Le kilogramme (kg)", "Le mètre par seconde (m/s)", "Le pascal (Pa)"],
                            'reponse_correcte': '0',
                            'explication': "Le poids est une force, il s'exprime en newtons (N).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Sur Terre, la valeur approchée de l'intensité de pesanteur g est :",
                            'options': ["9,81 m/s²", "6,67 × 10⁻¹¹ m/s²", "3,72 m/s²", "1,62 m/s²"],
                            'reponse_correcte': '0',
                            'explication': "À la surface de la Terre, g ≈ 9,81 m/s².",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Le poids d'un objet de 5 kg sur Terre (g = 10 m/s²) vaut :",
                            'options': ["50 N", "5 N", "0,5 N", "500 N"],
                            'reponse_correcte': '0',
                            'explication': "P = m × g = 5 × 10 = 50 N.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Le vecteur poids est dirigé :",
                            'options': ["Verticalement vers le bas", "Verticalement vers le haut", "Horizontalement", "Tangentiellement à la trajectoire"],
                            'reponse_correcte': '0',
                            'explication': "Le poids est dirigé vers le centre de la Terre, c'est-à-dire verticalement vers le bas.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "La réaction normale d'un support est :",
                            'options': ["Perpendiculaire à la surface de contact", "Parallèle à la surface de contact", "Verticale dans tous les cas", "Nulle si l'objet est en équilibre"],
                            'reponse_correcte': '0',
                            'explication': "La composante normale de la réaction est toujours perpendiculaire à la surface de contact.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Si la distance entre deux astres double, la force gravitationnelle entre eux :",
                            'options': ["Est divisée par 4", "Est divisée par 2", "Est multipliée par 2", "Est multipliée par 4"],
                            'reponse_correcte': '0',
                            'explication': "La force varie en 1/d². Si d est multiplié par 2, la force est divisée par 2² = 4.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Un astronaute de 70 kg se trouve sur la Lune (g = 1,62 m/s²). Son poids lunaire est environ :",
                            'options': ["113 N", "687 N", "70 N", "11,3 N"],
                            'reponse_correcte': '0',
                            'explication': "P = m × g = 70 × 1,62 = 113,4 N ≈ 113 N.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "La masse d'un objet sur la Lune comparée à sa masse sur Terre est :",
                            'options': ["Identique", "Six fois plus faible", "Six fois plus grande", "Variable selon l'altitude"],
                            'reponse_correcte': '0',
                            'explication': "La masse est une propriété intrinsèque de la matière, elle ne change pas selon le lieu.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Pour un objet en équilibre sur un plan horizontal sans frottement, on a :",
                            'options': ["P + R = 0 (les forces se compensent)", "P = 0", "R = 0", "P = 2R"],
                            'reponse_correcte': '0',
                            'explication': "À l'équilibre, la résultante des forces est nulle : le poids et la réaction se compensent.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "La constante de gravitation universelle G vaut environ :",
                            'options': ["6,67 × 10⁻¹¹ N·m²·kg⁻²", "9,81 N·m²·kg⁻²", "6,67 × 10¹¹ N·m²·kg⁻²", "3,00 × 10⁸ N·m²·kg⁻²"],
                            'reponse_correcte': '0',
                            'explication': "G = 6,674 × 10⁻¹¹ N·m²·kg⁻², une valeur très petite.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Le poids d'un objet est le même sur la Terre et sur la Lune.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le poids dépend de g qui varie selon le lieu. Sur la Lune, g ≈ 1,62 m/s² contre 9,81 m/s² sur Terre.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "La masse d'un objet change lorsqu'on le transporte sur un autre astre.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La masse est invariante. C'est le poids (P = mg) qui change car g varie d'un astre à l'autre.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La réaction du support peut se décomposer en une composante normale et une composante de frottement.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "La réaction R se décompose en réaction normale R_N (perpendiculaire) et force de frottement f (parallèle à la surface).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "La force gravitationnelle entre deux boules de bowling posées côte à côte est facilement perceptible au quotidien.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La force gravitationnelle entre des objets de masse ordinaire est extrêmement faible (de l'ordre de 10⁻⁸ N) et totalement imperceptible.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer le poids d'un objet de masse 3 kg sur Terre (g = 10 m/s²). Donner la valeur en N.",
                            'options': None,
                            'reponse_correcte': '30',
                            'tolerances': ["30 N", "30,0", "30.0", "30 n"],
                            'explication': "P = m × g = 3 × 10 = 30 N.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Quel instrument mesure le poids d'un objet ?",
                            'options': None,
                            'reponse_correcte': 'dynamomètre',
                            'tolerances': ["dynamometre", "un dynamomètre", "un dynamometre", "le dynamomètre"],
                            'explication': "Le dynamomètre mesure le poids (force), contrairement à la balance qui mesure la masse.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quelle lettre désigne la constante de gravitation universelle ?",
                            'options': None,
                            'reponse_correcte': 'G',
                            'tolerances': ["g majuscule"],
                            'explication': "La constante de gravitation universelle est notée G (majuscule), à ne pas confondre avec g (minuscule, intensité de pesanteur).",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 3 — Le principe d'inertie
    # ──────────────────────────────────────────────
    {
        'ordre': 3,
        'titre': "Le principe d'inertie",
        'description': "Comprendre le principe d'inertie (1ère loi de Newton), identifier un référentiel galiléen et analyser la chute libre.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Référentiel galiléen et principe d'inertie",
                'duree': 35,
                'contenu': """# Référentiel galiléen et principe d'inertie

## Introduction

Pourquoi un objet continue-t-il à avancer quand on cesse de le pousser ? Pourquoi un livre posé sur une table reste-t-il immobile ? Le **principe d'inertie**, ou première loi de Newton, répond à ces questions fondamentales.

---

## Le référentiel galiléen

### Définition

Un **référentiel galiléen** est un référentiel dans lequel le **principe d'inertie est vérifié**. Autrement dit, c'est un référentiel dans lequel un objet soumis à aucune force (ou à des forces qui se compensent) reste immobile ou en mouvement rectiligne uniforme.

### Exemples

- Le **référentiel héliocentrique** (centré sur le Soleil) est un excellent référentiel galiléen.
- Le **référentiel géocentrique** (centré sur la Terre) est galiléen en bonne approximation.
- Le **référentiel terrestre** (lié au sol) est considéré comme galiléen pour des expériences de **courte durée** (quelques heures) et de **faible étendue**.

### Contre-exemple

Un manège en rotation n'est **pas** un référentiel galiléen. Un objet lâché dans un manège en rotation ne se déplace pas en ligne droite par rapport au manège, même en l'absence de toute force horizontale.

---

## Le principe d'inertie (1ère loi de Newton)

### Énoncé

> Dans un **référentiel galiléen**, si la somme des forces extérieures appliquées à un système est nulle ($\\sum \\vec{F} = \\vec{0}$), alors le centre de masse du système est soit **au repos**, soit en **mouvement rectiligne uniforme** (MRU).

$$\\sum \\vec{F}_{\\text{ext}} = \\vec{0} \\implies \\text{repos ou MRU}$$

### L'inertie : une propriété de la matière

L'**inertie** est la tendance d'un corps à conserver son état de repos ou de mouvement. Plus un objet est **massif**, plus son inertie est grande, et plus il est difficile de modifier son mouvement.

> **Exemple quotidien :** dans un bus qui freine brusquement, votre corps continue d'avancer (par inertie) alors que le bus ralentit.

---

## La réciproque du principe d'inertie

La réciproque est tout aussi importante :

> Si un objet est au repos ou en MRU dans un référentiel galiléen, alors la somme des forces qui s'exercent sur lui est nulle.

$$\\text{repos ou MRU} \\implies \\sum \\vec{F}_{\\text{ext}} = \\vec{0}$$

### Application : objet en équilibre

Un lustre suspendu au plafond est **au repos**. D'après la réciproque du principe d'inertie, les forces se compensent :

$$\\vec{P} + \\vec{T} = \\vec{0}$$

où $\\vec{P}$ est le poids (vers le bas) et $\\vec{T}$ la tension du fil (vers le haut). Donc $T = P = mg$.

---

## La contraposée du principe d'inertie

La **contraposée** permet de raisonner lorsque le mouvement n'est pas un MRU :

> Si le mouvement d'un objet **n'est pas rectiligne uniforme** dans un référentiel galiléen, alors la somme des forces qui s'exercent sur lui **n'est pas nulle**.

$$\\text{pas MRU} \\implies \\sum \\vec{F}_{\\text{ext}} \\neq \\vec{0}$$

### Exemples d'application

| Situation | Type de mouvement | Les forces se compensent-elles ? |
|---|---|---|
| Livre posé sur une table | Repos | Oui : $\\vec{P} + \\vec{R} = \\vec{0}$ |
| Voiture à 90 km/h en ligne droite | MRU | Oui (moteur compense les frottements) |
| Balle en chute libre | Rectiligne accéléré | Non : seul le poids agit |
| Satellite en orbite circulaire | Circulaire | Non : la gravitation change la direction |
| Voiture qui freine | Rectiligne décéléré | Non : frottements > force motrice |

---

## Le vecteur variation de vitesse

### Définition

Entre deux instants $t_i$ et $t_f$, la **variation du vecteur vitesse** est :

$$\\Delta \\vec{v} = \\vec{v}_f - \\vec{v}_i$$

### Interprétation

- Si $\\Delta \\vec{v} = \\vec{0}$ : le vecteur vitesse ne change ni en norme, ni en direction → **MRU** → $\\sum \\vec{F} = \\vec{0}$.
- Si $\\Delta \\vec{v} \\neq \\vec{0}$ : le mouvement n'est pas un MRU → $\\sum \\vec{F} \\neq \\vec{0}$.

La direction de $\\Delta \\vec{v}$ donne une indication sur la direction de la **résultante des forces**.

### Construction graphique

Pour tracer $\\Delta \\vec{v} = \\vec{v}_f - \\vec{v}_i$ :

1. Placer $\\vec{v}_i$ et $\\vec{v}_f$ **à la même origine**.
2. Tracer le vecteur allant de l'**extrémité** de $\\vec{v}_i$ vers l'**extrémité** de $\\vec{v}_f$.

---

## Exemples complets

### Exemple 1 : palet sur coussin d'air (mouvement rectiligne uniforme)

Un palet sur une table à coussin d'air horizontale est lancé. En l'absence de frottements, le palet avance en **ligne droite** à **vitesse constante**.

**Analyse :**
- Système : le palet.
- Forces : poids $\\vec{P}$ (vers le bas) et réaction de la table $\\vec{R}$ (vers le haut).
- $\\vec{P} + \\vec{R} = \\vec{0}$ → les forces se compensent.
- D'après le principe d'inertie : le palet est en MRU ✓

### Exemple 2 : voiture qui accélère

Une voiture accélère sur une route rectiligne.

**Analyse :**
- Son mouvement est rectiligne **accéléré** (vitesse augmente).
- Ce n'est pas un MRU → d'après la contraposée, $\\sum \\vec{F} \\neq \\vec{0}$.
- La force motrice est **supérieure** aux forces de frottement.

---

## À retenir

- Un **référentiel galiléen** est un référentiel où le principe d'inertie est vérifié (terrestre ≈ galiléen pour des expériences courtes).
- **Principe d'inertie** : $\\sum \\vec{F} = \\vec{0} \\iff$ repos ou MRU (dans un référentiel galiléen).
- **Contraposée** : mouvement non-MRU → les forces ne se compensent pas.
- L'**inertie** est la tendance d'un corps à résister aux changements de mouvement ; elle est liée à la masse.
- $\\Delta \\vec{v} = \\vec{v}_f - \\vec{v}_i$ renseigne sur la résultante des forces.
""",
                'quiz': {
                    'titre': "Quiz — Référentiel galiléen et principe d'inertie",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Qu'est-ce qu'un référentiel galiléen ?",
                            'options': ["Un référentiel dans lequel le principe d'inertie est vérifié", "Un référentiel lié au Soleil", "Un référentiel en rotation", "Un référentiel immobile par rapport à la Terre"],
                            'reponse_correcte': '0',
                            'explication': "Un référentiel galiléen est un référentiel dans lequel le principe d'inertie est valable.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Le référentiel terrestre est considéré comme galiléen :",
                            'options': ["Pour des expériences de courte durée et de faible étendue", "Uniquement au pôle Nord", "Pour toutes les expériences sans exception", "Jamais"],
                            'reponse_correcte': '0',
                            'explication': "Le référentiel terrestre est une bonne approximation d'un référentiel galiléen pour des durées courtes et des distances faibles.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "D'après le principe d'inertie, si la somme des forces extérieures est nulle, le système est :",
                            'options': ["Au repos ou en mouvement rectiligne uniforme", "Toujours au repos", "Toujours en mouvement", "En mouvement circulaire uniforme"],
                            'reponse_correcte': '0',
                            'explication': "Le principe d'inertie affirme que si la résultante des forces est nulle, le système est au repos ou en MRU.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Le principe d'inertie est aussi appelé :",
                            'options': ["Première loi de Newton", "Deuxième loi de Newton", "Troisième loi de Newton", "Loi de Galilée"],
                            'reponse_correcte': '0',
                            'explication': "Le principe d'inertie correspond à la première loi de Newton.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Un manège en rotation est-il un référentiel galiléen ?",
                            'options': ["Non, car un objet lâché ne se déplace pas en ligne droite", "Oui, car il tourne à vitesse constante", "Oui, si la durée est courte", "Non, car il est trop petit"],
                            'reponse_correcte': '0',
                            'explication': "Un manège en rotation n'est pas galiléen : un objet lâché ne suit pas une trajectoire rectiligne dans ce référentiel.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "L'inertie d'un corps est d'autant plus grande que :",
                            'options': ["Sa masse est grande", "Sa vitesse est faible", "Sa taille est petite", "Sa température est élevée"],
                            'reponse_correcte': '0',
                            'explication': "L'inertie est la tendance d'un corps à résister au changement de mouvement ; elle est directement liée à la masse.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Un livre posé sur une table est immobile. D'après la réciproque du principe d'inertie :",
                            'options': ["La somme des forces est nulle : le poids et la réaction se compensent", "Aucune force ne s'exerce sur le livre", "Le poids est nul", "La réaction de la table est supérieure au poids"],
                            'reponse_correcte': '0',
                            'explication': "Le livre est au repos, donc les forces se compensent : P + R = 0.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Dans un bus qui freine brusquement, un passager debout est projeté vers l'avant. Cela s'explique par :",
                            'options': ["L'inertie du passager qui tend à conserver son mouvement", "Une force qui pousse le passager vers l'avant", "Le principe d'action-réaction", "L'attraction gravitationnelle du bus"],
                            'reponse_correcte': '0',
                            'explication': "Par inertie, le corps du passager tend à conserver son état de mouvement initial (vers l'avant), alors que le bus décélère.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Si le mouvement d'un objet n'est pas rectiligne uniforme dans un référentiel galiléen, on peut conclure que :",
                            'options': ["La somme des forces n'est pas nulle", "L'objet est au repos", "Les forces se compensent", "L'objet est dans un référentiel non galiléen"],
                            'reponse_correcte': '0',
                            'explication': "C'est la contraposée du principe d'inertie : pas de MRU → résultante des forces non nulle.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Une voiture roule à 90 km/h en ligne droite sur autoroute. Si les forces se compensent, son mouvement est :",
                            'options': ["Rectiligne uniforme", "Rectiligne accéléré", "Circulaire uniforme", "Décéléré"],
                            'reponse_correcte': '0',
                            'explication': "Vitesse constante en ligne droite = MRU, cohérent avec la compensation des forces (force motrice = frottements).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "La variation du vecteur vitesse entre deux instants est définie par :",
                            'options': ["Δv⃗ = v⃗f − v⃗i", "Δv⃗ = v⃗f + v⃗i", "Δv⃗ = v⃗i − v⃗f", "Δv⃗ = v⃗f × v⃗i"],
                            'reponse_correcte': '0',
                            'explication': "La variation du vecteur vitesse est la différence entre le vecteur vitesse final et le vecteur vitesse initial.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Un palet lancé sur une table à coussin d'air horizontale (sans frottements) a un mouvement :",
                            'options': ["Rectiligne uniforme, car les forces verticales se compensent et il n'y a pas de force horizontale", "Décéléré, car il finit par s'arrêter", "Accéléré, car le coussin le propulse", "Circulaire, à cause du coussin d'air"],
                            'reponse_correcte': '0',
                            'explication': "Sans frottements, poids et réaction se compensent ; aucune force horizontale → MRU d'après le principe d'inertie.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Pour construire graphiquement Δv⃗ = v⃗f − v⃗i, on place v⃗i et v⃗f à la même origine, puis on trace le vecteur allant :",
                            'options': ["De l'extrémité de v⃗i vers l'extrémité de v⃗f", "De l'origine commune vers l'extrémité de v⃗f", "De l'extrémité de v⃗f vers l'extrémité de v⃗i", "De l'extrémité de v⃗i vers l'origine"],
                            'reponse_correcte': '0',
                            'explication': "On place les deux vecteurs à la même origine, puis le vecteur Δv⃗ va de l'extrémité de v⃗i à celle de v⃗f.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Un satellite en orbite circulaire autour de la Terre a une vitesse de norme constante. Les forces se compensent-elles ?",
                            'options': ["Non, car la direction du vecteur vitesse change en permanence", "Oui, car la norme de la vitesse est constante", "Oui, car le satellite ne tombe pas", "Non, car le satellite accélère en permanence en norme"],
                            'reponse_correcte': '0',
                            'explication': "Le mouvement circulaire n'est pas rectiligne → d'après la contraposée, les forces ne se compensent pas (la gravitation maintient la trajectoire circulaire).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Le principe d'inertie n'est valable que dans un référentiel galiléen.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Le principe d'inertie est énoncé dans un référentiel galiléen ; dans un référentiel non galiléen, il faut ajouter des forces fictives.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Si un objet est en mouvement rectiligne uniforme, alors la somme des forces qui s'exercent sur lui est nulle.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est la réciproque du principe d'inertie : repos ou MRU ⟹ somme des forces = 0.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Un objet soumis à des forces qui ne se compensent pas peut être en mouvement rectiligne uniforme.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Si la résultante des forces est non nulle, le mouvement ne peut pas être un MRU dans un référentiel galiléen.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on la première loi de Newton ?",
                            'options': None,
                            'reponse_correcte': "principe d'inertie",
                            'tolerances': ["le principe d'inertie", "principe d inertie", "le principe d inertie", "loi d'inertie"],
                            'explication': "La première loi de Newton est le principe d'inertie.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Quel type de mouvement a un objet quand la somme des forces est nulle et qu'il n'est pas au repos ?",
                            'options': None,
                            'reponse_correcte': 'rectiligne uniforme',
                            'tolerances': ["mouvement rectiligne uniforme", "MRU", "mru", "un mouvement rectiligne uniforme"],
                            'explication': "Si la résultante des forces est nulle et l'objet est en mouvement, il est en mouvement rectiligne uniforme.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Un lustre suspendu au plafond est au repos. Quelle relation vectorielle lie le poids P⃗ et la tension du fil T⃗ ?",
                            'options': None,
                            'reponse_correcte': 'P + T = 0',
                            'tolerances': ["P+T=0", "T+P=0", "P = -T", "T = -P", "P⃗ + T⃗ = 0⃗"],
                            'explication': "Le lustre est au repos, donc d'après la réciproque du principe d'inertie, P⃗ + T⃗ = 0⃗.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Chute libre et mouvements variés',
                'duree': 40,
                'contenu': """# Chute libre et mouvements variés

## Introduction

Le principe d'inertie permet de prédire le mouvement d'un objet quand les forces se compensent. Mais que se passe-t-il quand elles **ne se compensent pas** ? Le cas le plus simple et le plus fondamental est celui de la **chute libre** : un objet soumis uniquement à son poids.

---

## La chute libre

### Définition

Un objet est en **chute libre** lorsqu'il n'est soumis qu'à son **poids** $\\vec{P} = m\\vec{g}$. On néglige toutes les autres forces (frottements de l'air, poussée d'Archimède…).

> ⚠️ « Chute libre » ne signifie pas forcément « tomber vers le bas ». Un objet lancé vers le haut est aussi en chute libre tant qu'il n'est soumis qu'à la gravité (phase ascendante comprise).

### Conditions de validité

L'approximation de la chute libre est bonne quand :

- L'objet est **dense** et **compact** (frottements de l'air négligeables).
- La vitesse n'est pas trop grande (sinon les frottements deviennent significatifs).
- L'objet se déplace **dans le vide** (expérience du tube de Newton).

---

## Chute libre verticale (sans vitesse initiale horizontale)

### Situation

Un objet de masse $m$ est **lâché sans vitesse initiale** (ou lancé verticalement) depuis une hauteur $h$. On choisit un axe vertical $(Oz)$ orienté **vers le bas** avec l'origine au point de lâcher.

### Analyse des forces

- Système : l'objet de masse $m$.
- Seule force : $\\vec{P} = m\\vec{g}$ (vers le bas).
- D'après la contraposée du principe d'inertie : $\\sum \\vec{F} = \\vec{P} \\neq \\vec{0}$ → le mouvement **n'est pas** un MRU.

### Résultats (admis en Seconde)

L'objet subit une **accélération constante** $a = g \\approx 9{,}81$ m/s² dirigée vers le bas.

La **vitesse** augmente linéairement avec le temps :

$$v(t) = g \\cdot t$$

La **position** (distance parcourue depuis le point de lâcher) évolue de façon quadratique :

$$z(t) = \\frac{1}{2} g \\cdot t^2$$

| Temps $t$ (s) | Vitesse $v$ (m/s) | Distance $z$ (m) |
|---|---|---|
| 0 | 0 | 0 |
| 1 | 9,81 | 4,9 |
| 2 | 19,6 | 19,6 |
| 3 | 29,4 | 44,1 |
| 4 | 39,2 | 78,5 |
| 5 | 49,1 | 122,6 |

> La vitesse augmente de $\\approx 9{,}8$ m/s **chaque seconde**. En 5 secondes, l'objet atteint environ 177 km/h !

### Propriété fondamentale

En chute libre, **tous les objets tombent à la même vitesse**, indépendamment de leur masse (en l'absence de frottements). C'est ce que Galilée a démontré au XVIᵉ siècle et que les astronautes d'Apollo 15 ont vérifié sur la Lune en lâchant un marteau et une plume.

---

## La chute libre avec vitesse initiale

### Lancer vertical vers le haut

Un objet est lancé verticalement vers le haut avec une vitesse initiale $v_0$. Prenons l'axe $(Oz)$ orienté vers le **haut**.

- **Phase ascendante** : la vitesse diminue ($g$ s'oppose au mouvement).
- **Au sommet** : la vitesse s'annule ($v = 0$).
- **Phase descendante** : la vitesse augmente vers le bas.

Les équations deviennent :

$$v(t) = v_0 - g \\cdot t$$

$$z(t) = v_0 \\cdot t - \\frac{1}{2} g \\cdot t^2$$

La **hauteur maximale** est atteinte quand $v = 0$, soit à $t_{\\max} = \\frac{v_0}{g}$ :

$$z_{\\max} = \\frac{v_0^2}{2g}$$

### Exemple numérique

On lance une balle verticalement vers le haut avec $v_0 = 15$ m/s. Quelle hauteur maximale atteint-elle ?

$$z_{\\max} = \\frac{v_0^2}{2g} = \\frac{15^2}{2 \\times 9{,}81} = \\frac{225}{19{,}62} \\approx 11{,}5 \\text{ m}$$

---

## Le mouvement circulaire

### Observation

Un objet en mouvement circulaire (ex : un satellite, une nacelle de manège) a un vecteur vitesse dont la **direction change** en permanence, même si la **norme** reste constante.

### Analyse avec le principe d'inertie

Puisque le vecteur vitesse **change de direction**, le mouvement n'est **pas rectiligne** uniforme. D'après la contraposée du principe d'inertie :

$$\\sum \\vec{F} \\neq \\vec{0}$$

Les forces ne se compensent pas, même si la vitesse (en norme) est constante !

### Cas du satellite en orbite circulaire

Un satellite en orbite circulaire autour de la Terre a une vitesse de norme constante, mais la direction du vecteur vitesse change continuellement. La seule force est l'**attraction gravitationnelle** $\\vec{F}_g$ dirigée vers le centre de la Terre. Cette force :

- ne modifie **pas** la norme de la vitesse ;
- modifie **la direction** de la vitesse → maintient le satellite sur sa trajectoire circulaire.

---

## Mouvement d'un projectile (chute libre à 2D)

### Situation

Un objet est lancé avec une vitesse initiale $\\vec{v}_0$ faisant un angle $\\alpha$ avec l'horizontale. En négligeant les frottements, l'objet est en chute libre.

### Allure de la trajectoire

La trajectoire est une **parabole**. Horizontalement, le mouvement est **uniforme** (pas de force horizontale). Verticalement, le mouvement est **uniformément accéléré** (soumis au poids).

---

## Chronophotographie et analyse du mouvement

### Mouvement rectiligne accéléré (chute libre)

Sur une chronophotographie de chute libre verticale, les points sont **de plus en plus espacés** : le mouvement est accéléré.

### Mouvement circulaire uniforme

Les points sont **régulièrement espacés** le long du cercle : la norme de la vitesse est constante (mais la direction change).

### Mouvement décéléré (freinage)

Les points sont **de plus en plus rapprochés** : la vitesse diminue.

---

## Résumé des différents mouvements

| Mouvement | Trajectoire | Vitesse | $\\sum \\vec{F}$ |
|---|---|---|---|
| Repos | Aucune (point fixe) | $v = 0$ | $= \\vec{0}$ |
| MRU | Rectiligne | Constante | $= \\vec{0}$ |
| Rectiligne accéléré | Rectiligne | Augmente | $\\neq \\vec{0}$ (dans le sens du mouvement) |
| Rectiligne décéléré | Rectiligne | Diminue | $\\neq \\vec{0}$ (sens opposé au mouvement) |
| Circulaire uniforme | Circulaire | Norme constante | $\\neq \\vec{0}$ (vers le centre) |
| Chute libre | Rectiligne ou parabolique | Varie | $= \\vec{P} \\neq \\vec{0}$ |

---

## Exemples d'application

### Exemple 1 : durée de chute

Un caillou est lâché du haut d'un pont situé à $h = 45$ m au-dessus de l'eau. Combien de temps met-il pour atteindre l'eau ?

$$z = \\frac{1}{2}gt^2 \\implies t = \\sqrt{\\frac{2h}{g}} = \\sqrt{\\frac{2 \\times 45}{9{,}81}} = \\sqrt{9{,}17} \\approx 3{,}0 \\text{ s}$$

### Exemple 2 : vitesse à l'arrivée

En reprenant l'exemple précédent, quelle est la vitesse du caillou quand il touche l'eau ?

$$v = g \\cdot t = 9{,}81 \\times 3{,}0 \\approx 29 \\text{ m/s} \\approx 106 \\text{ km/h}$$

---

## À retenir

- Un objet en **chute libre** n'est soumis qu'à son poids : $\\sum \\vec{F} = m\\vec{g}$.
- En chute libre verticale sans vitesse initiale : $v = gt$ et $z = \\frac{1}{2}gt^2$.
- Tous les objets tombent à la **même vitesse** en chute libre (indépendant de la masse).
- Un mouvement **circulaire** (même uniforme) implique $\\sum \\vec{F} \\neq \\vec{0}$ car le vecteur vitesse change de direction.
- La **chronophotographie** permet de caractériser un mouvement : points espacés → accéléré, rapprochés → décéléré, réguliers → uniforme.
""",
                'quiz': {
                    'titre': 'Quiz — Chute libre et mouvements variés',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Un objet en chute libre est soumis uniquement à :",
                            'options': ["Son poids", "La réaction du support", "Les frottements de l'air", "La poussée d'Archimède"],
                            'reponse_correcte': '0',
                            'explication': "En chute libre, on ne considère que le poids de l'objet (toutes les autres forces sont négligées).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "La valeur de l'accélération de pesanteur g à la surface de la Terre vaut environ :",
                            'options': ["9,81 m/s²", "6,67 m/s²", "3,00 m/s²", "10,81 m/s²"],
                            'reponse_correcte': '0',
                            'explication': "L'accélération de pesanteur à la surface de la Terre est g ≈ 9,81 m/s².",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "En chute libre verticale sans vitesse initiale, la vitesse de l'objet :",
                            'options': ["Augmente proportionnellement au temps", "Reste constante", "Diminue au cours du temps", "Augmente proportionnellement au carré du temps"],
                            'reponse_correcte': '0',
                            'explication': "En chute libre sans vitesse initiale : v = g·t, la vitesse augmente linéairement avec le temps.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Un objet lancé verticalement vers le haut est-il en chute libre pendant la phase ascendante ?",
                            'options': ["Oui, car il n'est soumis qu'à son poids", "Non, car il monte", "Non, car sa vitesse diminue", "Oui, uniquement s'il est dans le vide"],
                            'reponse_correcte': '0',
                            'explication': "'Chute libre' signifie que seul le poids agit, quel que soit le sens du mouvement (montée ou descente).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Sur une chronophotographie de chute libre verticale, les points successifs sont :",
                            'options': ["De plus en plus espacés", "Régulièrement espacés", "De plus en plus rapprochés", "Disposés en cercle"],
                            'reponse_correcte': '0',
                            'explication': "La vitesse augmente en chute libre, donc les distances entre positions successives augmentent.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "En chute libre, deux objets de masses différentes lâchés de la même hauteur arrivent au sol :",
                            'options': ["En même temps (en l'absence de frottements)", "L'objet le plus lourd arrive en premier", "L'objet le plus léger arrive en premier", "On ne peut pas savoir sans connaître les masses"],
                            'reponse_correcte': '0',
                            'explication': "En chute libre (sans frottements), tous les objets tombent à la même vitesse, indépendamment de leur masse.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "La position d'un objet en chute libre verticale (sans vitesse initiale) évolue selon :",
                            'options': ["z = ½·g·t²", "z = g·t", "z = g·t²", "z = ½·g·t"],
                            'reponse_correcte': '0',
                            'explication': "La position (distance parcourue) vaut z = ½·g·t² pour une chute libre sans vitesse initiale.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Qui a démontré expérimentalement que tous les objets tombent à la même vitesse en l'absence de frottements ?",
                            'options': ["Galilée", "Newton", "Einstein", "Archimède"],
                            'reponse_correcte': '0',
                            'explication': "Galilée a démontré au XVIᵉ siècle que la chute libre est indépendante de la masse.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Un objet en mouvement circulaire uniforme a-t-il une résultante des forces nulle ?",
                            'options': ["Non, car la direction du vecteur vitesse change", "Oui, car la norme de la vitesse est constante", "Oui, car la trajectoire est régulière", "Non, car la norme de la vitesse augmente"],
                            'reponse_correcte': '0',
                            'explication': "Le mouvement circulaire implique un changement de direction du vecteur vitesse → pas un MRU → forces non compensées.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Un caillou est lâché du haut d'un pont à 20 m au-dessus de l'eau. La durée de la chute est environ :",
                            'options': ["2,0 s", "1,0 s", "4,5 s", "3,0 s"],
                            'reponse_correcte': '0',
                            'explication': "t = √(2h/g) = √(2×20/9,81) = √(4,08) ≈ 2,0 s.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Un objet est lancé verticalement vers le haut avec v₀ = 20 m/s. La hauteur maximale atteinte vaut environ :",
                            'options': ["20,4 m", "10,2 m", "40,8 m", "2,0 m"],
                            'reponse_correcte': '0',
                            'explication': "z_max = v₀²/(2g) = 20²/(2×9,81) = 400/19,62 ≈ 20,4 m.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Au sommet de la trajectoire d'un objet lancé verticalement vers le haut, la vitesse vaut :",
                            'options': ["0 m/s", "v₀", "g", "v₀/2"],
                            'reponse_correcte': '0',
                            'explication': "Au point le plus haut, la vitesse s'annule avant que l'objet ne redescende.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "La trajectoire d'un projectile lancé en l'air (chute libre à 2D, sans frottements) est :",
                            'options': ["Une parabole", "Un cercle", "Une droite", "Une hyperbole"],
                            'reponse_correcte': '0',
                            'explication': "En chute libre à 2D, le mouvement horizontal est uniforme et le vertical est accéléré : la trajectoire est parabolique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Sur une chronophotographie, des points de plus en plus rapprochés indiquent un mouvement :",
                            'options': ["Décéléré", "Accéléré", "Uniforme", "Circulaire"],
                            'reponse_correcte': '0',
                            'explication': "Des points qui se rapprochent signifient que la distance parcourue entre deux instants diminue → la vitesse diminue → mouvement décéléré.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "En chute libre, l'accélération d'un objet dépend de sa masse.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "En chute libre, l'accélération vaut g ≈ 9,81 m/s² pour tous les objets, quelle que soit leur masse.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Un mouvement rectiligne avec une vitesse qui augmente correspond à une résultante des forces non nulle.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Un mouvement rectiligne accéléré n'est pas un MRU → d'après la contraposée du principe d'inertie, la résultante des forces est non nulle.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Un satellite en orbite circulaire autour de la Terre est en chute libre.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Un satellite en orbite n'est soumis qu'à la gravitation terrestre (son poids) : il est bien en chute libre permanente.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quelle est la formule de la vitesse en chute libre verticale sans vitesse initiale (en fonction de g et t) ?",
                            'options': None,
                            'reponse_correcte': 'v = g·t',
                            'tolerances': ["v = gt", "v=gt", "v = g*t", "v=g*t", "v = g × t"],
                            'explication': "En chute libre sans vitesse initiale, la vitesse est v = g·t.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Quelle forme a la trajectoire d'un projectile lancé en l'air (sans frottements) ?",
                            'options': None,
                            'reponse_correcte': 'parabole',
                            'tolerances': ["une parabole", "parabolique", "trajectoire parabolique"],
                            'explication': "La trajectoire d'un projectile en chute libre à 2D est une parabole.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Un objet est lâché sans vitesse initiale. Après 3 secondes de chute libre, quelle est sa vitesse (en m/s, arrondir à l'unité) ?",
                            'options': None,
                            'reponse_correcte': '29',
                            'tolerances': ["29 m/s", "30", "30 m/s", "29,4", "29,4 m/s"],
                            'explication': "v = g·t = 9,81 × 3 ≈ 29,4 m/s, soit environ 29 m/s.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 4 — L'électricité
    # ──────────────────────────────────────────────
    {
        'ordre': 4,
        'titre': "L'électricité",
        'description': "Circuits électriques, intensité, tension, lois de Kirchhoff et loi d'Ohm.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Circuit électrique — intensité et tension",
                'duree': 40,
                'contenu': """# Circuit électrique — intensité et tension

## Introduction

L'électricité est omniprésente dans notre quotidien : éclairage, chauffage, appareils électroniques… Comprendre les grandeurs fondamentales qui régissent un circuit électrique — **l'intensité** et **la tension** — est essentiel pour analyser et concevoir des circuits.

---

## Le circuit électrique

### Définition

Un **circuit électrique** est un ensemble de **dipôles** (composants à deux bornes) reliés entre eux par des fils conducteurs de manière à former un chemin fermé permettant la **circulation du courant électrique**.

### Composants de base

| Composant | Rôle | Symbole usuel |
|---|---|---|
| **Générateur** (pile, batterie) | Fournit l'énergie électrique | — |
| **Récepteur** (lampe, résistance, moteur) | Convertit l'énergie électrique | — |
| **Interrupteur** | Ouvre ou ferme le circuit | — |
| **Fils conducteurs** | Assurent la liaison entre composants | — |

### Circuit ouvert et circuit fermé

- **Circuit fermé** : le courant peut circuler — tous les dipôles sont connectés en un chemin continu.
- **Circuit ouvert** : le courant ne circule pas — le chemin est interrompu (interrupteur ouvert, fil coupé…).

> **Attention :** un **court-circuit** survient lorsqu'un fil conducteur relie directement les deux bornes d'un générateur sans passer par un récepteur. Cela peut provoquer un échauffement dangereux et endommager le matériel.

---

## Le courant électrique

### Nature du courant

Dans un **métal**, le courant électrique est dû au déplacement d'ensemble des **électrons libres** sous l'effet d'une tension.

- Les électrons se déplacent du pôle **−** vers le pôle **+** du générateur (sens réel).
- Par convention, le **sens conventionnel** du courant va du pôle **+** vers le pôle **−** à l'extérieur du générateur.

### Analogie hydraulique

On peut comparer un circuit électrique à un circuit d'eau :

| Électricité | Hydraulique |
|---|---|
| Générateur (pile) | Pompe |
| Courant (débit de charges) | Débit d'eau |
| Tension (d.d.p.) | Différence de pression |
| Résistance | Étranglement du tuyau |

---

## L'intensité du courant

### Définition

L'**intensité** $I$ du courant électrique mesure le **débit de charges** qui traverse une section de conducteur par unité de temps :

$$I = \\frac{Q}{\\Delta t}$$

avec :
- $I$ en **ampères** (A)
- $Q$ la charge électrique en **coulombs** (C)
- $\\Delta t$ la durée en **secondes** (s)

> **Ordre de grandeur :** la charge d'un électron vaut $e = 1{,}6 \\times 10^{-19}$ C. Un courant de 1 A correspond au passage d'environ $6{,}25 \\times 10^{18}$ électrons par seconde !

### Mesure de l'intensité

L'intensité se mesure avec un **ampèremètre**, branché **en série** dans le circuit (le courant doit traverser l'appareil).

**Règles de branchement :**
- Borne **A** (ou **+**) du côté où le courant **entre** dans l'ampèremètre.
- Borne **COM** (ou **−**) du côté où le courant **sort**.
- Choisir un calibre adapté (commencer par le plus grand pour protéger l'appareil).

### Propriétés en série et en dérivation

**Circuit série :** l'intensité est la **même** en tout point du circuit.

$$I = I_1 = I_2 = I_3$$

C'est la **loi d'unicité** de l'intensité en série.

**Circuit en dérivation (branches parallèles) :** l'intensité se **partage** entre les branches. Au niveau d'un **nœud** :

$$I_{\\text{entrant}} = I_{\\text{sortant}}$$

C'est la **loi des nœuds** (première loi de Kirchhoff).

> **Exemple :** si un nœud reçoit un courant $I = 2$ A et se divise en deux branches, on peut avoir $I_1 = 1{,}2$ A et $I_2 = 0{,}8$ A (avec $I_1 + I_2 = I$).

---

## La tension électrique

### Définition

La **tension** $U$ entre deux points A et B d'un circuit est la **différence de potentiel** (d.d.p.) entre ces deux points :

$$U_{AB} = V_A - V_B$$

avec :
- $U$ en **volts** (V)
- $V_A$ et $V_B$ les potentiels électriques des points A et B

La tension représente l'**énergie** fournie (ou reçue) par unité de charge entre deux points.

### Mesure de la tension

La tension se mesure avec un **voltmètre**, branché **en dérivation** (en parallèle) entre les deux points considérés.

**Règles de branchement :**
- Borne **V** (ou **+**) reliée au point de potentiel le plus élevé.
- Borne **COM** reliée au point de potentiel le plus bas.
- Le voltmètre ne doit **pas** être traversé par le courant principal.

### Propriétés

**Tension aux bornes d'un générateur :** le générateur **impose** une tension entre ses bornes. Pour une pile idéale de f.é.m. $E$ :

$$U_G = E$$

**Tension aux bornes d'un fil idéal :** un fil conducteur parfait ne « consomme » pas d'énergie :

$$U_{\\text{fil}} = 0 \\text{ V}$$

---

## Tension en série et en dérivation

### Loi d'additivité des tensions (en série)

Dans une branche série, la tension totale est la **somme** des tensions individuelles :

$$U_{\\text{totale}} = U_1 + U_2 + U_3$$

C'est une conséquence directe de la **loi des mailles** (deuxième loi de Kirchhoff).

### Tension en dérivation

Tous les dipôles branchés **en dérivation** (en parallèle) ont la **même tension** à leurs bornes :

$$U = U_1 = U_2 = U_3$$

C'est la **loi d'unicité** de la tension en dérivation.

> **Exemple :** deux lampes en parallèle alimentées par un générateur de 6 V ont chacune une tension de 6 V à leurs bornes.

---

## Applications numériques

### Exercice résolu 1

Un courant de $I = 0{,}5$ A traverse un circuit pendant $\\Delta t = 2$ min. Quelle charge électrique a traversé le circuit ?

**Solution :**

$$Q = I \\times \\Delta t = 0{,}5 \\times (2 \\times 60) = 0{,}5 \\times 120 = 60 \\text{ C}$$

### Exercice résolu 2

Dans un circuit série alimenté par une pile de 9 V, on mesure $U_1 = 3{,}5$ V aux bornes d'une lampe et $U_2 = 2{,}5$ V aux bornes d'une résistance. Quelle est la tension $U_3$ aux bornes d'un moteur ?

**Solution :**

$$U_3 = U_{\\text{pile}} - U_1 - U_2 = 9 - 3{,}5 - 2{,}5 = 3{,}0 \\text{ V}$$

---

## À retenir

- Le **courant électrique** est un déplacement ordonné de charges ; son sens conventionnel va du + vers le − à l'extérieur du générateur.
- L'**intensité** $I$ (en A) mesure le débit de charges : $I = \\frac{Q}{\\Delta t}$. Elle se mesure en **série** avec un ampèremètre.
- La **tension** $U$ (en V) est la différence de potentiel entre deux points. Elle se mesure en **dérivation** avec un voltmètre.
- **Loi des nœuds** : $\\sum I_{\\text{entrant}} = \\sum I_{\\text{sortant}}$.
- **Loi d'additivité** des tensions en série : $U_{\\text{totale}} = U_1 + U_2 + \\cdots$
- **Unicité** de la tension en dérivation : tous les dipôles en parallèle ont la même tension.
""",
                'quiz': {
                    'titre': 'Quiz — Circuit électrique, intensité et tension',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Un circuit électrique fermé permet :",
                            'options': ["La circulation du courant électrique", "L'accumulation de charges en un point", "La production de lumière sans énergie", "Le stockage de tension"],
                            'reponse_correcte': '0',
                            'explication': "Un circuit fermé forme un chemin continu permettant la circulation du courant.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Le sens conventionnel du courant va :",
                            'options': ["Du pôle + vers le pôle − à l'extérieur du générateur", "Du pôle − vers le pôle + à l'extérieur du générateur", "Du pôle + vers le pôle − à l'intérieur du générateur", "Dans le même sens que les électrons"],
                            'reponse_correcte': '0',
                            'explication': "Par convention, le courant circule du + vers le − à l'extérieur du générateur (sens inverse des électrons).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "L'intensité du courant électrique se mesure avec :",
                            'options': ["Un ampèremètre branché en série", "Un voltmètre branché en série", "Un ampèremètre branché en dérivation", "Un ohmmètre branché en série"],
                            'reponse_correcte': '0',
                            'explication': "L'intensité se mesure avec un ampèremètre branché en série dans le circuit.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "La tension électrique se mesure avec :",
                            'options': ["Un voltmètre branché en dérivation (parallèle)", "Un voltmètre branché en série", "Un ampèremètre branché en dérivation", "Un ohmmètre branché en parallèle"],
                            'reponse_correcte': '0',
                            'explication': "La tension se mesure avec un voltmètre branché en dérivation (en parallèle) entre les deux points.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Dans un circuit série, l'intensité du courant :",
                            'options': ["Est la même en tout point du circuit", "Diminue à chaque composant traversé", "Augmente après chaque résistance", "Dépend du nombre de fils"],
                            'reponse_correcte': '0',
                            'explication': "C'est la loi d'unicité de l'intensité en série : I est identique en tout point d'une branche série.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Deux lampes branchées en dérivation (parallèle) alimentées par un générateur de 6 V ont chacune une tension de :",
                            'options': ["6 V", "3 V", "12 V", "0 V"],
                            'reponse_correcte': '0',
                            'explication': "En dérivation, tous les dipôles partagent la même tension : c'est la loi d'unicité de la tension en parallèle.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Un court-circuit se produit quand :",
                            'options': ["Un fil relie directement les deux bornes du générateur sans récepteur", "On branche trop de lampes en série", "L'interrupteur est ouvert", "La pile est déchargée"],
                            'reponse_correcte': '0',
                            'explication': "Un court-circuit survient quand les bornes du générateur sont reliées directement sans passer par un récepteur.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "La formule de l'intensité en fonction de la charge et du temps est :",
                            'options': ["I = Q / Δt", "I = Q × Δt", "I = Δt / Q", "I = Q² / Δt"],
                            'reponse_correcte': '0',
                            'explication': "L'intensité est le débit de charges : I = Q / Δt, avec Q en coulombs et Δt en secondes.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Un courant de 0,5 A traverse un circuit pendant 2 minutes. La charge électrique qui a circulé vaut :",
                            'options': ["60 C", "1 C", "120 C", "0,25 C"],
                            'reponse_correcte': '0',
                            'explication': "Q = I × Δt = 0,5 × (2 × 60) = 0,5 × 120 = 60 C.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Dans un circuit série alimenté par 9 V, on mesure U₁ = 3,5 V et U₂ = 2,5 V. La tension U₃ aux bornes d'un troisième dipôle vaut :",
                            'options': ["3,0 V", "6,0 V", "9,0 V", "1,0 V"],
                            'reponse_correcte': '0',
                            'explication': "Loi d'additivité en série : U₃ = 9 − 3,5 − 2,5 = 3,0 V.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "La loi des nœuds (1ère loi de Kirchhoff) stipule que :",
                            'options': ["La somme des courants entrants = la somme des courants sortants", "La somme des tensions dans une maille = 0", "Le courant est le même en tout point du circuit", "La tension est la même en tout point du circuit"],
                            'reponse_correcte': '0',
                            'explication': "La loi des nœuds (conservation de la charge) : les courants entrants = les courants sortants en un nœud.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Dans un métal, les porteurs de charge qui se déplacent sont :",
                            'options': ["Les électrons libres", "Les protons", "Les neutrons", "Les ions positifs"],
                            'reponse_correcte': '0',
                            'explication': "Dans un conducteur métallique, le courant est dû au déplacement des électrons libres.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Au niveau d'un nœud, un courant de 2 A arrive et se divise en deux branches. Si I₁ = 1,2 A, alors I₂ vaut :",
                            'options': ["0,8 A", "1,2 A", "2,0 A", "3,2 A"],
                            'reponse_correcte': '0',
                            'explication': "Loi des nœuds : I = I₁ + I₂ → I₂ = 2 − 1,2 = 0,8 A.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "La tension aux bornes d'un fil conducteur idéal vaut :",
                            'options': ["0 V", "La même tension que le générateur", "L'intensité du courant", "La résistance du fil"],
                            'reponse_correcte': '0',
                            'explication': "Un fil conducteur idéal a une résistance nulle, donc la tension à ses bornes est nulle.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Les électrons se déplacent du pôle + vers le pôle − à l'extérieur du générateur.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Les électrons se déplacent du − vers le + (sens réel). Le sens conventionnel du courant est l'inverse.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La loi d'additivité des tensions en série signifie que la tension totale est la somme des tensions individuelles.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Dans une branche série, la tension totale est bien la somme des tensions de chaque dipôle.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Dans un circuit en dérivation, l'intensité est la même dans toutes les branches.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "En dérivation, c'est la tension qui est la même dans chaque branche (unicité de la tension). L'intensité se partage selon les résistances.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quel appareil mesure l'intensité du courant électrique ?",
                            'options': None,
                            'reponse_correcte': 'ampèremètre',
                            'tolerances': ["un ampèremètre", "l'ampèremètre", "amperemetre", "un amperemetre"],
                            'explication': "L'intensité se mesure avec un ampèremètre, branché en série dans le circuit.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "En quelle unité mesure-t-on la tension électrique ?",
                            'options': None,
                            'reponse_correcte': 'volt',
                            'tolerances': ["le volt", "volts", "V", "en volt", "en volts"],
                            'explication': "La tension électrique se mesure en volts (V).",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Comment branche-t-on un voltmètre dans un circuit (en série ou en dérivation) ?",
                            'options': None,
                            'reponse_correcte': 'en dérivation',
                            'tolerances': ["en derivation", "dérivation", "derivation", "en parallèle", "en parallele", "parallèle"],
                            'explication': "Un voltmètre se branche en dérivation (en parallèle) entre les deux points dont on veut mesurer la tension.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': "Lois de Kirchhoff et loi d'Ohm",
                'duree': 40,
                'contenu': """# Lois de Kirchhoff et loi d'Ohm

## Introduction

Dans la leçon précédente, nous avons découvert l'intensité et la tension. Nous allons maintenant établir les **lois fondamentales** qui permettent de **calculer** les grandeurs dans un circuit : les **lois de Kirchhoff** et la **loi d'Ohm**. Ces outils sont indispensables pour résoudre tout problème de circuit électrique.

---

## La résistance électrique

### Définition

La **résistance** $R$ d'un dipôle traduit sa capacité à **s'opposer** au passage du courant. Plus la résistance est élevée, plus le courant est faible pour une tension donnée.

- Unité : l'**ohm** (symbole $\\Omega$).
- Multiples courants : $1 \\text{ k}\\Omega = 10^3 \\; \\Omega$ ; $1 \\text{ M}\\Omega = 10^6 \\; \\Omega$.

### Le résistor

Un **résistor** (souvent appelé « résistance » par abus de langage) est un composant électronique dont la résistance est fixe et connue. Sa valeur peut être identifiée grâce au **code couleur** imprimé sur son boîtier.

| Bande | Couleur | Valeur |
|---|---|---|
| 1ère/2ème | Noir, Marron, … Rouge … | 0, 1, … 2 … |
| 3ème (multiplicateur) | Noir = ×1, Marron = ×10, … | — |
| 4ème (tolérance) | Or = ±5 %, Argent = ±10 % | — |

---

## La loi d'Ohm

### Énoncé

Pour un **dipôle ohmique** (résistor linéaire), la tension $U$ à ses bornes est **proportionnelle** à l'intensité $I$ qui le traverse :

$$\\boxed{U = R \\times I}$$

avec :
- $U$ en volts (V)
- $R$ en ohms ($\\Omega$)
- $I$ en ampères (A)

### Caractéristique d'un dipôle ohmique

La **caractéristique** $U = f(I)$ d'un résistor est une **droite passant par l'origine**, de pente égale à $R$ :

$$R = \\frac{U}{I} = \\frac{\\Delta U}{\\Delta I}$$

> **Remarque :** un dipôle dont la caractéristique n'est pas une droite (ex : diode, lampe) n'obéit **pas** à la loi d'Ohm — on dit qu'il est **non ohmique**.

### Méthode expérimentale

Pour tracer la caractéristique d'un résistor :
1. Brancher un générateur variable, un ampèremètre (en série) et un voltmètre (en dérivation aux bornes du résistor).
2. Faire varier la tension et relever les couples $(I, U)$.
3. Tracer $U = f(I)$ : si la courbe est une droite, le dipôle est ohmique et la pente donne $R$.

---

## Les lois de Kirchhoff

### Loi des nœuds (1ère loi)

**Énoncé :** En un **nœud** du circuit, la somme des intensités des courants qui **entrent** est égale à la somme des intensités des courants qui **sortent** :

$$\\boxed{\\sum I_{\\text{entrant}} = \\sum I_{\\text{sortant}}}$$

> **Interprétation physique :** c'est la **conservation de la charge** — les charges ne s'accumulent pas en un point.

**Exemple :** au nœud N, trois branches se rejoignent avec $I_1 = 3$ A entrant, $I_2$ sortant et $I_3 = 1{,}5$ A sortant. On a :

$$I_1 = I_2 + I_3 \\implies I_2 = 3 - 1{,}5 = 1{,}5 \\text{ A}$$

### Loi des mailles (2ème loi)

**Énoncé :** Dans une **maille** (boucle fermée) d'un circuit, la somme algébrique des tensions est nulle :

$$\\boxed{\\sum_{\\text{maille}} U_k = 0}$$

**Convention de signe :** on choisit un sens de parcours arbitraire de la maille. Une tension est comptée **positivement** si elle est dans le sens de parcours, **négativement** sinon.

**Exemple :** dans une maille contenant un générateur (tension $E = 12$ V) et deux résistances ($U_1$, $U_2$) :

$$E - U_1 - U_2 = 0 \\implies U_1 + U_2 = E = 12 \\text{ V}$$

> On retrouve la **loi d'additivité** des tensions en série comme cas particulier de la loi des mailles.

---

## Association de résistances

### En série

Lorsque plusieurs résistances sont branchées **en série**, elles sont traversées par le **même courant**. La résistance équivalente est la **somme** :

$$\\boxed{R_{\\text{éq}} = R_1 + R_2 + \\cdots + R_n}$$

> **Démonstration rapide :** loi des mailles : $E = U_1 + U_2 = R_1 I + R_2 I = (R_1 + R_2) I$.

**Exemple :** $R_1 = 100 \\; \\Omega$ et $R_2 = 220 \\; \\Omega$ en série → $R_{\\text{éq}} = 320 \\; \\Omega$.

### En dérivation (parallèle)

Lorsque plusieurs résistances sont branchées **en dérivation**, elles ont la **même tension** à leurs bornes. L'inverse de la résistance équivalente est la somme des inverses :

$$\\boxed{\\frac{1}{R_{\\text{éq}}} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\cdots + \\frac{1}{R_n}}$$

Pour deux résistances :

$$R_{\\text{éq}} = \\frac{R_1 \\times R_2}{R_1 + R_2}$$

> **Démonstration rapide :** loi des nœuds : $I = I_1 + I_2 = \\frac{U}{R_1} + \\frac{U}{R_2} = U \\left( \\frac{1}{R_1} + \\frac{1}{R_2} \\right)$.

**Exemple :** $R_1 = 100 \\; \\Omega$ et $R_2 = 100 \\; \\Omega$ en parallèle → $R_{\\text{éq}} = \\frac{100 \\times 100}{100 + 100} = 50 \\; \\Omega$.

> **Remarque :** la résistance équivalente en parallèle est toujours **inférieure** à la plus petite des résistances individuelles.

---

## Puissance et énergie électriques

### Puissance

La **puissance électrique** $P$ consommée par un dipôle vaut :

$$\\boxed{P = U \\times I}$$

avec $P$ en watts (W), $U$ en volts (V), $I$ en ampères (A).

Pour un résistor (loi d'Ohm $U = RI$) :

$$P = R I^2 = \\frac{U^2}{R}$$

### Énergie

L'**énergie** $E$ consommée pendant une durée $\\Delta t$ :

$$E = P \\times \\Delta t$$

avec $E$ en joules (J) si $\\Delta t$ en secondes, ou en **kilowattheures** (kWh) si $\\Delta t$ en heures et $P$ en kW.

> **Conversion :** $1 \\text{ kWh} = 3{,}6 \\times 10^6 \\text{ J} = 3{,}6 \\text{ MJ}$.

---

## Les capteurs résistifs

### Principe

Certains composants ont une résistance qui **varie** en fonction d'une grandeur physique. On les utilise comme **capteurs** :

| Capteur | Grandeur mesurée | Comportement |
|---|---|---|
| **Thermistance CTN** | Température | $R$ diminue quand $T$ augmente |
| **Photorésistance (LDR)** | Éclairement | $R$ diminue quand la lumière augmente |

### Utilisation

En intégrant un capteur dans un **pont diviseur de tension**, on convertit la variation de résistance en variation de tension, mesurable par un voltmètre ou un microcontrôleur.

**Pont diviseur de tension :** pour deux résistances $R_1$ et $R_2$ en série alimentées par $E$ :

$$U_{R_2} = E \\times \\frac{R_2}{R_1 + R_2}$$

Si $R_2$ est une thermistance, $U_{R_2}$ varie avec la température → on a un **thermomètre électronique**.

---

## Applications numériques

### Exercice résolu 1

Un résistor de $R = 470 \\; \\Omega$ est traversé par un courant $I = 20$ mA. Calculer la tension à ses bornes et la puissance dissipée.

**Solution :**

$$U = R \\times I = 470 \\times 0{,}020 = 9{,}4 \\text{ V}$$

$$P = U \\times I = 9{,}4 \\times 0{,}020 = 0{,}188 \\text{ W} \\approx 188 \\text{ mW}$$

### Exercice résolu 2

Deux résistances $R_1 = 200 \\; \\Omega$ et $R_2 = 300 \\; \\Omega$ sont en parallèle, alimentées par un générateur de 12 V. Calculer la résistance équivalente, le courant total et le courant dans chaque branche.

**Solution :**

$$R_{\\text{éq}} = \\frac{200 \\times 300}{200 + 300} = \\frac{60\\,000}{500} = 120 \\; \\Omega$$

$$I = \\frac{U}{R_{\\text{éq}}} = \\frac{12}{120} = 0{,}10 \\text{ A} = 100 \\text{ mA}$$

$$I_1 = \\frac{U}{R_1} = \\frac{12}{200} = 0{,}060 \\text{ A} = 60 \\text{ mA}$$

$$I_2 = \\frac{U}{R_2} = \\frac{12}{300} = 0{,}040 \\text{ A} = 40 \\text{ mA}$$

**Vérification :** $I_1 + I_2 = 60 + 40 = 100$ mA $= I$ ✓

---

## À retenir

- La **résistance** $R$ (en $\\Omega$) d'un dipôle traduit son opposition au passage du courant.
- **Loi d'Ohm** : $U = R \\times I$ pour un dipôle ohmique.
- **Loi des nœuds** : $\\sum I_{\\text{entrant}} = \\sum I_{\\text{sortant}}$ (conservation de la charge).
- **Loi des mailles** : $\\sum U_k = 0$ dans toute boucle fermée.
- **Résistances en série** : $R_{\\text{éq}} = R_1 + R_2$.
- **Résistances en parallèle** : $\\frac{1}{R_{\\text{éq}}} = \\frac{1}{R_1} + \\frac{1}{R_2}$.
- **Puissance** : $P = U \\times I = R I^2 = \\frac{U^2}{R}$.
- **Énergie** : $E = P \\times \\Delta t$.
""",
                'quiz': {
                    'titre': "Quiz — Lois de Kirchhoff et loi d'Ohm",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "La loi d'Ohm pour un dipôle ohmique s'écrit :",
                            'options': ["U = R × I", "U = R / I", "R = U × I", "I = R × U"],
                            'reponse_correcte': '0',
                            'explication': "La loi d'Ohm relie la tension, la résistance et l'intensité : U = R × I.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "L'unité de la résistance électrique est :",
                            'options': ["L'ohm (Ω)", "Le volt (V)", "L'ampère (A)", "Le watt (W)"],
                            'reponse_correcte': '0',
                            'explication': "La résistance s'exprime en ohms (symbole Ω).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "La caractéristique U = f(I) d'un résistor linéaire est :",
                            'options': ["Une droite passant par l'origine", "Une parabole", "Un cercle", "Une droite ne passant pas par l'origine"],
                            'reponse_correcte': '0',
                            'explication': "Pour un dipôle ohmique, U est proportionnel à I : la caractéristique est une droite passant par l'origine, de pente R.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "La loi des mailles (2ème loi de Kirchhoff) dit que dans une maille fermée :",
                            'options': ["La somme algébrique des tensions est nulle", "La somme des intensités est nulle", "Toutes les tensions sont égales", "Le courant est constant"],
                            'reponse_correcte': '0',
                            'explication': "La loi des mailles : dans toute boucle fermée, la somme algébrique des tensions vaut zéro.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Deux résistances R₁ = 100 Ω et R₂ = 200 Ω sont en série. La résistance équivalente vaut :",
                            'options': ["300 Ω", "150 Ω", "66,7 Ω", "100 Ω"],
                            'reponse_correcte': '0',
                            'explication': "En série : R_éq = R₁ + R₂ = 100 + 200 = 300 Ω.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "La puissance électrique consommée par un dipôle se calcule par :",
                            'options': ["P = U × I", "P = U / I", "P = I / U", "P = U + I"],
                            'reponse_correcte': '0',
                            'explication': "La puissance électrique est P = U × I, avec P en watts, U en volts et I en ampères.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Une thermistance CTN est un composant dont la résistance :",
                            'options': ["Diminue quand la température augmente", "Augmente quand la température augmente", "Ne varie jamais", "Augmente avec l'éclairement"],
                            'reponse_correcte': '0',
                            'explication': "CTN = Coefficient de Température Négatif : la résistance diminue quand la température augmente.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "1 kΩ (kilohm) correspond à :",
                            'options': ["1000 Ω", "100 Ω", "10 Ω", "1 000 000 Ω"],
                            'reponse_correcte': '0',
                            'explication': "Le préfixe k (kilo) signifie 10³ : 1 kΩ = 1000 Ω.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Un résistor de 470 Ω est traversé par un courant de 20 mA. La tension à ses bornes vaut :",
                            'options': ["9,4 V", "23,5 V", "0,94 V", "470 V"],
                            'reponse_correcte': '0',
                            'explication': "U = R × I = 470 × 0,020 = 9,4 V.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Deux résistances R₁ = 100 Ω et R₂ = 100 Ω en parallèle ont une résistance équivalente de :",
                            'options': ["50 Ω", "100 Ω", "200 Ω", "25 Ω"],
                            'reponse_correcte': '0',
                            'explication': "En parallèle : R_éq = (R₁ × R₂)/(R₁ + R₂) = (100 × 100)/(100 + 100) = 50 Ω.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Dans un pont diviseur de tension avec R₁ et R₂ en série alimenté par E, la tension aux bornes de R₂ vaut :",
                            'options': ["E × R₂ / (R₁ + R₂)", "E × R₁ / (R₁ + R₂)", "E × (R₁ + R₂) / R₂", "E / (R₁ × R₂)"],
                            'reponse_correcte': '0',
                            'explication': "Formule du pont diviseur : U_R₂ = E × R₂ / (R₁ + R₂).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "La résistance équivalente de résistances en parallèle est toujours :",
                            'options': ["Inférieure à la plus petite des résistances", "Égale à la somme des résistances", "Supérieure à la plus grande des résistances", "Égale à la moyenne des résistances"],
                            'reponse_correcte': '0',
                            'explication': "En parallèle, la résistance équivalente est toujours plus petite que la plus petite résistance individuelle.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Un générateur de 12 V alimente deux résistances en série de 200 Ω et 300 Ω. L'intensité du courant vaut :",
                            'options': ["24 mA", "60 mA", "40 mA", "12 mA"],
                            'reponse_correcte': '0',
                            'explication': "R_éq = 200 + 300 = 500 Ω. I = U/R = 12/500 = 0,024 A = 24 mA.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "1 kWh correspond à :",
                            'options': ["3,6 × 10⁶ J", "1000 J", "3600 J", "1 × 10⁶ J"],
                            'reponse_correcte': '0',
                            'explication': "1 kWh = 1000 W × 3600 s = 3,6 × 10⁶ J.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Un dipôle dont la caractéristique U = f(I) n'est pas une droite est dit ohmique.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Un dipôle ohmique a une caractéristique linéaire (droite passant par l'origine). Sinon, il est non ohmique.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La loi des nœuds traduit la conservation de la charge électrique.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "La loi des nœuds exprime que les charges ne s'accumulent pas : ce qui entre dans un nœud en ressort.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Pour un résistor, la puissance dissipée peut se calculer par P = U²/R.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "En combinant P = U×I et U = R×I, on obtient P = U²/R (ou P = R×I²).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quelle est la formule de la résistance équivalente de deux résistances R₁ et R₂ en série ?",
                            'options': None,
                            'reponse_correcte': 'R = R1 + R2',
                            'tolerances': ["Req = R1 + R2", "R_eq = R1 + R2", "R1 + R2", "R₁ + R₂"],
                            'explication': "En série, les résistances s'additionnent : R_éq = R₁ + R₂.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on un capteur dont la résistance diminue quand l'éclairement augmente ?",
                            'options': None,
                            'reponse_correcte': 'photorésistance',
                            'tolerances': ["une photorésistance", "photoresistance", "LDR", "ldr", "une photoresistance"],
                            'explication': "Une photorésistance (LDR) voit sa résistance diminuer lorsque l'éclairement augmente.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Un résistor de 200 Ω est soumis à une tension de 10 V. Quelle est l'intensité du courant (en A) ?",
                            'options': None,
                            'reponse_correcte': '0,05',
                            'tolerances': ["0.05", "0,05 A", "0.05 A", "50 mA"],
                            'explication': "I = U/R = 10/200 = 0,05 A = 50 mA.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 5 — Optique et lumière
    # ──────────────────────────────────────────────
    {
        'ordre': 5,
        'titre': "Optique et lumière",
        'description': "Spectres lumineux, propagation de la lumière, réflexion, réfraction et lentilles convergentes.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Lumière visible, spectres d'émission et d'absorption",
                'duree': 40,
                'contenu': """# Lumière visible, spectres d'émission et d'absorption

## Introduction

La lumière est un phénomène fondamental de la physique. Elle nous permet de **voir** le monde, mais elle est aussi un outil puissant d'**analyse** : en décomposant la lumière émise par une source, on obtient un **spectre** qui fournit des informations sur la composition chimique de cette source. L'étude des spectres — la **spectroscopie** — a révolutionné l'astronomie et la chimie.

---

## La lumière visible

### Nature de la lumière

La lumière est une **onde électromagnétique**. Elle se propage dans le vide à la vitesse :

$$c = 3{,}00 \\times 10^8 \\text{ m/s}$$

La lumière visible ne représente qu'une **petite partie** du spectre électromagnétique complet, qui comprend aussi les ondes radio, les infrarouges, les ultraviolets, les rayons X et les rayons gamma.

### Longueur d'onde

Chaque radiation lumineuse est caractérisée par sa **longueur d'onde** $\\lambda$ (lettre grecque « lambda »), mesurée en **nanomètres** (nm) :

$$1 \\text{ nm} = 10^{-9} \\text{ m}$$

Le **domaine visible** s'étend de $\\lambda \\approx 400$ nm (violet) à $\\lambda \\approx 800$ nm (rouge) :

| Couleur | Longueur d'onde (nm) |
|---|---|
| Violet | 400 – 450 |
| Bleu | 450 – 500 |
| Vert | 500 – 570 |
| Jaune | 570 – 590 |
| Orange | 590 – 620 |
| Rouge | 620 – 800 |

### Relation fréquence – longueur d'onde

La fréquence $f$ et la longueur d'onde $\\lambda$ sont liées par :

$$\\boxed{c = \\lambda \\times f}$$

avec $c$ en m/s, $\\lambda$ en m et $f$ en Hz.

> **Exemple :** pour une radiation rouge de $\\lambda = 650$ nm : $f = \\frac{c}{\\lambda} = \\frac{3 \\times 10^8}{650 \\times 10^{-9}} \\approx 4{,}6 \\times 10^{14}$ Hz.

---

## Décomposition de la lumière blanche

### La lumière blanche

La **lumière blanche** (émise par le Soleil, une lampe à incandescence…) est un **mélange** de toutes les radiations visibles. Elle n'est pas « simple » : elle contient toutes les longueurs d'onde du domaine visible.

### Dispersion par un prisme

Lorsqu'un faisceau de lumière blanche traverse un **prisme** en verre, chaque radiation est déviée d'un angle différent :

- Le **violet** (courte $\\lambda$) est **plus dévié** que le rouge (grande $\\lambda$).
- On observe un étalement des couleurs : c'est la **dispersion** de la lumière.

Le spectre obtenu sur un écran est un **arc-en-ciel continu** allant du violet au rouge. Ce phénomène explique aussi la formation de l'**arc-en-ciel** naturel (dispersion par les gouttes d'eau).

### Dispersion par un réseau

Un **réseau de diffraction** (surface comportant de nombreuses fentes parallèles) produit également la dispersion de la lumière. C'est le dispositif utilisé dans la plupart des spectroscopes modernes.

---

## Les spectres d'émission

### Spectre continu d'émission

Un **corps chaud** (solide, liquide ou gaz dense) émet un **spectre continu** : toutes les longueurs d'onde sont présentes, sans interruption.

- La **température** du corps détermine les couleurs prédominantes : plus le corps est chaud, plus le spectre s'enrichit vers le bleu-violet.
- Exemples : filament d'une lampe à incandescence, Soleil, lave en fusion.

> Le Soleil, de température de surface $T \\approx 5\\,800$ K, émet un maximum d'intensité dans le jaune-vert ($\\lambda \\approx 500$ nm).

### Spectre de raies d'émission

Un **gaz à basse pression**, excité par une décharge électrique ou un chauffage, émet un **spectre de raies** : seules certaines longueurs d'onde bien précises sont émises, apparaissant sous forme de **raies colorées** sur un fond noir.

**Caractéristiques essentielles :**
- Chaque **élément chimique** possède un spectre de raies **unique**, comme une empreinte digitale.
- Les raies sont toujours aux **mêmes longueurs d'onde** pour un élément donné, quelles que soient les conditions d'excitation.

**Exemples de spectres :**
- **Hydrogène** : raies rouge ($\\lambda = 656$ nm, raie $H_\\alpha$), bleu-vert ($486$ nm, $H_\\beta$), violet ($434$ nm, $H_\\gamma$)…
- **Sodium** : doublet jaune caractéristique ($\\lambda \\approx 589$ nm) — c'est la couleur des lampadaires au sodium.
- **Néon** : nombreuses raies dans le rouge-orangé — utilisé dans les enseignes lumineuses.

---

## Les spectres d'absorption

### Principe

Lorsqu'une lumière blanche traverse un **gaz froid** (à basse pression), certaines radiations sont **absorbées** par les atomes du gaz. On obtient un **spectre continu** (celui de la lumière blanche) marqué de **raies noires** : c'est le **spectre de raies d'absorption**.

### Lien avec le spectre d'émission

**Résultat fondamental :** les raies d'absorption d'un élément se trouvent exactement aux **mêmes longueurs d'onde** que ses raies d'émission.

$$\\lambda_{\\text{absorption}} = \\lambda_{\\text{émission}}$$

> Un atome absorbe exactement les mêmes radiations qu'il est capable d'émettre.

### Application : spectre du Soleil

Le spectre du Soleil (spectre de Fraunhofer) est un spectre **continu** (émis par la photosphère chaude) traversé de **raies noires** (absorption par les gaz plus froids de l'atmosphère solaire).

En identifiant les longueurs d'onde des raies d'absorption, on détermine la **composition chimique** de l'atmosphère solaire : hydrogène, hélium, sodium, calcium, fer…

> C'est ainsi que l'**hélium** a été découvert dans le spectre du Soleil avant d'être identifié sur Terre (1868, J. N. Lockyer).

---

## Identification d'un élément par spectroscopie

### Méthode

Pour identifier un élément inconnu :
1. On éclaire l'échantillon (gaz) ou on l'excite par décharge électrique.
2. On observe son spectre d'émission (ou d'absorption).
3. On compare les longueurs d'onde des raies observées avec les **spectres de référence** des éléments connus.

Si les raies coïncident → l'élément est identifié.

### Applications

- **Astronomie** : composition des étoiles et des nébuleuses.
- **Chimie analytique** : identification de substances inconnues.
- **Médecine légale** : analyse d'échantillons traces.
- **Contrôle industriel** : vérification de la pureté de matériaux.

---

## Lumière monochromatique et polychromatique

- **Lumière monochromatique** : contient une **seule** longueur d'onde (ex : laser He-Ne, $\\lambda = 632{,}8$ nm). Spectre : une seule raie.
- **Lumière polychromatique** : contient **plusieurs** longueurs d'onde. Spectre : plusieurs raies ou un continuum.

La lumière blanche est polychromatique (spectre continu). La lumière émise par un laser est (quasi) monochromatique.

---

## À retenir

- La lumière visible correspond aux longueurs d'onde $\\lambda \\in [400 \\text{ nm} ; 800 \\text{ nm}]$, du violet au rouge.
- La **lumière blanche** est un mélange de toutes les radiations visibles ; un prisme la **disperse** en un spectre continu.
- Un **corps chaud** émet un spectre continu ; un **gaz excité à basse pression** émet un spectre de **raies d'émission** (raies colorées sur fond noir).
- Un **gaz froid** traversé par la lumière blanche produit un spectre de **raies d'absorption** (raies noires sur fond continu).
- Les raies d'absorption et d'émission d'un élément ont les **mêmes longueurs d'onde** : c'est la signature de l'élément.
- La spectroscopie permet d'identifier la composition chimique d'une source lumineuse, y compris les **étoiles**.
""",
                'quiz': {
                    'titre': "Quiz — Lumière visible, spectres d'émission et d'absorption",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quel est le domaine de longueurs d'onde de la lumière visible ?",
                            'options': ["400 nm à 800 nm", "100 nm à 400 nm", "800 nm à 1200 nm", "10 nm à 100 nm"],
                            'reponse_correcte': '0',
                            'explication': "Le domaine visible s'étend de 400 nm (violet) à 800 nm (rouge).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quelle couleur correspond aux longueurs d'onde les plus courtes du spectre visible ?",
                            'options': ["Le violet", "Le rouge", "Le vert", "Le jaune"],
                            'reponse_correcte': '0',
                            'explication': "Le violet correspond aux courtes longueurs d'onde (≈ 400 nm).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "La lumière blanche est :",
                            'options': ["Un mélange de toutes les radiations visibles", "Une radiation monochromatique", "Une radiation infrarouge", "Une radiation ultraviolette"],
                            'reponse_correcte': '0',
                            'explication': "La lumière blanche contient toutes les longueurs d'onde du domaine visible.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Un prisme permet de décomposer la lumière blanche grâce au phénomène de :",
                            'options': ["Dispersion", "Réflexion totale", "Diffraction", "Absorption"],
                            'reponse_correcte': '0',
                            'explication': "Le prisme disperse la lumière : chaque longueur d'onde est déviée différemment.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Quel type de spectre émet un corps chaud (solide ou liquide) ?",
                            'options': ["Un spectre continu", "Un spectre de raies d'émission", "Un spectre de raies d'absorption", "Aucun spectre"],
                            'reponse_correcte': '0',
                            'explication': "Un corps chaud émet un spectre continu contenant toutes les longueurs d'onde.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Un gaz excité à basse pression émet :",
                            'options': ["Un spectre de raies d'émission", "Un spectre continu", "Un spectre de raies d'absorption", "De la lumière blanche"],
                            'reponse_correcte': '0',
                            'explication': "Un gaz excité à basse pression émet des raies colorées sur fond noir, caractéristiques de l'élément.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Le spectre de raies d'émission d'un élément est :",
                            'options': ["Unique pour chaque élément chimique", "Identique pour tous les éléments", "Toujours continu", "Invisible à l'œil nu"],
                            'reponse_correcte': '0',
                            'explication': "Chaque élément possède un spectre de raies unique, comme une empreinte digitale.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "La relation entre la vitesse de la lumière, la longueur d'onde et la fréquence est :",
                            'options': ["c = λ × f", "c = λ / f", "c = f / λ", "c = λ + f"],
                            'reponse_correcte': '0',
                            'explication': "La vitesse de la lumière est le produit de la longueur d'onde par la fréquence : c = λ × f.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Lorsqu'on observe un spectre de raies d'absorption, on voit :",
                            'options': ["Des raies noires sur un fond continu coloré", "Des raies colorées sur un fond noir", "Un spectre tout noir", "Un spectre entièrement continu"],
                            'reponse_correcte': '0',
                            'explication': "Le spectre d'absorption montre des raies noires (radiations absorbées) sur le fond continu de la lumière blanche.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Le doublet jaune caractéristique à λ ≈ 589 nm est celui de :",
                            'options': ["Le sodium", "L'hydrogène", "Le néon", "L'hélium"],
                            'reponse_correcte': '0',
                            'explication': "Le sodium émet un doublet jaune caractéristique à environ 589 nm, visible dans les lampadaires.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Le spectre du Soleil (spectre de Fraunhofer) est un spectre :",
                            'options': ["Continu avec des raies d'absorption", "De raies d'émission uniquement", "Entièrement continu sans raies", "De raies d'absorption uniquement sur fond noir"],
                            'reponse_correcte': '0',
                            'explication': "Le spectre solaire est continu (photosphère chaude) traversé de raies noires d'absorption (atmosphère solaire froide).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Quelle est la longueur d'onde de la raie Hα de l'hydrogène ?",
                            'options': ["656 nm", "589 nm", "434 nm", "400 nm"],
                            'reponse_correcte': '0',
                            'explication': "La raie Hα de l'hydrogène est une raie rouge située à λ = 656 nm.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "L'hélium a été découvert pour la première fois :",
                            'options': ["Dans le spectre du Soleil avant d'être trouvé sur Terre", "En laboratoire par synthèse chimique", "Dans l'atmosphère terrestre", "Dans des roches lunaires"],
                            'reponse_correcte': '0',
                            'explication': "L'hélium a été identifié en 1868 dans le spectre du Soleil par J. N. Lockyer, avant d'être trouvé sur Terre.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Une lumière monochromatique est une lumière qui :",
                            'options': ["Ne contient qu'une seule longueur d'onde", "Contient toutes les longueurs d'onde", "Est toujours de couleur blanche", "Est invisible"],
                            'reponse_correcte': '0',
                            'explication': "Une lumière monochromatique contient une seule longueur d'onde (ex : laser).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Les raies d'absorption d'un élément se trouvent aux mêmes longueurs d'onde que ses raies d'émission.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Un atome absorbe exactement les mêmes radiations qu'il est capable d'émettre.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Le violet est la couleur la plus déviée par un prisme car il a la plus grande longueur d'onde.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le violet est le plus dévié car il a la plus courte longueur d'onde (≈ 400 nm), pas la plus grande.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Un laser He-Ne émet une lumière polychromatique.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Un laser émet une lumière quasi monochromatique (une seule longueur d'onde : 632,8 nm pour le He-Ne).",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on le phénomène par lequel un prisme sépare les différentes couleurs de la lumière blanche ?",
                            'options': None,
                            'reponse_correcte': 'dispersion',
                            'tolerances': ["la dispersion", "dispersion de la lumière", "la dispersion de la lumière"],
                            'explication': "La dispersion est le phénomène par lequel chaque longueur d'onde est déviée différemment par le prisme.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on la technique d'analyse qui identifie les éléments chimiques grâce à leur spectre lumineux ?",
                            'options': None,
                            'reponse_correcte': 'spectroscopie',
                            'tolerances': ["la spectroscopie", "spectrométrie", "la spectrométrie"],
                            'explication': "La spectroscopie permet d'identifier la composition chimique d'une source via l'analyse de son spectre.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quelle est la vitesse de la lumière dans le vide, en m/s ? (notation scientifique : ex. 3e8)",
                            'options': None,
                            'reponse_correcte': '3e8',
                            'tolerances': ["3 × 10^8", "3x10^8", "300000000", "3.00e8", "3,00 × 10^8"],
                            'explication': "La vitesse de la lumière dans le vide est c = 3,00 × 10⁸ m/s.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': "Réfraction, lentilles et formation d'images",
                'duree': 45,
                'contenu': """# Réfraction, lentilles et formation d'images

## Introduction

La lumière se propage en ligne droite dans un milieu homogène et transparent. Mais que se passe-t-il lorsqu'elle **change de milieu** — par exemple de l'air au verre ou à l'eau ? Elle subit un phénomène de **réfraction** qui modifie sa direction. C'est ce phénomène qui permet le fonctionnement des **lentilles**, des **lunettes**, des **appareils photo** et de notre **œil** lui-même.

---

## Propagation rectiligne de la lumière

### Principe

Dans un milieu **homogène**, **transparent** et **isotrope**, la lumière se propage en **ligne droite**. On modélise le trajet de la lumière par un **rayon lumineux** : une droite orientée dans le sens de propagation.

### La vitesse de la lumière

La vitesse de la lumière dans le **vide** est une constante universelle :

$$c = 3{,}00 \\times 10^8 \\text{ m/s}$$

Dans un milieu matériel transparent (eau, verre…), la lumière se propage à une vitesse $v < c$.

### L'indice de réfraction

L'**indice de réfraction** $n$ d'un milieu transparent caractérise le « ralentissement » de la lumière dans ce milieu :

$$\\boxed{n = \\frac{c}{v}}$$

avec :
- $n$ sans unité (toujours $\\geq 1$)
- $c = 3{,}00 \\times 10^8$ m/s
- $v$ la vitesse de la lumière dans le milieu (m/s)

| Milieu | Indice $n$ |
|---|---|
| Vide | 1,000 |
| Air | 1,000 (≈ 1) |
| Eau | 1,33 |
| Verre courant | 1,50 |
| Diamant | 2,42 |

> Plus $n$ est grand, plus la lumière est « ralentie » dans le milieu, et plus le milieu est dit **réfringent**.

---

## La réflexion

### Principe

Lorsqu'un rayon lumineux rencontre une surface réfléchissante (miroir), il est **renvoyé** dans le même milieu.

### Loi de la réflexion

Le rayon réfléchi est tel que :

$$\\boxed{\\hat{i}_r = \\hat{i}_1}$$

- L'**angle d'incidence** $\\hat{i}_1$ est l'angle entre le rayon incident et la **normale** (perpendiculaire à la surface au point d'incidence).
- L'**angle de réflexion** $\\hat{i}_r$ est l'angle entre le rayon réfléchi et la normale.
- Le rayon incident, la normale et le rayon réfléchi sont dans le **même plan** (plan d'incidence).

---

## La réfraction

### Principe

Lorsqu'un rayon lumineux passe d'un milieu transparent d'indice $n_1$ à un milieu d'indice $n_2$ **différent**, il subit un **changement de direction** à la surface de séparation : c'est la **réfraction**.

### Lois de Snell-Descartes pour la réfraction

**1ère loi :** le rayon réfracté est dans le **plan d'incidence** (plan contenant le rayon incident et la normale).

**2ème loi (loi de Snell-Descartes) :**

$$\\boxed{n_1 \\sin(i_1) = n_2 \\sin(i_2)}$$

avec :
- $i_1$ l'angle d'incidence
- $i_2$ l'angle de réfraction
- $n_1$ l'indice du milieu incident
- $n_2$ l'indice du milieu réfracté

### Cas de figure

- Si $n_2 > n_1$ (passage vers un milieu plus réfringent, ex : air → verre) : le rayon se **rapproche** de la normale ($i_2 < i_1$).
- Si $n_2 < n_1$ (passage vers un milieu moins réfringent, ex : verre → air) : le rayon **s'éloigne** de la normale ($i_2 > i_1$).

### La réflexion totale

Lorsque la lumière passe d'un milieu plus réfringent vers un milieu moins réfringent ($n_1 > n_2$), il existe un **angle limite** $i_\\ell$ au-delà duquel **toute la lumière est réfléchie** : c'est la **réflexion totale interne**.

$$\\sin(i_\\ell) = \\frac{n_2}{n_1}$$

> **Application cruciale :** la réflexion totale est le principe de fonctionnement de la **fibre optique**, qui permet la transmission de données à très haut débit sur de longues distances.

### Exercice résolu

Un rayon lumineux passe de l'air ($n_1 = 1{,}00$) au verre ($n_2 = 1{,}50$) avec un angle d'incidence $i_1 = 45°$. Calculer l'angle de réfraction.

**Solution :**

$$n_1 \\sin(i_1) = n_2 \\sin(i_2)$$

$$\\sin(i_2) = \\frac{n_1 \\sin(i_1)}{n_2} = \\frac{1{,}00 \\times \\sin(45°)}{1{,}50} = \\frac{0{,}707}{1{,}50} = 0{,}471$$

$$i_2 = \\arcsin(0{,}471) \\approx 28{,}1°$$

Le rayon se rapproche de la normale : $i_2 = 28° < i_1 = 45°$ ✓

---

## La dispersion de la lumière

### Origine

L'indice de réfraction d'un milieu **dépend de la longueur d'onde** de la lumière :

$$n = n(\\lambda)$$

Les courtes longueurs d'onde (violet) ont un indice plus élevé que les grandes (rouge). Par conséquent, elles sont **plus déviées** lors de la réfraction.

### Conséquence

Lorsque la lumière blanche traverse un **prisme**, chaque radiation est déviée différemment → le faisceau est **décomposé** en ses couleurs constitutives. C'est le phénomène de **dispersion**.

> **Dans la nature :** l'arc-en-ciel résulte de la dispersion de la lumière solaire par les gouttes d'eau (réfraction + réflexion totale interne + réfraction).

---

## Les lentilles minces convergentes

### Définition

Une **lentille mince convergente** est un bloc de verre (ou plastique) transparent, plus épais au centre qu'aux bords, qui fait **converger** les rayons lumineux qui la traversent.

### Éléments caractéristiques

| Élément | Notation | Définition |
|---|---|---|
| Centre optique | $O$ | Centre de la lentille ; un rayon passant par $O$ n'est pas dévié |
| Axe optique | — | Droite perpendiculaire à la lentille passant par $O$ |
| Foyer image | $F'$ | Point où convergent des rayons incidents parallèles à l'axe |
| Foyer objet | $F$ | Symétrique de $F'$ par rapport à $O$ |
| Distance focale | $f'$ | Distance $OF' > 0$ pour une lentille convergente |

### Rayons particuliers

Pour construire l'image d'un objet, on utilise **trois rayons** dont on connaît le trajet :

1. Un rayon **parallèle à l'axe optique** → passe par le foyer image $F'$ après la lentille.
2. Un rayon passant par le **centre optique** $O$ → n'est **pas dévié**.
3. Un rayon passant par le **foyer objet** $F$ → ressort **parallèle** à l'axe optique.

L'**intersection** de deux de ces rayons (au moins) donne la position de l'image.

---

## Formation d'une image

### Relation de conjugaison

Pour une lentille mince convergente, la position de l'image $A'$ d'un objet ponctuel $A$ situé sur l'axe est donnée par la **relation de conjugaison** (avec origine au centre optique) :

$$\\boxed{\\frac{1}{\\overline{OA'}} - \\frac{1}{\\overline{OA}} = \\frac{1}{f'}}$$

**Convention de signe :** les distances sont algébriques, orientées dans le sens de propagation de la lumière. Un objet situé **avant** la lentille a $\\overline{OA} < 0$.

### Le grandissement

Le **grandissement** $\\gamma$ (gamma) caractérise le rapport de taille entre l'image et l'objet :

$$\\boxed{\\gamma = \\frac{\\overline{A'B'}}{\\overline{AB}} = \\frac{\\overline{OA'}}{\\overline{OA}}}$$

- Si $|\\gamma| > 1$ : l'image est **plus grande** que l'objet.
- Si $|\\gamma| < 1$ : l'image est **plus petite** que l'objet.
- Si $\\gamma > 0$ : l'image est **droite** (même sens que l'objet).
- Si $\\gamma < 0$ : l'image est **renversée**.

### Exercice résolu

Un objet est placé à $\\overline{OA} = -30$ cm d'une lentille convergente de distance focale $f' = 10$ cm. Trouver la position de l'image et le grandissement.

**Solution :**

$$\\frac{1}{\\overline{OA'}} = \\frac{1}{f'} + \\frac{1}{\\overline{OA}} = \\frac{1}{10} + \\frac{1}{(-30)} = \\frac{3}{30} - \\frac{1}{30} = \\frac{2}{30} = \\frac{1}{15}$$

$$\\overline{OA'} = +15 \\text{ cm}$$

L'image est à 15 cm **après** la lentille (image réelle).

$$\\gamma = \\frac{\\overline{OA'}}{\\overline{OA}} = \\frac{15}{-30} = -0{,}5$$

L'image est **renversée** ($\\gamma < 0$) et **deux fois plus petite** ($|\\gamma| = 0{,}5$).

---

## Modèle simplifié de l'œil

### L'œil comme système optique

L'**œil humain** peut être modélisé comme un système optique convergent :

| Partie de l'œil | Modèle optique |
|---|---|
| Cornée + cristallin | Lentille convergente (distance focale variable) |
| Rétine | Écran (où se forme l'image) |
| Iris (pupille) | Diaphragme (régule la quantité de lumière) |

### L'accommodation

Le cristallin peut modifier sa **courbure** (et donc sa distance focale $f'$) grâce aux muscles ciliaires :

- **Œil au repos** : $f'$ maximale → l'œil voit net les objets **éloignés** (point le plus loin = **punctum remotum**, à l'infini pour un œil normal).
- **Œil accommodant** : $f'$ diminue → l'œil voit net les objets **proches** (point le plus proche = **punctum proximum**, environ 25 cm pour un œil normal).

### Défauts de la vision

| Défaut | Cause | Image | Correction |
|---|---|---|---|
| **Myopie** | Œil trop long ou trop convergent | Se forme **avant** la rétine | Lentille divergente |
| **Hypermétropie** | Œil trop court ou pas assez convergent | Se forme **après** la rétine | Lentille convergente |

---

## À retenir

- L'**indice de réfraction** : $n = \\frac{c}{v}$ ($n \\geq 1$).
- **Loi de Snell-Descartes** : $n_1 \\sin(i_1) = n_2 \\sin(i_2)$.
- Si $n_2 > n_1$ → le rayon se rapproche de la normale ; si $n_1 > n_2$ → il s'en éloigne (possibilité de **réflexion totale**).
- La **dispersion** : l'indice dépend de $\\lambda$ → décomposition de la lumière blanche par un prisme.
- **Lentille convergente** : $f' > 0$ ; relation de conjugaison $\\frac{1}{\\overline{OA'}} - \\frac{1}{\\overline{OA}} = \\frac{1}{f'}$.
- **Grandissement** : $\\gamma = \\frac{\\overline{OA'}}{\\overline{OA}}$ ; $|\\gamma| > 1$ = agrandissement, $\\gamma < 0$ = image renversée.
- L'**œil** est modélisé par une lentille convergente (cornée + cristallin) et un écran (rétine). L'**accommodation** fait varier $f'$.
""",
                'quiz': {
                    'titre': "Quiz — Réfraction, lentilles et formation d'images",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "L'indice de réfraction d'un milieu transparent est défini par :",
                            'options': ["n = c / v", "n = v / c", "n = c × v", "n = c + v"],
                            'reponse_correcte': '0',
                            'explication': "L'indice de réfraction est le rapport de la vitesse de la lumière dans le vide sur la vitesse dans le milieu : n = c/v.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "L'indice de réfraction de l'eau vaut environ :",
                            'options': ["1,33", "1,00", "1,50", "2,42"],
                            'reponse_correcte': '0',
                            'explication': "L'indice de réfraction de l'eau est d'environ 1,33.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "La loi de Snell-Descartes pour la réfraction s'écrit :",
                            'options': ["n₁ sin(i₁) = n₂ sin(i₂)", "n₁ cos(i₁) = n₂ cos(i₂)", "n₁ / sin(i₁) = n₂ / sin(i₂)", "n₁ + sin(i₁) = n₂ + sin(i₂)"],
                            'reponse_correcte': '0',
                            'explication': "La deuxième loi de Snell-Descartes relie les angles et les indices : n₁ sin(i₁) = n₂ sin(i₂).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Lorsqu'un rayon passe de l'air (n=1) au verre (n=1,5), il :",
                            'options': ["Se rapproche de la normale", "S'éloigne de la normale", "Ne change pas de direction", "Est totalement réfléchi"],
                            'reponse_correcte': '0',
                            'explication': "Quand n₂ > n₁, le rayon se rapproche de la normale (i₂ < i₁).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Le foyer image F' d'une lentille convergente est le point où convergent :",
                            'options': ["Les rayons incidents parallèles à l'axe optique", "Tous les rayons lumineux", "Les rayons passant par le centre optique", "Les rayons réfléchis"],
                            'reponse_correcte': '0',
                            'explication': "Le foyer image F' est le point où convergent les rayons arrivant parallèles à l'axe optique.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Un rayon passant par le centre optique O d'une lentille mince :",
                            'options': ["N'est pas dévié", "Est totalement réfléchi", "Converge vers F'", "Sort parallèle à l'axe"],
                            'reponse_correcte': '0',
                            'explication': "Un rayon passant par le centre optique O traverse la lentille sans être dévié.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "La loi de la réflexion stipule que :",
                            'options': ["L'angle d'incidence est égal à l'angle de réflexion", "L'angle d'incidence est le double de l'angle de réflexion", "L'angle de réflexion vaut toujours 45°", "Le rayon réfléchi est perpendiculaire au rayon incident"],
                            'reponse_correcte': '0',
                            'explication': "La loi de la réflexion impose que l'angle d'incidence soit égal à l'angle de réflexion.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "L'indice de réfraction d'un milieu est toujours :",
                            'options': ["Supérieur ou égal à 1", "Inférieur à 1", "Égal à 0 dans le vide", "Négatif pour les gaz"],
                            'reponse_correcte': '0',
                            'explication': "L'indice de réfraction est toujours ≥ 1 car la lumière ne peut pas aller plus vite que c.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "La réflexion totale interne se produit lorsque :",
                            'options': ["La lumière passe d'un milieu plus réfringent vers un milieu moins réfringent avec un angle supérieur à l'angle limite", "La lumière passe de l'air au verre", "L'angle d'incidence est nul", "Le milieu est opaque"],
                            'reponse_correcte': '0',
                            'explication': "La réflexion totale se produit quand n₁ > n₂ et que l'angle d'incidence dépasse l'angle limite.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "La fibre optique fonctionne grâce au principe de :",
                            'options': ["Réflexion totale interne", "Dispersion de la lumière", "Diffraction", "Absorption sélective"],
                            'reponse_correcte': '0',
                            'explication': "La fibre optique guide la lumière par réflexion totale interne successive.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Si le grandissement γ = −0,5, l'image est :",
                            'options': ["Renversée et plus petite que l'objet", "Droite et plus grande", "Renversée et plus grande", "Droite et de même taille"],
                            'reponse_correcte': '0',
                            'explication': "γ < 0 signifie image renversée ; |γ| = 0,5 < 1 signifie image plus petite.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Dans le modèle simplifié de l'œil, la rétine joue le rôle :",
                            'options': ["D'écran", "De lentille convergente", "De diaphragme", "De miroir"],
                            'reponse_correcte': '0',
                            'explication': "La rétine est la surface sur laquelle se forme l'image, elle joue le rôle d'écran.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "La myopie se corrige avec une lentille :",
                            'options': ["Divergente", "Convergente", "Plan-convexe", "Cylindrique"],
                            'reponse_correcte': '0',
                            'explication': "L'œil myope est trop convergent ; une lentille divergente compense l'excès de convergence.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "L'accommodation de l'œil consiste à modifier :",
                            'options': ["La distance focale du cristallin", "La taille de la rétine", "L'indice de réfraction de l'air", "La distance entre l'œil et l'objet"],
                            'reponse_correcte': '0',
                            'explication': "Les muscles ciliaires déforment le cristallin pour modifier sa distance focale et voir net à différentes distances.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "La vitesse de la lumière dans un milieu matériel transparent est toujours inférieure à c.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Dans tout milieu matériel transparent, v < c, d'où n = c/v > 1.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Un diamant a un indice de réfraction plus faible que celui de l'eau.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le diamant a un indice n = 2,42 bien supérieur à celui de l'eau (n = 1,33).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "La dispersion de la lumière par un prisme est due au fait que l'indice de réfraction dépend de la longueur d'onde.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "L'indice varie avec λ : les courtes longueurs d'onde (violet) sont plus déviées que les grandes (rouge).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on le phénomène de changement de direction de la lumière lorsqu'elle passe d'un milieu à un autre ?",
                            'options': None,
                            'reponse_correcte': 'réfraction',
                            'tolerances': ["la réfraction", "refraction", "la refraction"],
                            'explication': "La réfraction est le changement de direction d'un rayon lumineux lors du passage d'un milieu à un autre.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on le point le plus éloigné que l'œil peut voir nettement sans accommoder ?",
                            'options': None,
                            'reponse_correcte': 'punctum remotum',
                            'tolerances': ["le punctum remotum", "remotum"],
                            'explication': "Le punctum remotum est le point le plus éloigné visible sans accommodation (à l'infini pour un œil normal).",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quel est l'indice de réfraction du verre courant ? (donner la valeur numérique)",
                            'options': None,
                            'reponse_correcte': '1.5',
                            'tolerances': ["1,5", "1.50", "1,50"],
                            'explication': "L'indice de réfraction du verre courant est d'environ 1,50.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 6 — L'énergie et ses conversions
    # ──────────────────────────────────────────────
    {
        'ordre': 6,
        'titre': "L'énergie et ses conversions",
        'description': "Formes d'énergie, conservation, transferts thermiques et conversions dans les systèmes physiques.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Formes d'énergie et principe de conservation",
                'duree': 40,
                'contenu': """# Formes d'énergie et principe de conservation

## Introduction

L'énergie est une grandeur **fondamentale** en physique. Elle intervient dans tous les phénomènes : le mouvement d'un objet, le chauffage d'un liquide, le fonctionnement d'un moteur, l'émission de lumière… Cette leçon présente les différentes **formes d'énergie** et le principe fondamental qui les relie : la **conservation de l'énergie**.

---

## Qu'est-ce que l'énergie ?

### Définition qualitative

L'**énergie** est une grandeur physique qui caractérise la capacité d'un système à **produire des transformations** : mettre en mouvement, chauffer, éclairer, déformer, etc.

L'énergie s'exprime en **joules** (J) dans le Système International.

> **Ordres de grandeur :**
> - Énergie d'une pomme tombant de 1 m : $\\approx 1$ J
> - Énergie cinétique d'une voiture à 90 km/h : $\\approx 3 \\times 10^5$ J
> - Énergie consommée par un foyer français en un jour : $\\approx 5 \\times 10^7$ J

---

## Les différentes formes d'énergie

### L'énergie cinétique $E_c$

L'**énergie cinétique** est l'énergie que possède un objet **du fait de son mouvement**. Elle dépend de la masse $m$ et de la vitesse $v$ de l'objet :

$$E_c = \\frac{1}{2} m v^2$$

- $E_c$ en joules (J)
- $m$ en kilogrammes (kg)
- $v$ en mètres par seconde (m/s)

> **Exemple :** une voiture de masse $m = 1200$ kg roulant à $v = 30$ m/s (108 km/h) possède une énergie cinétique :
>
> $$E_c = \\frac{1}{2} \\times 1200 \\times 30^2 = 5{,}4 \\times 10^5 \\text{ J} = 540 \\text{ kJ}$$

**Propriétés importantes :**
- $E_c$ est toujours **positive ou nulle** ($E_c = 0$ si l'objet est immobile).
- $E_c$ est **proportionnelle** au carré de la vitesse : doubler la vitesse **quadruple** l'énergie cinétique.
- $E_c$ dépend du **référentiel** (car $v$ en dépend).

### L'énergie potentielle de pesanteur $E_{pp}$

L'**énergie potentielle de pesanteur** est l'énergie que possède un objet **du fait de sa position en altitude** dans le champ de pesanteur terrestre :

$$E_{pp} = mgh$$

- $E_{pp}$ en joules (J)
- $m$ en kilogrammes (kg)
- $g \\approx 9{,}81$ m/s² (intensité de la pesanteur)
- $h$ en mètres (m) : altitude par rapport à une **référence** choisie

> **Exemple :** un livre de 500 g posé sur une étagère à 2 m du sol :
>
> $$E_{pp} = 0{,}5 \\times 9{,}81 \\times 2 = 9{,}81 \\text{ J}$$

**Remarques :**
- Le choix de l'**altitude de référence** ($h = 0$) est arbitraire mais doit être précisé.
- $E_{pp}$ peut être **négative** si l'objet se trouve **sous** l'altitude de référence.

### L'énergie mécanique $E_m$

L'**énergie mécanique** est la somme de l'énergie cinétique et de l'énergie potentielle de pesanteur :

$$E_m = E_c + E_{pp} = \\frac{1}{2}mv^2 + mgh$$

---

## Le principe de conservation de l'énergie

### Énoncé fondamental

> **L'énergie totale d'un système isolé se conserve.** Elle ne peut être ni créée, ni détruite : elle se **transforme** d'une forme en une autre ou se **transfère** d'un système à un autre.

### Conservation de l'énergie mécanique

Pour un système soumis **uniquement à son poids** (chute libre, sans frottement), l'énergie mécanique se conserve :

$$E_m = E_c + E_{pp} = \\text{constante}$$

Autrement dit, si $E_{pp}$ diminue (l'objet descend), alors $E_c$ augmente (il accélère), et inversement.

> **Exemple : chute libre**
>
> Un objet de masse $m$ lâché depuis une hauteur $h_0$ sans vitesse initiale.
>
> - En haut : $E_c = 0$ et $E_{pp} = mgh_0$ → $E_m = mgh_0$
> - En bas ($h = 0$) : $E_{pp} = 0$ et $E_c = \\frac{1}{2}mv^2$ → $E_m = \\frac{1}{2}mv^2$
>
> Conservation : $mgh_0 = \\frac{1}{2}mv^2$ → $v = \\sqrt{2gh_0}$

### Cas avec frottements — Non-conservation de $E_m$

Lorsque des **frottements** ou d'autres forces dissipatives interviennent, l'énergie mécanique **diminue**. L'énergie « perdue » est en réalité **convertie** en énergie thermique (chaleur) :

$$\\Delta E_m = E_{m,\\text{final}} - E_{m,\\text{initial}} < 0$$

$$|\\Delta E_m| = Q_{\\text{dissipée}}$$

L'énergie **totale** (mécanique + thermique) reste constante : le principe de conservation est toujours valide, mais l'énergie mécanique seule ne se conserve plus.

---

## Diagrammes énergétiques

Un **diagramme énergétique** (ou chaîne énergétique) permet de représenter schématiquement les **conversions** et **transferts** d'énergie dans un système.

### Conventions

- Chaque **réservoir d'énergie** est représenté par un ovale (ou rectangle).
- Les **flèches** indiquent le sens du transfert d'énergie.
- On peut indiquer la forme d'énergie et sa valeur sur chaque flèche.

### Exemple : chute libre d'une balle

```
  [Énergie potentielle]  ──→  [Énergie cinétique]
       E_pp diminue              E_c augmente
```

### Exemple : freinage d'une voiture

```
  [Énergie cinétique]  ──→  [Énergie thermique]
       E_c diminue           (chaleur dans les freins)
```

---

## Unités et conversions

| Unité | Symbole | Équivalence en joules |
|---|---|---|
| Joule | J | 1 J |
| Kilojoule | kJ | $10^3$ J |
| Calorie | cal | 4,18 J |
| Kilocalorie | kcal | 4180 J |
| Kilowatt-heure | kWh | $3{,}6 \\times 10^6$ J |
| Électronvolt | eV | $1{,}6 \\times 10^{-19}$ J |

### La puissance

La **puissance** $P$ est l'énergie transférée (ou convertie) par unité de temps :

$$P = \\frac{E}{\\Delta t}$$

- $P$ en watts (W)
- $E$ en joules (J)
- $\\Delta t$ en secondes (s)

> **Exemple :** une lampe de 60 W consomme 60 J chaque seconde. En 1 heure :
>
> $$E = P \\times \\Delta t = 60 \\times 3600 = 216\\,000 \\text{ J} = 216 \\text{ kJ}$$

---

## À retenir

- L'**énergie cinétique** : $E_c = \\frac{1}{2}mv^2$ (énergie de mouvement).
- L'**énergie potentielle de pesanteur** : $E_{pp} = mgh$ (énergie de position).
- L'**énergie mécanique** : $E_m = E_c + E_{pp}$.
- **Principe de conservation** : l'énergie totale d'un système isolé se conserve ; elle se transforme ou se transfère mais ne disparaît jamais.
- Sans frottement : $E_m$ se conserve. Avec frottements : $E_m$ diminue, convertie en énergie thermique.
- **Puissance** : $P = \\frac{E}{\\Delta t}$ (en watts).
""",
                'quiz': {
                    'titre': "Quiz — Formes d'énergie et principe de conservation",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "L'unité de l'énergie dans le Système International est :",
                            'options': ["Le joule (J)", "Le watt (W)", "Le newton (N)", "Le kilogramme (kg)"],
                            'reponse_correcte': '0',
                            'explication': "L'énergie s'exprime en joules (J) dans le Système International.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "L'énergie cinétique d'un objet dépend de :",
                            'options': ["Sa masse et sa vitesse", "Sa masse uniquement", "Son altitude", "Sa température"],
                            'reponse_correcte': '0',
                            'explication': "L'énergie cinétique Ec = ½mv² dépend de la masse m et de la vitesse v.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "La formule de l'énergie cinétique est :",
                            'options': ["Ec = ½mv²", "Ec = mgh", "Ec = mv", "Ec = ½mgh"],
                            'reponse_correcte': '0',
                            'explication': "L'énergie cinétique est Ec = ½mv², proportionnelle au carré de la vitesse.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "L'énergie potentielle de pesanteur s'exprime par :",
                            'options': ["Epp = mgh", "Epp = ½mv²", "Epp = mg/h", "Epp = mh/g"],
                            'reponse_correcte': '0',
                            'explication': "L'énergie potentielle de pesanteur est Epp = mgh avec h l'altitude par rapport à la référence.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "L'énergie mécanique est la somme de :",
                            'options': ["L'énergie cinétique et l'énergie potentielle de pesanteur", "L'énergie thermique et l'énergie chimique", "L'énergie cinétique et l'énergie thermique", "L'énergie potentielle et l'énergie nucléaire"],
                            'reponse_correcte': '0',
                            'explication': "L'énergie mécanique Em = Ec + Epp.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "La puissance est définie comme :",
                            'options': ["L'énergie transférée par unité de temps", "La force multipliée par la masse", "L'énergie multipliée par le temps", "La vitesse multipliée par la masse"],
                            'reponse_correcte': '0',
                            'explication': "La puissance P = E/Δt est l'énergie transférée (ou convertie) par unité de temps, en watts.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "1 kWh est équivalent à :",
                            'options': ["3,6 × 10⁶ J", "1 000 J", "3 600 J", "1 × 10⁹ J"],
                            'reponse_correcte': '0',
                            'explication': "1 kWh = 1000 W × 3600 s = 3,6 × 10⁶ J.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Si on double la vitesse d'un objet, son énergie cinétique est multipliée par :",
                            'options': ["4", "2", "8", "1"],
                            'reponse_correcte': '0',
                            'explication': "Ec = ½mv² : si v est doublé, v² est multiplié par 4, donc Ec aussi.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Lors d'une chute libre (sans frottement), l'énergie mécanique :",
                            'options': ["Se conserve", "Augmente", "Diminue", "S'annule"],
                            'reponse_correcte': '0',
                            'explication': "Sans frottement, l'énergie mécanique Em = Ec + Epp reste constante.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Un objet de 2 kg lâché d'une hauteur de 5 m atteint le sol avec une vitesse d'environ :",
                            'options': ["10 m/s", "5 m/s", "20 m/s", "50 m/s"],
                            'reponse_correcte': '0',
                            'explication': "v = √(2gh) = √(2 × 9,81 × 5) ≈ √(98,1) ≈ 9,9 m/s ≈ 10 m/s.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Lorsque des frottements interviennent, l'énergie mécanique perdue est convertie en :",
                            'options': ["Énergie thermique", "Énergie potentielle", "Énergie nucléaire", "Énergie lumineuse"],
                            'reponse_correcte': '0',
                            'explication': "Les frottements dissipent l'énergie mécanique sous forme de chaleur (énergie thermique).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Une lampe de 100 W fonctionne pendant 2 heures. L'énergie consommée est :",
                            'options': ["720 kJ", "200 J", "200 kJ", "100 kJ"],
                            'reponse_correcte': '0',
                            'explication': "E = P × Δt = 100 × (2 × 3600) = 720 000 J = 720 kJ.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Pendant une chute libre, quand l'énergie potentielle diminue, l'énergie cinétique :",
                            'options': ["Augmente de la même quantité", "Diminue aussi", "Reste constante", "Devient nulle"],
                            'reponse_correcte': '0',
                            'explication': "Conservation de Em : si Epp diminue, Ec augmente du même montant.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Le choix de l'altitude de référence (h = 0) pour l'énergie potentielle :",
                            'options': ["Est arbitraire mais doit être précisé", "Doit toujours être le sol", "Doit être le centre de la Terre", "N'a aucune importance"],
                            'reponse_correcte': '0',
                            'explication': "Le choix de la référence d'altitude est libre, mais il faut le préciser pour que Epp ait un sens.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "L'énergie cinétique peut être négative.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Ec = ½mv² est toujours positive ou nulle (m > 0 et v² ≥ 0).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "L'énergie totale d'un système isolé se conserve toujours.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Le principe de conservation de l'énergie stipule que l'énergie totale d'un système isolé est constante.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "En présence de frottements, l'énergie mécanique d'un système augmente.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Les frottements dissipent l'énergie mécanique (elle diminue), convertie en énergie thermique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quelle formule permet de calculer la vitesse d'un objet en chute libre depuis une hauteur h, sans vitesse initiale ? (format : v = ...)",
                            'options': None,
                            'reponse_correcte': 'v = √(2gh)',
                            'tolerances': ["√(2gh)", "racine de 2gh", "v=racine(2gh)", "v = racine(2gh)", "racine(2gh)"],
                            'explication': "Conservation de Em : mgh = ½mv² donne v = √(2gh).",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on l'énergie liée au mouvement d'un objet ?",
                            'options': None,
                            'reponse_correcte': 'énergie cinétique',
                            'tolerances': ["energie cinetique", "l'énergie cinétique", "l'energie cinetique", "cinétique"],
                            'explication': "L'énergie cinétique est l'énergie que possède un objet du fait de son mouvement.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quelle est l'unité de la puissance dans le Système International ?",
                            'options': None,
                            'reponse_correcte': 'watt',
                            'tolerances': ["le watt", "W", "watts"],
                            'explication': "La puissance s'exprime en watts (W), avec 1 W = 1 J/s.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': "Transferts thermiques et conversions d'énergie",
                'duree': 40,
                'contenu': """# Transferts thermiques et conversions d'énergie

## Introduction

L'énergie n'existe pas sous une seule forme : elle se **convertit** et se **transfère** en permanence. Cette leçon explore les différents modes de **transfert thermique**, les **conversions d'énergie** dans les systèmes courants et la notion de **rendement**.

---

## L'énergie thermique et la température

### Température et agitation thermique

La **température** d'un corps est liée à l'**agitation thermique** de ses particules (atomes, molécules). Plus les particules sont agitées, plus la température est élevée.

- La température se mesure en **degrés Celsius** (°C) ou en **kelvins** (K).
- Relation : $T(\\text{K}) = T(°\\text{C}) + 273{,}15$
- Le **zéro absolu** ($0$ K = $-273{,}15$ °C) correspond à l'arrêt total de l'agitation thermique.

### Énergie thermique

L'**énergie thermique** (ou énergie interne) $U$ d'un système est la somme des énergies cinétiques et potentielles de toutes ses particules à l'échelle microscopique.

Lorsqu'un corps reçoit de l'énergie thermique, sa température **augmente** (en général). La relation est :

$$Q = mc\\Delta T$$

- $Q$ : énergie thermique transférée (J)
- $m$ : masse du corps (kg)
- $c$ : **capacité thermique massique** du matériau (J·kg⁻¹·°C⁻¹)
- $\\Delta T = T_f - T_i$ : variation de température (°C ou K)

> **Valeurs de $c$ courantes :**
>
> | Matériau | $c$ (J·kg⁻¹·°C⁻¹) |
> |---|---|
> | Eau liquide | 4180 |
> | Glace | 2090 |
> | Aluminium | 897 |
> | Cuivre | 385 |
> | Fer | 444 |

> **Exemple :** chauffer 1 L d'eau ($m = 1$ kg) de 20 °C à 100 °C :
>
> $$Q = 1 \\times 4180 \\times (100 - 20) = 334\\,400 \\text{ J} \\approx 334 \\text{ kJ}$$

---

## Les trois modes de transfert thermique

Le transfert thermique se produit **spontanément** du corps **chaud** vers le corps **froid**. Il existe trois modes de transfert :

### 1. La conduction

La **conduction thermique** est le transfert d'énergie thermique **de proche en proche** au sein d'un milieu matériel, **sans déplacement de matière**.

- Prépondérante dans les **solides**.
- Les **métaux** sont de bons conducteurs thermiques ; les **isolants** (bois, polystyrène, laine de verre) sont de mauvais conducteurs.

> **Exemple :** une cuillère en métal plongée dans une soupe chaude → le manche devient chaud par conduction.

### 2. La convection

La **convection** est le transfert d'énergie thermique dû au **déplacement de matière** (fluide : liquide ou gaz).

- Le fluide chauffé **se dilate**, devient moins dense et **monte** → remplacé par du fluide froid → création de **courants de convection**.
- Prépondérante dans les **fluides** (liquides et gaz).

> **Exemple :** l'eau chauffée par le bas dans une casserole → courants de convection ; l'air chaud qui monte au-dessus d'un radiateur.

### 3. Le rayonnement

Le **rayonnement thermique** est le transfert d'énergie par **ondes électromagnétiques** (notamment infrarouges). Il ne nécessite **aucun milieu matériel** : il se propage aussi dans le **vide**.

- Tout corps dont la température est supérieure à 0 K émet un rayonnement.
- Plus la température est élevée, plus le rayonnement est intense.

> **Exemple :** le Soleil réchauffe la Terre à travers le vide spatial par rayonnement ; on sent la chaleur d'un feu de cheminée à distance.

### Tableau récapitulatif

| Mode | Mécanisme | Milieu | Exemple |
|---|---|---|---|
| **Conduction** | De proche en proche (sans déplacement de matière) | Solides surtout | Cuillère dans un thé chaud |
| **Convection** | Déplacement de matière | Fluides (liquides, gaz) | Courants dans une casserole |
| **Rayonnement** | Ondes électromagnétiques | Tous milieux + vide | Chaleur du Soleil |

---

## Conversions d'énergie dans les systèmes courants

### Le principe général

Un **convertisseur d'énergie** reçoit de l'énergie sous une forme et la restitue sous une ou plusieurs **autres formes**.

### Exemples de conversions

| Convertisseur | Énergie reçue | Énergie utile | Énergie « perdue » |
|---|---|---|---|
| **Moteur électrique** | Électrique | Cinétique (mécanique) | Thermique (échauffement) |
| **Panneau solaire photovoltaïque** | Rayonnement (lumineuse) | Électrique | Thermique |
| **Panneau solaire thermique** | Rayonnement (lumineuse) | Thermique | — |
| **Lampe à incandescence** | Électrique | Rayonnement (lumineuse) | Thermique (95 %) |
| **Lampe LED** | Électrique | Rayonnement (lumineuse) | Thermique (faible) |
| **Pile électrochimique** | Chimique | Électrique | Thermique |
| **Centrale nucléaire** | Nucléaire → Thermique → Cinétique | Électrique | Thermique (rejet dans l'environnement) |
| **Muscle** | Chimique (glucose + O₂) | Cinétique (mécanique) | Thermique |

### Chaîne énergétique d'une centrale thermique

```
[Énergie chimique]  →  [Énergie thermique]  →  [Énergie cinétique]  →  [Énergie électrique]
  (combustible)         (chaudière)              (turbine)               (alternateur)
                             ↓                        ↓
                      [Pertes thermiques]      [Pertes thermiques]
```

---

## Le rendement

### Définition

Le **rendement** $\\eta$ (lettre grecque « êta ») d'un convertisseur est le rapport entre l'énergie **utile** fournie et l'énergie **totale** reçue :

$$\\eta = \\frac{E_{\\text{utile}}}{E_{\\text{reçue}}}$$

- $\\eta$ est un nombre **sans unité**, compris entre 0 et 1.
- On l'exprime souvent en **pourcentage** : $\\eta = 0{,}30$ → rendement de 30 %.

> Un rendement de 100 % signifierait que **toute** l'énergie reçue est convertie en énergie utile (impossible en pratique à cause des pertes).

### Rendements typiques

| Convertisseur | Rendement typique |
|---|---|
| Moteur électrique | 85 – 95 % |
| Panneau photovoltaïque | 15 – 22 % |
| Lampe à incandescence | 5 % |
| Lampe LED | 30 – 50 % |
| Centrale nucléaire | 33 % |
| Centrale à gaz (cycle combiné) | 55 – 60 % |
| Muscle humain | 25 % |

### Puissance utile et puissance reçue

Le rendement peut aussi s'exprimer en termes de **puissance** :

$$\\eta = \\frac{P_{\\text{utile}}}{P_{\\text{reçue}}}$$

---

## Les sources d'énergie

### Sources renouvelables et non renouvelables

| Type | Caractéristique | Exemples |
|---|---|---|
| **Renouvelable** | Se régénère à l'échelle humaine | Solaire, éolien, hydraulique, biomasse, géothermie |
| **Non renouvelable** | Stock limité, épuisable | Pétrole, gaz, charbon, uranium |

### Impact environnemental

- Les **énergies fossiles** (charbon, pétrole, gaz) libèrent du $\\text{CO}_2$ lors de leur combustion → **effet de serre** et réchauffement climatique.
- L'**énergie nucléaire** ne produit pas de $\\text{CO}_2$ mais génère des **déchets radioactifs**.
- Les **énergies renouvelables** ont un impact moindre mais posent des questions d'**intermittence** (solaire, éolien) et d'**emprise au sol**.

---

## À retenir

- L'énergie thermique transférée : $Q = mc\\Delta T$.
- Trois modes de transfert thermique : **conduction** (solides), **convection** (fluides), **rayonnement** (tous milieux + vide).
- Le transfert thermique est toujours du **chaud** vers le **froid** (spontanément).
- Le **rendement** $\\eta = \\frac{E_{\\text{utile}}}{E_{\\text{reçue}}}$ est toujours inférieur à 1 en pratique.
- Les **sources d'énergie** sont renouvelables ou non renouvelables ; le choix a un impact environnemental majeur.
""",
                'quiz': {
                    'titre': "Quiz — Transferts thermiques et conversions d'énergie",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "La température est liée à :",
                            'options': ["L'agitation thermique des particules", "La masse du corps", "La pression atmosphérique", "Le volume du corps"],
                            'reponse_correcte': '0',
                            'explication': "La température d'un corps est liée à l'agitation thermique de ses particules.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "La relation entre kelvin et degré Celsius est :",
                            'options': ["T(K) = T(°C) + 273,15", "T(K) = T(°C) − 273,15", "T(K) = T(°C) × 273,15", "T(K) = T(°C) / 273,15"],
                            'reponse_correcte': '0',
                            'explication': "T(K) = T(°C) + 273,15. Le zéro absolu (0 K) correspond à −273,15 °C.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "La formule de l'énergie thermique transférée est :",
                            'options': ["Q = mcΔT", "Q = mgh", "Q = ½mv²", "Q = P × m"],
                            'reponse_correcte': '0',
                            'explication': "Q = mcΔT avec m la masse, c la capacité thermique massique et ΔT la variation de température.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "La capacité thermique massique de l'eau liquide vaut environ :",
                            'options': ["4180 J·kg⁻¹·°C⁻¹", "385 J·kg⁻¹·°C⁻¹", "897 J·kg⁻¹·°C⁻¹", "100 J·kg⁻¹·°C⁻¹"],
                            'reponse_correcte': '0',
                            'explication': "La capacité thermique massique de l'eau est d'environ 4180 J·kg⁻¹·°C⁻¹, la plus élevée des liquides courants.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La conduction thermique est un transfert de chaleur qui se fait :",
                            'options': ["De proche en proche sans déplacement de matière", "Par déplacement de matière", "Par ondes électromagnétiques", "Uniquement dans le vide"],
                            'reponse_correcte': '0',
                            'explication': "La conduction est un transfert thermique de proche en proche au sein d'un milieu, sans mouvement de matière.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "La convection est un transfert thermique dû à :",
                            'options': ["Un déplacement de matière (fluide)", "Des vibrations de proche en proche", "Des ondes électromagnétiques", "Un contact entre deux solides"],
                            'reponse_correcte': '0',
                            'explication': "La convection est un transfert thermique par déplacement de matière dans un fluide (liquide ou gaz).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Le rayonnement thermique peut se propager :",
                            'options': ["Dans le vide et dans la matière", "Uniquement dans les solides", "Uniquement dans les liquides", "Uniquement dans l'air"],
                            'reponse_correcte': '0',
                            'explication': "Le rayonnement se propage par ondes électromagnétiques et ne nécessite pas de milieu matériel.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Le transfert thermique se fait spontanément :",
                            'options': ["Du corps chaud vers le corps froid", "Du corps froid vers le corps chaud", "Dans les deux sens simultanément", "Uniquement entre corps de même température"],
                            'reponse_correcte': '0',
                            'explication': "Le transfert thermique spontané va toujours du corps le plus chaud vers le plus froid.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Le rendement d'un convertisseur d'énergie est défini comme :",
                            'options': ["Le rapport énergie utile / énergie reçue", "Le rapport énergie reçue / énergie utile", "La somme des énergies", "L'énergie perdue par unité de temps"],
                            'reponse_correcte': '0',
                            'explication': "Le rendement η = E_utile / E_reçue, toujours compris entre 0 et 1.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Le rendement d'une lampe à incandescence est d'environ :",
                            'options': ["5 %", "50 %", "90 %", "30 %"],
                            'reponse_correcte': '0',
                            'explication': "Une lampe à incandescence ne convertit qu'environ 5 % de l'énergie en lumière, le reste part en chaleur.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Un panneau solaire photovoltaïque convertit :",
                            'options': ["L'énergie lumineuse en énergie électrique", "L'énergie électrique en énergie lumineuse", "L'énergie chimique en énergie électrique", "L'énergie cinétique en énergie thermique"],
                            'reponse_correcte': '0',
                            'explication': "Un panneau photovoltaïque convertit le rayonnement solaire (énergie lumineuse) en énergie électrique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Les énergies fossiles (charbon, pétrole, gaz) sont qualifiées de :",
                            'options': ["Non renouvelables", "Renouvelables", "Inépuisables", "Nucléaires"],
                            'reponse_correcte': '0',
                            'explication': "Les énergies fossiles existent en stock limité et s'épuisent : elles sont non renouvelables.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Pour chauffer 2 kg d'eau de 20 °C à 80 °C (c = 4180 J·kg⁻¹·°C⁻¹), l'énergie nécessaire est :",
                            'options': ["501 600 J", "250 800 J", "83 600 J", "4 180 J"],
                            'reponse_correcte': '0',
                            'explication': "Q = mcΔT = 2 × 4180 × (80 − 20) = 2 × 4180 × 60 = 501 600 J.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Le Soleil réchauffe la Terre principalement par :",
                            'options': ["Rayonnement", "Conduction", "Convection", "Contact direct"],
                            'reponse_correcte': '0',
                            'explication': "La chaleur du Soleil atteint la Terre par rayonnement (ondes électromagnétiques à travers le vide spatial).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Le zéro absolu correspond à 0 °C.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le zéro absolu est 0 K = −273,15 °C, pas 0 °C.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Un rendement de 100 % est impossible en pratique pour un convertisseur d'énergie.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "En pratique, il y a toujours des pertes (thermiques, frottements…), donc η < 1.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "L'énergie nucléaire est une source d'énergie renouvelable.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "L'énergie nucléaire utilise l'uranium dont le stock est limité : elle est non renouvelable.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quel mode de transfert thermique se produit dans un fluide par déplacement de matière ?",
                            'options': None,
                            'reponse_correcte': 'convection',
                            'tolerances': ["la convection"],
                            'explication': "La convection est le transfert de chaleur par déplacement de matière dans un fluide.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on le rapport entre l'énergie utile et l'énergie reçue par un convertisseur ?",
                            'options': None,
                            'reponse_correcte': 'rendement',
                            'tolerances': ["le rendement", "η", "eta"],
                            'explication': "Le rendement η = E_utile / E_reçue mesure l'efficacité d'un convertisseur d'énergie.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quel mode de transfert thermique permet au Soleil de chauffer la Terre à travers le vide spatial ?",
                            'options': None,
                            'reponse_correcte': 'rayonnement',
                            'tolerances': ["le rayonnement", "rayonnement thermique", "le rayonnement thermique", "radiation"],
                            'explication': "Le rayonnement est le seul mode de transfert thermique qui se propage dans le vide.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 7 — Signaux et capteurs
    # ──────────────────────────────────────────────
    {
        'ordre': 7,
        'titre': "Signaux et capteurs",
        'description': "Signaux électriques, circuits de base, capteurs et lois fondamentales de l'électricité.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Le circuit électrique — tension, intensité et loi d'Ohm",
                'duree': 40,
                'contenu': """# Le circuit électrique — tension, intensité et loi d'Ohm

## Introduction

Les **circuits électriques** sont au cœur de tous les appareils que nous utilisons quotidiennement. Cette leçon présente les grandeurs fondamentales — **tension** et **intensité** — ainsi que la **loi d'Ohm**, relation essentielle pour comprendre le comportement des composants résistifs.

---

## Le circuit électrique

### Définition

Un **circuit électrique** est un ensemble de composants (générateur, récepteurs, fils conducteurs) reliés entre eux de façon à permettre la **circulation d'un courant électrique**.

### Le courant électrique

Le **courant électrique** est un déplacement ordonné de **porteurs de charges** :

- Dans les **métaux** : les porteurs sont les **électrons libres** (charges négatives).
- Dans les **solutions électrolytiques** : les porteurs sont des **ions** (positifs et négatifs).

### Sens conventionnel

Par convention, le **sens conventionnel** du courant va du pôle **+** vers le pôle **–** du générateur, à l'**extérieur** du générateur. Ce sens est **opposé** au sens réel de déplacement des électrons dans les métaux.

### Composants de base

| Composant | Rôle | Symbole |
|---|---|---|
| **Générateur** (pile, batterie) | Fournit l'énergie électrique | —\\|\\|— |
| **Lampe** | Convertit l'énergie électrique en lumière et chaleur | ⊗ |
| **Résistance** (résistor) | Limite le courant, convertit en chaleur | ▯ |
| **Interrupteur** | Ouvre ou ferme le circuit | / |
| **Diode** | Laisse passer le courant dans un seul sens | ▷\\| |
| **Moteur** | Convertit l'énergie électrique en énergie mécanique | M |

### Circuit ouvert et circuit fermé

- **Circuit fermé** : le courant peut circuler (boucle complète) → les récepteurs fonctionnent.
- **Circuit ouvert** : la boucle est interrompue → aucun courant ne circule.

---

## L'intensité du courant

### Définition

L'**intensité** $I$ du courant électrique est le **débit de charges** qui traversent une section du conducteur par unité de temps :

$$I = \\frac{Q}{\\Delta t}$$

- $I$ en ampères (A)
- $Q$ en coulombs (C) : quantité de charges
- $\\Delta t$ en secondes (s)

### Mesure

L'intensité se mesure avec un **ampèremètre**, branché **en série** dans le circuit (le courant doit traverser l'appareil).

### Ordres de grandeur

| Appareil | Intensité typique |
|---|---|
| LED | $\\approx 20$ mA |
| Lampe de bureau | $\\approx 0{,}3$ A |
| Radiateur électrique | $\\approx 10$ A |
| Démarreur de voiture | $\\approx 100$ A |
| Foudre | $\\approx 20\\,000$ A |

---

## La tension électrique

### Définition

La **tension électrique** $U$ entre deux points A et B d'un circuit est la **différence de potentiel** entre ces deux points :

$$U_{AB} = V_A - V_B$$

- $U$ en volts (V)
- $V_A$, $V_B$ : potentiels électriques (V)

La tension est ce qui « pousse » les charges à se déplacer : sans **différence de potentiel**, pas de courant.

### Mesure

La tension se mesure avec un **voltmètre**, branché **en dérivation** (en parallèle) entre les deux points considérés.

### Ordres de grandeur

| Source | Tension typique |
|---|---|
| Pile ronde (AA) | 1,5 V |
| Batterie de voiture | 12 V |
| Prise secteur (France) | 230 V (alternatif) |
| Ligne haute tension | 400 000 V |
| Tension neuronale | $\\approx 70$ mV |

---

## La loi d'Ohm

### Énoncé

Pour un **dipôle résistif** (résistor, aussi appelé résistance), la **tension** $U$ à ses bornes est proportionnelle à l'**intensité** $I$ du courant qui le traverse :

$$U = R \\times I$$

- $U$ en volts (V)
- $R$ en ohms ($\\Omega$) : résistance du dipôle
- $I$ en ampères (A)

### Caractéristique d'un résistor

La **caractéristique** $U = f(I)$ d'un résistor est une **droite passant par l'origine** dont la pente est $R$.

| $I$ (A) | $U$ (V) pour $R = 100\\ \\Omega$ |
|---|---|
| 0 | 0 |
| 0,05 | 5 |
| 0,10 | 10 |
| 0,15 | 15 |
| 0,20 | 20 |

### Puissance dissipée par effet Joule

Tout résistor traversé par un courant **dissipe** de l'énergie sous forme de **chaleur** (effet Joule). La puissance dissipée est :

$$P = U \\times I = R \\times I^2 = \\frac{U^2}{R}$$

> **Exemple :** un résistor de 220 Ω traversé par un courant de 0,1 A :
>
> $$P = 220 \\times (0{,}1)^2 = 2{,}2 \\text{ W}$$

---

## Association de résistances

### En série

Les résistances sont traversées par le **même courant**. La résistance équivalente est :

$$R_{\\text{eq}} = R_1 + R_2 + \\cdots + R_n$$

> Deux résistances de 100 Ω en série : $R_{\\text{eq}} = 200\\ \\Omega$.

### En dérivation (parallèle)

Les résistances sont soumises à la **même tension**. La résistance équivalente vérifie :

$$\\frac{1}{R_{\\text{eq}}} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\cdots + \\frac{1}{R_n}$$

Pour deux résistances :

$$R_{\\text{eq}} = \\frac{R_1 \\times R_2}{R_1 + R_2}$$

> Deux résistances de 100 Ω en parallèle : $R_{\\text{eq}} = \\frac{100 \\times 100}{100 + 100} = 50\\ \\Omega$.

---

## Les lois de Kirchhoff

### Loi des nœuds (loi des courants)

Un **nœud** est un point du circuit où **au moins trois conducteurs** se rejoignent.

> La somme des intensités des courants qui **entrent** dans un nœud est égale à la somme des intensités des courants qui en **sortent**.

$$\\sum I_{\\text{entrants}} = \\sum I_{\\text{sortants}}$$

> **Exemple :** si $I_1 = 3$ A entre dans un nœud et deux branches en sortent avec $I_2$ et $I_3$, alors : $I_1 = I_2 + I_3$.

### Loi des mailles (loi des tensions)

Une **maille** est un parcours fermé dans le circuit.

> La somme algébrique des tensions le long d'une maille est nulle.

$$\\sum U_i = 0$$

> **Exemple :** dans une maille contenant un générateur de tension $E$ et deux résistances $R_1$ et $R_2$ en série :
>
> $$E - U_1 - U_2 = 0 \\quad \\Rightarrow \\quad E = R_1 I + R_2 I$$

---

## À retenir

- L'**intensité** $I$ (A) est le débit de charges ; se mesure avec un ampèremètre **en série**.
- La **tension** $U$ (V) est la différence de potentiel ; se mesure avec un voltmètre **en dérivation**.
- **Loi d'Ohm** : $U = R \\times I$ pour un résistor.
- **Puissance dissipée** : $P = U \\times I = R I^2 = \\frac{U^2}{R}$.
- **Loi des nœuds** : $\\sum I_{\\text{entrants}} = \\sum I_{\\text{sortants}}$.
- **Loi des mailles** : $\\sum U_i = 0$ dans un parcours fermé.
- Résistances en **série** : $R_{\\text{eq}} = R_1 + R_2$ ; en **parallèle** : $\\frac{1}{R_{\\text{eq}}} = \\frac{1}{R_1} + \\frac{1}{R_2}$.
""",
                'quiz': {
                    'titre': "Quiz — Le circuit électrique, tension, intensité et loi d'Ohm",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quel est le sens conventionnel du courant électrique dans un circuit ?",
                            'options': ["Du pôle + vers le pôle – à l'extérieur du générateur", "Du pôle – vers le pôle + à l'extérieur du générateur", "Du pôle + vers le pôle – à l'intérieur du générateur", "Il n'y a pas de convention"],
                            'reponse_correcte': '0',
                            'explication': "Par convention, le courant circule du pôle + vers le pôle – à l'extérieur du générateur, soit le sens inverse du déplacement réel des électrons.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Comment doit-on brancher un ampèremètre dans un circuit ?",
                            'options': ["En série", "En dérivation (parallèle)", "Entre les bornes du générateur directement", "Peu importe, les deux fonctionnent"],
                            'reponse_correcte': '0',
                            'explication': "L'ampèremètre se branche toujours en série : le courant doit le traverser pour être mesuré.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Quelle est l'unité de la tension électrique ?",
                            'options': ["Le volt (V)", "L'ampère (A)", "L'ohm (Ω)", "Le watt (W)"],
                            'reponse_correcte': '0',
                            'explication': "La tension électrique, ou différence de potentiel, s'exprime en volts (V).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Comment branche-t-on un voltmètre ?",
                            'options': ["En dérivation (parallèle) entre les deux points de mesure", "En série dans le circuit", "À la place du composant à mesurer", "Entre le pôle + du générateur et la masse"],
                            'reponse_correcte': '0',
                            'explication': "Le voltmètre se branche en dérivation (parallèle) entre les deux points dont on veut mesurer la différence de potentiel.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Quels sont les porteurs de charge dans un fil métallique ?",
                            'options': ["Les électrons libres", "Les protons", "Les ions positifs", "Les neutrons"],
                            'reponse_correcte': '0',
                            'explication': "Dans les métaux, le courant est dû au déplacement ordonné des électrons libres (charges négatives).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Que se passe-t-il dans un circuit ouvert ?",
                            'options': ["Aucun courant ne circule", "Le courant circule normalement", "La tension est nulle partout", "Les résistances deviennent infinies"],
                            'reponse_correcte': '0',
                            'explication': "Dans un circuit ouvert, la boucle est interrompue et aucun courant ne peut circuler.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "D'après la loi d'Ohm, si $R = 200\\ \\Omega$ et $I = 0{,}05$ A, quelle est la tension $U$ ?",
                            'options': ["10 V", "4 000 V", "0,0025 V", "100 V"],
                            'reponse_correcte': '0',
                            'explication': "$U = R \\times I = 200 \\times 0{,}05 = 10$ V.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Quelle est la caractéristique $U = f(I)$ d'un résistor idéal ?",
                            'options': ["Une droite passant par l'origine", "Une courbe exponentielle", "Une droite ne passant pas par l'origine", "Une parabole"],
                            'reponse_correcte': '0',
                            'explication': "Pour un résistor obéissant à la loi d'Ohm, $U = RI$ est une relation linéaire passant par l'origine.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Quelle est la résistance équivalente de deux résistances de 100 Ω branchées en série ?",
                            'options': ["200 Ω", "100 Ω", "50 Ω", "10 000 Ω"],
                            'reponse_correcte': '0',
                            'explication': "En série, les résistances s'additionnent : $R_{eq} = R_1 + R_2 = 100 + 100 = 200\\ \\Omega$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quelle est la résistance équivalente de deux résistances de 100 Ω branchées en parallèle ?",
                            'options': ["50 Ω", "200 Ω", "100 Ω", "25 Ω"],
                            'reponse_correcte': '0',
                            'explication': "En parallèle : $R_{eq} = \\frac{R_1 \\times R_2}{R_1 + R_2} = \\frac{100 \\times 100}{200} = 50\\ \\Omega$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Un résistor de 50 Ω est traversé par un courant de 0,2 A. Quelle puissance dissipe-t-il ?",
                            'options': ["2 W", "10 W", "0,4 W", "25 W"],
                            'reponse_correcte': '0',
                            'explication': "$P = R \\times I^2 = 50 \\times (0{,}2)^2 = 50 \\times 0{,}04 = 2$ W.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Que stipule la loi des nœuds ?",
                            'options': ["La somme des courants entrants dans un nœud égale la somme des courants sortants", "La somme des tensions dans un nœud est nulle", "Le courant est le même partout dans un circuit", "La tension aux bornes d'un nœud est constante"],
                            'reponse_correcte': '0',
                            'explication': "La loi des nœuds (Kirchhoff) affirme que la somme des intensités entrant dans un nœud est égale à la somme des intensités sortantes.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Dans une maille contenant un générateur de 12 V et deux résistances en série ($R_1 = 200\\ \\Omega$, $R_2 = 400\\ \\Omega$), quelle est l'intensité $I$ ?",
                            'options': ["0,02 A", "0,06 A", "0,03 A", "2 A"],
                            'reponse_correcte': '0',
                            'explication': "Loi des mailles : $E = (R_1 + R_2) I$ → $I = \\frac{12}{200 + 400} = \\frac{12}{600} = 0{,}02$ A.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Quelle formule exprime la puissance électrique dissipée par un résistor en fonction de $U$ et $R$ uniquement ?",
                            'options': ["$P = U^2 / R$", "$P = R / U^2$", "$P = U \\times R$", "$P = R^2 / U$"],
                            'reponse_correcte': '0',
                            'explication': "En combinant $P = UI$ et $U = RI$, on obtient $P = U^2 / R$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'qcm',
                            'texte': "Si trois branches arrivent à un nœud avec $I_1 = 3$ A entrant, $I_2 = 1$ A sortant, quelle est $I_3$ ?",
                            'options': ["2 A sortant", "4 A sortant", "2 A entrant", "3 A sortant"],
                            'reponse_correcte': '0',
                            'explication': "Loi des nœuds : $I_1 = I_2 + I_3$ → $I_3 = 3 - 1 = 2$ A sortant.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'qcm',
                            'texte': "Qu'est-ce que l'effet Joule ?",
                            'options': ["L'échauffement d'un conducteur traversé par un courant", "La création d'un champ magnétique par un courant", "L'apparition d'une tension dans un circuit ouvert", "La variation de résistance avec la température"],
                            'reponse_correcte': '0',
                            'explication': "L'effet Joule est la dissipation d'énergie sous forme de chaleur lorsqu'un courant traverse un conducteur résistif.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Dans un circuit en série, l'intensité est la même en tout point du circuit.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "En série, il n'y a qu'un seul chemin pour le courant : l'intensité est identique partout.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'vrai_faux',
                            'texte': "La loi des mailles stipule que la somme algébrique des tensions le long d'une maille est nulle.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est exactement l'énoncé de la loi des mailles de Kirchhoff : $\\sum U_i = 0$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Quel appareil mesure l'intensité du courant dans un circuit ? (un mot)",
                            'options': None,
                            'reponse_correcte': 'ampèremètre',
                            'tolerances': ['amperemetre', 'ampéremètre', 'Ampèremètre', 'un ampèremètre'],
                            'explication': "L'intensité se mesure avec un ampèremètre, branché en série dans le circuit.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quelle est la formule de la loi d'Ohm reliant U, R et I ? (écrire sous la forme U = ...)",
                            'options': None,
                            'reponse_correcte': 'U = R × I',
                            'tolerances': ['U = RI', 'U=RI', 'U = R*I', 'U=R*I', 'U = R x I', 'U=RxI'],
                            'explication': "La loi d'Ohm s'écrit $U = R \\times I$ pour un dipôle résistif.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': "Capteurs électriques et signaux",
                'duree': 40,
                'contenu': """# Capteurs électriques et signaux

## Introduction

Les **capteurs** sont des composants qui permettent de convertir une grandeur physique (température, lumière, pression…) en un **signal électrique** exploitable. Ils sont au cœur des systèmes de mesure et des objets connectés. Cette leçon explore leur fonctionnement et les caractéristiques des signaux qu'ils produisent.

---

## Qu'est-ce qu'un capteur ?

### Définition

Un **capteur** est un dispositif qui transforme une **grandeur physique** (appelée le **mesurande**) en une **grandeur électrique** (tension, résistance, intensité…) mesurable.

### Schéma fonctionnel

```
  Grandeur physique       Capteur        Signal électrique
  (température, lumière,  ──────→        (tension, résistance
   pression, force…)                      variable…)
```

### Exemples de capteurs courants

| Capteur | Mesurande | Grandeur électrique qui varie |
|---|---|---|
| **Thermistance** (CTN) | Température | Résistance ($R$ diminue quand $T$ augmente) |
| **Photorésistance** (LDR) | Éclairement lumineux | Résistance ($R$ diminue quand la lumière augmente) |
| **Thermocouple** | Température | Tension |
| **Microphone** | Pression acoustique (son) | Tension |
| **Capteur de pression** | Pression | Tension |
| **Capteur à effet Hall** | Champ magnétique | Tension |

---

## La thermistance CTN

### Principe

Une **thermistance CTN** (*Coefficient de Température Négatif*) est une résistance dont la valeur **diminue** lorsque la température **augmente**.

### Caractéristique $R = f(T)$

La courbe $R(T)$ d'une CTN est une fonction **décroissante** :

| Température (°C) | Résistance typique (Ω) |
|---|---|
| 0 | 27 000 |
| 20 | 10 000 |
| 40 | 4 000 |
| 60 | 1 800 |
| 80 | 900 |
| 100 | 500 |

La relation n'est **pas linéaire** : la résistance chute rapidement au début puis plus lentement.

### Utilisation dans un circuit

Pour exploiter une thermistance comme capteur de température, on l'insère dans un **circuit diviseur de tension** :

$$U_{\\text{CTN}} = E \\times \\frac{R_{\\text{CTN}}}{R_{\\text{CTN}} + R_0}$$

où $E$ est la tension du générateur et $R_0$ une résistance fixe.

Quand la température augmente :
- $R_{\\text{CTN}}$ diminue
- $U_{\\text{CTN}}$ diminue
- On peut mesurer cette tension et en déduire la température

---

## La photorésistance (LDR)

### Principe

Une **photorésistance** (*Light Dependent Resistor*, LDR) est une résistance dont la valeur **diminue** lorsque l'**éclairement** augmente.

### Caractéristique $R = f(E_v)$

| Éclairement $E_v$ (lux) | Résistance typique (Ω) |
|---|---|
| 0 (obscurité) | > 1 000 000 |
| 10 (faible lumière) | 50 000 |
| 100 (pièce éclairée) | 5 000 |
| 1 000 (lumière du jour) | 500 |
| 10 000 (plein soleil) | 100 |

### Application

La photorésistance est utilisée dans les **détecteurs de luminosité** : éclairage public automatique, ajustement de la luminosité d'un écran, alarmes.

Montée en diviseur de tension, elle fournit une tension qui varie avec l'éclairement, facilement mesurable.

---

## Étalonnage d'un capteur

### Principe

**Étalonner** un capteur, c'est établir la **relation** entre le mesurande et la grandeur électrique de sortie. On réalise une série de mesures en faisant varier le mesurande de façon connue et en relevant la grandeur de sortie.

### Courbe d'étalonnage

On trace le graphique $U = f(\\text{mesurande})$ ou $R = f(\\text{mesurande})$. Cette courbe permet ensuite de **convertir** une mesure électrique en valeur du mesurande.

### Exemple

Pour étalonner une thermistance :

1. Plonger la CTN dans des bains d'eau à températures connues (mesurées avec un thermomètre de référence).
2. Mesurer $R$ (ou $U$ dans un diviseur de tension) pour chaque température.
3. Tracer $R = f(T)$ ou $U = f(T)$.
4. Lors d'une mesure inconnue : lire $R$ (ou $U$), puis utiliser la courbe pour en déduire $T$.

---

## Les signaux électriques

### Signal analogique

Un **signal analogique** varie de façon **continue** au cours du temps. Il peut prendre une infinité de valeurs dans un intervalle donné.

> **Exemple :** la tension délivrée par un microphone face à un son : une courbe continue $U(t)$.

### Signal numérique

Un **signal numérique** ne prend qu'un nombre **fini** de valeurs (souvent deux : 0 et 1). C'est le langage des ordinateurs et des systèmes numériques.

> **Exemple :** le signal sortant d'un convertisseur analogique-numérique (CAN) : une suite de niveaux discrets.

### Conversion analogique → numérique

Un **convertisseur analogique-numérique** (CAN) transforme un signal analogique en signal numérique. Deux paramètres clés :

- La **fréquence d'échantillonnage** $f_e$ : nombre de mesures par seconde (en Hz).
- La **résolution** (nombre de bits) : précision de chaque mesure.

Pour **restituer fidèlement** un signal de fréquence maximale $f_{\\max}$, le **théorème de Shannon** impose :

$$f_e \\geq 2 f_{\\max}$$

> **Exemple :** pour un son audible ($f_{\\max} = 20\\,000$ Hz), il faut $f_e \\geq 40\\,000$ Hz. Le standard audio CD utilise $f_e = 44\\,100$ Hz.

---

## Signaux périodiques

### Définition

Un signal est **périodique** s'il se reproduit identique à lui-même à intervalles de temps réguliers. La durée d'un motif élémentaire est la **période** $T$ (en secondes).

### Fréquence

La **fréquence** $f$ est le nombre de motifs (périodes) par seconde :

$$f = \\frac{1}{T}$$

- $f$ en hertz (Hz)
- $T$ en secondes (s)

> **Exemple :** un signal de période $T = 0{,}02$ s a une fréquence $f = \\frac{1}{0{,}02} = 50$ Hz. C'est la fréquence du courant secteur en France.

### Tension maximale et tension efficace

Pour un signal sinusoïdal de tension :

$$u(t) = U_{\\max} \\sin(2\\pi f t)$$

- $U_{\\max}$ : **tension maximale** (amplitude)
- $U_{\\text{eff}}$ : **tension efficace**, liée à $U_{\\max}$ par :

$$U_{\\text{eff}} = \\frac{U_{\\max}}{\\sqrt{2}}$$

> **Exemple :** le secteur en France : $U_{\\text{eff}} = 230$ V → $U_{\\max} = 230 \\times \\sqrt{2} \\approx 325$ V.

---

## Sécurité électrique

### Dangers du courant électrique

Le passage du courant dans le corps humain peut provoquer :

| Intensité | Effet sur le corps |
|---|---|
| 0,5 mA | Seuil de perception (picotement) |
| 10 mA | Contraction musculaire (impossibilité de lâcher) |
| 30 mA | Fibrillation ventriculaire possible (danger mortel) |
| 1 A | Brûlures graves, arrêt cardiaque |

### Dispositifs de protection

- **Disjoncteur différentiel** (30 mA) : coupe le circuit si un courant de fuite est détecté (protection des personnes).
- **Fusible** et **disjoncteur magnétothermique** : protègent les installations contre les surintensités.
- **Prise de terre** : évacue les courants de fuite vers le sol.

### Règles de sécurité

- Ne jamais manipuler un appareil électrique avec les mains mouillées.
- Ne pas surcharger les multiprises.
- Vérifier l'état des câbles et prises.
- En cas d'accident électrique : couper le courant **avant** de toucher la victime.

---

## À retenir

- Un **capteur** convertit une grandeur physique en signal électrique.
- **Thermistance CTN** : $R$ diminue quand $T$ augmente. **Photorésistance LDR** : $R$ diminue quand la lumière augmente.
- L'**étalonnage** établit la relation mesurande ↔ grandeur électrique de sortie.
- Signal **analogique** : continu ; signal **numérique** : discret (0/1). Conversion par un CAN.
- **Théorème de Shannon** : $f_e \\geq 2 f_{\\max}$ pour restituer fidèlement un signal.
- Signal **périodique** : période $T$, fréquence $f = \\frac{1}{T}$.
- Tension efficace : $U_{\\text{eff}} = \\frac{U_{\\max}}{\\sqrt{2}}$.
- **Sécurité** : le courant est dangereux dès 30 mA ; disjoncteur différentiel = protection des personnes.
""",
                'quiz': {
                    'titre': "Quiz — Capteurs électriques et signaux",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Qu'est-ce qu'un capteur ?",
                            'options': ["Un dispositif qui convertit une grandeur physique en signal électrique", "Un générateur de courant alternatif", "Un appareil qui amplifie un signal", "Un composant qui stocke l'énergie électrique"],
                            'reponse_correcte': '0',
                            'explication': "Un capteur transforme une grandeur physique (mesurande) en une grandeur électrique mesurable.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Comment varie la résistance d'une thermistance CTN quand la température augmente ?",
                            'options': ["Elle diminue", "Elle augmente", "Elle reste constante", "Elle oscille"],
                            'reponse_correcte': '0',
                            'explication': "CTN = Coefficient de Température Négatif : la résistance diminue quand la température augmente.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Que signifie le sigle LDR ?",
                            'options': ["Light Dependent Resistor", "Low Density Resistor", "Linear Digital Receptor", "Laser Detection Range"],
                            'reponse_correcte': '0',
                            'explication': "LDR signifie Light Dependent Resistor (résistance dépendante de la lumière), c'est-à-dire une photorésistance.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Comment varie la résistance d'une photorésistance (LDR) quand l'éclairement augmente ?",
                            'options': ["Elle diminue", "Elle augmente", "Elle reste constante", "Elle s'annule"],
                            'reponse_correcte': '0',
                            'explication': "La résistance d'une LDR diminue lorsque l'éclairement lumineux augmente.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Quelle est la différence principale entre un signal analogique et un signal numérique ?",
                            'options': ["Le signal analogique varie de façon continue, le numérique ne prend que des valeurs discrètes", "Le signal analogique est toujours périodique, pas le numérique", "Le signal numérique est plus puissant", "Il n'y a aucune différence fondamentale"],
                            'reponse_correcte': '0',
                            'explication': "Un signal analogique peut prendre une infinité de valeurs (continu), tandis qu'un signal numérique ne prend qu'un nombre fini de valeurs discrètes.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quel composant réalise la conversion d'un signal analogique en signal numérique ?",
                            'options': ["Un convertisseur analogique-numérique (CAN)", "Un amplificateur opérationnel", "Un transformateur", "Une diode"],
                            'reponse_correcte': '0',
                            'explication': "Le CAN (convertisseur analogique-numérique) échantillonne le signal analogique et le convertit en valeurs discrètes.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Quelle est la relation entre la période $T$ et la fréquence $f$ d'un signal périodique ?",
                            'options': ["$f = 1/T$", "$f = T$", "$f = 2\\pi T$", "$f = T^2$"],
                            'reponse_correcte': '0',
                            'explication': "La fréquence est l'inverse de la période : $f = 1/T$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Quel est le rôle d'un disjoncteur différentiel 30 mA ?",
                            'options': ["Protéger les personnes contre les fuites de courant", "Protéger les appareils contre la surtension", "Réguler la tension du secteur", "Convertir le courant alternatif en courant continu"],
                            'reponse_correcte': '0',
                            'explication': "Le disjoncteur différentiel 30 mA coupe le circuit dès qu'un courant de fuite est détecté, protégeant ainsi les personnes contre l'électrocution.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "D'après le théorème de Shannon, quelle condition doit vérifier la fréquence d'échantillonnage $f_e$ pour restituer fidèlement un signal de fréquence maximale $f_{max}$ ?",
                            'options': ["$f_e \\geq 2 f_{max}$", "$f_e \\geq f_{max}$", "$f_e = f_{max}$", "$f_e \\leq f_{max} / 2$"],
                            'reponse_correcte': '0',
                            'explication': "Le théorème de Shannon impose $f_e \\geq 2 f_{max}$ pour éviter le repliement du signal.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Un signal périodique a une période de 0,02 s. Quelle est sa fréquence ?",
                            'options': ["50 Hz", "20 Hz", "0,02 Hz", "500 Hz"],
                            'reponse_correcte': '0',
                            'explication': "$f = 1/T = 1/0{,}02 = 50$ Hz. C'est la fréquence du courant secteur en France.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "La tension maximale du secteur français est d'environ 325 V. Quelle est la tension efficace correspondante ?",
                            'options': ["230 V", "325 V", "163 V", "460 V"],
                            'reponse_correcte': '0',
                            'explication': "$U_{eff} = U_{max} / \\sqrt{2} = 325 / 1{,}414 \\approx 230$ V.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Qu'est-ce que l'étalonnage d'un capteur ?",
                            'options': ["Établir la relation entre le mesurande et la grandeur électrique de sortie", "Régler la sensibilité du capteur au maximum", "Remplacer le capteur par un capteur de référence", "Mesurer la résistance interne du capteur"],
                            'reponse_correcte': '0',
                            'explication': "Étalonner un capteur consiste à établir la correspondance entre les valeurs du mesurande et les valeurs de la grandeur électrique de sortie.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Pour numériser un signal sonore dont la fréquence maximale est 20 kHz, quelle fréquence d'échantillonnage minimale faut-il utiliser ?",
                            'options': ["40 kHz", "20 kHz", "10 kHz", "80 kHz"],
                            'reponse_correcte': '0',
                            'explication': "D'après Shannon : $f_e \\geq 2 \\times 20\\,000 = 40\\,000$ Hz = 40 kHz.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Dans un montage diviseur de tension avec une CTN et une résistance fixe $R_0$, que se passe-t-il quand la température augmente ?",
                            'options': ["La tension aux bornes de la CTN diminue", "La tension aux bornes de la CTN augmente", "La tension aux bornes de la CTN reste constante", "Le courant dans le circuit s'annule"],
                            'reponse_correcte': '0',
                            'explication': "Quand $T$ augmente, $R_{CTN}$ diminue, donc $U_{CTN} = E \\times R_{CTN}/(R_{CTN} + R_0)$ diminue aussi.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'qcm',
                            'texte': "À partir de quelle intensité le courant électrique traversant le corps humain peut provoquer une fibrillation ventriculaire ?",
                            'options': ["30 mA", "0,5 mA", "10 A", "500 mA"],
                            'reponse_correcte': '0',
                            'explication': "Dès 30 mA, le courant peut provoquer une fibrillation ventriculaire potentiellement mortelle.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'qcm',
                            'texte': "La fréquence d'échantillonnage du format CD audio est de 44 100 Hz. D'après Shannon, quelle est la fréquence maximale du son restitué fidèlement ?",
                            'options': ["22 050 Hz", "44 100 Hz", "88 200 Hz", "11 025 Hz"],
                            'reponse_correcte': '0',
                            'explication': "$f_{max} = f_e / 2 = 44\\,100 / 2 = 22\\,050$ Hz, ce qui couvre le domaine audible.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Une thermistance CTN a une caractéristique $R(T)$ linéaire.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La caractéristique $R(T)$ d'une CTN est non linéaire : la résistance chute rapidement au début puis plus lentement.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'vrai_faux',
                            'texte': "Un signal numérique ne peut prendre qu'un nombre fini de valeurs.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Par définition, un signal numérique est discret et ne prend qu'un nombre fini de valeurs (souvent codées en binaire).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Quel type de capteur voit sa résistance diminuer quand la lumière augmente ? (un mot composé)",
                            'options': None,
                            'reponse_correcte': 'photorésistance',
                            'tolerances': ['photoresistance', 'LDR', 'ldr', 'photo-résistance', 'une photorésistance'],
                            'explication': "La photorésistance (ou LDR) est un capteur dont la résistance diminue avec l'éclairement.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quelle est la relation entre la tension efficace $U_{eff}$ et la tension maximale $U_{max}$ d'un signal sinusoïdal ? (écrire sous la forme Ueff = ...)",
                            'options': None,
                            'reponse_correcte': 'Ueff = Umax / √2',
                            'tolerances': ['Ueff = Umax/√2', 'Ueff = Umax / racine(2)', 'Ueff=Umax/racine(2)', 'Ueff = Umax/racine de 2', 'Ueff = Umax / sqrt(2)', 'Ueff=Umax/sqrt(2)'],
                            'explication': "Pour un signal sinusoïdal, $U_{eff} = U_{max} / \\sqrt{2}$.",
                            'difficulte': 'difficile',
                            'points': 1,
                        },
                    ],
                },
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Seed Physique Seconde — 7 chapitres, leçons uniquement (sans quiz)."

    def handle(self, *args, **options):
        matiere, created = Matiere.objects.get_or_create(
            nom='physique',
            defaults={
                'description': "La physique au lycée : mécanique, ondes, optique et électricité.",
            },
        )
        if created:
            self.stdout.write(f"  ✔ Matière « {matiere} » créée")
        else:
            self.stdout.write(f"  … Matière « {matiere} » existante")

        total_lecons = 0
        total_quizzes = 0

        for chap_data in CHAPITRES:
            chapitre, ch_created = Chapitre.objects.get_or_create(
                matiere=matiere,
                niveau='seconde',
                ordre=chap_data['ordre'],
                defaults={
                    'titre': chap_data['titre'],
                    'description': chap_data['description'],
                    'score_minimum_deblocage': chap_data['score_minimum'],
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
            f"\n✅ Physique Seconde — {len(CHAPITRES)} chapitres, {total_lecons} leçons, {total_quizzes} quiz traités."
        ))
