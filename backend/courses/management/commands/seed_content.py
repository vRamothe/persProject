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
                # ── Ch.1 : Suites numériques ────────────────────────
                {
                    "ordre": 1,
                    "titre": "Suites numériques",
                    "description": "Suites arithmétiques et géométriques, raisonnement par récurrence, limites de suites.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Généralités, suites arithmétiques et géométriques",
                            "duree": 35,
                            "contenu": r"""# Généralités sur les suites

## Définition

Une **suite numérique** $(u_n)$ est une fonction de $\mathbb{N}$ (ou d'une partie de $\mathbb{N}$) dans $\mathbb{R}$.

- $(u_n)$ **croissante** si $u_{n+1} \ge u_n$ pour tout $n$.
- $(u_n)$ **majorée** s'il existe $M$ tel que $u_n \le M$ pour tout $n$.
- $(u_n)$ **bornée** si elle est majorée et minorée.

## Suite arithmétique

$(u_n)$ est **arithmétique** de raison $r$ si pour tout $n$ :

$$u_{n+1} = u_n + r$$

**Terme général :** $u_n = u_0 + nr$ ou $u_n = u_p + (n-p)r$.

**Somme des termes :**

$$\sum_{k=p}^{n} u_k = (n-p+1) \times \frac{u_p + u_n}{2}$$

En particulier : $\displaystyle\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$.

**Variations :** croissante si $r > 0$, décroissante si $r < 0$, constante si $r = 0$.

## Suite géométrique

$(u_n)$ est **géométrique** de raison $q$ si pour tout $n$ :

$$u_{n+1} = u_n \times q$$

**Terme général :** $u_n = u_0 \times q^n$ ou $u_n = u_p \times q^{n-p}$.

**Somme des termes ($q \neq 1$) :**

$$\sum_{k=p}^{n} u_k = u_p \times \frac{1 - q^{n-p+1}}{1 - q}$$

En particulier : $\displaystyle\sum_{k=0}^{n} q^k = \frac{1-q^{n+1}}{1-q}$.

**Variations :** croissante si $q > 1$, décroissante si $0 < q < 1$, alternée si $q < 0$.

## Suite arithmético-géométrique

Pour $u_{n+1} = a u_n + b$ avec $a \neq 1$, on cherche le point fixe $\alpha$ de $x = ax + b$, puis on pose $v_n = u_n - \alpha$. La suite $(v_n)$ est géométrique de raison $a$.

### Exemple

Soit $u_0 = 1$ et $u_{n+1} = 6 - 0{,}5 u_n$. Le point fixe est $\alpha = 4$.

On pose $v_n = u_n - 4$, alors $v_{n+1} = -0{,}5 v_n$ (géométrique de raison $-0{,}5$).

$v_n = -3 \times (-0{,}5)^n$ donc $u_n = 4 - 3 \times (-0{,}5)^n$.
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
                                        "explication": "u₁₀ = u₀ + 10r = 5 + 30 = 35.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Quelle est la somme 1 + 2 + … + 100 ?",
                                        "options": ["5000", "5050", "10000", "10100"],
                                        "reponse_correcte": "1",
                                        "explication": "S = n(n+1)/2 = 100×101/2 = 5050.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Une suite géométrique de raison q = −0,5 est monotone.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "Si q < 0, la suite est alternée : elle n'est pas monotone.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Raisonnement par récurrence",
                            "duree": 30,
                            "contenu": r"""# Le raisonnement par récurrence

## Principe

Pour démontrer qu'une propriété $\mathcal{P}(n)$ est vraie pour tout $n \ge n_0$, on procède en **trois étapes** :

1. **Initialisation :** on vérifie $\mathcal{P}(n_0)$.
2. **Hérédité :** on suppose $\mathcal{P}(k)$ vraie pour un $k \ge n_0$ quelconque (*hypothèse de récurrence*) et on démontre $\mathcal{P}(k+1)$.
3. **Conclusion :** par le principe de récurrence, $\mathcal{P}(n)$ est vraie pour tout $n \ge n_0$.

## Exemple 1 : Démontrer une formule

Soit $(u_n)$ définie par $u_0 = 2$ et $u_{n+1} = 2u_n - 3$. Montrer que $u_n = 3 - 2^n$.

- **Initialisation :** $u_0 = 3 - 2^0 = 2$ ✓
- **Hérédité :** si $u_k = 3 - 2^k$, alors $u_{k+1} = 2(3 - 2^k) - 3 = 6 - 2^{k+1} - 3 = 3 - 2^{k+1}$ ✓
- **Conclusion :** pour tout $n \ge 0$, $u_n = 3 - 2^n$.

## Exemple 2 : Démontrer une inégalité

Montrer que $2^n \ge n + 1$ pour tout $n \ge 1$.

- **Initialisation :** $2^1 = 2 \ge 2 = 1 + 1$ ✓
- **Hérédité :** si $2^k \ge k + 1$ alors $2^{k+1} = 2 \times 2^k \ge 2(k+1) = 2k + 2 \ge k + 2 = (k+1) + 1$ ✓
- **Conclusion :** pour tout $n \ge 1$, $2^n \ge n + 1$.

## Erreurs fréquentes

- Oublier l'**initialisation** (elle n'est jamais optionnelle).
- Utiliser la propriété au rang $n$ sans la supposer (on *suppose* $\mathcal{P}(k)$, on *démontre* $\mathcal{P}(k+1)$).
""",
                            "quiz": {
                                "titre": "Quiz — Récurrence",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quelles sont les deux étapes indispensables d'un raisonnement par récurrence ?",
                                        "options": [
                                            "Initialisation et hérédité",
                                            "Hypothèse et conclusion",
                                            "Calcul et vérification",
                                            "Analyse et synthèse",
                                        ],
                                        "reponse_correcte": "0",
                                        "explication": "Il faut d'abord vérifier la propriété au rang initial (initialisation) puis montrer l'hérédité.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Dans l'étape d'hérédité, on démontre P(k) à partir de P(k+1).",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "C'est l'inverse : on suppose P(k) et on démontre P(k+1).",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 3,
                            "titre": "Limites de suites",
                            "duree": 35,
                            "contenu": r"""# Notions de limites de suites

## Suite convergente

$(u_n)$ admet pour limite $\ell \in \mathbb{R}$ si tout intervalle ouvert contenant $\ell$ contient tous les termes de la suite à partir d'un certain rang.

$$\lim_{n \to +\infty} u_n = \ell$$

Autrement dit, pour tout $\alpha > 0$, il existe $N$ tel que pour tout $n \ge N$, $|u_n - \ell| < \alpha$.

## Suite divergente vers $+\infty$ ou $-\infty$

