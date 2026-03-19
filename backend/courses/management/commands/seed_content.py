"""
Contenu pédagogique initial pour ScienceLycée.
Physique, Chimie, Mathématiques — Seconde, Première, Terminale.
"""

SEED_DATA = {

    # ================================================================== #
    #  PHYSIQUE                                                            #
    # ================================================================== #
    "physique": {
        "description": "Explorez les lois fondamentales qui régissent l'univers : mécanique, optique, électricité, ondes et bien plus.",
        "niveaux": {
            "seconde": [
                {
                    "ordre": 1,
                    "titre": "Les forces et les interactions",
                    "description": "Découvrez les différents types de forces et comment elles agissent sur les objets.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Les différentes forces",
                            "duree": 20,
                            "contenu": """# Les différentes forces

## Qu'est-ce qu'une force ?

Une **force** est une action mécanique qu'un corps exerce sur un autre corps. Elle peut :
- Modifier le mouvement d'un objet (l'accélérer, le freiner, le dévier)
- Déformer un objet

Une force est une **grandeur vectorielle** : elle possède une valeur (module), une direction, un sens et un point d'application.

## Les types de forces

### Le poids

Le poids est la force d'attraction exercée par la Terre sur un objet de masse $m$.

$$\\vec{P} = m \\cdot \\vec{g}$$

Avec :
- $m$ : masse en kilogrammes (kg)
- $\\vec{g}$ : champ de pesanteur terrestre ≈ $9{,}8 \\text{ N/kg}$ (dirigé vers le bas)

> **Exemple :** Un livre de masse $m = 0{,}5 \\text{ kg}$ a un poids $P = 0{,}5 \\times 9{,}8 = 4{,}9 \\text{ N}$.

### La réaction normale (réaction du support)

Quand un objet repose sur une surface, la surface exerce sur lui une force perpendiculaire à la surface appelée **réaction normale** $\\vec{R}$.

### La tension d'un fil

Un fil tendu exerce sur l'objet auquel il est accroché une force appelée **tension** $\\vec{T}$, dirigée le long du fil vers le point d'attache.

### Les forces de frottement

Les surfaces en contact exercent des forces de frottement **qui s'opposent au mouvement** relatif. Dans les problèmes de lycée, on les néglige souvent (contact sans frottement).

### La poussée d'Archimède

Tout objet placé dans un fluide (liquide ou gaz) est soumis à une force verticale orientée **vers le haut**, la poussée d'Archimède :

$$F_A = \\rho_{\\text{fluide}} \\times g \\times V_{\\text{objet immergé}}$$

## Représenter une force

On représente une force par une **flèche** (vecteur) :
1. Le point d'application est le point de l'objet où s'applique la force.
2. La direction et le sens indiquent où la force pousse/tire.
3. La longueur est proportionnelle à l'intensité (module) de la force.

## Additionner des forces

La **résultante** (somme vectorielle) de plusieurs forces est la force unique qui produit le même effet :

$$\\vec{F}_{\\text{résultante}} = \\vec{F}_1 + \\vec{F}_2 + \\cdots$$

Si deux forces sont colinéaires et de même sens, on additionne les modules.
Si elles sont colinéaires et de sens contraire, on soustrait les modules.
""",
                            "quiz": {
                                "titre": "Quiz — Les différentes forces",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Un objet de masse 2 kg est soumis à la pesanteur terrestre (g = 9,8 N/kg). Quel est son poids ?",
                                        "options": ["2 N", "9,8 N", "19,6 N", "4,9 N"],
                                        "reponse_correcte": "2",
                                        "explication": "P = m × g = 2 × 9,8 = 19,6 N. La réponse correcte est 19,6 N (index 2).",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La réaction normale exercée par le sol sur un objet est toujours perpendiculaire à la surface de contact.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "Par définition, la réaction normale est perpendiculaire à la surface de contact.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Dans quel sens est dirigée la poussée d'Archimède ?",
                                        "options": ["Vers le bas", "Vers le haut", "Horizontalement", "Dans la direction du mouvement"],
                                        "reponse_correcte": "1",
                                        "explication": "La poussée d'Archimède est toujours dirigée verticalement vers le haut.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 4,
                                        "type": "qcm",
                                        "texte": "Qu'est-ce qu'une grandeur vectorielle ?",
                                        "options": [
                                            "Une grandeur qui possède uniquement un module",
                                            "Une grandeur qui possède un module, une direction et un sens",
                                            "Une grandeur sans unité",
                                            "Une grandeur toujours positive",
                                        ],
                                        "reponse_correcte": "1",
                                        "explication": "Un vecteur est défini par son module (intensité), sa direction et son sens.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Les lois de Newton",
                            "duree": 25,
                            "contenu": """# Les lois de Newton

## La première loi de Newton (principe d'inertie)

> **« Tout corps persévère dans son état de repos ou de mouvement rectiligne uniforme si aucune force extérieure ne s'exerce sur lui, ou si la résultante des forces est nulle. »**

En d'autres termes : si $\\sum \\vec{F} = \\vec{0}$, alors l'objet est soit **au repos**, soit en **mouvement rectiligne uniforme** (vitesse constante).

## La deuxième loi de Newton (principe fondamental de la dynamique)

$$\\sum \\vec{F} = m \\cdot \\vec{a}$$

Avec :
- $\\sum \\vec{F}$ : résultante des forces en **Newtons (N)**
- $m$ : masse de l'objet en **kilogrammes (kg)**
- $\\vec{a}$ : accélération en **m/s²**

Cette loi montre que plus la masse est grande, plus il faut de force pour accélérer un objet.

### Exemple de calcul

Un véhicule de masse $m = 1000 \\text{ kg}$ est soumis à une force nette de $F = 3000 \\text{ N}$. Son accélération vaut :

$$a = \\frac{F}{m} = \\frac{3000}{1000} = 3 \\text{ m/s}^2$$

## La troisième loi de Newton (principe des actions réciproques)

> **« Si un corps A exerce une force sur un corps B, alors B exerce sur A une force opposée (même direction, même module, sens contraire). »**

$$\\vec{F}_{A \\to B} = -\\vec{F}_{B \\to A}$$

Ces deux forces s'appliquent sur **deux corps différents** et ne se compensent donc pas.

## Application : objet en équilibre

Un objet est en **équilibre statique** lorsque la somme vectorielle de toutes les forces qui s'exercent sur lui est nulle :

$$\\sum \\vec{F} = \\vec{0}$$

**Exemple :** Un livre posé sur une table est soumis à son poids $\\vec{P}$ (vers le bas) et à la réaction normale $\\vec{R}$ (vers le haut). L'équilibre implique $\\vec{P} + \\vec{R} = \\vec{0}$, donc $R = P$.
""",
                            "quiz": {
                                "titre": "Quiz — Les lois de Newton",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Une voiture de 800 kg accélère de 2 m/s². Quelle est la force nette appliquée ?",
                                        "options": ["400 N", "800 N", "1 600 N", "3 200 N"],
                                        "reponse_correcte": "2",
                                        "explication": "F = m × a = 800 × 2 = 1 600 N.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Selon la 3e loi de Newton, les deux forces d'une paire action-réaction s'exercent sur le même corps.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "Les forces action-réaction s'exercent sur deux corps DIFFÉRENTS.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Un objet se déplace en ligne droite à vitesse constante. Qu'est-ce que cela signifie ?",
                                        "options": [
                                            "Aucune force ne s'exerce sur lui",
                                            "La résultante des forces est nulle",
                                            "Il est en chute libre",
                                            "Une seule force s'exerce sur lui",
                                        ],
                                        "reponse_correcte": "1",
                                        "explication": "D'après la 1ère loi de Newton, si la résultante est nulle, l'objet garde son état de mouvement rectiligne uniforme.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                {
                    "ordre": 2,
                    "titre": "L'électricité",
                    "description": "Comprendre les circuits électriques, les lois fondamentales et les composants.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Les circuits électriques",
                            "duree": 20,
                            "contenu": """# Les circuits électriques

## Qu'est-ce qu'un circuit électrique ?

Un **circuit électrique** est un ensemble de composants reliés par des conducteurs qui forment un chemin fermé permettant la circulation du courant électrique.

## Le courant électrique

Le courant électrique est un **déplacement ordonné de porteurs de charges** (généralement des électrons dans un métal).

- **Convention** : le courant conventionnel va du + vers le − à l'extérieur du générateur.
- **Réalité** : les électrons se déplacent en sens inverse (du − vers le +).
- **Unité** : l'Ampère (A), mesuré avec un **ampèremètre**.

## La tension électrique

La tension (ou différence de potentiel) $U$ est mesurée en **Volts (V)** avec un **voltmètre** branché en parallèle.

$$U_{AB} = V_A - V_B$$

## Dipôles en série et en parallèle

### En série
- Le courant est le même dans tous les composants : $I_1 = I_2 = I$
- Les tensions s'additionnent : $U = U_1 + U_2$

### En parallèle
- La tension est la même aux bornes de chaque branche : $U_1 = U_2 = U$
- Les courants s'additionnent : $I = I_1 + I_2$

## Les lois de Kirchhoff

**Loi des nœuds** : la somme des courants entrant en un nœud est égale à la somme des courants sortant.

$$\\sum I_{\\text{entrants}} = \\sum I_{\\text{sortants}}$$

**Loi des mailles** : la somme algébrique des tensions le long d'une maille fermée est nulle.

$$\\sum U_k = 0$$
""",
                            "quiz": {
                                "titre": "Quiz — Circuits électriques",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Dans un circuit en série, comment est le courant dans chaque dipôle ?",
                                        "options": ["Différent pour chaque dipôle", "Le même dans tous les dipôles", "Nul", "Proportionnel à la résistance"],
                                        "reponse_correcte": "1",
                                        "explication": "Dans un circuit série, le courant est identique dans tous les composants.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Comment mesure-t-on la tension électrique ?",
                                        "options": ["Avec un ampèremètre en série", "Avec un voltmètre en parallèle", "Avec un ohmmètre en série", "Avec un voltmètre en série"],
                                        "reponse_correcte": "1",
                                        "explication": "La tension se mesure avec un voltmètre branché en parallèle aux bornes du dipôle.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Dans un circuit en parallèle, la tension est la même aux bornes de chaque branche.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "C'est la propriété fondamentale des dipôles en parallèle.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "La loi d'Ohm",
                            "duree": 15,
                            "contenu": """# La loi d'Ohm

## Énoncé de la loi d'Ohm

Pour un conducteur ohmique (résistance), la tension $U$ à ses bornes est proportionnelle au courant $I$ qui le traverse :

$$U = R \\cdot I$$

Avec :
- $U$ : tension en **Volts (V)**
- $R$ : résistance en **Ohms (Ω)**
- $I$ : intensité du courant en **Ampères (A)**

## La résistance

La **résistance** est une propriété d'un conducteur qui s'oppose au passage du courant. Elle dépend de :
- La nature du matériau (résistivité $\\rho$)
- Les dimensions du conducteur (longueur $L$, section $S$)

$$R = \\rho \\cdot \\frac{L}{S}$$

## Association de résistances

### En série
$$R_{\\text{éq}} = R_1 + R_2 + \\cdots + R_n$$

### En parallèle
$$\\frac{1}{R_{\\text{éq}}} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\cdots + \\frac{1}{R_n}$$

## La puissance électrique

La puissance dissipée par une résistance est :

$$P = U \\cdot I = R \\cdot I^2 = \\frac{U^2}{R}$$

Unité : **Watt (W)**

## Exemple résolu

Une résistance de $R = 100 \\text{ Ω}$ est parcourue par un courant de $I = 0{,}5 \\text{ A}$.

- Tension : $U = R \\times I = 100 \\times 0{,}5 = 50 \\text{ V}$
- Puissance : $P = U \\times I = 50 \\times 0{,}5 = 25 \\text{ W}$
""",
                            "quiz": {
                                "titre": "Quiz — Loi d'Ohm",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Une résistance de 47 Ω est soumise à une tension de 9,4 V. Quelle est l'intensité du courant ?",
                                        "options": ["0,1 A", "0,2 A", "0,5 A", "2 A"],
                                        "reponse_correcte": "1",
                                        "explication": "I = U / R = 9,4 / 47 = 0,2 A.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Deux résistances R₁ = 20 Ω et R₂ = 30 Ω sont en série. Quelle est la résistance équivalente ?",
                                        "options": ["10 Ω", "12 Ω", "50 Ω", "600 Ω"],
                                        "reponse_correcte": "2",
                                        "explication": "En série : Réq = R₁ + R₂ = 20 + 30 = 50 Ω.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
            ],
            "premiere": [
                {
                    "ordre": 1,
                    "titre": "Mécanique : cinématique et dynamique",
                    "description": "Description du mouvement et effets des forces dans le référentiel terrestre.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Description du mouvement",
                            "duree": 20,
                            "contenu": """# Description du mouvement

## Repère et référentiel

Pour décrire un mouvement, on a besoin d'un **référentiel** (solide de référence) et d'un **repère** (système de coordonnées).

- **Référentiel terrestre** : la Terre est considérée comme fixe — valable pour la plupart des expériences de laboratoire.
- **Référentiel géocentrique** : le centre de la Terre est fixe — pour les satellites.
- **Référentiel héliocentrique** (de Copernic) : le Soleil est fixe — pour les planètes.

## Position, vitesse et accélération

### Position

La position d'un point M est repérée par ses coordonnées $(x, y)$ à l'instant $t$.

### Vitesse instantanée

$$\\vec{v}(t) = \\frac{d\\vec{OM}}{dt}$$

En coordonnées : $v_x = \\frac{dx}{dt}$

**Unité :** m/s (ou km/h)

### Accélération instantanée

$$\\vec{a}(t) = \\frac{d\\vec{v}}{dt}$$

**Unité :** m/s²

## Types de mouvements

| Type | Vitesse | Accélération |
|------|---------|--------------|
| Rectiligne uniforme | Constante | Nulle |
| Rectiligne accéléré | Croissante | Constante > 0 |
| Rectiligne décéléré | Décroissante | Constante < 0 |
| Circulaire uniforme | Module constant | Centripète |

## Équations du mouvement uniformément varié (MUV)

$$v(t) = v_0 + a \\cdot t$$

$$x(t) = x_0 + v_0 \\cdot t + \\frac{1}{2} a \\cdot t^2$$

$$v^2 = v_0^2 + 2a(x - x_0)$$
""",
                            "quiz": {
                                "titre": "Quiz — Description du mouvement",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Un objet part du repos (v₀ = 0) avec une accélération de 3 m/s². Quelle est sa vitesse après 5 s ?",
                                        "options": ["3 m/s", "8 m/s", "15 m/s", "45 m/s"],
                                        "reponse_correcte": "2",
                                        "explication": "v = v₀ + a·t = 0 + 3 × 5 = 15 m/s.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Pour un mouvement circulaire uniforme, le vecteur vitesse est constant.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "Le module est constant mais la direction change : le vecteur vitesse n'est pas constant.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
            ],
            "terminale": [
                {
                    "ordre": 1,
                    "titre": "Mécanique : loi de la gravitation universelle",
                    "description": "La gravitation newtonienne et le mouvement des planètes.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Loi de la gravitation universelle",
                            "duree": 25,
                            "contenu": """# Loi de la gravitation universelle

## Énoncé de Newton

Deux corps ponctuels de masses $m_1$ et $m_2$, séparés d'une distance $r$, s'attirent mutuellement avec une force :

$$F = G \\cdot \\frac{m_1 \\cdot m_2}{r^2}$$

Avec :
- $G = 6{,}674 \\times 10^{-11} \\text{ N·m}^2\\text{·kg}^{-2}$ : constante gravitationnelle universelle
- $r$ : distance entre les centres de masse (en m)
- $F$ : force gravitationnelle (en N)

La force est **attractive** et suit la 3e loi de Newton (action-réaction).

## Champ de gravitation

Le champ de gravitation créé par une masse $M$ à la distance $r$ :

$$g = G \\cdot \\frac{M}{r^2}$$

Au voisinage de la Terre : $g_0 \\approx 9{,}81 \\text{ m/s}^2$

## Mouvement des satellites

Pour un satellite en orbite circulaire de rayon $r$, la force gravitationnelle fournit la force centripète :

$$G \\cdot \\frac{M \\cdot m}{r^2} = m \\cdot \\frac{v^2}{r}$$

Vitesse orbitale : $v = \\sqrt{\\frac{GM}{r}}$

Période orbitale : $T = 2\\pi \\sqrt{\\frac{r^3}{GM}}$

## 3e loi de Kepler

$$\\frac{T^2}{r^3} = \\frac{4\\pi^2}{GM} = \\text{constante}$$

Cette relation est vérifiée pour tous les corps en orbite autour du même astre.
""",
                            "quiz": {
                                "titre": "Quiz — Gravitation universelle",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Que se passe-t-il à la force gravitationnelle si la distance entre deux masses est doublée ?",
                                        "options": ["Elle double", "Elle est divisée par 2", "Elle est divisée par 4", "Elle est multipliée par 4"],
                                        "reponse_correcte": "2",
                                        "explication": "F ∝ 1/r². Si r double, F est divisée par 4.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La constante G (constante gravitationnelle) est la même partout dans l'univers.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "G est une constante fondamentale universelle.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
            ],
        },
    },

    # ================================================================== #
    #  CHIMIE                                                              #
    # ================================================================== #
    "chimie": {
        "description": "De la structure de l'atome aux réactions chimiques, en passant par les solutions et la chimie organique.",
        "niveaux": {
            "seconde": [
                {
                    "ordre": 1,
                    "titre": "L'atome et les ions",
                    "description": "Structure atomique, tableau périodique et formation des ions.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Structure de l'atome",
                            "duree": 20,
                            "contenu": """# Structure de l'atome

## Le modèle de l'atome

Un atome est constitué de deux parties principales :

### Le noyau (au centre)
- Très petit (rayon ≈ $10^{-15}$ m) mais très dense
- Contient les **protons** (charge +1, masse = 1 u) et les **neutrons** (charge 0, masse = 1 u)
- **Numéro atomique Z** = nombre de protons
- **Nombre de masse A** = nombre de protons + nombre de neutrons

On note un atome : $^A_Z X$

### Le cortège électronique (autour du noyau)
- Contient les **électrons** (charge −1, masse ≈ 0)
- Orbitales organisées en **couches** (K, L, M, ...)
- Un atome neutre a autant d'électrons que de protons : $n_{e^-} = Z$

## Configuration électronique

Les électrons se répartissent sur les couches selon les règles de remplissage :
- Couche K : 2 électrons max
- Couche L : 8 électrons max
- Couche M : 18 électrons max (simplification : 8 en lycée)

**Exemple :** L'atome de sodium $^{23}_{11}\\text{Na}$ a Z = 11.
Configuration : K(2) L(8) M(1) → les électrons de valence sont sur la couche M.

## Le tableau périodique

Les éléments sont classés par **numéro atomique Z croissant**.
- Les **colonnes** (groupes) regroupent les éléments ayant les mêmes propriétés chimiques (même nombre d'électrons de valence).
- Les **lignes** (périodes) correspondent à une même couche de valence.

## Les isotopes

Des atomes du même élément (même Z) mais avec un nombre de neutrons différent (donc A différent) sont des **isotopes**.

Exemple : $^{12}_6\\text{C}$ et $^{14}_6\\text{C}$ sont deux isotopes du carbone.
""",
                            "quiz": {
                                "titre": "Quiz — Structure de l'atome",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Un atome d'oxygène a Z = 8. Combien d'électrons possède-t-il en état neutre ?",
                                        "options": ["6", "7", "8", "16"],
                                        "reponse_correcte": "2",
                                        "explication": "Un atome neutre a autant d'électrons que de protons : n(e⁻) = Z = 8.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Quelle est la charge d'un proton ?",
                                        "options": ["-1", "0", "+1", "+2"],
                                        "reponse_correcte": "2",
                                        "explication": "Un proton a une charge de +1 (charge élémentaire positive).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Deux isotopes d'un même élément ont le même nombre de protons.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "Les isotopes ont le même Z (même nombre de protons) mais des nombres de neutrons différents.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Les ions",
                            "duree": 15,
                            "contenu": """# Les ions

## Définition

Un **ion** est un atome ou un groupe d'atomes qui a gagné ou perdu des électrons, acquérant ainsi une charge électrique.

- **Cation** : perte d'électrons → charge **positive** (+)
- **Anion** : gain d'électrons → charge **négative** (−)

## Formation des ions

### Cation
Un atome perd $n$ électrons :

$$\\text{Na} \\rightarrow \\text{Na}^+ + e^-$$

$^{23}_{11}\\text{Na}$ (11 protons, 11 électrons) → $\\text{Na}^+$ (11 protons, **10** électrons)

### Anion
Un atome gagne $n$ électrons :

$$\\text{Cl} + e^- \\rightarrow \\text{Cl}^-$$

$^{35}_{17}\\text{Cl}$ (17 protons, 17 électrons) → $\\text{Cl}^-$ (17 protons, **18** électrons)

## Ions polyatomiques courants

| Ion | Formule | Charge |
|-----|---------|--------|
| Ion hydroxyde | $\\text{OH}^-$ | −1 |
| Ion sulfate | $\\text{SO}_4^{2-}$ | −2 |
| Ion nitrate | $\\text{NO}_3^-$ | −1 |
| Ion ammonium | $\\text{NH}_4^+$ | +1 |
| Ion carbonate | $\\text{CO}_3^{2-}$ | −2 |

## Règle de l'octet

Les atomes ont tendance à gagner ou perdre des électrons pour acquérir la **configuration électronique du gaz noble** le plus proche (8 électrons sur la couche externe, ou 2 pour l'hélium).

Exemples :
- Na (Z=11) : K(2)L(8)M(1) → perd 1e⁻ → Na⁺ comme le Néon
- Cl (Z=17) : K(2)L(8)M(7) → gagne 1e⁻ → Cl⁻ comme l'Argon
""",
                            "quiz": {
                                "titre": "Quiz — Les ions",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Un ion Ca²⁺ a Z = 20. Combien d'électrons possède-t-il ?",
                                        "options": ["18", "20", "22", "40"],
                                        "reponse_correcte": "0",
                                        "explication": "Ca²⁺ a perdu 2 électrons : n(e⁻) = 20 - 2 = 18.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Quelle est la formule de l'ion sulfate ?",
                                        "options": ["SO₄²⁺", "SO₄²⁻", "SO₃²⁻", "S²⁻"],
                                        "reponse_correcte": "1",
                                        "explication": "L'ion sulfate est SO₄²⁻ (charge 2−).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Un anion est un ion chargé positivement.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "Un anion est un ion de charge NÉGATIVE (il a gagné des électrons).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
            ],
            "premiere": [
                {
                    "ordre": 1,
                    "titre": "Les réactions acide-base",
                    "description": "Comprendre les transferts de proton et le pH des solutions.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Acides, bases et pH",
                            "duree": 25,
                            "contenu": """# Acides, bases et pH

## Définitions de Brønsted-Lowry

- **Acide** : espèce chimique qui peut donner (céder) un proton H⁺
- **Base** : espèce chimique qui peut accepter (capter) un proton H⁺

Réaction acide-base = **transfert de proton** entre un acide et une base.

$$\\text{AH} + \\text{B} \\rightleftharpoons \\text{A}^- + \\text{BH}^+$$

## Les couples acide/base conjugués

Chaque acide AH est associé à sa **base conjuguée** A⁻ (qui se forme après le don du proton) :

| Acide | Base conjuguée |
|-------|---------------|
| HCl | Cl⁻ |
| CH₃COOH (acide acétique) | CH₃COO⁻ (acétate) |
| H₂O | OH⁻ |
| NH₄⁺ | NH₃ |

## Le pH

Le **pH** est une grandeur sans unité qui mesure l'acidité ou la basicité d'une solution aqueuse :

$$\\text{pH} = -\\log[\\text{H}_3\\text{O}^+]$$

Avec $[\\text{H}_3\\text{O}^+]$ en mol/L.

- $\\text{pH} < 7$ : solution **acide**
- $\\text{pH} = 7$ : solution **neutre** (à 25°C)
- $\\text{pH} > 7$ : solution **basique**

## Produit ionique de l'eau

À 25°C :

$$K_e = [\\text{H}_3\\text{O}^+][\\text{OH}^-] = 10^{-14}$$

Donc : $\\text{pH} + \\text{pOH} = 14$
""",
                            "quiz": {
                                "titre": "Quiz — Acides, bases et pH",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Une solution a [H₃O⁺] = 10⁻³ mol/L. Quel est son pH ?",
                                        "options": ["1", "3", "7", "11"],
                                        "reponse_correcte": "1",
                                        "explication": "pH = -log[H₃O⁺] = -log(10⁻³) = 3.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Quelle est la base conjuguée de l'acide acétique CH₃COOH ?",
                                        "options": ["CH₃COO⁻", "CH₃COOH₂⁺", "CH₄", "COO²⁻"],
                                        "reponse_correcte": "0",
                                        "explication": "CH₃COOH cède H⁺ pour donner sa base conjuguée CH₃COO⁻.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
            ],
            "terminale": [
                {
                    "ordre": 1,
                    "titre": "Cinétique chimique",
                    "description": "Vitesse des réactions, facteurs cinétiques et catalyse.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Vitesse de réaction",
                            "duree": 25,
                            "contenu": """# Vitesse de réaction

## Définition

La **vitesse de réaction** quantifie l'évolution de la concentration d'un réactif ou d'un produit en fonction du temps.

$$v = -\\frac{1}{a}\\frac{d[A]}{dt} = \\frac{1}{b}\\frac{d[B]}{dt}$$

Pour la réaction $a A \\rightarrow b B$.

**Unité :** mol·L⁻¹·s⁻¹

## Facteurs influençant la vitesse

### Température
Augmenter la température **accélère** la réaction. Une hausse de 10°C double environ la vitesse.

### Concentration des réactifs
Plus les concentrations sont élevées, plus les chocs entre molécules sont fréquents → réaction plus rapide.

### État de division
Un réactif solide finement broyé réagit plus vite (plus grande surface de contact).

### Catalyseur
Un **catalyseur** augmente la vitesse d'une réaction sans être consommé. Il abaisse l'énergie d'activation.

## Demi-vie

La **demi-vie** $t_{1/2}$ est la durée nécessaire pour que la concentration d'un réactif diminue de moitié.

Pour une réaction d'ordre 1 :

$$t_{1/2} = \\frac{\\ln 2}{k} \\approx \\frac{0{,}693}{k}$$

Avec $k$ la constante de vitesse.
""",
                            "quiz": {
                                "titre": "Quiz — Vitesse de réaction",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Parmi les facteurs suivants, lequel N'accélère PAS une réaction chimique ?",
                                        "options": [
                                            "Augmenter la température",
                                            "Ajouter un catalyseur",
                                            "Diminuer la concentration des réactifs",
                                            "Broyer finement les réactifs solides",
                                        ],
                                        "reponse_correcte": "2",
                                        "explication": "Diminuer la concentration ralentit la réaction (moins de chocs moléculaires).",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Un catalyseur est consommé à la fin de la réaction.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "Par définition, un catalyseur n'est pas consommé : il se retrouve intact à la fin.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
            ],
        },
    },

    # ================================================================== #
    #  MATHÉMATIQUES                                                       #
    # ================================================================== #
    "mathematiques": {
        "description": "Du calcul algébrique à l'analyse, en passant par la géométrie et les probabilités.",
        "niveaux": {
            "seconde": [
                {
                    "ordre": 1,
                    "titre": "Fonctions — Généralités",
                    "description": "Notion de fonction, domaine de définition, variations et représentation graphique.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Introduction aux fonctions",
                            "duree": 20,
                            "contenu": """# Introduction aux fonctions

## Définition

Une **fonction** $f$ est une règle qui associe à chaque réel $x$ d'un ensemble D (domaine de définition) **un seul** réel $f(x)$ (image).

On note : $f : D \\rightarrow \\mathbb{R}$, $x \\mapsto f(x)$

## Vocabulaire

- $x$ est l'**antécédent**
- $f(x)$ est l'**image** de $x$
- L'**ensemble de définition** (ou domaine) D est l'ensemble des valeurs de $x$ pour lesquelles $f(x)$ est défini.

## Exemples courants

| Fonction | Expression | Domaine |
|----------|-----------|---------|
| Fonction carré | $f(x) = x^2$ | $\\mathbb{R}$ |
| Fonction racine carrée | $f(x) = \\sqrt{x}$ | $[0; +\\infty[$ |
| Fonction inverse | $f(x) = \\frac{1}{x}$ | $\\mathbb{R}^*$ |
| Fonction affine | $f(x) = ax + b$ | $\\mathbb{R}$ |

## Lecture graphique

Sur la courbe représentative d'une fonction :
- **Image d'un point** : à partir de $x$ sur l'axe horizontal, on lit $y = f(x)$ sur l'axe vertical
- **Antécédent** : à partir de $y$, on lit les valeurs de $x$ correspondantes

## Parité

- $f$ est **paire** si $f(-x) = f(x)$ pour tout $x$ du domaine (courbe symétrique par rapport à l'axe des ordonnées)
- $f$ est **impaire** si $f(-x) = -f(x)$ (courbe symétrique par rapport à l'origine)
""",
                            "quiz": {
                                "titre": "Quiz — Introduction aux fonctions",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Pour f(x) = √x, quel est l'ensemble de définition ?",
                                        "options": ["ℝ", "ℝ*", "[0 ; +∞[", "]0 ; +∞["],
                                        "reponse_correcte": "2",
                                        "explication": "La racine carrée est définie pour x ≥ 0, soit [0 ; +∞[.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Soit f(x) = 2x + 5. Quelle est l'image de x = 3 ?",
                                        "options": ["8", "11", "6", "15"],
                                        "reponse_correcte": "1",
                                        "explication": "f(3) = 2×3 + 5 = 6 + 5 = 11.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La fonction f(x) = x² est une fonction paire.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "f(-x) = (-x)² = x² = f(x), donc f est paire.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Variations d'une fonction",
                            "duree": 20,
                            "contenu": """# Variations d'une fonction

## Fonctions monotones

Une fonction $f$ est :
- **Croissante** sur un intervalle $I$ si : pour tous $a, b \\in I$ avec $a < b$, on a $f(a) \\leq f(b)$
- **Décroissante** sur $I$ si : pour tous $a, b \\in I$ avec $a < b$, on a $f(a) \\geq f(b)$

## Tableau de variations

Un **tableau de variation** résume graphiquement le comportement d'une fonction sur son domaine.

Exemple pour $f(x) = x^2$ :

```
x     | -∞          0          +∞
f'(x) |     -     0     +
f(x)  |  ↘       0       ↗
```

(La fonction décroît sur $]-\\infty; 0]$ et croît sur $[0; +\\infty[$)

## Extremum

- **Maximum** local : la valeur de $f$ en ce point est supérieure à toutes les valeurs voisines
- **Minimum** local : inférieure à toutes les valeurs voisines

Pour $f(x) = x^2$, le minimum est $f(0) = 0$ (en $x = 0$).

## Applications : sens de variations à retenir

| Fonction | Monotonie |
|----------|-----------|
| $f(x) = x$ | Croissante sur ℝ |
| $f(x) = x^2$ | Décroissante sur $]-\\infty; 0]$, croissante sur $[0; +\\infty[$ |
| $f(x) = \\sqrt{x}$ | Croissante sur $[0; +\\infty[$ |
| $f(x) = \\frac{1}{x}$ | Décroissante sur $]-\\infty; 0[$ et sur $]0; +\\infty[$ |

## Encadrement et comparaison par les variations

Si $f$ est **croissante** sur $[a; b]$ :

$$\\forall x \\in [a; b], \\quad f(a) \\leq f(x) \\leq f(b)$$
""",
                            "quiz": {
                                "titre": "Quiz — Variations d'une fonction",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Sur quel intervalle la fonction f(x) = x² est-elle strictement décroissante ?",
                                        "options": ["[0 ; +∞[", "]-∞ ; 0]", "ℝ", "]-∞ ; 0["],
                                        "reponse_correcte": "3",
                                        "explication": "f(x) = x² est strictement décroissante sur ]-∞ ; 0[ (décroissante en excluant 0).",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Une fonction peut avoir un maximum sans avoir de minimum sur un intervalle donné.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "Par exemple, f(x) = -x² a un maximum en 0 mais pas de minimum sur ℝ.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                {
                    "ordre": 2,
                    "titre": "Géométrie dans le plan",
                    "description": "Vecteurs, coordonnées, droites et cercles.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Les vecteurs",
                            "duree": 25,
                            "contenu": """# Les vecteurs

## Définition

Un **vecteur** $\\vec{u}$ est défini par :
- Sa **direction** (droite support)
- Son **sens**
- Son **module** (longueur, notée $|\\vec{u}|$ ou $||\\vec{u}||$)

Deux vecteurs sont **égaux** s'ils ont même direction, sens et module (même représentant à translation près).

## Coordonnées d'un vecteur

Dans un repère orthonormé $(O; \\vec{i}, \\vec{j})$, le vecteur $\\overrightarrow{AB}$ a pour coordonnées :

$$\\overrightarrow{AB} = \\begin{pmatrix} x_B - x_A \\\\ y_B - y_A \\end{pmatrix}$$

## Opérations sur les vecteurs

### Addition (règle du parallélogramme ou de Chasles)

$$\\vec{u} + \\vec{v} = \\begin{pmatrix} u_x + v_x \\\\ u_y + v_y \\end{pmatrix}$$

**Relation de Chasles :** $\\overrightarrow{AC} = \\overrightarrow{AB} + \\overrightarrow{BC}$

### Multiplication scalaire

$$k \\cdot \\vec{u} = \\begin{pmatrix} k \\cdot u_x \\\\ k \\cdot u_y \\end{pmatrix}$$

### Norme (module)

$$||\\vec{u}|| = \\sqrt{u_x^2 + u_y^2}$$

## Colinéarité

Deux vecteurs $\\vec{u}(a; b)$ et $\\vec{v}(c; d)$ sont **colinéaires** si et seulement si :

$$ad - bc = 0$$

(le déterminant est nul)

## Milieu d'un segment

Le milieu $I$ du segment $[AB]$ a pour coordonnées :

$$I = \\left(\\frac{x_A + x_B}{2}; \\frac{y_A + y_B}{2}\\right)$$
""",
                            "quiz": {
                                "titre": "Quiz — Les vecteurs",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "A(1 ; 2) et B(4 ; 6). Quelles sont les coordonnées du vecteur AB⃗ ?",
                                        "options": ["(5 ; 8)", "(3 ; 4)", "(-3 ; -4)", "(2,5 ; 4)"],
                                        "reponse_correcte": "1",
                                        "explication": "AB⃗ = (x_B - x_A ; y_B - y_A) = (4-1 ; 6-2) = (3 ; 4).",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Quelle est la norme du vecteur u⃗ = (3 ; 4) ?",
                                        "options": ["5", "7", "12", "25"],
                                        "reponse_correcte": "0",
                                        "explication": "||u⃗|| = √(3² + 4²) = √(9 + 16) = √25 = 5.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
            ],
            "premiere": [
                {
                    "ordre": 1,
                    "titre": "Dérivation",
                    "description": "La dérivée d'une fonction, règles de calcul et applications à l'étude des variations.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Définition et règles de dérivation",
                            "duree": 30,
                            "contenu": """# La dérivée d'une fonction

## Définition

Le **nombre dérivé** de $f$ en $a$ est la limite (si elle existe) du taux de variation :

$$f'(a) = \\lim_{h \\to 0} \\frac{f(a+h) - f(a)}{h}$$

Géométriquement, $f'(a)$ est la **pente de la tangente** à la courbe au point d'abscisse $a$.

## Dérivées usuelles

| Fonction | Dérivée |
|----------|---------|
| $f(x) = c$ (constante) | $f'(x) = 0$ |
| $f(x) = x^n$ | $f'(x) = n \\cdot x^{n-1}$ |
| $f(x) = \\sqrt{x}$ | $f'(x) = \\dfrac{1}{2\\sqrt{x}}$ |
| $f(x) = \\dfrac{1}{x}$ | $f'(x) = -\\dfrac{1}{x^2}$ |
| $f(x) = e^x$ | $f'(x) = e^x$ |
| $f(x) = \\ln x$ | $f'(x) = \\dfrac{1}{x}$ |

## Règles opératoires

Pour $u$ et $v$ dérivables et $k$ réel :

$$[k \\cdot u]' = k \\cdot u'$$

$$[u + v]' = u' + v'$$

$$[u \\cdot v]' = u' \\cdot v + u \\cdot v'$$

$$\\left[\\frac{u}{v}\\right]' = \\frac{u' v - u v'}{v^2} \\quad (v \\neq 0)$$

$$[u(v(x))]' = v'(x) \\cdot u'(v(x)) \\quad \\text{(dérivée d'une composée)}$$

## Applications aux variations

- Si $f'(x) > 0$ sur $I$ → $f$ est **croissante** sur $I$
- Si $f'(x) < 0$ sur $I$ → $f$ est **décroissante** sur $I$
- Si $f'(a) = 0$ et $f'$ change de signe en $a$ → **extremum local** en $a$

### Exemple

$f(x) = x^3 - 3x + 2$

$f'(x) = 3x^2 - 3 = 3(x^2 - 1) = 3(x-1)(x+1)$

- $f'(x) > 0$ pour $x < -1$ ou $x > 1$ : $f$ croissante
- $f'(x) < 0$ pour $-1 < x < 1$ : $f$ décroissante
- Maximum local en $x = -1$ : $f(-1) = 4$
- Minimum local en $x = 1$ : $f(1) = 0$
""",
                            "quiz": {
                                "titre": "Quiz — Dérivation",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quelle est la dérivée de f(x) = 3x⁴ - 2x² + 5 ?",
                                        "options": ["12x³ - 4x", "12x³ - 2x", "3x³ - 2x", "12x⁴ - 4x²"],
                                        "reponse_correcte": "0",
                                        "explication": "f'(x) = 4×3x³ - 2×2x = 12x³ - 4x.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Si f'(x) < 0 sur un intervalle I, que peut-on conclure ?",
                                        "options": [
                                            "f est croissante sur I",
                                            "f est décroissante sur I",
                                            "f est constante sur I",
                                            "f a un maximum sur I",
                                        ],
                                        "reponse_correcte": "1",
                                        "explication": "f'(x) < 0 sur I signifie que f est strictement décroissante sur I.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La dérivée de f(x) = eˣ est f'(x) = eˣ.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "La fonction exponentielle est sa propre dérivée : (eˣ)' = eˣ.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
            ],
            "terminale": [
                {
                    "ordre": 1,
                    "titre": "Suites numériques",
                    "description": "Suites arithmétiques, géométriques, limites et raisonnement par récurrence.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Suites arithmétiques et géométriques",
                            "duree": 30,
                            "contenu": """# Suites arithmétiques et géométriques

## Définitions générales

Une **suite numérique** est une fonction $u : \\mathbb{N} \\to \\mathbb{R}$. On note ses termes $u_0, u_1, u_2, \\ldots, u_n$.

## Suite arithmétique

Une suite $(u_n)$ est **arithmétique** de raison $r$ si :

$$u_{n+1} - u_n = r \\quad (\\text{raison constante})$$

**Terme général :** $u_n = u_0 + n \\cdot r$ (ou $u_n = u_p + (n-p) \\cdot r$)

**Somme des termes :**

$$S_n = u_0 + u_1 + \\cdots + u_n = \\frac{(n+1)(u_0 + u_n)}{2}$$

### Exemple

La suite $3, 7, 11, 15, \\ldots$ est arithmétique de raison $r = 4$.

$u_n = 3 + 4n$

## Suite géométrique

Une suite $(u_n)$ est **géométrique** de raison $q$ ($q \\neq 0$) si :

$$\\frac{u_{n+1}}{u_n} = q \\quad (\\text{rapport constant})$$

**Terme général :** $u_n = u_0 \\times q^n$

**Somme des termes (si $q \\neq 1$) :**

$$S_n = u_0 \\times \\frac{1 - q^{n+1}}{1 - q}$$

### Exemple

La suite $2, 6, 18, 54, \\ldots$ est géométrique de raison $q = 3$.

$u_n = 2 \\times 3^n$

## Convergence

- Suite arithmétique avec $r > 0$ → **diverge vers $+\\infty$**
- Suite arithmétique avec $r < 0$ → **diverge vers $-\\infty$**
- Suite géométrique avec $|q| < 1$ → **converge vers 0**
- Suite géométrique avec $|q| > 1$ → **diverge vers $+\\infty$ ou $-\\infty$**
- Suite géométrique avec $q = 1$ → constante
""",
                            "quiz": {
                                "titre": "Quiz — Suites arithmétiques et géométriques",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Une suite arithmétique a u₀ = 5 et raison r = 3. Quel est u₁₀ ?",
                                        "options": ["30", "35", "38", "50"],
                                        "reponse_correcte": "1",
                                        "explication": "u₁₀ = u₀ + 10r = 5 + 10×3 = 5 + 30 = 35.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Une suite géométrique a u₀ = 4 et q = 2. Quel est u₃ ?",
                                        "options": ["10", "14", "32", "64"],
                                        "reponse_correcte": "2",
                                        "explication": "u₃ = u₀ × q³ = 4 × 8 = 32.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Une suite géométrique de raison q = 0,5 converge vers 0.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "|q| = 0,5 < 1, donc u_n = u₀ × 0.5ⁿ → 0.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
            ],
        },
    },
}
