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
                # ── Ch.1 : Ondes et matière ──────────────────────────
                {
                    "ordre": 1,
                    "titre": "Ondes et matière",
                    "description": "Ondes mécaniques et électromagnétiques, diffraction, interférences et effet Doppler.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Ondes, particules et caractéristiques",
                            "duree": 35,
                            "contenu": r"""# Ondes et particules

## Rayonnements et particules

L'Univers est empli d'émetteurs électromagnétiques sur tout le spectre. Les photons, les particules élémentaires (électrons, protons, neutrinos) et les ondes mécaniques sont des supports d'information.

### Spectre électromagnétique

| Domaine | Longueur d'onde |
|---|---|
| Rayons $\gamma$ | $< 0{,}001$ nm |
| Rayons X | $0{,}001$ – $10$ nm |
| UV | $10$ – $400$ nm |
| Visible | $400$ – $800$ nm |
| IR | $800$ nm – $1$ mm |
| Micro-ondes | $1$ mm – $1$ m |
| Ondes hertziennes | $> 1$ m |

## Caractéristiques d'une onde

- **Période** $T$ (en s) et **fréquence** $\nu = \frac{1}{T}$ (en Hz).
- **Longueur d'onde** : $\lambda = c \cdot T = \frac{c}{\nu}$ avec $c = 3{,}00 \times 10^8$ m·s⁻¹.
- **Célérité** : vitesse de propagation de l'onde dans le milieu.

### Ondes mécaniques vs électromagnétiques

| | Mécanique | Électromagnétique |
|---|---|---|
| Milieu matériel | **Nécessaire** | Non nécessaire |
| Exemple | Son ($v \approx 340$ m·s⁻¹) | Lumière ($c$) |

## Loi de Wien

$$\lambda_{\max} \times T = 2{,}9 \times 10^{-3} \text{ K·m}$$

Plus un corps est chaud, plus $\lambda_{\max}$ est petit (décalé vers le bleu).
""",
                            "quiz": {
                                "titre": "Quiz — Ondes et particules",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quelle est la célérité de la lumière dans le vide ?",
                                        "options": ["340 m/s", "3×10⁶ m/s", "3×10⁸ m/s", "3×10¹⁰ m/s"],
                                        "reponse_correcte": "2",
                                        "explication": "c = 3,00 × 10⁸ m·s⁻¹ dans le vide.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Une onde sonore peut se propager dans le vide.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "Le son est une onde mécanique qui nécessite un milieu matériel pour se propager.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Diffraction, interférences et effet Doppler",
                            "duree": 35,
                            "contenu": r"""# Diffraction, interférences et effet Doppler

## Diffraction

Lorsqu'une onde rencontre une ouverture ou un obstacle de dimension $a$ comparable à sa longueur d'onde $\lambda$, elle se **diffracte** : elle s'étale au-delà de l'obstacle.

**Condition de diffraction marquée :** $a \lesssim \lambda$.

L'écart angulaire du faisceau diffracté est :

$$\theta \approx \frac{\lambda}{a}$$

Plus l'ouverture est petite (par rapport à $\lambda$), plus la diffraction est importante.

## Interférences

Lorsque deux ondes **cohérentes** se superposent, on observe des **interférences** :
- **Constructives** : les amplitudes s'ajoutent (crêtes en phase).
- **Destructives** : les amplitudes s'annulent (opposition de phase).

### Différence de marche

$$\delta = d_2 - d_1$$

- Interférences constructives : $\delta = k\lambda$ ($k$ entier).
- Interférences destructives : $\delta = (k + \frac{1}{2})\lambda$.

### Interfrange (fentes d'Young)

$$i = \frac{\lambda \cdot D}{a}$$

$D$ : distance fentes–écran, $a$ : distance entre les deux fentes.

## Effet Doppler

La fréquence perçue d'une onde est modifiée lorsque la source et l'observateur sont en mouvement relatif :

- **Rapprochement** : fréquence perçue **augmentée** (son plus aigu, lumière décalée vers le bleu).
- **Éloignement** : fréquence perçue **diminuée** (son plus grave, lumière décalée vers le rouge).

$$\frac{\Delta f}{f} = \frac{v}{c}$$

*Application : radar, échographie Doppler, décalage vers le rouge des galaxies lointaines (expansion de l'Univers).*
""",
                            "quiz": {
                                "titre": "Quiz — Diffraction et interférences",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La diffraction est d'autant plus marquée que :",
                                        "options": [
                                            "L'ouverture est grande devant λ",
                                            "L'ouverture est petite devant λ",
                                            "La fréquence est élevée",
                                            "L'onde est transversale",
                                        ],
                                        "reponse_correcte": "1",
                                        "explication": "La diffraction est marquée quand a est de l'ordre de λ ou plus petit.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on le phénomène de changement de fréquence perçue lié au mouvement relatif source/observateur ?",
                                        "reponse_correcte": "effet Doppler",
                                        "tolerances": ["effet Doppler", "Doppler", "doppler", "effet doppler"],
                                        "explication": "L'effet Doppler décrit le décalage de fréquence lié au mouvement relatif.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.2 : Cinématique et dynamique newtoniennes ─────
                {
                    "ordre": 2,
                    "titre": "Cinématique et dynamique newtoniennes",
                    "description": "Vecteur vitesse, accélération, les trois lois de Newton, chute libre.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Cinématique du point",
                            "duree": 30,
                            "contenu": r"""# Cinématique du point

## Référentiel

Un **référentiel** est un corps de référence muni d'un repère d'espace et d'une horloge. Le mouvement dépend du référentiel choisi.

- **Référentiel terrestre** : lié à la surface de la Terre.
- **Référentiel géocentrique** : centré sur la Terre, directions vers les étoiles lointaines.
- **Référentiel héliocentrique** : centré sur le Soleil.

## Vecteur vitesse

$$\vec{v} = \frac{d\overrightarrow{OM}}{dt}$$

Le vecteur vitesse est **tangent à la trajectoire** en chaque point.

Pour un mouvement rectiligne : $v = \frac{dx}{dt}$.

## Vecteur accélération

$$\vec{a} = \frac{d\vec{v}}{dt}$$

### Types de mouvements

| Mouvement | Trajectoire | Accélération |
|---|---|---|
| Rectiligne uniforme | Droite | $\vec{a} = \vec{0}$ |
| Rectiligne unifor. varié | Droite | $\vec{a}$ constant, colinéaire à $\vec{v}$ |
| Circulaire uniforme | Cercle | $a = \frac{v^2}{R}$, centripète |

## Mouvement circulaire uniforme

La vitesse angulaire $\omega$ est constante : $\theta = \omega t$.

$$v = R\omega \qquad a = \frac{v^2}{R} = R\omega^2$$

L'accélération est **centripète** (dirigée vers le centre du cercle).
""",
                            "quiz": {
                                "titre": "Quiz — Cinématique",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Pour un mouvement circulaire uniforme, l'accélération est :",
                                        "options": ["Nulle", "Tangente à la trajectoire", "Centripète", "Centrifuge"],
                                        "reponse_correcte": "2",
                                        "explication": "L'accélération est dirigée vers le centre du cercle : elle est centripète.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Le vecteur vitesse est toujours tangent à la trajectoire.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "Par définition, le vecteur vitesse est tangent à la trajectoire en chaque point.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Les lois de Newton et la chute libre",
                            "duree": 35,
                            "contenu": r"""# Les lois de Newton

## Première loi (principe d'inertie)

Dans un **référentiel galiléen**, si la somme des forces est nulle, le point matériel est au repos ou en mouvement rectiligne uniforme.

$$\sum \vec{F} = \vec{0} \implies \vec{v} = \text{cte}$$

## Deuxième loi (relation fondamentale)

$$\sum \vec{F} = m\vec{a}$$

La résultante des forces est égale à la masse multipliée par l'accélération.

## Troisième loi (action-réaction)

$$\vec{F}_{A \to B} = -\vec{F}_{B \to A}$$

Les forces sont de même valeur, même direction, sens opposés, et sur la même droite d'action.

## Chute libre dans le champ de pesanteur uniforme

**Hypothèse :** seul le poids agit → $\vec{a} = \vec{g}$.

En prenant Oz vertical ascendant et l'origine au point de lancement :

$$a_x = 0 \qquad a_z = -g$$
$$v_x = v_0 \cos\alpha \qquad v_z = -gt + v_0 \sin\alpha$$
$$x = v_0 \cos\alpha \cdot t \qquad z = -\frac{1}{2}gt^2 + v_0 \sin\alpha \cdot t$$

### Cas particuliers

- **Chute verticale** ($\alpha = \frac{\pi}{2}$) : $z(t) = -\frac{1}{2}gt^2 + v_0 t$
- **Tir horizontal** ($\alpha = 0$) : $x = v_0 t$, $z = -\frac{1}{2}gt^2$

L'équation de la trajectoire $z(x)$ est une **parabole**.
""",
                            "quiz": {
                                "titre": "Quiz — Lois de Newton",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "En chute libre, l'accélération vaut :",
                                        "options": ["0", "v²/R", "g ≈ 9,81 m/s²", "mg"],
                                        "reponse_correcte": "2",
                                        "explication": "En chute libre (seul le poids), a⃗ = g⃗ donc a = g ≈ 9,81 m·s⁻².",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on la loi F⃗(A→B) = −F⃗(B→A) ?",
                                        "reponse_correcte": "action-réaction",
                                        "tolerances": ["action-réaction", "action réaction", "troisième loi de Newton", "3e loi de Newton"],
                                        "explication": "C'est le principe des actions réciproques ou 3ᵉ loi de Newton.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.3 : Satellites et lois de Kepler ──────────────
                {
                    "ordre": 3,
                    "titre": "Mouvement des satellites et des planètes",
                    "description": "Lois de Kepler, mouvement circulaire des satellites, période orbitale.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Lois de Kepler et gravitation",
                            "duree": 35,
                            "contenu": r"""# Mouvement des satellites et des planètes

## Lois de Kepler

### 1ʳᵉ loi (loi des orbites)

Les planètes décrivent des **ellipses** dont le Soleil est l'un des foyers.

### 2ᵉ loi (loi des aires)

Le segment reliant le Soleil à la planète balaie des **aires égales** en des **temps égaux**.

*Conséquence : une planète se déplace plus vite lorsqu'elle est proche du Soleil (périhélie).*

### 3ᵉ loi (loi des périodes)

$$\frac{T^2}{a^3} = \text{constante}$$

$T$ : période de révolution, $a$ : demi-grand axe de l'ellipse. La constante ne dépend que de la masse de l'astre attracteur.

## Gravitation universelle

$$F = G \frac{Mm}{r^2}$$

- $G = 6{,}67 \times 10^{-11}$ N·m²·kg⁻²
- $M$ : masse de l'astre attracteur, $m$ : masse du corps attiré
- $r$ : distance centre à centre

## Satellite en orbite circulaire

La force gravitationnelle fournit l'accélération centripète :

$$G\frac{M}{r^2} = \frac{v^2}{r} \implies v = \sqrt{\frac{GM}{r}}$$

**Période orbitale :**

$$T = 2\pi\sqrt{\frac{r^3}{GM}}$$

On retrouve la 3ᵉ loi de Kepler : $\frac{T^2}{r^3} = \frac{4\pi^2}{GM}$.

## Satellite géostationnaire

Un satellite géostationnaire a $T = 24$ h et orbite dans le plan équatorial à une altitude d'environ $36\,000$ km.
""",
                            "quiz": {
                                "titre": "Quiz — Satellites et Kepler",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Si la distance entre deux masses est doublée, la force gravitationnelle est :",
                                        "options": ["Doublée", "Divisée par 2", "Divisée par 4", "Multipliée par 4"],
                                        "reponse_correcte": "2",
                                        "explication": "F ∝ 1/r². Si r est doublé, F est divisée par 4.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on la loi T²/a³ = constante ?",
                                        "reponse_correcte": "troisième loi de Kepler",
                                        "tolerances": ["troisième loi de Kepler", "3e loi de Kepler", "loi des périodes", "Kepler"],
                                        "explication": "La 3ᵉ loi de Kepler relie le carré de la période au cube du demi-grand axe.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.4 : Transferts énergétiques et amortissement ──
                {
                    "ordre": 4,
                    "titre": "Transferts énergétiques et amortissement",
                    "description": "Travail d'une force, énergie mécanique, conservation et dissipation.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Travail d'une force et énergie mécanique",
                            "duree": 35,
                            "contenu": r"""# Travail d'une force et énergie mécanique

## Travail d'une force constante

Le travail d'une force constante $\vec{F}$ lors d'un déplacement de A à B :

$$W_{A \to B}(\vec{F}) = \vec{F} \cdot \overrightarrow{AB} = F \times AB \times \cos\alpha$$

- $\alpha$ : angle entre $\vec{F}$ et $\overrightarrow{AB}$
- Si $W > 0$ : travail **moteur** (favorise le mouvement)
- Si $W < 0$ : travail **résistant** (s'oppose au mouvement)
- Si $W = 0$ : force perpendiculaire au déplacement

**Le travail d'une force constante ne dépend pas du chemin suivi.**

## Travail du poids

$$W_{A \to B}(\vec{P}) = mg(z_A - z_B)$$

Il ne dépend que de la différence d'altitude : le poids est une **force conservative**.

## Énergie cinétique

$$E_c = \frac{1}{2}mv^2$$

**Théorème de l'énergie cinétique :** $\Delta E_c = \sum W(\vec{F})$.

## Énergie potentielle de pesanteur

$$E_p = mgz$$

(avec une référence de hauteur $z = 0$)

## Énergie mécanique

$$E_m = E_c + E_p = \frac{1}{2}mv^2 + mgz$$

## Conservation de l'énergie mécanique

Si les forces de frottement sont **négligeables**, l'énergie mécanique se conserve :

$$E_m = \text{constante}$$

Sinon, $\Delta E_m = W(\vec{f})$ avec $\vec{f}$ les forces de frottement ($< 0$) → l'énergie mécanique **diminue**.
""",
                            "quiz": {
                                "titre": "Quiz — Énergie mécanique",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Le travail du poids dépend :",
                                        "options": ["Du chemin suivi", "De la différence d'altitude uniquement", "De la masse uniquement", "De la vitesse"],
                                        "reponse_correcte": "1",
                                        "explication": "W(P⃗) = mg(zA − zB) : il ne dépend que de la différence d'altitude.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "L'énergie mécanique se conserve toujours.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "Elle ne se conserve que si les forces de frottement sont négligeables.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Dissipation d'énergie et oscillateur amorti",
                            "duree": 30,
                            "contenu": r"""# Dissipation d'énergie et oscillateur amorti

## Oscillateur non amorti

Un système masse-ressort sans frottement oscille indéfiniment avec une **période propre** :

$$T_0 = 2\pi\sqrt{\frac{m}{k}}$$

$k$ : constante de raideur du ressort, $m$ : masse.

L'énergie mécanique se conserve : il y a échange permanent entre $E_c$ et $E_p$ élastique.

## Oscillateur amorti

En présence de **frottements**, l'énergie mécanique **décroît** au cours du temps. L'amplitude des oscillations diminue progressivement.

### Régimes d'amortissement

- **Pseudo-périodique** : le système oscille avec une amplitude décroissante.
- **Apériodique** (critique ou sur-amorti) : le système revient à l'équilibre sans osciller.

## Facteur de qualité

Le **facteur de qualité** $Q$ caractérise l'amortissement :
- $Q$ élevé → faible amortissement → oscillations durables
- $Q$ faible → fort amortissement → retour rapide à l'équilibre

## Bilan énergétique

L'énergie mécanique dissipée est transformée en **énergie thermique** par les frottements :

$$\Delta E_m = W(\vec{f}) < 0$$

*L'énergie totale du système + environnement reste constante (premier principe).*
""",
                            "quiz": {
                                "titre": "Quiz — Oscillateur amorti",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La période propre d'un système masse-ressort dépend de :",
                                        "options": ["m et k", "m uniquement", "k uniquement", "L'amplitude"],
                                        "reponse_correcte": "0",
                                        "explication": "T₀ = 2π√(m/k), elle dépend de la masse et de la raideur.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Sous quelle forme l'énergie mécanique dissipée est-elle transformée en présence de frottements ?",
                                        "reponse_correcte": "énergie thermique",
                                        "tolerances": ["énergie thermique", "chaleur", "thermique", "energie thermique"],
                                        "explication": "Les frottements convertissent l'énergie mécanique en énergie thermique.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.5 : Temps et relativité restreinte ────────────
                {
                    "ordre": 5,
                    "titre": "Temps et relativité restreinte",
                    "description": "Postulats d'Einstein, dilatation des durées, invariance de c.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Postulats et dilatation des durées",
                            "duree": 30,
                            "contenu": r"""# Temps et relativité restreinte

## Contexte historique

La mesure du temps repose sur des phénomènes périodiques de plus en plus précis : cadrans solaires → horloges mécaniques → horloges à quartz → horloges atomiques.

La mécanique newtonienne suppose un **temps absolu** identique pour tous les observateurs. Einstein a montré en 1905 que cette hypothèse est fausse.

## Postulats d'Einstein (1905)

1. Les lois de la physique sont les mêmes dans tous les **référentiels galiléens**.
2. La vitesse de la lumière dans le vide est la même ($c = 3{,}00 \times 10^8$ m·s⁻¹) pour tous les observateurs, **indépendamment** de leur mouvement.

## Dilatation des durées

Soit $\Delta t_0$ la durée d'un phénomène mesurée dans le référentiel où il a lieu (**durée propre**). Un observateur en mouvement à la vitesse $v$ mesure :

$$\Delta t = \frac{\Delta t_0}{\sqrt{1 - \frac{v^2}{c^2}}} = \gamma \, \Delta t_0$$

avec le **facteur de Lorentz** $\gamma = \frac{1}{\sqrt{1 - v^2/c^2}} \ge 1$.

$\Delta t > \Delta t_0$ : **le temps « passe plus lentement » pour l'objet en mouvement.**

## Vérification expérimentale

- **Muons cosmiques** : leur durée de vie mesurée au sol est plus longue que leur durée de vie propre.
- **Horloges à bord d'avion** : expérience de Hafele-Keating (1971).
- **GPS** : sans correction relativiste, l'erreur de positionnement serait de ~10 km/jour.

## Limite

Pour $v \ll c$ : $\gamma \approx 1$ et $\Delta t \approx \Delta t_0$ → on retrouve la mécanique newtonienne.
""",
                            "quiz": {
                                "titre": "Quiz — Relativité restreinte",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Le facteur de Lorentz γ est toujours :",
                                        "options": ["< 1", "= 1", "≥ 1", "= c"],
                                        "reponse_correcte": "2",
                                        "explication": "γ = 1/√(1−v²/c²) ≥ 1 car v ≤ c.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La vitesse de la lumière dans le vide dépend du référentiel.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "Le 2ᵉ postulat d'Einstein affirme que c est la même pour tous les observateurs.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.6 : Énergie, matière et rayonnement ───────────
                {
                    "ordre": 6,
                    "titre": "Énergie, matière et rayonnement",
                    "description": "Du macroscopique au microscopique, transferts quantiques et dualité onde-particule.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Du macroscopique au microscopique et transferts thermiques",
                            "duree": 35,
                            "contenu": r"""# Du macroscopique au microscopique

## Agitation thermique

À l'échelle microscopique, les particules (atomes, molécules) sont en **mouvement permanent et désordonné**. La température est une mesure de l'**énergie cinétique moyenne** d'agitation.

$$E_c = \frac{1}{2}m\langle v^2 \rangle = \frac{3}{2}k_B T$$

$k_B = 1{,}38 \times 10^{-23}$ J·K⁻¹ (constante de Boltzmann).

## Nombre d'Avogadro et quantité de matière

$$N_A = 6{,}02 \times 10^{23} \text{ mol}^{-1}$$

$$n = \frac{N}{N_A} = \frac{m}{M}$$

## Transferts thermiques

### Conduction

Transport de chaleur **sans déplacement de matière** (de proche en proche). Les métaux sont de bons conducteurs.

### Convection

Transport de chaleur **avec déplacement de matière** (courants d'air chaud ascendants).

### Rayonnement

Transfert d'énergie par **ondes électromagnétiques** (infrarouge). Ne nécessite pas de milieu matériel.

## Flux thermique

$$\Phi = \frac{Q}{\Delta t}$$

$\Phi$ en watts (W), $Q$ en joules (J). Le flux va toujours du corps **chaud** vers le corps **froid**.
""",
                            "quiz": {
                                "titre": "Quiz — Macroscopique au microscopique",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La température mesure :",
                                        "options": ["La quantité de chaleur", "L'énergie cinétique moyenne d'agitation", "L'énergie potentielle", "La pression"],
                                        "reponse_correcte": "1",
                                        "explication": "La température est proportionnelle à l'énergie cinétique moyenne d'agitation thermique.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Le transfert thermique par convection implique :",
                                        "options": ["Pas de déplacement de matière", "Un déplacement de matière", "Des ondes EM", "Le vide"],
                                        "reponse_correcte": "1",
                                        "explication": "La convection nécessite un déplacement de matière (fluide).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Transferts quantiques d'énergie et dualité onde-particule",
                            "duree": 35,
                            "contenu": r"""# Transferts quantiques d'énergie

## Quantification des niveaux d'énergie

Un atome ne peut exister que dans des **états d'énergie discrets** $E_1, E_2, \ldots$

- L'état de plus basse énergie est l'**état fondamental**.
- Les autres sont des **états excités**.

## Émission et absorption d'un photon

Un photon transporte l'énergie :

$$E_{\text{photon}} = h\nu = \frac{hc}{\lambda}$$

$h = 6{,}63 \times 10^{-34}$ J·s (constante de Planck).

- **Absorption** : l'atome passe du niveau $E_n$ au niveau $E_p$ si $E_{\text{photon}} = E_p - E_n$.
- **Émission** : l'atome revient de $E_p$ à $E_n$ en émettant un photon de même énergie.

## Spectre d'émission et d'absorption

- **Émission** : raies brillantes sur fond noir (gaz chaud et peu dense).
- **Absorption** : raies sombres sur fond continu (gaz froid devant une source chaude).

## Dualité onde-particule

La matière a un double comportement :
- **Ondulatoire** : diffraction des électrons (expérience de Davisson-Germer).
- **Corpusculaire** : effet photoélectrique.

**Longueur d'onde de De Broglie :**

$$\lambda = \frac{h}{mv}$$

$m$ : masse de la particule, $v$ : sa vitesse. Pour les objets macroscopiques, $\lambda$ est si petite que le comportement ondulatoire est inobservable.
""",
                            "quiz": {
                                "titre": "Quiz — Transferts quantiques",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "L'énergie d'un photon est donnée par :",
                                        "options": ["E = mc²", "E = hν", "E = ½mv²", "E = kT"],
                                        "reponse_correcte": "1",
                                        "explication": "E = hν = hc/λ avec h la constante de Planck.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on la longueur d'onde λ = h/(mv) associée à une particule ?",
                                        "reponse_correcte": "De Broglie",
                                        "tolerances": ["De Broglie", "de Broglie", "longueur d'onde de De Broglie", "longueur de De Broglie"],
                                        "explication": "C'est la longueur d'onde de De Broglie, qui relie propriétés ondulatoires et corpusculaires.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.7 : Transmettre et stocker l'information ──────
                {
                    "ordre": 7,
                    "titre": "Transmettre et stocker l'information",
                    "description": "Signal analogique/numérique, transmission, stockage optique.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Transmission et procédés physiques",
                            "duree": 30,
                            "contenu": r"""# Transmettre et stocker l'information

## Chaîne de transmission

$$\text{Source} \to \text{Émetteur} \to \text{Canal} \to \text{Récepteur} \to \text{Destinataire}$$

## Signal analogique et signal numérique

- **Analogique** : varie **continûment** dans le temps (ex : tension d'un micro).
- **Numérique** : suite de valeurs **discrètes** codées en binaire (0 et 1).

### Conversion analogique → numérique

1. **Échantillonnage** : prélèvement de valeurs à intervalles réguliers (fréquence $f_e$).
   - Théorème de Shannon : $f_e \ge 2 f_{\max}$ pour éviter le repliement spectral.
2. **Quantification** : arrondi de chaque échantillon à la valeur la plus proche.
3. **Codage** : écriture en binaire sur $n$ bits → $2^n$ niveaux possibles.

## Propagation guidée

### Câble coaxial
Transmission par signal électrique. Atténuation croissante avec la fréquence et la distance.

### Fibre optique
Transmission par **lumière** (réflexion totale dans le cœur de la fibre). Très faible atténuation, grande bande passante.

$$n_1 \sin i_1 = n_2 \sin i_2 \quad \text{(loi de Snell-Descartes)}$$

Réflexion totale si $i > i_{\text{limite}}$ avec $\sin i_{\text{limite}} = \frac{n_2}{n_1}$ ($n_1 > n_2$).

### Propagation libre
Ondes hertziennes (radio, Wi-Fi, satellite). Atténuation en $1/d^2$.
""",
                            "quiz": {
                                "titre": "Quiz — Transmission de l'information",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "D'après le théorème de Shannon, la fréquence d'échantillonnage doit être :",
                                        "options": ["= fmax", "≥ 2·fmax", "≤ fmax/2", "quelconque"],
                                        "reponse_correcte": "1",
                                        "explication": "Shannon impose fe ≥ 2·fmax pour une numérisation fidèle.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La fibre optique transmet l'information sous forme électrique.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "La fibre optique transmet l'information sous forme de lumière.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Stockage optique et images numériques",
                            "duree": 25,
                            "contenu": r"""# Stockage optique et images numériques

## Stockage optique

### Principe du CD / DVD / Blu-ray

Un **laser** lit des creux (*pits*) et des plats (*lands*) gravés sur un disque réfléchissant.

| Support | $\lambda$ laser | Capacité |
|---|---|---|
| CD | 780 nm (IR) | 700 Mo |
| DVD | 650 nm (rouge) | 4,7 Go |
| Blu-ray | 405 nm (bleu) | 25 Go |

Plus la longueur d'onde est courte, plus la résolution est fine → plus de données.

## Images numériques

### Pixel

L'image est découpée en **pixels** (picture elements). Plus il y a de pixels, meilleure est la **définition**.

### Codage des couleurs

Chaque pixel est codé en **RVB** (Rouge, Vert, Bleu), chaque canal sur 8 bits :
- $2^8 = 256$ niveaux par canal
- $256^3 \approx 16{,}7$ millions de couleurs

### Taille d'un fichier image

$$\text{Taille} = \text{nombre de pixels} \times \text{profondeur de couleur}$$

Exemple : image $1920 \times 1080$ en 24 bits → $1920 \times 1080 \times 3 \approx 6{,}2$ Mo (non compressé).
""",
                            "quiz": {
                                "titre": "Quiz — Stockage et images",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Pourquoi le Blu-ray stocke-t-il plus que le DVD ?",
                                        "options": [
                                            "La vitesse de rotation est plus élevée",
                                            "Le laser bleu a une longueur d'onde plus courte",
                                            "Le disque est plus grand",
                                            "Le laser est plus puissant",
                                        ],
                                        "reponse_correcte": "1",
                                        "explication": "λ plus courte → meilleure résolution → pits plus petits → plus de données.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on chaque point élémentaire d'une image numérique ?",
                                        "reponse_correcte": "pixel",
                                        "tolerances": ["pixel", "un pixel", "Pixel"],
                                        "explication": "Un pixel (picture element) est le plus petit élément d'une image numérique.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.8 : Son et musique (SPÉCIALITÉ) ───────────────
                {
                    "ordre": 8,
                    "titre": "Son et musique (Spécialité)",
                    "description": "Acoustique musicale, instruments, émetteurs et récepteurs sonores. Chapitre de spécialité Physique-Chimie.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Acoustique musicale",
                            "duree": 35,
                            "contenu": r"""# Acoustique musicale — *Spécialité*

## L'onde sonore

Le son est une **onde mécanique progressive longitudinale** : les particules du milieu oscillent **dans la direction de propagation**.

### Caractéristiques d'un son

- **Hauteur** : liée à la **fréquence** $f$ (grave : $f$ petit, aigu : $f$ grand).
- **Timbre** : déterminé par le **spectre** (ensemble des harmoniques).
- **Intensité** : liée à l'**amplitude** de la vibration.

## Spectre d'un son

Un son musical comporte un **fondamental** de fréquence $f_1$ et des **harmoniques** de fréquences :

$$f_n = n \times f_1 \qquad (n = 1, 2, 3, \ldots)$$

Le **timbre** du son caractérise les amplitudes relatives des harmoniques. Il permet de distinguer un piano d'une flûte jouant la même note.

## Gamme tempérée

Le rapport de fréquence entre deux notes consécutives est :

$$r = 2^{1/12} \approx 1{,}059$$

Un **octave** correspond à un doublement de fréquence. Le **la₃** a une fréquence de 440 Hz.

## Niveau d'intensité sonore

$$L = 10 \log\!\left(\frac{I}{I_0}\right)$$

$L$ en décibels (dB), $I$ : intensité en W·m⁻², $I_0 = 10^{-12}$ W·m⁻² (seuil d'audibilité).

- Seuil de douleur : $L \approx 120$ dB.
- Doublement de $I$ → augmentation de 3 dB.
""",
                            "quiz": {
                                "titre": "Quiz — Acoustique musicale",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Les harmoniques d'un son de fondamental f₁ ont pour fréquences :",
                                        "options": ["f₁/n", "n×f₁", "f₁ + n", "f₁ⁿ"],
                                        "reponse_correcte": "1",
                                        "explication": "Les harmoniques sont des multiples entiers du fondamental : fn = n×f₁.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Quelle caractéristique du son permet de distinguer deux instruments jouant la même note ?",
                                        "reponse_correcte": "timbre",
                                        "tolerances": ["timbre", "le timbre", "Timbre"],
                                        "explication": "Le timbre est lié au spectre (amplitudes relatives des harmoniques).",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Instruments de musique, émetteurs et récepteurs",
                            "duree": 30,
                            "contenu": r"""# Instruments de musique — *Spécialité*

## Instruments à cordes

Une corde vibrante de longueur $L$, de masse linéique $\mu$ et de tension $T$ produit des **modes propres** :

$$f_n = \frac{n}{2L}\sqrt{\frac{T}{\mu}}$$

Le fondamental ($n = 1$) détermine la hauteur de la note.

*Plus la corde est courte, tendue ou légère, plus le son est aigu.*

## Instruments à vent (tuyaux sonores)

### Tuyau ouvert aux deux extrémités

$$f_n = n \times \frac{v_{\text{son}}}{2L}$$

### Tuyau fermé à une extrémité

$$f_n = (2n-1) \times \frac{v_{\text{son}}}{4L}$$

(seuls les harmoniques impairs sont présents)

## Récepteurs sonores

### Le microphone
Convertit les vibrations acoustiques en **signal électrique**. Le courant produit a la même fréquence que l'onde sonore.

### L'oreille humaine
Domaine audible : $20$ Hz à $20\,000$ Hz. Sensibilité maximale autour de $3\,000$ Hz.

## Émetteurs sonores

### Le haut-parleur
Convertit un signal électrique en vibrations mécaniques (membrane). C'est l'inverse du microphone.

## Son et architecture

Dans une salle de concert, les **réflexions** du son sur les parois créent une **réverbération**. Le temps de réverbération optimal dépend de l'usage (musique, parole).
""",
                            "quiz": {
                                "titre": "Quiz — Instruments de musique",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Pour qu'une corde vibrante donne un son plus aigu, il faut :",
                                        "options": ["Augmenter la longueur", "Diminuer la tension", "Raccourcir la corde", "Augmenter la masse linéique"],
                                        "reponse_correcte": "2",
                                        "explication": "f = (1/2L)√(T/μ) : une corde plus courte donne un son plus aigu.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Un tuyau fermé à une extrémité ne produit que des harmoniques impairs.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "Les conditions aux limites imposent fn = (2n−1)·v/(4L), soit uniquement les harmoniques impairs.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.9 : Radioactivité et réactions nucléaires ─────
                {
                    "ordre": 9,
                    "titre": "Radioactivité et réactions nucléaires",
                    "description": "Désintégrations radioactives, loi de décroissance, énergie de liaison et applications.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Radioactivité et décroissance radioactive",
                            "duree": 35,
                            "contenu": r"""# Radioactivité

## Noyau atomique

Un noyau $^A_Z X$ contient $Z$ protons et $N = A - Z$ neutrons ($A$ = nombre de nucléons).

Des noyaux ayant le même $Z$ mais des $A$ différents sont des **isotopes**.

## Types de radioactivité

### Radioactivité $\alpha$

$$^A_Z X \to ^{A-4}_{Z-2} Y + ^4_2 He$$

Émission d'un noyau d'hélium (particule α).

### Radioactivité $\beta^-$

$$^A_Z X \to ^A_{Z+1} Y + ^0_{-1} e$$

Un neutron se transforme en proton avec émission d'un électron.

### Radioactivité $\beta^+$

$$^A_Z X \to ^A_{Z-1} Y + ^0_{+1} e$$

Un proton se transforme en neutron avec émission d'un positon.

### Rayonnement $\gamma$

Émission d'un photon $\gamma$ lors de la désexcitation du noyau. Pas de changement de $A$ ni $Z$.

## Loi de décroissance radioactive

$$N(t) = N_0 \, e^{-\lambda t}$$

$\lambda$ : constante radioactive (s⁻¹). **Demi-vie :**

$$t_{1/2} = \frac{\ln 2}{\lambda}$$

Après $t_{1/2}$, il reste la moitié des noyaux radioactifs.

## Activité

$$A(t) = \lambda N(t) = A_0 \, e^{-\lambda t}$$

$A$ en becquerels (Bq) : nombre de désintégrations par seconde.
""",
                            "quiz": {
                                "titre": "Quiz — Radioactivité",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Lors d'une désintégration α, le nombre de nucléons A :",
                                        "options": ["Ne change pas", "Diminue de 2", "Diminue de 4", "Augmente de 4"],
                                        "reponse_correcte": "2",
                                        "explication": "La particule α emporte 4 nucléons (2 protons + 2 neutrons).",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on la durée au bout de laquelle il reste la moitié des noyaux radioactifs ?",
                                        "reponse_correcte": "demi-vie",
                                        "tolerances": ["demi-vie", "demi vie", "temps de demi-vie", "période radioactive"],
                                        "explication": "La demi-vie t₁/₂ est la durée au bout de laquelle la moitié des noyaux se sont désintégrés.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.10 : Mesures et incertitudes ──────────────────
                {
                    "ordre": 10,
                    "titre": "Mesures et incertitudes",
                    "description": "Évaluer une mesure, incertitude-type, propagation des incertitudes.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Incertitudes de mesure et chiffres significatifs",
                            "duree": 25,
                            "contenu": r"""# Mesures et incertitudes

## Erreurs de mesure

### Erreur aléatoire
Fluctuation imprévisible d'une mesure à l'autre. On la réduit en **répétant** les mesures.

### Erreur systématique
Décalage constant dans le même sens, lié à un défaut de l'instrument ou du protocole. Non détectable par répétition.

## Valeur mesurée et incertitude

Le **résultat d'une mesure** s'écrit :

$$X = x_{\text{mes}} \pm U(x)$$

$U(x)$ : **incertitude élargie** (souvent à 95 %).

## Incertitude-type

### Type A (statistique)

On effectue $n$ mesures $x_1, x_2, \ldots, x_n$.

$$\bar{x} = \frac{1}{n}\sum x_i \qquad s = \sqrt{\frac{1}{n-1}\sum(x_i - \bar{x})^2}$$

L'incertitude-type est $u(x) = \frac{s}{\sqrt{n}}$.

### Type B (constructeur, graduation)

Basée sur la résolution de l'instrument ou les données du fabricant.

## Chiffres significatifs

Le résultat final doit être arrondi de sorte que l'incertitude ne comporte que **1 ou 2 chiffres significatifs**.

## Propagation des incertitudes

Pour $y = f(x_1, x_2, \ldots)$ :
- **Somme/différence** : $u(y) = \sqrt{u(x_1)^2 + u(x_2)^2}$
- **Produit/quotient** : $\frac{u(y)}{y} = \sqrt{\left(\frac{u(x_1)}{x_1}\right)^2 + \left(\frac{u(x_2)}{x_2}\right)^2}$
""",
                            "quiz": {
                                "titre": "Quiz — Mesures et incertitudes",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Pour réduire l'incertitude de type A, il faut :",
                                        "options": ["Changer d'instrument", "Répéter les mesures", "Augmenter la température", "Utiliser une formule"],
                                        "reponse_correcte": "1",
                                        "explication": "u(x) = s/√n : plus n augmente, plus l'incertitude diminue.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Une erreur systématique peut être détectée en répétant les mesures.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "L'erreur systématique se reproduit identiquement à chaque mesure ; la répétition ne la détecte pas.",
                                        "points": 2,
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
                # ── Ch.1 : Spectroscopies ────────────────────────────
                {
                    "ordre": 1,
                    "titre": "Spectroscopies UV-visible, IR et RMN",
                    "description": "Spectroscopie UV-visible, infrarouge (groupes caractéristiques) et RMN du proton.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Spectroscopie UV-visible et IR",
                            "duree": 35,
                            "contenu": r"""# Spectroscopie UV-visible et infrarouge

## Spectroscopie UV-visible

### Principe

Les molécules possédant des **doubles liaisons conjuguées** ou des **groupes chromophores** absorbent la lumière dans le domaine UV-visible (200–800 nm).

### Loi de Beer-Lambert

$$A = \varepsilon \cdot \ell \cdot c$$

- $A$ : absorbance (sans unité)
- $\varepsilon$ : coefficient d'absorption molaire (L·mol⁻¹·cm⁻¹)
- $\ell$ : épaisseur de la cuve (cm)
- $c$ : concentration (mol·L⁻¹)

La loi n'est valable que pour des solutions **diluées** et des radiations **monochromatiques**.

### Couleur d'une solution

La couleur perçue est la **couleur complémentaire** de la couleur absorbée :

| Couleur absorbée | $\lambda$ absorbée (nm) | Couleur perçue |
|---|---|---|
| Violet | 400–450 | Jaune-vert |
| Bleu | 450–490 | Orange |
| Vert | 490–560 | Rouge |
| Rouge | 620–750 | Cyan |

## Spectroscopie infrarouge (IR)

### Principe

Les liaisons chimiques vibrent (élongation, déformation). Elles absorbent un rayonnement IR à des **nombres d'onde** $\tilde{\nu}$ caractéristiques.

$$\tilde{\nu} = \frac{1}{\lambda} \quad \text{(cm}^{-1}\text{)}$$

### Bandes caractéristiques

| Liaison | $\tilde{\nu}$ (cm⁻¹) | Forme |
|---|---|---|
| O–H (libre) | 3580–3650 | Fine |
| O–H (lié, H) | 3200–3400 | Large |
| N–H | 3300–3500 | Moyenne |
| C–H | 2800–3100 | Moyenne |
| C=O | 1650–1750 | Forte, fine |
| C=C | 1600–1680 | Moyenne |

La zone 1500–500 cm⁻¹ est l'**empreinte digitale** de la molécule.
""",
                            "quiz": {
                                "titre": "Quiz — UV-visible et IR",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La bande d'absorption IR vers 1700 cm⁻¹ correspond typiquement à :",
                                        "options": ["O–H", "C–H", "C=O", "N–H"],
                                        "reponse_correcte": "2",
                                        "explication": "Le groupe C=O absorbe entre 1650 et 1750 cm⁻¹.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "L'absorbance est proportionnelle à la concentration selon la loi de Beer-Lambert.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "A = ε·ℓ·c : l'absorbance est bien proportionnelle à c.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Spectroscopie RMN du proton",
                            "duree": 35,
                            "contenu": r"""# Spectroscopie RMN du proton

## Principe

La **Résonance Magnétique Nucléaire** du proton ($^1$H) permet de déterminer l'**environnement chimique** des atomes d'hydrogène dans une molécule.

Les noyaux d'hydrogène, soumis à un **champ magnétique intense**, absorbent des radiofréquences à des **déplacements chimiques** $\delta$ caractéristiques.

## Déplacement chimique $\delta$

$\delta$ est exprimé en **ppm** (parties par million). Il dépend de l'environnement électronique du proton.

| Environnement | $\delta$ (ppm) |
|---|---|
| R–CH₃ (alkyle) | 0,8 – 1,0 |
| R–CH₂–R | 1,2 – 1,4 |
| C=C–H (alcène) | 4,5 – 6,5 |
| Ar–H (aromatique) | 6,5 – 8,0 |
| R–CHO (aldéhyde) | 9,0 – 10,0 |
| R–COOH (acide) | 10 – 12 |

## Protons équivalents

Des protons rendus **identiques par symétrie** de la molécule sont dit **équivalents** : ils donnent un **seul signal**.

**Exemple :** le propan-2-ol (CH₃)₂CHOH a 3 groupes de H équivalents → 3 signaux.

## Intégration

L'**aire sous un signal** (courbe d'intégration) est proportionnelle au **nombre de protons** qui le produisent.

## Multiplicité (couplage spin-spin)

Un signal de protons voisins de $n$ protons équivalents est **dédoublé** en $n + 1$ pics :

| Voisins $n$ | Multiplicité |
|---|---|
| 0 | Singulet (s) |
| 1 | Doublet (d) |
| 2 | Triplet (t) |
| 3 | Quadruplet (q) |

*Règle des (n+1) : ne s'applique pas aux protons portés par le même carbone.*
""",
                            "quiz": {
                                "titre": "Quiz — RMN",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Un proton ayant 2 voisins équivalents donne un signal sous forme de :",
                                        "options": ["Singulet", "Doublet", "Triplet", "Quadruplet"],
                                        "reponse_correcte": "2",
                                        "explication": "n = 2 voisins → n + 1 = 3 pics → triplet.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on la grandeur δ (en ppm) caractéristique de l'environnement d'un proton en RMN ?",
                                        "reponse_correcte": "déplacement chimique",
                                        "tolerances": ["déplacement chimique", "deplacement chimique", "chemical shift"],
                                        "explication": "Le déplacement chimique δ repère la position du signal sur le spectre RMN.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.2 : Cinétique chimique et stéréochimie ────────
                {
                    "ordre": 2,
                    "titre": "Cinétique chimique et stéréochimie",
                    "description": "Vitesse de réaction, facteurs cinétiques, catalyse, stéréoisomérie.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Vitesse de réaction et facteurs cinétiques",
                            "duree": 30,
                            "contenu": r"""# Cinétique chimique

## Vitesse de réaction

La **vitesse volumique** de réaction quantifie la vitesse de disparition des réactifs ou de formation des produits :

$$v = -\frac{1}{\nu_{\text{réactif}}} \frac{d[\text{réactif}]}{dt} = \frac{1}{\nu_{\text{produit}}} \frac{d[\text{produit}]}{dt}$$

$v$ en mol·L⁻¹·s⁻¹, $\nu$ : coefficient stœchiométrique (en valeur absolue).

La vitesse est **toujours positive** et **décroît** au cours du temps.

## Facteurs cinétiques

### Concentration des réactifs
Plus les concentrations sont élevées → plus les chocs moléculaires sont fréquents → réaction plus rapide.

### Température
Une augmentation de température augmente l'**énergie cinétique** des molécules → davantage de chocs efficaces.

*En pratique : +10 °C double environ la vitesse.*

### Solvant
Peut modifier les interactions entre réactifs et donc la vitesse.

## Demi-vie (temps de demi-réaction)

$$t_{1/2}$$ : durée nécessaire pour que l'avancement $x$ atteigne la moitié de $x_{\text{final}}$.

## Catalyse

Un **catalyseur** accélère la réaction sans être consommé. Il abaisse l'**énergie d'activation** $E_a$.

| Type | Description | Exemple |
|---|---|---|
| Homogène | Même phase que les réactifs | Ion Fe³⁺ en solution |
| Hétérogène | Phase différente | Platine solide |
| Enzymatique | Catalyseur biologique (enzyme) | Lipase, amylase |
""",
                            "quiz": {
                                "titre": "Quiz — Cinétique",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Un catalyseur agit en :",
                                        "options": [
                                            "Augmentant l'énergie d'activation",
                                            "Diminuant l'énergie d'activation",
                                            "Modifiant les produits",
                                            "Augmentant la température",
                                        ],
                                        "reponse_correcte": "1",
                                        "explication": "Le catalyseur abaisse l'énergie d'activation sans modifier les produits.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Un catalyseur est consommé lors de la réaction.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "Par définition, un catalyseur est régénéré à la fin de la réaction.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Stéréochimie : chiralité et stéréoisomérie",
                            "duree": 30,
                            "contenu": r"""# Stéréochimie

## Carbone asymétrique

Un atome de carbone est **asymétrique** (ou chiral, noté C*) s'il est lié à **4 substituants différents**.

## Chiralité

Une molécule est **chirale** si elle n'est **pas superposable** à son image dans un miroir.

*Critère pratique : une molécule possédant un carbone asymétrique est généralement chirale.*

## Énantiomères

Les énantiomères sont des **stéréoisomères** images l'un de l'autre dans un miroir, **non superposables**.

Propriétés :
- Mêmes propriétés physiques (Tf, Teb, densité, solubilité).
- **Activité optique opposée** (dévient le plan de polarisation de la lumière en sens contraire).
- Propriétés biologiques souvent **différentes** (odeur, goût, activité pharmaceutique).

## Diastéréoisomères

Stéréoisomères qui ne sont **pas énantiomères**.

Exemples :
- Isomères Z/E autour d'une double liaison C=C.
- Molécules à 2 carbones asymétriques (on peut avoir énantiomères **et** diastéréoisomères).

Les diastéréoisomères ont des **propriétés physiques et chimiques différentes**.

## Mélange racémique

Un mélange **équimolaire** (50/50) de deux énantiomères est **optiquement inactif** (les rotations s'annulent).
""",
                            "quiz": {
                                "titre": "Quiz — Stéréochimie",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Un carbone asymétrique est lié à :",
                                        "options": ["4 H", "4 substituants identiques", "4 substituants différents", "3 substituants"],
                                        "reponse_correcte": "2",
                                        "explication": "Un C* porte 4 groupes tous différents.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on deux stéréoisomères images dans un miroir, non superposables ?",
                                        "reponse_correcte": "énantiomères",
                                        "tolerances": ["énantiomères", "enantiomeres", "des énantiomères", "enantiomère"],
                                        "explication": "Les énantiomères sont des isomères miroirs non superposables.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.3 : Réaction acide-base et dosage ─────────────
                {
                    "ordre": 3,
                    "titre": "Réaction chimique par échange de protons et dosage",
                    "description": "Acides, bases selon Brønsted, pH, dosage par titrage.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Acides, bases et pH",
                            "duree": 35,
                            "contenu": r"""# Réaction acide-base

## Définitions de Brønsted

- **Acide** : espèce capable de **céder** un proton H⁺.
- **Base** : espèce capable de **capter** un proton H⁺.

### Couple acide-base

$$\text{AH} \rightleftharpoons \text{A}^- + \text{H}^+$$

Exemples :
- CH₃COOH / CH₃COO⁻ (acide éthanoïque / ion éthanoate)
- NH₄⁺ / NH₃ (ion ammonium / ammoniac)
- H₂O / HO⁻ (eau / ion hydroxyde)

L'eau est **amphotère** : elle peut jouer le rôle d'acide ou de base.

## Autoprotolyse de l'eau

$$2\,\text{H}_2\text{O} \rightleftharpoons \text{H}_3\text{O}^+ + \text{HO}^-$$

**Produit ionique de l'eau :** $K_e = [\text{H}_3\text{O}^+][\text{HO}^-] = 10^{-14}$ à 25 °C.

## pH

$$\text{pH} = -\log[\text{H}_3\text{O}^+]$$

| pH | Milieu |
|---|---|
| < 7 | Acide |
| = 7 | Neutre |
| > 7 | Basique |

## Force des acides et des bases

### Constante d'acidité

$$K_a = \frac{[\text{A}^-][\text{H}_3\text{O}^+]}{[\text{AH}]}$$

$$\text{p}K_a = -\log K_a$$

- **Acide fort** : dissociation totale ($K_a$ très grand, $\text{p}K_a < 0$). Ex : HCl, H₂SO₄.
- **Acide faible** : dissociation partielle. Ex : CH₃COOH ($\text{p}K_a = 4{,}8$).

### Diagramme de prédominance

$$\text{pH} < \text{p}K_a \implies \text{AH prédomine}$$
$$\text{pH} > \text{p}K_a \implies \text{A}^- \text{ prédomine}$$
""",
                            "quiz": {
                                "titre": "Quiz — Acides et bases",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Une solution de pH = 3 est :",
                                        "options": ["Basique", "Neutre", "Acide", "Impossible à déterminer"],
                                        "reponse_correcte": "2",
                                        "explication": "pH < 7 correspond à une solution acide.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Quelle est la valeur du produit ionique de l'eau Ke à 25 °C ?",
                                        "reponse_correcte": "10⁻¹⁴",
                                        "tolerances": ["10⁻¹⁴", "1e-14", "10^-14", "10^(-14)", "10-14"],
                                        "explication": "Ke = [H₃O⁺][HO⁻] = 10⁻¹⁴ à 25 °C.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Dosage acide-base par titrage",
                            "duree": 35,
                            "contenu": r"""# Dosage acide-base par titrage

## Principe

Un **titrage** (ou dosage) consiste à déterminer la concentration d'une espèce en solution par réaction avec un réactif titrant de **concentration connue**.

## Équivalence

Au point d'**équivalence**, les réactifs ont été mélangés en **proportions stœchiométriques** : il ne reste ni acide ni base en excès.

$$n_{\text{acide}} = n_{\text{base}} \implies c_A \cdot V_A = c_B \cdot V_{BE}$$

$V_{BE}$ : volume de base ajouté à l'équivalence.

## Repérage de l'équivalence

### Par indicateur coloré

Un **indicateur coloré** change de couleur dans une zone de pH. On choisit un indicateur dont la **zone de virage** contient le pH à l'équivalence.

| Indicateur | Zone de virage |
|---|---|
| Hélianthine | 3,1 – 4,4 |
| BBT | 6,0 – 7,6 |
| Phénolphtaléine | 8,2 – 10,0 |

### Par pH-métrie

On trace la courbe $\text{pH} = f(V_B)$. L'équivalence se situe au **point d'inflexion** (dérivée maximale).

### Par conductimétrie

On suit la **conductivité** $\sigma$ de la solution. L'équivalence est repérée par un **changement de pente**.

## Dosage d'un acide fort par une base forte

- Avant l'équivalence : pH acide, augmente lentement.
- À l'équivalence : pH = 7 (saut de pH brutal).
- Après l'équivalence : pH basique, augmente lentement.

## Dosage d'un acide faible par une base forte

- À la demi-équivalence ($V = V_{BE}/2$) : pH = pKₐ.
- À l'équivalence : pH > 7 (milieu basique car A⁻ est une base faible).
""",
                            "quiz": {
                                "titre": "Quiz — Dosage acide-base",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "À l'équivalence d'un dosage acide faible / base forte, le pH est :",
                                        "options": ["< 7", "= 7", "> 7", "= pKa"],
                                        "reponse_correcte": "2",
                                        "explication": "La base conjuguée A⁻ est en solution → pH > 7.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "À la demi-équivalence, pH = pKa.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "À V = VBE/2, [AH] = [A⁻] donc pH = pKa.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.4 : Transformation en chimie organique ────────
                {
                    "ordre": 4,
                    "titre": "Transformation en chimie organique",
                    "description": "Groupes caractéristiques, réactivité des liaisons polarisées, mécanismes réactionnels.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Groupes caractéristiques et réactivité",
                            "duree": 30,
                            "contenu": r"""# Groupes caractéristiques et réactivité

## Groupes caractéristiques en chimie organique

| Famille | Groupe | Exemple |
|---|---|---|
| Alcool | –OH | Éthanol CH₃CH₂OH |
| Aldéhyde | –CHO | Éthanal CH₃CHO |
| Cétone | –CO– | Propanone CH₃COCH₃ |
| Acide carboxylique | –COOH | Acide éthanoïque CH₃COOH |
| Amine | –NH₂ | Éthanamine CH₃CH₂NH₂ |
| Ester | –COO– | Éthanoate d'éthyle CH₃COOC₂H₅ |
| Amide | –CONH₂ | Éthanamide CH₃CONH₂ |

## Électronégativité et polarisation

L'**électronégativité** $\chi$ mesure la capacité d'un atome à attirer les électrons d'une liaison.

Échelle : F > O > N > C > H

Une liaison **polarisée** C–X (X plus électronégatif) crée :
- Un site **électrophile** ($\delta^+$) sur le carbone.
- Un site **nucléophile** ($\delta^-$) sur X.

## Sites réactifs

- **Nucléophile** : espèce riche en électrons, donneur de doublet. Ex : HO⁻, NH₃, H₂O.
- **Électrophile** : espèce pauvre en électrons, accepteur de doublet. Ex : H⁺, C$^{\delta+}$.

## Types de réaction

| Type | Bilan |
|---|---|
| **Substitution** | Un atome (ou groupe) en remplace un autre |
| **Addition** | Des atomes s'ajoutent sur une double liaison |
| **Élimination** | Une petite molécule est éliminée, création d'une double liaison |
""",
                            "quiz": {
                                "titre": "Quiz — Chimie organique",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Le groupe –COOH est le groupe caractéristique des :",
                                        "options": ["Alcools", "Aldéhydes", "Acides carboxyliques", "Cétones"],
                                        "reponse_correcte": "2",
                                        "explication": "–COOH est le groupe carboxyle, caractéristique des acides carboxyliques.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on une espèce chimique riche en électrons, donneur de doublet ?",
                                        "reponse_correcte": "nucléophile",
                                        "tolerances": ["nucléophile", "nucleophile", "un nucléophile"],
                                        "explication": "Un nucléophile est un donneur de doublet d'électrons.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Mécanismes réactionnels en chimie organique",
                            "duree": 30,
                            "contenu": r"""# Mécanismes réactionnels

## Modification de chaîne

### Allongement de chaîne

Ajout d'atomes de carbone à la chaîne carbonée (polymérisation, réactions de couplage).

### Raccourcissement de chaîne

Coupure de la chaîne carbonée (craquage, vapocraquage).

### Ramification

Transformation d'une chaîne linéaire en chaîne ramifiée (isomérisation).

## Modification de groupe caractéristique

### Oxydation

$$\text{Alcool primaire} \xrightarrow{\text{ox.}} \text{Aldéhyde} \xrightarrow{\text{ox.}} \text{Acide carboxylique}$$

$$\text{Alcool secondaire} \xrightarrow{\text{ox.}} \text{Cétone}$$

*Un alcool tertiaire ne s'oxyde pas (pas de H sur C–OH).*

### Réduction

Réactions inverses de l'oxydation : l'acide carboxylique ou l'aldéhyde sont réduits en alcool.

## Catégorie de mécanismes

### Substitution nucléophile

Un nucléophile remplace un groupe partant sur un carbone $\delta^+$ :

$$\text{R–X} + \text{Nu}^- \to \text{R–Nu} + \text{X}^-$$

### Addition sur une double liaison

Le nucléophile attaque le carbone $\delta^+$ de la liaison C=O (ou C=C polarisée).

### Élimination

Perte d'une petite molécule (H₂O, HX) avec formation d'une double liaison.

## Notion de sélectivité

Une réaction est **sélective** quand elle agit préférentiellement sur un site réactif parmi plusieurs possibles.
""",
                            "quiz": {
                                "titre": "Quiz — Mécanismes",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "L'oxydation ménagée d'un alcool primaire donne :",
                                        "options": ["Une cétone", "Un aldéhyde", "Un ester", "Un acide aminé"],
                                        "reponse_correcte": "1",
                                        "explication": "Alcool primaire → aldéhyde puis éventuellement acide carboxylique.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Un alcool tertiaire peut être oxydé en cétone.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "Un alcool tertiaire n'a pas d'hydrogène sur le carbone fonctionnel : il ne s'oxyde pas.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.5 : Synthèse organique ────────────────────────
                {
                    "ordre": 5,
                    "titre": "Stratégie de synthèse organique",
                    "description": "Étapes d'une synthèse, rendement, sélectivité et chimie verte.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Stratégie et protocole de synthèse",
                            "duree": 35,
                            "contenu": r"""# Stratégie de synthèse organique

## Étapes d'une synthèse

1. **Transformation** : réaction chimique (chauffage à reflux, etc.).
2. **Traitement** : isolement du produit (extraction, lavage, séchage).
3. **Purification** : élimination des impuretés (recristallisation, distillation, chromatographie).
4. **Analyse** : identification et contrôle de pureté (spectroscopies IR, RMN, point de fusion).

## Chauffage à reflux

Le **reflux** permet de chauffer le milieu réactionnel sans perte de matière. Les vapeurs sont condensées par le réfrigérant et retombent dans le ballon.

## Rendement

$$\eta = \frac{n_{\text{produit obtenu}}}{n_{\text{produit théorique}}} \times 100$$

Le rendement est toujours $\le 100\%$ (pertes, réaction incomplète, réactions parasites).

## Protection de groupe

Quand une molécule possède **plusieurs groupes réactifs**, on peut **protéger** un groupe pour que la réaction n'ait lieu que sur l'autre. Après réaction, on **déprotège**.

## Réaction sélective

On choisit les conditions (réactif, solvant, température, catalyseur) pour favoriser la transformation d'**un seul** groupe caractéristique.

## Chimie verte (12 principes)

Les principes clés :
- **Économie d'atomes** : maximiser l'incorporation des atomes des réactifs dans le produit.
- **Solvants plus sûrs** : eau, solvants non toxiques.
- **Catalyse** : préférer un catalyseur à un réactif stœchiométrique.
- **Réduction des déchets** : concevoir la synthèse pour minimiser les sous-produits.
""",
                            "quiz": {
                                "titre": "Quiz — Synthèse organique",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Le chauffage à reflux permet de :",
                                        "options": [
                                            "Refroidir rapidement le mélange",
                                            "Chauffer sans perte de matière",
                                            "Cristalliser le produit",
                                            "Séparer deux liquides miscibles",
                                        ],
                                        "reponse_correcte": "1",
                                        "explication": "Le reflux chauffe le mélange tout en condensant les vapeurs (pas de perte).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on le rapport entre la quantité de produit obtenu et la quantité théorique, exprimé en pourcentage ?",
                                        "reponse_correcte": "rendement",
                                        "tolerances": ["rendement", "le rendement", "Rendement"],
                                        "explication": "η = (n_obtenu / n_théorique) × 100 est le rendement de la synthèse.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.6 : Eau et environnement (SPÉCIALITÉ) ─────────
                {
                    "ordre": 6,
                    "titre": "Eau et environnement (Spécialité)",
                    "description": "Traceurs chimiques océaniques, érosion, dissolution. Chapitre de spécialité Physique-Chimie.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Traceurs chimiques et cycle de l'eau",
                            "duree": 30,
                            "contenu": r"""# Eau et environnement — *Spécialité*

## Mers et océans : traceurs chimiques

### Salinité

La **salinité** exprime la masse de sels dissous par kilogramme d'eau de mer. Valeur moyenne : $S \approx 35$ g·kg⁻¹.

Les ions majoritaires : Na⁺, Cl⁻, Mg²⁺, SO₄²⁻, Ca²⁺, K⁺.

### Traceurs chimiques

Certaines espèces chimiques servent de **traceurs** pour étudier les courants océaniques et le cycle de l'eau :
- **Température** et **salinité** : identifient les masses d'eau.
- **Isotopes de l'oxygène** ($^{18}$O / $^{16}$O) : traceurs climatiques dans les carottes de glace.
- **pH de l'océan** : environ 8,1, tendance à l'**acidification** par absorption de CO₂.

$$\text{CO}_2 + \text{H}_2\text{O} \rightleftharpoons \text{H}_2\text{CO}_3 \rightleftharpoons \text{HCO}_3^- + \text{H}^+$$

## Érosion et dissolution

### Dissolution du calcaire

$$\text{CaCO}_3(s) + \text{CO}_2(aq) + \text{H}_2\text{O} \to \text{Ca}^{2+}(aq) + 2\,\text{HCO}_3^-(aq)$$

L'eau chargée en CO₂ dissout les roches calcaires → formation de **grottes** et **stalactites/stalagmites**.

### Dureté de l'eau

La **dureté** (titre hydrotimétrique, °TH) mesure la concentration en ions Ca²⁺ et Mg²⁺.

- Eau douce : < 15 °TH
- Eau dure : > 30 °TH

L'eau dure provoque l'**entartrage** des canalisations.
""",
                            "quiz": {
                                "titre": "Quiz — Eau et environnement",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "L'acidification des océans est principalement due à :",
                                        "options": ["L'érosion des roches", "L'absorption de CO₂", "Les rejets industriels", "L'évaporation"],
                                        "reponse_correcte": "1",
                                        "explication": "CO₂ dissous dans l'eau forme H₂CO₃ puis libère H⁺ → baisse du pH.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Quelle grandeur mesure la concentration en ions Ca²⁺ et Mg²⁺ dans l'eau ?",
                                        "reponse_correcte": "dureté",
                                        "tolerances": ["dureté", "durete", "titre hydrotimétrique", "TH", "la dureté"],
                                        "explication": "La dureté (°TH) quantifie les ions Ca²⁺ et Mg²⁺ responsables de l'entartrage.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.7 : Eau et ressources (SPÉCIALITÉ) ────────────
                {
                    "ordre": 7,
                    "titre": "Eau et ressources (Spécialité)",
                    "description": "Traitement des eaux, pile à combustible, production d'énergie. Chapitre de spécialité Physique-Chimie.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Traitement des eaux et production d'énergie",
                            "duree": 35,
                            "contenu": r"""# Eau et ressources — *Spécialité*

## Traitement des eaux

### Potabilisation

Les étapes de traitement de l'eau brute :

1. **Dégrillage** : retrait des gros débris.
2. **Floculation-décantation** : ajout d'un floculant (Al₂(SO₄)₃) → les particules s'agglomèrent et sédimentent.
3. **Filtration** : sur sable pour retenir les particules fines.
4. **Désinfection** : chloration, ozonation ou UV pour éliminer les micro-organismes.

### Contrôle qualité

- pH (entre 6,5 et 9)
- Turbidité
- Concentrations en ions (nitrates < 50 mg/L, etc.)

### Épuration des eaux usées

Traitement biologique : les **bactéries** décomposent la matière organique. Les boues activées sont ensuite séparées par décantation.

## Eau et énergie

### Pile à combustible

La pile à hydrogène produit de l'électricité par **oxydation de H₂** :

- **Anode** : $\text{H}_2 \to 2\,\text{H}^+ + 2\,e^-$ (oxydation)
- **Cathode** : $\frac{1}{2}\text{O}_2 + 2\,\text{H}^+ + 2\,e^- \to \text{H}_2\text{O}$ (réduction)
- **Bilan** : $\text{H}_2 + \frac{1}{2}\text{O}_2 \to \text{H}_2\text{O}$

Le seul sous-produit est l'**eau** → énergie propre (si H₂ est produit de manière renouvelable).

### Électrolyse de l'eau

Réaction inverse de la pile : on fournit de l'énergie électrique pour décomposer l'eau en H₂ et O₂.

$$2\,\text{H}_2\text{O} \xrightarrow{\text{énergie}} 2\,\text{H}_2 + \text{O}_2$$
""",
                            "quiz": {
                                "titre": "Quiz — Eau et ressources",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quel est le sous-produit de la réaction dans une pile à hydrogène ?",
                                        "options": ["CO₂", "H₂O", "O₃", "HCl"],
                                        "reponse_correcte": "1",
                                        "explication": "H₂ + ½O₂ → H₂O : le seul sous-produit est l'eau.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "L'électrolyse de l'eau produit du dihydrogène et du dioxygène.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "2H₂O → 2H₂ + O₂ par apport d'énergie électrique.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.8 : Les matériaux (SPÉCIALITÉ) ────────────────
                {
                    "ordre": 8,
                    "titre": "Les matériaux (Spécialité)",
                    "description": "Tensioactifs, adhésifs, semi-conducteurs et nouveaux matériaux. Chapitre de spécialité Physique-Chimie.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Tensioactifs, adhésifs et semi-conducteurs",
                            "duree": 35,
                            "contenu": r"""# Les matériaux — *Spécialité*

## Tensioactifs

Un **tensioactif** (ou surfactant) est une molécule **amphiphile** : elle possède une partie **hydrophile** (tête polaire) et une partie **hydrophobe** (queue apolaire).

### Applications
- **Savons** : sels d'acide gras (R–COO⁻Na⁺).
- **Détergents** : molécules de synthèse (alkylsulfates, etc.).
- **Émulsifiants** : stabilisent les émulsions eau/huile.

### Micelles

Au-delà de la **concentration micellaire critique** (CMC), les tensioactifs s'organisent en **micelles** : les queues hydrophobes s'orientent vers l'intérieur, les têtes hydrophiles vers l'eau.

## Adhésifs

### Principe d'adhésion

L'adhésion repose sur des **interactions intermoléculaires** entre le matériau et l'adhésif :
- Forces de van der Waals
- Liaisons hydrogène
- Parfois liaisons covalentes (colles époxydes)

### Types de colles
- **Colles thermoplastiques** : ramollissent à la chaleur (colle chaude).
- **Colles thermodurcissables** : durcissent irréversiblement (époxy, résines).
- **Colles à solvant** : le solvant s'évapore, le polymère durcit.

## Semi-conducteurs

### Conducteurs, isolants, semi-conducteurs

- **Conducteur** (métaux) : résistivité faible (ex : Cu, $\rho \approx 10^{-8}$ Ω·m).
- **Isolant** : résistivité très élevée (ex : verre, $\rho > 10^{10}$ Ω·m).
- **Semi-conducteur** : résistivité intermédiaire, diminue avec la température (ex : Si, Ge).

### Dopage

On introduit des **impuretés** dans le silicium pour modifier ses propriétés :
- **Type n** : dopage avec P ou As (electrons en excès).
- **Type p** : dopage avec B ou Al (trous en excès).

La **jonction p-n** est à la base des diodes, transistors et cellules photovoltaïques.

## Nouveaux matériaux

- **Cristaux liquides** : utilisés dans les écrans LCD.
- **Polymères conducteurs** : polyacétylène, polyaniline.
- **Nanomatériaux** : propriétés extraordinaires dues à l'échelle nanométrique.
""",
                            "quiz": {
                                "titre": "Quiz — Matériaux",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Un tensioactif possède :",
                                        "options": [
                                            "Deux parties hydrophiles",
                                            "Deux parties hydrophobes",
                                            "Une partie hydrophile et une partie hydrophobe",
                                            "Aucune partie polaire",
                                        ],
                                        "reponse_correcte": "2",
                                        "explication": "Un tensioactif est amphiphile : tête hydrophile + queue hydrophobe.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on le dopage d'un semi-conducteur avec un élément qui apporte des électrons excédentaires ?",
                                        "reponse_correcte": "type n",
                                        "tolerances": ["type n", "dopage n", "dopage de type n", "n"],
                                        "explication": "Le dopage de type n introduit des électrons en excès (P, As dans Si).",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.9 : Chimie durable et chimie verte ────────────
                {
                    "ordre": 9,
                    "titre": "Chimie durable et chimie verte",
                    "description": "Économie d'atomes, solvants verts, catalyse et développement durable.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Les 12 principes de la chimie verte",
                            "duree": 30,
                            "contenu": r"""# Chimie durable et chimie verte

## Contexte

La chimie industrielle traditionnelle génère des **déchets**, utilise des **solvants toxiques** et des **réactifs dangereux**. La **chimie verte** (ou chimie durable) vise à concevoir des procédés plus respectueux de l'environnement.

## Les 12 principes de la chimie verte (Anastas & Warner, 1998)

1. **Prévention des déchets** : mieux vaut ne pas produire de déchets que de les traiter.
2. **Économie d'atomes** : maximiser l'incorporation des atomes des réactifs dans le produit final.
3. **Synthèses moins dangereuses** : utiliser des réactifs peu toxiques.
4. **Conception de produits plus sûrs** : les produits doivent être non toxiques.
5. **Solvants et auxiliaires plus sûrs** : préférer l'eau, les fluides supercritiques, ou s'en passer.
6. **Efficacité énergétique** : conduire les réactions à température et pression ambiantes.
7. **Matières premières renouvelables** : biomasse plutôt que pétrole.
8. **Réduction des dérivés** : éviter les groupes protecteurs quand possible.
9. **Catalyse** : préférer un catalyseur (récupérable) à un réactif stœchiométrique.
10. **Conception dégradable** : les produits doivent se décomposer en fin de vie.
11. **Analyse en temps réel** : surveiller le procédé pour éviter la formation de sous-produits.
12. **Chimie intrinsèquement plus sûre** : minimiser les risques d'accidents.

## Économie d'atomes

$$\text{EA} = \frac{M_{\text{produit désiré}}}{\sum M_{\text{tous les produits}}} \times 100$$

Plus EA est élevée, moins il y a de sous-produits.

**Exemple :** une réaction d'**addition** a une EA de 100 % (tous les atomes sont dans le produit). Une **substitution** génère un sous-produit → EA < 100 %.

## Valorisation du CO₂

Le CO₂, déchet de la combustion, peut être **valorisé** :
- Synthèse de carbonates cycliques
- Production de méthanol
- Minéralisation
""",
                            "quiz": {
                                "titre": "Quiz — Chimie verte",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Une réaction d'addition a une économie d'atomes de :",
                                        "options": ["0 %", "50 %", "75 %", "100 %"],
                                        "reponse_correcte": "3",
                                        "explication": "En addition, tous les atomes des réactifs se retrouvent dans le produit → EA = 100 %.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La chimie verte préconise l'utilisation de réactifs stœchiométriques plutôt que des catalyseurs.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "Au contraire, la chimie verte préfère la catalyse (principe n°9).",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.10 : Dosages par étalonnage et contrôle qualité
                {
                    "ordre": 10,
                    "titre": "Dosages par étalonnage et contrôle qualité",
                    "description": "Dosage spectrophotométrique, conductimétrique, contrôle qualité.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Dosage par étalonnage spectrophotométrique",
                            "duree": 30,
                            "contenu": r"""# Dosages par étalonnage

## Principe du dosage par étalonnage

On mesure une **grandeur physique** (absorbance, conductivité, etc.) pour des solutions de **concentrations connues** (solutions étalons). On trace une **droite d'étalonnage**, puis on détermine la concentration inconnue par lecture graphique.

## Dosage spectrophotométrique

### Rappel : loi de Beer-Lambert

$$A = \varepsilon \cdot \ell \cdot c$$

L'absorbance $A$ est **proportionnelle** à la concentration $c$ → la courbe d'étalonnage est une **droite** passant par l'origine.

### Protocole

1. Préparer des solutions étalons de concentrations $c_1, c_2, \ldots, c_n$.
2. Mesurer l'absorbance $A$ de chaque solution au spectrophotomètre (à $\lambda_{\max}$).
3. Tracer $A = f(c)$ → droite d'étalonnage.
4. Mesurer l'absorbance de la solution inconnue et lire $c$ sur la droite.

## Dosage conductimétrique

### Conductivité

$$\sigma = \sum \lambda_i \cdot [X_i]$$

$\lambda_i$ : conductivité molaire ionique de l'ion $X_i$ (S·m²·mol⁻¹).

La conductivité dépend de la **nature** et de la **concentration** des ions en solution.

### Étalonnage conductimétrique

Même principe que le dosage spectrophotométrique, mais on mesure la conductivité $\sigma$ à la place de l'absorbance.

## Contrôle qualité

Le **contrôle qualité** vérifie qu'un produit (alimentaire, pharmaceutique, cosmétique) respecte les **normes** en vigueur :
- Concentration en principe actif (médicament)
- Taux de sucre, d'acidité (alimentaire)
- Pureté d'un réactif

Le dosage par étalonnage est une méthode **non destructive** (on ne modifie pas la solution analysée, contrairement au titrage).
""",
                            "quiz": {
                                "titre": "Quiz — Dosage par étalonnage",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La droite d'étalonnage A = f(c) passe par l'origine car :",
                                        "options": [
                                            "A est toujours nulle",
                                            "A = ε·ℓ·c (proportionnalité)",
                                            "La cuve est vide",
                                            "Le spectrophotomètre est défectueux",
                                        ],
                                        "reponse_correcte": "1",
                                        "explication": "D'après Beer-Lambert, si c = 0 alors A = 0 : proportionnalité directe.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Le dosage par étalonnage est une méthode destructive.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "Le dosage par étalonnage est non destructif : la solution n'est pas modifiée.",
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
                # ── Ch.1 : Vocabulaire de la Logique et Révisions Algébriques ──
                {
                    "ordre": 1,
                    "titre": "Vocabulaire de la Logique et Révisions Algébriques",
                    "description": "Logique mathématique, connecteurs, implications, raisonnement par récurrence et polynômes du second degré.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Introduction à la Logique Mathématique",
                            "duree": 25,
                            "contenu": r"""# Introduction à la Logique Mathématique

## Définition d'une proposition

Une **proposition** est un énoncé mathématique auquel on peut attribuer une valeur de vérité unique : il est soit **vrai**, soit **faux**.

**Exemple :** Considérons un quadrilatère $ABCD$ dans le plan.
- $P$ : « $ABCD$ est un carré »
- $Q$ : « $ABCD$ est un parallélogramme »

Selon la nature géométrique de $ABCD$, ces propositions possèdent une valeur de vérité (V ou F).

## La Négation d'une proposition

La négation d'une proposition $P$ est notée $\bar{P}$ (ou « non $P$ »). Par définition, elle est **fausse** quand $P$ est vraie, et **vraie** quand $P$ est fausse.

**Propriété :** La négation de la négation est la proposition originale : $P \equiv \bar{\bar{P}}$.

### Exemples de négations

| Proposition | Négation |
|---|---|
| $x > 2$ | $x \le 2$ |
| Pour tout réel $x$ : $0 \le x^2$ | Il existe un réel $x$ tel que $0 > x^2$ |
| $n$ est pair | $n$ est impair |

### Négation des quantificateurs

- La négation de « $\forall x \in E, P(x)$ » est « $\exists x \in E, \overline{P(x)}$ »
- La négation de « $\exists x \in E, P(x)$ » est « $\forall x \in E, \overline{P(x)}$ »
""",
                            "quiz": {
                                "titre": "Quiz — Logique Mathématique",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "vrai_faux",
                                        "texte": "La négation de « x > 2 » est « x < 2 ».",
                                        "reponse_correcte": "faux",
                                        "explication": "La négation de « x > 2 » est « x ≤ 2 » (et non x < 2, car il faut inclure l'égalité).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Quelle est la négation de « Pour tout réel x, x² ≥ 0 » ?",
                                        "options": ["Pour tout réel x, x² < 0", "Il existe un réel x tel que x² < 0", "Il existe un réel x tel que x² ≤ 0", "Pour tout réel x, x² > 0"],
                                        "reponse_correcte": "1",
                                        "explication": "La négation de ∀x P(x) est ∃x ¬P(x). Donc : il existe un réel x tel que x² < 0.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La double négation d'une proposition P redonne P.",
                                        "reponse_correcte": "vrai",
                                        "explication": "C'est la propriété fondamentale : P ≡ non(non P).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Connecteurs Logiques et Opérations sur les Ensembles",
                            "duree": 30,
                            "contenu": r"""# Connecteurs Logiques et Opérations sur les Ensembles

## Conjonction (« Et ») et Intersection

La proposition $P \wedge Q$ est vraie uniquement si $P$ **et** $Q$ sont simultanément vraies.

**Lien avec les ensembles :** Si $P$ représente $x \in I$ et $Q$ représente $x \in J$, alors $P \wedge Q$ équivaut à $x \in I \cap J$.

## Disjonction (« Ou ») et Union

En mathématiques, le « ou » est **inclusif**. La proposition $P \vee Q$ est vraie si **au moins l'une** des deux propositions est vraie.

**Lien avec les ensembles :** $P \vee Q$ équivaut à $x \in I \cup J$.

## Les Lois de Morgan

Ces lois fondamentales permettent de distribuer la négation sur les connecteurs :

$$\overline{P \vee Q} \equiv \bar{P} \wedge \bar{Q}$$

$$\overline{P \wedge Q} \equiv \bar{P} \vee \bar{Q}$$

Pour les ensembles $F$ et $G$ : $\overline{F \cup G} = \bar{F} \cap \bar{G}$ et $\overline{F \cap G} = \bar{F} \cup \bar{G}$.

## Propriétés des opérations

| Propriété | Ensembles | Propositions |
|---|---|---|
| Commutativité | $F \cap G = G \cap F$ | $P \wedge Q \equiv Q \wedge P$ |
| Associativité | $F \cap (G \cap H) = (F \cap G) \cap H$ | $P \wedge (Q \wedge R) \equiv (P \wedge Q) \wedge R$ |
| Distributivité | $F \cap (G \cup H) = (F \cap G) \cup (F \cap H)$ | $P \wedge (Q \vee R) \equiv (P \wedge Q) \vee (P \wedge R)$ |
| Élément neutre | $F \cap \Omega = F$ ; $F \cup \emptyset = F$ | $P \wedge \text{Vrai} \equiv P$ ; $P \vee \text{Faux} \equiv P$ |
""",
                            "quiz": {
                                "titre": "Quiz — Connecteurs Logiques",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Selon les lois de Morgan, la négation de (P ∨ Q) est :",
                                        "options": ["P̄ ∨ Q̄", "P̄ ∧ Q̄", "P ∧ Q", "P ∨ Q̄"],
                                        "reponse_correcte": "1",
                                        "explication": "La loi de Morgan donne : la négation de (P ∨ Q) est (P̄ ∧ Q̄).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "En mathématiques, le « ou » est exclusif.",
                                        "reponse_correcte": "faux",
                                        "explication": "En mathématiques, le « ou » est inclusif : P ∨ Q est vrai si au moins l'un des deux est vrai.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Si P correspond à x ∈ I et Q correspond à x ∈ J, alors (P ∧ Q) correspond à :",
                                        "options": ["x ∈ I ∪ J", "x ∈ I ∩ J", "x ∉ I ∩ J", "x ∈ I ∖ J"],
                                        "reponse_correcte": "1",
                                        "explication": "La conjonction (ET) correspond à l'intersection des ensembles.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Implications et Équivalences",
                            "duree": 30,
                            "contenu": r"""# Implications et Équivalences

## L'implication $P \Rightarrow Q$

L'implication « si $P$, alors $Q$ » est définie logiquement par $(Q \vee \bar{P})$.

- **Condition suffisante :** $P$ est une condition suffisante pour $Q$.
- **Condition nécessaire :** $Q$ est une condition nécessaire pour $P$.

**Exemple :** Soit $P$ : « $ABCD$ est un carré » et $Q$ : « $ABCD$ est un parallélogramme ». On a $P \Rightarrow Q$.
Être un carré est **suffisant** pour être un parallélogramme. Être un parallélogramme est **nécessaire** pour être un carré.

### Structures de preuve

- **Modus Ponens :** Si $P$ vraie et $P \Rightarrow Q$ vraie, alors $Q$ vraie.
- **Modus Tollens :** Si $Q$ fausse et $P \Rightarrow Q$ vraie, alors $P$ fausse (raisonnement par l'absurde).

## Réciproque et Contraposée

Soit l'implication $P \Rightarrow Q$ :

- **Réciproque :** $Q \Rightarrow P$ — elle n'est **pas nécessairement** vraie.
- **Contraposée :** $\bar{Q} \Rightarrow \bar{P}$ — elle est **rigoureusement équivalente** à l'implication initiale.

**Démonstration :**
1. $P \Rightarrow Q \equiv (\bar{P} \vee Q)$
2. $\bar{Q} \Rightarrow \bar{P} \equiv (Q \vee \bar{P})$

Par commutativité du « ou », les deux expressions sont identiques.

**Exemple :** Démontrer que « si $n^2$ est impair, alors $n$ est impair ».
Par contraposition : « si $n$ est pair, alors $n^2$ est pair ».
Si $n = 2k$, alors $n^2 = 4k^2 = 2(2k^2)$, qui est pair. ✓

## L'équivalence $P \Leftrightarrow Q$

L'équivalence (« si et seulement si ») est vraie lorsque l'implication **et** sa réciproque sont toutes deux vraies.
""",
                            "quiz": {
                                "titre": "Quiz — Implications et Équivalences",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La contraposée de P ⇒ Q est :",
                                        "options": ["Q ⇒ P", "Q̄ ⇒ P̄", "P̄ ⇒ Q̄", "P ⇒ Q̄"],
                                        "reponse_correcte": "1",
                                        "explication": "La contraposée de P ⇒ Q est Q̄ ⇒ P̄.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La réciproque d'une implication vraie est toujours vraie.",
                                        "reponse_correcte": "faux",
                                        "explication": "La réciproque n'est pas nécessairement vraie. Exemple : tout carré est un parallélogramme, mais tout parallélogramme n'est pas un carré.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Dans P ⇒ Q, P est appelée :",
                                        "options": ["Condition nécessaire", "Condition suffisante", "Condition nécessaire et suffisante", "Contraposée"],
                                        "reponse_correcte": "1",
                                        "explication": "P est une condition suffisante pour Q. Q est une condition nécessaire pour P.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "Raisonnement par Récurrence",
                            "duree": 30,
                            "contenu": r"""# Méthodologie du Raisonnement par Récurrence

## Principe et Axiome

Le raisonnement par récurrence est un pilier de l'arithmétique. Fondé sur les **axiomes de Peano**, il stipule que si une propriété se transmet d'un rang au suivant et est vérifiée initialement, elle appartient à tout l'ensemble $\mathbb{N}$.

**Analogie des dominos :** faire tomber le premier ($n_0$) garantit la chute de tous les suivants si chaque domino fait tomber son successeur.

## Étapes de la démonstration

1. **Initialisation :** Vérifier que $P_{n_0}$ est vraie.
2. **Hérédité :** Supposer $P_k$ vraie pour un entier $k \ge n_0$. Démontrer alors que $P_{k+1}$ est vraie.

## Exemple : Somme des cubes

Montrons que $\forall n \in \mathbb{N}^*$ :

$$1^3 + 2^3 + \dots + n^3 = \left(\frac{n(n+1)}{2}\right)^2$$

**Initialisation :** Pour $n = 1$ : $1^3 = 1$ et $\left(\frac{1 \times 2}{2}\right)^2 = 1$. ✓

**Hérédité :** Supposons $P_k$ vraie. Alors :

$$\sum_{i=1}^{k+1} i^3 = \left(\frac{k(k+1)}{2}\right)^2 + (k+1)^3 = (k+1)^2\left(\frac{k^2}{4} + (k+1)\right)$$

$$= (k+1)^2 \cdot \frac{k^2 + 4k + 4}{4} = \frac{(k+1)^2(k+2)^2}{4} = \left(\frac{(k+1)(k+2)}{2}\right)^2$$

L'expression obtenue est bien $\left(\frac{(k+1)(k+2)}{2}\right)^2$. La propriété est héréditaire. ✓
""",
                            "quiz": {
                                "titre": "Quiz — Raisonnement par Récurrence",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quelles sont les deux étapes d'un raisonnement par récurrence ?",
                                        "options": ["Hypothèse et conclusion", "Initialisation et hérédité", "Analyse et synthèse", "Nécessité et suffisance"],
                                        "reponse_correcte": "1",
                                        "explication": "Le raisonnement par récurrence comporte une initialisation (vérification au premier rang) et une hérédité (transmission au rang suivant).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Si l'hérédité est vérifiée mais pas l'initialisation, la propriété est vraie pour tout n.",
                                        "reponse_correcte": "faux",
                                        "explication": "Les deux étapes sont indispensables. Sans initialisation, la récurrence ne prouve rien.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Que vaut 1³ + 2³ + 3³ + 4³ ?",
                                        "reponse_correcte": "100",
                                        "tolerances": ["100"],
                                        "explication": "1 + 8 + 27 + 64 = 100. On peut aussi utiliser la formule : (4×5/2)² = 10² = 100.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "Polynômes du Second Degré",
                            "duree": 30,
                            "contenu": r"""# Révisions : Polynômes du Second Degré

## Forme Canonique et Discriminant

Tout trinôme $f(x) = ax^2 + bx + c$ ($a \neq 0$) peut s'écrire sous sa **forme canonique** :

$$f(x) = a\left[\left(x + \frac{b}{2a}\right)^2 - \frac{\Delta}{4a^2}\right]$$

où le **discriminant** est : $\Delta = b^2 - 4ac$.

## Résolution et Factorisation

| Signe de $\Delta$ | Racines | Forme factorisée |
|---|---|---|
| $\Delta > 0$ | $x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a}$ | $a(x - x_1)(x - x_2)$ |
| $\Delta = 0$ | $x_0 = -\frac{b}{2a}$ (racine double) | $a(x - x_0)^2$ |
| $\Delta < 0$ | Aucune racine réelle | Pas de factorisation |

## Étude du Signe

- Si $\Delta > 0$ : le trinôme est du **signe de $a$** à l'extérieur des racines et du signe de $-a$ entre les racines.
- Si $\Delta \le 0$ : le trinôme est **toujours du signe de $a$** (ou nul en $x_0$).

## Variations

La courbe est une parabole de sommet $S\left(-\frac{b}{2a} ; f\left(-\frac{b}{2a}\right)\right)$.

- Si $a > 0$ : décroissante puis croissante (parabole tournée vers le haut).
- Si $a < 0$ : croissante puis décroissante (parabole tournée vers le bas).

## Relations de Viète

Pour un trinôme possédant deux racines $x_1$ et $x_2$ :

$$x_1 + x_2 = -\frac{b}{a} \quad \text{et} \quad x_1 \cdot x_2 = \frac{c}{a}$$

Deux nombres de somme $S$ et de produit $P$ sont les solutions de : $x^2 - Sx + P = 0$.
""",
                            "quiz": {
                                "titre": "Quiz — Polynômes du Second Degré",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quel est le discriminant du trinôme 2x² − 3x + 1 ?",
                                        "reponse_correcte": "1",
                                        "tolerances": ["1"],
                                        "explication": "Δ = b² − 4ac = (−3)² − 4×2×1 = 9 − 8 = 1.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Si Δ < 0, combien de racines réelles possède le trinôme ?",
                                        "options": ["0", "1", "2", "Une infinité"],
                                        "reponse_correcte": "0",
                                        "explication": "Si Δ < 0, le trinôme n'admet aucune racine réelle.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Quelle est la somme des racines de x² − 5x + 6 = 0 ?",
                                        "options": ["5", "6", "−5", "−6"],
                                        "reponse_correcte": "0",
                                        "explication": "Par les relations de Viète : x₁ + x₂ = −b/a = −(−5)/1 = 5.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.2 : Les Suites Numériques ───────────────────────
                {
                    "ordre": 2,
                    "titre": "Les Suites Numériques",
                    "description": "Modes de génération, propriétés globales, suites arithmétiques et géométriques, limites, matrices colonnes.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Introduction et Modes de Génération",
                            "duree": 30,
                            "contenu": r"""# Introduction et Modes de Génération

## Définitions et Vocabulaire

Une **suite numérique** est une fonction définie sur $\mathbb{N}$ (ou une partie) à valeurs dans $\mathbb{R}$.

- **Notation :** $(u_n)_{n \in \mathbb{N}}$ désigne la suite, $u_n$ est le **terme de rang** $n$.

## Modes de définition

### Définition explicite

$u_n$ est exprimé directement en fonction de $n$ : $u_n = f(n)$.

**Exemple :** $u_n = \frac{n^2}{n+1}$ pour $n \in \mathbb{N}$.

### Définition par récurrence

Le terme $u_{n+1}$ est défini en fonction de $u_n$ : $u_{n+1} = f(u_n)$, avec la donnée d'un premier terme $u_0$.

## Le Raisonnement par Récurrence (rappel)

Pour démontrer qu'une propriété $P_n$ est vraie pour tout $n \ge n_0$ :

1. **Initialisation :** Vérifier $P_{n_0}$.
2. **Hérédité :** Supposer $P_k$ vraie, démontrer $P_{k+1}$.
3. **Conclusion :** La propriété est vraie pour tout $n \ge n_0$.

### Exemple : Inégalité de Bernoulli

Pour tout $\alpha \ge -1$ et pour tout $n \in \mathbb{N}$ :

$$(1 + \alpha)^n \ge 1 + n\alpha$$

Lors de l'hérédité, la multiplication par $(1+\alpha)$ préserve le sens car $1+\alpha \ge 0$.
""",
                            "quiz": {
                                "titre": "Quiz — Introduction aux Suites",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quelle est la définition d'une suite définie par récurrence ?",
                                        "options": ["u_n = f(n)", "u_{n+1} = f(u_n) avec u_0 donné", "u_n = u_0 + nr", "u_n = u_0 × qⁿ"],
                                        "reponse_correcte": "1",
                                        "explication": "Une suite par récurrence est définie via u_{n+1} = f(u_n) avec un premier terme u_0.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "L'inégalité de Bernoulli affirme que (1+α)ⁿ ≥ 1+nα pour tout α ≥ −1.",
                                        "reponse_correcte": "vrai",
                                        "explication": "C'est l'inégalité de Bernoulli, valable pour α ≥ −1 et n ∈ ℕ.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Combien d'étapes comporte un raisonnement par récurrence ?",
                                        "reponse_correcte": "2",
                                        "tolerances": ["2", "deux", "3", "trois"],
                                        "explication": "Il comporte 2 étapes essentielles : initialisation et hérédité (plus la conclusion).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Propriétés Globales des Suites",
                            "duree": 25,
                            "contenu": r"""# Propriétés Globales des Suites

## Vocabulaire de l'ordre

Soit $(u_n)$ une suite définie pour tout $n \in \mathbb{N}$.

- **Suite majorée :** $\exists M \in \mathbb{R},\ \forall n \in \mathbb{N},\ u_n \le M$
- **Suite minorée :** $\exists m \in \mathbb{R},\ \forall n \in \mathbb{N},\ u_n \ge m$
- **Suite bornée :** elle est à la fois majorée et minorée.

## Sens de variation (Monotonie)

Deux méthodes principales :

### Étude du signe de la différence
Si $u_{n+1} - u_n \ge 0$ pour tout $n$, la suite est **croissante**.

### Comparaison du quotient à 1
Pour une suite à termes **strictement positifs** ($u_n > 0$) :
- Si $\frac{u_{n+1}}{u_n} \ge 1$ : suite croissante
- Si $\frac{u_{n+1}}{u_n} \le 1$ : suite décroissante

## Représentation graphique

Pour une suite $u_{n+1} = f(u_n)$, on utilise la courbe $\mathcal{C}_f$ et la droite $\Delta : y = x$ :

1. Placer $u_0$ sur l'axe des abscisses
2. Rejoindre verticalement $\mathcal{C}_f$ pour obtenir $u_1$ en ordonnée
3. Rejoindre horizontalement $\Delta$ pour reporter $u_1$ sur l'axe des abscisses
4. Répéter (construction en « escalier » ou en « spirale »)
""",
                            "quiz": {
                                "titre": "Quiz — Propriétés des Suites",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Une suite est bornée si elle est :",
                                        "options": ["Croissante et majorée", "Majorée et minorée", "Convergente", "Monotone"],
                                        "reponse_correcte": "1",
                                        "explication": "Une suite bornée est une suite à la fois majorée et minorée.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Pour montrer qu'une suite à termes positifs est croissante, on peut vérifier que :",
                                        "options": ["u_{n+1}/u_n ≤ 1", "u_{n+1}/u_n ≥ 1", "u_{n+1} − u_n < 0", "u_n → +∞"],
                                        "reponse_correcte": "1",
                                        "explication": "Si le quotient u_{n+1}/u_n ≥ 1, la suite à termes positifs est croissante.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La représentation graphique d'une suite récurrente utilise la droite y = x.",
                                        "reponse_correcte": "vrai",
                                        "explication": "On utilise la courbe de f et la droite y = x (bissectrice) pour la construction escalier/spirale.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Suites Arithmétiques et Géométriques",
                            "duree": 30,
                            "contenu": r"""# Suites Arithmétiques et Géométriques

## Suite arithmétique

| Propriété | Formule |
|---|---|
| Relation de récurrence | $u_{n+1} = u_n + r$ |
| Terme général | $u_n = u_0 + nr$ |
| Somme des $n+1$ premiers termes | $S_n = \frac{(n+1)(u_0 + u_n)}{2}$ |
| Convergence | Diverge vers $\pm\infty$ si $r \neq 0$ |

## Suite géométrique

| Propriété | Formule |
|---|---|
| Relation de récurrence | $u_{n+1} = q \times u_n$ |
| Terme général | $u_n = u_0 \times q^n$ |
| Somme des $n+1$ premiers termes | $S_n = u_0 \cdot \frac{1 - q^{n+1}}{1 - q}$ (si $q \neq 1$) |
| Convergence | Converge vers 0 si $|q| < 1$ |

## Formule utile

$$\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$$
""",
                            "quiz": {
                                "titre": "Quiz — Suites Arithmétiques et Géométriques",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Si (u_n) est arithmétique de raison 3 avec u_0 = 2, que vaut u_5 ?",
                                        "reponse_correcte": "17",
                                        "tolerances": ["17"],
                                        "explication": "u_5 = u_0 + 5×r = 2 + 5×3 = 17.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Une suite géométrique de raison q converge vers 0 si :",
                                        "options": ["|q| > 1", "|q| = 1", "|q| < 1", "q = 0"],
                                        "reponse_correcte": "2",
                                        "explication": "Une suite géométrique converge vers 0 si et seulement si |q| < 1.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Que vaut la somme 1 + 2 + 3 + ... + 10 ?",
                                        "reponse_correcte": "55",
                                        "tolerances": ["55"],
                                        "explication": "S = 10×11/2 = 55.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "Limites et Théorèmes de Convergence",
                            "duree": 30,
                            "contenu": r"""# Limites et Théorèmes de Convergence

## Définition de la convergence

Une suite $(u_n)$ **converge** vers un réel $l$ si tout intervalle ouvert contenant $l$ contient tous les termes de la suite à partir d'un certain rang :

$$\lim_{n \to +\infty} u_n = l$$

## Théorème des Gendarmes

Si $v_n \le u_n \le w_n$ à partir d'un certain rang et si :

$$\lim_{n \to +\infty} v_n = \lim_{n \to +\infty} w_n = l$$

alors $\lim_{n \to +\infty} u_n = l$.

## Comparaison à l'infini

Si $u_n \ge v_n$ et $\lim_{n \to +\infty} v_n = +\infty$, alors $\lim_{n \to +\infty} u_n = +\infty$.

## Théorème de convergence monotone

- Toute suite **croissante et majorée** converge.
- Toute suite **décroissante et minorée** converge.

## Suites adjacentes

Deux suites $(u_n)$ et $(v_n)$ sont **adjacentes** si :
- $(u_n)$ est croissante
- $(v_n)$ est décroissante
- $\lim_{n \to +\infty} (v_n - u_n) = 0$

**Propriété :** Elles convergent vers une limite commune $l$ telle que $\forall n \in \mathbb{N},\ u_n \le l \le v_n$.
""",
                            "quiz": {
                                "titre": "Quiz — Limites de Suites",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Toute suite croissante et majorée :",
                                        "options": ["Diverge", "Converge", "Est bornée mais peut diverger", "Tend vers +∞"],
                                        "reponse_correcte": "1",
                                        "explication": "Le théorème de convergence monotone assure qu'une suite croissante et majorée converge.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Le théorème des gendarmes nécessite que les deux suites encadrantes aient la même limite.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Il faut que v_n et w_n tendent vers la même limite l pour conclure que u_n → l.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Deux suites adjacentes convergent vers :",
                                        "options": ["Deux limites différentes", "Une limite commune", "+∞", "0"],
                                        "reponse_correcte": "1",
                                        "explication": "Par définition, deux suites adjacentes convergent vers une même limite l.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "Suites de Matrices Colonnes",
                            "duree": 30,
                            "contenu": r"""# Suites de Matrices Colonnes

## Modèle $U_{n+1} = AU_n + B$

Soit $(U_n)$ une suite de matrices colonnes.

### Cas homogène ($B = 0$)

$$U_{n+1} = AU_n \implies U_n = A^n U_0$$

### Cas général ($B \neq 0$)

1. On cherche l'**état stable** (point fixe) $\Omega$ tel que $\Omega = A\Omega + B$.
2. On résout $(I - A)\Omega = B$ pour obtenir $\Omega$.
3. On pose $V_n = U_n - \Omega$, ce qui donne la suite géométrique : $V_n = A^n V_0$.
4. **Terme général :** $U_n = A^n(U_0 - \Omega) + \Omega$.

## Suites couplées

Le formalisme matriciel résout les systèmes de suites.

**Exemple :** si $u_{n+1} = 3u_n - v_n$ et $v_{n+1} = -2u_n + 2v_n$, on pose :

$$U_n = \begin{pmatrix} u_n \\ v_n \end{pmatrix},\quad A = \begin{pmatrix} 3 & -1 \\ -2 & 2 \end{pmatrix}$$

d'où $U_n = A^n U_0$.

## Recherche de l'état stable

Pour trouver $\Omega$, résoudre $(I-A)\Omega = B$ :
- Si $(I-A)$ est inversible : $\Omega = (I-A)^{-1}B$.
""",
                            "quiz": {
                                "titre": "Quiz — Suites Matricielles",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Dans le modèle U_{n+1} = AU_n (cas homogène), que vaut U_n en fonction de A et U_0 ?",
                                        "reponse_correcte": "A^n U_0",
                                        "tolerances": ["A^n U_0", "A^nU_0", "AⁿU₀"],
                                        "explication": "Par récurrence immédiate : U_n = A^n U_0.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "L'état stable Ω est solution de :",
                                        "options": ["Ω = AΩ", "Ω = AΩ + B", "(I−A)Ω = 0", "Ω = A⁻¹B"],
                                        "reponse_correcte": "1",
                                        "explication": "L'état stable vérifie Ω = AΩ + B, ce qui donne (I−A)Ω = B.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Les suites couplées peuvent se résoudre en posant U_n comme vecteur colonne.",
                                        "reponse_correcte": "vrai",
                                        "explication": "On regroupe les termes en un vecteur colonne U_n et la relation devient U_{n+1} = AU_n.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 6,
                            "titre": "Exercices d'Application Typiques",
                            "duree": 25,
                            "contenu": r"""# Exercices d'Application — Méthodes

## Méthode 1 : Raisonnement par l'absurde

**Énoncé :** Démontrer que pour tout $n \in \mathbb{N}$, $6n+5$ n'est pas divisible par 3.

1. **Supposition :** Supposons qu'il existe $n$ tel que 3 divise $6n+5$.
2. **Traduction :** $\exists k \in \mathbb{Z},\ 6n+5 = 3k$.
3. **Contradiction :** $5 = 3k - 6n = 3(k-2n)$, donc 3 diviserait 5 — **absurde**.
4. **Conclusion :** $6n+5$ n'est jamais divisible par 3.

## Méthode 2 : Étude de parité et périodicité

Soit $f(x) = \cos(2x) - \frac{1}{2}$.

- **Parité :** $f(-x) = \cos(-2x) - \frac{1}{2} = f(x)$ → fonction **paire**.
- **Périodicité :** $f(x+\pi) = \cos(2x+2\pi) - \frac{1}{2} = f(x)$ → $\pi$-périodique.

## Méthode 3 : Résolution par matrices

Pour l'état stable $\Omega$ du système $U_{n+1} = AU_n + B$ :

1. Poser $(I-A)\Omega = B$
2. Si $(I-A)$ inversible : $\Omega = (I-A)^{-1}B$
3. Cette limite représente les valeurs vers lesquelles tendent les suites couplées.
""",
                            "quiz": {
                                "titre": "Quiz — Méthodes sur les Suites",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Le raisonnement par l'absurde consiste à :",
                                        "options": ["Vérifier tous les cas", "Supposer le contraire et aboutir à une contradiction", "Raisonner par récurrence", "Utiliser la contraposée"],
                                        "reponse_correcte": "1",
                                        "explication": "On suppose la négation de ce qu'on veut prouver et on montre que cela mène à une contradiction.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "f(x) = cos(2x) est π-périodique.",
                                        "reponse_correcte": "vrai",
                                        "explication": "cos(2(x+π)) = cos(2x+2π) = cos(2x), donc f est bien π-périodique.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "6×4+5 = 29. Est-ce que 29 est divisible par 3 ?",
                                        "reponse_correcte": "non",
                                        "tolerances": ["non", "Non", "NON"],
                                        "explication": "29/3 = 9 reste 2. Donc 29 n'est pas divisible par 3, conformément au résultat démontré.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.3 : Limites et Continuité des Fonctions ──────────
                {
                    "ordre": 3,
                    "titre": "Limites et Continuité des Fonctions",
                    "description": "Limites de fonctions, formes indéterminées, théorèmes de comparaison, continuité, TVI et convexité.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Rappels de Logique et Ensembles",
                            "duree": 20,
                            "contenu": r"""# Rappels de Logique et Ensembles

## Définitions fondamentales

- **Proposition :** Énoncé mathématique soit vrai, soit faux.
- **Négation :** $\bar{P}$ ou $\neg P$, fausse quand $P$ est vraie et vice versa.
- **Équivalence :** $P \iff Q$ signifie $P \implies Q$ et $Q \implies P$.

## Lois de Morgan

$$\neg(P \vee Q) \iff (\neg P \wedge \neg Q)$$
$$\neg(P \wedge Q) \iff (\neg P \vee \neg Q)$$

## Raisonnement par récurrence (rappel)

1. **Initialisation :** Vérifier $P_{n_0}$.
2. **Hérédité :** $P_k \implies P_{k+1}$ pour tout $k \ge n_0$.

Sans l'initialisation, le mécanisme de transmission ne démarre pas.
""",
                            "quiz": {
                                "titre": "Quiz — Rappels Logique",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "vrai_faux",
                                        "texte": "P ⟺ Q signifie que P ⟹ Q et Q ⟹ P sont toutes deux vraies.",
                                        "reponse_correcte": "vrai",
                                        "explication": "L'équivalence est la conjonction d'une implication et de sa réciproque.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "La négation de (P ∧ Q) est :",
                                        "options": ["¬P ∧ ¬Q", "¬P ∨ ¬Q", "P ∨ Q", "¬P ∧ Q"],
                                        "reponse_correcte": "1",
                                        "explication": "Par la loi de Morgan : ¬(P ∧ Q) ⟺ (¬P ∨ ¬Q).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Limites de Fonctions : Fondements",
                            "duree": 30,
                            "contenu": r"""# Limites de Fonctions : Fondements

## Limite en $+\infty$

$f(x)$ a pour limite $L$ en $+\infty$ si, pour tout intervalle ouvert contenant $L$, toutes les valeurs de $f(x)$ finissent par appartenir à cet intervalle pour $x$ suffisamment grand :

$$\lim_{x \to +\infty} f(x) = L$$

## Limite en un réel $a$

$$\lim_{x \to a} f(x) = L$$

signifie que $f(x)$ devient arbitrairement proche de $L$ lorsque $x$ tend vers $a$.

## Synthèse des comportements

| Type de limite | Notation | Conséquence graphique |
|---|---|---|
| Finie à l'infini | $\lim_{x \to \pm\infty} f(x) = L$ | Asymptote horizontale $y = L$ |
| Infinie à l'infini | $\lim_{x \to \pm\infty} f(x) = \pm\infty$ | Branche infinie |
| Infinie en un point | $\lim_{x \to a} f(x) = \pm\infty$ | Asymptote verticale $x = a$ |

## Convergence matricielle

Pour une suite de vecteurs colonnes $U_n = \begin{pmatrix} u_n \\ v_n \end{pmatrix}$ :

$$\lim_{n \to +\infty} U_n = \begin{pmatrix} L_1 \\ L_2 \end{pmatrix} \iff \lim u_n = L_1 \text{ et } \lim v_n = L_2$$
""",
                            "quiz": {
                                "titre": "Quiz — Limites de Fonctions",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Si lim(x→+∞) f(x) = 3, quelle est la conséquence graphique ?",
                                        "options": ["Asymptote verticale x = 3", "Asymptote horizontale y = 3", "Point d'inflexion en x = 3", "Maximum en x = 3"],
                                        "reponse_correcte": "1",
                                        "explication": "Une limite finie en ±∞ correspond à une asymptote horizontale.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Si lim(x→2) f(x) = +∞, alors x = 2 est :",
                                        "options": ["Une asymptote horizontale", "Une asymptote verticale", "Un point d'inflexion", "Un extremum"],
                                        "reponse_correcte": "1",
                                        "explication": "Une limite infinie en un point réel correspond à une asymptote verticale.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La convergence d'un vecteur colonne se fait composante par composante.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Un vecteur converge ssi chacune de ses composantes converge.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Opérations et Levée d'Indétermination",
                            "duree": 30,
                            "contenu": r"""# Opérations et Levée d'Indétermination

## Formes Indéterminées (FI)

Les opérations sur les limites peuvent produire des **formes indéterminées** :

$$\infty - \infty \qquad 0 \times \infty \qquad \frac{0}{0} \qquad \frac{\infty}{\infty}$$

Dans ces cas, le calcul direct est impossible et il faut lever l'indétermination.

## Factorisation par le terme de plus haut degré

Pour un polynôme $P(x) = ax^2 + bx + c$ :

$$P(x) = x^2\left(a + \frac{b}{x} + \frac{c}{x^2}\right)$$

Comme $\lim_{x \to \pm\infty} \frac{b}{x} = 0$ et $\lim_{x \to \pm\infty} \frac{c}{x^2} = 0$ :

$$\lim_{x \to \pm\infty} P(x) = \lim_{x \to \pm\infty} ax^2$$

**Règle générale :** La limite d'un polynôme à l'infini est celle de son **monôme de plus haut degré**.

## Application aux fractions rationnelles

Pour $\frac{P(x)}{Q(x)}$, on factorise numérateur et dénominateur par leur monôme dominant.
""",
                            "quiz": {
                                "titre": "Quiz — Formes Indéterminées",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Laquelle n'est PAS une forme indéterminée ?",
                                        "options": ["∞ − ∞", "0 × ∞", "∞ × ∞", "0/0"],
                                        "reponse_correcte": "2",
                                        "explication": "∞ × ∞ = ∞ n'est pas indéterminé. Les FI classiques sont ∞−∞, 0×∞, 0/0, ∞/∞.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Quelle est la limite de 3x² − 5x + 1 quand x → +∞ ?",
                                        "reponse_correcte": "+∞",
                                        "tolerances": ["+∞", "+infini", "infini", "+inf"],
                                        "explication": "La limite est celle du monôme dominant 3x², qui tend vers +∞.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "Théorèmes de Comparaison et d'Encadrement",
                            "duree": 25,
                            "contenu": r"""# Théorèmes de Comparaison et d'Encadrement

## Théorème des Gendarmes

Si au voisinage de $a$ : $g(x) \le f(x) \le h(x)$ et si :

$$\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L$$

alors $\lim_{x \to a} f(x) = L$.

## Bornage des fonctions trigonométriques

$$\forall x \in \mathbb{R}, \quad -1 \le \sin(x) \le 1 \quad \text{et} \quad -1 \le \cos(x) \le 1$$

Ces inégalités sont systématiquement utilisées pour encadrer des expressions oscillantes.

**Exemple :** Pour $f(x) = \frac{\sin(x)}{x}$ quand $x \to +\infty$ :

$$-\frac{1}{x} \le \frac{\sin(x)}{x} \le \frac{1}{x}$$

Par le théorème des gendarmes : $\lim_{x \to +\infty} \frac{\sin(x)}{x} = 0$.
""",
                            "quiz": {
                                "titre": "Quiz — Théorèmes de Comparaison",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quelle est la limite de sin(x)/x quand x → +∞ ?",
                                        "reponse_correcte": "0",
                                        "tolerances": ["0"],
                                        "explication": "Par le théorème des gendarmes avec −1/x ≤ sin(x)/x ≤ 1/x, la limite vaut 0.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Le théorème des gendarmes requiert que les deux fonctions encadrantes aient la même limite.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Il faut g(x) et h(x) tendent vers la même limite L pour conclure que f(x) → L.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "Comportement Asymptotique",
                            "duree": 25,
                            "contenu": r"""# Étude du Comportement Asymptotique

## Asymptote Verticale

Si $\lim_{x \to a} f(x) = \pm\infty$, la droite $x = a$ est **asymptote verticale** à $\mathcal{C}_f$.

## Asymptote Horizontale

Si $\lim_{x \to \pm\infty} f(x) = L$, la droite $y = L$ est **asymptote horizontale** à $\mathcal{C}_f$.

## Symétries et réduction d'étude

- **Fonction paire** ($f(-x) = f(x)$) : symétrie par rapport à l'axe des ordonnées.
- **Fonction impaire** ($f(-x) = -f(x)$) : symétrie par rapport à l'origine.

L'étude de ces propriétés permet de **réduire l'intervalle d'étude** et d'en déduire les limites par symétrie.
""",
                            "quiz": {
                                "titre": "Quiz — Asymptotes",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La fonction f(x) = 1/x admet :",
                                        "options": ["Une asymptote horizontale y = 0 et une asymptote verticale x = 0", "Seulement une asymptote horizontale", "Seulement une asymptote verticale", "Aucune asymptote"],
                                        "reponse_correcte": "0",
                                        "explication": "lim(x→±∞) 1/x = 0 (AH y=0) et lim(x→0) 1/x = ±∞ (AV x=0).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Une fonction paire a sa courbe symétrique par rapport à l'origine.",
                                        "reponse_correcte": "faux",
                                        "explication": "Une fonction paire est symétrique par rapport à l'axe des ordonnées. C'est la fonction impaire qui est symétrique par rapport à l'origine.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 6,
                            "titre": "Notion de Continuité",
                            "duree": 25,
                            "contenu": r"""# Notion de Continuité

## Définition formelle

Une fonction $f$ est **continue en un point** $a$ si :

$$\lim_{x \to a} f(x) = f(a)$$

Intuitivement, la courbe peut être tracée « sans lever le crayon ».

## Continuité et Dérivabilité

- Toute fonction **dérivable** sur $I$ est **continue** sur $I$.
- La réciproque est **fausse** (ex : la valeur absolue en 0 est continue mais non dérivable).

## Continuité des fonctions de référence

- **Polynômes :** continus sur $\mathbb{R}$ (sommes et produits de fonctions continues).
- **Fonctions trigonométriques :** $\sin$ et $\cos$ sont continues sur $\mathbb{R}$.
- **Sommes, produits, composées** de fonctions continues sont continus.
""",
                            "quiz": {
                                "titre": "Quiz — Continuité",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "vrai_faux",
                                        "texte": "Toute fonction dérivable est continue.",
                                        "reponse_correcte": "vrai",
                                        "explication": "La dérivabilité implique la continuité, mais la réciproque est fausse.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "f est continue en a signifie que :",
                                        "options": ["f'(a) existe", "lim(x→a) f(x) = f(a)", "f(a) = 0", "f est dérivable en a"],
                                        "reponse_correcte": "1",
                                        "explication": "La continuité en a se définit par lim(x→a) f(x) = f(a).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 7,
                            "titre": "Théorème des Valeurs Intermédiaires et Bijection",
                            "duree": 30,
                            "contenu": r"""# Théorème des Valeurs Intermédiaires (TVI) et Bijection

## Théorème des Valeurs Intermédiaires

Si $f$ est **continue** sur $[a; b]$, alors pour tout réel $k$ compris entre $f(a)$ et $f(b)$, il existe **au moins** un $c \in [a; b]$ tel que $f(c) = k$.

## Corollaire de la Bijection

Si $f$ est **continue** et **strictement monotone** sur $[a; b]$, alors pour tout $k$ entre $f(a)$ et $f(b)$, l'équation $f(x) = k$ admet une **unique** solution dans $[a; b]$.

## Protocole de démonstration d'unicité

Pour montrer que $f(x) = k$ possède une unique solution $\alpha$ sur $I$ :

1. Justifier la **continuité** de $f$ sur $I$.
2. Établir la **stricte monotonie** (signe de $f'$).
3. Calculer les images des bornes ou les limites pour vérifier que $k \in f(I)$.
4. Conclure par le corollaire du TVI.

## Méthode de dichotomie

La dichotomie permet d'approcher numériquement la solution $\alpha$ :
- Diviser l'intervalle en deux
- Tester le changement de signe de $f$
- Réduire l'intervalle de moitié à chaque étape
""",
                            "quiz": {
                                "titre": "Quiz — TVI et Bijection",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Le TVI s'applique si f est :",
                                        "options": ["Dérivable", "Continue", "Monotone", "Bornée"],
                                        "reponse_correcte": "1",
                                        "explication": "Le TVI nécessite la continuité de f sur [a;b].",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Pour garantir l'UNICITÉ de la solution, il faut ajouter au TVI :",
                                        "options": ["La dérivabilité", "La stricte monotonie", "La bornitude", "La parité"],
                                        "reponse_correcte": "1",
                                        "explication": "Le corollaire du TVI nécessite continuité + stricte monotonie pour l'unicité.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La dichotomie divise l'intervalle en deux à chaque étape.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Le principe de la dichotomie est de couper l'intervalle en deux et de garder la moitié contenant la solution.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 8,
                            "titre": "Synthèse Graphique et Convexité",
                            "duree": 25,
                            "contenu": r"""# Synthèse Graphique et Convexité

## Lien Dérivée / Variations

Le signe de $f'(x)$ détermine le sens de variation de $f$ :
- $f'(x) > 0$ sur $I$ ⟹ $f$ est strictement croissante sur $I$.
- $f'(x) < 0$ sur $I$ ⟹ $f$ est strictement décroissante sur $I$.

## Convexité

- $f$ est **convexe** sur $I$ si $f'$ est croissante, c'est-à-dire $f''(x) \ge 0$.
- $f$ est **concave** sur $I$ si $f'$ est décroissante, c'est-à-dire $f''(x) \le 0$.

### Interprétation graphique
- **Convexe :** la courbe est au-dessus de ses tangentes (en dessous de ses cordes).
- **Concave :** la courbe est en dessous de ses tangentes (au-dessus de ses cordes).

## Point d'inflexion

$A(a; f(a))$ est un **point d'inflexion** si $f''$ s'annule et **change de signe** en $a$.

Ce point marque un changement de convexité : la courbe traverse sa tangente.
""",
                            "quiz": {
                                "titre": "Quiz — Convexité",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "f est convexe sur I si :",
                                        "options": ["f'(x) ≥ 0", "f''(x) ≥ 0", "f'(x) ≤ 0", "f''(x) ≤ 0"],
                                        "reponse_correcte": "1",
                                        "explication": "f est convexe quand f'' ≥ 0 (la dérivée première est croissante).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Un point d'inflexion est un point où f'' s'annule sans changer de signe.",
                                        "reponse_correcte": "faux",
                                        "explication": "Un point d'inflexion nécessite que f'' s'annule ET change de signe.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Si f est convexe, sa courbe est :",
                                        "options": ["Au-dessus de ses cordes", "Au-dessus de ses tangentes", "En dessous de ses tangentes", "Symétrique"],
                                        "reponse_correcte": "1",
                                        "explication": "Une fonction convexe a sa courbe au-dessus de ses tangentes (et en dessous de ses cordes).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.4 : Dérivabilité et Convexité ─────────────────────
                {
                    "ordre": 4,
                    "titre": "Dérivabilité et Convexité",
                    "description": "Dérivées, fonctions composées, dérivées successives, variations, extremums, convexité et points d'inflexion.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Fondements de la Dérivabilité",
                            "duree": 30,
                            "contenu": r"""# Fondements de la Dérivabilité

## Nombre dérivé

Soit $f$ définie sur un intervalle $I$ et $a \in I$. Le **nombre dérivé** de $f$ en $a$ est :

$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$

Si cette limite existe pour tout $x \in I$, $f$ est **dérivable sur $I$** et on définit la **fonction dérivée** $f' : x \mapsto f'(x)$.

## Dérivées des fonctions usuelles

| Fonction $f(x)$ | Dérivée $f'(x)$ | Domaine de dérivabilité |
|---|---|---|
| $k$ (constante) | $0$ | $\mathbb{R}$ |
| $x^n$ ($n \in \mathbb{N}^*$) | $nx^{n-1}$ | $\mathbb{R}$ |
| $\frac{1}{x}$ | $-\frac{1}{x^2}$ | $\mathbb{R}^*$ |
| $\sqrt{x}$ | $\frac{1}{2\sqrt{x}}$ | $]0; +\infty[$ |
| $\cos(x)$ | $-\sin(x)$ | $\mathbb{R}$ |
| $\sin(x)$ | $\cos(x)$ | $\mathbb{R}$ |
""",
                            "quiz": {
                                "titre": "Quiz — Fondements Dérivabilité",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La dérivée de x³ est :",
                                        "options": ["x²", "3x²", "3x³", "x³/3"],
                                        "reponse_correcte": "1",
                                        "explication": "Par la formule (xⁿ)' = nxⁿ⁻¹ : (x³)' = 3x².",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Quelle est la dérivée de sin(x) ?",
                                        "reponse_correcte": "cos(x)",
                                        "tolerances": ["cos(x)", "cos x", "cosx"],
                                        "explication": "La dérivée de sin(x) est cos(x).",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Le nombre dérivé de f en a est défini comme :",
                                        "options": ["f(a+h) − f(a)", "lim(h→0) [f(a+h)−f(a)]/h", "f(a)/a", "[f(b)−f(a)]/(b−a)"],
                                        "reponse_correcte": "1",
                                        "explication": "f'(a) = lim(h→0) [f(a+h) − f(a)] / h.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Opérations et Fonctions Composées",
                            "duree": 30,
                            "contenu": r"""# Opérations et Dérivation de Fonctions Composées

## Théorème de dérivation d'une composée

Soit $u$ dérivable sur $I$ et $g$ dérivable sur $J$ avec $u(I) \subset J$. Alors $g \circ u$ est dérivable et :

$$(g \circ u)' = u' \times (g' \circ u)$$

## Formules de composition usuelles

Pour $u$ dérivable sur $I$ :

| Composée | Dérivée |
|---|---|
| $u^n$ ($n \in \mathbb{Z}$) | $n \cdot u' \cdot u^{n-1}$ |
| $\sqrt{u}$ | $\frac{u'}{2\sqrt{u}}$ (si $u > 0$) |
| $\cos(ax+b)$ | $-a\sin(ax+b)$ |
| $\sin(ax+b)$ | $a\cos(ax+b)$ |

## Rappel des opérations

- $(u + v)' = u' + v'$
- $(uv)' = u'v + uv'$
- $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$ (si $v \neq 0$)
""",
                            "quiz": {
                                "titre": "Quiz — Fonctions Composées",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La dérivée de cos(3x + 1) est :",
                                        "options": ["−sin(3x+1)", "−3sin(3x+1)", "3cos(3x+1)", "sin(3x+1)"],
                                        "reponse_correcte": "1",
                                        "explication": "[cos(ax+b)]' = −a·sin(ax+b), donc ici −3sin(3x+1).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "La formule (g∘u)' est :",
                                        "options": ["g' × u'", "u' × (g'∘u)", "g' + u'", "(g∘u')"],
                                        "reponse_correcte": "1",
                                        "explication": "(g∘u)' = u' × (g'∘u).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Dérivées Successives",
                            "duree": 25,
                            "contenu": r"""# Dérivées Successives

## Définition

Si $f$ est dérivable et que $f'$ est elle-même dérivable, on dit que $f$ est **deux fois dérivable**.

La **dérivée seconde** est : $f'' = (f')'$.

Plus généralement, la **dérivée $n$-ième** est notée $f^{(n)}$.

## Exemple : $g(x) = xe^x$

**Dérivée première** (règle du produit) :
$$g'(x) = 1 \cdot e^x + x \cdot e^x = e^x(1+x)$$

**Dérivée seconde** :
$$g''(x) = e^x(1) + (1+x)e^x = e^x(2+x)$$

## Application

La dérivée seconde est l'outil fondamental pour :
- L'étude de la **convexité** ($f'' \ge 0$ ⟹ convexe)
- La recherche des **points d'inflexion** ($f'' = 0$ avec changement de signe)
""",
                            "quiz": {
                                "titre": "Quiz — Dérivées Successives",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Si g(x) = xe^x, que vaut g'(x) ?",
                                        "reponse_correcte": "e^x(1+x)",
                                        "tolerances": ["e^x(1+x)", "(1+x)e^x", "e^x(x+1)", "(x+1)e^x"],
                                        "explication": "Par la règle du produit : g'(x) = e^x + xe^x = e^x(1+x).",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La dérivée seconde f'' est la dérivée de f'.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Par définition, f'' = (f')'.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "Variations et Extremums",
                            "duree": 25,
                            "contenu": r"""# Étude des Variations et Extremums

## Monotonie

Soit $f$ dérivable sur $I$ :
- $f'(x) \ge 0$ pour tout $x \in I$ ⟹ $f$ est **croissante** sur $I$.
- $f'(x) \le 0$ pour tout $x \in I$ ⟹ $f$ est **décroissante** sur $I$.

## Extremum local

$f$ admet un **extremum local** en $x_0$ si $f'(x_0) = 0$ et $f'$ **change de signe** en $x_0$.

## Exemple : $f(x) = xe^{-x^2}$

$$f'(x) = (1 - 2x^2)e^{-x^2}$$

L'exponentielle est strictement positive, donc $f'(x)$ est du signe de $1 - 2x^2$.

Racines : $x = \pm\frac{1}{\sqrt{2}}$

| $x$ | $-\infty$ | $-\frac{1}{\sqrt{2}}$ | | $\frac{1}{\sqrt{2}}$ | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | $-$ | $0$ | $+$ | $0$ | $-$ |
| $f$ | $\searrow$ | min | $\nearrow$ | max | $\searrow$ |
""",
                            "quiz": {
                                "titre": "Quiz — Variations et Extremums",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "f admet un extremum local en x₀ si :",
                                        "options": ["f'(x₀) = 0", "f'(x₀) = 0 et f' change de signe", "f''(x₀) = 0", "f(x₀) = 0"],
                                        "reponse_correcte": "1",
                                        "explication": "Un extremum local nécessite f'(x₀) = 0 ET un changement de signe de f'.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Si f'(x) > 0 sur I, alors f est croissante sur I.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Une dérivée strictement positive implique la croissance stricte.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "Étude de la Convexité",
                            "duree": 30,
                            "contenu": r"""# Étude de la Convexité

## Définitions géométriques

- **Par les cordes :** $f$ est **convexe** si le segment reliant deux points de la courbe est au-dessus de la courbe. **Concave** si en dessous.
- **Par les tangentes :** $f$ est **convexe** si la courbe est au-dessus de ses tangentes. **Concave** si en dessous.

## Propriété fondamentale (dérivée seconde)

Pour $f$ deux fois dérivable sur $I$ :

- $f$ **convexe** sur $I$ $\iff$ $f'$ croissante sur $I$ $\iff$ $f''(x) \ge 0$
- $f$ **concave** sur $I$ $\iff$ $f'$ décroissante sur $I$ $\iff$ $f''(x) \le 0$

## Convexité des fonctions usuelles

| Fonction | Convexité |
|---|---|
| $x^2$ | Convexe sur $\mathbb{R}$ |
| $x^3$ | Concave sur $]-\infty; 0]$, convexe sur $[0; +\infty[$ |
| $1/x$ | Concave sur $]-\infty; 0[$, convexe sur $]0; +\infty[$ |
| $\sqrt{x}$ | Concave sur $[0; +\infty[$ |
""",
                            "quiz": {
                                "titre": "Quiz — Convexité",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "f est convexe sur I si et seulement si :",
                                        "options": ["f'(x) ≥ 0", "f''(x) ≥ 0", "f'(x) ≤ 0", "f(x) ≥ 0"],
                                        "reponse_correcte": "1",
                                        "explication": "f convexe ⟺ f'' ≥ 0 (la dérivée première est croissante).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La fonction carré x² est concave sur ℝ.",
                                        "reponse_correcte": "faux",
                                        "explication": "x² est convexe sur ℝ car (x²)'' = 2 > 0.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 6,
                            "titre": "Points d'Inflexion",
                            "duree": 20,
                            "contenu": r"""# Points d'Inflexion

## Définition

Un **point d'inflexion** est un point de la courbe où celle-ci **traverse sa tangente**.

## Propriété algébrique

Pour $f$ deux fois dérivable, la courbe admet un point d'inflexion en $x_0$ si et seulement si :

$$f''(x_0) = 0 \quad \text{et} \quad f'' \text{ change de signe en } x_0$$

**Attention :** L'annulation de $f''$ est **nécessaire mais non suffisante**. Il faut vérifier le changement de signe.

## Exemple : $f(x) = x^3$

$$f''(x) = 6x$$

$f''(0) = 0$ et $f''$ change de signe en 0 (négatif avant, positif après).

Donc $(0; 0)$ est un **point d'inflexion**.
""",
                            "quiz": {
                                "titre": "Quiz — Points d'Inflexion",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "vrai_faux",
                                        "texte": "f''(x₀) = 0 suffit pour avoir un point d'inflexion en x₀.",
                                        "reponse_correcte": "faux",
                                        "explication": "Il faut aussi que f'' change de signe en x₀ (condition nécessaire et suffisante).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "En quel point la fonction x³ admet-elle un point d'inflexion ?",
                                        "reponse_correcte": "0",
                                        "tolerances": ["0", "x=0", "en 0", "(0,0)", "(0;0)"],
                                        "explication": "f''(x) = 6x, f''(0) = 0 avec changement de signe. Point d'inflexion en x = 0.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 7,
                            "titre": "Optimisation",
                            "duree": 25,
                            "contenu": r"""# Optimisation et Résolution de Problèmes

## Problème guide : Coût de fabrication

Une entreprise produit $x$ milliers de clés USB ($x \in [0; 10]$). Le coût est :

$$C(x) = 0{,}05x^3 - 1{,}05x^2 + 8x + 4$$

### Dérivées

$$C'(x) = 0{,}15x^2 - 2{,}1x + 8$$
$$C''(x) = 0{,}3x - 2{,}1$$

### Point d'inflexion

$C''(x) = 0 \iff x = 7$

- Sur $[0; 7]$ : $C''(x) \le 0$ → concave (croissance ralentit)
- Sur $[7; 10]$ : $C''(x) \ge 0$ → convexe (croissance s'accélère)

$C(7) = 25{,}7$ : le point $(7; 25{,}7)$ est un point d'inflexion.

### Interprétation économique

Avant 7000 clés, la croissance du coût **ralentit**. Au-delà, elle **s'accélère**.
""",
                            "quiz": {
                                "titre": "Quiz — Optimisation",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Pour C(x) = 0,05x³ − 1,05x² + 8x + 4, que vaut C''(x) ?",
                                        "reponse_correcte": "0,3x − 2,1",
                                        "tolerances": ["0,3x - 2,1", "0.3x - 2.1", "0,3x-2,1", "0.3x-2.1"],
                                        "explication": "C'(x) = 0,15x² − 2,1x + 8, donc C''(x) = 0,3x − 2,1.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Le point d'inflexion du coût de fabrication est en x = :",
                                        "options": ["5", "7", "10", "3"],
                                        "reponse_correcte": "1",
                                        "explication": "C''(x) = 0 ⟹ 0,3x = 2,1 ⟹ x = 7.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 8,
                            "titre": "Synthèse des Méthodes",
                            "duree": 20,
                            "contenu": r"""# Synthèse des Méthodes de Résolution

## Étude complète de la convexité d'une fonction

1. **Déterminer** l'ensemble de définition et de dérivabilité.
2. **Calculer** la dérivée première $f'(x)$.
3. **Calculer** la dérivée seconde $f''(x)$.
4. **Étudier le signe** de $f''(x)$.
5. **Dresser le tableau de convexité** :
   - Signe de $f''(x)$
   - Nature (convexe/concave)
   - Position des points d'inflexion

## Points de vigilance

- L'annulation de $f''$ est **nécessaire mais non suffisante** pour un point d'inflexion.
- Vérifier le **changement de signe** de $f''$.
- Ne pas confondre : $f' = 0$ (extremum possible) et $f'' = 0$ (inflexion possible).

## Résumé des liens

| Outil | Information |
|---|---|
| Signe de $f'$ | Sens de variation de $f$ |
| Signe de $f''$ | Convexité de $f$ |
| $f'(x_0) = 0$ + changement signe $f'$ | Extremum local |
| $f''(x_0) = 0$ + changement signe $f''$ | Point d'inflexion |
""",
                            "quiz": {
                                "titre": "Quiz — Synthèse Dérivabilité",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Le signe de f'' renseigne sur :",
                                        "options": ["Les variations de f", "La convexité de f", "Les zéros de f", "La parité de f"],
                                        "reponse_correcte": "1",
                                        "explication": "f'' ≥ 0 → convexe, f'' ≤ 0 → concave.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Le signe de f' renseigne sur :",
                                        "options": ["La convexité", "Le sens de variation", "Les points d'inflexion", "La continuité"],
                                        "reponse_correcte": "1",
                                        "explication": "f' > 0 → croissante, f' < 0 → décroissante.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.5 : Fonctions Trigonométriques ────────────────────
                {
                    "ordre": 5,
                    "titre": "Fonctions Trigonométriques",
                    "description": "Cercle trigonométrique, valeurs remarquables, formulaire, équations, étude de sin et cos, Euler et Moivre.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Le Cercle Trigonométrique et Définitions",
                            "duree": 30,
                            "contenu": r"""# Rappels : Le Cercle Trigonométrique

## Définitions

Le cercle trigonométrique est un cercle de centre $O$, de rayon 1, orienté dans le sens direct.

- $\cos(x)$ = abscisse du point $M$ associé à $x$
- $\sin(x)$ = ordonnée du point $M$ associé à $x$

## Propriétés fondamentales

$$-1 \le \cos(x) \le 1 \quad\text{et}\quad -1 \le \sin(x) \le 1$$

$$\cos^2(x) + \sin^2(x) = 1$$

## Formules de symétrie

| Transformation | $\cos$ | $\sin$ |
|---|---|---|
| Opposés : $-x$ | $\cos(x)$ | $-\sin(x)$ |
| Supplémentaires : $\pi - x$ | $-\cos(x)$ | $\sin(x)$ |
| Différant de $\pi$ : $\pi + x$ | $-\cos(x)$ | $-\sin(x)$ |
| Complémentaires : $\frac{\pi}{2} - x$ | $\sin(x)$ | $\cos(x)$ |
| Déphasage $\frac{\pi}{2}$ : $\frac{\pi}{2} + x$ | $-\sin(x)$ | $\cos(x)$ |
""",
                            "quiz": {
                                "titre": "Quiz — Cercle Trigonométrique",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "cos²(x) + sin²(x) = ?",
                                        "options": ["0", "1", "2", "x"],
                                        "reponse_correcte": "1",
                                        "explication": "C'est la relation pythagoricienne fondamentale.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Que vaut cos(−x) en fonction de cos(x) ?",
                                        "reponse_correcte": "cos(x)",
                                        "tolerances": ["cos(x)", "cos x", "cosx"],
                                        "explication": "cos(−x) = cos(x) : le cosinus est une fonction paire.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "sin(π − x) = −sin(x).",
                                        "reponse_correcte": "faux",
                                        "explication": "sin(π − x) = sin(x) (et non −sin(x)).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Valeurs Remarquables",
                            "duree": 20,
                            "contenu": r"""# Valeurs Remarquables

## Tableau des valeurs

| $x$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\pi$ |
|---|---|---|---|---|---|---|
| $\cos(x)$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ | $-1$ |
| $\sin(x)$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ | $0$ |
| $\tan(x)$ | $0$ | $\frac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ | — | $0$ |

## Lecture sur le cercle

- Le cosinus se lit sur l'axe des **abscisses** (horizontal).
- Le sinus se lit sur l'axe des **ordonnées** (vertical).
- Pour $x = \frac{\pi}{2}$, le point $M$ est en $(0, 1)$ : $\cos = 0$, $\sin = 1$.
""",
                            "quiz": {
                                "titre": "Quiz — Valeurs Remarquables",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Que vaut cos(π/3) ?",
                                        "reponse_correcte": "1/2",
                                        "tolerances": ["1/2", "0.5", "0,5"],
                                        "explication": "cos(π/3) = 1/2, valeur remarquable à connaître.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Que vaut sin(π/4) ?",
                                        "options": ["1/2", "√2/2", "√3/2", "1"],
                                        "reponse_correcte": "1",
                                        "explication": "sin(π/4) = √2/2.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Que vaut tan(π/4) ?",
                                        "reponse_correcte": "1",
                                        "tolerances": ["1"],
                                        "explication": "tan(π/4) = sin(π/4)/cos(π/4) = (√2/2)/(√2/2) = 1.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Formulaire : Addition et Duplication",
                            "duree": 30,
                            "contenu": r"""# Formulaire de Trigonométrie

## Formules d'Addition

$$\cos(a+b) = \cos a \cos b - \sin a \sin b$$
$$\cos(a-b) = \cos a \cos b + \sin a \sin b$$
$$\sin(a+b) = \sin a \cos b + \cos a \sin b$$
$$\sin(a-b) = \sin a \cos b - \cos a \sin b$$

## Formules de Duplication

En posant $a = b$ :

$$\cos(2a) = \cos^2(a) - \sin^2(a) = 2\cos^2(a) - 1 = 1 - 2\sin^2(a)$$
$$\sin(2a) = 2\sin(a)\cos(a)$$

## Exemple : calcul de $\cos\left(\frac{5\pi}{12}\right)$

$$\frac{5\pi}{12} = \frac{\pi}{4} + \frac{\pi}{6}$$

$$\cos\left(\frac{5\pi}{12}\right) = \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} - \frac{\sqrt{2}}{2} \cdot \frac{1}{2} = \frac{\sqrt{6} - \sqrt{2}}{4}$$
""",
                            "quiz": {
                                "titre": "Quiz — Formulaire Trigonométrie",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "sin(2a) = ?",
                                        "options": ["2sin(a)", "2sin(a)cos(a)", "sin²(a) + cos²(a)", "cos(2a)"],
                                        "reponse_correcte": "1",
                                        "explication": "La formule de duplication du sinus : sin(2a) = 2sin(a)cos(a).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "cos(a+b) = ?",
                                        "options": ["cos(a)cos(b) + sin(a)sin(b)", "cos(a)cos(b) − sin(a)sin(b)", "sin(a)cos(b) + cos(a)sin(b)", "cos(a) + cos(b)"],
                                        "reponse_correcte": "1",
                                        "explication": "cos(a+b) = cos(a)cos(b) − sin(a)sin(b).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Quelle expression est égale à cos(2a) ?",
                                        "options": ["2cos²(a) − 1", "2sin(a)cos(a)", "cos²(a) + sin²(a)", "1 + 2sin²(a)"],
                                        "reponse_correcte": "0",
                                        "explication": "cos(2a) = 2cos²(a) − 1 = cos²(a) − sin²(a) = 1 − 2sin²(a).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "Équations et Inéquations Trigonométriques",
                            "duree": 30,
                            "contenu": r"""# Résolution d'Équations Trigonométriques

## Équations fondamentales

$$\cos(x) = \cos(\alpha) \iff x = \alpha + 2k\pi \text{ ou } x = -\alpha + 2k\pi \quad (k \in \mathbb{Z})$$

$$\sin(x) = \sin(\alpha) \iff x = \alpha + 2k\pi \text{ ou } x = \pi - \alpha + 2k\pi \quad (k \in \mathbb{Z})$$

$$\tan(x) = \tan(\alpha) \iff x = \alpha + k\pi \quad (k \in \mathbb{Z})$$

## Inéquations

**Exemple :** $\sin(x) \le \frac{\sqrt{3}}{2}$ sur $]-\pi; \pi]$.

1. Équation associée : $\sin(x) = \frac{\sqrt{3}}{2}$ donne $x = \frac{\pi}{3}$ ou $x = \frac{2\pi}{3}$.
2. Sur le cercle, on repère l'arc en dessous de $y = \frac{\sqrt{3}}{2}$.
3. Solution : $S = \left]-\pi; \frac{\pi}{3}\right] \cup \left[\frac{2\pi}{3}; \pi\right]$.

## Méthode $a\cos x + b\sin x = c$

On pose $r = \sqrt{a^2 + b^2}$ et on trouve $\theta$ tel que $\cos\theta = \frac{a}{r}$, $\sin\theta = \frac{b}{r}$.

L'équation se simplifie en : $\cos(x - \theta) = \frac{c}{r}$.
""",
                            "quiz": {
                                "titre": "Quiz — Équations Trigonométriques",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "cos(x) = cos(α) admet les solutions :",
                                        "options": ["x = α + kπ", "x = α + 2kπ ou x = −α + 2kπ", "x = π − α + 2kπ", "x = α uniquement"],
                                        "reponse_correcte": "1",
                                        "explication": "cos(x) = cos(α) ⟺ x = α + 2kπ ou x = −α + 2kπ.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "tan(x) = tan(α) admet les solutions :",
                                        "options": ["x = α + 2kπ", "x = α + kπ", "x = −α + kπ", "x = π − α + kπ"],
                                        "reponse_correcte": "1",
                                        "explication": "tan(x) = tan(α) ⟺ x = α + kπ (k ∈ ℤ).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "Étude Complète de sin et cos",
                            "duree": 30,
                            "contenu": r"""# Étude Complète des Fonctions Sinus et Cosinus

## Périodicité

Les fonctions $\cos$ et $\sin$ sont $2\pi$-périodiques : $f(x + 2\pi) = f(x)$.

## Parité

- **Cosinus :** $\cos(-x) = \cos(x)$ → fonction **paire**.
- **Sinus :** $\sin(-x) = -\sin(x)$ → fonction **impaire**.

## Dérivées

$$\cos'(x) = -\sin(x) \qquad \sin'(x) = \cos(x)$$

## Variations sur $[0; \pi]$

### Cosinus

| $x$ | $0$ | → | $\pi$ |
|---|---|---|---|
| $-\sin(x)$ | $0$ | $-$ | $0$ |
| $\cos(x)$ | $1$ | $\searrow$ | $-1$ |

### Sinus sur $[0; \pi]$

| $x$ | $0$ | → $\frac{\pi}{2}$ | → $\pi$ |
|---|---|---|---|
| $\cos(x)$ | $+$ | $0$ | $-$ |
| $\sin(x)$ | $0 \nearrow$ | $1$ | $\searrow 0$ |

## Représentations

Les courbes sont des **sinusoïdes**. On complète le tracé sur $\mathbb{R}$ par translations de vecteur $2k\pi \vec{i}$.
""",
                            "quiz": {
                                "titre": "Quiz — Étude de sin et cos",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quelle est la période de la fonction cosinus ?",
                                        "reponse_correcte": "2π",
                                        "tolerances": ["2π", "2pi", "2*pi"],
                                        "explication": "cos(x + 2π) = cos(x), la période est 2π.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "La fonction sinus est :",
                                        "options": ["Paire", "Impaire", "Ni paire ni impaire", "Périodique de période π"],
                                        "reponse_correcte": "1",
                                        "explication": "sin(−x) = −sin(x), la fonction sinus est impaire.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Que vaut la dérivée de cos(x) ?",
                                        "reponse_correcte": "-sin(x)",
                                        "tolerances": ["-sin(x)", "-sin x", "-sinx"],
                                        "explication": "(cos x)' = −sin(x).",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 6,
                            "titre": "Applications : Euler et Moivre",
                            "duree": 30,
                            "contenu": r"""# Applications : Formules d'Euler et de Moivre

## Exponentielle complexe

$$e^{i\theta} = \cos\theta + i\sin\theta$$

## Formule de Moivre

$$(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$$

La formule de Moivre est l'outil pour exprimer $\cos(nx)$ en fonction de $\cos(x)$.

## Formules d'Euler

$$\cos(\theta) = \frac{e^{i\theta} + e^{-i\theta}}{2}$$

$$\sin(\theta) = \frac{e^{i\theta} - e^{-i\theta}}{2i}$$

## Technique de Linéarisation

Transformer une puissance ($\cos^n x$) en somme de termes $\cos(kx)$.

**Exemple :** $\cos^3(x)$

$$\cos^3(x) = \left(\frac{e^{ix} + e^{-ix}}{2}\right)^3 = \frac{1}{8}(e^{3ix} + 3e^{ix} + 3e^{-ix} + e^{-3ix})$$

$$= \frac{1}{4}\cos(3x) + \frac{3}{4}\cos(x)$$
""",
                            "quiz": {
                                "titre": "Quiz — Euler et Moivre",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La formule d'Euler pour cos(θ) est :",
                                        "options": ["(e^{iθ} + e^{−iθ})/2", "(e^{iθ} − e^{−iθ})/2i", "e^{iθ} − e^{−iθ}", "e^{iθ}"],
                                        "reponse_correcte": "0",
                                        "explication": "cos(θ) = (e^{iθ} + e^{−iθ})/2.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La formule de Moivre donne (cos θ + i sin θ)ⁿ = cos(nθ) + i sin(nθ).",
                                        "reponse_correcte": "vrai",
                                        "explication": "C'est exactement la formule de Moivre.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Que vaut e^{iπ} + 1 ? (identité d'Euler)",
                                        "reponse_correcte": "0",
                                        "tolerances": ["0"],
                                        "explication": "e^{iπ} = cos(π) + i sin(π) = −1, donc e^{iπ} + 1 = 0.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.6 : Fonction Exponentielle et Équations Différentielles ──
                {
                    "ordre": 6,
                    "titre": "Fonction Exponentielle et Équations Différentielles",
                    "description": "Définition, propriétés algébriques, étude analytique, équations différentielles y'=ay et y'=ay+b, loi exponentielle.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Introduction et Définition",
                            "duree": 25,
                            "contenu": r"""# Introduction et Définition de la Fonction Exponentielle

## Définition fondamentale

La **fonction exponentielle** $\exp : x \mapsto e^x$ est l'**unique** fonction $f$ dérivable sur $\mathbb{R}$ solution de :

$$f' = f \quad \text{avec} \quad f(0) = 1$$

Cette définition garantit l'existence et l'unicité. Propriété immédiate : pour tout réel $x$, $e^x \neq 0$.

## Valeurs de référence

- $e^0 = 1$
- $e^1 = e \approx 2{,}718$
- $e^x > 0$ pour tout $x \in \mathbb{R}$
""",
                            "quiz": {
                                "titre": "Quiz — Définition Exponentielle",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Que vaut e⁰ ?",
                                        "reponse_correcte": "1",
                                        "tolerances": ["1"],
                                        "explication": "Par la condition initiale de la définition : f(0) = 1.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La fonction exponentielle est définie comme l'unique solution de f' = f avec f(0) = 1.",
                                        "reponse_correcte": "vrai",
                                        "explication": "C'est la définition analytique de la fonction exponentielle.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Il existe un réel x tel que e^x = 0.",
                                        "reponse_correcte": "faux",
                                        "explication": "L'exponentielle est strictement positive : e^x > 0 pour tout x.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Propriétés Algébriques",
                            "duree": 25,
                            "contenu": r"""# Propriétés Algébriques de l'Exponentielle

L'exponentielle transforme les **sommes en produits**.

## Formules fondamentales

Pour tous réels $a$ et $b$ :

| Propriété | Formule |
|---|---|
| Relation produit | $e^{a+b} = e^a \times e^b$ |
| Relation inverse | $e^{-a} = \frac{1}{e^a}$ |
| Relation quotient | $e^{a-b} = \frac{e^a}{e^b}$ |
| Relation puissance | $(e^a)^n = e^{na}$ |

## Lien avec les complexes

La notation $e^{i\theta} = \cos\theta + i\sin\theta$ provient du fait que la fonction $f(\theta) = \cos\theta + i\sin\theta$ vérifie $f(\theta)f(\theta') = f(\theta+\theta')$, la même équation fonctionnelle que l'exponentielle réelle.

**Identité d'Euler :** $e^{i\pi} = -1$.
""",
                            "quiz": {
                                "titre": "Quiz — Propriétés Algébriques",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "e^(a+b) = ?",
                                        "options": ["e^a + e^b", "e^a × e^b", "(e^a)^b", "e^(ab)"],
                                        "reponse_correcte": "1",
                                        "explication": "L'exponentielle transforme les sommes en produits : e^(a+b) = e^a × e^b.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Simplifier e^3 × e^(−3).",
                                        "reponse_correcte": "1",
                                        "tolerances": ["1", "e^0"],
                                        "explication": "e^3 × e^(−3) = e^(3−3) = e^0 = 1.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Étude Analytique",
                            "duree": 30,
                            "contenu": r"""# Étude Analytique de la Fonction Exponentielle

## Dérivée

$$(e^x)' = e^x$$

Pour $u$ dérivable : $(e^{u(x)})' = u'(x) \cdot e^{u(x)}$.

**Exemple :** $g(x) = xe^x$ ⟹ $g'(x) = e^x(1+x)$.

## Sens de variation

$e^x > 0$ pour tout $x$, donc $f'(x) = e^x > 0$ : l'exponentielle est **strictement croissante** sur $\mathbb{R}$.

## Limites

$$\lim_{x \to +\infty} e^x = +\infty \qquad \lim_{x \to -\infty} e^x = 0$$

La limite en $-\infty$ donne une **asymptote horizontale** $y = 0$.

## Croissance comparée

$$\lim_{x \to +\infty} \frac{e^x}{x} = +\infty$$

L'exponentielle **l'emporte** sur toute fonction puissance.

## Convexité

$f''(x) = e^x > 0$ : l'exponentielle est **convexe** sur $\mathbb{R}$ (courbe au-dessus de ses tangentes).
""",
                            "quiz": {
                                "titre": "Quiz — Étude Analytique",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "lim(x→−∞) e^x = ?",
                                        "options": ["+∞", "0", "1", "−∞"],
                                        "reponse_correcte": "1",
                                        "explication": "L'exponentielle tend vers 0 en −∞, d'où l'asymptote y = 0.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La fonction exponentielle est concave sur ℝ.",
                                        "reponse_correcte": "faux",
                                        "explication": "f''(x) = e^x > 0 : l'exponentielle est convexe (pas concave).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "L'exponentielle est strictement croissante sur ℝ.",
                                        "reponse_correcte": "vrai",
                                        "explication": "f'(x) = e^x > 0 pour tout x, donc f est strictement croissante.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "Équations Différentielles y' = ay",
                            "duree": 30,
                            "contenu": r"""# Équations Différentielles du Type $y' = ay$

## Théorème

Les solutions de $y' = ay$ sont les fonctions :

$$f(x) = Ce^{ax}$$

où $C$ est une constante réelle.

## Méthode de résolution

1. **Identifier** la valeur de $a$.
2. **Écrire** la solution générale $f(x) = Ce^{ax}$.
3. **Déterminer** $C$ avec la condition initiale $f(x_0) = y_0$ :

$$Ce^{ax_0} = y_0 \implies C = y_0 e^{-ax_0}$$

## Exemple

Résoudre $y' = 2y$ avec $f(0) = 3$.

- Solution générale : $f(x) = Ce^{2x}$
- Condition initiale : $f(0) = C = 3$
- **Solution :** $f(x) = 3e^{2x}$
""",
                            "quiz": {
                                "titre": "Quiz — y' = ay",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La solution générale de y' = 5y est :",
                                        "options": ["f(x) = Ce^{5x}", "f(x) = 5e^x", "f(x) = Ce^{x/5}", "f(x) = 5x"],
                                        "reponse_correcte": "0",
                                        "explication": "Les solutions de y' = ay sont f(x) = Ce^{ax}, ici f(x) = Ce^{5x}.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Résoudre y' = −2y avec f(0) = 4. Que vaut C ?",
                                        "reponse_correcte": "4",
                                        "tolerances": ["4"],
                                        "explication": "f(x) = Ce^{−2x}, f(0) = C = 4.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "Équations Différentielles y' = ay + b",
                            "duree": 30,
                            "contenu": r"""# Équations Différentielles du Type $y' = ay + b$

## Solution générale

$$f(x) = Ce^{ax} - \frac{b}{a}$$

## Tableau récapitulatif

| Équation | Solution générale | Constante $C$ |
|---|---|---|
| $y' = ay$ | $Ce^{ax}$ | $C = f(x_0)/e^{ax_0}$ |
| $y' = ay + b$ | $Ce^{ax} - \frac{b}{a}$ | $C = \left(f(x_0) + \frac{b}{a}\right)/e^{ax_0}$ |

## Solution particulière constante

On pose $f(x) = k$ (donc $f'(x) = 0$) :

$$0 = ak + b \implies k = -\frac{b}{a}$$

## Exemple : $y' = -3y + 6$ avec $f(0) = 4$

1. $a = -3$, $b = 6$ → solution générale : $f(x) = Ce^{-3x} + 2$
2. $f(0) = C + 2 = 4$ → $C = 2$
3. **Solution :** $f(x) = 2e^{-3x} + 2$
""",
                            "quiz": {
                                "titre": "Quiz — y' = ay + b",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quelle est la solution particulière constante de y' = 2y − 6 ?",
                                        "reponse_correcte": "3",
                                        "tolerances": ["3", "y=3"],
                                        "explication": "On pose y' = 0 : 0 = 2k − 6, donc k = 3.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "La solution générale de y' = ay + b est :",
                                        "options": ["Ce^{ax}", "Ce^{ax} − b/a", "Ce^{bx} + a", "Ce^{ax} + b"],
                                        "reponse_correcte": "1",
                                        "explication": "f(x) = Ce^{ax} − b/a.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 6,
                            "titre": "Applications et Exercices",
                            "duree": 25,
                            "contenu": r"""# Applications de la Fonction Exponentielle

## La Loi Exponentielle (Probabilités)

La loi exponentielle de paramètre $\lambda > 0$ modélise des **durées de vie sans vieillissement**.

- **Densité :** $f(x) = \lambda e^{-\lambda x}$ pour $x \ge 0$
- **Répartition :** $P(X \le x) = 1 - e^{-\lambda x}$
- **Espérance :** $E(X) = \frac{1}{\lambda}$
- **Absence de mémoire :** $P_{X \ge t}(X \ge t+h) = P(X \ge h)$

## Exercice type : Équation exponentielle

Résoudre $e^{2x+1} = e^3$.

Par stricte croissance : $e^a = e^b \iff a = b$

$$2x + 1 = 3 \implies x = 1$$

## Exercice type : Étude de convexité

Pour $g(x) = xe^{-x^2}$ :
- $g'(x) = (1-2x^2)e^{-x^2}$
- $g''(x)$ s'annule aux points d'inflexion
""",
                            "quiz": {
                                "titre": "Quiz — Applications Exponentielle",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Résoudre e^{2x+1} = e^3. Que vaut x ?",
                                        "reponse_correcte": "1",
                                        "tolerances": ["1", "x=1"],
                                        "explication": "2x + 1 = 3 ⟹ x = 1.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "L'espérance de la loi exponentielle de paramètre λ est :",
                                        "options": ["λ", "1/λ", "λ²", "e^λ"],
                                        "reponse_correcte": "1",
                                        "explication": "E(X) = 1/λ pour une loi exponentielle de paramètre λ.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La loi exponentielle possède la propriété d'absence de mémoire.",
                                        "reponse_correcte": "vrai",
                                        "explication": "P(X ≥ t+h | X ≥ t) = P(X ≥ h), le passé n'influence pas le futur.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                {
                    "ordre": 7,
                    "titre": "La Fonction Logarithme Népérien",
                    "description": "Définition comme réciproque de l'exponentielle, propriétés algébriques, étude analytique complète, convexité, comparaison avec exp, calcul intégral et applications.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Introduction et Fondements de la Fonction ln",
                            "duree": 30,
                            "contenu": r"""## Définition de la Fonction Logarithme Népérien

### Théorème d'existence

La fonction exponentielle $\exp : x \mapsto e^x$ est continue et strictement croissante sur $\mathbb{R}$, à valeurs dans $]0\,;\,+\infty[$.

Par le **théorème de la bijection**, elle admet une **réciproque unique** appelée **fonction logarithme népérien**, notée $\ln$.

### Ensemble de définition

$$\mathcal{D}_{\ln} = \,]0\,;\,+\infty[$$

### Relation fondamentale

Pour tout $x > 0$ et tout $y \in \mathbb{R}$ :

$$y = \ln(x) \iff x = e^y$$

### Valeurs particulières

- $\ln(1) = 0$ car $e^0 = 1$
- $\ln(e) = 1$ car $e^1 = e$

### Compositions réciproques

$$\forall x \in \mathbb{R},\; \ln(e^x) = x \qquad \forall x > 0,\; e^{\ln x} = x$$
""",
                            "quiz": {
                                "titre": "Quiz — Définition de ln",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quel est l'ensemble de définition de la fonction ln ?",
                                        "reponse_correcte": "]0;+∞[",
                                        "tolerances": ["]0,+inf[", "R+*", "les reels strictement positifs"],
                                        "explication": "La fonction ln est définie sur ]0;+∞[.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Que vaut ln(1) ?",
                                        "reponse_correcte": "0",
                                        "tolerances": [],
                                        "explication": "ln(1) = 0 car e^0 = 1.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "La fonction ln est la réciproque de :",
                                        "choix": ["La fonction carré", "La fonction racine carrée", "La fonction exponentielle", "La fonction inverse"],
                                        "reponse_correcte": "La fonction exponentielle",
                                        "explication": "ln est définie comme la réciproque de exp.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Propriétés Algébriques du Logarithme",
                            "duree": 25,
                            "contenu": r"""## Propriétés Algébriques

### Transformation produit → somme

Pour tous $a, b > 0$ :

$$\ln(a \times b) = \ln(a) + \ln(b)$$

### Quotient et puissance

$$\ln\left(\frac{a}{b}\right) = \ln(a) - \ln(b) \qquad \ln(a^n) = n\,\ln(a)$$

### Racine carrée

$$\ln(\sqrt{a}) = \frac{1}{2}\ln(a)$$

### Puissances réelles

Pour tout $a > 0$ et tout réel $b$ :

$$a^b = e^{b\,\ln(a)}$$

### Applications

- **Résolution d'équations** : $2^x = 5 \iff e^{x\ln 2} = 5 \iff x = \dfrac{\ln 5}{\ln 2}$
- **Simplifications** : $\ln(8) = \ln(2^3) = 3\ln(2)$
""",
                            "quiz": {
                                "titre": "Quiz — Propriétés algébriques",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "ln(a × b) est égal à :",
                                        "choix": ["ln(a) × ln(b)", "ln(a) + ln(b)", "ln(a) - ln(b)", "ln(a) / ln(b)"],
                                        "reponse_correcte": "ln(a) + ln(b)",
                                        "explication": "Le logarithme transforme un produit en somme.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Simplifier ln(8) en utilisant ln(2).",
                                        "reponse_correcte": "3ln(2)",
                                        "tolerances": ["3 ln(2)", "3*ln(2)", "3 ln 2"],
                                        "explication": "ln(8) = ln(2³) = 3ln(2).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "ln(a/b) = ln(a) - ln(b) pour tous a, b > 0.",
                                        "reponse_correcte": "vrai",
                                        "explication": "C'est la propriété du logarithme d'un quotient.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Étude Analytique Complète",
                            "duree": 35,
                            "contenu": r"""## Étude Analytique de ln

### Dérivée

$$(\ln(x))' = \frac{1}{x} \quad \text{pour } x > 0$$

**Forme composée** : si $u$ est dérivable et strictement positive :

$$(\ln(u))' = \frac{u'}{u}$$

### Sens de variation

Pour tout $x > 0$ : $\dfrac{1}{x} > 0$, donc $\ln$ est **strictement croissante** sur $]0\,;\,+\infty[$.

### Continuité

$\ln$ est dérivable, donc continue sur $]0\,;\,+\infty[$, ce qui justifie son caractère bijectif.

### Limites aux bornes

$$\lim_{x \to 0^+} \ln(x) = -\infty \qquad \lim_{x \to +\infty} \ln(x) = +\infty$$

L'axe des ordonnées ($x = 0$) est **asymptote verticale**.

### Tableau de variation

| $x$ | $0$ | | $+\infty$ |
|---|---|---|---|
| $\ln'(x)$ | | $+$ | |
| $\ln(x)$ | $-\infty$ | $\nearrow$ | $+\infty$ |
""",
                            "quiz": {
                                "titre": "Quiz — Étude analytique",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quelle est la dérivée de ln(x) ?",
                                        "reponse_correcte": "1/x",
                                        "tolerances": ["1 / x", "x^(-1)"],
                                        "explication": "(ln(x))' = 1/x.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "lim(x→0⁺) ln(x) = ?",
                                        "choix": ["+∞", "0", "-∞", "1"],
                                        "reponse_correcte": "-∞",
                                        "explication": "La fonction ln tend vers -∞ quand x tend vers 0 par valeurs positives.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La fonction ln est strictement décroissante sur ]0;+∞[.",
                                        "reponse_correcte": "faux",
                                        "explication": "ln'(x) = 1/x > 0, donc ln est strictement CROISSANTE.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "Analyse de la Convexité",
                            "duree": 20,
                            "contenu": r"""## Convexité de la Fonction ln

### Dérivée seconde

$$f'(x) = \frac{1}{x} = x^{-1} \implies f''(x) = -x^{-2} = -\frac{1}{x^2}$$

### Signe de $f''$

Pour tout $x > 0$ : $x^2 > 0$, donc $f''(x) = -\dfrac{1}{x^2} < 0$.

### Conclusion

$f''(x) < 0$ sur $]0\,;\,+\infty[$ : la fonction $\ln$ est **concave**.

### Interprétation graphique

- La courbe $\mathcal{C}_{\ln}$ est située **en dessous** de chacune de ses tangentes
- La courbe est située **au-dessus** de chacune de ses cordes

### Inégalité caractéristique

Pour tous $a, b > 0$ et $t \in [0\,;\,1]$ :

$$\ln(ta + (1-t)b) \geq t\,\ln(a) + (1-t)\,\ln(b)$$
""",
                            "quiz": {
                                "titre": "Quiz — Convexité de ln",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La fonction ln est :",
                                        "choix": ["Convexe", "Concave", "Ni l'un ni l'autre", "Convexe puis concave"],
                                        "reponse_correcte": "Concave",
                                        "explication": "f''(x) = -1/x² < 0 sur ]0;+∞[, donc ln est concave.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Quelle est la dérivée seconde de ln(x) ?",
                                        "reponse_correcte": "-1/x²",
                                        "tolerances": ["-1/x^2", "-x^(-2)"],
                                        "explication": "f''(x) = -1/x².",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La courbe de ln est au-dessus de ses tangentes.",
                                        "reponse_correcte": "faux",
                                        "explication": "Étant concave, la courbe est EN DESSOUS de ses tangentes.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "Comparaison avec la Fonction Exponentielle",
                            "duree": 20,
                            "contenu": r"""## ln et exp : Fonctions Réciproques

### Symétrie axiale

Les courbes $\mathcal{C}_{\exp}$ et $\mathcal{C}_{\ln}$ sont **symétriques par rapport à la droite** $y = x$.

**Justification** : si $M(a\,;\,b) \in \mathcal{C}_{\exp}$, alors $b = e^a$, donc $a = \ln(b)$, et $M'(b\,;\,a) \in \mathcal{C}_{\ln}$.

### Tableau comparatif

| Critère | $\exp$ | $\ln$ |
|---|---|---|
| Ensemble de définition | $\mathbb{R}$ | $]0\,;\,+\infty[$ |
| Ensemble image | $]0\,;\,+\infty[$ | $\mathbb{R}$ |
| Comportement en $-\infty$ (ou $0^+$) | $\lim e^x = 0$ | $\lim \ln(x) = -\infty$ |
| Comportement en $+\infty$ | $\lim e^x = +\infty$ | $\lim \ln(x) = +\infty$ |
| Valeur remarquable | $e^0 = 1$ | $\ln(1) = 0$ |
| Dérivée | $(\exp)' = \exp$ | $(\ln)' = 1/x$ |
| Convexité | Convexe | Concave |

### Croissances comparées

$$\lim_{x \to +\infty} \frac{\ln(x)}{x} = 0$$

L'exponentielle **l'emporte** sur le logarithme en $+\infty$.
""",
                            "quiz": {
                                "titre": "Quiz — Comparaison ln et exp",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "vrai_faux",
                                        "texte": "Les courbes de ln et exp sont symétriques par rapport à y = x.",
                                        "reponse_correcte": "vrai",
                                        "explication": "C'est la propriété géométrique des fonctions réciproques.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Que vaut lim(x→+∞) ln(x)/x ?",
                                        "reponse_correcte": "0",
                                        "tolerances": [],
                                        "explication": "L'exponentielle l'emporte sur le logarithme, donc ln(x)/x → 0.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "L'ensemble image de ln est :",
                                        "choix": ["]0;+∞[", "ℝ", "[0;+∞[", "]-∞;0]"],
                                        "reponse_correcte": "ℝ",
                                        "explication": "ln est une bijection de ]0;+∞[ vers ℝ.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 6,
                            "titre": "Logarithme Népérien et Calcul Intégral",
                            "duree": 25,
                            "contenu": r"""## ln et Intégration

### Définition intégrale

La fonction $\ln$ est l'**unique primitive** de $x \mapsto \frac{1}{x}$ sur $]0\,;\,+\infty[$ qui s'annule en 1 :

$$\ln(x) = \int_1^x \frac{1}{t}\,dt$$

### Primitives de $\frac{u'}{u}$

Si $u$ est dérivable et strictement positive sur un intervalle $I$, alors les primitives de $\dfrac{u'}{u}$ sont :

$$F(x) = \ln(u(x)) + C, \quad C \in \mathbb{R}$$

### Exemples de calcul

$$\int_1^e \frac{1}{t}\,dt = [\ln(t)]_1^e = \ln(e) - \ln(1) = 1 - 0 = 1$$

$$\int_1^2 \frac{2x}{x^2 + 1}\,dx = [\ln(x^2 + 1)]_1^2 = \ln(5) - \ln(2)$$

### Aire sous la courbe

L'aire sous la courbe de $\frac{1}{x}$ entre $1$ et $a$ (avec $a > 1$) vaut $\ln(a)$.
""",
                            "quiz": {
                                "titre": "Quiz — ln et intégration",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Calculer ∫₁ᵉ (1/t) dt.",
                                        "reponse_correcte": "1",
                                        "tolerances": [],
                                        "explication": "∫₁ᵉ (1/t) dt = [ln(t)]₁ᵉ = ln(e) - ln(1) = 1.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "La primitive de u'/u (avec u > 0) est :",
                                        "choix": ["ln(u) + C", "u'/u² + C", "1/u + C", "u·ln(u) + C"],
                                        "reponse_correcte": "ln(u) + C",
                                        "explication": "Les primitives de u'/u sont de la forme ln(u(x)) + C.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "ln(x) = ∫₁ˣ (1/t) dt pour tout x > 0.",
                                        "reponse_correcte": "vrai",
                                        "explication": "C'est la définition intégrale du logarithme népérien.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 7,
                            "titre": "Applications et Exercices Types",
                            "duree": 30,
                            "contenu": r"""## Applications du Logarithme

### Résolution d'équations logarithmiques

Pour résoudre $\ln(A(x)) = \ln(B(x))$ :

1. **Ensemble de validité** : $A(x) > 0$ et $B(x) > 0$
2. **Bijectivité** : $\ln(A) = \ln(B) \iff A = B$ (car $\ln$ strictement croissante)
3. **Vérification** : les solutions doivent appartenir à l'ensemble de validité

### Exemple

Résoudre $\ln(2x - 1) = \ln(x + 3)$.

- Validité : $2x - 1 > 0$ et $x + 3 > 0 \Rightarrow x > \frac{1}{2}$
- Équation : $2x - 1 = x + 3 \Rightarrow x = 4$
- Vérification : $4 > \frac{1}{2}$ ✓

### Croissances comparées

Résultat fondamental :

$$\lim_{x \to +\infty} \frac{\ln(x)}{x} = 0$$

**Démonstration** : posons $X = \ln(x)$, alors $x = e^X$ et quand $x \to +\infty$, $X \to +\infty$.

$$\frac{\ln(x)}{x} = \frac{X}{e^X} \xrightarrow[X \to +\infty]{} 0$$

Car $\lim \frac{e^X}{X} = +\infty$ (l'exponentielle l'emporte).

### Résolution d'inéquations

$\ln(x) > 2 \iff x > e^2$ (croissance de $\ln$)

$\ln(x) < -1 \iff 0 < x < e^{-1} = \frac{1}{e}$
""",
                            "quiz": {
                                "titre": "Quiz — Applications ln",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Résoudre ln(2x-1) = ln(x+3).",
                                        "reponse_correcte": "x = 4",
                                        "tolerances": ["4", "x=4"],
                                        "explication": "2x-1 = x+3, donc x = 4. Vérification : 4 > 1/2 ✓.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "L'inéquation ln(x) > 2 a pour solution :",
                                        "choix": ["x > 2", "x > e²", "x > ln(2)", "x > 2e"],
                                        "reponse_correcte": "x > e²",
                                        "explication": "ln(x) > 2 ⟺ x > e² par croissance de ln.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "lim(x→+∞) ln(x)/x = +∞.",
                                        "reponse_correcte": "faux",
                                        "explication": "Cette limite vaut 0 (croissances comparées).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },

                {
                    "ordre": 8,
                    "titre": "Intégration et Primitives",
                    "description": "Cours complet sur les primitives, l'intégrale de Riemann, le théorème fondamental, les propriétés algébriques, l'intégration par parties, la valeur moyenne et les applications.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Primitives d'une Fonction",
                            "duree": 30,
                            "contenu": r"""## Primitives d'une Fonction

### Définition

Soit $f$ une fonction continue sur un intervalle $I$. On appelle **primitive** de $f$ sur $I$ toute fonction $F$ dérivable sur $I$ telle que :

$$\forall x \in I, \quad F'(x) = f(x)$$

### Propriété fondamentale

Si $F$ est une primitive de $f$ sur $I$, alors **toute** autre primitive $G$ de $f$ sur $I$ est de la forme :

$$G(x) = F(x) + C, \quad C \in \mathbb{R}$$

L'ensemble des primitives forme une **famille de fonctions translatées verticalement**.

### Primitive vérifiant une condition initiale

Pour déterminer l'unique primitive $F$ telle que $F(x_0) = y_0$ :

1. Trouver une primitive générale $F(x) + C$
2. Résoudre $F(x_0) + C = y_0$ pour trouver $C$

### Linéarisation par les formules d'Euler

Pour les puissances de fonctions trigonométriques, on utilise :

$$\cos(x) = \frac{e^{ix} + e^{-ix}}{2}, \quad \sin(x) = \frac{e^{ix} - e^{-ix}}{2i}$$

**Exemple** : $\cos^3(x) = \dfrac{1}{4}\cos(3x) + \dfrac{3}{4}\cos(x)$

D'où la primitive : $F(x) = \dfrac{1}{12}\sin(3x) + \dfrac{3}{4}\sin(x) + C$
""",
                            "quiz": {
                                "titre": "Quiz — Primitives",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Si F est une primitive de f sur I, que peut-on dire des autres primitives de f ?",
                                        "choix": ["Elles sont de la forme F(x) + C", "Elles sont de la forme C × F(x)", "Il n'y en a pas d'autre", "Elles sont de la forme F(x)²"],
                                        "reponse_correcte": "Elles sont de la forme F(x) + C",
                                        "explication": "Deux primitives d'une même fonction diffèrent d'une constante.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Toute fonction continue sur un intervalle admet des primitives.",
                                        "reponse_correcte": "vrai",
                                        "explication": "C'est un théorème fondamental : toute fonction continue sur un intervalle admet des primitives.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Quelle est une primitive de f(x) = 3x² ?",
                                        "reponse_correcte": "x³",
                                        "tolerances": ["x^3", "x³ + C", "x^3 + C"],
                                        "explication": "F(x) = x³ car F'(x) = 3x² = f(x).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Tableaux des Primitives Usuelles et Composées",
                            "duree": 35,
                            "contenu": r"""## Primitives Usuelles et Composées

### Tableau 1 : Primitives des fonctions usuelles

| Fonction $f(x)$ | Primitive $F(x)$ | Conditions |
|---|---|---|
| $a$ (constante) | $ax + C$ | $\mathbb{R}$ |
| $x^n$ | $\dfrac{x^{n+1}}{n+1} + C$ | $n \neq -1$ |
| $\dfrac{1}{x}$ | $\ln\|x\| + C$ | $x \neq 0$ |
| $e^x$ | $e^x + C$ | $\mathbb{R}$ |
| $e^{ax+b}$ | $\dfrac{1}{a}e^{ax+b} + C$ | $a \neq 0$ |
| $\cos(x)$ | $\sin(x) + C$ | $\mathbb{R}$ |
| $\sin(x)$ | $-\cos(x) + C$ | $\mathbb{R}$ |

### Tableau 2 : Primitives des fonctions composées

Pour $u$ dérivable sur $I$ :

| Forme | Primitive | Conditions |
|---|---|---|
| $u' \cdot u^n$ | $\dfrac{u^{n+1}}{n+1} + C$ | $n \neq -1$ |
| $\dfrac{u'}{u}$ | $\ln\|u\| + C$ | $u \neq 0$ |
| $u' \cdot e^u$ | $e^u + C$ | — |
| $u' \cos(u)$ | $\sin(u) + C$ | — |
| $u' \sin(u)$ | $-\cos(u) + C$ | — |

### Méthode de reconnaissance

1. **Identifier** la forme composée ($u'u^n$, $u'/u$, $u'e^u$...)
2. **Repérer** $u$ et vérifier que le numérateur/facteur contient $u'$
3. **Ajuster** le coefficient si nécessaire

### Exemple

$\displaystyle\int \frac{2x}{x^2+1}\,dx$ : on pose $u = x^2+1$, $u' = 2x$. C'est la forme $\dfrac{u'}{u}$, donc la primitive est $\ln(x^2+1) + C$.
""",
                            "quiz": {
                                "titre": "Quiz — Primitives usuelles",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quelle est une primitive de e^(2x) ?",
                                        "reponse_correcte": "(1/2)e^(2x)",
                                        "tolerances": ["e^(2x)/2", "(1/2)e^(2x) + C", "e^(2x)/2 + C"],
                                        "explication": "La primitive de e^(ax) est (1/a)e^(ax), ici a = 2.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Quelle est la primitive de u'/u ?",
                                        "choix": ["ln|u| + C", "u² + C", "1/u + C", "e^u + C"],
                                        "reponse_correcte": "ln|u| + C",
                                        "explication": "C'est la forme logarithmique : la primitive de u'/u est ln|u| + C.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Quelle est une primitive de cos(x) ?",
                                        "reponse_correcte": "sin(x)",
                                        "tolerances": ["sin(x) + C", "sinx"],
                                        "explication": "La primitive de cos(x) est sin(x) + C.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Intégrale de Riemann et Notion d'Aire",
                            "duree": 35,
                            "contenu": r"""## Intégrale de Riemann

### Approche géométrique

Pour une fonction $f$ **continue et positive** sur $[a ; b]$, l'intégrale :

$$\int_{a}^{b} f(x)\,dx$$

représente l'**aire** du domaine délimité par :
- la courbe $\mathcal{C}_f$
- l'axe des abscisses
- les droites $x = a$ et $x = b$

### Construction par les sommes de Riemann

On subdivise $[a ; b]$ en $n$ sous-intervalles de largeur $\Delta x = \dfrac{b-a}{n}$.

**Somme de Riemann** (rectangles à gauche) :

$$S_n = \sum_{k=0}^{n-1} f(a + k\Delta x) \cdot \Delta x$$

L'intégrale est la **limite** de ces sommes quand $n \to +\infty$ :

$$\int_{a}^{b} f(x)\,dx = \lim_{n \to +\infty} S_n$$

### Interprétation en probabilités

Pour une variable aléatoire continue $X$ de densité $f$ :

$$P(a \leq X \leq b) = \int_{a}^{b} f(x)\,dx$$

L'aire sous la courbe de densité représente la probabilité.

### Cas d'une fonction négative

Si $f(x) \leq 0$ sur $[a ; b]$, alors $\displaystyle\int_{a}^{b} f(x)\,dx \leq 0$.

L'aire géométrique est $\displaystyle\left|\int_{a}^{b} f(x)\,dx\right|$.
""",
                            "quiz": {
                                "titre": "Quiz — Intégrale de Riemann",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "vrai_faux",
                                        "texte": "L'intégrale d'une fonction positive sur [a ; b] représente l'aire sous la courbe.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Pour f ≥ 0 sur [a ; b], ∫ₐᵇ f(x) dx = aire du domaine entre la courbe, l'axe Ox et les droites x=a, x=b.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Comment s'interprète ∫ₐᵇ f(x) dx en probabilités (f densité) ?",
                                        "choix": ["P(X = a)", "P(a ≤ X ≤ b)", "E(X)", "V(X)"],
                                        "reponse_correcte": "P(a ≤ X ≤ b)",
                                        "explication": "Pour une VA continue X de densité f, P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Une intégrale est toujours positive.",
                                        "reponse_correcte": "faux",
                                        "explication": "Si f est négative sur [a ; b], l'intégrale est négative. Seule l'aire géométrique est toujours positive.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "Le Théorème Fondamental de l'Analyse",
                            "duree": 30,
                            "contenu": r"""## Théorème Fondamental

### Énoncé

Soit $f$ une fonction **continue** sur $[a ; b]$. Si $F$ est une primitive de $f$ sur $[a ; b]$, alors :

$$\int_{a}^{b} f(x)\,dx = \Big[F(x)\Big]_{a}^{b} = F(b) - F(a)$$

Ce théorème établit le **pont** entre le calcul intégral (aire) et le calcul différentiel (primitives).

### Notation crochet

$$\Big[F(x)\Big]_{a}^{b} = F(b) - F(a)$$

### Méthode de calcul

1. Trouver une primitive $F$ de $f$
2. Calculer $F(b)$ et $F(a)$
3. Faire la différence $F(b) - F(a)$

### Exemples

**Exemple 1** :

$$\int_{0}^{1} x^2\,dx = \left[\frac{x^3}{3}\right]_{0}^{1} = \frac{1}{3} - 0 = \frac{1}{3}$$

**Exemple 2** :

$$\int_{1}^{e} \frac{1}{x}\,dx = \Big[\ln(x)\Big]_{1}^{e} = \ln(e) - \ln(1) = 1 - 0 = 1$$

**Exemple 3** (densité de probabilité) :

Pour $f(x) = 0{,}015x - 0{,}00075x^2$ sur $[0 ; 20]$ :

$$\int_{0}^{20} f(x)\,dx = \Big[0{,}0075x^2 - 0{,}00025x^3\Big]_{0}^{20} = 3 - 2 = 1$$

La condition de normalisation est vérifiée.
""",
                            "quiz": {
                                "titre": "Quiz — Théorème fondamental",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Calculer ∫₀¹ x² dx.",
                                        "reponse_correcte": "1/3",
                                        "tolerances": ["0.333", "0,333"],
                                        "explication": "∫₀¹ x² dx = [x³/3]₀¹ = 1/3 - 0 = 1/3.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Calculer ∫₁ᵉ (1/x) dx.",
                                        "reponse_correcte": "1",
                                        "tolerances": [],
                                        "explication": "∫₁ᵉ (1/x) dx = [ln(x)]₁ᵉ = ln(e) - ln(1) = 1 - 0 = 1.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Le théorème fondamental relie :",
                                        "choix": ["Les limites et la continuité", "Les primitives et les intégrales", "Les dérivées et les limites", "Les suites et les fonctions"],
                                        "reponse_correcte": "Les primitives et les intégrales",
                                        "explication": "Le théorème fondamental établit que ∫ₐᵇ f(x)dx = F(b) - F(a) où F est une primitive de f.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "Propriétés Algébriques de l'Intégrale",
                            "duree": 30,
                            "contenu": r"""## Propriétés Algébriques

### Relation de Chasles

Pour tout $c \in [a ; b]$ :

$$\int_{a}^{b} f(x)\,dx = \int_{a}^{c} f(x)\,dx + \int_{c}^{b} f(x)\,dx$$

### Linéarité

Pour tous réels $\alpha, \beta$ :

$$\int_{a}^{b} \big(\alpha f(x) + \beta g(x)\big)\,dx = \alpha \int_{a}^{b} f(x)\,dx + \beta \int_{a}^{b} g(x)\,dx$$

### Conventions

- $\displaystyle\int_{a}^{a} f(x)\,dx = 0$
- $\displaystyle\int_{b}^{a} f(x)\,dx = -\int_{a}^{b} f(x)\,dx$

### Signe et aires

L'intégrale peut être **négative** si $f$ change de signe.

Pour calculer l'**aire géométrique** quand $f$ change de signe en $c \in [a ; b]$ :

$$\mathcal{A} = \int_{a}^{c} f(x)\,dx - \int_{c}^{b} f(x)\,dx$$

(si $f \geq 0$ sur $[a ; c]$ et $f \leq 0$ sur $[c ; b]$)

### Aire entre deux courbes

Si $f(x) \geq g(x)$ sur $[a ; b]$ :

$$\mathcal{A} = \int_{a}^{b} \big(f(x) - g(x)\big)\,dx$$
""",
                            "quiz": {
                                "titre": "Quiz — Propriétés de l'intégrale",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La relation de Chasles affirme que :",
                                        "choix": ["∫ₐᵇ f = ∫ₐᶜ f + ∫ᶜᵇ f", "∫ₐᵇ f = ∫ₐᵇ f' ", "∫ₐᵇ (f+g) = ∫ₐᵇ f × ∫ₐᵇ g", "∫ₐᵇ f = f(b) - f(a)"],
                                        "reponse_correcte": "∫ₐᵇ f = ∫ₐᶜ f + ∫ᶜᵇ f",
                                        "explication": "La relation de Chasles découpe l'intégrale en sous-intervalles.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "∫ₐᵃ f(x) dx = 0 pour toute fonction f continue.",
                                        "reponse_correcte": "vrai",
                                        "explication": "L'intégrale sur un intervalle de longueur nulle est toujours 0.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "∫ᵇₐ f(x) dx = ∫ₐᵇ f(x) dx.",
                                        "reponse_correcte": "faux",
                                        "explication": "∫ᵇₐ f(x) dx = -∫ₐᵇ f(x) dx. L'inversion des bornes change le signe.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 6,
                            "titre": "Intégration par Parties",
                            "duree": 35,
                            "contenu": r"""## Intégration par Parties (IPP)

### Théorème

Soient $u$ et $v$ deux fonctions de classe $\mathcal{C}^1$ sur $[a ; b]$. On a :

$$\int_{a}^{b} u(x)\,v'(x)\,dx = \Big[u(x)\,v(x)\Big]_{a}^{b} - \int_{a}^{b} u'(x)\,v(x)\,dx$$

### Origine

C'est la transposition de la formule de dérivation d'un produit :

$$(uv)' = u'v + uv' \implies uv' = (uv)' - u'v$$

En intégrant les deux membres sur $[a ; b]$, on obtient la formule d'IPP.

### Méthode

1. **Choisir** $u$ et $v'$ (on dérive $u$, on primitive $v'$)
2. **Calculer** $u'$ et $v$
3. **Appliquer** la formule

### Règle de choix (LIATE)

Ordre de priorité pour le choix de $u$ :
- **L**ogarithme, **I**nverse trigo, **A**lgébrique, **T**rigo, **E**xponentielle

### Exemples

**Exemple 1** : $\displaystyle\int_{0}^{1} x\,e^x\,dx$

On pose $u = x$, $v' = e^x$, donc $u' = 1$, $v = e^x$.

$$\int_{0}^{1} x\,e^x\,dx = \Big[x\,e^x\Big]_{0}^{1} - \int_{0}^{1} e^x\,dx = e - \Big[e^x\Big]_{0}^{1} = e - (e - 1) = 1$$

**Exemple 2** : $\displaystyle\int_{1}^{e} \ln(x)\,dx$

On pose $u = \ln(x)$, $v' = 1$, donc $u' = \dfrac{1}{x}$, $v = x$.

$$\int_{1}^{e} \ln(x)\,dx = \Big[x\ln(x)\Big]_{1}^{e} - \int_{1}^{e} 1\,dx = e - (e - 1) = 1$$
""",
                            "quiz": {
                                "titre": "Quiz — IPP",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Calculer ∫₁ᵉ ln(x) dx.",
                                        "reponse_correcte": "1",
                                        "tolerances": [],
                                        "explication": "Par IPP avec u=ln(x) et v'=1 : [x·ln(x)]₁ᵉ - ∫₁ᵉ dx = e - (e-1) = 1.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Dans la formule d'IPP, ∫ u·v' dx = ?",
                                        "choix": ["[uv] - ∫ u'·v dx", "[uv] + ∫ u'·v dx", "u·v - ∫ u'·v' dx", "[u'v'] - ∫ uv dx"],
                                        "reponse_correcte": "[uv] - ∫ u'·v dx",
                                        "explication": "La formule d'IPP est ∫ u·v' = [uv] - ∫ u'·v.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "L'IPP provient de la formule de dérivation d'un produit.",
                                        "reponse_correcte": "vrai",
                                        "explication": "(uv)' = u'v + uv', donc uv' = (uv)' - u'v. En intégrant, on obtient l'IPP.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 7,
                            "titre": "Comparaison, Inégalités et Valeur Moyenne",
                            "duree": 30,
                            "contenu": r"""## Propriétés de Comparaison et Valeur Moyenne

### Positivité de l'intégrale

Si $f \geq 0$ sur $[a ; b]$ avec $a \leq b$, alors :

$$\int_{a}^{b} f(x)\,dx \geq 0$$

### Comparaison

Si $f(x) \leq g(x)$ pour tout $x \in [a ; b]$, alors :

$$\int_{a}^{b} f(x)\,dx \leq \int_{a}^{b} g(x)\,dx$$

### Inégalité de la moyenne

Si $m \leq f(x) \leq M$ sur $[a ; b]$, alors :

$$m(b - a) \leq \int_{a}^{b} f(x)\,dx \leq M(b - a)$$

### Valeur moyenne

La **valeur moyenne** de $f$ sur $[a ; b]$ est :

$$\mu = \frac{1}{b - a}\int_{a}^{b} f(x)\,dx$$

C'est la hauteur du rectangle de même base $[a ; b]$ ayant la même aire que le domaine sous la courbe.

### Distinction avec l'espérance

| Notion | Formule | Interprétation |
|---|---|---|
| Valeur moyenne de $f$ | $\mu = \dfrac{1}{b-a}\displaystyle\int_{a}^{b} f(x)\,dx$ | Moyenne des valeurs de $f$ |
| Espérance de $X$ | $E(X) = \displaystyle\int_{a}^{b} x\,f(x)\,dx$ | Moyenne pondérée des valeurs de $X$ |

### Inégalité triangulaire

$$\left|\int_{a}^{b} f(x)\,dx\right| \leq \int_{a}^{b} |f(x)|\,dx$$
""",
                            "quiz": {
                                "titre": "Quiz — Comparaison et valeur moyenne",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La valeur moyenne de f sur [a ; b] est :",
                                        "choix": ["(f(a) + f(b)) / 2", "∫ₐᵇ f(x) dx", "(1/(b-a)) ∫ₐᵇ f(x) dx", "f((a+b)/2)"],
                                        "reponse_correcte": "(1/(b-a)) ∫ₐᵇ f(x) dx",
                                        "explication": "La valeur moyenne est μ = (1/(b-a)) ∫ₐᵇ f(x) dx.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Si f ≥ 0 sur [a ; b], alors ∫ₐᵇ f(x) dx ≥ 0.",
                                        "reponse_correcte": "vrai",
                                        "explication": "C'est la propriété de positivité de l'intégrale.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La valeur moyenne de f et l'espérance de X (de densité f) sont la même chose.",
                                        "reponse_correcte": "faux",
                                        "explication": "La valeur moyenne est (1/(b-a))∫f dx, l'espérance est ∫x·f(x) dx. Ce sont deux notions différentes.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 8,
                            "titre": "Applications et Exercices d'Illustration",
                            "duree": 35,
                            "contenu": r"""## Applications

### Exercice 1 : Loi uniforme

On considère une loi uniforme sur $[0 ; 60]$ de densité $f(x) = \dfrac{1}{60}$.

$$P(15 \leq X \leq 40) = \int_{15}^{40} \frac{1}{60}\,dx = \left[\frac{x}{60}\right]_{15}^{40} = \frac{40 - 15}{60} = \frac{25}{60} = \frac{5}{12}$$

L'espérance est $E(X) = \dfrac{0 + 60}{2} = 30$.

### Exercice 2 : Coût marginal et coût total

Le coût marginal est $C'(x) = 0{,}15x^2 - 2{,}1x + 8$ avec $C(0) = 4$ (milliers d'euros).

Par intégration :

$$C(x) = \int C'(x)\,dx = 0{,}05x^3 - 1{,}05x^2 + 8x + K$$

Condition initiale : $C(0) = 4 \implies K = 4$.

$$C(x) = 0{,}05x^3 - 1{,}05x^2 + 8x + 4$$

### Exercice 3 : Aire entre deux courbes

Calculer l'aire entre $f(x) = x^2$ et $g(x) = x$ sur $[0 ; 1]$.

On a $g(x) \geq f(x)$ sur $[0 ; 1]$, donc :

$$\mathcal{A} = \int_{0}^{1} (x - x^2)\,dx = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_{0}^{1} = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$$

### Exercice 4 : Valeur moyenne

Calculer la valeur moyenne de $f(x) = \sin(x)$ sur $[0 ; \pi]$ :

$$\mu = \frac{1}{\pi - 0}\int_{0}^{\pi} \sin(x)\,dx = \frac{1}{\pi}\Big[-\cos(x)\Big]_{0}^{\pi} = \frac{1}{\pi}(1 + 1) = \frac{2}{\pi}$$
""",
                            "quiz": {
                                "titre": "Quiz — Applications de l'intégration",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Calculer l'aire entre f(x) = x² et g(x) = x sur [0 ; 1] (g ≥ f).",
                                        "reponse_correcte": "1/6",
                                        "tolerances": ["0.167", "0,167"],
                                        "explication": "∫₀¹ (x - x²) dx = [x²/2 - x³/3]₀¹ = 1/2 - 1/3 = 1/6.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Quelle est la valeur moyenne de sin(x) sur [0 ; π] ?",
                                        "reponse_correcte": "2/π",
                                        "tolerances": ["2/pi", "0.637"],
                                        "explication": "μ = (1/π)∫₀π sin(x) dx = (1/π)[-cos(x)]₀π = (1/π)(1+1) = 2/π.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "L'intégration permet de passer du coût marginal au coût total.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Le coût total C(x) est une primitive du coût marginal C'(x), ajustée par la condition initiale C(0).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                {
                    "ordre": 9,
                    "titre": "Les Nombres Complexes",
                    "description": "Cours complet sur les nombres complexes : forme algébrique, conjugué, module et argument, forme trigonométrique et exponentielle, formules d'Euler et de Moivre, équations polynomiales et applications géométriques.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Introduction et Fondements de l'Ensemble C",
                            "duree": 30,
                            "contenu": r"""## Introduction et Fondements de $\mathbb{C}$

### Motivation

L'ensemble $\mathbb{C}$ des nombres complexes a été conçu pour résoudre des équations impossibles dans $\mathbb{R}$, comme $x^2 + 1 = 0$.

### Unité imaginaire

L'ensemble $\mathbb{C}$ contient $\mathbb{R}$ et possède un élément $i$ tel que :

$$i^2 = -1$$

### Forme algébrique

Tout nombre complexe $z$ s'écrit de manière **unique** sous la forme :

$$z = a + ib, \quad (a, b) \in \mathbb{R}^2$$

- $a = \text{Re}(z)$ : **partie réelle**
- $b = \text{Im}(z)$ : **partie imaginaire**

### Condition d'égalité

$$a + ib = a' + ib' \iff \begin{cases} a = a' \\ b = b' \end{cases}$$

### Opérations fondamentales

**Addition** :

$$(a + ib) + (a' + ib') = (a + a') + i(b + b')$$

**Multiplication** :

$$(a + ib)(a' + ib') = (aa' - bb') + i(ab' + ba')$$

### Cas particuliers

- $z$ est **réel** si $\text{Im}(z) = 0$
- $z$ est **imaginaire pur** si $\text{Re}(z) = 0$
""",
                            "quiz": {
                                "titre": "Quiz — Fondements de C",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Que vaut i² ?",
                                        "reponse_correcte": "-1",
                                        "tolerances": [],
                                        "explication": "Par définition, i² = -1. C'est la propriété fondamentale de l'unité imaginaire.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Quelle est la partie imaginaire de z = 3 - 2i ?",
                                        "choix": ["3", "-2", "2", "-2i"],
                                        "reponse_correcte": "-2",
                                        "explication": "Pour z = a + ib, Im(z) = b. Ici z = 3 + i(-2), donc Im(z) = -2.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Deux nombres complexes sont égaux si et seulement si ils ont la même partie réelle et la même partie imaginaire.",
                                        "reponse_correcte": "vrai",
                                        "explication": "C'est la condition d'égalité dans C : a + ib = a' + ib' ⟺ a = a' et b = b'.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Conjugué et Propriétés Algébriques",
                            "duree": 30,
                            "contenu": r"""## Conjugué et Propriétés

### Définition

Pour $z = a + ib$, le **conjugué** de $z$ est :

$$\bar{z} = a - ib$$

Géométriquement, le point d'affixe $\bar{z}$ est le symétrique du point d'affixe $z$ par rapport à l'axe des réels.

### Propriétés du conjugué

Pour tous $z, z' \in \mathbb{C}$ et $n \in \mathbb{N}$ :

| Propriété | Formule |
|---|---|
| Linéarité | $\overline{z + z'} = \bar{z} + \bar{z}'$ |
| Produit | $\overline{z \times z'} = \bar{z} \times \bar{z}'$ |
| Puissance | $\overline{z^n} = (\bar{z})^n$ |
| Quotient | $\overline{\left(\frac{z}{z'}\right)} = \frac{\bar{z}}{\bar{z}'}$ |

### Caractérisation

- $z$ est **réel** $\iff z = \bar{z}$
- $z$ est **imaginaire pur** $\iff z = -\bar{z}$

### Relation fondamentale

$$z\bar{z} = (a + ib)(a - ib) = a^2 + b^2$$

Ce produit est toujours un **réel positif** et correspond au carré du module de $z$.

### Application : Division de complexes

Pour calculer $\dfrac{z}{z'}$, on multiplie numérateur et dénominateur par $\bar{z}'$ :

$$\frac{z}{z'} = \frac{z \cdot \bar{z}'}{z' \cdot \bar{z}'} = \frac{z \cdot \bar{z}'}{|z'|^2}$$
""",
                            "quiz": {
                                "titre": "Quiz — Conjugué",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quel est le conjugué de z = 2 + 3i ?",
                                        "reponse_correcte": "2 - 3i",
                                        "tolerances": ["2-3i"],
                                        "explication": "Le conjugué de a + ib est a - ib, donc le conjugué de 2 + 3i est 2 - 3i.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "z est réel si et seulement si z = conjugué(z).",
                                        "reponse_correcte": "vrai",
                                        "explication": "Si z = a + ib, alors z = z̄ ⟺ b = 0 ⟺ z est réel.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Que vaut z × conjugué(z) si z = 1 + 2i ?",
                                        "reponse_correcte": "5",
                                        "tolerances": [],
                                        "explication": "z·z̄ = (1+2i)(1-2i) = 1 + 4 = 5.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Affixe, Module et Argument",
                            "duree": 35,
                            "contenu": r"""## Interprétations Géométriques

### Affixe d'un point

Dans le plan muni d'un repère orthonormé direct $(O ; \vec{u}, \vec{v})$, à tout nombre complexe $z = a + ib$ on associe le point $M(a ; b)$.

- $z$ est l'**affixe** du point $M$, noté $M(z)$
- Pour un vecteur $\vec{w}(x ; y)$, son affixe est $z_{\vec{w}} = x + iy$

### Module

Le **module** de $z = a + ib$ est :

$$|z| = \sqrt{a^2 + b^2} = \sqrt{z\bar{z}}$$

Il représente la **distance** $OM$.

### Propriétés du module

- $|z| \geq 0$ et $|z| = 0 \iff z = 0$
- $|z \cdot z'| = |z| \cdot |z'|$
- $\left|\dfrac{z}{z'}\right| = \dfrac{|z|}{|z'|}$
- $|z^n| = |z|^n$
- **Inégalité triangulaire** : $|z + z'| \leq |z| + |z'|$

### Argument

Pour $z \neq 0$, l'**argument** de $z$, noté $\arg(z)$, est l'angle $(\vec{u}, \overrightarrow{OM})$ défini **modulo $2\pi$**.

### Détermination de l'argument

Pour $z = a + ib$ avec $|z| = r$ :

$$\cos(\arg(z)) = \frac{a}{r}, \quad \sin(\arg(z)) = \frac{b}{r}$$

### Distance et milieu

- **Distance** : $AB = |z_B - z_A|$
- **Milieu** : $z_I = \dfrac{z_A + z_B}{2}$
""",
                            "quiz": {
                                "titre": "Quiz — Module et argument",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Calculer le module de z = 3 + 4i.",
                                        "reponse_correcte": "5",
                                        "tolerances": [],
                                        "explication": "|z| = √(3² + 4²) = √(9 + 16) = √25 = 5.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Le module de z représente géométriquement :",
                                        "choix": ["L'aire du triangle OMz", "La distance OM", "L'angle (Ox, OM)", "La partie réelle de z"],
                                        "reponse_correcte": "La distance OM",
                                        "explication": "|z| = √(a² + b²) est la distance de l'origine O au point M d'affixe z.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "|z × z'| = |z| × |z'| pour tous z, z' complexes.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Le module est multiplicatif : le module d'un produit est le produit des modules.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "Rappels de Trigonométrie pour les Complexes",
                            "duree": 25,
                            "contenu": r"""## Outils de Trigonométrie

### Valeurs remarquables

| $x$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\pi$ |
|---|---|---|---|---|---|---|
| $\cos(x)$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ | $-1$ |
| $\sin(x)$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ | $0$ |
| $\tan(x)$ | $0$ | $\frac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ | — | $0$ |

### Formules d'addition

$$\cos(a \pm b) = \cos a \cos b \mp \sin a \sin b$$

$$\sin(a \pm b) = \sin a \cos b \pm \cos a \sin b$$

### Formules de duplication

$$\cos(2a) = \cos^2 a - \sin^2 a = 2\cos^2 a - 1 = 1 - 2\sin^2 a$$

$$\sin(2a) = 2\sin a \cos a$$

### Formule fondamentale

$$\cos^2(x) + \sin^2(x) = 1$$

Ces formules sont essentielles pour la détermination des formes trigonométrique et exponentielle des nombres complexes.
""",
                            "quiz": {
                                "titre": "Quiz — Trigonométrie",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Que vaut cos(π/3) ?",
                                        "reponse_correcte": "1/2",
                                        "tolerances": ["0.5", "0,5"],
                                        "explication": "cos(π/3) = 1/2 est une valeur remarquable à connaître.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "La formule de cos(a + b) est :",
                                        "choix": ["cos(a)cos(b) - sin(a)sin(b)", "cos(a)cos(b) + sin(a)sin(b)", "sin(a)cos(b) + cos(a)sin(b)", "cos(a) + cos(b)"],
                                        "reponse_correcte": "cos(a)cos(b) - sin(a)sin(b)",
                                        "explication": "cos(a + b) = cos(a)cos(b) - sin(a)sin(b).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Que vaut sin(2a) en fonction de sin(a) et cos(a) ?",
                                        "reponse_correcte": "2sin(a)cos(a)",
                                        "tolerances": ["2 sin(a) cos(a)", "2sinacosa"],
                                        "explication": "sin(2a) = 2sin(a)cos(a) est la formule de duplication du sinus.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "Forme Trigonométrique et Notation Exponentielle",
                            "duree": 40,
                            "contenu": r"""## Forme Trigonométrique et Exponentielle

### Forme trigonométrique

Tout nombre complexe non nul $z$ de module $r$ et d'argument $\theta$ s'écrit :

$$z = r(\cos\theta + i\sin\theta)$$

### Notation exponentielle (formule d'Euler)

Pour tout réel $\theta$ :

$$e^{i\theta} = \cos\theta + i\sin\theta$$

D'où la **forme exponentielle** : $z = r\,e^{i\theta}$

### Méthode : passage algébrique → exponentielle

Pour $z = 3 - 3i$ :

1. **Module** : $r = |z| = \sqrt{9 + 9} = 3\sqrt{2}$
2. **Argument** : $\cos\theta = \frac{3}{3\sqrt{2}} = \frac{\sqrt{2}}{2}$, $\sin\theta = \frac{-3}{3\sqrt{2}} = -\frac{\sqrt{2}}{2}$
3. Donc $\theta = -\frac{\pi}{4}$
4. **Résultat** : $z = 3\sqrt{2}\,e^{-i\frac{\pi}{4}}$

### Formule de Moivre

Pour tout $n \in \mathbb{N}$ et $\theta \in \mathbb{R}$ :

$$(e^{i\theta})^n = e^{in\theta} \iff (\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$$

### Formules d'Euler

$$\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}, \quad \sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$$

### Propriétés de l'exponentielle complexe

- $e^{i\theta} \times e^{i\theta'} = e^{i(\theta + \theta')}$
- $\dfrac{1}{e^{i\theta}} = e^{-i\theta} = \overline{e^{i\theta}}$
- **Relation d'Euler** : $e^{i\pi} = -1$, soit $e^{i\pi} + 1 = 0$
""",
                            "quiz": {
                                "titre": "Quiz — Forme exponentielle",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Écrire e^(iπ) sous forme algébrique.",
                                        "reponse_correcte": "-1",
                                        "tolerances": ["-1 + 0i"],
                                        "explication": "e^(iπ) = cos(π) + i·sin(π) = -1 + 0i = -1. C'est la relation d'Euler.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "La formule de Moivre affirme que (cos θ + i sin θ)ⁿ = ?",
                                        "choix": ["cos(nθ) + i sin(nθ)", "n cos θ + i n sin θ", "cosⁿ(θ) + i sinⁿ(θ)", "cos(θ/n) + i sin(θ/n)"],
                                        "reponse_correcte": "cos(nθ) + i sin(nθ)",
                                        "explication": "(cos θ + i sin θ)ⁿ = cos(nθ) + i sin(nθ), c'est la formule de Moivre.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Quel est le module de z = 3 - 3i ?",
                                        "reponse_correcte": "3√2",
                                        "tolerances": ["3*sqrt(2)", "3 racine de 2", "4.24"],
                                        "explication": "|z| = √(9 + 9) = √18 = 3√2.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 6,
                            "titre": "Équations du Second Degré dans C",
                            "duree": 35,
                            "contenu": r"""## Équations Polynomiales dans $\mathbb{C}$

### Résolution de $az^2 + bz + c = 0$ avec $a, b, c \in \mathbb{R}$

On calcule le discriminant $\Delta = b^2 - 4ac$.

| Cas | Solutions |
|---|---|
| $\Delta > 0$ | $z_1 = \dfrac{-b - \sqrt{\Delta}}{2a}$, $z_2 = \dfrac{-b + \sqrt{\Delta}}{2a}$ (réelles) |
| $\Delta = 0$ | $z_0 = -\dfrac{b}{2a}$ (réelle double) |
| $\Delta < 0$ | $z_1 = \dfrac{-b - i\sqrt{|\Delta|}}{2a}$, $z_2 = \dfrac{-b + i\sqrt{|\Delta|}}{2a}$ (complexes conjuguées) |

### Exemple

Résoudre $z^2 + z + 1 = 0$ :

- $\Delta = 1 - 4 = -3 < 0$
- $z_1 = \dfrac{-1 - i\sqrt{3}}{2}$ et $z_2 = \dfrac{-1 + i\sqrt{3}}{2}$

Les solutions sont complexes conjuguées.

### Théorème fondamental de l'algèbre

Tout polynôme non constant de degré $n$ admet **exactement $n$ racines** dans $\mathbb{C}$ (comptées avec multiplicité).

### Factorisation

Si $z_0$ est racine de $P(z)$, alors :

$$P(z) = (z - z_0)\,Q(z), \quad \deg(Q) = \deg(P) - 1$$

### Propriété des racines conjuguées

Si $P$ est à coefficients **réels** et $z_0$ est racine de $P$, alors $\bar{z}_0$ est aussi racine de $P$.
""",
                            "quiz": {
                                "titre": "Quiz — Équations dans C",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quand Δ < 0 pour az² + bz + c = 0 (a,b,c réels), les solutions sont :",
                                        "choix": ["Deux réelles distinctes", "Une réelle double", "Deux complexes conjuguées", "Il n'y a pas de solution"],
                                        "reponse_correcte": "Deux complexes conjuguées",
                                        "explication": "Quand Δ < 0, les solutions sont z = (-b ± i√|Δ|) / (2a), complexes conjuguées.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Calculer le discriminant de z² + z + 1 = 0.",
                                        "reponse_correcte": "-3",
                                        "tolerances": [],
                                        "explication": "Δ = b² - 4ac = 1 - 4(1)(1) = 1 - 4 = -3.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Un polynôme de degré n à coefficients complexes admet exactement n racines dans C (comptées avec multiplicité).",
                                        "reponse_correcte": "vrai",
                                        "explication": "C'est le théorème fondamental de l'algèbre (théorème de d'Alembert-Gauss).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 7,
                            "titre": "Racines n-ièmes de l'Unité",
                            "duree": 35,
                            "contenu": r"""## Racines n-ièmes

### Racines n-ièmes de l'unité

Les solutions de $z^n = 1$ sont :

$$\omega_k = e^{i\frac{2k\pi}{n}}, \quad k \in \{0, 1, \ldots, n-1\}$$

**Démonstration** :
1. On pose $z = e^{i\theta}$, l'équation devient $e^{in\theta} = e^{i \cdot 0}$
2. Donc $n\theta = 2k\pi$, soit $\theta_k = \dfrac{2k\pi}{n}$
3. Il y a exactement $n$ valeurs distinctes pour $k \in \{0, 1, \ldots, n-1\}$

### Interprétation géométrique

Les points d'affixe $\omega_k$ sont les **sommets d'un polygone régulier** à $n$ côtés, inscrit dans le cercle unité, avec un sommet en $1$.

### Propriétés

- $\omega_0 = 1$
- $\omega_1 = e^{i\frac{2\pi}{n}}$ est la racine primitive
- $\omega_k = (\omega_1)^k$
- $\displaystyle\sum_{k=0}^{n-1} \omega_k = 0$

### Racines n-ièmes d'un complexe $Z = Re^{i\Phi}$

Pour résoudre $z^n = Z$ :

1. Poser $z = re^{i\theta}$
2. **Modules** : $r^n = R \implies r = \sqrt[n]{R}$
3. **Arguments** : $n\theta = \Phi + 2k\pi \implies \theta_k = \dfrac{\Phi}{n} + \dfrac{2k\pi}{n}$
4. On obtient $n$ solutions pour $k \in \{0, 1, \ldots, n-1\}$

### Exemple : racines carrées de $i$

$i = e^{i\frac{\pi}{2}}$, donc $z = e^{i\frac{\pi}{4}}$ ou $z = e^{i\frac{5\pi}{4}}$, soit $z = \dfrac{\sqrt{2}}{2}(1+i)$ ou $z = -\dfrac{\sqrt{2}}{2}(1+i)$.
""",
                            "quiz": {
                                "titre": "Quiz — Racines n-ièmes",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Combien de racines cubiques de l'unité existe-t-il ?",
                                        "reponse_correcte": "3",
                                        "tolerances": ["trois"],
                                        "explication": "L'équation z³ = 1 admet exactement 3 solutions dans C.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Les racines n-ièmes de l'unité forment un polygone régulier inscrit dans le cercle unité.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Les n racines sont régulièrement espacées sur le cercle unité, formant un polygone régulier à n côtés.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "La somme de toutes les racines n-ièmes de l'unité vaut :",
                                        "choix": ["0", "1", "n", "-1"],
                                        "reponse_correcte": "0",
                                        "explication": "La somme des racines n-ièmes de l'unité est toujours 0 (pour n ≥ 2).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 8,
                            "titre": "Applications Géométriques des Complexes",
                            "duree": 35,
                            "contenu": r"""## Applications à la Géométrie du Plan

### Outils fondamentaux

| Notion | Formule complexe |
|---|---|
| **Distance** $AB$ | $\|z_B - z_A\|$ |
| **Milieu** de $[AB]$ | $z_I = \dfrac{z_A + z_B}{2}$ |
| **Angle** $(\overrightarrow{AB}, \overrightarrow{CD})$ | $\arg\!\left(\dfrac{z_D - z_C}{z_B - z_A}\right)$ |
| **Barycentre** | $z_G = \dfrac{\sum \alpha_i z_i}{\sum \alpha_i}$ |

### Transformations du plan

| Transformation | Écriture complexe |
|---|---|
| **Translation** de vecteur $\vec{u}$ d'affixe $b$ | $z' = z + b$ |
| **Homothétie** de centre $\Omega(\omega)$, rapport $k$ | $z' - \omega = k(z - \omega)$ |
| **Rotation** de centre $\Omega(\omega)$, angle $\theta$ | $z' - \omega = e^{i\theta}(z - \omega)$ |
| **Similitude directe** | $z' = az + b$ avec $a \in \mathbb{C}^*$ |

### Alignement et orthogonalité

Trois points $A$, $B$, $C$ sont **alignés** si et seulement si $\dfrac{z_C - z_A}{z_B - z_A}$ est **réel**.

Les droites $(AB)$ et $(CD)$ sont **perpendiculaires** si et seulement si $\dfrac{z_D - z_C}{z_B - z_A}$ est **imaginaire pur**.

### Cercle

Le point $M(z)$ appartient au cercle de centre $\Omega(\omega)$ et de rayon $r$ si et seulement si :

$$|z - \omega| = r$$

### Exemple : rotation

Image de $A(2+i)$ par la rotation de centre $O$ et d'angle $\frac{\pi}{2}$ :

$$z' = e^{i\frac{\pi}{2}} \cdot z = i(2+i) = -1 + 2i$$
""",
                            "quiz": {
                                "titre": "Quiz — Géométrie et complexes",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "L'écriture complexe d'une rotation de centre O et d'angle θ est :",
                                        "choix": ["z' = z + e^(iθ)", "z' = e^(iθ) × z", "z' = |z| × e^(iθ)", "z' = z × θ"],
                                        "reponse_correcte": "z' = e^(iθ) × z",
                                        "explication": "La rotation de centre O et d'angle θ s'écrit z' = e^(iθ)·z.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Calculer la distance AB si z_A = 1 + i et z_B = 4 + 5i.",
                                        "reponse_correcte": "5",
                                        "tolerances": [],
                                        "explication": "AB = |z_B - z_A| = |3 + 4i| = √(9 + 16) = 5.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Trois points A, B, C sont alignés si (z_C - z_A)/(z_B - z_A) est imaginaire pur.",
                                        "reponse_correcte": "faux",
                                        "explication": "Trois points sont alignés si le rapport est RÉEL (pas imaginaire pur). Si le rapport est imaginaire pur, les droites sont perpendiculaires.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                {
                    "ordre": 10,
                    "titre": "Géométrie dans l'Espace",
                    "description": "Fondements vectoriels, produit scalaire et orthogonalité, représentations paramétriques de droites, équations cartésiennes de plans, intersections et systèmes linéaires.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Fondements Vectoriels et Combinaisons Linéaires",
                            "duree": 35,
                            "contenu": r"""## Fondements Vectoriels dans l'Espace

### Vecteurs et coordonnées

Dans un repère orthonormé $(O ; \vec{i}, \vec{j}, \vec{k})$ de l'espace, tout vecteur $\vec{u}$ est défini par ses trois coordonnées :

$$\vec{u} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$$

Pour deux points $A(x_A, y_A, z_A)$ et $B(x_B, y_B, z_B)$ :

$$\vec{AB} = \begin{pmatrix} x_B - x_A \\ y_B - y_A \\ z_B - z_A \end{pmatrix}$$

### Combinaison linéaire

Un vecteur $\vec{w}$ est **combinaison linéaire** de $\vec{u}$ et $\vec{v}$ s'il existe $m, n \in \mathbb{R}$ tels que :

$$\vec{w} = m\vec{u} + n\vec{v}$$

### Colinéarité

Deux vecteurs $\vec{u}$ et $\vec{v}$ sont **colinéaires** si et seulement si :

$$\exists k \in \mathbb{R}, \quad \vec{v} = k\vec{u}$$

Conséquence : trois points $A$, $B$, $C$ sont alignés $\iff$ $\vec{AB}$ et $\vec{AC}$ sont colinéaires.

### Coplanarité

Trois vecteurs $\vec{u}$, $\vec{v}$, $\vec{w}$ sont **coplanaires** si et seulement si l'un d'eux est combinaison linéaire des deux autres :

$$\exists (m, n) \in \mathbb{R}^2, \quad \vec{w} = m\vec{u} + n\vec{v}$$

Quatre points $A$, $B$, $C$, $D$ sont coplanaires $\iff$ $\vec{AB}$, $\vec{AC}$, $\vec{AD}$ sont coplanaires.

### Norme d'un vecteur

$$\|\vec{u}\| = \sqrt{x^2 + y^2 + z^2}$$
""",
                            "quiz": {
                                "titre": "Quiz — Vecteurs dans l'espace",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Calculer les coordonnées de AB si A(1, 2, 3) et B(4, 0, 1).",
                                        "reponse_correcte": "(3, -2, -2)",
                                        "tolerances": ["3, -2, -2", "(3;-2;-2)"],
                                        "explication": "AB = (4-1, 0-2, 1-3) = (3, -2, -2).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Trois points A, B, C sont alignés si et seulement si AB et AC sont colinéaires.",
                                        "reponse_correcte": "vrai",
                                        "explication": "L'alignement de trois points équivaut à la colinéarité des vecteurs AB et AC.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Quatre points sont coplanaires si et seulement si :",
                                        "choix": ["Leurs 4 vecteurs sont nuls", "Un des vecteurs AB, AC, AD est combinaison linéaire des deux autres", "Ils sont tous alignés", "Leurs coordonnées sont entières"],
                                        "reponse_correcte": "Un des vecteurs AB, AC, AD est combinaison linéaire des deux autres",
                                        "explication": "A, B, C, D coplanaires ⟺ les vecteurs AB, AC, AD sont coplanaires (l'un est CL des deux autres).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Orthogonalité et Produit Scalaire",
                            "duree": 35,
                            "contenu": r"""## Produit Scalaire dans l'Espace

### Définition géométrique

$$\vec{u} \cdot \vec{v} = \|\vec{u}\| \times \|\vec{v}\| \times \cos(\theta)$$

où $\theta = (\vec{u}, \vec{v})$ est l'angle entre les deux vecteurs.

### Définition analytique

Pour $\vec{u}(x, y, z)$ et $\vec{v}(x', y', z')$ :

$$\vec{u} \cdot \vec{v} = xx' + yy' + zz'$$

### Propriétés algébriques

- **Commutativité** : $\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}$
- **Distributivité** : $\vec{u} \cdot (\vec{v} + \vec{w}) = \vec{u} \cdot \vec{v} + \vec{u} \cdot \vec{w}$
- **Homogénéité** : $(\lambda\vec{u}) \cdot \vec{v} = \lambda(\vec{u} \cdot \vec{v})$
- **Carré scalaire** : $\vec{u} \cdot \vec{u} = \|\vec{u}\|^2$

### Orthogonalité

$$\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0 \iff xx' + yy' + zz' = 0$$

### Théorème d'Al-Kashi

Dans un triangle $ABC$ :

$$a^2 = b^2 + c^2 - 2bc\cos(\hat{A})$$

Le théorème de Pythagore en est le cas particulier où $\hat{A} = \frac{\pi}{2}$.

### Calcul d'angle entre vecteurs

$$\cos(\theta) = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \times \|\vec{v}\|}$$
""",
                            "quiz": {
                                "titre": "Quiz — Produit scalaire",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Calculer le produit scalaire de u(1, 2, 3) et v(4, -1, 2).",
                                        "reponse_correcte": "8",
                                        "tolerances": [],
                                        "explication": "u·v = 1×4 + 2×(-1) + 3×2 = 4 - 2 + 6 = 8.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Deux vecteurs sont orthogonaux si et seulement si :",
                                        "choix": ["Leur produit scalaire vaut 1", "Leur produit scalaire vaut 0", "Ils sont colinéaires", "Leur somme est nulle"],
                                        "reponse_correcte": "Leur produit scalaire vaut 0",
                                        "explication": "u ⊥ v ⟺ u·v = 0.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Le théorème de Pythagore est un cas particulier du théorème d'Al-Kashi.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Quand l'angle A vaut π/2, cos(A) = 0 et Al-Kashi donne a² = b² + c².",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Représentations Paramétriques de Droites",
                            "duree": 30,
                            "contenu": r"""## Droites dans l'Espace

### Détermination d'une droite

Une droite $(d)$ est définie par :
- un **point** $A(x_A, y_A, z_A)$
- un **vecteur directeur** $\vec{u}(a, b, c)$ non nul

### Représentation paramétrique

Un point $M(x, y, z)$ appartient à $(d)$ si et seulement si $\vec{AM}$ et $\vec{u}$ sont colinéaires, soit $\vec{AM} = t\vec{u}$ :

$$\begin{cases} x = x_A + ta \\ y = y_A + tb \\ z = z_A + tc \end{cases}, \quad t \in \mathbb{R}$$

### Exemple

Droite passant par $A(1, 2, -1)$ de vecteur directeur $\vec{u}(3, -1, 2)$ :

$$\begin{cases} x = 1 + 3t \\ y = 2 - t \\ z = -1 + 2t \end{cases}, \quad t \in \mathbb{R}$$

### Positions relatives de deux droites

Deux droites $(d_1)$ et $(d_2)$ de vecteurs directeurs $\vec{u_1}$ et $\vec{u_2}$ peuvent être :

| Position | Condition |
|---|---|
| **Parallèles** | $\vec{u_1}$ et $\vec{u_2}$ colinéaires |
| **Confondues** | Parallèles + un point commun |
| **Sécantes** | Non parallèles + un point commun |
| **Non coplanaires** | Ni parallèles ni sécantes |

### Droites et plans

- $(d) \subset \mathcal{P}$ : $\vec{u}$ orthogonal à $\vec{n}$ et un point de $(d)$ dans $\mathcal{P}$
- $(d) \parallel \mathcal{P}$ : $\vec{u} \cdot \vec{n} = 0$ et aucun point commun
- $(d)$ sécante à $\mathcal{P}$ : $\vec{u} \cdot \vec{n} \neq 0$
""",
                            "quiz": {
                                "titre": "Quiz — Droites dans l'espace",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Deux droites de vecteurs directeurs colinéaires sont :",
                                        "choix": ["Sécantes", "Parallèles ou confondues", "Perpendiculaires", "Non coplanaires"],
                                        "reponse_correcte": "Parallèles ou confondues",
                                        "explication": "Si les vecteurs directeurs sont colinéaires, les droites sont parallèles (distinctes ou confondues).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Dans l'espace, deux droites non parallèles sont toujours sécantes.",
                                        "reponse_correcte": "faux",
                                        "explication": "Dans l'espace, deux droites non parallèles peuvent être non coplanaires (gauches) et ne pas se croiser.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Donner la représentation paramétrique de la droite passant par A(0,1,2) de vecteur u(1,0,-1). (écrire x=..., y=..., z=...)",
                                        "reponse_correcte": "x = t, y = 1, z = 2 - t",
                                        "tolerances": ["x=t, y=1, z=2-t"],
                                        "explication": "x = 0 + t, y = 1 + 0t = 1, z = 2 + (-1)t = 2 - t.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "Équations Cartésiennes de Plans",
                            "duree": 35,
                            "contenu": r"""## Plans dans l'Espace

### Vecteur normal

Un vecteur non nul $\vec{n}$ est **normal** au plan $\mathcal{P}$ s'il est orthogonal à tout vecteur du plan.

### Équation cartésienne

Le plan $\mathcal{P}$ passant par $A(x_A, y_A, z_A)$ de vecteur normal $\vec{n}(a, b, c)$ a pour équation :

$$ax + by + cz + d = 0$$

où $d = -(ax_A + by_A + cz_A)$.

**Justification** : $M \in \mathcal{P} \iff \vec{AM} \cdot \vec{n} = 0$

$$a(x - x_A) + b(y - y_A) + c(z - z_A) = 0$$

### Lecture de l'équation

Dans l'équation $ax + by + cz + d = 0$ :
- Les coefficients $(a, b, c)$ donnent un **vecteur normal** $\vec{n}(a, b, c)$

### Positions relatives de deux plans

Pour $\mathcal{P}_1 : a_1x + b_1y + c_1z + d_1 = 0$ et $\mathcal{P}_2 : a_2x + b_2y + c_2z + d_2 = 0$ :

| Position | Condition |
|---|---|
| **Parallèles** | $\vec{n_1}$ et $\vec{n_2}$ colinéaires |
| **Confondus** | Parallèles + un point commun |
| **Sécants** | $\vec{n_1}$ et $\vec{n_2}$ non colinéaires |

### Distance d'un point à un plan

$$d(M_0, \mathcal{P}) = \frac{|ax_0 + by_0 + cz_0 + d|}{\sqrt{a^2 + b^2 + c^2}}$$

### Plans perpendiculaires

$\mathcal{P}_1 \perp \mathcal{P}_2 \iff \vec{n_1} \cdot \vec{n_2} = 0$
""",
                            "quiz": {
                                "titre": "Quiz — Plans et équations",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Donner un vecteur normal au plan 2x - y + 3z + 5 = 0.",
                                        "reponse_correcte": "(2, -1, 3)",
                                        "tolerances": ["(2;-1;3)", "2, -1, 3"],
                                        "explication": "Les coefficients de x, y, z donnent le vecteur normal : n(2, -1, 3).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Deux plans sont perpendiculaires si et seulement si :",
                                        "choix": ["Leurs vecteurs normaux sont colinéaires", "Leurs vecteurs normaux ont un produit scalaire nul", "Ils ont une droite commune", "Leurs équations diffèrent d'une constante"],
                                        "reponse_correcte": "Leurs vecteurs normaux ont un produit scalaire nul",
                                        "explication": "P₁ ⊥ P₂ ⟺ n₁ · n₂ = 0.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Deux plans dont les vecteurs normaux sont colinéaires sont parallèles.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Si les vecteurs normaux sont colinéaires, les plans sont parallèles (distincts ou confondus).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "Intersections et Systèmes Linéaires",
                            "duree": 35,
                            "contenu": r"""## Intersections dans l'Espace

### Intersection de deux plans

Deux plans sécants s'intersectent selon une **droite**.

On résout le système de 2 équations à 3 inconnues en paramétrant une variable.

### Intersection de trois plans

Le système de 3 équations à 3 inconnues s'écrit sous forme matricielle :

$$A \times X = B$$

avec $A$ la matrice des coefficients, $X = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$, $B$ le second membre.

### Types d'intersections

| $\det(A)$ | Nature | Intersection |
|---|---|---|
| $\neq 0$ (inversible) | Solution unique | **Point** |
| $= 0$ | Infinité de solutions | **Droite** ou **plan** |
| $= 0$ | Aucune solution | **Vide** (plans parallèles) |

Si $\det(A) \neq 0$ : $X = A^{-1}B$ (solution unique).

### Intersection droite-plan

Pour trouver l'intersection de la droite $\begin{cases} x = x_A + ta \\ y = y_A + tb \\ z = z_A + tc \end{cases}$ avec le plan $\alpha x + \beta y + \gamma z + \delta = 0$ :

1. Substituer les expressions paramétriques dans l'équation du plan
2. Résoudre en $t$
3. Si une solution $t_0$ existe, le point d'intersection a pour coordonnées $(x_A + t_0 a, \; y_A + t_0 b, \; z_A + t_0 c)$

### Exemple

Plan $\mathcal{P} : 2x + y + z = 5$, $\mathcal{P}' : x + y = 3$, $\mathcal{P}'' : y + z = 2$.

Le système donne $\det(A) = 2 \neq 0$, donc l'intersection est un point unique.
""",
                            "quiz": {
                                "titre": "Quiz — Intersections",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "L'intersection de deux plans sécants est :",
                                        "choix": ["Un point", "Une droite", "Un plan", "Vide"],
                                        "reponse_correcte": "Une droite",
                                        "explication": "Deux plans sécants (non parallèles) s'intersectent selon une droite.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Si le déterminant de la matrice A du système est non nul, l'intersection de trois plans est un point unique.",
                                        "reponse_correcte": "vrai",
                                        "explication": "det(A) ≠ 0 signifie que le système a une unique solution, donc l'intersection est un point.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Pour trouver l'intersection d'une droite et d'un plan, on :",
                                        "choix": ["Calcule le produit scalaire", "Substitue les équations paramétriques dans l'équation du plan", "Calcule le déterminant", "Fait un produit vectoriel"],
                                        "reponse_correcte": "Substitue les équations paramétriques dans l'équation du plan",
                                        "explication": "On remplace x, y, z par les expressions paramétriques dans l'équation cartésienne du plan.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 6,
                            "titre": "Exercices d'Application",
                            "duree": 35,
                            "contenu": r"""## Exercices Corrigés

### Exercice 1 : Calcul d'angle

**Énoncé** : Soient $\vec{u}(1, 1, 0)$ et $\vec{v}(0, \sqrt{3}, \sqrt{3})$. Calculer l'angle $\theta$ entre ces vecteurs.

**Correction** :

- $\|\vec{u}\| = \sqrt{1 + 1} = \sqrt{2}$
- $\|\vec{v}\| = \sqrt{3 + 3} = \sqrt{6}$
- $\vec{u} \cdot \vec{v} = 0 + \sqrt{3} + 0 = \sqrt{3}$
- $\cos\theta = \dfrac{\sqrt{3}}{\sqrt{2} \times \sqrt{6}} = \dfrac{\sqrt{3}}{2\sqrt{3}} = \dfrac{1}{2}$
- Donc $\theta = \dfrac{\pi}{3}$

### Exercice 2 : Équation de plan

**Énoncé** : Déterminer l'équation du plan passant par $A(1, 0, -1)$ de vecteur normal $\vec{n}(2, 3, -1)$.

**Correction** :

$2(x-1) + 3(y-0) + (-1)(z-(-1)) = 0$

$2x - 2 + 3y - z - 1 = 0$

$$2x + 3y - z - 3 = 0$$

### Exercice 3 : Distance point-plan

**Énoncé** : Calculer la distance du point $M(1, 2, 3)$ au plan $x + 2y - 2z + 1 = 0$.

**Correction** :

$$d = \frac{|1 + 4 - 6 + 1|}{\sqrt{1 + 4 + 4}} = \frac{0}{3} = 0$$

Le point $M$ appartient au plan.

### Exercice 4 : Intersection

**Énoncé** : Trouver l'intersection de la droite $\begin{cases} x = 1 + t \\ y = 2 - t \\ z = 3 + 2t \end{cases}$ avec le plan $x + y + z = 10$.

**Correction** :

$(1+t) + (2-t) + (3+2t) = 10 \implies 6 + 2t = 10 \implies t = 2$

Point d'intersection : $(3, 0, 7)$.
""",
                            "quiz": {
                                "titre": "Quiz — Exercices de géométrie spatiale",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Calculer le produit scalaire de u(1, 1, 0) et v(0, √3, √3).",
                                        "reponse_correcte": "√3",
                                        "tolerances": ["racine de 3", "1.73"],
                                        "explication": "u·v = 1×0 + 1×√3 + 0×√3 = √3.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Déterminer l'équation du plan passant par A(1,0,-1) de vecteur normal n(2,3,-1). (forme ax+by+cz+d=0)",
                                        "reponse_correcte": "2x + 3y - z - 3 = 0",
                                        "tolerances": ["2x+3y-z-3=0", "2x + 3y - z = 3"],
                                        "explication": "2(x-1) + 3y - (z+1) = 0, soit 2x + 3y - z - 3 = 0.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Trouver le point d'intersection de la droite (x=1+t, y=2-t, z=3+2t) avec le plan x+y+z=10.",
                                        "reponse_correcte": "(3, 0, 7)",
                                        "tolerances": ["(3;0;7)", "3, 0, 7"],
                                        "explication": "(1+t)+(2-t)+(3+2t)=10 → 6+2t=10 → t=2. Point : (3, 0, 7).",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                {
                    "ordre": 11,
                    "titre": "Le Barycentre dans le Plan et l'Espace",
                    "description": "Systèmes de points pondérés, définition vectorielle du barycentre, propriétés fondamentales, affixe du barycentre, applications géométriques et exercices types.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Introduction aux Systèmes de Points Pondérés",
                            "duree": 25,
                            "contenu": r"""## Systèmes de Points Pondérés

### Définitions

- **Point pondéré** : couple $(A, \alpha)$ où $A$ est un point et $\alpha \in \mathbb{R}$ est le **coefficient** (ou masse).

- **Système de points pondérés** : ensemble de $n$ points associés à des réels :

$$S = \{(A_i, \alpha_i)\}_{1 \leq i \leq n}$$

### Condition d'existence du barycentre

Le barycentre du système $S$ existe et est **unique** si et seulement si :

$$\sum_{i=1}^{n} \alpha_i \neq 0$$

### Cas dégénéré

Si $\displaystyle\sum_{i=1}^{n} \alpha_i = 0$, le vecteur $\displaystyle\sum \alpha_i \vec{MA_i}$ est **constant** quel que soit $M$, mais le système n'admet pas de barycentre (pas de point d'équilibre unique).

### Exemples de systèmes

| Système | Somme des coefficients | Barycentre ? |
|---|---|---|
| $\{(A, 2), (B, 3)\}$ | $5 \neq 0$ | Oui |
| $\{(A, 1), (B, -1)\}$ | $0$ | Non |
| $\{(A, 1), (B, 1), (C, 1)\}$ | $3 \neq 0$ | Oui (isobarycentre) |
""",
                            "quiz": {
                                "titre": "Quiz — Points pondérés",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "vrai_faux",
                                        "texte": "Le barycentre d'un système existe si et seulement si la somme des coefficients est non nulle.",
                                        "reponse_correcte": "vrai",
                                        "explication": "C'est la condition nécessaire et suffisante d'existence du barycentre.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Quel est le type du barycentre de {(A,1), (B,1), (C,1)} ?",
                                        "choix": ["Barycentre partiel", "Isobarycentre", "Barycentre pondéré", "Le barycentre n'existe pas"],
                                        "reponse_correcte": "Isobarycentre",
                                        "explication": "Quand tous les coefficients sont égaux, on parle d'isobarycentre (centre de gravité).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Le barycentre de {(A, 1), (B, -1)} existe.",
                                        "reponse_correcte": "faux",
                                        "explication": "La somme des coefficients est 1 + (-1) = 0, donc le barycentre n'existe pas.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Définition Vectorielle du Barycentre",
                            "duree": 35,
                            "contenu": r"""## Définition Vectorielle

### Définition fondamentale

Le barycentre $G$ du système $\{(A_1, \alpha_1), \ldots, (A_n, \alpha_n)\}$ est l'unique point vérifiant :

$$\sum_{i=1}^{n} \alpha_i \, \vec{GA_i} = \vec{0}$$

### Cas de deux points

Pour $\{(A, \alpha), (B, \beta)\}$ avec $\alpha + \beta \neq 0$ :

$$\alpha \, \vec{GA} + \beta \, \vec{GB} = \vec{0}$$

D'où : $\vec{AG} = \dfrac{\beta}{\alpha + \beta} \, \vec{AB}$

Le point $G$ divise le segment $[AB]$ dans le rapport $\dfrac{\beta}{\alpha}$.

### Formule de réduction vectorielle

Pour **tout point** $M$ de l'espace :

$$\sum_{i=1}^{n} \alpha_i \, \vec{MA_i} = \left(\sum_{i=1}^{n} \alpha_i\right) \vec{MG}$$

**Démonstration** (par relation de Chasles) :

$$\sum \alpha_i \vec{MA_i} = \sum \alpha_i (\vec{MG} + \vec{GA_i}) = \left(\sum \alpha_i\right) \vec{MG} + \underbrace{\sum \alpha_i \vec{GA_i}}_{= \vec{0}} = \left(\sum \alpha_i\right) \vec{MG}$$

### Coordonnées du barycentre

$$x_G = \frac{\sum \alpha_i \, x_i}{\sum \alpha_i}, \quad y_G = \frac{\sum \alpha_i \, y_i}{\sum \alpha_i}, \quad z_G = \frac{\sum \alpha_i \, z_i}{\sum \alpha_i}$$
""",
                            "quiz": {
                                "titre": "Quiz — Définition vectorielle",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quelle relation vectorielle définit le barycentre G d'un système {(A, α), (B, β)} ?",
                                        "reponse_correcte": "α·GA + β·GB = 0",
                                        "tolerances": ["alpha GA + beta GB = 0", "αGA + βGB = 0"],
                                        "explication": "Par définition, G vérifie α·vec(GA) + β·vec(GB) = vec(0).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "La formule de réduction vectorielle permet d'écrire Σ αᵢ MAᵢ comme :",
                                        "choix": ["(Σ αᵢ) × MG", "(Σ αᵢ) × GA", "Σ αᵢ × MAᵢ²", "MG / Σ αᵢ"],
                                        "reponse_correcte": "(Σ αᵢ) × MG",
                                        "explication": "Σ αᵢ vec(MAᵢ) = (Σ αᵢ) × vec(MG) pour tout point M.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Calculer x_G pour le barycentre de {(A(1), 2), (B(3), 1)} (coordonnée x seulement).",
                                        "reponse_correcte": "5/3",
                                        "tolerances": ["1.67", "1,67"],
                                        "explication": "x_G = (2×1 + 1×3) / (2+1) = 5/3.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Propriétés Fondamentales du Barycentre",
                            "duree": 30,
                            "contenu": r"""## Propriétés

### Homogénéité

Le barycentre est **inchangé** si l'on multiplie tous les coefficients par un même réel $k \neq 0$ :

$$\text{bar}\{(A, \alpha), (B, \beta)\} = \text{bar}\{(A, k\alpha), (B, k\beta)\}$$

### Associativité (barycentre partiel)

On peut remplacer un **sous-système** par son barycentre affecté de la somme des coefficients.

Si $G = \text{bar}\{(A, \alpha), (B, \beta), (C, \gamma)\}$ et $\alpha + \beta \neq 0$, en posant $G_1 = \text{bar}\{(A, \alpha), (B, \beta)\}$ :

$$G = \text{bar}\{(G_1, \alpha + \beta), (C, \gamma)\}$$

Cette propriété permet de construire $G$ **par étapes** géométriques.

### Isobarycentre

Si tous les coefficients sont **égaux** et non nuls, le barycentre est appelé **isobarycentre** :

- **Milieu** : isobarycentre de $\{(A, 1), (B, 1)\}$
- **Centre de gravité** d'un triangle : isobarycentre de $\{(A, 1), (B, 1), (C, 1)\}$

$$\vec{GA} + \vec{GB} + \vec{GC} = \vec{0}$$

### Théorème de la médiane

Pour un triangle $ABC$ avec $A'$ milieu de $[BC]$ :

$$2AA'^2 = AB^2 + AC^2 - \frac{1}{2}BC^2$$

**Preuve** : On utilise $2\vec{AA'} = \vec{AB} + \vec{AC}$ et on développe le carré scalaire.
""",
                            "quiz": {
                                "titre": "Quiz — Propriétés du barycentre",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "vrai_faux",
                                        "texte": "Le barycentre de {(A, 2), (B, 4)} est le même que celui de {(A, 1), (B, 2)}.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Par homogénéité, multiplier tous les coefficients par k=1/2 ne change pas le barycentre.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Le centre de gravité d'un triangle est :",
                                        "choix": ["Le barycentre de coefficients (1, 2, 3)", "L'isobarycentre des trois sommets", "Le milieu d'un côté", "Le pied d'une hauteur"],
                                        "reponse_correcte": "L'isobarycentre des trois sommets",
                                        "explication": "Le centre de gravité est l'isobarycentre de {(A,1), (B,1), (C,1)}, même coefficients.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "L'associativité permet de calculer un barycentre de 3 points par étapes successives.",
                                        "reponse_correcte": "vrai",
                                        "explication": "On peut d'abord calculer le barycentre de 2 points, puis celui du résultat avec le 3e point.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "Affixe du Barycentre",
                            "duree": 25,
                            "contenu": r"""## Barycentre et Nombres Complexes

### Formule de l'affixe

Pour un système $\{(A, \alpha), (B, \beta), (C, \gamma)\}$ dans le plan complexe, l'**affixe** du barycentre $G$ est :

$$z_G = \frac{\alpha z_A + \beta z_B + \gamma z_C}{\alpha + \beta + \gamma}$$

### Cas général à $n$ points

$$z_G = \frac{\sum_{i=1}^{n} \alpha_i z_{A_i}}{\sum_{i=1}^{n} \alpha_i}$$

### Cas particuliers

**Milieu** de $[AB]$ (coefficients égaux) :

$$z_I = \frac{z_A + z_B}{2}$$

**Centre de gravité** du triangle $ABC$ :

$$z_G = \frac{z_A + z_B + z_C}{3}$$

### Exemple

Soient $A(2+i)$, $B(-1+3i)$, $C(i)$ avec les coefficients $(2, 1, 1)$ :

$$z_G = \frac{2(2+i) + 1(-1+3i) + 1(i)}{2+1+1} = \frac{4+2i-1+3i+i}{4} = \frac{3+6i}{4}$$

### Lien avec les coordonnées

Si $z_A = x_A + iy_A$, alors $z_G = x_G + iy_G$ où $x_G$ et $y_G$ sont les coordonnées du barycentre.
""",
                            "quiz": {
                                "titre": "Quiz — Affixe du barycentre",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quelle est l'affixe du milieu de [AB] si z_A = 1+i et z_B = 3-i ?",
                                        "reponse_correcte": "2",
                                        "tolerances": ["2 + 0i", "2+0i"],
                                        "explication": "z_I = (z_A + z_B)/2 = (1+i+3-i)/2 = 4/2 = 2.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "L'affixe du centre de gravité d'un triangle ABC est :",
                                        "choix": ["(z_A + z_B + z_C) / 3", "(z_A × z_B × z_C) / 3", "z_A + z_B + z_C", "(z_A - z_B + z_C) / 3"],
                                        "reponse_correcte": "(z_A + z_B + z_C) / 3",
                                        "explication": "Le centre de gravité est l'isobarycentre, donc z_G = (z_A + z_B + z_C) / 3.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La formule de l'affixe du barycentre est une moyenne pondérée des affixes.",
                                        "reponse_correcte": "vrai",
                                        "explication": "z_G = Σ(αᵢ·zᵢ) / Σαᵢ est bien une moyenne pondérée des affixes par les coefficients.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "Applications Géométriques",
                            "duree": 30,
                            "contenu": r"""## Applications Géométriques

### Points remarquables d'un triangle

| Point | Système barycentrique |
|---|---|
| **Milieu** de $[AB]$ | $\text{bar}\{(A, 1), (B, 1)\}$ |
| **Centre de gravité** | $\text{bar}\{(A, 1), (B, 1), (C, 1)\}$ |
| **Centre du cercle inscrit** | $\text{bar}\{(A, a), (B, b), (C, c)\}$ où $a, b, c$ sont les longueurs des côtés opposés |

### Lieux géométriques

Le barycentre permet de caractériser des **ensembles de points** vérifiant une condition vectorielle.

**Exemple** : Trouver le lieu des points $M$ tels que $2\|\vec{MA}\|^2 + \|\vec{MB}\|^2 = k$.

On utilise la formule de réduction : $2\vec{MA} + \vec{MB} = 3\vec{MG}$ où $G = \text{bar}\{(A, 2), (B, 1)\}$.

Puis avec le développement des normes au carré, on obtient une équation de cercle.

### Position du barycentre de deux points

Le barycentre $G$ de $\{(A, \alpha), (B, \beta)\}$ est situé **sur le segment** $[AB]$ si $\alpha$ et $\beta$ sont de même signe, et **à l'extérieur** sinon.

$$\vec{AG} = \frac{\beta}{\alpha + \beta}\vec{AB}$$

- Si $\alpha$ et $\beta > 0$ : $G$ est entre $A$ et $B$
- Si $\alpha$ et $\beta$ de signes opposés : $G$ est à l'extérieur de $[AB]$

### Barycentre dans l'espace

Les définitions et propriétés sont **identiques** dans $\mathbb{R}^3$ :

$$x_G = \frac{\sum \alpha_i x_i}{\sum \alpha_i}, \quad y_G = \frac{\sum \alpha_i y_i}{\sum \alpha_i}, \quad z_G = \frac{\sum \alpha_i z_i}{\sum \alpha_i}$$
""",
                            "quiz": {
                                "titre": "Quiz — Applications géométriques",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Le milieu de [AB] est le barycentre de :",
                                        "choix": ["{(A, 1), (B, 2)}", "{(A, 1), (B, 1)}", "{(A, 2), (B, 1)}", "{(A, 0), (B, 1)}"],
                                        "reponse_correcte": "{(A, 1), (B, 1)}",
                                        "explication": "Le milieu est l'isobarycentre avec des coefficients égaux.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Si α et β sont de même signe, le barycentre G de {(A,α),(B,β)} est entre A et B.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Si α et β sont de même signe, le rapport β/(α+β) est entre 0 et 1, donc G est entre A et B.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Les propriétés du barycentre dans le plan s'étendent identiquement à l'espace.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Les définitions vectorielles sont les mêmes dans R² et R³.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 6,
                            "titre": "Méthodes et Exercices Types",
                            "duree": 35,
                            "contenu": r"""## Méthodes et Exercices

### Méthodologie générale

1. **Vérifier** que $\sum \alpha_i \neq 0$
2. **Réduire** les expressions vectorielles avec la formule de réduction
3. **Associer** par barycentres partiels si nécessaire
4. **Calculer** les coordonnées ou l'affixe pour confirmer

### Exercice 1 : Calcul de coordonnées

**Énoncé** : $A(1, 2)$, $B(-1, 4)$, $C(0, -2)$. Calculer $G = \text{bar}\{(A, 2), (B, 1), (C, 1)\}$.

**Correction** :

- $\sum \alpha_i = 2 + 1 + 1 = 4 \neq 0$ ✓
- $x_G = \dfrac{2(1) + 1(-1) + 1(0)}{4} = \dfrac{1}{4}$
- $y_G = \dfrac{2(2) + 1(4) + 1(-2)}{4} = \dfrac{6}{4} = \dfrac{3}{2}$

$$G\left(\frac{1}{4} \,;\, \frac{3}{2}\right)$$

### Exercice 2 : Construction par associativité

**Énoncé** : Construire $G = \text{bar}\{(A, 3), (B, 1), (C, 2)\}$.

**Méthode** :

1. $G_1 = \text{bar}\{(A, 3), (B, 1)\}$ : $\vec{AG_1} = \frac{1}{4}\vec{AB}$
2. $G = \text{bar}\{(G_1, 4), (C, 2)\}$ : $\vec{G_1 G} = \frac{2}{6}\vec{G_1 C} = \frac{1}{3}\vec{G_1 C}$

### Exercice 3 : Lieu géométrique

**Énoncé** : Trouver le lieu des points $M$ tels que $\|2\vec{MA} + \vec{MB}\| = 3$.

**Correction** : Soit $G$ le barycentre de $\{(A, 2), (B, 1)\}$.

$2\vec{MA} + \vec{MB} = 3\vec{MG}$, donc $\|3\vec{MG}\| = 3$, soit $MG = 1$.

Le lieu est le **cercle** de centre $G$ et de rayon $1$.
""",
                            "quiz": {
                                "titre": "Quiz — Exercices barycentre",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Calculer x_G pour G = bar{(A(1,2), 2), (B(-1,4), 1), (C(0,-2), 1)}.",
                                        "reponse_correcte": "1/4",
                                        "tolerances": ["0.25", "0,25"],
                                        "explication": "x_G = (2×1 + 1×(-1) + 1×0) / (2+1+1) = 1/4.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Le lieu des points M tels que ||2·MA + MB|| = 3 est :",
                                        "choix": ["Une droite", "Un cercle de rayon 3", "Un cercle de rayon 1", "Un point"],
                                        "reponse_correcte": "Un cercle de rayon 1",
                                        "explication": "2MA + MB = 3MG donc ||3MG|| = 3, soit MG = 1 : cercle de centre G et rayon 1.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La première étape pour résoudre un problème de barycentre est de vérifier que la somme des coefficients est non nulle.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Si la somme est nulle, le barycentre n'existe pas et la résolution est différente.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                {
                    "ordre": 12,
                    "titre": "Théorie des Ensembles et Dénombrement",
                    "description": "Logique propositionnelle, opérations ensemblistes, lois de Morgan, produit cartésien, factorielles, arrangements, combinaisons et synthèse méthodologique.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Vocabulaire de la Logique et Fondements des Ensembles",
                            "duree": 30,
                            "contenu": r"""## Logique et Ensembles

### Propositions et négation

- **Proposition** : énoncé mathématique susceptible d'être soit vrai, soit faux.
- **Négation** de $P$, notée $\neg P$ ou $\bar{P}$ : fausse quand $P$ est vraie, et vraie quand $P$ est fausse. On a $\neg(\neg P) \equiv P$.

### Connecteurs logiques

| Connecteur | Notation | Vrai si… |
|---|---|---|
| **Conjonction** « et » | $P \wedge Q$ | $P$ **et** $Q$ vraies simultanément |
| **Disjonction** « ou » | $P \vee Q$ | Au moins l'une est vraie (ou inclusif) |

### Méthodes d'inférence

- **Modus Ponens** : si $P$ est vraie et $P \Rightarrow Q$ est vraie, alors $Q$ est vraie.
- **Modus Tollens** : si $P \Rightarrow Q$ est vraie et $Q$ est fausse, alors $P$ est fausse (fondement du raisonnement par l'absurde).

### Isomorphisme logique–ensembles

Il existe une correspondance structurelle entre logique et opérations sur les parties d'un univers $\Omega$ :

| Logique | Ensembles |
|---|---|
| Négation $\neg P$ | Complémentaire $\bar{A}$ |
| Conjonction $P \wedge Q$ | Intersection $A \cap B$ |
| Disjonction $P \vee Q$ | Union $A \cup B$ |
""",
                            "quiz": {
                                "titre": "Quiz — Logique et ensembles",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La disjonction P ∨ Q est vraie si :",
                                        "choix": ["P et Q sont fausses", "P et Q sont vraies uniquement", "Au moins l'une des deux est vraie", "Aucune condition"],
                                        "reponse_correcte": "Au moins l'une des deux est vraie",
                                        "explication": "Le « ou » logique est inclusif : P ∨ Q est vraie dès qu'au moins une proposition est vraie.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "La conjonction P ∧ Q correspond en théorie des ensembles à :",
                                        "choix": ["L'union A ∪ B", "L'intersection A ∩ B", "Le complémentaire de A", "Le produit cartésien A × B"],
                                        "reponse_correcte": "L'intersection A ∩ B",
                                        "explication": "La conjonction (les deux vrais) correspond à l'intersection (les éléments communs).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Le Modus Tollens est le fondement du raisonnement par l'absurde.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Si P ⇒ Q est vraie et Q est fausse, alors P est fausse : c'est le raisonnement par l'absurde.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Opérations Algébriques sur les Parties d'un Ensemble",
                            "duree": 30,
                            "contenu": r"""## Opérations sur $\mathcal{P}(\Omega)$

### Définition

Soit $\Omega$ un ensemble de référence. L'ensemble de toutes les parties de $\Omega$ est noté $\mathcal{P}(\Omega)$. Les opérations $\cap$ et $\cup$ lui confèrent une structure algébrique.

### Propriétés fondamentales

Pour tous $F, G, H \in \mathcal{P}(\Omega)$ :

- **Commutativité** : $F \cap G = G \cap F$ et $F \cup G = G \cup F$
- **Associativité** : $F \cap (G \cap H) = (F \cap G) \cap H$ et $F \cup (G \cup H) = (F \cup G) \cup H$
- **Distributivité** :
  - $F \cap (G \cup H) = (F \cap G) \cup (F \cap H)$
  - $F \cup (G \cap H) = (F \cup G) \cap (F \cup H)$

### Éléments neutres

- $\Omega$ est neutre pour l'intersection : $F \cap \Omega = F$
- $\emptyset$ est neutre pour l'union : $F \cup \emptyset = F$

### Lois de Morgan

$$\overline{F \cup G} = \bar{F} \cap \bar{G}$$

$$\overline{F \cap G} = \bar{F} \cup \bar{G}$$

**Justification logique** :
- $\neg(P \vee Q) \equiv \neg P \wedge \neg Q$
- $\neg(P \wedge Q) \equiv \neg P \vee \neg Q$

### Application au dénombrement

Le passage au complémentaire permet de dénombrer par **soustraction** :

$$|A| = |\Omega| - |\bar{A}|$$

C'est la méthode de l'**événement contraire**.
""",
                            "quiz": {
                                "titre": "Quiz — Opérations ensemblistes",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Compléter la loi de Morgan : le complémentaire de F ∪ G est égal à…",
                                        "reponse_correcte": "F̄ ∩ Ḡ",
                                        "tolerances": ["complement de F inter complement de G", "F barre inter G barre"],
                                        "explication": "Par les lois de Morgan, le complémentaire de F ∪ G = F̄ ∩ Ḡ.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "L'élément neutre pour l'intersection est :",
                                        "choix": ["L'ensemble vide ∅", "L'univers Ω", "L'ensemble {0}", "Aucun"],
                                        "reponse_correcte": "L'univers Ω",
                                        "explication": "F ∩ Ω = F pour tout F, donc Ω est l'élément neutre pour ∩.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "L'intersection est distributive par rapport à l'union.",
                                        "reponse_correcte": "vrai",
                                        "explication": "F ∩ (G ∪ H) = (F ∩ G) ∪ (F ∩ H) : c'est la distributivité de ∩ sur ∪.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Notions Préliminaires au Dénombrement",
                            "duree": 25,
                            "contenu": r"""## Préliminaires au Dénombrement

### Parties et complémentarité

Une **partie** $A$ de $\Omega$ est un sous-ensemble tel que $\forall x,\; x \in A \Rightarrow x \in \Omega$.

Le passage au complémentaire permet de dénombrer par soustraction :

$$|A| = |\Omega| - |\bar{A}|$$

### Cardinal d'une union (formule d'inclusion-exclusion)

Pour deux ensembles :

$$|A \cup B| = |A| + |B| - |A \cap B|$$

Pour trois ensembles :

$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$$

### Produit cartésien

Le **produit cartésien** de $n$ ensembles est l'ensemble des $n$-uplets ordonnés :

$$\Omega_1 \times \Omega_2 \times \cdots \times \Omega_n = \{(\omega_1, \omega_2, \ldots, \omega_n) \mid \omega_i \in \Omega_i\}$$

**Cardinal** :

$$|\Omega_1 \times \Omega_2 \times \cdots \times \Omega_n| = |\Omega_1| \times |\Omega_2| \times \cdots \times |\Omega_n|$$

### Exemples

- **Géométrique** : si $I$ et $J$ sont des intervalles, $I \times J$ est un rectangle du plan.
- **Expériences répétées** : lancer un dé 3 fois revient à considérer $\{1,...,6\}^3$, de cardinal $6^3 = 216$.
""",
                            "quiz": {
                                "titre": "Quiz — Préliminaires au dénombrement",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quel est le cardinal de {1,2,3,4,5,6}³ (lancer un dé 3 fois) ?",
                                        "reponse_correcte": "216",
                                        "tolerances": ["6^3"],
                                        "explication": "|Ω³| = 6³ = 216.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "La formule |A ∪ B| = |A| + |B| - |A ∩ B| est appelée :",
                                        "choix": ["Formule de Bayes", "Formule d'inclusion-exclusion", "Loi de Morgan", "Formule du binôme"],
                                        "reponse_correcte": "Formule d'inclusion-exclusion",
                                        "explication": "C'est la formule d'inclusion-exclusion (ou formule du crible).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Le cardinal d'un produit cartésien est le produit des cardinaux.",
                                        "reponse_correcte": "vrai",
                                        "explication": "|Ω₁ × Ω₂ × … × Ωₙ| = |Ω₁| × |Ω₂| × … × |Ωₙ|.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "La Factorielle et l'Analyse Combinatoire",
                            "duree": 25,
                            "contenu": r"""## La Factorielle

### Définition

Pour tout entier naturel $n$ :

$$n! = n \times (n-1) \times \cdots \times 2 \times 1$$

Par convention : $0! = 1$.

### Premières valeurs

| $n$ | $n!$ |
|---|---|
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |
| 6 | 720 |
| 10 | 3 628 800 |

### Interprétation combinatoire

$n!$ est le nombre de **permutations** d'un ensemble à $n$ éléments, c'est-à-dire le nombre de manières d'ordonner $n$ objets distincts.

### Relation de récurrence

$$n! = n \times (n-1)!$$

### Coefficient binomial

Le nombre de manières de choisir $p$ éléments parmi $n$ (sans ordre) est :

$$\binom{n}{p} = \frac{n!}{p!(n-p)!}$$

### Propriétés du coefficient binomial

- **Symétrie** : $\binom{n}{p} = \binom{n}{n-p}$
- **Cas extrêmes** : $\binom{n}{0} = \binom{n}{n} = 1$
- **Formule de Pascal** : $\binom{n+1}{p} = \binom{n}{p-1} + \binom{n}{p}$
""",
                            "quiz": {
                                "titre": "Quiz — Factorielle et combinatoire",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Combien vaut 5! ?",
                                        "reponse_correcte": "120",
                                        "tolerances": [],
                                        "explication": "5! = 5 × 4 × 3 × 2 × 1 = 120.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Combien vaut C(5,2) (nombre de combinaisons de 2 parmi 5) ?",
                                        "reponse_correcte": "10",
                                        "tolerances": [],
                                        "explication": "C(5,2) = 5! / (2! × 3!) = 120 / (2 × 6) = 10.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Par convention, 0! = 0.",
                                        "reponse_correcte": "faux",
                                        "explication": "Par convention, 0! = 1 (pas 0).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "Méthodes de Tirages : p-listes, Arrangements, Combinaisons",
                            "duree": 35,
                            "contenu": r"""## Les Trois Modèles de Tirage

### Tirages successifs avec remise : $p$-listes

Un **tirage successif avec remise** de $p$ éléments parmi $n$ est un élément du produit cartésien $\Omega^p$ :

- L'**ordre** est pris en compte
- La **répétition** est autorisée

$$\text{Nombre de } p\text{-listes} = n^p$$

**Exemple** : codes à 4 chiffres parmi $\{0, 1, \ldots, 9\}$ → $10^4 = 10\,000$ codes.

### Tirages successifs sans remise : Arrangements

Un **arrangement** de $p$ éléments parmi $n$ est une séquence ordonnée sans répétition :

- L'**ordre** est pris en compte
- La **répétition** est exclue

$$A_n^p = \frac{n!}{(n-p)!} = n(n-1)(n-2)\cdots(n-p+1)$$

**Exemple** : podium de 3 coureurs parmi 10 → $A_{10}^3 = 10 \times 9 \times 8 = 720$.

### Tirages simultanés : Combinaisons

Un **tirage simultané** de $p$ éléments parmi $n$ revient à choisir une partie de cardinal $p$ :

- L'**ordre** n'intervient pas
- La **répétition** est impossible

$$\binom{n}{p} = \frac{n!}{p!(n-p)!} = \frac{A_n^p}{p!}$$

**Exemple** : choisir 3 délégués parmi 10 → $\binom{10}{3} = \frac{720}{6} = 120$.

### Lien entre les modèles

$$\binom{n}{p} = \frac{A_n^p}{p!}$$

On « divise » les arrangements par $p!$ car l'ordre n'importe plus.
""",
                            "quiz": {
                                "titre": "Quiz — Modèles de tirage",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Pour un tirage successif AVEC remise de p parmi n, le nombre total est :",
                                        "choix": ["n!", "n^p", "n!/(n-p)!", "n!/(p!(n-p)!)"],
                                        "reponse_correcte": "n^p",
                                        "explication": "Avec remise et ordre, on a n choix à chaque étape, soit n^p au total.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Calculer A(10,3), le nombre d'arrangements de 3 parmi 10.",
                                        "reponse_correcte": "720",
                                        "tolerances": [],
                                        "explication": "A(10,3) = 10 × 9 × 8 = 720.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Le tirage simultané (sans ordre, sans répétition) correspond au modèle des :",
                                        "choix": ["p-listes", "Arrangements", "Combinaisons", "Permutations"],
                                        "reponse_correcte": "Combinaisons",
                                        "explication": "Un tirage simultané = choix d'une partie = combinaison.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 6,
                            "titre": "Synthèse Méthodologique pour le Choix du Modèle",
                            "duree": 20,
                            "contenu": r"""## Synthèse : Choisir le Bon Modèle

### Tableau récapitulatif

| Type de tirage | Ordre ? | Répétition ? | Formule |
|---|---|---|---|
| Successif **avec** remise | Oui | Oui | $n^p$ |
| Successif **sans** remise | Oui | Non | $A_n^p = \dfrac{n!}{(n-p)!}$ |
| Simultané | Non | Non | $\dbinom{n}{p} = \dfrac{n!}{p!(n-p)!}$ |

### Méthode de résolution

1. **Identifier** l'univers $\Omega$ et son cardinal $n$
2. **Déterminer** si l'ordre intervient dans la question
3. **Vérifier** si la répétition est possible
4. **Appliquer** la formule correspondante

### Cas fréquents au baccalauréat

- **Mot de passe** → $p$-listes (avec remise, ordre compte)
- **Classement / podium** → Arrangements (sans remise, ordre compte)
- **Comité / groupe** → Combinaisons (sans remise, sans ordre)
- **Permutations** → cas particulier d'arrangement avec $p = n$, soit $n!$

### Formule du binôme de Newton

$$\forall a, b \in \mathbb{R}, \quad (a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}$$

On retrouve les coefficients binomiaux dans le **triangle de Pascal**.
""",
                            "quiz": {
                                "titre": "Quiz — Synthèse méthodologique",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Pour choisir un comité de 4 personnes parmi 12, on utilise :",
                                        "choix": ["12^4", "A(12,4)", "C(12,4)", "12!"],
                                        "reponse_correcte": "C(12,4)",
                                        "explication": "Un comité = pas d'ordre, pas de répétition → combinaison C(12,4).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Pour un code PIN à 4 chiffres (0-9, répétitions possibles), le nombre de codes est :",
                                        "choix": ["10!", "10^4", "A(10,4)", "C(10,4)"],
                                        "reponse_correcte": "10^4",
                                        "explication": "Ordre + répétition autorisée → p-listes → 10^4 = 10 000.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Combien vaut le nombre de permutations de 4 éléments ?",
                                        "reponse_correcte": "24",
                                        "tolerances": ["4!"],
                                        "explication": "4! = 4 × 3 × 2 × 1 = 24 permutations.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 7,
                            "titre": "Raisonnement par Récurrence et Applications",
                            "duree": 30,
                            "contenu": r"""## Le Raisonnement par Récurrence

### Principe

Pour démontrer qu'une propriété $P(n)$ est vraie pour tout $n \in \mathbb{N}$ :

1. **Initialisation** : prouver que $P(n_0)$ est vraie (souvent $n_0 = 0$ ou $1$)
2. **Hérédité** : supposer $P(k)$ vraie et démontrer que $P(k+1)$ est vraie
3. **Conclusion** : par le principe de récurrence, $P(n)$ est vraie pour tout $n \geq n_0$

### Exemple : $10^n - 1$ est divisible par 9

**Proposition** $P(n)$ : « $10^n - 1$ est un multiple de 9 ».

**Initialisation** ($n = 0$) : $10^0 - 1 = 0 = 9 \times 0$ ✓

**Hérédité** : supposons $P(k)$ vraie, i.e. $\exists m \in \mathbb{Z},\; 10^k - 1 = 9m$.

Alors :

$$10^{k+1} - 1 = 10 \times 10^k - 1 = 10(9m + 1) - 1 = 90m + 9 = 9(10m + 1)$$

Donc $10^{k+1} - 1$ est un multiple de 9 : $P(k+1)$ est vraie.

**Conclusion** : $P(n)$ est vraie pour tout $n \in \mathbb{N}$.

### Application au dénombrement

Le raisonnement par récurrence permet de prouver :

- La formule du binôme de Newton
- Les propriétés des coefficients binomiaux
- Les formules de sommation : $\displaystyle\sum_{k=0}^{n} \binom{n}{k} = 2^n$

### Variantes

- **Récurrence forte** : on suppose $P(j)$ vraie pour tout $j \leq k$, puis on démontre $P(k+1)$
- **Récurrence double** : on initialise à $n_0$ et $n_0 + 1$, et l'hérédité utilise $P(k)$ et $P(k+1)$ pour prouver $P(k+2)$
""",
                            "quiz": {
                                "titre": "Quiz — Récurrence",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quelles sont les étapes d'un raisonnement par récurrence ?",
                                        "choix": ["Initialisation, Hérédité, Conclusion", "Hypothèse, Thèse, Antithèse", "Analyse, Synthèse, Vérification", "Conjecture, Preuve, Contre-exemple"],
                                        "reponse_correcte": "Initialisation, Hérédité, Conclusion",
                                        "explication": "Le raisonnement par récurrence comporte trois étapes : initialisation, hérédité, conclusion.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Dans l'hérédité, on suppose P(k) vraie et on démontre P(k+1) vraie.",
                                        "reponse_correcte": "vrai",
                                        "explication": "C'est exactement le principe de l'hérédité dans le raisonnement par récurrence.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Que vaut la somme des coefficients binomiaux C(n,0) + C(n,1) + ... + C(n,n) ?",
                                        "reponse_correcte": "2^n",
                                        "tolerances": ["2**n", "2 puissance n"],
                                        "explication": "Σ C(n,k) pour k de 0 à n = 2^n (conséquence du binôme de Newton avec a=b=1).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                {
                    "ordre": 13,
                    "titre": "Probabilités, Conditionnement et Indépendance",
                    "description": "Probabilités conditionnelles, propriété d'absence de mémoire, formule des probabilités totales, variables aléatoires, indépendance, échantillons, inégalité de Bienaymé-Tchebychev et loi des grands nombres.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Probabilités Conditionnelles",
                            "duree": 35,
                            "contenu": r"""## Probabilités Conditionnelles

### Définition

Soit $A$ un événement de probabilité non nulle. Pour tout événement $B$, la **probabilité de $B$ sachant $A$**, notée $P_A(B)$, est :

$$P_A(B) = \frac{P(A \cap B)}{P(A)}$$

Le conditionnement par $A$ correspond à une **restriction de l'univers** : $A$ devient le nouvel univers de référence.

### Formule des probabilités composées

$$P(A \cap B) = P(A) \times P_A(B)$$

### Absence de mémoire (loi exponentielle)

Soit $X$ une variable aléatoire suivant une loi exponentielle de paramètre $\lambda > 0$.

**Théorème** : pour tous réels $t, h > 0$ :

$$P_{X \geq t}(X \geq t+h) = P(X \geq h)$$

**Démonstration** :

$$P_{X \geq t}(X \geq t+h) = \frac{P(X \geq t+h)}{P(X \geq t)} = \frac{e^{-\lambda(t+h)}}{e^{-\lambda t}} = e^{-\lambda h} = P(X \geq h)$$

### Exemple

La durée de vie $X$ d'un composant suit une loi exponentielle de paramètre $\lambda = 0{,}0035$.

Calculons $P_{X \geq 200}(X \leq 300)$ :

$$P_{X \geq 200}(X \leq 300) = 1 - P_{X \geq 200}(X > 300) = 1 - P(X > 100) = P(X \leq 100)$$

$$= 1 - e^{-0{,}35} \approx 1 - 0{,}705 \approx 0{,}295$$
""",
                            "quiz": {
                                "titre": "Quiz — Probabilités conditionnelles",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La probabilité de B sachant A est définie par :",
                                        "choix": ["P(A) × P(B)", "P(A ∩ B) / P(A)", "P(A ∪ B) / P(B)", "P(B) / P(A ∩ B)"],
                                        "reponse_correcte": "P(A ∩ B) / P(A)",
                                        "explication": "P_A(B) = P(A ∩ B) / P(A), avec P(A) ≠ 0.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La loi exponentielle possède la propriété d'absence de mémoire.",
                                        "reponse_correcte": "vrai",
                                        "explication": "P(X ≥ t+h | X ≥ t) = P(X ≥ h) : le passé n'influence pas le futur.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Le conditionnement par A correspond à :",
                                        "choix": ["Un agrandissement de l'univers", "Une restriction de l'univers à A", "La suppression de A", "Une union avec A"],
                                        "reponse_correcte": "Une restriction de l'univers à A",
                                        "explication": "Conditionner par A revient à réduire l'univers des possibles à A.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Formule des Probabilités Totales et Variables Aléatoires",
                            "duree": 40,
                            "contenu": r"""## Probabilités Totales et Variables Aléatoires

### Formule des probabilités totales

Si $(A_1, A_2, \ldots, A_n)$ forme un **système complet d'événements** (partition de l'univers), alors pour tout événement $B$ :

$$P(B) = \sum_{i=1}^{n} P(A_i) \times P_{A_i}(B)$$

### Variable aléatoire discrète — Loi de Bernoulli

Lancer un dé équilibré. $X = 1$ si le résultat est pair, $X = 0$ sinon.

$$P(X = 1) = \frac{|\{2,4,6\}|}{6} = 0{,}5$$

$X$ suit une **loi de Bernoulli** de paramètre $p = 0{,}5$.

### Variable aléatoire continue — Densité

Une fonction $f$ définie sur un intervalle $I$ est une **densité de probabilité** si :

1. $f$ est **continue** et **positive** sur $I$
2. $\displaystyle\int_I f(t)\,dt = 1$

Pour tout $k \in I$ : $P(X = k) = \displaystyle\int_k^k f(t)\,dt = 0$.

### Espérance d'une variable continue

$$E(X) = \int_a^b t\,f(t)\,dt$$

### Exemple : dalles en plâtre

Masse $X$ (en tonnes) de densité $f(x) = 0{,}015x - 0{,}00075x^2$ sur $[0\,;\,20]$.

**Vérification** : $\displaystyle\int_0^{20} f(t)\,dt = \left[0{,}0075t^2 - 0{,}00025t^3\right]_0^{20} = 3 - 2 = 1$ ✓

**Espérance** :

$$E(X) = \int_0^{20} t(0{,}015t - 0{,}00075t^2)\,dt = \left[0{,}005t^3 - 0{,}0001875t^4\right]_0^{20} = 40 - 30 = 10 \text{ tonnes}$$
""",
                            "quiz": {
                                "titre": "Quiz — Probabilités totales et VA",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "vrai_faux",
                                        "texte": "Pour une variable aléatoire continue, P(X = k) = 0 pour tout k.",
                                        "reponse_correcte": "vrai",
                                        "explication": "L'intégrale sur un point est nulle : P(X = k) = ∫_k^k f(t) dt = 0.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Une fonction de densité doit vérifier :",
                                        "choix": ["f positive et intégrale = 0", "f positive et intégrale = 1", "f négative et intégrale = 1", "f quelconque et intégrale finie"],
                                        "reponse_correcte": "f positive et intégrale = 1",
                                        "explication": "Une densité est positive, continue, et son intégrale totale vaut 1.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Quelle est l'espérance de X pour la loi de Bernoulli de paramètre p ?",
                                        "reponse_correcte": "p",
                                        "tolerances": ["E(X) = p"],
                                        "explication": "E(X) = 0 × (1-p) + 1 × p = p.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Indépendance de Deux Événements",
                            "duree": 25,
                            "contenu": r"""## Indépendance de Deux Événements

### Définition

Deux événements $A$ et $B$ sont **indépendants** si et seulement si :

$$P(A \cap B) = P(A) \times P(B)$$

### Lien avec le conditionnement

Si $A$ et $B$ sont indépendants :

$$P_A(B) = \frac{P(A \cap B)}{P(A)} = \frac{P(A) \times P(B)}{P(A)} = P(B)$$

La réalisation de $A$ n'apporte **aucune information** utile pour prévoir $B$.

### Exemple : deux lancers de dé

Soit $X_1$ et $X_2$ les résultats de deux lancers successifs. On définit $X_i = 0$ si impair, $X_i = 1$ si pair.

$$P(X_1 = 0 \cap X_2 = 0) = P(X_1 = 0) \times P(X_2 = 0) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$$

L'égalité est vérifiée : les deux lancers sont **indépendants**.

### Propriétés dérivées

Si $A$ et $B$ sont indépendants, alors :

- $A$ et $\bar{B}$ sont indépendants
- $\bar{A}$ et $B$ sont indépendants
- $\bar{A}$ et $\bar{B}$ sont indépendants

### Attention à l'incompatibilité

Deux événements **incompatibles** (mutuellement exclusifs, $A \cap B = \emptyset$) de probabilités non nulles ne sont **jamais indépendants** car $P(A \cap B) = 0 \neq P(A) \times P(B)$.
""",
                            "quiz": {
                                "titre": "Quiz — Indépendance",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "A et B sont indépendants si et seulement si :",
                                        "choix": ["P(A ∩ B) = 0", "P(A ∩ B) = P(A) + P(B)", "P(A ∩ B) = P(A) × P(B)", "P(A ∪ B) = P(A) × P(B)"],
                                        "reponse_correcte": "P(A ∩ B) = P(A) × P(B)",
                                        "explication": "C'est la définition de l'indépendance de deux événements.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Deux événements incompatibles de probabilités non nulles sont indépendants.",
                                        "reponse_correcte": "faux",
                                        "explication": "Si A ∩ B = ∅, alors P(A∩B) = 0 ≠ P(A)×P(B) (si P(A) et P(B) > 0).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Si A et B sont indépendants, alors P_A(B) = P(B).",
                                        "reponse_correcte": "vrai",
                                        "explication": "Par définition : P_A(B) = P(A∩B)/P(A) = P(A)P(B)/P(A) = P(B).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "Indépendance de Variables Aléatoires et Échantillons",
                            "duree": 30,
                            "contenu": r"""## Variables Aléatoires et Échantillons

### Échantillon

Un **échantillon** de taille $n$ est une suite de variables aléatoires $X_1, X_2, \ldots, X_n$ :

- **Indépendantes** entre elles
- Suivant toutes la **même loi** que la variable $X$

### Variable aléatoire moyenne

$$M_n = \frac{X_1 + X_2 + \cdots + X_n}{n}$$

### Propriétés de $M_n$

| Propriété | Variable $X$ | Moyenne $M_n$ |
|---|---|---|
| Espérance | $E(X)$ | $E(M_n) = E(X)$ |
| Variance | $V(X)$ | $V(M_n) = \dfrac{V(X)}{n}$ |
| Écart-type | $\sigma(X)$ | $\sigma(M_n) = \dfrac{\sigma(X)}{\sqrt{n}}$ |

### Exemple : Bernoulli de paramètre $p = 0{,}5$

Pour $M_2$ (moyenne de deux lancers), les valeurs possibles sont $\{0\,;\, 0{,}5\,;\, 1\}$ :

| $k$ | $0$ | $0{,}5$ | $1$ |
|---|---|---|---|
| $P(M_2 = k)$ | $\frac{1}{4}$ | $\frac{1}{2}$ | $\frac{1}{4}$ |

$$E(M_2) = 0 \times \frac{1}{4} + 0{,}5 \times \frac{1}{2} + 1 \times \frac{1}{4} = 0{,}5 = E(X) \quad \checkmark$$

### Interprétation

- L'espérance de $M_n$ est **inchangée** par rapport à $E(X)$
- La variance **diminue** en $\frac{1}{n}$ : plus l'échantillon est grand, plus $M_n$ est concentrée autour de $E(X)$
""",
                            "quiz": {
                                "titre": "Quiz — Échantillons et moyenne",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "L'écart-type de la moyenne M_n d'un échantillon de taille n est σ(M_n) = ?",
                                        "reponse_correcte": "σ(X)/√n",
                                        "tolerances": ["sigma(X)/racine(n)", "sigma/racine de n"],
                                        "explication": "σ(M_n) = σ(X)/√n : l'écart-type diminue avec la racine de n.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "E(M_n) = E(X) quel que soit n.",
                                        "reponse_correcte": "vrai",
                                        "explication": "L'espérance de la moyenne d'un échantillon est égale à l'espérance de la variable.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Quand la taille n de l'échantillon augmente, la variance de M_n :",
                                        "choix": ["Augmente", "Reste constante", "Diminue", "Oscille"],
                                        "reponse_correcte": "Diminue",
                                        "explication": "V(M_n) = V(X)/n diminue quand n augmente.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "Inégalités de Concentration et Loi des Grands Nombres",
                            "duree": 35,
                            "contenu": r"""## Inégalités et Loi des Grands Nombres

### Inégalité de Bienaymé-Tchebychev

Pour toute variable aléatoire $X$ admettant une espérance et une variance, et pour tout réel $\delta > 0$ :

$$P(|X - E(X)| \geq \delta) \leq \frac{V(X)}{\delta^2}$$

### Inégalité de concentration

En appliquant Bienaymé-Tchebychev à la moyenne $M_n$ d'un échantillon :

$$P(|M_n - E(X)| \geq \delta) \leq \frac{V(X)}{n\delta^2}$$

Le membre de droite **tend vers 0** quand $n \to +\infty$.

### Loi des Grands Nombres

**Théorème** : soit $M_n$ la moyenne d'un échantillon de taille $n$ d'une variable $X$ d'espérance $E(X)$. Pour tout $\delta > 0$ :

$$\lim_{n \to +\infty} P(|M_n - E(X)| \geq \delta) = 0$$

**Démonstration** : par le **théorème des gendarmes**, car :

$$0 \leq P(|M_n - E(X)| \geq \delta) \leq \frac{V(X)}{n\delta^2} \xrightarrow[n \to +\infty]{} 0$$

### Interprétation

Ce résultat justifie l'**approche fréquentiste** des probabilités : pour un échantillon suffisamment grand, la moyenne observée $M_n$ converge vers l'espérance théorique $E(X)$.

### Application pratique

Pour estimer $E(X)$ avec une précision $\delta$ et un seuil de confiance $1 - \alpha$, il faut :

$$n \geq \frac{V(X)}{\alpha \, \delta^2}$$
""",
                            "quiz": {
                                "titre": "Quiz — LGN et inégalités",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "L'inégalité de Bienaymé-Tchebychev borne P(|X - E(X)| ≥ δ) par :",
                                        "choix": ["V(X) / δ", "V(X) / δ²", "E(X) / δ²", "σ(X) / δ"],
                                        "reponse_correcte": "V(X) / δ²",
                                        "explication": "P(|X - E(X)| ≥ δ) ≤ V(X) / δ².",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La loi des grands nombres affirme que M_n converge vers E(X) quand n → +∞.",
                                        "reponse_correcte": "vrai",
                                        "explication": "La probabilité que M_n s'écarte de E(X) de plus de δ tend vers 0.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "La loi des grands nombres justifie l'approche :",
                                        "choix": ["Bayésienne", "Fréquentiste", "Déterministe", "Axiomatique"],
                                        "reponse_correcte": "Fréquentiste",
                                        "explication": "La moyenne observée converge vers l'espérance : c'est le fondement fréquentiste.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                {
                    "ordre": 14,
                    "titre": "Probabilités — Lois à Densité",
                    "description": "Variables aléatoires continues, fonctions de densité, fonction de répartition, espérance, variance, loi uniforme et loi exponentielle avec propriété d'absence de mémoire.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Introduction aux Variables Aléatoires Continues",
                            "duree": 25,
                            "contenu": r"""## Du Discret au Continu

### Variables aléatoires discrètes (rappel)

- L'univers $\Omega$ est **fini** (ex : six faces d'un dé)
- La loi est définie par un tableau : chaque valeur $x_i$ a une probabilité $P(X = x_i)$
- $\displaystyle\sum P(X = x_i) = 1$

### Le passage au continu

De nombreux phénomènes ne se prêtent pas au découpage discret.

**Exemple** : la durée de vie $X$ d'un disque dur peut prendre toute valeur dans $[0\,;\,+\infty[$. La probabilité d'une valeur **exacte** (ex : exactement 5000,000... heures) est quasi nulle.

### La transition vers l'intégrale

Dans le cadre continu :
- La probabilité n'est plus associée à une **valeur isolée** mais à un **intervalle**
- On passe d'une logique de **sommation** ($\sum$) à une logique de **mesure d'aire** sous une courbe ($\int$)
- L'outil fondamental est la **fonction de densité**

### Conséquence fondamentale

Pour toute variable aléatoire continue $X$ et tout réel $c$ :

$$P(X = c) = 0$$

Les inégalités strictes ou larges donnent le même résultat :

$$P(c \leq X \leq d) = P(c < X < d) = P(c \leq X < d) = P(c < X \leq d)$$
""",
                            "quiz": {
                                "titre": "Quiz — Variables continues",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "vrai_faux",
                                        "texte": "Pour une variable aléatoire continue, P(X = c) = 0 pour tout c.",
                                        "reponse_correcte": "vrai",
                                        "explication": "L'intégrale sur un point unique est nulle.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Dans le cadre continu, la probabilité est associée à :",
                                        "choix": ["Une valeur exacte", "Un intervalle", "Un point isolé", "Un nombre entier"],
                                        "reponse_correcte": "Un intervalle",
                                        "explication": "En continu, on calcule P(a ≤ X ≤ b) par intégration sur un intervalle.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "P(c ≤ X ≤ d) = P(c < X < d) pour une variable continue.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Puisque P(X = c) = P(X = d) = 0, les bornes strictes ou larges ne changent rien.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Généralités sur les Fonctions de Densité",
                            "duree": 35,
                            "contenu": r"""## Fonctions de Densité

### Définition

Une **fonction de densité** est une fonction $f$ définie sur un intervalle $I$ vérifiant :

1. **Continuité** : $f$ est continue sur $I$
2. **Positivité** : $\forall x \in I,\; f(x) \geq 0$
3. **Normalisation** : $\displaystyle\int_I f(t)\,dt = 1$

### Calcul de probabilité

Si $X$ est une variable aléatoire continue de densité $f$ sur $[a\,;\,b]$ :

$$P(c \leq X \leq d) = \int_c^d f(t)\,dt$$

### Méthode de vérification

Pour prouver que $f$ est une densité sur $[a\,;\,b]$ :

1. **Continuité** : citer le type de fonction (polynomiale, exponentielle…)
2. **Positivité** : étudier le signe de $f$ sur $[a\,;\,b]$
3. **Intégrale** : calculer $\int_a^b f(t)\,dt$ et vérifier qu'elle vaut 1

### Exemple

Démontrer que $f(x) = 0{,}5x - 1$ est une densité sur $[2\,;\,4]$.

- **Continuité** : $f$ est affine, donc continue sur $\mathbb{R}$
- **Positivité** : sur $[2\,;\,4]$, $x \geq 2 \Rightarrow 0{,}5x \geq 1 \Rightarrow f(x) \geq 0$
- **Intégrale** :

$$\int_2^4 (0{,}5t - 1)\,dt = \left[0{,}25t^2 - t\right]_2^4 = (4 - 4) - (1 - 2) = 0 - (-1) = 1 \quad \checkmark$$
""",
                            "quiz": {
                                "titre": "Quiz — Fonctions de densité",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Une fonction de densité doit vérifier trois conditions :",
                                        "choix": ["Continuité, positivité, intégrale = 1", "Dérivabilité, croissance, intégrale = 0", "Positivité, décroissance, somme = 1", "Parité, bornée, intégrale = 1"],
                                        "reponse_correcte": "Continuité, positivité, intégrale = 1",
                                        "explication": "Les trois conditions impératives sont : continuité, positivité et intégrale totale égale à 1.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Si X est de densité f sur [a,b], comment calcule-t-on P(c ≤ X ≤ d) ?",
                                        "reponse_correcte": "intégrale de f de c à d",
                                        "tolerances": ["integrale de c a d de f(t)dt", "int_c^d f(t) dt"],
                                        "explication": "P(c ≤ X ≤ d) = ∫_c^d f(t) dt.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La fonction f(x) = 0,5x - 1 est une densité sur [2;4].",
                                        "reponse_correcte": "vrai",
                                        "explication": "f est continue, positive sur [2;4] et son intégrale vaut 1.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Fonction de Répartition, Espérance et Variance",
                            "duree": 35,
                            "contenu": r"""## Indicateurs d'une Loi Continue

### Fonction de répartition

Pour $X$ de densité $f$ sur $[a\,;\,b]$, la **fonction de répartition** $F$ est :

$$F(x) = P(X \leq x) = \int_a^x f(t)\,dt$$

$F$ est croissante, continue, avec $F(a) = 0$ et $F(b) = 1$. De plus, $F'(x) = f(x)$.

### Espérance

$$E(X) = \int_a^b t\,f(t)\,dt$$

C'est la **valeur moyenne** théorique de la variable $X$.

### Variance

$$V(X) = \int_a^b (t - E(X))^2\,f(t)\,dt = \int_a^b t^2\,f(t)\,dt - [E(X)]^2$$

L'**écart-type** est $\sigma(X) = \sqrt{V(X)}$.

### Exemple : production de dalles

$X$ (tonnes) suit la densité $f(x) = 0{,}015x - 0{,}00075x^2$ sur $[0\,;\,20]$.

**Probabilité** $P(X \geq 12)$ :

$$P(X \geq 12) = \int_{12}^{20} (0{,}015t - 0{,}00075t^2)\,dt = \left[0{,}0075t^2 - 0{,}00025t^3\right]_{12}^{20}$$

$$= 1 - 0{,}648 = 0{,}352$$

**Espérance** :

$$E(X) = \int_0^{20} t(0{,}015t - 0{,}00075t^2)\,dt = \left[0{,}005t^3 - 0{,}0001875t^4\right]_0^{20} = 40 - 30 = 10 \text{ tonnes}$$
""",
                            "quiz": {
                                "titre": "Quiz — Répartition, espérance, variance",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La fonction de répartition F(x) = P(X ≤ x) est :",
                                        "choix": ["Décroissante", "Croissante", "Constante", "Périodique"],
                                        "reponse_correcte": "Croissante",
                                        "explication": "F est croissante car f ≥ 0, donc l'intégrale croît avec x.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Quelle est la relation entre F' et f pour une variable continue ?",
                                        "reponse_correcte": "F'(x) = f(x)",
                                        "tolerances": ["F' = f", "la derivee de F est f"],
                                        "explication": "La dérivée de la fonction de répartition est la fonction de densité.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Pour l'exemple des dalles (f sur [0;20]), quelle est l'espérance E(X) ?",
                                        "reponse_correcte": "10",
                                        "tolerances": ["10 tonnes"],
                                        "explication": "E(X) = 40 - 30 = 10 tonnes.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "La Loi Uniforme",
                            "duree": 25,
                            "contenu": r"""## Loi Uniforme

### Définition

On dit que $X$ suit une **loi uniforme** sur $[a\,;\,b]$, notée $X \sim \mathcal{U}(a\,;\,b)$, si sa densité est **constante** :

$$f(x) = \frac{1}{b - a} \quad \text{pour } x \in [a\,;\,b]$$

### Cas particulier : $\mathcal{U}(0\,;\,1)$

La densité est $f(x) = 1$ sur $[0\,;\,1]$. C'est le modèle du « choix au hasard » d'un nombre dans $[0\,;\,1]$.

### Propriétés

| Propriété | Formule |
|---|---|
| **Densité** | $f(x) = \dfrac{1}{b-a}$ |
| **Fonction de répartition** | $F(x) = \dfrac{x-a}{b-a}$ |
| **Espérance** | $E(X) = \dfrac{a+b}{2}$ |
| **Variance** | $V(X) = \dfrac{(b-a)^2}{12}$ |

### Démonstration de l'espérance

$$E(X) = \int_a^b t \cdot \frac{1}{b-a}\,dt = \frac{1}{b-a} \left[\frac{t^2}{2}\right]_a^b = \frac{b^2 - a^2}{2(b-a)} = \frac{(b-a)(b+a)}{2(b-a)} = \frac{a+b}{2}$$

### Interprétation géométrique

La densité constante correspond à un **rectangle** de largeur $b - a$ et de hauteur $\frac{1}{b-a}$, dont l'aire est 1.

La probabilité $P(c \leq X \leq d)$ est le **rapport des longueurs** :

$$P(c \leq X \leq d) = \frac{d - c}{b - a}$$
""",
                            "quiz": {
                                "titre": "Quiz — Loi uniforme",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quelle est l'espérance de la loi uniforme U(a,b) ?",
                                        "reponse_correcte": "(a+b)/2",
                                        "tolerances": ["(a + b) / 2", "a+b sur 2"],
                                        "explication": "E(X) = (a+b)/2, c'est le milieu de l'intervalle.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "La densité de la loi uniforme U(a,b) est :",
                                        "choix": ["f(x) = 1", "f(x) = 1/(b-a)", "f(x) = (b-a)", "f(x) = x/(b-a)"],
                                        "reponse_correcte": "f(x) = 1/(b-a)",
                                        "explication": "La densité est constante : f(x) = 1/(b-a) sur [a;b].",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Quelle est la variance de U(0, 6) ?",
                                        "reponse_correcte": "3",
                                        "tolerances": ["36/12"],
                                        "explication": "V(X) = (b-a)²/12 = 36/12 = 3.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "La Loi Exponentielle",
                            "duree": 35,
                            "contenu": r"""## Loi Exponentielle

### Définition

$X$ suit une **loi exponentielle** de paramètre $\lambda > 0$ sur $[0\,;\,+\infty[$ si sa densité est :

$$f(x) = \lambda\,e^{-\lambda x}$$

### Fonction de répartition

$$F(x) = P(X \leq x) = \int_0^x \lambda\,e^{-\lambda t}\,dt = \left[-e^{-\lambda t}\right]_0^x = 1 - e^{-\lambda x}$$

D'où : $P(X > x) = e^{-\lambda x}$

### Espérance

$$E(X) = \frac{1}{\lambda}$$

### Propriété d'absence de mémoire

Pour tous $t, h > 0$ :

$$P_{X \geq t}(X \geq t + h) = P(X \geq h)$$

**Interprétation** : la probabilité qu'un composant survive encore $h$ heures **ne dépend pas** du temps $t$ déjà écoulé. C'est un modèle de « durée de vie sans vieillissement ».

### Raccourci utile

$$P_{X \geq a}(X \geq b) = P(X \geq b - a) \quad (b > a)$$

### Exemple d'application

Durée de vie $X \sim \mathcal{E}(0{,}0035)$. Sachant $X \geq 200$, probabilité de panne avant 300 heures :

$$P_{X \geq 200}(X \leq 300) = 1 - P_{X \geq 200}(X > 300) = 1 - P(X > 100) = P(X \leq 100)$$

$$= 1 - e^{-0{,}35} \approx 1 - 0{,}705 \approx 0{,}3$$

Il y a environ **30 %** de chances de défaillance.
""",
                            "quiz": {
                                "titre": "Quiz — Loi exponentielle",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quelle est l'espérance de la loi exponentielle de paramètre λ ?",
                                        "reponse_correcte": "1/λ",
                                        "tolerances": ["1/lambda", "un sur lambda"],
                                        "explication": "E(X) = 1/λ pour la loi exponentielle.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "P(X > x) pour X ~ Exp(λ) vaut :",
                                        "choix": ["1 - e^(-λx)", "e^(-λx)", "λe^(-λx)", "1 - λe^(-λx)"],
                                        "reponse_correcte": "e^(-λx)",
                                        "explication": "P(X > x) = 1 - F(x) = 1 - (1 - e^(-λx)) = e^(-λx).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La propriété d'absence de mémoire signifie que le passé influence le futur.",
                                        "reponse_correcte": "faux",
                                        "explication": "C'est le contraire : l'absence de mémoire signifie que le passé n'a aucune influence.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                    ],
                },
                {
                    "ordre": 15,
                    "titre": "Lois Normales, Intervalles de Fluctuation et Estimation",
                    "description": "Rappels sur les lois continues, lois uniforme et exponentielle, moyenne d'un échantillon, inégalités de concentration, loi des grands nombres et méthodes d'estimation.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Rappels : Variables Continues, Densité et Répartition",
                            "duree": 30,
                            "contenu": r"""## Rappels sur les Variables Continues

### Fonction de densité

Une fonction $f$ définie sur un intervalle $I$ est une **densité** si :

1. $f$ est **continue** sur $I$
2. $f(x) \geq 0$ pour tout $x \in I$
3. $\displaystyle\int_I f(t)\,dt = 1$

### Calcul de probabilités

$$P(X \in [c\,;\,d]) = \int_c^d f(t)\,dt$$

C'est l'**aire sous la courbe** de $f$ entre $c$ et $d$.

**Remarque** : $P(X = a) = 0$ pour toute variable continue, donc $P(X \leq a) = P(X < a)$.

### Fonction de répartition

$$F(x) = P(X \leq x) = \int_a^x f(t)\,dt$$

### Espérance et variance

$$E(X) = \int_a^b t\,f(t)\,dt \qquad V(X) = \int_a^b (t - E(X))^2 f(t)\,dt$$

### Exemple : vérifier qu'une fonction est une densité

$f(x) = 0{,}5x - 1$ sur $[2\,;\,4]$ :

- **Continue** : fonction affine ✓
- **Positive** : $x \geq 2 \Rightarrow 0{,}5x - 1 \geq 0$ ✓
- **Intégrale** : $\int_2^4 (0{,}5t-1)\,dt = [0{,}25t^2 - t]_2^4 = 0-(-1) = 1$ ✓
""",
                            "quiz": {
                                "titre": "Quiz — Rappels variables continues",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Pour une variable aléatoire continue, P(X = a) vaut :",
                                        "choix": ["f(a)", "F(a)", "0", "1"],
                                        "reponse_correcte": "0",
                                        "explication": "L'intégrale sur un point est nulle : P(X = a) = ∫_a^a f(t)dt = 0.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "P(X ≤ a) = P(X < a) pour une variable continue.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Puisque P(X = a) = 0, ajouter ou retirer la borne ne change rien.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "La fonction de répartition F est la dérivée de :",
                                        "choix": ["La densité f", "L'espérance E", "La variance V", "Rien, c'est F' = f"],
                                        "reponse_correcte": "Rien, c'est F' = f",
                                        "explication": "C'est l'inverse : F' = f. La dérivée de F est la densité.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Lois Usuelles : Uniforme et Exponentielle",
                            "duree": 30,
                            "contenu": r"""## Lois Usuelles à Densité

### Loi uniforme $\mathcal{U}(a\,;\,b)$

Modélise une **équirépartition** sur un intervalle.

| Propriété | Formule |
|---|---|
| Densité | $f(x) = \dfrac{1}{b-a}$ |
| Répartition | $F(x) = \dfrac{x-a}{b-a}$ |
| Espérance | $E(X) = \dfrac{a+b}{2}$ |
| Variance | $V(X) = \dfrac{(b-a)^2}{12}$ |

### Loi exponentielle $\mathcal{E}(\lambda)$

Modélise des **durées de vie** ou des **temps d'attente** sans usure.

| Propriété | Formule |
|---|---|
| Densité | $f(x) = \lambda\,e^{-\lambda x}$ sur $[0\,;\,+\infty[$ |
| Répartition | $F(x) = 1 - e^{-\lambda x}$ |
| Espérance | $E(X) = \dfrac{1}{\lambda}$ |

### Propriété d'absence de mémoire

Pour tous $t, h > 0$ :

$$P_{X \geq t}(X \geq t+h) = P(X \geq h)$$

Forme simplifiée : $P_{X \geq a}(X \geq b) = P(X \geq b - a)$ pour $b > a$.

### Application

$X \sim \mathcal{E}(0{,}0035)$, sachant $X \geq 200$, probabilité de panne avant 300h :

$$P_{X \geq 200}(X \leq 300) = P(X \leq 100) = 1 - e^{-0{,}35} \approx 0{,}3$$
""",
                            "quiz": {
                                "titre": "Quiz — Lois uniforme et exponentielle",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quelle est la densité de la loi uniforme U(a,b) ?",
                                        "reponse_correcte": "1/(b-a)",
                                        "tolerances": ["f(x) = 1/(b-a)", "un sur b moins a"],
                                        "explication": "f(x) = 1/(b-a) : densité constante sur [a;b].",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "L'espérance de la loi exponentielle de paramètre λ est :",
                                        "choix": ["λ", "1/λ", "λ²", "e^(-λ)"],
                                        "reponse_correcte": "1/λ",
                                        "explication": "E(X) = 1/λ pour la loi exponentielle.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La propriété d'absence de mémoire s'applique à la loi uniforme.",
                                        "reponse_correcte": "faux",
                                        "explication": "L'absence de mémoire est une propriété caractéristique de la loi exponentielle, pas de la loi uniforme.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Moyenne d'un Échantillon et Inégalités Fondamentales",
                            "duree": 30,
                            "contenu": r"""## Moyenne d'un Échantillon

### Échantillon et variable moyenne

Soit $X_1, X_2, \ldots, X_n$ un échantillon de taille $n$ (variables i.i.d. de même loi que $X$).

$$M_n = \frac{X_1 + X_2 + \cdots + X_n}{n}$$

### Propriétés de $M_n$

| | $X$ | $M_n$ |
|---|---|---|
| Espérance | $E(X)$ | $E(M_n) = E(X)$ |
| Variance | $V(X)$ | $V(M_n) = \dfrac{V(X)}{n}$ |
| Écart-type | $\sigma(X)$ | $\sigma(M_n) = \dfrac{\sigma(X)}{\sqrt{n}}$ |

### Inégalité de Bienaymé-Tchebychev

Pour toute variable aléatoire $X$ et tout $\delta > 0$ :

$$P(|X - E(X)| \geq \delta) \leq \frac{V(X)}{\delta^2}$$

### Inégalité de concentration

En appliquant Bienaymé-Tchebychev à $M_n$ :

$$P(|M_n - E(X)| \geq \delta) \leq \frac{V(X)}{n\,\delta^2}$$

Le second membre **tend vers 0** quand $n \to +\infty$, ce qui prépare la loi des grands nombres.
""",
                            "quiz": {
                                "titre": "Quiz — Échantillon et inégalités",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "texte_libre",
                                        "texte": "Quelle est la variance de M_n en fonction de V(X) et n ?",
                                        "reponse_correcte": "V(X)/n",
                                        "tolerances": ["V(X) / n", "variance de X sur n"],
                                        "explication": "V(M_n) = V(X)/n.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "L'inégalité de Bienaymé-Tchebychev donne une borne sur :",
                                        "choix": ["P(X = E(X))", "P(|X - E(X)| ≥ δ)", "P(X > 0)", "E(X²)"],
                                        "reponse_correcte": "P(|X - E(X)| ≥ δ)",
                                        "explication": "Elle majore la probabilité que X s'écarte de son espérance d'au moins δ.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "E(M_n) dépend de la taille n de l'échantillon.",
                                        "reponse_correcte": "faux",
                                        "explication": "E(M_n) = E(X) quel que soit n : l'espérance ne dépend pas de la taille.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 4,
                            "titre": "Loi des Grands Nombres et Estimation",
                            "duree": 35,
                            "contenu": r"""## Loi des Grands Nombres

### Énoncé

Pour tout réel $\delta > 0$ :

$$\lim_{n \to +\infty} P(|M_n - E(X)| \geq \delta) = 0$$

### Interprétation

Plus $n$ augmente, plus $M_n$ se **concentre** autour de $E(X)$. La moyenne observée converge vers l'espérance théorique.

### Méthode d'estimation : déterminer la taille d'un échantillon

**Énoncé** : $X \sim \text{Bernoulli}(p = 0{,}2)$. Trouver $n$ pour que $P(M_n \in [0{,}03\,;\,0{,}37]) \geq 0{,}95$.

**Correction** :

1. $E(X) = 0{,}2$. L'intervalle s'écrit $[0{,}2 - 0{,}17\,;\,0{,}2 + 0{,}17]$, donc $\delta = 0{,}17$.

2. On veut $P(|M_n - 0{,}2| < 0{,}17) \geq 0{,}95$, soit $P(|M_n - 0{,}2| \geq 0{,}17) \leq 0{,}05$.

3. Par l'inégalité de concentration avec $V(X) = p(1-p) = 0{,}16$ :

$$\frac{V(X)}{n\delta^2} \leq 0{,}05 \iff \frac{0{,}16}{n \times 0{,}0289} \leq 0{,}05$$

4. Résolution :

$$n \geq \frac{0{,}16}{0{,}05 \times 0{,}0289} \approx 110{,}7$$

Il faut un échantillon de taille $n \geq 111$.
""",
                            "quiz": {
                                "titre": "Quiz — LGN et estimation",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La loi des grands nombres affirme que quand n → +∞ :",
                                        "choix": ["V(M_n) → +∞", "M_n → 0", "M_n converge vers E(X)", "P(M_n = E(X)) = 1"],
                                        "reponse_correcte": "M_n converge vers E(X)",
                                        "explication": "La probabilité d'écart entre M_n et E(X) tend vers 0.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Pour X ~ Bernoulli(0.2), combien faut-il d'observations (minimum) pour que P(|M_n - 0.2| < 0.17) ≥ 0.95 ?",
                                        "reponse_correcte": "111",
                                        "tolerances": ["n = 111", "n >= 111"],
                                        "explication": "n ≥ 0.16 / (0.05 × 0.17²) ≈ 110.7, donc n ≥ 111.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "La loi des grands nombres fonde l'approche fréquentiste des probabilités.",
                                        "reponse_correcte": "vrai",
                                        "explication": "Elle justifie que la fréquence observée converge vers la probabilité théorique.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 5,
                            "titre": "Synthèse et Lien avec la Loi Normale",
                            "duree": 25,
                            "contenu": r"""## Synthèse Pédagogique

### Tableau récapitulatif des lois

| Loi | Paramètre(s) | Densité $f(x)$ | Espérance |
|---|---|---|---|
| **Uniforme** $\mathcal{U}(a\,;\,b)$ | $a, b$ | $\dfrac{1}{b-a}$ | $\dfrac{a+b}{2}$ |
| **Exponentielle** $\mathcal{E}(\lambda)$ | $\lambda > 0$ | $\lambda\,e^{-\lambda x}$ | $\dfrac{1}{\lambda}$ |
| **Moyenne** $M_n$ | taille $n$, loi de $X$ | dépend de $X$ | $E(X)$ |

### Lien avec la loi normale

Les résultats sur la concentration de la moyenne et la loi des grands nombres constituent le **fondement de l'inférence statistique**.

Ils préfigurent le **théorème de Moivre-Laplace** : sous certaines conditions, la loi binomiale $\mathcal{B}(n, p)$ peut être approchée par une **loi normale** $\mathcal{N}(np,\, np(1-p))$ quand $n$ est grand.

### La loi normale $\mathcal{N}(\mu, \sigma^2)$

Sa densité est la célèbre **courbe en cloche** :

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

**Propriétés** :
- Symétrique par rapport à $x = \mu$
- $E(X) = \mu$ et $V(X) = \sigma^2$
- **Règle des 68-95-99,7** :
  - $P(\mu - \sigma \leq X \leq \mu + \sigma) \approx 0{,}68$
  - $P(\mu - 2\sigma \leq X \leq \mu + 2\sigma) \approx 0{,}95$
  - $P(\mu - 3\sigma \leq X \leq \mu + 3\sigma) \approx 0{,}997$

### Remarque

L'inégalité de Bienaymé-Tchebychev est **universelle** mais pas optimale : les probabilités réelles sont souvent bien plus faibles que la borne supérieure théorique.
""",
                            "quiz": {
                                "titre": "Quiz — Synthèse et loi normale",
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "La règle des 68-95-99,7 concerne quelle loi ?",
                                        "choix": ["Loi uniforme", "Loi exponentielle", "Loi normale", "Loi de Bernoulli"],
                                        "reponse_correcte": "Loi normale",
                                        "explication": "Cette règle caractérise la répartition des valeurs autour de la moyenne pour la loi normale.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Quel pourcentage des valeurs tombe dans [μ - 2σ ; μ + 2σ] pour une loi normale ?",
                                        "reponse_correcte": "95%",
                                        "tolerances": ["0.95", "95", "environ 95%"],
                                        "explication": "P(μ - 2σ ≤ X ≤ μ + 2σ) ≈ 0,95, soit environ 95%.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "qcm",
                                        "texte": "Le théorème de Moivre-Laplace permet d'approcher la loi binomiale par :",
                                        "choix": ["La loi uniforme", "La loi exponentielle", "La loi normale", "La loi de Poisson"],
                                        "reponse_correcte": "La loi normale",
                                        "explication": "B(n,p) ≈ N(np, np(1-p)) quand n est grand.",
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