$\lim_{n \to +\infty} u_n = +\infty$ si tout intervalle $]A\,;\,+\infty[$ contient tous les termes à partir d'un certain rang.

## Limites de référence

$$\lim_{n \to +\infty} \frac{1}{n^k} = 0 \quad (k \ge 1) \qquad \lim_{n \to +\infty} n^k = +\infty \quad (k \ge 1) \qquad \lim_{n \to +\infty} \sqrt{n} = +\infty$$

Pour $q > 1$ : $\lim q^n = +\infty$. Pour $|q| < 1$ : $\lim q^n = 0$.

## Opérations sur les limites

Les limites se combinent par somme, produit, quotient, **sauf** dans les **formes indéterminées** :
- $+\infty - \infty$
- $0 \times \infty$
- $\frac{\infty}{\infty}$
- $\frac{0}{0}$

Pour lever une indétermination, on **factorise** par le terme dominant.

## Théorèmes de comparaison

### Théorème des gendarmes

Si $u_n \le v_n \le w_n$ à partir d'un certain rang et $\lim u_n = \lim w_n = \ell$, alors $\lim v_n = \ell$.

### Comparaison et divergence

- Si $u_n \ge v_n$ et $\lim v_n = +\infty$, alors $\lim u_n = +\infty$.
- Si $u_n \le v_n$ et $\lim v_n = -\infty$, alors $\lim u_n = -\infty$.

## Théorème de la suite monotone bornée

Toute suite **croissante et majorée** converge (de même, décroissante et minorée).
""",
                            "quiz": {
                                "titre": "Quiz — Limites de suites",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quelle est la limite de (1/n²) quand n → +∞ ?",
                                        "options": ["1", "+∞", "0", "−∞"],
                                        "reponse_correcte": "2",
                                        "explication": "1/n² → 0 car le dénominateur tend vers +∞.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Parmi ces expressions, laquelle est une forme indéterminée ?",
                                        "options": ["+∞ + 3", "0 × (+∞)", "+∞ × 2", "3/+∞"],
                                        "reponse_correcte": "1",
                                        "explication": "0 × ∞ est une forme indéterminée. Les autres ont des résultats directs.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on le théorème qui encadre une suite entre deux suites de même limite ?",
                                        "reponse_correcte": "gendarmes",
                                        "tolerances": ["gendarmes", "théorème des gendarmes", "theoreme des gendarmes", "sandwich"],
                                        "explication": "Le théorème des gendarmes (ou d'encadrement) permet de conclure quand u_n ≤ v_n ≤ w_n et lim u_n = lim w_n.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.2 : Étude de fonctions ────────────────────────
                {
                    "ordre": 2,
                    "titre": "Étude de fonctions",
                    "description": "Fonctions sinus et cosinus, limites de fonctions, continuité, dérivation et variations.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Fonctions sinus et cosinus",
                            "duree": 30,
                            "contenu": r"""# Fonctions sinus et cosinus

## Définition

Sur le cercle trigonométrique, pour tout réel $x$, le point $M$ d'abscisse angulaire $x$ a pour coordonnées $(\cos x\,;\,\sin x)$.

## Propriétés fondamentales

- $\cos^2 x + \sin^2 x = 1$
- $\cos(-x) = \cos x$ (fonction **paire**)
- $\sin(-x) = -\sin x$ (fonction **impaire**)
- Périodicité : $\cos(x + 2\pi) = \cos x$ et $\sin(x + 2\pi) = \sin x$

## Valeurs remarquables

| $x$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ |
|---|---|---|---|---|---|
| $\cos x$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ |
| $\sin x$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ |

## Dérivées

$$(\cos x)' = -\sin x \qquad (\sin x)' = \cos x$$

## Formules d'addition

$$\cos(a+b) = \cos a \cos b - \sin a \sin b$$
$$\sin(a+b) = \sin a \cos b + \cos a \sin b$$

## Formules de duplication

$$\cos(2a) = \cos^2 a - \sin^2 a = 2\cos^2 a - 1 = 1 - 2\sin^2 a$$
$$\sin(2a) = 2 \sin a \cos a$$
""",
                            "quiz": {
                                "titre": "Quiz — Fonctions sinus et cosinus",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quelle est la dérivée de sin(x) ?",
                                        "options": ["-cos(x)", "cos(x)", "-sin(x)", "sin(x)"],
                                        "reponse_correcte": "1",
                                        "explication": "(sin x)' = cos x.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Quelle est la valeur de cos(π/3) ?",
                                        "options": ["0", "1/2", "√2/2", "√3/2"],
                                        "reponse_correcte": "1",
                                        "explication": "cos(π/3) = 1/2.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Limites de fonctions, continuité et dérivation",
                            "duree": 40,
                            "contenu": r"""# Limites de fonctions

## Limites en l'infini

$\lim_{x \to +\infty} f(x) = \ell$ signifie que $f(x)$ est aussi proche de $\ell$ que l'on veut pour $x$ assez grand. Si $\ell$ est fini, la droite $y = \ell$ est **asymptote horizontale**.

## Limites en un point

$\lim_{x \to a} f(x) = \pm\infty$ : la droite $x = a$ est **asymptote verticale**.

## Limites de référence

$$\lim_{x \to +\infty} x^n = +\infty \quad (n \ge 1) \qquad \lim_{x \to 0^+} \frac{1}{x} = +\infty \qquad \lim_{x \to +\infty} \frac{1}{x^n} = 0$$

## Opérations et formes indéterminées

Même principe que pour les suites : somme, produit, quotient. **Formes indéterminées :** $\frac{0}{0}$, $\frac{\infty}{\infty}$, $0 \times \infty$, $\infty - \infty$.

**Méthode :** factoriser par le terme de plus haut degré.

# Continuité

## Théorème des valeurs intermédiaires (TVI)

Si $f$ est continue sur $[a\,;\,b]$ et $k$ est un réel compris entre $f(a)$ et $f(b)$, alors il existe $c \in [a\,;\,b]$ tel que $f(c) = k$.

**Corollaire :** si $f$ est **strictement monotone** sur $[a\,;\,b]$, ce $c$ est **unique**.

# Dérivation

## Nombre dérivé et tangente

$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$

Équation de la tangente en $a$ : $y = f'(a)(x - a) + f(a)$.

## Formulaire

| $f(x)$ | $f'(x)$ |
|---|---|
| $x^n$ | $nx^{n-1}$ |
| $\frac{1}{x}$ | $-\frac{1}{x^2}$ |
| $\sqrt{x}$ | $\frac{1}{2\sqrt{x}}$ |

Opérations : $(uv)' = u'v + uv'$, $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$.

## Lien dérivée-variations

- $f'(x) \ge 0$ sur $I$ $\Leftrightarrow$ $f$ croissante sur $I$.
- $f'(x) \le 0$ sur $I$ $\Leftrightarrow$ $f$ décroissante sur $I$.
- Si $f'(a) = 0$ et $f'$ change de signe en $a$ : **extremum local**.
""",
                            "quiz": {
                                "titre": "Quiz — Limites, continuité et dérivation",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Si f est continue sur [a,b] et f(a)×f(b) < 0, que peut-on conclure ?",
                                        "options": [
                                            "f admet un maximum sur [a,b]",
                                            "f s'annule au moins une fois sur ]a,b[",
                                            "f est dérivable sur ]a,b[",
                                            "f est monotone sur [a,b]",
                                        ],
                                        "reponse_correcte": "1",
                                        "explication": "Par le TVI, si f(a) et f(b) sont de signes contraires, il existe c ∈ ]a,b[ tel que f(c) = 0.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on la droite y = ℓ lorsque lim f(x) = ℓ en +∞ ?",
                                        "reponse_correcte": "asymptote horizontale",
                                        "tolerances": ["asymptote horizontale", "asymptote", "horizontale"],
                                        "explication": "Quand f(x) → ℓ en ±∞, la droite y = ℓ est une asymptote horizontale.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.3 : Probabilités conditionnelles ──────────────
                {
                    "ordre": 3,
                    "titre": "Probabilités : conditionnement et indépendance",
                    "description": "Probabilités conditionnelles, formule des probabilités totales, indépendance.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Probabilités conditionnelles",
                            "duree": 35,
                            "contenu": r"""# Probabilités conditionnelles

## Définition

Soient $A$ et $B$ deux événements avec $P(A) \neq 0$. La **probabilité de $B$ sachant $A$** est :

$$P_A(B) = \frac{P(A \cap B)}{P(A)}$$

## Probabilité d'une intersection

$$P(A \cap B) = P(A) \times P_A(B) = P(B) \times P_B(A)$$

**Attention :** ne pas confondre $P(A \cap B)$, $P_A(B)$ et $P_B(A)$.

## Probabilité de l'événement contraire sachant $A$

$$P_A(\bar{B}) = 1 - P_A(B)$$

## Arbre pondéré

- Sur chaque branche, on inscrit la probabilité conditionnelle.
- La probabilité d'un chemin = produit des probabilités des branches.
- La probabilité d'un événement = somme des probabilités des chemins y aboutissant.

### Exemple

Urne : 3 blanches, 5 noires. Tirage sans remise de 2 boules.

$P(B_1) = \frac{3}{8}$, $P_{B_1}(B_2) = \frac{2}{7}$ donc $P(B_1 \cap B_2) = \frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \frac{3}{28}$.

## Formule des probabilités totales

Si $A_1, A_2, \ldots, A_n$ forment une **partition** de $\Omega$ (incompatibles deux à deux, de réunion $\Omega$), avec $P(A_i) > 0$, alors :

$$P(B) = \sum_{i=1}^{n} P(A_i) \times P_{A_i}(B)$$

Cas usuel ($A$ et $\bar{A}$) :

$$P(B) = P(A) \times P_A(B) + P(\bar{A}) \times P_{\bar{A}}(B)$$
""",
                            "quiz": {
                                "titre": "Quiz — Probabilités conditionnelles",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "P(A) = 0,6 et P_A(B) = 0,5. Que vaut P(A ∩ B) ?",
                                        "options": ["0,10", "0,30", "0,55", "1,10"],
                                        "reponse_correcte": "1",
                                        "explication": "P(A ∩ B) = P(A) × P_A(B) = 0,6 × 0,5 = 0,30.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on la formule P(B) = P(A)·P_A(B) + P(Ā)·P_Ā(B) ?",
                                        "reponse_correcte": "probabilités totales",
                                        "tolerances": ["probabilités totales", "probabilites totales", "formule des probabilités totales", "formule des probabilites totales"],
                                        "explication": "C'est la formule des probabilités totales, appliquée à la partition {A, Ā}.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Indépendance de deux événements",
                            "duree": 25,
                            "contenu": r"""# Indépendance de deux événements

## Définition

Deux événements $A$ et $B$ sont **indépendants** si et seulement si :

$$P(A \cap B) = P(A) \times P(B)$$

Cela équivaut à $P_A(B) = P(B)$ (savoir que $A$ est réalisé ne change pas la probabilité de $B$).

## Propriétés

Si $A$ et $B$ sont indépendants, alors $A$ et $\bar{B}$ sont indépendants (de même $\bar{A}$ et $B$, $\bar{A}$ et $\bar{B}$).

**Attention :** indépendance $\neq$ incompatibilité.
- Deux événements incompatibles ($A \cap B = \emptyset$) ne sont **jamais** indépendants (sauf si l'un est impossible).

## Succession d'épreuves indépendantes

Lorsqu'on répète $n$ fois de façon **indépendante** une même épreuve de Bernoulli (succès de probabilité $p$), le nombre de succès suit une **loi binomiale** $\mathcal{B}(n, p)$.

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

$E(X) = np$, $\sigma(X) = \sqrt{np(1-p)}$.
""",
                            "quiz": {
                                "titre": "Quiz — Indépendance",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "vrai_faux",
                                        "texte": "Deux événements incompatibles de probabilité non nulle sont indépendants.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "Si A ∩ B = ∅ avec P(A)>0 et P(B)>0, alors P(A∩B) = 0 ≠ P(A)×P(B), donc non indépendants.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "A et B indépendants, P(A) = 0,3, P(B) = 0,4. Que vaut P(A ∩ B) ?",
                                        "options": ["0,70", "0,12", "0,10", "0,07"],
                                        "reponse_correcte": "1",
                                        "explication": "P(A ∩ B) = P(A) × P(B) = 0,3 × 0,4 = 0,12.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.4 : Fonction exponentielle ────────────────────
                {
                    "ordre": 4,
                    "titre": "Fonction exponentielle",
                    "description": "Définition, propriétés algébriques, étude complète et équations avec exp.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Définition et propriétés algébriques de exp",
                            "duree": 35,
                            "contenu": r"""# La fonction exponentielle

## Définition (théorème d'existence et d'unicité)

Il existe une **unique** fonction $f$ définie et dérivable sur $\mathbb{R}$ telle que :

$$f' = f \quad \text{et} \quad f(0) = 1$$

Cette fonction est appelée **fonction exponentielle**, notée $\exp$.

## Conséquences immédiates

- $\exp'(x) = \exp(x)$ pour tout $x \in \mathbb{R}$.
- $\exp(0) = 1$.
- Pour tout $x$, $\exp(x) \neq 0$ (démonstration : $\exp(x) \times \exp(-x) = 1$).
- Pour tout $x$, $\exp(x) > 0$.

## Notation

On note $e = \exp(1) \approx 2{,}718$. On écrit $e^x$ au lieu de $\exp(x)$.

## Propriétés algébriques

Pour tous réels $a$ et $b$ :

$$e^{a+b} = e^a \times e^b \qquad e^{a-b} = \frac{e^a}{e^b} \qquad (e^a)^n = e^{na} \qquad e^{-a} = \frac{1}{e^a}$$

**Démonstration de $e^{a+b} = e^a \times e^b$ :** on pose $f(x) = \frac{\exp(x+b)}{\exp(b)}$, on montre $f' = f$ et $f(0) = 1$, donc $f = \exp$ par unicité.

## Équations et inéquations

La fonction $\exp$ est une **bijection** de $\mathbb{R}$ sur $]0\,;\,+\infty[$ :

$$e^a = e^b \iff a = b \qquad e^a < e^b \iff a < b$$
""",
                            "quiz": {
                                "titre": "Quiz — Définition et propriétés de exp",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Que vaut exp(0) ?",
                                        "options": ["0", "1", "e", "−1"],
                                        "reponse_correcte": "1",
                                        "explication": "Par définition, exp(0) = 1.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Simplifier e³ × e⁻¹.",
                                        "options": ["e⁴", "e²", "e⁻³", "1"],
                                        "reponse_correcte": "1",
                                        "explication": "e³ × e⁻¹ = e^(3+(−1)) = e².",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "vrai_faux",
                                        "texte": "Il existe un réel x tel que eˣ = 0.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "Pour tout réel x, eˣ > 0. L'exponentielle ne s'annule jamais.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Étude de la fonction exponentielle",
                            "duree": 30,
                            "contenu": r"""# Étude de la fonction exponentielle

## Sens de variation

$\exp'(x) = \exp(x) > 0$ pour tout $x$ : la fonction exponentielle est **strictement croissante** sur $\mathbb{R}$.

## Limites

$$\lim_{x \to +\infty} e^x = +\infty \qquad \lim_{x \to -\infty} e^x = 0$$

## Croissances comparées (résultats fondamentaux)

$$\lim_{x \to +\infty} \frac{e^x}{x^n} = +\infty \qquad \lim_{x \to -\infty} x^n e^x = 0$$

*L'exponentielle l'emporte toujours sur toute puissance de $x$.*

## Dérivée de $e^{u(x)}$

Si $u$ est dérivable, alors $(e^u)' = u' \times e^u$.

### Exemple

$f(x) = e^{3x+1}$ → $f'(x) = 3 e^{3x+1}$.

## Tableau de variation type

Pour $f(x) = (ax+b) e^{cx}$, on dérive : $f'(x) = (ac x + bc + a) e^{cx}$. Le signe de $f'(x)$ dépend de celui du facteur polynomial puisque $e^{cx} > 0$.

## Équations différentielles $y' = ky$

Les solutions de $y' = ky$ sont les fonctions $y(x) = C e^{kx}$ avec $C \in \mathbb{R}$.

Si $y(0) = y_0$, alors $C = y_0$ et l'unique solution est $y(x) = y_0 e^{kx}$.

*Application : désintégration radioactive $N(t) = N_0 e^{-\lambda t}$.*
""",
                            "quiz": {
                                "titre": "Quiz — Étude de exp",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quelle est la limite de eˣ/x² quand x → +∞ ?",
                                        "options": ["0", "1", "+∞", "e"],
                                        "reponse_correcte": "2",
                                        "explication": "Par croissance comparée, eˣ l'emporte sur x² : la limite est +∞.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Quelle est la dérivée de e^(2x) ?",
                                        "reponse_correcte": "2e^(2x)",
                                        "tolerances": ["2e^(2x)", "2 e^(2x)", "2exp(2x)", "2e^2x"],
                                        "explication": "(e^u)' = u'·e^u, ici u = 2x donc u' = 2.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.5 : Fonction logarithme népérien ──────────────
                {
                    "ordre": 5,
                    "titre": "Fonction logarithme népérien",
                    "description": "Définition comme réciproque de exp, propriétés algébriques, étude et compléments.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Définition et propriétés algébriques de ln",
                            "duree": 35,
                            "contenu": r"""# La fonction logarithme népérien

## Définition

La fonction logarithme népérien, notée $\ln$, est la **bijection réciproque** de la fonction exponentielle.

$$\ln : ]0\,;\,+\infty[ \to \mathbb{R}$$

$$\ln(x) = y \iff e^y = x$$

## Valeurs fondamentales

- $\ln 1 = 0$
- $\ln e = 1$
- $\ln(e^n) = n$

## Relation fondamentale

Pour tout $x > 0$ : $e^{\ln x} = x$. Pour tout $x \in \mathbb{R}$ : $\ln(e^x) = x$.

## Propriétés algébriques

Pour $a > 0$ et $b > 0$ :

$$\ln(ab) = \ln a + \ln b \qquad \ln\!\left(\frac{a}{b}\right) = \ln a - \ln b$$

$$\ln(a^n) = n \ln a \qquad \ln\!\left(\frac{1}{a}\right) = -\ln a \qquad \ln(\sqrt{a}) = \frac{1}{2}\ln a$$

*L'exponentielle transforme les sommes en produits ; le logarithme transforme les produits en sommes.*

## Équations et inéquations

La fonction $\ln$ est **strictement croissante** :

$$\ln a = \ln b \iff a = b \qquad \ln a < \ln b \iff a < b$$

### Exemple

$\ln(x-1) = 3 \iff x - 1 = e^3 \iff x = 1 + e^3$.
""",
                            "quiz": {
                                "titre": "Quiz — Définition et propriétés de ln",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Que vaut ln(1) ?",
                                        "options": ["1", "0", "e", "−1"],
                                        "reponse_correcte": "1",
                                        "explication": "ln(1) = 0 car e⁰ = 1.",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Simplifier ln(a²) − ln(a) pour a > 0.",
                                        "options": ["ln(a)", "2", "ln(2a)", "a"],
                                        "reponse_correcte": "0",
                                        "explication": "ln(a²) − ln(a) = 2ln(a) − ln(a) = ln(a).",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 3,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on la relation ln(ab) = ln(a) + ln(b) ?",
                                        "reponse_correcte": "logarithme d'un produit",
                                        "tolerances": ["logarithme d'un produit", "ln d'un produit", "propriété du produit", "relation fonctionnelle"],
                                        "explication": "ln transforme un produit en somme : c'est la propriété fondamentale du logarithme.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Étude de la fonction ln et compléments",
                            "duree": 30,
                            "contenu": r"""# Étude de la fonction logarithme népérien

## Dérivée

$$(\ln x)' = \frac{1}{x} \quad (x > 0)$$

Plus généralement, si $u > 0$ : $(\ln u)' = \frac{u'}{u}$.

## Sens de variation

$\ln'(x) = \frac{1}{x} > 0$ pour $x > 0$ → $\ln$ est **strictement croissante** sur $]0\,;\,+\infty[$.

## Limites

$$\lim_{x \to +\infty} \ln x = +\infty \qquad \lim_{x \to 0^+} \ln x = -\infty$$

## Croissances comparées

$$\lim_{x \to +\infty} \frac{\ln x}{x} = 0 \qquad \lim_{x \to 0^+} x \ln x = 0$$

Plus généralement : $\displaystyle\lim_{x \to +\infty} \frac{\ln x}{x^n} = 0$ pour tout $n \ge 1$.

*N'importe quelle puissance de $x$ l'emporte sur $\ln x$.*

## Logarithme décimal

$$\log_{10}(x) = \frac{\ln x}{\ln 10}$$

Le logarithme décimal est utilisé pour l'échelle des décibels, le pH, etc.

## Tableau de variation

| $x$ | $0$ | | $+\infty$ |
|---|---|---|---|
| $\ln'(x)$ | | $+$ | |
| $\ln(x)$ | $-\infty$ | ↗ | $+\infty$ |
""",
                            "quiz": {
                                "titre": "Quiz — Étude de ln",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quelle est la limite de ln(x)/x quand x → +∞ ?",
                                        "options": ["+∞", "1", "0", "−∞"],
                                        "reponse_correcte": "2",
                                        "explication": "Par croissance comparée, ln(x) croît moins vite que x : ln(x)/x → 0.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La limite de x·ln(x) quand x → 0⁺ est −∞.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "faux",
                                        "explication": "lim(x→0⁺) x·ln(x) = 0 (croissance comparée).",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.6 : Nombres complexes ─────────────────────────
                {
                    "ordre": 6,
                    "titre": "Nombres complexes",
                    "description": "Forme algébrique, forme trigonométrique, module, argument et opérations.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Définition et forme algébrique",
                            "duree": 35,
                            "contenu": r"""# Nombres complexes — Forme algébrique

## L'ensemble $\mathbb{C}$

On définit l'ensemble $\mathbb{C}$ des nombres complexes en introduisant un nombre $i$ tel que $i^2 = -1$.

Tout nombre complexe $z$ s'écrit de manière unique sous la forme :

$$z = a + ib \quad (a, b \in \mathbb{R})$$

- $a = \text{Re}(z)$ : **partie réelle**
- $b = \text{Im}(z)$ : **partie imaginaire**

## Conjugué

Le **conjugué** de $z = a + ib$ est $\bar{z} = a - ib$.

**Propriétés :**
- $z + \bar{z} = 2a$, $z - \bar{z} = 2ib$
- $\overline{z_1 + z_2} = \bar{z_1} + \bar{z_2}$, $\overline{z_1 \times z_2} = \bar{z_1} \times \bar{z_2}$
- $z \times \bar{z} = a^2 + b^2$ (toujours réel positif)

## Module

$$|z| = \sqrt{a^2 + b^2}$$

**Propriétés :** $|z_1 z_2| = |z_1| \times |z_2|$, $\left|\frac{z_1}{z_2}\right| = \frac{|z_1|}{|z_2|}$.

## Interprétation géométrique

Dans le plan complexe, $z = a + ib$ correspond au point $M(a\,;\,b)$. Le module $|z|$ est la distance $OM$.

## Équation du second degré dans $\mathbb{C}$

Pour $az^2 + bz + c = 0$ avec $\Delta = b^2 - 4ac$ :
- Si $\Delta > 0$ : deux solutions réelles.
- Si $\Delta = 0$ : une solution double réelle.
- Si $\Delta < 0$ : deux solutions complexes conjuguées $z = \frac{-b \pm i\sqrt{|\Delta|}}{2a}$.
""",
                            "quiz": {
                                "titre": "Quiz — Forme algébrique",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quel est le module de z = 3 + 4i ?",
                                        "options": ["7", "5", "25", "√7"],
                                        "reponse_correcte": "1",
                                        "explication": "|z| = √(9+16) = √25 = 5.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Que vaut i² ?",
                                        "options": ["1", "−1", "i", "−i"],
                                        "reponse_correcte": "1",
                                        "explication": "Par définition, i² = −1.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Forme trigonométrique",
                            "duree": 30,
                            "contenu": r"""# Forme trigonométrique

## Écriture

Tout nombre complexe $z \neq 0$ peut s'écrire :

$$z = r(\cos\theta + i\sin\theta)$$

où $r = |z|$ (module) et $\theta = \arg(z)$ (argument, défini modulo $2\pi$).

## Formule d'Euler (notation exponentielle)

$$e^{i\theta} = \cos\theta + i\sin\theta$$

Donc $z = r e^{i\theta}$.

## Opérations en forme trigonométrique

Pour $z_1 = r_1 e^{i\theta_1}$ et $z_2 = r_2 e^{i\theta_2}$ :

$$z_1 z_2 = r_1 r_2 \, e^{i(\theta_1 + \theta_2)} \qquad \frac{z_1}{z_2} = \frac{r_1}{r_2} \, e^{i(\theta_1 - \theta_2)}$$

*Les modules se multiplient, les arguments s'ajoutent.*

## Formule de Moivre

$$(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$$

## Arguments remarquables

| $z$ | $1$ | $-1$ | $i$ | $-i$ |
|---|---|---|---|---|
| $\arg(z)$ | $0$ | $\pi$ | $\frac{\pi}{2}$ | $-\frac{\pi}{2}$ |

## Applications géométriques

- $|z_B - z_A| = AB$ (distance entre deux points)
- $\arg\!\left(\frac{z_C - z_A}{z_B - z_A}\right) = (\overrightarrow{AB}\,,\,\overrightarrow{AC})$ (angle orienté)
""",
                            "quiz": {
                                "titre": "Quiz — Forme trigonométrique",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quel est l'argument de z = −1 ?",
                                        "options": ["0", "π/2", "π", "−π"],
                                        "reponse_correcte": "2",
                                        "explication": "−1 = e^(iπ), donc arg(−1) = π.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment s'appelle la formule (cos θ + i sin θ)ⁿ = cos(nθ) + i sin(nθ) ?",
                                        "reponse_correcte": "Moivre",
                                        "tolerances": ["Moivre", "formule de Moivre", "De Moivre", "formule de moivre"],
                                        "explication": "C'est la formule de Moivre, utilisée pour calculer les puissances n-ièmes.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.7 : Intégration ───────────────────────────────
                {
                    "ordre": 7,
                    "titre": "Intégration",
                    "description": "Aire et intégrale, primitives, théorème fondamental et applications du calcul intégral.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Aire, intégrale et primitives",
                            "duree": 40,
                            "contenu": r"""# Intégration

## Intégrale d'une fonction continue et positive

Soit $f$ une fonction **continue et positive** sur $[a\,;\,b]$. L'intégrale $\displaystyle\int_a^b f(x)\,\mathrm{d}x$ est l'**aire** (en u.a.) du domaine compris entre la courbe de $f$, l'axe des abscisses et les droites $x = a$, $x = b$.

## Primitives

### Définition

$F$ est une **primitive** de $f$ sur un intervalle $I$ si $F'(x) = f(x)$ pour tout $x \in I$.

Si $F$ est une primitive de $f$, toutes les primitives s'écrivent $F(x) + C$ ($C \in \mathbb{R}$).

### Primitives usuelles

| $f(x)$ | $F(x)$ |
|---|---|
| $x^n$ ($n \neq -1$) | $\frac{x^{n+1}}{n+1}$ |
| $\frac{1}{x}$ ($x > 0$) | $\ln x$ |
| $e^x$ | $e^x$ |
| $\cos x$ | $\sin x$ |
| $\sin x$ | $-\cos x$ |

### Primitives de fonctions composées

| $f(x)$ | $F(x)$ |
|---|---|
| $u'(x) \, e^{u(x)}$ | $e^{u(x)}$ |
| $\frac{u'(x)}{u(x)}$ ($u > 0$) | $\ln(u(x))$ |
| $u'(x) \, [u(x)]^n$ ($n \neq -1$) | $\frac{[u(x)]^{n+1}}{n+1}$ |

## Théorème fondamental

Si $f$ est continue sur $[a\,;\,b]$ et $F$ est une primitive de $f$, alors :

$$\int_a^b f(x)\,\mathrm{d}x = F(b) - F(a) = [F(x)]_a^b$$
""",
                            "quiz": {
                                "titre": "Quiz — Intégrale et primitives",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quelle est une primitive de f(x) = 2x ?",
                                        "options": ["2", "x²", "x² + 1", "2x²"],
                                        "reponse_correcte": "1",
                                        "explication": "F(x) = x² car F'(x) = 2x. (x²+1 est aussi correcte, mais x² est la primitive usuelle.)",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "Que vaut ∫₀¹ eˣ dx ?",
                                        "options": ["e", "e − 1", "1", "e + 1"],
                                        "reponse_correcte": "1",
                                        "explication": "[eˣ]₀¹ = e¹ − e⁰ = e − 1.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Propriétés de l'intégrale et applications",
                            "duree": 30,
                            "contenu": r"""# Propriétés et applications de l'intégrale

## Propriétés

### Linéarité

$$\int_a^b [\alpha f(x) + \beta g(x)]\,\mathrm{d}x = \alpha \int_a^b f(x)\,\mathrm{d}x + \beta \int_a^b g(x)\,\mathrm{d}x$$

### Relation de Chasles

$$\int_a^b f(x)\,\mathrm{d}x + \int_b^c f(x)\,\mathrm{d}x = \int_a^c f(x)\,\mathrm{d}x$$

### Positivité

Si $f(x) \ge 0$ sur $[a\,;\,b]$ alors $\displaystyle\int_a^b f(x)\,\mathrm{d}x \ge 0$.

Si $f(x) \ge g(x)$ sur $[a\,;\,b]$ alors $\displaystyle\int_a^b f(x)\,\mathrm{d}x \ge \int_a^b g(x)\,\mathrm{d}x$.

### Convention d'orientation

$$\int_a^b f(x)\,\mathrm{d}x = -\int_b^a f(x)\,\mathrm{d}x$$

## Valeur moyenne

La **valeur moyenne** de $f$ sur $[a\,;\,b]$ est :

$$\mu = \frac{1}{b-a}\int_a^b f(x)\,\mathrm{d}x$$

## Aires entre deux courbes

L'aire entre les courbes de $f$ et $g$ sur $[a\,;\,b]$ est :

$$\mathcal{A} = \int_a^b |f(x) - g(x)|\,\mathrm{d}x$$

Si $f(x) \ge g(x)$ sur $[a\,;\,b]$, on peut ôter la valeur absolue.

### Exemple

Aire entre $y = x^2$ et $y = x$ sur $[0\,;\,1]$ :

$$\mathcal{A} = \int_0^1 (x - x^2)\,\mathrm{d}x = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$$
""",
                            "quiz": {
                                "titre": "Quiz — Propriétés et applications",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Que vaut la valeur moyenne de f(x) = x sur [0 ; 4] ?",
                                        "options": ["2", "4", "8", "16"],
                                        "reponse_correcte": "0",
                                        "explication": "μ = (1/4)∫₀⁴ x dx = (1/4)[x²/2]₀⁴ = (1/4)×8 = 2.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on la propriété ∫ₐᵇ f + ∫ᵇᶜ f = ∫ₐᶜ f ?",
                                        "reponse_correcte": "relation de Chasles",
                                        "tolerances": ["relation de Chasles", "Chasles", "chasles", "relation de chasles"],
                                        "explication": "C'est la relation de Chasles pour les intégrales.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.8 : Lois à densité ────────────────────────────
                {
                    "ordre": 8,
                    "titre": "Lois à densité",
                    "description": "Variables aléatoires continues, loi uniforme, loi exponentielle.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Lois de probabilité à densité",
                            "duree": 30,
                            "contenu": r"""# Lois de probabilité à densité

## Variable aléatoire continue

Lorsque l'univers est un intervalle $I$ de $\mathbb{R}$, on utilise des **variables aléatoires continues** dont les valeurs forment un intervalle.

## Densité de probabilité

Une fonction $f$ définie sur $I$ est une **densité de probabilité** si :
- $f$ est continue sur $I$
- $f(x) \ge 0$ pour tout $x \in I$
- L'aire sous la courbe de $f$ est égale à $1$

$$P(c \le X \le d) = \int_c^d f(x)\,\mathrm{d}x$$

**Conséquence :** $P(X = c) = 0$ pour toute valeur $c$. Donc $P(c \le X \le d) = P(c < X < d)$.

## Espérance et variance

$$E(X) = \int_I x \, f(x)\,\mathrm{d}x \qquad V(X) = \int_I (x - E(X))^2 f(x)\,\mathrm{d}x = E(X^2) - [E(X)]^2$$

$$\sigma(X) = \sqrt{V(X)}$$
""",
                            "quiz": {
                                "titre": "Quiz — Lois à densité",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "vrai_faux",
                                        "texte": "Pour une variable continue X, P(X = 3) = 0.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "La probabilité d'une valeur exacte est nulle pour une loi à densité (aire d'un segment = 0).",
                                        "points": 1,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "qcm",
                                        "texte": "L'aire totale sous une densité de probabilité vaut :",
                                        "options": ["0", "1", "π", "Cela dépend de la loi"],
                                        "reponse_correcte": "1",
                                        "explication": "Par définition, l'aire totale sous une densité vaut 1.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Loi uniforme et loi exponentielle",
                            "duree": 35,
                            "contenu": r"""# Loi uniforme

## Définition

$X$ suit la **loi uniforme** sur $[a\,;\,b]$ si sa densité est :

$$f(x) = \frac{1}{b-a} \quad \text{pour } x \in [a\,;\,b]$$

## Espérance et variance

$$E(X) = \frac{a+b}{2} \qquad V(X) = \frac{(b-a)^2}{12}$$

## Probabilité

$$P(c \le X \le d) = \frac{d - c}{b - a}$$

# Loi exponentielle

## Définition

$X$ suit la **loi exponentielle** de paramètre $\lambda > 0$ si sa densité est :

$$f(x) = \lambda e^{-\lambda x} \quad \text{pour } x \ge 0$$

## Espérance et écart type

$$E(X) = \frac{1}{\lambda} \qquad \sigma(X) = \frac{1}{\lambda}$$

## Probabilité

$$P(X \le t) = 1 - e^{-\lambda t} \qquad P(X > t) = e^{-\lambda t}$$

## Propriété « sans mémoire »

$$P_{X > s}(X > s + t) = P(X > t)$$

C'est la seule loi continue ayant cette propriété de **durée de vie sans vieillissement**.

### Exemple

Un composant électronique a une durée de vie suivant $\mathcal{E}(0{,}01)$.

$E(X) = 100$ heures. $P(X > 50) = e^{-0{,}5} \approx 0{,}607$.
""",
                            "quiz": {
                                "titre": "Quiz — Loi uniforme et loi exponentielle",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "X ~ U([2 ; 8]). Que vaut E(X) ?",
                                        "options": ["3", "5", "6", "10"],
                                        "reponse_correcte": "1",
                                        "explication": "E(X) = (2+8)/2 = 5.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Comment appelle-t-on la propriété P(X > s+t | X > s) = P(X > t) ?",
                                        "reponse_correcte": "sans mémoire",
                                        "tolerances": ["sans mémoire", "loi sans mémoire", "durée de vie sans vieillissement", "absence de mémoire"],
                                        "explication": "C'est la propriété « sans mémoire » (ou de durée de vie sans vieillissement), propre à la loi exponentielle.",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.9 : Loi normale et estimation ─────────────────
                {
                    "ordre": 9,
                    "titre": "Loi normale et estimation",
                    "description": "Lois normales, variable centrée réduite, intervalle de fluctuation, estimation.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Lois normales",
                            "duree": 35,
                            "contenu": r"""# Lois normales

## Rappels : loi binomiale

$X \sim \mathcal{B}(n, p)$ : $E(X) = np$, $\sigma(X) = \sqrt{np(1-p)}$.

## Théorème de Moivre-Laplace

Si $X_n \sim \mathcal{B}(n, p)$, alors pour $n$ grand, la variable **centrée réduite** :

$$Z_n = \frac{X_n - np}{\sqrt{np(1-p)}}$$

suit approximativement la **loi normale centrée réduite** $\mathcal{N}(0\,;\,1)$.

## Loi normale centrée réduite $\mathcal{N}(0\,;\,1)$

Sa densité est la courbe en cloche de Gauss :

$$\varphi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$$

Propriétés : $E(Z) = 0$, $\sigma(Z) = 1$, $\varphi$ est **paire** (symétrique par rapport à $x = 0$).

### Valeurs clés

$$P(-1{,}96 \le Z \le 1{,}96) \approx 0{,}95 \qquad P(-2{,}58 \le Z \le 2{,}58) \approx 0{,}99$$

## Loi normale $\mathcal{N}(\mu\,;\,\sigma^2)$

Si $Z \sim \mathcal{N}(0\,;\,1)$, alors $X = \mu + \sigma Z$ suit $\mathcal{N}(\mu\,;\,\sigma^2)$.

$E(X) = \mu$, $\sigma(X) = \sigma$.

### Règle des « 68-95-99,7 »
- $P(\mu - \sigma \le X \le \mu + \sigma) \approx 0{,}683$
- $P(\mu - 2\sigma \le X \le \mu + 2\sigma) \approx 0{,}954$
- $P(\mu - 3\sigma \le X \le \mu + 3\sigma) \approx 0{,}997$
""",
                            "quiz": {
                                "titre": "Quiz — Lois normales",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Z ~ N(0,1). Quelle est la probabilité approchée que Z ∈ [−1,96 ; 1,96] ?",
                                        "options": ["0,90", "0,95", "0,99", "0,68"],
                                        "reponse_correcte": "1",
                                        "explication": "P(−1,96 ≤ Z ≤ 1,96) ≈ 0,95 est une valeur clé à connaître.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "La courbe de Gauss est symétrique par rapport à l'axe des ordonnées.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "La densité φ(x) = (1/√(2π))·exp(−x²/2) est paire, donc symétrique par rapport à x = 0.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Intervalle de fluctuation et estimation",
                            "duree": 30,
                            "contenu": r"""# Intervalle de fluctuation et estimation

## Intervalle de fluctuation

Soit $F_n = \frac{X_n}{n}$ la fréquence observée pour $X_n \sim \mathcal{B}(n, p)$. Pour $n$ assez grand ($n \ge 30$, $np \ge 5$, $n(1-p) \ge 5$) :

$$I_n = \left[ p - 1{,}96\frac{\sqrt{p(1-p)}}{\sqrt{n}} \;;\; p + 1{,}96\frac{\sqrt{p(1-p)}}{\sqrt{n}} \right]$$

est un **intervalle de fluctuation** au seuil de $95\,\%$ : la fréquence $F_n$ appartient à $I_n$ avec une probabilité d'environ $0{,}95$.

## Prise de décision

Si la fréquence observée $f$ **n'appartient pas** à $I_n$, on rejette l'hypothèse que le paramètre vaut $p$ (au risque de $5\,\%$).

## Estimation d'une proportion

On observe une fréquence $f$ sur un échantillon de taille $n$. Un **intervalle de confiance** au niveau $95\,\%$ pour la proportion inconnue $p$ est :

$$\left[ f - \frac{1}{\sqrt{n}} \;;\; f + \frac{1}{\sqrt{n}} \right]$$

(valable pour $n \ge 30$, $nf \ge 5$, $n(1-f) \ge 5$)

### Exemple

Pour $n = 400$ et $f = 0{,}55$ :

$$IC = \left[ 0{,}55 - \frac{1}{20} \;;\; 0{,}55 + \frac{1}{20} \right] = [0{,}50 \;;\; 0{,}60]$$

On estime que $p \in [0{,}50 \;;\; 0{,}60]$ avec une confiance de $95\,\%$.
""",
                            "quiz": {
                                "titre": "Quiz — Fluctuation et estimation",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Pour n = 100 et f = 0,6, quelle est l'amplitude de l'IC au niveau 95 % (formule simplifiée) ?",
                                        "options": ["0,1", "0,2", "0,05", "0,01"],
                                        "reponse_correcte": "1",
                                        "explication": "L'IC est [f − 1/√n ; f + 1/√n] = [0,5 ; 0,7] soit une amplitude de 0,2.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Si la fréquence observée est hors de l'intervalle de fluctuation, que décide-t-on ?",
                                        "reponse_correcte": "rejeter",
                                        "tolerances": ["rejeter", "on rejette l'hypothèse", "rejet", "rejeter l'hypothèse"],
                                        "explication": "On rejette l'hypothèse au seuil fixé (souvent 5%).",
                                        "points": 2,
                                    },
                                ],
                            },
                        },
                    ],
                },
                # ── Ch.10 : Géométrie dans l'espace ──────────────────
                {
                    "ordre": 10,
                    "titre": "Géométrie dans l'espace",
                    "description": "Calcul vectoriel, orthogonalité, produit scalaire, droites et plans de l'espace.",
                    "score_minimum": 60.0,
                    "lecons": [
                        {
                            "ordre": 1,
                            "titre": "Vecteurs et produit scalaire dans l'espace",
                            "duree": 35,
                            "contenu": r"""# Vecteurs dans l'espace

## Vecteurs et bases

Dans l'espace, trois vecteurs $\vec{u}$, $\vec{v}$, $\vec{w}$ **non coplanaires** forment une base.

Tout vecteur $\vec{t}$ s'écrit de manière unique $\vec{t} = x\vec{u} + y\vec{v} + z\vec{w}$.

Un repère orthonormé de l'espace est $(O\,;\,\vec{i},\vec{j},\vec{k})$ avec $\vec{i}$, $\vec{j}$, $\vec{k}$ orthogonaux deux à deux et de norme 1.

## Coordonnées

$\overrightarrow{AB} = (x_B - x_A\,;\, y_B - y_A\,;\, z_B - z_A)$.

**Milieu :** $I = \left(\frac{x_A + x_B}{2}\,;\,\frac{y_A + y_B}{2}\,;\,\frac{z_A + z_B}{2}\right)$

**Distance :** $AB = \sqrt{(x_B-x_A)^2 + (y_B-y_A)^2 + (z_B-z_A)^2}$

## Colinéarité et coplanarité

Deux vecteurs sont **colinéaires** si $\vec{u} = k\vec{v}$.

Trois vecteurs sont **coplanaires** si l'un est combinaison linéaire des deux autres.

## Produit scalaire

$$\vec{u} \cdot \vec{v} = xx' + yy' + zz'$$

ou $\vec{u} \cdot \vec{v} = \|\vec{u}\| \times \|\vec{v}\| \times \cos(\vec{u},\vec{v})$.

**Norme :** $\|\vec{u}\| = \sqrt{\vec{u} \cdot \vec{u}} = \sqrt{x^2+y^2+z^2}$.

## Orthogonalité

$$\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0$$

**Vecteur normal** à un plan : un vecteur $\vec{n}$ orthogonal à tout vecteur directeur du plan.
""",
                            "quiz": {
                                "titre": "Quiz — Vecteurs et produit scalaire",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "u⃗ = (1,2,3) et v⃗ = (4,−1,2). Que vaut u⃗ · v⃗ ?",
                                        "options": ["8", "4", "12", "−2"],
                                        "reponse_correcte": "0",
                                        "explication": "u⃗ · v⃗ = 1×4 + 2×(−1) + 3×2 = 4 − 2 + 6 = 8.",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "vrai_faux",
                                        "texte": "Si u⃗ · v⃗ = 0, alors u⃗ et v⃗ sont orthogonaux.",
                                        "options": ["Vrai", "Faux"],
                                        "reponse_correcte": "vrai",
                                        "explication": "Par définition, le produit scalaire nul caractérise l'orthogonalité.",
                                        "points": 1,
                                    },
                                ],
                            },
                        },
                        {
                            "ordre": 2,
                            "titre": "Droites et plans de l'espace",
                            "duree": 35,
                            "contenu": r"""# Droites et plans de l'espace

## Équation cartésienne d'un plan

Un plan de vecteur normal $\vec{n}(a\,;\,b\,;\,c)$ passant par $A(x_0,y_0,z_0)$ a pour équation :

$$a(x - x_0) + b(y - y_0) + c(z - z_0) = 0$$

soit $ax + by + cz + d = 0$.

## Représentation paramétrique d'une droite

La droite passant par $A(x_0,y_0,z_0)$ de vecteur directeur $\vec{u}(a,b,c)$ :

$$\begin{cases} x = x_0 + at \\ y = y_0 + bt \\ z = z_0 + ct \end{cases} \quad (t \in \mathbb{R})$$

## Positions relatives

### Droite et plan

- **Sécants** en un point (solution unique du système)
- Droite **parallèle** au plan (pas de solution ou droite incluse)
- Droite **incluse** dans le plan

$\vec{u} \cdot \vec{n} = 0$ $\Leftrightarrow$ droite parallèle au plan (ou incluse).

### Deux plans

- **Sécants** selon une droite
- **Parallèles** (strictement ou confondus)

Deux plans sont parallèles $\iff$ leurs vecteurs normaux sont colinéaires.

## Distance d'un point à un plan

La distance du point $M_0(x_0, y_0, z_0)$ au plan $ax + by + cz + d = 0$ est :

$$d(M_0, \mathcal{P}) = \frac{|ax_0 + by_0 + cz_0 + d|}{\sqrt{a^2 + b^2 + c^2}}$$

### Exemple

Distance de $M(1,2,3)$ au plan $2x - y + 2z - 1 = 0$ :

$$d = \frac{|2(1) - 2 + 2(3) - 1|}{\sqrt{4+1+4}} = \frac{|2-2+6-1|}{3} = \frac{5}{3}$$
""",
                            "quiz": {
                                "titre": "Quiz — Droites et plans",
                                "score_minimum": 60.0,
                                "questions": [
                                    {
                                        "ordre": 1,
                                        "type": "qcm",
                                        "texte": "Quel est un vecteur normal au plan 3x − 2y + z = 5 ?",
                                        "options": ["(3, −2, 1)", "(3, 2, 1)", "(−3, 2, −1)", "(1, 1, 1)"],
                                        "reponse_correcte": "0",
                                        "explication": "Les coefficients de x, y, z donnent directement le vecteur normal : (3, −2, 1).",
                                        "points": 2,
                                    },
                                    {
                                        "ordre": 2,
                                        "type": "texte_libre",
                                        "texte": "Deux plans sont parallèles si et seulement si leurs vecteurs normaux sont…",
                                        "reponse_correcte": "colinéaires",
                                        "tolerances": ["colinéaires", "colineaires", "proportionnels", "parallèles"],
                                        "explication": "Deux plans sont parallèles ssi leurs vecteurs normaux sont colinéaires (proportionnels).",
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
}
