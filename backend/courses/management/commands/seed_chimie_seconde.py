"""
Seed Chimie Seconde — chapitres 1-9, leçons uniquement (sans quiz).
Usage : python manage.py seed_chimie_seconde
"""

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from courses.models import Matiere, Chapitre, Lecon, Quiz, Question

CHAPITRES = [
    # ──────────────────────────────────────────────
    # CHAPITRE 1 — Corps purs et mélanges
    # ──────────────────────────────────────────────
    {
        'ordre': 1,
        'titre': 'Corps purs et mélanges',
        'description': "Distinguer corps purs et mélanges, caractériser une espèce chimique par ses propriétés physiques et l'identifier par différentes méthodes.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Corps purs et mélanges',
                'duree': 30,
                'contenu': """# Corps purs et mélanges

## Introduction

La matière qui nous entoure est rarement constituée d'une seule espèce chimique. L'eau du robinet, l'air, le jus d'orange, le bronze… sont des **mélanges**. Comprendre la différence entre un **corps pur** et un **mélange** est le point de départ de toute étude en chimie.

---

## Espèce chimique

### Définition

Une **espèce chimique** est un ensemble d'entités chimiques (atomes, ions ou molécules) identiques. Chaque espèce chimique possède un nom, une formule et des propriétés physico-chimiques qui la caractérisent.

> **Exemples :** l'eau $H_2O$, le glucose $C_6H_{12}O_6$, le dioxygène $O_2$, le chlorure de sodium $NaCl$.

### Espèces naturelles et synthétiques

- Une **espèce naturelle** est produite par la nature (ex : caféine dans le café, vitamine C dans le citron).
- Une **espèce synthétique** est fabriquée par l'Homme en laboratoire ou en industrie.

> **Point clé :** une espèce synthétique peut être **identique** à l'espèce naturelle correspondante (même formule, mêmes propriétés). Le paracétamol synthétique est la même molécule que celle qui pourrait exister dans la nature.

---

## Corps pur

### Définition

Un **corps pur** est un échantillon de matière constitué d'une **seule espèce chimique**.

### Corps pur simple et composé

| Type | Définition | Exemples |
|------|-----------|----------|
| **Corps pur simple** | Constitué d'atomes d'un seul élément chimique | $O_2$ (dioxygène), $Fe$ (fer), $N_2$ (diazote) |
| **Corps pur composé** | Constitué de molécules formées de plusieurs éléments chimiques | $H_2O$ (eau), $CO_2$ (dioxyde de carbone), $NaCl$ |

> **Remarque :** l'eau distillée est un corps pur ; l'eau minérale est un mélange (elle contient des ions dissous).

---

## Mélanges

### Définition

Un **mélange** est un échantillon de matière constitué de **plusieurs espèces chimiques**.

### Mélange homogène et hétérogène

| Type | Caractéristique | Exemples |
|------|----------------|----------|
| **Mélange homogène** | On ne distingue **qu'une seule phase** : l'aspect est uniforme, même au microscope | Eau salée, air, vinaigre, sirop dilué |
| **Mélange hétérogène** | On distingue **au moins deux phases** à l'œil nu ou au microscope | Eau + huile, jus d'orange avec pulpe, sable + eau |

> **Attention :** un mélange homogène n'est **pas** un corps pur. L'eau sucrée semble pure visuellement, mais elle contient deux espèces chimiques (eau et saccharose).

---

## Composition de l'air

L'air est un **mélange homogène** de gaz :

| Gaz | Formule | Proportion volumique |
|-----|---------|---------------------|
| Diazote | $N_2$ | $\\approx 78\\%$ |
| Dioxygène | $O_2$ | $\\approx 21\\%$ |
| Argon | $Ar$ | $\\approx 0{,}93\\%$ |
| Dioxyde de carbone | $CO_2$ | $\\approx 0{,}04\\%$ |
| Autres gaz | — | traces |

---

## Techniques de séparation

Pour isoler les espèces chimiques d'un mélange, on exploite les **différences de propriétés physiques** :

### Décantation

On laisse reposer un mélange hétérogène liquide/liquide ou solide/liquide. La composante la plus dense se dépose au fond par gravité.

> **Exemple :** eau + sable → le sable se dépose au fond du récipient.

### Filtration

On fait passer un mélange hétérogène solide/liquide à travers un **filtre** (papier filtre, membrane). Le solide est retenu (résidu), le liquide passe (filtrat).

### Distillation

On chauffe un mélange homogène liquide. L'espèce chimique ayant la température d'ébullition la plus basse s'évapore en premier, puis se condense dans un réfrigérant. On recueille le **distillat**.

> **Exemple :** distillation d'eau salée → on récupère de l'eau pure (distillat) et le sel reste dans le ballon.

### Chromatographie sur couche mince (CCM)

Technique permettant de **séparer et identifier** les espèces chimiques d'un mélange. Un échantillon est déposé sur une plaque de silice (phase fixe) et entraîné par un solvant (phase mobile, l'éluant).

Chaque espèce chimique migre à une hauteur caractéristique. On définit le **rapport frontal** :

$$R_f = \\frac{h}{H}$$

- $h$ : distance parcourue par l'espèce
- $H$ : distance parcourue par le front du solvant

> **Interprétation :** deux espèces chimiques identiques ont le **même** $R_f$ dans les mêmes conditions expérimentales.

---

## À retenir

- Un **corps pur** = une seule espèce chimique ; un **mélange** = plusieurs espèces chimiques.
- Un mélange **homogène** présente un aspect uniforme (une seule phase) ; un mélange **hétérogène** présente plusieurs phases visibles.
- On sépare les mélanges par décantation, filtration, distillation ou chromatographie.
- La **CCM** permet d'identifier une espèce chimique grâce à son rapport frontal $R_f$.
""",
                'quiz': {
                    'titre': 'Quiz — Corps purs et mélanges',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Qu'est-ce qu'un corps pur ?",
                            'options': ["Un échantillon constitué d'une seule espèce chimique", "Un mélange de plusieurs espèces chimiques", "Un liquide transparent", "Un solide cristallin"],
                            'reponse_correcte': '0',
                            'explication': "Un corps pur est constitué d'une seule espèce chimique, contrairement à un mélange qui en contient plusieurs.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Parmi les exemples suivants, lequel est un mélange homogène ?",
                            'options': ["L'eau salée", "L'eau et l'huile", "Le sable et l'eau", "Le jus d'orange avec pulpe"],
                            'reponse_correcte': '0',
                            'explication': "L'eau salée est un mélange homogène car on ne distingue qu'une seule phase : le sel est entièrement dissous.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Quel est le gaz majoritaire dans l'air ?",
                            'options': ["Le diazote (environ 78 %)", "Le dioxygène (environ 21 %)", "Le dioxyde de carbone (environ 0,04 %)", "L'argon (environ 0,93 %)"],
                            'reponse_correcte': '0',
                            'explication': "Le diazote N₂ représente environ 78 % du volume de l'air, ce qui en fait le gaz majoritaire.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quelle technique de séparation utilise un papier filtre pour retenir un solide ?",
                            'options': ["La filtration", "La décantation", "La distillation", "La chromatographie"],
                            'reponse_correcte': '0',
                            'explication': "La filtration consiste à faire passer un mélange hétérogène à travers un filtre : le solide (résidu) est retenu, le liquide (filtrat) passe.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "L'eau distillée est :",
                            'options': ["Un corps pur", "Un mélange homogène", "Un mélange hétérogène", "Un corps pur simple"],
                            'reponse_correcte': '0',
                            'explication': "L'eau distillée ne contient qu'une seule espèce chimique (H₂O), c'est donc un corps pur (composé).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Le dioxygène O₂ est un corps pur :",
                            'options': ["Simple", "Composé", "Ni simple ni composé", "Mixte"],
                            'reponse_correcte': '0',
                            'explication': "O₂ est constitué d'atomes d'un seul élément chimique (l'oxygène), c'est donc un corps pur simple.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Lors d'une décantation, que se passe-t-il ?",
                            'options': ["La composante la plus dense se dépose au fond par gravité", "Le liquide s'évapore", "Le solide est retenu par un filtre", "Les espèces migrent sur une plaque de silice"],
                            'reponse_correcte': '0',
                            'explication': "La décantation exploite la gravité : la composante la plus dense se dépose au fond du récipient.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "L'air est :",
                            'options': ["Un mélange homogène de gaz", "Un corps pur composé", "Un mélange hétérogène", "Un corps pur simple"],
                            'reponse_correcte': '0',
                            'explication': "L'air est un mélange homogène contenant principalement du diazote, du dioxygène et d'autres gaz en faible proportion.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Quel est le rôle de l'éluant en chromatographie sur couche mince (CCM) ?",
                            'options': ["C'est la phase mobile qui entraîne les espèces chimiques", "C'est la phase fixe sur laquelle on dépose l'échantillon", "C'est le révélateur utilisé pour colorer les taches", "C'est le solvant dans lequel on dissout l'échantillon avant dépôt"],
                            'reponse_correcte': '0',
                            'explication': "L'éluant est la phase mobile en CCM : il monte par capillarité sur la plaque et entraîne les espèces chimiques à des hauteurs différentes.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quelle technique permet de séparer les composants d'un mélange homogène liquide en exploitant leurs températures d'ébullition différentes ?",
                            'options': ["La distillation", "La filtration", "La décantation", "La chromatographie"],
                            'reponse_correcte': '0',
                            'explication': "La distillation permet de séparer les composants d'un mélange homogène : l'espèce ayant la température d'ébullition la plus basse s'évapore en premier.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "En CCM, deux espèces chimiques identiques, dans les mêmes conditions expérimentales, auront :",
                            'options': ["Le même rapport frontal Rf", "Des rapports frontaux Rf différents", "La même couleur", "La même masse"],
                            'reponse_correcte': '0',
                            'explication': "Le rapport frontal Rf est caractéristique d'une espèce dans des conditions données. Deux espèces identiques ont le même Rf.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "L'eau minérale est :",
                            'options': ["Un mélange homogène", "Un corps pur", "Un mélange hétérogène", "Un corps pur simple"],
                            'reponse_correcte': '0',
                            'explication': "L'eau minérale contient de l'eau et des ions dissous (calcium, magnésium, etc.), c'est donc un mélange homogène.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Lors de la distillation d'eau salée, que récupère-t-on dans le distillat ?",
                            'options': ["De l'eau pure", "Du sel", "De l'eau salée diluée", "Un mélange de sel et d'eau"],
                            'reponse_correcte': '0',
                            'explication': "L'eau s'évapore en premier (Teb = 100 °C), se condense dans le réfrigérant et est recueillie sous forme d'eau pure (distillat). Le sel reste dans le ballon.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Quel est le pourcentage volumique approximatif du dioxygène dans l'air ?",
                            'options': ["21 %", "78 %", "1 %", "0,04 %"],
                            'reponse_correcte': '0',
                            'explication': "Le dioxygène O₂ représente environ 21 % du volume de l'air.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "L'eau sucrée est un corps pur car elle est transparente.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "L'eau sucrée est un mélange homogène (eau + saccharose). L'aspect transparent ne signifie pas qu'il s'agit d'un corps pur.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Le bronze est un mélange.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Le bronze est un alliage (mélange homogène) de cuivre et d'étain.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Une espèce chimique synthétique a toujours des propriétés différentes de l'espèce naturelle correspondante.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Une espèce synthétique peut être identique à l'espèce naturelle (même formule, mêmes propriétés). Exemple : le paracétamol synthétique est la même molécule.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on la technique de séparation qui exploite la différence de migration des espèces sur une plaque de silice ?",
                            'options': None,
                            'reponse_correcte': 'chromatographie',
                            'tolerances': ['chromatographie sur couche mince', 'CCM', 'ccm', 'chromatographie sur couche mince (CCM)'],
                            'explication': "La chromatographie sur couche mince (CCM) sépare les espèces chimiques en exploitant leur migration différente sur une plaque de silice (phase fixe) entraînées par un éluant (phase mobile).",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "En CCM, une espèce chimique a migré de 3,2 cm et le front du solvant de 4,0 cm. Calculer le rapport frontal Rf (donner la valeur numérique).",
                            'options': None,
                            'reponse_correcte': '0.8',
                            'tolerances': ['0,8', '0.80', '0,80'],
                            'explication': "Rf = h / H = 3,2 / 4,0 = 0,8. Le rapport frontal est sans unité.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quel est le nom du liquide recueilli après une distillation ?",
                            'options': None,
                            'reponse_correcte': 'distillat',
                            'tolerances': ['le distillat'],
                            'explication': "Le liquide recueilli après condensation des vapeurs lors d'une distillation s'appelle le distillat.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': "Propriétés physiques et identification d'une espèce chimique",
                'duree': 35,
                'contenu': """# Propriétés physiques et identification d'une espèce chimique

## Introduction

Chaque espèce chimique possède des **propriétés physiques caractéristiques** qui permettent de l'identifier. Ces propriétés sont mesurables et ne dépendent pas de la quantité d'échantillon considéré.

---

## Température de changement d'état

### Température de fusion $T_f$

La **température de fusion** est la température à laquelle une espèce chimique passe de l'état solide à l'état liquide, sous une pression donnée (généralement la pression atmosphérique standard, $P = 1{,}013 \\times 10^5$ Pa).

### Température d'ébullition $T_{eb}$

La **température d'ébullition** est la température à laquelle une espèce passe de l'état liquide à l'état gazeux, sous une pression donnée.

### Exemples

| Espèce chimique | Formule | $T_f$ (°C) | $T_{eb}$ (°C) |
|----------------|---------|------------|---------------|
| Eau | $H_2O$ | 0 | 100 |
| Éthanol | $C_2H_6O$ | −114 | 78 |
| Acide acétique | $CH_3COOH$ | 17 | 118 |
| Fer | $Fe$ | 1 538 | 2 861 |

> **Critère d'identification :** lors du changement d'état d'un **corps pur**, la température reste **constante** (on observe un **palier** sur la courbe de chauffage). Pour un mélange, la température varie pendant le changement d'état.

---

## Masse volumique

### Définition

La **masse volumique** $\\rho$ (lettre grecque « rhô ») d'un échantillon est le rapport de sa masse sur son volume :

$$\\rho = \\frac{m}{V}$$

| Grandeur | Symbole | Unité SI | Autres unités courantes |
|----------|---------|----------|------------------------|
| Masse volumique | $\\rho$ | $\\text{kg/m}^3$ | $\\text{g/cm}^3$ ou $\\text{g/mL}$ |
| Masse | $m$ | $\\text{kg}$ | $\\text{g}$ |
| Volume | $V$ | $\\text{m}^3$ | $\\text{cm}^3$ ou $\\text{mL}$ |

### Conversion

$$1 \\text{ g/cm}^3 = 1 \\text{ g/mL} = 1000 \\text{ kg/m}^3$$

### Exemples

| Espèce chimique | $\\rho$ (g/cm³) |
|----------------|----------------|
| Eau (à 25 °C) | 1,00 |
| Éthanol | 0,79 |
| Fer | 7,87 |
| Aluminium | 2,70 |
| Mercure | 13,55 |

> **Application :** un objet coule dans un liquide si sa masse volumique est **supérieure** à celle du liquide.

---

## Densité

La **densité** $d$ d'un solide ou d'un liquide est le rapport de sa masse volumique à celle de l'eau :

$$d = \\frac{\\rho_{\\text{espèce}}}{\\rho_{\\text{eau}}}$$

Comme $\\rho_{\\text{eau}} = 1{,}00$ g/cm³ à 25 °C, la densité est **numériquement égale** à la masse volumique exprimée en g/cm³. C'est un nombre **sans unité**.

> **Exemple :** l'éthanol a $\\rho = 0{,}79$ g/cm³, donc $d = 0{,}79$. Il est moins dense que l'eau et flotte à sa surface.

---

## Indice de réfraction

L'**indice de réfraction** $n$ d'un milieu transparent caractérise la façon dont la lumière se propage dans ce milieu. Il est mesuré à l'aide d'un **réfractomètre**.

$$n = \\frac{c}{v}$$

- $c = 3{,}00 \\times 10^8$ m/s : vitesse de la lumière dans le vide
- $v$ : vitesse de la lumière dans le milieu

| Milieu | $n$ |
|--------|-----|
| Vide / Air | $\\approx 1{,}00$ |
| Eau | 1,33 |
| Éthanol | 1,36 |
| Verre | 1,50 – 1,90 |
| Diamant | 2,42 |

> L'indice de réfraction est toujours **supérieur ou égal à 1** et n'a **pas d'unité**.

---

## Identification d'une espèce chimique

Pour **identifier** une espèce chimique dans un échantillon, on compare ses propriétés physiques mesurées aux valeurs connues (tables de données). On peut combiner plusieurs méthodes :

### 1. Mesure d'une température de changement d'état

Si on observe un palier de température à $T_f = 0$ °C lors de la solidification d'un liquide pur, on peut affirmer qu'il s'agit probablement d'eau.

### 2. Mesure de la masse volumique

On mesure $m$ et $V$ de l'échantillon, on calcule $\\rho = m/V$, puis on compare aux tables.

### 3. Chromatographie sur couche mince (CCM)

On compare le $R_f$ de l'espèce inconnue avec celui d'espèces de référence.

### 4. Tests chimiques caractéristiques

| Test | Réactif | Résultat positif | Ion ou espèce détecté(e) |
|------|---------|-------------------|--------------------------|
| Test de l'eau | Sulfate de cuivre anhydre (blanc) | Devient **bleu** | Eau ($H_2O$) |
| Test du $CO_2$ | Eau de chaux | Devient **trouble** (précipité blanc) | Dioxyde de carbone ($CO_2$) |
| Test du $H_2$ | Flamme (bûchette) | **Détonation** (« pop ») | Dihydrogène ($H_2$) |
| Test du $O_2$ | Bûchette incandescente | Se **rallume** vivement | Dioxygène ($O_2$) |
| Test des ions chlorure | Nitrate d'argent $AgNO_3$ | Précipité **blanc** qui noircit à la lumière | $Cl^-$ |

---

## Démarche d'identification — exemple

On dispose d'un liquide incolore inconnu. On effectue les mesures suivantes :

| Propriété mesurée | Valeur obtenue |
|-------------------|----------------|
| $T_{eb}$ | 78 °C |
| $\\rho$ | 0,79 g/cm³ |
| $n$ | 1,36 |

En comparant aux tables de données :

| Propriété | Eau | Éthanol | Acétone |
|-----------|-----|---------|---------|
| $T_{eb}$ (°C) | 100 | 78 | 56 |
| $\\rho$ (g/cm³) | 1,00 | 0,79 | 0,78 |
| $n$ | 1,33 | 1,36 | 1,36 |

> **Conclusion :** les trois propriétés mesurées correspondent à l'**éthanol**. L'espèce chimique est identifiée.

---

## À retenir

- Les propriétés physiques caractéristiques d'une espèce : $T_f$, $T_{eb}$, $\\rho$, $n$, $R_f$.
- La **masse volumique** se calcule par $\\rho = \\frac{m}{V}$.
- La température est **constante** lors du changement d'état d'un **corps pur** (palier).
- Pour identifier une espèce, on **compare** ses propriétés mesurées aux valeurs tabulées.
- Les tests chimiques (eau de chaux, sulfate de cuivre, etc.) complètent les mesures physiques.
""",
                'quiz': {
                    'titre': "Quiz — Propriétés physiques et identification d'une espèce chimique",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quelle grandeur relie la masse d'un échantillon à son volume ?",
                            'options': ["La masse volumique", "La densité", "L'indice de réfraction", "La température d'ébullition"],
                            'reponse_correcte': '0',
                            'explication': "La masse volumique ρ est définie par ρ = m/V. Elle relie directement la masse au volume.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quelle est l'unité SI de la masse volumique ?",
                            'options': ["kg/m³", "g/cm³", "g/L", "mol/L"],
                            'reponse_correcte': '0',
                            'explication': "L'unité SI de la masse volumique est le kilogramme par mètre cube (kg/m³). Le g/cm³ est une unité courante mais pas l'unité SI.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Lors du changement d'état d'un corps pur, la température :",
                            'options': ["Reste constante (palier)", "Augmente progressivement", "Diminue progressivement", "Oscille autour d'une valeur moyenne"],
                            'reponse_correcte': '0',
                            'explication': "Lors du changement d'état d'un corps pur, on observe un palier de température : la température reste constante pendant toute la durée du changement d'état.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quel réactif utilise-t-on pour détecter la présence d'eau ?",
                            'options': ["Le sulfate de cuivre anhydre", "L'eau de chaux", "Le nitrate d'argent", "Une bûchette enflammée"],
                            'reponse_correcte': '0',
                            'explication': "Le sulfate de cuivre anhydre est blanc ; il devient bleu en présence d'eau. C'est le test caractéristique de l'eau.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Comment détecte-t-on le dioxyde de carbone CO₂ ?",
                            'options': ["Avec l'eau de chaux qui se trouble", "Avec une bûchette incandescente", "Avec du sulfate de cuivre anhydre", "Avec du nitrate d'argent"],
                            'reponse_correcte': '0',
                            'explication': "L'eau de chaux se trouble (précipité blanc de carbonate de calcium) en présence de CO₂.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "La densité d'un solide ou d'un liquide est :",
                            'options': ["Un nombre sans unité", "Exprimée en g/cm³", "Exprimée en kg/m³", "Exprimée en mol/L"],
                            'reponse_correcte': '0',
                            'explication': "La densité est le rapport de la masse volumique de l'espèce à celle de l'eau. C'est un nombre sans dimension (sans unité).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "La température d'ébullition de l'eau pure sous pression atmosphérique normale est :",
                            'options': ["100 °C", "0 °C", "78 °C", "118 °C"],
                            'reponse_correcte': '0',
                            'explication': "L'eau pure bout à 100 °C sous 1 atm (pression atmosphérique standard).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Quel appareil permet de mesurer l'indice de réfraction d'un liquide ?",
                            'options': ["Un réfractomètre", "Un densimètre", "Un thermomètre", "Un chronomètre"],
                            'reponse_correcte': '0',
                            'explication': "L'indice de réfraction se mesure à l'aide d'un réfractomètre.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Un liquide inconnu a une masse volumique de 0,79 g/cm³ et une température d'ébullition de 78 °C. Il s'agit probablement de :",
                            'options': ["L'éthanol", "L'eau", "L'acétone", "Le mercure"],
                            'reponse_correcte': '0',
                            'explication': "ρ = 0,79 g/cm³ et Teb = 78 °C correspondent aux valeurs tabulées de l'éthanol.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Lors du changement d'état d'un mélange, la température :",
                            'options': ["Varie pendant le changement d'état", "Reste constante (palier)", "Chute brutalement", "Double de valeur"],
                            'reponse_correcte': '0',
                            'explication': "Contrairement à un corps pur, un mélange ne présente pas de palier de température lors d'un changement d'état : la température continue de varier.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "La formule de la densité d'un liquide par rapport à l'eau est :",
                            'options': ["d = ρ_espèce / ρ_eau", "d = m / V", "d = ρ_eau / ρ_espèce", "d = V / m"],
                            'reponse_correcte': '0',
                            'explication': "La densité est le rapport de la masse volumique de l'espèce à celle de l'eau : d = ρ_espèce / ρ_eau.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "L'indice de réfraction est toujours :",
                            'options': ["Supérieur ou égal à 1", "Compris entre 0 et 1", "Négatif pour les gaz", "Égal à la masse volumique"],
                            'reponse_correcte': '0',
                            'explication': "L'indice de réfraction n = c/v est toujours ≥ 1 car la lumière se propage toujours moins vite dans un milieu que dans le vide.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Le test au nitrate d'argent AgNO₃ produit un précipité blanc qui noircit à la lumière. Ce test met en évidence la présence de :",
                            'options': ["Ions chlorure Cl⁻", "Dioxyde de carbone CO₂", "Eau H₂O", "Dioxygène O₂"],
                            'reponse_correcte': '0',
                            'explication': "Le nitrate d'argent forme avec les ions chlorure un précipité de chlorure d'argent AgCl, blanc, qui noircit à la lumière.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Quelle propriété physique n'est PAS caractéristique d'une espèce chimique ?",
                            'options': ["Sa couleur", "Sa température de fusion", "Sa masse volumique", "Son indice de réfraction"],
                            'reponse_correcte': '0',
                            'explication': "La couleur n'est pas une propriété caractéristique suffisante pour identifier une espèce chimique. De nombreuses espèces incolores sont différentes. Les grandeurs Tf, ρ et n sont caractéristiques.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "La masse volumique de l'eau est de 1,00 g/cm³ à 25 °C.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "La masse volumique de l'eau est en effet d'environ 1,00 g/cm³ à 25 °C (et à 4 °C elle est très légèrement supérieure).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Une bûchette incandescente qui se rallume vivement permet de détecter le dihydrogène H₂.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Une bûchette incandescente qui se rallume vivement est le test du dioxygène O₂. Le test du dihydrogène H₂ produit une détonation (\"pop\") à l'approche d'une flamme.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Pour identifier une espèce chimique, il suffit de mesurer une seule propriété physique.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Une seule propriété peut correspondre à plusieurs espèces. Il faut combiner plusieurs mesures (Teb, ρ, n, Rf…) pour confirmer l'identification.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Un échantillon a une masse de 135 g et un volume de 50 cm³. Calculer sa masse volumique en g/cm³ (donner la valeur numérique).",
                            'options': None,
                            'reponse_correcte': '2.7',
                            'tolerances': ['2,7', '2.70', '2,70'],
                            'explication': "ρ = m / V = 135 / 50 = 2,7 g/cm³. Cette valeur correspond à l'aluminium.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Quelle est la température de fusion de l'eau pure sous pression atmosphérique normale (en °C) ?",
                            'options': None,
                            'reponse_correcte': '0',
                            'tolerances': ['0°C', '0 °C', '0°', '0 degrés'],
                            'explication': "La température de fusion de l'eau pure est de 0 °C sous 1 atm.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quel est le nom de l'instrument de mesure utilisé pour déterminer l'indice de réfraction ?",
                            'options': None,
                            'reponse_correcte': 'réfractomètre',
                            'tolerances': ['refractometre', 'un réfractomètre', 'le réfractomètre'],
                            'explication': "L'indice de réfraction se mesure avec un réfractomètre.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 2 — La structure de l'atome
    # ──────────────────────────────────────────────
    {
        'ordre': 2,
        'titre': "La structure de l'atome",
        'description': "Comprendre la constitution d'un atome, sa notation symbolique, les isotopes, et la structure électronique en couches.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Le noyau atomique — composition et notation',
                'duree': 35,
                'contenu': """# Le noyau atomique — composition et notation

## Introduction — l'atome, brique élémentaire de la matière

Toute la matière est constituée d'**atomes**. Un atome est une entité extrêmement petite (rayon de l'ordre de $10^{-10}$ m, soit $0{,}1$ nm) composée de deux parties :

1. Un **noyau** central, très compact et chargé positivement.
2. Un **cortège électronique** constitué d'électrons en mouvement autour du noyau.

> **Ordre de grandeur :** le rayon du noyau est environ $10^{-15}$ m, soit **100 000 fois** plus petit que celui de l'atome. L'atome est essentiellement constitué de **vide**.

---

## Constitution du noyau

Le noyau contient deux types de particules appelées **nucléons** :

| Particule | Symbole | Charge | Masse |
|-----------|---------|--------|-------|
| **Proton** | $p$ | $+e = +1{,}6 \\times 10^{-19}$ C | $m_p \\approx 1{,}673 \\times 10^{-27}$ kg |
| **Neutron** | $n$ | $0$ (neutre) | $m_n \\approx 1{,}675 \\times 10^{-27}$ kg |

> **Remarque :** le proton et le neutron ont quasiment la **même masse** ($m_p \\approx m_n$). La masse du noyau est donc environ $A \\times m_p$, où $A$ est le nombre total de nucléons.

---

## L'électron

L'**électron** est une particule de charge négative $-e$ qui se déplace autour du noyau :

| Propriété | Valeur |
|-----------|--------|
| Charge | $-e = -1{,}6 \\times 10^{-19}$ C |
| Masse | $m_e \\approx 9{,}109 \\times 10^{-31}$ kg |

Le rapport des masses est considérable :

$$\\frac{m_p}{m_e} \\approx 1836$$

> **Conséquence :** la masse de l'atome est **concentrée dans le noyau**. Les électrons contribuent de manière négligeable à la masse totale.

---

## Notation symbolique du noyau

Un noyau (ou un atome) est représenté par la notation :

$$^A_Z X$$

| Symbole | Nom | Signification |
|---------|-----|---------------|
| $X$ | Symbole chimique | Identifie l'élément (H, C, O, Fe…) |
| $Z$ | Numéro atomique | Nombre de **protons** dans le noyau |
| $A$ | Nombre de masse | Nombre total de **nucléons** (protons + neutrons) |

Le nombre de **neutrons** se déduit :

$$N = A - Z$$

### Exemples

| Atome | Notation | $Z$ | $A$ | Protons | Neutrons | Électrons |
|-------|----------|-----|-----|---------|----------|-----------|
| Hydrogène | $^1_1 H$ | 1 | 1 | 1 | 0 | 1 |
| Carbone | $^{12}_{\\phantom{0}6} C$ | 6 | 12 | 6 | 6 | 6 |
| Oxygène | $^{16}_{\\phantom{0}8} O$ | 8 | 16 | 8 | 8 | 8 |
| Fer | $^{56}_{26} Fe$ | 26 | 56 | 26 | 30 | 26 |
| Uranium | $^{238}_{\\phantom{0}92} U$ | 92 | 238 | 92 | 146 | 92 |

---

## Neutralité électrique de l'atome

Un atome est **électriquement neutre** : la charge totale positive du noyau compense exactement la charge totale négative des électrons.

$$\\text{Nombre de protons} = \\text{Nombre d'électrons} = Z$$

> Un atome de carbone ($Z = 6$) possède 6 protons et 6 électrons.

---

## Les isotopes

### Définition

Des **isotopes** sont des atomes qui ont le **même numéro atomique** $Z$ (même élément chimique) mais des **nombres de masse** $A$ différents (nombre de neutrons différent).

### Exemples — isotopes de l'hydrogène

| Isotope | Notation | Protons | Neutrons | Nom usuel |
|---------|----------|---------|----------|-----------|
| Hydrogène | $^1_1 H$ | 1 | 0 | Protium (hydrogène « léger ») |
| Deutérium | $^2_1 H$ | 1 | 1 | Deutérium |
| Tritium | $^3_1 H$ | 1 | 2 | Tritium (radioactif) |

### Exemples — isotopes du carbone

| Isotope | Protons | Neutrons | Remarque |
|---------|---------|----------|----------|
| $^{12}C$ | 6 | 6 | Le plus abondant (98,9 %) |
| $^{13}C$ | 6 | 7 | Stable, abondance 1,1 % |
| $^{14}C$ | 6 | 8 | Radioactif, utilisé pour la datation |

> **Point essentiel :** les isotopes d'un même élément ont les **mêmes propriétés chimiques** car ils possèdent le même nombre d'électrons. Leurs propriétés physiques (masse, stabilité nucléaire) diffèrent.

---

## Masse de l'atome

La masse de l'atome est pratiquement égale à la masse du noyau :

$$m_{\\text{atome}} \\approx m_{\\text{noyau}} = A \\times m_p$$

car $m_p \\approx m_n$ et la masse des électrons est négligeable.

### Application numérique

Masse d'un atome de carbone 12 :

$$m_{^{12}C} \\approx 12 \\times 1{,}673 \\times 10^{-27} = 2{,}008 \\times 10^{-26} \\text{ kg}$$

---

## À retenir

- L'atome est constitué d'un **noyau** (protons + neutrons) et d'un **cortège d'électrons**.
- La notation $^A_Z X$ donne le numéro atomique $Z$, le nombre de masse $A$, et le nombre de neutrons $N = A - Z$.
- L'atome est **électriquement neutre** : nombre de protons = nombre d'électrons = $Z$.
- Des **isotopes** ont le même $Z$ mais des $A$ différents.
- La masse de l'atome est essentiellement celle de son noyau : $m \\approx A \\times m_p$.
""",
                'quiz': {
                    'titre': 'Quiz — Le noyau atomique — composition et notation',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quelles sont les deux particules constituant le noyau d'un atome ?",
                            'options': ["Protons et neutrons", "Protons et électrons", "Neutrons et électrons", "Photons et neutrons"],
                            'reponse_correcte': '0',
                            'explication': "Le noyau est constitué de nucléons : les protons (chargés positivement) et les neutrons (neutres).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quelle est la charge électrique d'un proton ?",
                            'options': ["+e = +1,6 × 10⁻¹⁹ C", "-e = -1,6 × 10⁻¹⁹ C", "0 (neutre)", "+2e"],
                            'reponse_correcte': '0',
                            'explication': "Le proton porte une charge positive élémentaire +e = +1,6 × 10⁻¹⁹ C.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Dans la notation ᴬ_Z X, que représente Z ?",
                            'options': ["Le numéro atomique (nombre de protons)", "Le nombre de masse (protons + neutrons)", "Le nombre de neutrons", "Le nombre d'électrons de valence"],
                            'reponse_correcte': '0',
                            'explication': "Z est le numéro atomique : il indique le nombre de protons dans le noyau.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Comment calcule-t-on le nombre de neutrons N d'un atome ?",
                            'options': ["N = A − Z", "N = A + Z", "N = Z − A", "N = A × Z"],
                            'reponse_correcte': '0',
                            'explication': "Le nombre de neutrons est la différence entre le nombre de masse A (total de nucléons) et le numéro atomique Z (protons) : N = A − Z.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La masse de l'atome est essentiellement concentrée dans :",
                            'options': ["Le noyau", "Le cortège électronique", "Les électrons de valence", "L'espace vide entre noyau et électrons"],
                            'reponse_correcte': '0',
                            'explication': "Le noyau contient protons et neutrons dont la masse est environ 1836 fois celle d'un électron. La masse de l'atome est donc concentrée dans le noyau.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Un atome neutre possède Z = 8. Combien a-t-il d'électrons ?",
                            'options': ["8", "16", "6", "10"],
                            'reponse_correcte': '0',
                            'explication': "Un atome neutre possède autant d'électrons que de protons. Avec Z = 8, il a 8 protons et donc 8 électrons.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Le rapport entre la masse du proton et celle de l'électron est environ :",
                            'options': ["1836", "100", "10", "18"],
                            'reponse_correcte': '0',
                            'explication': "mp/me ≈ 1836. Le proton est environ 1836 fois plus lourd que l'électron.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Le rayon du noyau est environ combien de fois plus petit que celui de l'atome ?",
                            'options': ["100 000 fois", "10 fois", "1 000 fois", "1 million de fois"],
                            'reponse_correcte': '0',
                            'explication': "Le rayon de l'atome est de l'ordre de 10⁻¹⁰ m et celui du noyau de 10⁻¹⁵ m, soit un facteur 100 000.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Des isotopes sont des atomes qui ont :",
                            'options': ["Le même Z mais des A différents", "Le même A mais des Z différents", "Le même nombre de neutrons", "Le même nombre d'électrons de valence"],
                            'reponse_correcte': '0',
                            'explication': "Des isotopes ont le même numéro atomique Z (même élément) mais des nombres de masse A différents (nombre de neutrons différent).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "L'atome de fer est noté ⁵⁶₂₆Fe. Combien de neutrons contient-il ?",
                            'options': ["30", "26", "56", "82"],
                            'reponse_correcte': '0',
                            'explication': "N = A − Z = 56 − 26 = 30 neutrons.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Le carbone 14 (¹⁴C, Z = 6) est utilisé en :",
                            'options': ["Datation archéologique", "Production d'énergie nucléaire", "Fabrication de médicaments", "Purification de l'eau"],
                            'reponse_correcte': '0',
                            'explication': "Le carbone 14 est un isotope radioactif utilisé pour la datation d'échantillons archéologiques (datation au carbone 14).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Quelle est la masse approximative d'un atome de carbone 12 ?",
                            'options': ["2,0 × 10⁻²⁶ kg", "1,67 × 10⁻²⁷ kg", "12 g", "9,1 × 10⁻³¹ kg"],
                            'reponse_correcte': '0',
                            'explication': "m ≈ A × mp = 12 × 1,673 × 10⁻²⁷ ≈ 2,0 × 10⁻²⁶ kg.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Parmi ces isotopes de l'hydrogène, lequel est radioactif ?",
                            'options': ["Le tritium ³H", "Le protium ¹H", "Le deutérium ²H", "Aucun des trois"],
                            'reponse_correcte': '0',
                            'explication': "Le tritium (³H, 1 proton + 2 neutrons) est radioactif. Le protium et le deutérium sont stables.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Les isotopes d'un même élément possèdent :",
                            'options': ["Les mêmes propriétés chimiques", "Les mêmes propriétés physiques", "Un nombre d'électrons différent", "Un numéro atomique Z différent"],
                            'reponse_correcte': '0',
                            'explication': "Les isotopes ont le même Z donc le même nombre d'électrons, ce qui leur confère les mêmes propriétés chimiques. Leurs masses diffèrent, donc leurs propriétés physiques aussi.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Le neutron porte une charge électrique positive.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le neutron est électriquement neutre (charge nulle). C'est le proton qui porte la charge positive.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "L'atome est essentiellement constitué de vide.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Le rayon du noyau est 100 000 fois plus petit que celui de l'atome. L'espace entre le noyau et les électrons est essentiellement vide.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Deux isotopes d'un même élément ont le même nombre de neutrons.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Des isotopes ont le même Z (protons) mais des A différents, donc des nombres de neutrons (N = A − Z) différents.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Un atome est noté ²³Na (Z = 11). Combien de neutrons possède-t-il ? (donner le nombre)",
                            'options': None,
                            'reponse_correcte': '12',
                            'tolerances': ['douze'],
                            'explication': "N = A − Z = 23 − 11 = 12 neutrons.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on les particules du noyau (protons et neutrons) d'un nom générique ?",
                            'options': None,
                            'reponse_correcte': 'nucléons',
                            'tolerances': ['nucleons', 'les nucléons', 'des nucléons'],
                            'explication': "Les particules du noyau (protons et neutrons) sont appelées nucléons.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quelle est la masse approximative d'un proton en kg ? (donner l'ordre de grandeur sous la forme a × 10⁻²⁷)",
                            'options': None,
                            'reponse_correcte': '1.67e-27',
                            'tolerances': ['1,67 × 10⁻²⁷', '1.67 × 10⁻²⁷', '1,67e-27', '1,673 × 10⁻²⁷', '1.673e-27', '1.673 × 10⁻²⁷'],
                            'explication': "La masse d'un proton est mp ≈ 1,673 × 10⁻²⁷ kg.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Structure électronique de l\'atome',
                'duree': 35,
                'contenu': """# Structure électronique de l'atome

## Introduction

Les propriétés chimiques d'un atome dépendent principalement de la **répartition de ses électrons** autour du noyau. Cette répartition suit des règles précises qui déterminent le comportement de l'atome dans les réactions chimiques.

---

## Les couches électroniques

Les électrons se répartissent autour du noyau sur des **couches électroniques** (ou niveaux d'énergie). En classe de Seconde, on considère les trois premières couches :

| Couche | Numéro $n$ | Nombre maximal d'électrons |
|--------|------------|---------------------------|
| K | $n = 1$ | $2$ |
| L | $n = 2$ | $8$ |
| M | $n = 3$ | $18$ |

> **Règle générale :** la couche de numéro $n$ peut contenir au maximum $2n^2$ électrons.

| Couche | $n$ | Capacité maximale $2n^2$ |
|--------|-----|--------------------------|
| K | 1 | $2 \\times 1^2 = 2$ |
| L | 2 | $2 \\times 2^2 = 8$ |
| M | 3 | $2 \\times 3^2 = 18$ |

---

## Règles de remplissage

### Principe de remplissage (règle de Klechkowski simplifiée)

Les électrons remplissent les couches **dans l'ordre croissant d'énergie** : d'abord K, puis L, puis M.

> On ne commence à remplir la couche suivante que lorsque la précédente est **saturée** (pleine).

### Méthode pas à pas

Pour écrire la structure électronique d'un atome de numéro atomique $Z$ :

1. Compter le nombre d'électrons : c'est $Z$ (atome neutre).
2. Remplir la couche K avec 2 électrons maximum.
3. Remplir la couche L avec 8 électrons maximum.
4. Placer le reste sur la couche M.

---

## Exemples de structures électroniques

| Atome | $Z$ | Électrons | Structure électronique | Couche externe |
|-------|-----|-----------|----------------------|----------------|
| Hydrogène $H$ | 1 | 1 | (K)$^1$ | K |
| Hélium $He$ | 2 | 2 | (K)$^2$ | K |
| Lithium $Li$ | 3 | 3 | (K)$^2$ (L)$^1$ | L |
| Carbone $C$ | 6 | 6 | (K)$^2$ (L)$^4$ | L |
| Azote $N$ | 7 | 7 | (K)$^2$ (L)$^5$ | L |
| Oxygène $O$ | 8 | 8 | (K)$^2$ (L)$^6$ | L |
| Néon $Ne$ | 10 | 10 | (K)$^2$ (L)$^8$ | L |
| Sodium $Na$ | 11 | 11 | (K)$^2$ (L)$^8$ (M)$^1$ | M |
| Aluminium $Al$ | 13 | 13 | (K)$^2$ (L)$^8$ (M)$^3$ | M |
| Chlore $Cl$ | 17 | 17 | (K)$^2$ (L)$^8$ (M)$^7$ | M |
| Argon $Ar$ | 18 | 18 | (K)$^2$ (L)$^8$ (M)$^8$ | M |

> **Cas particulier de l'argon :** bien que la couche M puisse contenir jusqu'à 18 électrons, en Seconde on admet que les atomes étudiés ont au maximum **8 électrons** sur la couche M (les éléments jusqu'à $Z = 18$).

---

## Couche externe et électrons de valence

### Couche externe

La **couche externe** (ou couche de valence) est la **dernière couche occupée**, la plus éloignée du noyau. C'est celle qui contient le ou les derniers électrons placés.

### Électrons de valence

Les **électrons de valence** sont les électrons situés sur la couche externe. Ce sont eux qui interviennent dans les liaisons chimiques et les réactions.

> **Exemple :** le carbone $C$ ($Z = 6$) a pour structure (K)$^2$ (L)$^4$. Sa couche externe est L et il possède **4 électrons de valence**.

### Électrons de cœur

Les **électrons de cœur** sont ceux des couches internes (couches complètement remplies situées sous la couche externe). Ils ne participent pas aux liaisons chimiques.

> **Exemple :** pour le sodium ($Z = 11$), structure (K)$^2$ (L)$^8$ (M)$^1$, les 10 électrons des couches K et L sont des électrons de cœur ; le seul électron de la couche M est l'électron de valence.

---

## Importance de la couche externe

La couche externe détermine :

1. **Le nombre d'électrons de valence** → combien de liaisons l'atome peut former.
2. **La famille chimique** → les atomes ayant le même nombre d'électrons de valence ont des propriétés chimiques similaires (on le verra en détail au chapitre suivant).
3. **La stabilité** → un atome est particulièrement stable quand sa couche externe est **saturée** (2 électrons pour la couche K, 8 pour les couches L et M) : c'est la configuration des **gaz nobles**.

### Configuration des gaz nobles

| Gaz noble | $Z$ | Structure | Couche externe |
|-----------|-----|-----------|----------------|
| Hélium $He$ | 2 | (K)$^2$ | K saturée (2 é) |
| Néon $Ne$ | 10 | (K)$^2$ (L)$^8$ | L saturée (8 é) |
| Argon $Ar$ | 18 | (K)$^2$ (L)$^8$ (M)$^8$ | M à 8 é |

> Les gaz nobles sont chimiquement **inertes** (quasi aucune réactivité) car leur couche externe est déjà complète.

---

## Exercice type

**Énoncé :** Déterminer la structure électronique du phosphore $P$ ($Z = 15$).

**Résolution :**

1. L'atome possède $Z = 15$ électrons.
2. Remplissage :
   - Couche K : 2 électrons → il reste $15 - 2 = 13$ électrons.
   - Couche L : 8 électrons → il reste $13 - 8 = 5$ électrons.
   - Couche M : 5 électrons.
3. Structure électronique : **(K)$^2$ (L)$^8$ (M)$^5$**
4. Couche externe : M, avec **5 électrons de valence**.

---

## À retenir

- Les électrons se répartissent sur les couches K, L, M… en remplissant d'abord les couches les plus proches du noyau.
- La couche $n$ contient au maximum $2n^2$ électrons (K : 2, L : 8, M : 18).
- Les **électrons de valence** sont ceux de la **couche externe** : ils déterminent les propriétés chimiques.
- Les **gaz nobles** ont une couche externe saturée, ce qui les rend chimiquement stables.
""",
                'quiz': {
                    'titre': "Quiz — Structure électronique de l'atome",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Combien d'électrons peut contenir au maximum la couche K ?",
                            'options': ["2", "8", "18", "1"],
                            'reponse_correcte': '0',
                            'explication': "La couche K (n = 1) peut contenir au maximum 2n² = 2 × 1² = 2 électrons.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Combien d'électrons peut contenir au maximum la couche L ?",
                            'options': ["8", "2", "18", "32"],
                            'reponse_correcte': '0',
                            'explication': "La couche L (n = 2) peut contenir au maximum 2n² = 2 × 2² = 8 électrons.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Quelle est la structure électronique du carbone C (Z = 6) ?",
                            'options': ["(K)² (L)⁴", "(K)² (L)⁶", "(K)⁶", "(K)² (L)² (M)²"],
                            'reponse_correcte': '0',
                            'explication': "Le carbone a 6 électrons : 2 sur K (saturée) et 4 sur L. Structure : (K)²(L)⁴.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Les électrons de valence sont ceux situés sur :",
                            'options': ["La couche externe", "La couche K uniquement", "Toutes les couches internes", "Le noyau"],
                            'reponse_correcte': '0',
                            'explication': "Les électrons de valence sont les électrons de la couche externe (la dernière couche occupée). Ce sont eux qui participent aux liaisons chimiques.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La structure électronique du sodium Na (Z = 11) est :",
                            'options': ["(K)² (L)⁸ (M)¹", "(K)² (L)⁹", "(K)² (L)⁸ (M)³", "(K)¹¹"],
                            'reponse_correcte': '0',
                            'explication': "Na a 11 électrons : 2 sur K, 8 sur L (saturée), 1 sur M. Structure : (K)²(L)⁸(M)¹.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quel est le rôle des électrons de cœur ?",
                            'options': ["Ils ne participent pas aux liaisons chimiques", "Ils forment les liaisons covalentes", "Ils déterminent les propriétés chimiques", "Ils sont échangés lors des réactions"],
                            'reponse_correcte': '0',
                            'explication': "Les électrons de cœur sont ceux des couches internes saturées. Ils ne participent pas aux liaisons chimiques, contrairement aux électrons de valence.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Pourquoi les gaz nobles sont-ils chimiquement stables ?",
                            'options': ["Leur couche externe est saturée", "Ils n'ont pas d'électrons", "Ils n'ont pas de noyau", "Leur couche K est vide"],
                            'reponse_correcte': '0',
                            'explication': "Les gaz nobles (He, Ne, Ar…) ont leur couche externe pleine (2 pour He, 8 pour les autres), ce qui les rend très stables et quasi inertes chimiquement.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "L'hélium He (Z = 2) a pour structure électronique :",
                            'options': ["(K)²", "(K)¹ (L)¹", "(K)² (L)²", "(L)²"],
                            'reponse_correcte': '0',
                            'explication': "L'hélium a 2 électrons qui remplissent entièrement la couche K. Structure : (K)².",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Combien d'électrons de valence possède l'oxygène O (Z = 8) ?",
                            'options': ["6", "8", "2", "4"],
                            'reponse_correcte': '0',
                            'explication': "O (Z = 8) : structure (K)²(L)⁶. La couche externe est L avec 6 électrons de valence.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Le chlore Cl (Z = 17) a pour structure (K)²(L)⁸(M)⁷. Combien d'électrons de cœur possède-t-il ?",
                            'options': ["10", "7", "17", "2"],
                            'reponse_correcte': '0',
                            'explication': "Les électrons de cœur sont ceux des couches internes : K (2) + L (8) = 10 électrons de cœur.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "La formule générale donnant le nombre maximal d'électrons sur la couche n est :",
                            'options': ["2n²", "n²", "2n", "n + 2"],
                            'reponse_correcte': '0',
                            'explication': "La couche de numéro n peut contenir au maximum 2n² électrons.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Quelle est la structure électronique de l'aluminium Al (Z = 13) ?",
                            'options': ["(K)² (L)⁸ (M)³", "(K)² (L)⁸ (M)⁵", "(K)² (L)¹¹", "(K)¹³"],
                            'reponse_correcte': '0',
                            'explication': "Al a 13 électrons : 2 sur K, 8 sur L (saturée), 3 sur M. Structure : (K)²(L)⁸(M)³.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Le néon Ne (Z = 10) est un gaz noble car :",
                            'options': ["Sa couche externe L contient 8 électrons (saturée)", "Il n'a pas d'électrons", "Sa couche M est pleine", "Il a 10 neutrons"],
                            'reponse_correcte': '0',
                            'explication': "Ne (Z = 10) : (K)²(L)⁸. La couche L est saturée avec 8 électrons, ce qui confère au néon une grande stabilité chimique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Deux atomes ayant le même nombre d'électrons de valence ont :",
                            'options': ["Des propriétés chimiques similaires", "La même masse", "Le même nombre de neutrons", "Le même numéro atomique"],
                            'reponse_correcte': '0',
                            'explication': "Les électrons de valence déterminent les propriétés chimiques. Deux atomes avec le même nombre d'électrons de valence appartiennent à la même famille et ont des propriétés chimiques similaires.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "On remplit d'abord la couche L avant la couche K.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "On remplit les couches dans l'ordre croissant d'énergie : K d'abord, puis L, puis M.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La couche M peut contenir au maximum 18 électrons.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "D'après la formule 2n², la couche M (n = 3) peut contenir au maximum 2 × 3² = 18 électrons.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Le lithium Li (Z = 3) possède 3 électrons de valence.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Li (Z = 3) : (K)²(L)¹. Il possède 1 seul électron de valence sur la couche L. Les 2 électrons de K sont des électrons de cœur.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Donner la structure électronique de l'azote N (Z = 7) sous la forme (K)ⁿ(L)ⁿ.",
                            'options': None,
                            'reponse_correcte': '(K)2(L)5',
                            'tolerances': ['(K)²(L)⁵', '(K)2 (L)5', '(K)² (L)⁵', 'K2 L5', 'K2L5'],
                            'explication': "N (Z = 7) : 2 électrons sur K, 5 sur L → (K)²(L)⁵.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Combien d'électrons de valence possède le phosphore P (Z = 15) ?",
                            'options': None,
                            'reponse_correcte': '5',
                            'tolerances': ['cinq'],
                            'explication': "P (Z = 15) : (K)²(L)⁸(M)⁵. La couche externe M contient 5 électrons de valence.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quel gaz noble possède la structure électronique (K)²(L)⁸ ?",
                            'options': None,
                            'reponse_correcte': 'néon',
                            'tolerances': ['neon', 'Ne', 'le néon'],
                            'explication': "(K)²(L)⁸ correspond à 10 électrons → Z = 10, c'est le néon (Ne).",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 3 — La classification périodique
    # ──────────────────────────────────────────────
    {
        'ordre': 3,
        'titre': 'La classification périodique',
        'description': "Comprendre l'organisation du tableau périodique, les familles chimiques et leurs propriétés.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Construction et lecture du tableau périodique',
                'duree': 35,
                'contenu': """# Construction et lecture du tableau périodique

## Introduction historique

En 1869, le chimiste russe **Dmitri Mendeleïev** propose de classer les éléments chimiques connus par **masse atomique croissante** et en regroupant ceux qui ont des propriétés chimiques similaires. Ce travail visionnaire aboutit au **tableau périodique des éléments**, l'un des outils les plus importants de la chimie.

> **Fait remarquable :** Mendeleïev avait laissé des cases vides dans son tableau, prédisant l'existence d'éléments alors inconnus. Ils furent découverts par la suite avec les propriétés qu'il avait annoncées !

Le tableau moderne est classé par **numéro atomique** $Z$ croissant (et non par masse).

---

## Structure du tableau périodique

Le tableau périodique est organisé en **lignes** (périodes) et **colonnes** (groupes).

### Les périodes (lignes)

Une **période** est une ligne horizontale du tableau. Tous les éléments d'une même période possèdent le **même nombre de couches électroniques occupées**.

| Période | Couches occupées | Nombre d'éléments | Exemples |
|---------|------------------|--------------------|----------|
| 1 | K | 2 | $H$, $He$ |
| 2 | K, L | 8 | $Li$, $C$, $N$, $O$, $Ne$ |
| 3 | K, L, M | 8 | $Na$, $Al$, $Si$, $Cl$, $Ar$ |

> **Règle :** le numéro de la période correspond au numéro $n$ de la **couche externe**.

### Les groupes (colonnes)

Un **groupe** (ou famille) est une colonne du tableau. Tous les éléments d'un même groupe possèdent le **même nombre d'électrons de valence**.

> **Règle :** le numéro du groupe (pour les groupes principaux, notés 1 à 18 ou IA à VIIIA) est lié au nombre d'électrons sur la couche externe.

| Groupe | Électrons de valence | Nom de la famille |
|--------|---------------------|-------------------|
| 1 (IA) | 1 | Alcalins |
| 2 (IIA) | 2 | Alcalino-terreux |
| 17 (VIIA) | 7 | Halogènes |
| 18 (VIIIA) | 8 (ou 2 pour He) | Gaz nobles |

---

## Lire le tableau périodique

Chaque case du tableau périodique fournit des informations sur l'élément :

### Informations contenues dans une case

Pour un élément donné, on trouve généralement :

- Le **symbole** chimique (ex : $Na$, $Cl$, $Fe$)
- Le **numéro atomique** $Z$ (nombre de protons)
- Le **nom** de l'élément
- La **masse atomique relative** (moyenne pondérée des isotopes, en u.m.a.)

### Localiser un élément à partir de sa structure électronique

**Méthode :**

1. Écrire la structure électronique de l'atome.
2. Le **numéro de la période** = numéro de la couche externe.
3. Le **numéro du groupe** (principal) = nombre d'électrons de valence (pour les groupes 1, 2 et 13 à 18).

### Exemple : le soufre $S$ ($Z = 16$)

1. Structure : (K)$^2$ (L)$^8$ (M)$^6$
2. Couche externe : M → **période 3**
3. Électrons de valence : 6 → **groupe 16** (VIA)

Le soufre se trouve en **période 3**, **groupe 16**.

### Exemple : le magnésium $Mg$ ($Z = 12$)

1. Structure : (K)$^2$ (L)$^8$ (M)$^2$
2. Couche externe : M → **période 3**
3. Électrons de valence : 2 → **groupe 2** (IIA)

Le magnésium se trouve en **période 3**, **groupe 2** (alcalino-terreux).

---

## Les 18 premiers éléments

| $Z$ | Symbole | Nom | Structure | Période | Groupe |
|-----|---------|-----|-----------|---------|--------|
| 1 | $H$ | Hydrogène | (K)$^1$ | 1 | 1 |
| 2 | $He$ | Hélium | (K)$^2$ | 1 | 18 |
| 3 | $Li$ | Lithium | (K)$^2$(L)$^1$ | 2 | 1 |
| 4 | $Be$ | Béryllium | (K)$^2$(L)$^2$ | 2 | 2 |
| 5 | $B$ | Bore | (K)$^2$(L)$^3$ | 2 | 13 |
| 6 | $C$ | Carbone | (K)$^2$(L)$^4$ | 2 | 14 |
| 7 | $N$ | Azote | (K)$^2$(L)$^5$ | 2 | 15 |
| 8 | $O$ | Oxygène | (K)$^2$(L)$^6$ | 2 | 16 |
| 9 | $F$ | Fluor | (K)$^2$(L)$^7$ | 2 | 17 |
| 10 | $Ne$ | Néon | (K)$^2$(L)$^8$ | 2 | 18 |
| 11 | $Na$ | Sodium | (K)$^2$(L)$^8$(M)$^1$ | 3 | 1 |
| 12 | $Mg$ | Magnésium | (K)$^2$(L)$^8$(M)$^2$ | 3 | 2 |
| 13 | $Al$ | Aluminium | (K)$^2$(L)$^8$(M)$^3$ | 3 | 13 |
| 14 | $Si$ | Silicium | (K)$^2$(L)$^8$(M)$^4$ | 3 | 14 |
| 15 | $P$ | Phosphore | (K)$^2$(L)$^8$(M)$^5$ | 3 | 15 |
| 16 | $S$ | Soufre | (K)$^2$(L)$^8$(M)$^6$ | 3 | 16 |
| 17 | $Cl$ | Chlore | (K)$^2$(L)$^8$(M)$^7$ | 3 | 17 |
| 18 | $Ar$ | Argon | (K)$^2$(L)$^8$(M)$^8$ | 3 | 18 |

---

## Évolution de $Z$ dans le tableau

En parcourant le tableau de **gauche à droite** sur une période, $Z$ augmente de 1 à chaque case. On ajoute un électron (et un proton) à chaque nouvel élément.

En descendant dans un **groupe**, $Z$ augmente et une nouvelle couche électronique est ajoutée, mais le nombre d'électrons de valence reste le même.

---

## À retenir

- Le tableau périodique classe les éléments par **numéro atomique** $Z$ croissant.
- Une **période** (ligne) = même nombre de couches électroniques ; le numéro de la période = numéro de la couche externe.
- Un **groupe** (colonne) = même nombre d'électrons de valence → propriétés chimiques similaires.
- On retrouve la position d'un élément à partir de sa **structure électronique** : période = couche externe, groupe = électrons de valence.
""",
                'quiz': {
                    'titre': 'Quiz — Construction et lecture du tableau périodique',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Qui a proposé la première classification périodique des éléments en 1869 ?",
                            'options': ["Dmitri Mendeleïev", "Antoine Lavoisier", "John Dalton", "Marie Curie"],
                            'reponse_correcte': '0',
                            'explication': "Dmitri Mendeleïev a proposé en 1869 de classer les éléments par masse atomique croissante en regroupant ceux ayant des propriétés chimiques similaires.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Dans le tableau périodique actuel, les éléments sont classés par ordre croissant de :",
                            'options': ["Numéro atomique Z", "Masse atomique", "Nombre de neutrons", "Électronégativité"],
                            'reponse_correcte': '0',
                            'explication': "Le tableau moderne classe les éléments par numéro atomique Z croissant (nombre de protons).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Qu'est-ce qu'une période dans le tableau périodique ?",
                            'options': ["Une ligne horizontale regroupant les éléments ayant le même nombre de couches électroniques", "Une colonne verticale regroupant les éléments ayant les mêmes propriétés", "Un bloc d'éléments métalliques", "Un ensemble d'éléments de même masse"],
                            'reponse_correcte': '0',
                            'explication': "Une période est une ligne horizontale du tableau. Tous les éléments d'une même période possèdent le même nombre de couches électroniques occupées.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Qu'est-ce qu'un groupe (colonne) du tableau périodique ?",
                            'options': ["Un ensemble d'éléments ayant le même nombre d'électrons de valence", "Un ensemble d'éléments de même masse", "Un ensemble d'éléments ayant le même nombre de neutrons", "Un ensemble d'éléments gazeux"],
                            'reponse_correcte': '0',
                            'explication': "Un groupe (colonne) rassemble les éléments ayant le même nombre d'électrons de valence, ce qui leur confère des propriétés chimiques similaires.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Le sodium Na (Z = 11) a la structure (K)²(L)⁸(M)¹. Dans quelle période se trouve-t-il ?",
                            'options': ["Période 3", "Période 1", "Période 2", "Période 11"],
                            'reponse_correcte': '0',
                            'explication': "La couche externe du sodium est M (3e couche), donc il se trouve en période 3.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Combien d'éléments contient la période 2 du tableau périodique ?",
                            'options': ["8", "2", "18", "10"],
                            'reponse_correcte': '0',
                            'explication': "La période 2 contient 8 éléments (du lithium Li au néon Ne), correspondant au remplissage de la couche L (8 électrons max).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Le carbone C (Z = 6) a la structure (K)²(L)⁴. Quel est son numéro de groupe ?",
                            'options': ["Groupe 14", "Groupe 4", "Groupe 6", "Groupe 2"],
                            'reponse_correcte': '0',
                            'explication': "Le carbone a 4 électrons de valence. Pour les éléments du bloc principal à partir de la colonne 13, le groupe est 10 + nombre d'électrons de valence = 14.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Quel élément a la structure électronique (K)²(L)⁸(M)⁷ ?",
                            'options': ["Le chlore (Cl)", "Le soufre (S)", "L'argon (Ar)", "Le phosphore (P)"],
                            'reponse_correcte': '0',
                            'explication': "2 + 8 + 7 = 17 électrons → Z = 17, c'est le chlore Cl.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Quelle information le numéro de la période d'un élément donne-t-il directement ?",
                            'options': ["Le numéro de la couche externe", "Le nombre total d'électrons", "Le nombre de neutrons", "La masse atomique"],
                            'reponse_correcte': '0',
                            'explication': "Le numéro de la période correspond au numéro n de la couche électronique externe de l'atome.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "L'aluminium Al (Z = 13) possède la structure (K)²(L)⁸(M)³. Il se trouve en :",
                            'options': ["Période 3, groupe 13", "Période 2, groupe 3", "Période 13, groupe 3", "Période 3, groupe 3"],
                            'reponse_correcte': '0',
                            'explication': "Couche externe = M → période 3. Électrons de valence = 3 → groupe 13 (car 10 + 3 = 13 pour le bloc p).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Un élément est en période 2 et possède 5 électrons de valence. De quel élément s'agit-il ?",
                            'options': ["L'azote (N)", "Le phosphore (P)", "Le bore (B)", "L'oxygène (O)"],
                            'reponse_correcte': '0',
                            'explication': "Période 2 → couches K et L. 5 électrons de valence sur la couche L → (K)²(L)⁵ → Z = 7 → azote N.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Pourquoi Mendeleïev avait-il laissé des cases vides dans son tableau ?",
                            'options': ["Il prédisait l'existence d'éléments non encore découverts", "Il ne connaissait pas assez d'éléments", "Il avait fait des erreurs de calcul", "Les éléments correspondants étaient radioactifs"],
                            'reponse_correcte': '0',
                            'explication': "Mendeleïev a laissé des cases vides en prédisant les propriétés d'éléments alors inconnus, qui furent découverts par la suite.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Combien de couches électroniques un élément de la période 1 possède-t-il ?",
                            'options': ["1 (couche K uniquement)", "2", "3", "0"],
                            'reponse_correcte': '0',
                            'explication': "Les éléments de la période 1 (H et He) n'ont qu'une seule couche électronique occupée : la couche K.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Le soufre S (Z = 16) est dans le groupe 16. Combien d'électrons de valence possède-t-il ?",
                            'options': ["6", "16", "8", "2"],
                            'reponse_correcte': '0',
                            'explication': "Le soufre a la structure (K)²(L)⁸(M)⁶. Il possède 6 électrons sur sa couche externe M.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Tous les éléments d'une même colonne du tableau périodique possèdent le même nombre de couches électroniques.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Les éléments d'une même colonne ont le même nombre d'électrons de valence, mais pas le même nombre de couches. C'est dans une même ligne (période) que le nombre de couches est identique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "L'hélium He (Z = 2) est un gaz noble situé en période 1 et groupe 18.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "L'hélium a la structure (K)² : couche K uniquement → période 1, et sa couche externe est saturée → gaz noble, groupe 18.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Le numéro atomique Z correspond au nombre de neutrons dans le noyau.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le numéro atomique Z correspond au nombre de protons dans le noyau (et au nombre d'électrons dans l'atome neutre), pas au nombre de neutrons.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quelle est la structure électronique du néon Ne (Z = 10) ? Écrire sous la forme (K)ˣ(L)ʸ.",
                            'options': None,
                            'reponse_correcte': '(K)2(L)8',
                            'tolerances': ['(K)²(L)⁸', 'K2 L8', 'K2L8', '(K)2 (L)8'],
                            'explication': "Le néon a 10 électrons : 2 sur la couche K (saturée) et 8 sur la couche L (saturée) → (K)²(L)⁸.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Un élément a pour structure électronique (K)²(L)⁸(M)⁶. Quel est son symbole chimique ?",
                            'options': None,
                            'reponse_correcte': 'S',
                            'tolerances': ['s', 'soufre', 'Soufre'],
                            'explication': "Z = 2 + 8 + 6 = 16 → c'est le soufre, de symbole S.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quel est le nom de la famille chimique des éléments du groupe 17 (colonne 17) ?",
                            'options': None,
                            'reponse_correcte': 'halogènes',
                            'tolerances': ['halogenes', 'les halogènes', 'les halogenes', 'Halogènes'],
                            'explication': "Les éléments du groupe 17 (F, Cl, Br, I…) forment la famille des halogènes. Ils possèdent 7 électrons de valence.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Familles chimiques et propriétés',
                'duree': 35,
                'contenu': """# Familles chimiques et propriétés

## Introduction

Les éléments d'une même **colonne** (groupe) du tableau périodique forment une **famille chimique** : ils partagent le même nombre d'**électrons de valence** et présentent des propriétés chimiques similaires. Cette régularité est à l'origine du mot « périodique » dans le nom du tableau.

---

## Les principales familles chimiques

### Les alcalins — Groupe 1 (colonne 1)

Les **alcalins** sont les éléments du groupe 1, à l'exception de l'hydrogène (cas particulier).

| Élément | $Z$ | Structure | Électrons de valence |
|---------|-----|-----------|---------------------|
| Lithium $Li$ | 3 | (K)$^2$(L)$^1$ | 1 |
| Sodium $Na$ | 11 | (K)$^2$(L)$^8$(M)$^1$ | 1 |
| Potassium $K$ | 19 | …(M)$^8$(N)$^1$ | 1 |

**Propriétés communes :**

- **1 électron de valence** → ils perdent facilement cet électron pour former un **cation** de charge $+1$ : $Li^+$, $Na^+$, $K^+$
- Métaux mous, brillants quand fraîchement coupés
- Très **réactifs** : réagissent vivement avec l'eau ($2Na + 2H_2O \\to 2NaOH + H_2$)
- La réactivité **augmente** en descendant dans le groupe (le potassium est plus réactif que le sodium)

> **Attention :** l'hydrogène $H$ est placé dans le groupe 1 car il possède 1 électron de valence, mais il n'est **pas** un métal alcalin. C'est un non-métal gazeux.

---

### Les alcalino-terreux — Groupe 2 (colonne 2)

| Élément | $Z$ | Structure | Électrons de valence |
|---------|-----|-----------|---------------------|
| Béryllium $Be$ | 4 | (K)$^2$(L)$^2$ | 2 |
| Magnésium $Mg$ | 12 | (K)$^2$(L)$^8$(M)$^2$ | 2 |
| Calcium $Ca$ | 20 | …(M)$^8$(N)$^2$ | 2 |

**Propriétés communes :**

- **2 électrons de valence** → forment des **cations** de charge $+2$ : $Mg^{2+}$, $Ca^{2+}$
- Métaux réactifs (moins que les alcalins)
- Le calcium réagit avec l'eau plus lentement que le sodium

---

### Les halogènes — Groupe 17 (colonne 17)

| Élément | $Z$ | Structure | Électrons de valence |
|---------|-----|-----------|---------------------|
| Fluor $F$ | 9 | (K)$^2$(L)$^7$ | 7 |
| Chlore $Cl$ | 17 | (K)$^2$(L)$^8$(M)$^7$ | 7 |
| Brome $Br$ | 35 | …(M)$^{18}$(N)$^7$ | 7 |
| Iode $I$ | 53 | … | 7 |

**Propriétés communes :**

- **7 électrons de valence** → il leur manque **1 seul électron** pour compléter leur couche externe
- Ils gagnent facilement un électron pour former un **anion** de charge $-1$ : $F^-$, $Cl^-$, $Br^-$, $I^-$
- **Non-métaux**, très réactifs, à l'état naturel sous forme de molécules diatomiques : $F_2$, $Cl_2$, $Br_2$, $I_2$
- La réactivité **diminue** en descendant dans le groupe (le fluor est le plus réactif)

> Le chlore est un gaz jaune-vert toxique ; le brome est un liquide rouge-brun ; l'iode est un solide gris-violet qui se sublime facilement.

---

### Les gaz nobles — Groupe 18 (colonne 18)

| Élément | $Z$ | Structure | Électrons de valence |
|---------|-----|-----------|---------------------|
| Hélium $He$ | 2 | (K)$^2$ | 2 (couche K saturée) |
| Néon $Ne$ | 10 | (K)$^2$(L)$^8$ | 8 |
| Argon $Ar$ | 18 | (K)$^2$(L)$^8$(M)$^8$ | 8 |

**Propriétés communes :**

- Couche externe **saturée** (2 pour He, 8 pour les autres) → configuration très stable
- **Chimiquement inertes** : ne forment quasiment aucune liaison chimique
- Gaz incolores et inodores à température ambiante
- Utilisations : néon (enseignes lumineuses), argon (ampoules à incandescence, soudure), hélium (ballons, plongée)

---

## Métaux, non-métaux et métalloïdes

Le tableau périodique sépare les éléments en grandes catégories :

### Métaux

- Situés **à gauche et au centre** du tableau (majorité des éléments)
- Propriétés : solides à température ambiante (sauf le mercure $Hg$, liquide), brillants, bons conducteurs de chaleur et d'électricité, malléables et ductiles
- Tendent à **perdre** des électrons → forment des **cations** ($Na^+$, $Fe^{2+}$, $Al^{3+}$…)

### Non-métaux

- Situés **en haut à droite** du tableau
- Propriétés : mauvais conducteurs (isolants), souvent gazeux ou solides cassants
- Tendent à **gagner** des électrons → forment des **anions** ($Cl^-$, $O^{2-}$, $S^{2-}$…)
- Exemples : $C$, $N$, $O$, $F$, $Cl$, $S$, $P$

### Métalloïdes (semi-métaux)

- Situés le long de la **diagonale** séparant métaux et non-métaux
- Propriétés intermédiaires : semi-conducteurs (silicium $Si$, germanium $Ge$)
- Utilisés en électronique (puces, panneaux solaires)

---

## Évolution des propriétés dans le tableau

### Le long d'une période (de gauche à droite)

En avançant de gauche à droite sur une même période :

- Le nombre de protons ($Z$) augmente → le noyau attire plus fortement les électrons
- Le **rayon atomique diminue** (les électrons sont plus attirés vers le noyau)
- L'**électronégativité augmente** (capacité à attirer les électrons dans une liaison)
- Le caractère **métallique diminue** : on passe des métaux (à gauche) aux non-métaux (à droite)

### Le long d'un groupe (de haut en bas)

En descendant dans un groupe :

- On ajoute une couche électronique → le **rayon atomique augmente**
- Les électrons de valence sont plus éloignés du noyau → l'**électronégativité diminue**
- Le caractère **métallique augmente**

---

## L'électronégativité

### Définition

L'**électronégativité** est la capacité d'un atome à **attirer** vers lui les électrons d'une liaison chimique. Elle est notée $\\chi$ (chi) et se mesure sans unité sur l'échelle de Pauling.

### Tendances

- L'élément le **plus électronégatif** est le **fluor** ($\\chi = 4{,}0$)
- Les gaz nobles n'ont pas d'électronégativité définie (ils ne forment pas de liaisons)
- L'électronégativité **croît** de gauche à droite et de bas en haut dans le tableau

| Élément | $\\chi$ (Pauling) |
|---------|------------------|
| $F$ | 4,0 |
| $O$ | 3,4 |
| $N$ | 3,0 |
| $Cl$ | 3,2 |
| $C$ | 2,6 |
| $H$ | 2,2 |
| $Na$ | 0,9 |

> **Application :** dans une liaison entre deux atomes, l'atome le plus électronégatif attire davantage les électrons de la liaison. Cela crée une **liaison polarisée**.

---

## Notion d'ion stable

Un atome a tendance à gagner ou perdre des électrons pour acquérir la **configuration électronique du gaz noble le plus proche** :

| Atome | $Z$ | Électrons de valence | Tendance | Ion formé | Configuration du gaz noble |
|-------|-----|---------------------|----------|-----------|----------------------------|
| $Na$ | 11 | 1 | Perd 1 é | $Na^+$ (10 é) | Néon ($Ne$) |
| $Mg$ | 12 | 2 | Perd 2 é | $Mg^{2+}$ (10 é) | Néon ($Ne$) |
| $Al$ | 13 | 3 | Perd 3 é | $Al^{3+}$ (10 é) | Néon ($Ne$) |
| $O$ | 8 | 6 | Gagne 2 é | $O^{2-}$ (10 é) | Néon ($Ne$) |
| $F$ | 9 | 7 | Gagne 1 é | $F^-$ (10 é) | Néon ($Ne$) |
| $Cl$ | 17 | 7 | Gagne 1 é | $Cl^-$ (18 é) | Argon ($Ar$) |

> **Règle de l'octet :** les atomes tendent à acquérir **8 électrons** sur leur couche externe (ou 2 pour ceux de la période 1, règle du **duet**). C'est ce qui gouverne la formation des ions et des liaisons chimiques.

---

## À retenir

- Les éléments d'un même **groupe** ont le même nombre d'électrons de valence → propriétés chimiques similaires.
- **Alcalins** (groupe 1) : 1 é de valence, forment $X^+$, très réactifs.
- **Halogènes** (groupe 17) : 7 é de valence, forment $X^-$, très réactifs.
- **Gaz nobles** (groupe 18) : couche externe saturée, quasi inertes.
- Le caractère métallique **diminue** de gauche à droite et **augmente** de haut en bas.
- L'**électronégativité** croît de gauche à droite et de bas en haut (le fluor est le plus électronégatif).
- Les atomes forment des ions pour atteindre la configuration du **gaz noble le plus proche** (règle de l'octet).
""",
                'quiz': {
                    'titre': 'Quiz — Familles chimiques et propriétés',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Les éléments d'une même famille chimique ont en commun :",
                            'options': ["Le même nombre d'électrons de valence", "Le même nombre de couches électroniques", "Le même numéro atomique", "La même masse atomique"],
                            'reponse_correcte': '0',
                            'explication': "Les éléments d'un même groupe (colonne) partagent le même nombre d'électrons de valence, ce qui leur confère des propriétés chimiques similaires.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "À quelle famille appartient le sodium Na (groupe 1) ?",
                            'options': ["Les alcalins", "Les halogènes", "Les gaz nobles", "Les alcalino-terreux"],
                            'reponse_correcte': '0',
                            'explication': "Le sodium se trouve dans le groupe 1 : c'est un métal alcalin (1 électron de valence).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Les gaz nobles (groupe 18) sont chimiquement inertes car :",
                            'options': ["Leur couche externe est saturée", "Ils n'ont pas d'électrons", "Ils sont toujours à l'état liquide", "Ils possèdent un seul proton"],
                            'reponse_correcte': '0',
                            'explication': "Les gaz nobles ont leur couche externe saturée (2 é pour He, 8 é pour les autres), ce qui les rend très stables et quasi inertes chimiquement.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Les halogènes (groupe 17) possèdent combien d'électrons de valence ?",
                            'options': ["7", "1", "8", "17"],
                            'reponse_correcte': '0',
                            'explication': "Les halogènes (F, Cl, Br, I) possèdent 7 électrons de valence. Il leur manque 1 électron pour saturer leur couche externe.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Quel est le type d'ion que forment préférentiellement les alcalins ?",
                            'options': ["Un cation de charge +1", "Un anion de charge −1", "Un cation de charge +2", "Ils ne forment pas d'ions"],
                            'reponse_correcte': '0',
                            'explication': "Les alcalins possèdent 1 électron de valence qu'ils perdent facilement, formant un cation de charge +1 (ex : Na⁺, K⁺).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Les métaux sont situés principalement dans quelle partie du tableau périodique ?",
                            'options': ["À gauche et au centre", "En haut à droite", "Uniquement dans la dernière colonne", "Uniquement en période 1"],
                            'reponse_correcte': '0',
                            'explication': "Les métaux constituent la majorité des éléments et sont situés à gauche et au centre du tableau périodique.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Quel gaz noble a la configuration électronique (K)²(L)⁸ ?",
                            'options': ["Le néon (Ne)", "L'hélium (He)", "L'argon (Ar)", "Le krypton (Kr)"],
                            'reponse_correcte': '0',
                            'explication': "Le néon (Z = 10) a la structure (K)²(L)⁸ avec 10 électrons au total.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Parmi ces éléments, lequel est un non-métal ?",
                            'options': ["Le chlore (Cl)", "Le fer (Fe)", "Le cuivre (Cu)", "Le sodium (Na)"],
                            'reponse_correcte': '0',
                            'explication': "Le chlore est un non-métal situé en haut à droite du tableau (groupe 17, halogènes). Le fer, le cuivre et le sodium sont des métaux.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Lorsqu'on se déplace de gauche à droite sur une période, l'électronégativité :",
                            'options': ["Augmente", "Diminue", "Reste constante", "Passe par un maximum au centre"],
                            'reponse_correcte': '0',
                            'explication': "L'électronégativité croît de gauche à droite sur une période car le noyau, plus chargé, attire plus fortement les électrons de liaison.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quel est l'élément le plus électronégatif du tableau périodique ?",
                            'options': ["Le fluor (F)", "L'oxygène (O)", "Le chlore (Cl)", "L'azote (N)"],
                            'reponse_correcte': '0',
                            'explication': "Le fluor (χ = 4,0 sur l'échelle de Pauling) est l'élément le plus électronégatif du tableau périodique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "En descendant dans un groupe du tableau périodique, le rayon atomique :",
                            'options': ["Augmente", "Diminue", "Reste le même", "Dépend de la masse uniquement"],
                            'reponse_correcte': '0',
                            'explication': "En descendant dans un groupe, on ajoute une couche électronique à chaque période, ce qui éloigne les électrons externes du noyau et augmente le rayon atomique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Les alcalino-terreux (groupe 2) forment préférentiellement des ions de charge :",
                            'options': ["+2", "+1", "−1", "−2"],
                            'reponse_correcte': '0',
                            'explication': "Les alcalino-terreux possèdent 2 électrons de valence qu'ils perdent pour former des cations de charge +2 (ex : Mg²⁺, Ca²⁺).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Quel ion stable forme le chlore Cl (Z = 17, groupe 17) ?",
                            'options': ["Cl⁻", "Cl⁺", "Cl²⁻", "Cl²⁺"],
                            'reponse_correcte': '0',
                            'explication': "Le chlore a 7 électrons de valence ; il gagne 1 électron pour saturer sa couche externe (8 é), formant l'anion Cl⁻.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Le silicium (Si) est classé comme :",
                            'options': ["Un métalloïde (semi-métal)", "Un métal", "Un non-métal", "Un gaz noble"],
                            'reponse_correcte': '0',
                            'explication': "Le silicium est un métalloïde situé le long de la diagonale séparant métaux et non-métaux. C'est un semi-conducteur utilisé en électronique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "L'hydrogène appartient à la famille des alcalins car il est dans le groupe 1.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "L'hydrogène est dans le groupe 1 car il possède 1 électron de valence, mais c'est un non-métal gazeux. Il n'appartient pas à la famille des alcalins.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Le caractère métallique augmente de haut en bas dans un groupe du tableau périodique.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "En descendant dans un groupe, le rayon atomique augmente et les électrons de valence sont moins retenus par le noyau, renforçant le caractère métallique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Les halogènes se trouvent à l'état naturel sous forme de molécules diatomiques (F₂, Cl₂, Br₂, I₂).",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Les halogènes sont très réactifs et se trouvent à l'état naturel sous forme de molécules diatomiques : F₂ (gaz), Cl₂ (gaz), Br₂ (liquide), I₂ (solide).",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quel est le nom de la famille chimique du groupe 2 du tableau périodique ?",
                            'options': None,
                            'reponse_correcte': 'alcalino-terreux',
                            'tolerances': ['alcalino terreux', 'les alcalino-terreux', 'alcalinoterreux', 'les alcalino terreux'],
                            'explication': "Les éléments du groupe 2 (Be, Mg, Ca, Sr, Ba…) forment la famille des alcalino-terreux. Ils possèdent 2 électrons de valence.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Le magnésium Mg (Z = 12) perd 2 électrons. Quelle est la configuration électronique du gaz noble dont il acquiert la structure ?",
                            'options': None,
                            'reponse_correcte': '(K)2(L)8',
                            'tolerances': ['(K)²(L)⁸', 'K2 L8', 'K2L8', '(K)2 (L)8', 'neon', 'néon', 'Ne'],
                            'explication': "Mg²⁺ a 10 électrons : (K)²(L)⁸, soit la configuration du néon Ne.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quel est le symbole de l'élément le plus électronégatif ?",
                            'options': None,
                            'reponse_correcte': 'F',
                            'tolerances': ['f', 'fluor', 'Fluor'],
                            'explication': "Le fluor (F) est l'élément le plus électronégatif avec χ = 4,0 sur l'échelle de Pauling.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 4 — Les molécules et les ions
    # ──────────────────────────────────────────────
    {
        'ordre': 4,
        'titre': 'Les molécules et les ions',
        'description': "Comprendre la formation des ions monoatomiques, la liaison covalente, le schéma de Lewis et la géométrie des molécules.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Ions monoatomiques — formation et stabilité',
                'duree': 35,
                'contenu': """# Ions monoatomiques — formation et stabilité

## Introduction

Les atomes isolés sont rarement stables dans la nature. Pour atteindre une configuration électronique plus stable, ils peuvent **gagner** ou **perdre** des électrons et se transformer en **ions**. La compréhension des ions est essentielle : ils composent les cristaux ioniques (sel de cuisine, calcaire…), sont dissous dans l'eau de mer, dans notre sang, et interviennent dans d'innombrables réactions chimiques.

---

## Rappels — stabilité des gaz nobles

Les **gaz nobles** (hélium $He$, néon $Ne$, argon $Ar$…) sont chimiquement inertes car leur couche externe est **saturée** :

| Gaz noble | $Z$ | Structure électronique | Couche externe |
|-----------|-----|----------------------|----------------|
| $He$ | 2 | (K)$^2$ | 2 électrons (saturée) |
| $Ne$ | 10 | (K)$^2$(L)$^8$ | 8 électrons (saturée) |
| $Ar$ | 18 | (K)$^2$(L)$^8$(M)$^8$ | 8 électrons (saturée) |

> **Règle de l'octet :** les atomes tendent à acquérir **8 électrons** sur leur couche externe pour atteindre la configuration du gaz noble le plus proche.

> **Règle du duet :** pour les atomes proches de l'hélium ($H$, $Li$), la stabilité correspond à **2 électrons** sur la couche K.

---

## Qu'est-ce qu'un ion ?

### Définition

Un **ion** est un atome (ou un groupe d'atomes) qui a **gagné ou perdu** un ou plusieurs électrons. Un ion porte donc une **charge électrique** non nulle.

- Si l'atome **perd** des électrons → il devient un **cation** (ion positif, noté $X^{n+}$)
- Si l'atome **gagne** des électrons → il devient un **anion** (ion négatif, noté $X^{n-}$)

### Ion monoatomique

Un **ion monoatomique** est issu d'un **seul atome** ayant gagné ou perdu des électrons.

> **Exemples :** $Na^+$ (sodium ayant perdu 1 électron), $Cl^-$ (chlore ayant gagné 1 électron).

---

## Formation des cations

### Mécanisme

Un atome de **métal** (situé à gauche du tableau périodique) possède peu d'électrons de valence (1, 2 ou 3). Il est plus « facile » énergétiquement de **perdre** ces quelques électrons que d'en gagner 5, 6 ou 7 pour compléter la couche externe.

### Exemples détaillés

#### Le sodium $Na$ ($Z = 11$)

- Structure de l'atome : (K)$^2$(L)$^8$(M)$^1$ → **1 électron de valence**
- Il perd cet électron :

$$Na \\longrightarrow Na^+ + e^-$$

- Structure de $Na^+$ : (K)$^2$(L)$^8$ → même configuration que le **néon** $Ne$ → **stable**
- L'ion sodium $Na^+$ porte une charge $+1$ car il a 11 protons pour seulement 10 électrons.

#### Le magnésium $Mg$ ($Z = 12$)

- Structure de l'atome : (K)$^2$(L)$^8$(M)$^2$ → **2 électrons de valence**

$$Mg \\longrightarrow Mg^{2+} + 2e^-$$

- Structure de $Mg^{2+}$ : (K)$^2$(L)$^8$ → configuration du **néon** → **stable**

#### L'aluminium $Al$ ($Z = 13$)

- Structure de l'atome : (K)$^2$(L)$^8$(M)$^3$ → **3 électrons de valence**

$$Al \\longrightarrow Al^{3+} + 3e^-$$

- Structure de $Al^{3+}$ : (K)$^2$(L)$^8$ → configuration du **néon** → **stable**

### Tableau récapitulatif — cations courants

| Atome | $Z$ | Électrons de valence | Électrons perdus | Ion formé | Config. du gaz noble |
|-------|-----|---------------------|------------------|-----------|---------------------|
| $Li$ | 3 | 1 | 1 | $Li^+$ | $He$ (2 é) |
| $Na$ | 11 | 1 | 1 | $Na^+$ | $Ne$ (10 é) |
| $K$ | 19 | 1 | 1 | $K^+$ | $Ar$ (18 é) |
| $Mg$ | 12 | 2 | 2 | $Mg^{2+}$ | $Ne$ (10 é) |
| $Ca$ | 20 | 2 | 2 | $Ca^{2+}$ | $Ar$ (18 é) |
| $Al$ | 13 | 3 | 3 | $Al^{3+}$ | $Ne$ (10 é) |

> **Règle :** la charge du cation est égale au nombre d'électrons de valence perdus, qui correspond au numéro du groupe pour les groupes 1, 2 et 13.

---

## Formation des anions

### Mécanisme

Un atome de **non-métal** (situé à droite du tableau périodique) possède beaucoup d'électrons de valence (5, 6 ou 7). Il lui est plus favorable de **gagner** les quelques électrons manquants pour saturer sa couche externe.

### Exemples détaillés

#### Le chlore $Cl$ ($Z = 17$)

- Structure de l'atome : (K)$^2$(L)$^8$(M)$^7$ → **7 électrons de valence**, il manque 1 électron
- Il gagne 1 électron :

$$Cl + e^- \\longrightarrow Cl^-$$

- Structure de $Cl^-$ : (K)$^2$(L)$^8$(M)$^8$ → configuration de l'**argon** $Ar$ → **stable**
- L'ion chlorure $Cl^-$ porte une charge $-1$ car il a 17 protons pour 18 électrons.

#### L'oxygène $O$ ($Z = 8$)

- Structure de l'atome : (K)$^2$(L)$^6$ → **6 électrons de valence**, il manque 2 électrons

$$O + 2e^- \\longrightarrow O^{2-}$$

- Structure de $O^{2-}$ : (K)$^2$(L)$^8$ → configuration du **néon** → **stable**

#### Le fluor $F$ ($Z = 9$)

$$F + e^- \\longrightarrow F^-$$

- Structure de $F^-$ : (K)$^2$(L)$^8$ → configuration du **néon** → **stable**

### Tableau récapitulatif — anions courants

| Atome | $Z$ | Électrons de valence | Électrons gagnés | Ion formé | Config. du gaz noble |
|-------|-----|---------------------|------------------|-----------|---------------------|
| $F$ | 9 | 7 | 1 | $F^-$ | $Ne$ (10 é) |
| $Cl$ | 17 | 7 | 1 | $Cl^-$ | $Ar$ (18 é) |
| $Br$ | 35 | 7 | 1 | $Br^-$ | $Kr$ (36 é) |
| $O$ | 8 | 6 | 2 | $O^{2-}$ | $Ne$ (10 é) |
| $S$ | 16 | 6 | 2 | $S^{2-}$ | $Ar$ (18 é) |
| $N$ | 7 | 5 | 3 | $N^{3-}$ | $Ne$ (10 é) |

> **Règle :** la charge de l'anion est égale au nombre d'électrons gagnés = $8 -$ nombre d'électrons de valence.

---

## Ions isoélectroniques

Deux espèces chimiques sont **isoélectroniques** si elles possèdent le **même nombre d'électrons** et donc la même structure électronique.

### Exemple : la série isoélectronique du néon (10 électrons)

| Espèce | Protons ($Z$) | Électrons | Charge | Type |
|--------|---------------|-----------|--------|------|
| $N^{3-}$ | 7 | 10 | $3-$ | anion |
| $O^{2-}$ | 8 | 10 | $2-$ | anion |
| $F^-$ | 9 | 10 | $1-$ | anion |
| $Ne$ | 10 | 10 | $0$ | atome neutre |
| $Na^+$ | 11 | 10 | $1+$ | cation |
| $Mg^{2+}$ | 12 | 10 | $2+$ | cation |
| $Al^{3+}$ | 13 | 10 | $3+$ | cation |

> Toutes ces espèces ont la structure (K)$^2$(L)$^8$, soit **10 électrons**.

---

## Composés ioniques

Les **cations** et les **anions** s'associent par **attraction électrostatique** pour former des **composés ioniques** (ou solides ioniques / cristaux ioniques).

### Neutralité électrique

Un composé ionique est **électriquement neutre** : la somme des charges positives compense exactement la somme des charges négatives.

### Exemples

| Composé | Cation | Anion | Formule | Nom |
|---------|--------|-------|---------|-----|
| Chlorure de sodium | $Na^+$ | $Cl^-$ | $NaCl$ | Sel de cuisine |
| Chlorure de calcium | $Ca^{2+}$ | $Cl^-$ | $CaCl_2$ | Sel de déneigement |
| Oxyde d'aluminium | $Al^{3+}$ | $O^{2-}$ | $Al_2O_3$ | Alumine |
| Fluorure de magnésium | $Mg^{2+}$ | $F^-$ | $MgF_2$ | Utilisé en optique |

> **Méthode pour trouver la formule :** on croise les charges. Pour $Al^{3+}$ et $O^{2-}$ : il faut 2 ions $Al^{3+}$ (charge totale $+6$) et 3 ions $O^{2-}$ (charge totale $-6$) → $Al_2O_3$.

---

## À retenir

- Un **ion** est un atome qui a gagné ou perdu des électrons pour atteindre la configuration du **gaz noble le plus proche** (règle de l'octet/duet).
- Les **métaux** perdent des électrons → **cations** ($Na^+$, $Ca^{2+}$, $Al^{3+}$).
- Les **non-métaux** gagnent des électrons → **anions** ($Cl^-$, $O^{2-}$, $F^-$).
- La charge d'un ion se déduit du nombre d'électrons gagnés ou perdus.
- Les composés ioniques sont **électriquement neutres** : on croise les charges pour écrire la formule.
""",
                'quiz': {
                    'titre': 'Quiz — Ions monoatomiques',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Un ion est un atome qui a :",
                            'options': ["Gagné ou perdu un ou plusieurs électrons", "Gagné ou perdu des protons", "Changé de nombre de neutrons", "Fusionné avec un autre atome"],
                            'reponse_correcte': '0',
                            'explication': "Un ion est un atome (ou groupe d'atomes) qui a gagné ou perdu un ou plusieurs électrons, ce qui lui confère une charge électrique non nulle.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Comment appelle-t-on un ion chargé positivement ?",
                            'options': ["Un cation", "Un anion", "Un neutron", "Un proton"],
                            'reponse_correcte': '0',
                            'explication': "Un cation est un ion positif, formé lorsqu'un atome perd un ou plusieurs électrons. Un anion est un ion négatif.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Le sodium Na (Z = 11) forme l'ion Na⁺. Combien d'électrons possède Na⁺ ?",
                            'options': ["10", "11", "12", "9"],
                            'reponse_correcte': '0',
                            'explication': "Na a 11 électrons. En perdant 1 électron pour former Na⁺, il en possède 11 − 1 = 10.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quel type d'atome forme préférentiellement des cations ?",
                            'options': ["Les métaux", "Les non-métaux", "Les gaz nobles", "Les métalloïdes"],
                            'reponse_correcte': '0',
                            'explication': "Les métaux (situés à gauche du tableau) possèdent peu d'électrons de valence et les perdent facilement pour former des cations.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "L'ion chlorure Cl⁻ s'est formé en :",
                            'options': ["Gagnant 1 électron", "Perdant 1 électron", "Gagnant 1 proton", "Perdant 1 neutron"],
                            'reponse_correcte': '0',
                            'explication': "Le chlore (7 électrons de valence) gagne 1 électron pour obtenir 8 électrons sur sa couche externe et former l'anion Cl⁻.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "La règle de l'octet stipule que les atomes tendent à acquérir combien d'électrons sur leur couche externe ?",
                            'options': ["8", "2", "6", "18"],
                            'reponse_correcte': '0',
                            'explication': "La règle de l'octet indique que les atomes tendent à acquérir 8 électrons sur leur couche externe pour atteindre la stabilité d'un gaz noble.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Quel ion forme l'aluminium Al (Z = 13, 3 électrons de valence) ?",
                            'options': ["Al³⁺", "Al⁺", "Al²⁺", "Al³⁻"],
                            'reponse_correcte': '0',
                            'explication': "L'aluminium perd ses 3 électrons de valence pour obtenir la configuration du néon, formant l'ion Al³⁺.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Quelle est la formule du composé ionique formé par Na⁺ et Cl⁻ ?",
                            'options': ["NaCl", "Na₂Cl", "NaCl₂", "Na₂Cl₃"],
                            'reponse_correcte': '0',
                            'explication': "Na⁺ a une charge +1 et Cl⁻ a une charge −1 : il faut 1 ion de chaque pour la neutralité → NaCl.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "L'ion O²⁻ a acquis la configuration électronique de quel gaz noble ?",
                            'options': ["Le néon (Ne)", "L'hélium (He)", "L'argon (Ar)", "Le krypton (Kr)"],
                            'reponse_correcte': '0',
                            'explication': "O (Z = 8) gagne 2 électrons → O²⁻ a 10 électrons, soit la configuration (K)²(L)⁸ du néon.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Combien d'électrons possède l'ion Mg²⁺ ?",
                            'options': ["10", "12", "14", "8"],
                            'reponse_correcte': '0',
                            'explication': "Le magnésium (Z = 12) possède 12 électrons à l'état neutre. En perdant 2 électrons pour former Mg²⁺, il en a 10.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Quelle est la formule du composé ionique formé par Ca²⁺ et Cl⁻ ?",
                            'options': ["CaCl₂", "CaCl", "Ca₂Cl", "Ca₂Cl₃"],
                            'reponse_correcte': '0',
                            'explication': "Ca²⁺ a une charge +2 et Cl⁻ une charge −1 : il faut 2 ions Cl⁻ pour compenser → CaCl₂.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Les espèces Na⁺, Ne et F⁻ sont isoélectroniques car :",
                            'options': ["Elles possèdent toutes 10 électrons", "Elles ont le même nombre de protons", "Elles ont la même charge", "Elles ont la même masse"],
                            'reponse_correcte': '0',
                            'explication': "Na⁺ (11 − 1 = 10 é), Ne (10 é) et F⁻ (9 + 1 = 10 é) ont tous 10 électrons : ils sont isoélectroniques.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Combien d'électrons l'oxygène (Z = 8) doit-il gagner pour satisfaire la règle de l'octet ?",
                            'options': ["2", "1", "6", "8"],
                            'reponse_correcte': '0',
                            'explication': "L'oxygène a 6 électrons de valence. Il lui en manque 8 − 6 = 2 pour saturer sa couche externe → il forme O²⁻.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Quelle est la formule du composé ionique formé par Al³⁺ et O²⁻ ?",
                            'options': ["Al₂O₃", "AlO", "Al₃O₂", "AlO₃"],
                            'reponse_correcte': '0',
                            'explication': "On croise les charges : 2 × Al³⁺ (charge +6) et 3 × O²⁻ (charge −6) → neutralité : Al₂O₃.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Un composé ionique est toujours électriquement neutre.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Un composé ionique est formé de cations et d'anions en proportions telles que la charge globale est nulle (neutralité électrique).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "L'ion K⁺ et l'atome d'argon Ar ont le même nombre d'électrons.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "K (Z = 19) perd 1 électron → K⁺ a 18 électrons. L'argon (Z = 18) a aussi 18 électrons. Ils sont isoélectroniques.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "L'ion Na⁺ a plus d'électrons que l'atome de sodium Na.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Na⁺ a perdu 1 électron par rapport à Na : Na a 11 électrons, Na⁺ en a 10. Na⁺ a donc moins d'électrons.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quel ion stable forme le fluor F (Z = 9) ?",
                            'options': None,
                            'reponse_correcte': 'F-',
                            'tolerances': ['F⁻', 'f-', 'fluorure', 'ion fluorure'],
                            'explication': "Le fluor (7 é de valence) gagne 1 électron pour compléter sa couche externe et forme l'anion fluorure F⁻.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Combien d'électrons possède l'ion Al³⁺ ? (donner le nombre)",
                            'options': None,
                            'reponse_correcte': '10',
                            'tolerances': ['dix'],
                            'explication': "L'aluminium (Z = 13) possède 13 électrons à l'état neutre. Al³⁺ en a perdu 3, donc 13 − 3 = 10 électrons.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quelle est la formule du composé ionique formé par Mg²⁺ et F⁻ ?",
                            'options': None,
                            'reponse_correcte': 'MgF2',
                            'tolerances': ['MgF₂', 'mgf2'],
                            'explication': "Mg²⁺ (charge +2) et F⁻ (charge −1) : il faut 2 ions F⁻ pour compenser → MgF₂.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Molécules — liaison covalente et schéma de Lewis',
                'duree': 40,
                'contenu': """# Molécules — liaison covalente et schéma de Lewis

## Introduction

Les atomes de **non-métaux** peuvent aussi atteindre la stabilité (couche externe saturée) sans gagner ni perdre d'électrons : ils **partagent** des électrons entre eux. Ce partage constitue une **liaison covalente** et donne naissance à des **molécules**. Ce chapitre explique la formation des liaisons covalentes, la représentation de Lewis et la géométrie moléculaire.

---

## La liaison covalente

### Définition

Une **liaison covalente** est la mise en commun de **deux électrons** (un doublet d'électrons) entre deux atomes. Chaque atome apporte un électron au doublet partagé (en général).

> En formant une liaison covalente, chaque atome augmente d'un électron le nombre d'électrons « autour de lui » et se rapproche ainsi de la configuration du gaz noble le plus proche.

### Exemple fondamental : la molécule de dihydrogène $H_2$

- L'atome d'hydrogène $H$ ($Z = 1$) possède **1 seul électron** sur la couche K.
- Pour atteindre la configuration de l'hélium (K)$^2$, il lui faut **2 électrons** (règle du duet).
- Deux atomes d'hydrogène mettent **chacun 1 électron** en commun :

$$H \\cdot + \\cdot H \\longrightarrow H - H$$

- Le trait « $-$ » représente le **doublet liant** (2 électrons partagés).
- Chaque atome H « voit » alors 2 électrons autour de lui → couche K saturée → **stable**.

### Types de liaisons covalentes

| Type | Doublets liants partagés | Notation | Exemple |
|------|--------------------------|----------|---------|
| Liaison **simple** | 1 doublet (2 é) | $-$ | $H-H$, $C-H$, $O-H$ |
| Liaison **double** | 2 doublets (4 é) | $=$ | $O=O$, $C=O$ |
| Liaison **triple** | 3 doublets (6 é) | $\\equiv$ | $N \\equiv N$ |

> Plus le nombre de doublets liants est élevé, plus la liaison est **courte** et **forte** (énergie de liaison plus grande).

---

## Doublets liants et doublets non liants

### Doublet liant

Un **doublet liant** est une paire d'électrons **partagée** entre deux atomes. Il constitue la liaison covalente et est représenté par un **trait** entre les deux atomes.

### Doublet non liant (paire libre)

Un **doublet non liant** est une paire d'électrons localisée sur **un seul atome**, qui ne participe pas à une liaison. Il est représenté par un **trait** (ou deux points) sur l'atome.

> **Exemple :** dans l'eau $H_2O$, l'oxygène possède 2 doublets liants (avec les deux H) et 2 doublets non liants.

---

## Nombre de liaisons d'un atome

Pour satisfaire la règle de l'octet (ou du duet), chaque atome forme un nombre précis de liaisons covalentes :

$$\\text{Nombre de liaisons} = 8 - \\text{nombre d'électrons de valence}$$

(pour les atomes de la période 2 et 3 ; pour l'hydrogène : $2 - 1 = 1$)

| Atome | $Z$ | Électrons de valence | Liaisons | Doublets non liants |
|-------|-----|---------------------|----------|---------------------|
| $H$ | 1 | 1 | **1** | 0 |
| $C$ | 6 | 4 | **4** | 0 |
| $N$ | 7 | 5 | **3** | 1 |
| $O$ | 8 | 6 | **2** | 2 |
| $F$ | 9 | 7 | **1** | 3 |
| $Cl$ | 17 | 7 | **1** | 3 |

> **Moyen mnémotechnique :** « HONC 1234 » → l'Hydrogène forme **1** liaison, l'Oxygène **2**, l'Azote (N) **3**, le Carbone **4**.

---

## Le schéma de Lewis

### Définition

Le **schéma de Lewis** (ou représentation de Lewis) d'une molécule montre :
- Tous les **doublets liants** (traits entre atomes)
- Tous les **doublets non liants** (traits sur les atomes)

### Méthode de construction

1. **Identifier** les atomes et compter le total d'électrons de valence de la molécule.
2. **Placer** l'atome central (celui qui forme le plus de liaisons, en général pas H).
3. **Relier** les atomes par des liaisons simples.
4. **Compléter** les octets en ajoutant des doublets non liants.
5. Si des atomes n'ont pas leur octet → transformer des doublets non liants en **liaisons multiples**.

### Exemples de schémas de Lewis

#### Eau $H_2O$ (total : $2 \\times 1 + 6 = 8$ électrons de valence, soit 4 doublets)

L'oxygène est l'atome central :
- 2 liaisons $O-H$ (2 doublets liants)
- 2 doublets non liants sur O

> L'oxygène a $2 + 2 \\times 2 = 6$… plus exactement : 2 doublets liants + 2 doublets non liants = 4 doublets = 8 électrons autour de O → **octet satisfait** ✓

#### Ammoniac $NH_3$ (total : $5 + 3 \\times 1 = 8$ é de valence, soit 4 doublets)

L'azote est l'atome central :
- 3 liaisons $N-H$ (3 doublets liants)
- 1 doublet non liant sur N

> L'azote est entouré de $3 + 1 = 4$ doublets = 8 électrons → **octet satisfait** ✓

#### Méthane $CH_4$ (total : $4 + 4 \\times 1 = 8$ é de valence, soit 4 doublets)

Le carbone est l'atome central :
- 4 liaisons $C-H$ (4 doublets liants)
- 0 doublet non liant sur C

> Le carbone est entouré de 4 doublets liants = 8 électrons → **octet satisfait** ✓

#### Dioxygène $O_2$ (total : $2 \\times 6 = 12$ é de valence, soit 6 doublets)

- 1 liaison double $O=O$ (2 doublets liants)
- 2 doublets non liants sur chaque O

> Chaque oxygène est entouré de $2 + 2 = 4$ doublets = 8 électrons → **octet satisfait** ✓

#### Diazote $N_2$ (total : $2 \\times 5 = 10$ é de valence, soit 5 doublets)

- 1 liaison triple $N \\equiv N$ (3 doublets liants)
- 1 doublet non liant sur chaque N

> Chaque azote est entouré de $3 + 1 = 4$ doublets = 8 électrons → **octet satisfait** ✓

#### Dioxyde de carbone $CO_2$ (total : $4 + 2 \\times 6 = 16$ é de valence, soit 8 doublets)

- 2 liaisons doubles $O=C=O$ (4 doublets liants)
- 2 doublets non liants sur chaque O

> Le carbone : $2 \\times 2 = 4$ doublets = 8 é → ✓ ; chaque oxygène : $2 + 2 = 4$ doublets = 8 é → ✓

---

## Formule brute et formule développée

| Représentation | Notation | Exemple ($C_2H_6O$, éthanol) |
|---------------|----------|-------------------------------|
| **Formule brute** | Nombre d'atomes de chaque élément | $C_2H_6O$ |
| **Formule développée** | Tous les doublets liants et non liants | Tous les traits $C-C$, $C-H$, $C-O$, $O-H$ visibles |
| **Formule semi-développée** | Liaisons $C-C$, $C-O$, $C=O$ visibles, liaisons $C-H$ implicites | $CH_3-CH_2-OH$ |

> La formule développée est le schéma de Lewis complet de la molécule.

---

## Géométrie des molécules — modèle VSEPR simplifié

La **forme** d'une molécule dépend de la répulsion entre les doublets d'électrons (liants et non liants) autour de l'atome central. Les doublets s'éloignent le plus possible les uns des autres.

| Doublets autour de l'atome central | Géométrie | Angle(s) approximatif(s) | Exemple |
|-------------------------------------|-----------|--------------------------|---------|
| 2 (liants) | **Linéaire** | 180° | $CO_2$ |
| 3 (dont 0 non liant) | **Triangulaire plane** | 120° | $BH_3$ |
| 3 (dont 1 non liant) | **Coudée (V)** | $\\approx 120°$ | $SO_2$ |
| 4 (dont 0 non liant) | **Tétraédrique** | 109,5° | $CH_4$ |
| 4 (dont 1 non liant) | **Pyramidale** | $\\approx 107°$ | $NH_3$ |
| 4 (dont 2 non liants) | **Coudée (V)** | $\\approx 104{,}5°$ | $H_2O$ |

> **Point important :** les doublets non liants « prennent plus de place » que les doublets liants, ce qui réduit légèrement l'angle entre les liaisons.

---

## Molécules polaires et apolaires

### Liaison polarisée

Lorsque deux atomes d'**électronégativités différentes** sont liés, le doublet liant est attiré vers l'atome le plus électronégatif. La liaison est dite **polarisée**.

On note par $\\delta^+$ l'atome le moins électronégatif et $\\delta^-$ l'atome le plus électronégatif.

> **Exemple :** dans $H-Cl$, le chlore ($\\chi = 3{,}2$) est plus électronégatif que l'hydrogène ($\\chi = 2{,}2$) → $H^{\\delta+}-Cl^{\\delta-}$.

### Molécule polaire vs apolaire

- Une molécule est **polaire** si la répartition des charges n'est pas symétrique → il existe un **moment dipolaire** non nul (ex : $H_2O$, $HCl$, $NH_3$).
- Une molécule est **apolaire** si la géométrie est symétrique et que les polarités se compensent (ex : $CO_2$ linéaire, $CH_4$ tétraédrique).

---

## À retenir

- Une **liaison covalente** = mise en commun de 2 électrons entre deux atomes.
- **Règle HONC 1234 :** H forme 1 liaison, O en forme 2, N en forme 3, C en forme 4.
- Le **schéma de Lewis** montre tous les doublets (liants et non liants) de la molécule.
- La géométrie d'une molécule dépend du nombre de doublets autour de l'atome central (modèle VSEPR).
- Une liaison entre deux atomes d'électronégativités différentes est **polarisée**.
""",
                'quiz': {
                    'titre': 'Quiz — Molécules et liaison covalente',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Une liaison covalente correspond à :",
                            'options': ["La mise en commun de 2 électrons entre deux atomes", "Le transfert d'un électron d'un atome à un autre", "L'attraction entre un cation et un anion", "La perte de neutrons par un noyau"],
                            'reponse_correcte': '0',
                            'explication': "Une liaison covalente est la mise en commun de 2 électrons (un doublet) entre deux atomes, chacun contribuant en général un électron.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Combien de liaisons covalentes le carbone C forme-t-il ?",
                            'options': ["4", "2", "3", "1"],
                            'reponse_correcte': '0',
                            'explication': "Le carbone a 4 électrons de valence et forme 4 liaisons covalentes pour compléter son octet (règle HONC 1234 : C = 4).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Combien de liaisons covalentes l'hydrogène H forme-t-il ?",
                            'options': ["1", "2", "3", "4"],
                            'reponse_correcte': '0',
                            'explication': "L'hydrogène a 1 électron de valence et forme 1 seule liaison pour atteindre la configuration de l'hélium (règle du duet).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Qu'est-ce qu'un doublet non liant ?",
                            'options': ["Une paire d'électrons localisée sur un seul atome, ne participant pas à une liaison", "Une paire d'électrons partagée entre deux atomes", "Un proton libre dans une molécule", "Une liaison entre trois atomes"],
                            'reponse_correcte': '0',
                            'explication': "Un doublet non liant (paire libre) est une paire d'électrons appartenant à un seul atome, qui ne participe pas à une liaison covalente.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Combien de doublets non liants possède l'oxygène dans la molécule d'eau H₂O ?",
                            'options': ["2", "0", "1", "3"],
                            'reponse_correcte': '0',
                            'explication': "L'oxygène a 6 électrons de valence. 2 sont engagés dans 2 liaisons O−H (2 doublets liants), les 4 restants forment 2 doublets non liants.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Dans le schéma de Lewis de la molécule de méthane CH₄, combien de doublets liants trouve-t-on ?",
                            'options': ["4", "2", "3", "8"],
                            'reponse_correcte': '0',
                            'explication': "Le méthane possède 4 liaisons C−H, donc 4 doublets liants. Le carbone n'a aucun doublet non liant.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "La molécule de diazote N₂ possède une liaison :",
                            'options': ["Triple", "Simple", "Double", "Quadruple"],
                            'reponse_correcte': '0',
                            'explication': "L'azote a 5 électrons de valence et forme 3 liaisons. Dans N₂, les deux atomes partagent 3 doublets → liaison triple N≡N.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Que signifie le moyen mnémotechnique « HONC 1234 » ?",
                            'options': ["H forme 1 liaison, O forme 2, N forme 3, C forme 4", "H a 1 proton, O en a 2, N en a 3, C en a 4", "H a 1 couche, O en a 2, N en a 3, C en a 4", "H pèse 1 g, O pèse 2 g, N pèse 3 g, C pèse 4 g"],
                            'reponse_correcte': '0',
                            'explication': "HONC 1234 résume le nombre de liaisons covalentes typiques : H = 1, O = 2, N = 3, C = 4.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "La géométrie de la molécule de méthane CH₄ est :",
                            'options': ["Tétraédrique", "Linéaire", "Triangulaire plane", "Pyramidale"],
                            'reponse_correcte': '0',
                            'explication': "Le carbone est entouré de 4 doublets liants (0 non liant) → géométrie tétraédrique avec des angles de 109,5°.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quelle est la géométrie de la molécule d'eau H₂O ?",
                            'options': ["Coudée (V)", "Linéaire", "Tétraédrique", "Triangulaire plane"],
                            'reponse_correcte': '0',
                            'explication': "L'oxygène a 4 doublets (2 liants + 2 non liants). Les 2 doublets non liants compriment l'angle → géométrie coudée (V), angle ≈ 104,5°.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Quelle est la géométrie de la molécule d'ammoniac NH₃ ?",
                            'options': ["Pyramidale", "Triangulaire plane", "Linéaire", "Tétraédrique"],
                            'reponse_correcte': '0',
                            'explication': "L'azote a 4 doublets (3 liants + 1 non liant). Le doublet non liant déforme la géométrie → pyramide à base triangulaire, angle ≈ 107°.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "La molécule de CO₂ a une géométrie :",
                            'options': ["Linéaire", "Coudée", "Tétraédrique", "Pyramidale"],
                            'reponse_correcte': '0',
                            'explication': "Le carbone dans CO₂ est entouré de 2 doubles liaisons (2 directions) et 0 doublet non liant → géométrie linéaire, angle = 180°.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Dans la molécule de dioxygène O₂, combien de doublets liants trouve-t-on entre les deux atomes d'oxygène ?",
                            'options': ["2 (liaison double)", "1 (liaison simple)", "3 (liaison triple)", "4"],
                            'reponse_correcte': '0',
                            'explication': "Dans O₂, les deux atomes d'oxygène partagent 2 doublets liants, formant une liaison double O=O.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Une liaison est dite polarisée lorsque :",
                            'options': ["Les deux atomes liés ont des électronégativités différentes", "Les deux atomes ont le même nombre de protons", "La liaison est triple", "Les deux atomes sont des métaux"],
                            'reponse_correcte': '0',
                            'explication': "Quand deux atomes liés ont des électronégativités différentes, le doublet liant est attiré vers l'atome le plus électronégatif → liaison polarisée.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "La molécule de CO₂ est polaire car elle contient des liaisons C=O polarisées.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Bien que les liaisons C=O soient polarisées, la géométrie linéaire de CO₂ fait que les polarités se compensent exactement. La molécule est donc apolaire.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Plus une liaison covalente est multiple (double, triple), plus elle est courte et forte.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Une liaison double est plus courte et plus forte qu'une simple, et une triple encore davantage, car plus d'électrons sont partagés entre les atomes.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "L'azote N dans la molécule NH₃ possède un doublet non liant.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "L'azote a 5 électrons de valence. 3 participent à des liaisons N−H, les 2 restants forment 1 doublet non liant.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Combien de doublets (liants + non liants) au total possède la molécule d'eau H₂O dans son schéma de Lewis ?",
                            'options': None,
                            'reponse_correcte': '4',
                            'tolerances': ['quatre', '4 doublets'],
                            'explication': "H₂O a 8 électrons de valence (2×1 + 6) soit 4 doublets : 2 doublets liants (O−H) et 2 doublets non liants sur O.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Quel est l'angle approximatif entre les liaisons dans une molécule tétraédrique (en degrés) ?",
                            'options': None,
                            'reponse_correcte': '109.5',
                            'tolerances': ['109,5', '109', '109.5°', '109,5°'],
                            'explication': "La géométrie tétraédrique (4 doublets liants, 0 non liant) correspond à un angle de 109,5° entre chaque liaison.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quelle est la formule semi-développée de l'éthanol ?",
                            'options': None,
                            'reponse_correcte': 'CH3-CH2-OH',
                            'tolerances': ['CH₃-CH₂-OH', 'CH3CH2OH', 'C2H5OH', 'CH3-CH2OH'],
                            'explication': "L'éthanol (C₂H₆O) a pour formule semi-développée CH₃−CH₂−OH.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 5 — La mole et les quantités de matière
    # ──────────────────────────────────────────────
    {
        'ordre': 5,
        'titre': 'La mole et les quantités de matière',
        'description': "Maîtriser le concept de mole, la constante d'Avogadro, la masse molaire et les calculs de quantité de matière (solides, liquides, gaz).",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "La mole et le nombre d'Avogadro",
                'duree': 35,
                'contenu': """# La mole et le nombre d'Avogadro

## Introduction — pourquoi la mole ?

Les entités chimiques (atomes, molécules, ions) sont **incroyablement petites** et **incroyablement nombreuses** dans un échantillon de matière ordinaire. Un simple verre d'eau ($\\approx 200$ mL) contient environ $6{,}7 \\times 10^{24}$ molécules d'eau ! Manipuler directement ces nombres gigantesques serait impraticable.

Les chimistes ont donc inventé une **unité de comptage** adaptée à l'échelle atomique : la **mole**.

> **Analogie :** de même qu'on utilise la « douzaine » pour compter les œufs (1 douzaine = 12 œufs), on utilise la « mole » pour compter les entités chimiques. Mais une mole représente un nombre **considérablement** plus grand !

---

## La mole — définition

### Définition officielle (SI, 2019)

La **mole** (symbole : $\\text{mol}$) est l'unité de **quantité de matière**. Une mole contient exactement :

$$N_A = 6{,}022 \\, 140 \\, 76 \\times 10^{23} \\text{ entités}$$

Ce nombre est la **constante d'Avogadro**, notée $N_A$.

> En pratique, on utilise la valeur arrondie : $N_A \\approx 6{,}02 \\times 10^{23} \\text{ mol}^{-1}$.

### Signification concrète

- 1 mole d'atomes de carbone = $6{,}02 \\times 10^{23}$ atomes de carbone
- 1 mole de molécules d'eau = $6{,}02 \\times 10^{23}$ molécules de $H_2O$
- 1 mole d'ions sodium = $6{,}02 \\times 10^{23}$ ions $Na^+$
- 0,5 mole de molécules de dioxygène = $0{,}5 \\times 6{,}02 \\times 10^{23} = 3{,}01 \\times 10^{23}$ molécules de $O_2$

> **Important :** la mole s'applique à **n'importe quel type d'entité** (atomes, molécules, ions, électrons), mais il faut toujours **préciser** le type d'entité.

---

## Relation entre quantité de matière et nombre d'entités

La **quantité de matière** $n$ (en mol) d'un échantillon est liée au nombre d'entités $N$ par :

$$\\boxed{n = \\frac{N}{N_A}}$$

ou de manière équivalente :

$$N = n \\times N_A$$

| Grandeur | Symbole | Unité |
|----------|---------|-------|
| Quantité de matière | $n$ | mol |
| Nombre d'entités | $N$ | sans unité (nombre pur) |
| Constante d'Avogadro | $N_A$ | $\\text{mol}^{-1}$ |

### Exemples de calculs

#### Exemple 1 : nombre de molécules dans 2 moles d'eau

$$N = n \\times N_A = 2 \\times 6{,}02 \\times 10^{23} = 1{,}204 \\times 10^{24} \\text{ molécules}$$

#### Exemple 2 : quantité de matière de $3{,}01 \\times 10^{22}$ atomes de fer

$$n = \\frac{N}{N_A} = \\frac{3{,}01 \\times 10^{22}}{6{,}02 \\times 10^{23}} = 0{,}050 \\text{ mol} = 5{,}0 \\times 10^{-2} \\text{ mol}$$

---

## Ordre de grandeur du nombre d'Avogadro

Pour apprécier l'immensité de $N_A$ :

- Si l'on comptait 1 milliard d'entités par seconde ($10^9$/s), il faudrait **19 millions d'années** pour compter une mole.
- Une mole de grains de sable ($\\approx 1$ mm chacun) recouvrirait la surface de la France sur une épaisseur de **plus d'un kilomètre**.
- Une mole d'eau ($18$ g) tient dans une cuillère à soupe, mais contient $6{,}02 \\times 10^{23}$ molécules.

> Ces exemples illustrent le fossé d'échelle entre le monde macroscopique (ce que l'on voit) et le monde microscopique (les atomes et molécules).

---

## Quantité de matière et échantillon macroscopique

### Le lien micro–macro

La mole est le **pont** entre les deux échelles :

| Échelle microscopique | Pont | Échelle macroscopique |
|----------------------|------|----------------------|
| Nombre d'entités $N$ | $N_A$ | Quantité de matière $n$ (mol) |
| Masse d'une entité | $N_A$ | Masse molaire $M$ (g/mol) |
| Volume d'une entité (gaz) | $N_A$ | Volume molaire $V_m$ (L/mol) |

> Connaître $n$ permet de calculer la **masse** ou le **volume** d'un échantillon, et réciproquement. C'est l'objet de la leçon suivante.

---

## Exercices types

### Exercice 1

**Énoncé :** Combien de molécules contient un échantillon de $0{,}25$ mol de glucose $C_6H_{12}O_6$ ?

**Résolution :**

$$N = n \\times N_A = 0{,}25 \\times 6{,}02 \\times 10^{23} = 1{,}505 \\times 10^{23} \\text{ molécules}$$

soit environ $1{,}5 \\times 10^{23}$ molécules.

### Exercice 2

**Énoncé :** Un échantillon contient $1{,}806 \\times 10^{24}$ ions $Cl^-$. Quelle est la quantité de matière en ions chlorure ?

**Résolution :**

$$n = \\frac{N}{N_A} = \\frac{1{,}806 \\times 10^{24}}{6{,}02 \\times 10^{23}} = 3{,}00 \\text{ mol}$$

### Exercice 3

**Énoncé :** Une mole de fer contient-elle le même nombre d'entités qu'une mole d'eau ?

**Réponse :** **Oui.** Par définition, une mole de n'importe quelle entité contient toujours $N_A = 6{,}02 \\times 10^{23}$ entités. La nature de l'entité (atome de fer ou molécule d'eau) ne change rien au nombre.

---

## À retenir

- La **mole** est l'unité de quantité de matière ; elle contient $N_A = 6{,}02 \\times 10^{23}$ entités.
- La relation fondamentale est $n = \\frac{N}{N_A}$.
- $N_A$ est la **constante d'Avogadro** : le lien entre le monde microscopique (entités) et macroscopique (moles).
- Il faut toujours préciser la **nature** de l'entité comptée (atomes, molécules, ions…).
""",
                'quiz': {
                    'titre': 'Quiz — La mole et le nombre d\'Avogadro',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Que représente la constante d'Avogadro ?",
                            'options': ["Le nombre d'entités contenues dans une mole", "La masse d'une mole d'atomes", "Le volume d'une mole de gaz", "La charge d'un électron"],
                            'reponse_correcte': '0',
                            'explication': "La constante d'Avogadro Nₐ = 6,02 × 10²³ mol⁻¹ représente le nombre d'entités contenues dans une mole de n'importe quelle espèce chimique.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quelle est la valeur (arrondie) de la constante d'Avogadro ?",
                            'options': ["6,02 × 10²³ mol⁻¹", "6,02 × 10²² mol⁻¹", "3,00 × 10²³ mol⁻¹", "6,02 × 10²⁴ mol⁻¹"],
                            'reponse_correcte': '0',
                            'explication': "Nₐ ≈ 6,02 × 10²³ mol⁻¹. C'est la valeur à retenir pour les calculs de quantité de matière.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Quelle formule relie la quantité de matière n au nombre d'entités N ?",
                            'options': ["n = N / Nₐ", "n = N × Nₐ", "n = Nₐ / N", "n = N + Nₐ"],
                            'reponse_correcte': '0',
                            'explication': "La relation fondamentale est n = N / Nₐ, où n est en mol, N le nombre d'entités et Nₐ la constante d'Avogadro.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Combien de molécules contient 1 mole d'eau ?",
                            'options': ["6,02 × 10²³", "12,04 × 10²³", "3,01 × 10²³", "6,02 × 10²²"],
                            'reponse_correcte': '0',
                            'explication': "Par définition, 1 mole contient Nₐ = 6,02 × 10²³ entités, quelle que soit la nature de l'entité.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La mole est l'unité de :",
                            'options': ["Quantité de matière", "Masse", "Volume", "Nombre d'entités"],
                            'reponse_correcte': '0',
                            'explication': "La mole (mol) est l'unité SI de la grandeur 'quantité de matière'.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Une mole d'atomes de fer contient-elle le même nombre d'entités qu'une mole de molécules d'eau ?",
                            'options': ["Oui, toujours Nₐ entités", "Non, cela dépend de la masse", "Non, cela dépend du volume", "Oui, mais seulement aux CNTP"],
                            'reponse_correcte': '0',
                            'explication': "Par définition, 1 mole de n'importe quelle entité contient exactement Nₐ entités. La nature (atome, molécule, ion) ne change pas ce nombre.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Combien de molécules contient 0,5 mol de dioxygène O₂ ?",
                            'options': ["3,01 × 10²³", "6,02 × 10²³", "1,20 × 10²⁴", "3,01 × 10²²"],
                            'reponse_correcte': '0',
                            'explication': "N = n × Nₐ = 0,5 × 6,02 × 10²³ = 3,01 × 10²³ molécules.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Quelle est l'unité de la constante d'Avogadro ?",
                            'options': ["mol⁻¹", "mol", "g/mol", "sans unité"],
                            'reponse_correcte': '0',
                            'explication': "Nₐ s'exprime en mol⁻¹ (nombre d'entités par mole).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Un échantillon contient 1,204 × 10²⁴ molécules de CO₂. Quelle est sa quantité de matière ?",
                            'options': ["2,0 mol", "1,0 mol", "0,5 mol", "20 mol"],
                            'reponse_correcte': '0',
                            'explication': "n = N / Nₐ = 1,204 × 10²⁴ / 6,02 × 10²³ = 2,0 mol.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quelle quantité de matière correspond à 3,01 × 10²² atomes de carbone ?",
                            'options': ["0,050 mol", "0,50 mol", "5,0 mol", "0,0050 mol"],
                            'reponse_correcte': '0',
                            'explication': "n = N / Nₐ = 3,01 × 10²² / 6,02 × 10²³ = 0,050 mol.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "On dispose de 0,25 mol de glucose. Combien de molécules cela représente-t-il ?",
                            'options': ["1,505 × 10²³", "6,02 × 10²³", "2,408 × 10²⁴", "1,505 × 10²²"],
                            'reponse_correcte': '0',
                            'explication': "N = n × Nₐ = 0,25 × 6,02 × 10²³ = 1,505 × 10²³ molécules.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Pourquoi les chimistes utilisent-ils la mole plutôt que de compter directement les entités ?",
                            'options': ["Parce que le nombre d'entités dans un échantillon est gigantesque et impraticable à manipuler", "Parce que les entités sont trop grosses pour être comptées", "Parce que la mole est une unité de volume", "Parce que les atomes n'existent pas individuellement"],
                            'reponse_correcte': '0',
                            'explication': "Un échantillon ordinaire contient des milliards de milliards d'entités. La mole est une unité de comptage adaptée à ces nombres gigantesques.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Un échantillon contient 9,03 × 10²³ ions Na⁺. Quelle est la quantité de matière ?",
                            'options': ["1,5 mol", "1,0 mol", "0,15 mol", "15 mol"],
                            'reponse_correcte': '0',
                            'explication': "n = N / Nₐ = 9,03 × 10²³ / 6,02 × 10²³ = 1,5 mol.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Si l'on double la quantité de matière d'un échantillon, le nombre d'entités :",
                            'options': ["Double également", "Reste le même", "Est divisé par deux", "Est multiplié par Nₐ"],
                            'reponse_correcte': '0',
                            'explication': "N = n × Nₐ. Si n double, N double aussi (Nₐ étant une constante).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Une mole de molécules d'eau et une mole d'atomes de fer contiennent le même nombre d'entités.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "Par définition, 1 mole contient toujours Nₐ = 6,02 × 10²³ entités, quelle que soit la nature de l'entité.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La constante d'Avogadro dépend de la nature de l'espèce chimique considérée.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "Nₐ est une constante universelle. Sa valeur (6,02 × 10²³ mol⁻¹) est la même quelle que soit l'espèce chimique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "La quantité de matière n s'exprime en grammes.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "La quantité de matière n s'exprime en moles (mol). C'est la masse m qui s'exprime en grammes.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer la quantité de matière (en mol) d'un échantillon contenant 1,806 × 10²⁴ ions Cl⁻. Donner la valeur numérique.",
                            'options': None,
                            'reponse_correcte': '3',
                            'tolerances': ['3,0', '3.0', '3,00', '3.00', '3 mol'],
                            'explication': "n = N / Nₐ = 1,806 × 10²⁴ / 6,02 × 10²³ = 3,00 mol.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment s'appelle la grandeur qui mesure le nombre de moles d'une espèce chimique dans un échantillon ?",
                            'options': None,
                            'reponse_correcte': 'quantité de matière',
                            'tolerances': ['quantite de matiere', 'la quantité de matière', 'la quantite de matiere'],
                            'explication': "La quantité de matière (symbole n, unité mol) est la grandeur qui permet de dénombrer les entités chimiques à l'échelle macroscopique.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Un échantillon contient 0,10 mol de molécules de diazote N₂. Combien de molécules contient-il ? Donner la réponse sous la forme a × 10²² (valeur de a × 10²²).",
                            'options': None,
                            'reponse_correcte': '6,02 × 10²²',
                            'tolerances': ['6.02 × 10²²', '6,02 x 10^22', '6.02 x 10^22', '6,02e22', '6.02e22'],
                            'explication': "N = n × Nₐ = 0,10 × 6,02 × 10²³ = 6,02 × 10²² molécules.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Masse molaire et volume molaire',
                'duree': 40,
                'contenu': """# Masse molaire et volume molaire

## Introduction

La mole permet de « compter » les entités chimiques, mais au laboratoire on ne compte pas les atomes un par un : on mesure des **masses** (avec une balance) et des **volumes** (avec de la verrerie). Il faut donc relier la quantité de matière $n$ à la masse $m$ et au volume $V$. C'est le rôle de la **masse molaire** et du **volume molaire**.

---

## Masse molaire atomique

### Définition

La **masse molaire atomique** $M$ d'un élément est la masse d'**une mole d'atomes** de cet élément. Elle s'exprime en **grammes par mole** ($\\text{g/mol}$ ou $\\text{g} \\cdot \\text{mol}^{-1}$).

> La valeur numérique de $M$ est donnée dans le tableau périodique : c'est la **masse atomique relative** de l'élément.

### Exemples

| Élément | Symbole | $M$ (g/mol) |
|---------|---------|-------------|
| Hydrogène | $H$ | 1,0 |
| Carbone | $C$ | 12,0 |
| Azote | $N$ | 14,0 |
| Oxygène | $O$ | 16,0 |
| Sodium | $Na$ | 23,0 |
| Soufre | $S$ | 32,1 |
| Chlore | $Cl$ | 35,5 |
| Fer | $Fe$ | 55,8 |
| Cuivre | $Cu$ | 63,5 |

> **Signification :** $M_C = 12{,}0$ g/mol signifie qu'une mole d'atomes de carbone ($6{,}02 \\times 10^{23}$ atomes) a une masse de 12,0 g.

---

## Masse molaire moléculaire

### Définition

La **masse molaire moléculaire** d'une molécule est la masse d'**une mole de molécules**. Elle se calcule en additionnant les masses molaires atomiques de tous les atomes qui composent la molécule.

### Méthode de calcul

Pour une molécule de formule brute $X_a Y_b Z_c$ :

$$M_{X_a Y_b Z_c} = a \\times M_X + b \\times M_Y + c \\times M_Z$$

### Exemples détaillés

#### Eau $H_2O$

$$M_{H_2O} = 2 \\times M_H + 1 \\times M_O = 2 \\times 1{,}0 + 16{,}0 = 18{,}0 \\text{ g/mol}$$

> Une mole d'eau (environ 18 mL, soit une cuillère à soupe) a une masse de 18,0 g.

#### Dioxyde de carbone $CO_2$

$$M_{CO_2} = 1 \\times M_C + 2 \\times M_O = 12{,}0 + 2 \\times 16{,}0 = 44{,}0 \\text{ g/mol}$$

#### Glucose $C_6H_{12}O_6$

$$M_{C_6H_{12}O_6} = 6 \\times 12{,}0 + 12 \\times 1{,}0 + 6 \\times 16{,}0 = 72{,}0 + 12{,}0 + 96{,}0 = 180{,}0 \\text{ g/mol}$$

#### Acide sulfurique $H_2SO_4$

$$M_{H_2SO_4} = 2 \\times 1{,}0 + 32{,}1 + 4 \\times 16{,}0 = 2{,}0 + 32{,}1 + 64{,}0 = 98{,}1 \\text{ g/mol}$$

---

## Relation masse – quantité de matière

### Formule fondamentale

$$\\boxed{n = \\frac{m}{M}}$$

ou de manière équivalente :

$$m = n \\times M \\qquad \\text{et} \\qquad M = \\frac{m}{n}$$

| Grandeur | Symbole | Unité |
|----------|---------|-------|
| Quantité de matière | $n$ | mol |
| Masse | $m$ | g |
| Masse molaire | $M$ | g/mol |

### Exemples de calculs

#### Exemple 1 : quelle quantité de matière dans 36,0 g d'eau ?

$$n = \\frac{m}{M} = \\frac{36{,}0}{18{,}0} = 2{,}00 \\text{ mol}$$

#### Exemple 2 : quelle masse pour 0,50 mol de glucose ?

$$m = n \\times M = 0{,}50 \\times 180{,}0 = 90{,}0 \\text{ g}$$

#### Exemple 3 : quelle est la masse molaire d'un composé si 4,40 g correspondent à 0,10 mol ?

$$M = \\frac{m}{n} = \\frac{4{,}40}{0{,}10} = 44{,}0 \\text{ g/mol}$$

> On reconnaît la masse molaire du $CO_2$.

---

## Volume molaire des gaz

### Constat expérimental — loi d'Avogadro

À **température** et **pression** identiques, des volumes égaux de gaz différents contiennent le **même nombre de molécules** (et donc le même nombre de moles).

> **Conséquence :** une mole de **n'importe quel gaz** occupe le **même volume** dans des conditions données. Ce volume est appelé **volume molaire** $V_m$.

### Définition

Le **volume molaire** $V_m$ est le volume occupé par **une mole de gaz** dans des conditions de température et de pression données.

### Valeurs de référence

| Conditions | Température | Pression | $V_m$ |
|-----------|-------------|----------|-------|
| Conditions normales de température et de pression (CNTP) | $0$ °C ($273{,}15$ K) | $1{,}013 \\times 10^5$ Pa ($1$ atm) | $22{,}4$ L/mol |
| Conditions ambiantes | $20$ °C ($293$ K) | $1{,}013 \\times 10^5$ Pa | $\\approx 24{,}0$ L/mol |
| Conditions ambiantes | $25$ °C ($298$ K) | $1{,}013 \\times 10^5$ Pa | $\\approx 24{,}5$ L/mol |

> **Point crucial :** le volume molaire dépend de la **température** et de la **pression**, mais **pas de la nature du gaz**. C'est la même valeur pour $O_2$, $N_2$, $CO_2$, $H_2$, etc.

### Relation volume – quantité de matière (gaz uniquement)

$$\\boxed{n = \\frac{V}{V_m}}$$

ou de manière équivalente :

$$V = n \\times V_m$$

| Grandeur | Symbole | Unité |
|----------|---------|-------|
| Quantité de matière | $n$ | mol |
| Volume du gaz | $V$ | L |
| Volume molaire | $V_m$ | L/mol |

### Exemples de calculs

#### Exemple 1 : quel volume occupe 0,50 mol de $CO_2$ à 20 °C et 1 atm ?

$$V = n \\times V_m = 0{,}50 \\times 24{,}0 = 12{,}0 \\text{ L}$$

#### Exemple 2 : quelle quantité de matière dans 4,48 L de $O_2$ aux CNTP ?

$$n = \\frac{V}{V_m} = \\frac{4{,}48}{22{,}4} = 0{,}200 \\text{ mol}$$

---

## Masse volumique et quantité de matière (liquides et solides)

Pour les **liquides** et les **solides**, on utilise la **masse volumique** $\\rho$ (ou la densité $d$) pour passer du volume à la masse, puis on calcule $n$ :

### Méthode en deux étapes

1. Calculer la masse : $m = \\rho \\times V$
2. Calculer la quantité de matière : $n = \\frac{m}{M}$

Ou en une seule formule :

$$n = \\frac{\\rho \\times V}{M}$$

### Exemple : quantité de matière dans 100 mL d'éthanol pur

Données : $\\rho_{\\text{éthanol}} = 0{,}789$ g/mL, $M_{C_2H_6O} = 46{,}0$ g/mol

$$m = \\rho \\times V = 0{,}789 \\times 100 = 78{,}9 \\text{ g}$$

$$n = \\frac{m}{M} = \\frac{78{,}9}{46{,}0} = 1{,}72 \\text{ mol}$$

---

## Tableau récapitulatif des formules

| Situation | Formule | Grandeurs |
|-----------|---------|-----------|
| Compter les entités | $n = \\frac{N}{N_A}$ | $N$ : nombre d'entités, $N_A = 6{,}02 \\times 10^{23}$ |
| Peser un solide/liquide | $n = \\frac{m}{M}$ | $m$ : masse (g), $M$ : masse molaire (g/mol) |
| Mesurer un volume de gaz | $n = \\frac{V}{V_m}$ | $V$ : volume (L), $V_m$ : volume molaire (L/mol) |
| Volume et masse volumique | $n = \\frac{\\rho \\times V}{M}$ | $\\rho$ : masse volumique (g/mL ou g/L) |

---

## À retenir

- La **masse molaire** moléculaire est la somme des masses molaires atomiques pondérées par le nombre d'atomes.
- $n = \\frac{m}{M}$ relie la quantité de matière à la masse mesurée.
- Le **volume molaire** $V_m$ est le même pour tous les gaz dans des conditions $T$ et $P$ données ($22{,}4$ L/mol aux CNTP, $\\approx 24$ L/mol à 20 °C).
- $n = \\frac{V}{V_m}$ relie la quantité de matière au volume d'un gaz.
- Pour les liquides/solides, on passe par la masse volumique : $n = \\frac{\\rho V}{M}$.
""",
                'quiz': {
                    'titre': 'Quiz — Masse molaire et volume molaire',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Qu'est-ce que la masse molaire atomique ?",
                            'options': ["La masse d'une mole d'atomes d'un élément", "La masse d'un seul atome", "Le nombre d'atomes dans une mole", "Le volume d'une mole d'atomes"],
                            'reponse_correcte': '0',
                            'explication': "La masse molaire atomique M est la masse d'une mole d'atomes d'un élément, exprimée en g/mol.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quelle est la masse molaire de l'eau H₂O ?",
                            'options': ["18,0 g/mol", "16,0 g/mol", "20,0 g/mol", "2,0 g/mol"],
                            'reponse_correcte': '0',
                            'explication': "M(H₂O) = 2 × M(H) + M(O) = 2 × 1,0 + 16,0 = 18,0 g/mol.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Quelle formule permet de calculer la quantité de matière à partir de la masse ?",
                            'options': ["n = m / M", "n = m × M", "n = M / m", "n = m + M"],
                            'reponse_correcte': '0',
                            'explication': "La relation fondamentale est n = m / M, avec m en g et M en g/mol.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Le volume molaire d'un gaz aux CNTP (0 °C, 1 atm) vaut :",
                            'options': ["22,4 L/mol", "24,0 L/mol", "18,0 L/mol", "11,2 L/mol"],
                            'reponse_correcte': '0',
                            'explication': "Aux conditions normales de température et de pression (0 °C, 1 atm), Vm = 22,4 L/mol.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Quelle est la masse molaire du dioxyde de carbone CO₂ ?",
                            'options': ["44,0 g/mol", "28,0 g/mol", "32,0 g/mol", "12,0 g/mol"],
                            'reponse_correcte': '0',
                            'explication': "M(CO₂) = M(C) + 2 × M(O) = 12,0 + 2 × 16,0 = 44,0 g/mol.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Le volume molaire des gaz dépend :",
                            'options': ["De la température et de la pression", "Uniquement de la nature du gaz", "Uniquement de la masse molaire", "De rien, c'est une constante universelle"],
                            'reponse_correcte': '0',
                            'explication': "Le volume molaire Vm dépend de la température et de la pression, mais PAS de la nature du gaz (loi d'Avogadro).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Quelle est la masse molaire du glucose C₆H₁₂O₆ ?",
                            'options': ["180,0 g/mol", "162,0 g/mol", "72,0 g/mol", "342,0 g/mol"],
                            'reponse_correcte': '0',
                            'explication': "M(C₆H₁₂O₆) = 6 × 12,0 + 12 × 1,0 + 6 × 16,0 = 72,0 + 12,0 + 96,0 = 180,0 g/mol.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "L'unité de la masse molaire est :",
                            'options': ["g/mol", "mol/g", "g", "mol"],
                            'reponse_correcte': '0',
                            'explication': "La masse molaire M s'exprime en grammes par mole (g/mol ou g·mol⁻¹).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Quelle quantité de matière représentent 36,0 g d'eau (M = 18,0 g/mol) ?",
                            'options': ["2,00 mol", "0,50 mol", "18,0 mol", "1,00 mol"],
                            'reponse_correcte': '0',
                            'explication': "n = m / M = 36,0 / 18,0 = 2,00 mol.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quel volume occupe 0,50 mol de gaz à 20 °C et 1 atm (Vm = 24,0 L/mol) ?",
                            'options': ["12,0 L", "24,0 L", "48,0 L", "11,2 L"],
                            'reponse_correcte': '0',
                            'explication': "V = n × Vm = 0,50 × 24,0 = 12,0 L.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Quelle masse a 0,50 mol de glucose C₆H₁₂O₆ (M = 180,0 g/mol) ?",
                            'options': ["90,0 g", "180,0 g", "360,0 g", "45,0 g"],
                            'reponse_correcte': '0',
                            'explication': "m = n × M = 0,50 × 180,0 = 90,0 g.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Quelle quantité de matière de O₂ est contenue dans 4,48 L aux CNTP (Vm = 22,4 L/mol) ?",
                            'options': ["0,200 mol", "2,00 mol", "0,448 mol", "0,100 mol"],
                            'reponse_correcte': '0',
                            'explication': "n = V / Vm = 4,48 / 22,4 = 0,200 mol.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "À 20 °C et 1 atm, 1 mole de diazote N₂ et 1 mole de dioxygène O₂ occupent :",
                            'options': ["Le même volume (≈ 24 L)", "Des volumes différents car leurs masses molaires diffèrent", "Le même volume uniquement aux CNTP", "Un volume proportionnel à leur masse molaire"],
                            'reponse_correcte': '0',
                            'explication': "D'après la loi d'Avogadro, à T et P identiques, tous les gaz ont le même volume molaire, quelle que soit leur nature.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "On veut calculer n pour un liquide dont on connaît le volume V, la masse volumique ρ et la masse molaire M. Quelle formule utilise-t-on ?",
                            'options': ["n = ρ × V / M", "n = V / Vm", "n = M / (ρ × V)", "n = V × M / ρ"],
                            'reponse_correcte': '0',
                            'explication': "Pour un liquide : m = ρ × V puis n = m / M, soit n = ρ × V / M.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Le volume molaire Vm est le même pour tous les gaz dans les mêmes conditions de température et de pression.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est la loi d'Avogadro : à T et P données, le volume molaire est identique pour tous les gaz.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La formule n = V / Vm est valable pour les liquides et les solides.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "La formule n = V / Vm n'est valable que pour les GAZ. Pour les liquides et solides, on utilise n = m / M (avec m = ρ × V si nécessaire).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "La masse molaire du carbone est de 12,0 g/mol, ce qui signifie qu'un seul atome de carbone pèse 12,0 g.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "12,0 g/mol est la masse d'UNE MOLE d'atomes de carbone (6,02 × 10²³ atomes), pas d'un seul atome.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer la masse molaire de l'acide sulfurique H₂SO₄ en g/mol. (M_H = 1,0 ; M_S = 32,1 ; M_O = 16,0)",
                            'options': None,
                            'reponse_correcte': '98,1',
                            'tolerances': ['98.1', '98,1 g/mol', '98.1 g/mol'],
                            'explication': "M(H₂SO₄) = 2 × 1,0 + 32,1 + 4 × 16,0 = 2,0 + 32,1 + 64,0 = 98,1 g/mol.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "On dispose de 4,40 g d'un composé dont la masse molaire est 44,0 g/mol. Quelle est la quantité de matière (en mol) ?",
                            'options': None,
                            'reponse_correcte': '0,10',
                            'tolerances': ['0.10', '0,1', '0.1', '0,10 mol', '0.10 mol'],
                            'explication': "n = m / M = 4,40 / 44,0 = 0,10 mol.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quel volume (en L) occupe 2,0 mol de gaz à 20 °C et 1 atm ? (Vm = 24,0 L/mol)",
                            'options': None,
                            'reponse_correcte': '48',
                            'tolerances': ['48,0', '48.0', '48 L', '48,0 L', '48.0 L'],
                            'explication': "V = n × Vm = 2,0 × 24,0 = 48,0 L.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 6 — Les solutions aqueuses
    # ──────────────────────────────────────────────
    {
        'ordre': 6,
        'titre': 'Les solutions aqueuses',
        'description': "Comprendre les notions de soluté, solvant, concentration massique et molaire, préparer une solution par dissolution et dilution.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Concentration massique et concentration molaire',
                'duree': 35,
                'contenu': """# Concentration massique et concentration molaire

## Introduction

Une **solution** est omniprésente au quotidien et au laboratoire : eau salée, sirop, sérum physiologique, acide chlorhydrique dilué… Pour caractériser une solution, il faut connaître sa **concentration**, c'est-à-dire la quantité de substance dissoute dans un volume donné de solution. Il existe deux façons de l'exprimer : en masse et en moles.

---

## Vocabulaire des solutions

### Définitions

| Terme | Définition |
|-------|-----------|
| **Solution** | Mélange homogène obtenu en dissolvant une ou plusieurs espèces chimiques dans un liquide |
| **Solvant** | Espèce chimique **majoritaire** dans la solution (souvent l'eau) |
| **Soluté** | Espèce chimique **dissoute** dans le solvant (minoritaire) |
| **Solution aqueuse** | Solution dont le solvant est l'**eau** |

> **Exemple :** dans l'eau sucrée, le **solvant** est l'eau et le **soluté** est le saccharose (sucre).

### Solution saturée

Une solution est **saturée** lorsque le solvant ne peut plus dissoudre de soluté supplémentaire à une température donnée. Le soluté en excès reste sous forme solide au fond du récipient.

> **Exemple :** à 20 °C, on peut dissoudre au maximum environ 360 g de $NaCl$ dans 1 L d'eau. Au-delà, la solution est saturée.

---

## Concentration massique

### Définition

La **concentration massique** $C_m$ (ou titre massique) d'un soluté en solution est le rapport de la **masse de soluté** dissoute sur le **volume de solution** :

$$\\boxed{C_m = \\frac{m_{\\text{soluté}}}{V_{\\text{solution}}}}$$

| Grandeur | Symbole | Unité |
|----------|---------|-------|
| Concentration massique | $C_m$ | $\\text{g/L}$ (ou g·L⁻¹) |
| Masse de soluté | $m_{\\text{soluté}}$ | $\\text{g}$ |
| Volume de solution | $V_{\\text{solution}}$ | $\\text{L}$ |

> **Attention :** $V$ est le volume de la **solution** (solvant + soluté), pas le volume du solvant seul.

### Exemples de calculs

#### Exemple 1

On dissout $5{,}0$ g de chlorure de sodium dans de l'eau pour obtenir $250$ mL de solution. Quelle est la concentration massique ?

$$C_m = \\frac{m}{V} = \\frac{5{,}0}{0{,}250} = 20 \\text{ g/L}$$

#### Exemple 2

Quelle masse de glucose faut-il pour préparer $500$ mL de solution à $C_m = 10$ g/L ?

$$m = C_m \\times V = 10 \\times 0{,}500 = 5{,}0 \\text{ g}$$

#### Exemple 3

Le sérum physiologique a une concentration massique en $NaCl$ de $C_m = 9{,}0$ g/L. Quelle masse de sel contient une poche de $500$ mL ?

$$m = C_m \\times V = 9{,}0 \\times 0{,}500 = 4{,}5 \\text{ g}$$

---

## Concentration molaire

### Définition

La **concentration molaire** $C$ (ou concentration en quantité de matière) d'un soluté en solution est le rapport de la **quantité de matière de soluté** sur le **volume de solution** :

$$\\boxed{C = \\frac{n_{\\text{soluté}}}{V_{\\text{solution}}}}$$

| Grandeur | Symbole | Unité |
|----------|---------|-------|
| Concentration molaire | $C$ | $\\text{mol/L}$ (ou mol·L⁻¹) |
| Quantité de matière | $n_{\\text{soluté}}$ | $\\text{mol}$ |
| Volume de solution | $V_{\\text{solution}}$ | $\\text{L}$ |

### Exemples de calculs

#### Exemple 1

On dissout $0{,}10$ mol de $NaCl$ dans de l'eau pour obtenir $500$ mL de solution. Quelle est la concentration molaire ?

$$C = \\frac{n}{V} = \\frac{0{,}10}{0{,}500} = 0{,}20 \\text{ mol/L}$$

#### Exemple 2

Quelle quantité de matière de glucose se trouve dans $200$ mL de solution à $C = 0{,}50$ mol/L ?

$$n = C \\times V = 0{,}50 \\times 0{,}200 = 0{,}10 \\text{ mol}$$

---

## Relation entre $C_m$ et $C$

Puisque $n = \\frac{m}{M}$, on peut relier les deux concentrations :

$$C = \\frac{n}{V} = \\frac{m}{M \\times V} = \\frac{C_m}{M}$$

$$\\boxed{C_m = C \\times M}$$

$$\\boxed{C = \\frac{C_m}{M}}$$

| Pour passer de… | …à… | Formule |
|-----------------|------|---------|
| $C_m$ (g/L) | $C$ (mol/L) | $C = \\frac{C_m}{M}$ |
| $C$ (mol/L) | $C_m$ (g/L) | $C_m = C \\times M$ |

### Exemple

Le sérum physiologique a $C_m = 9{,}0$ g/L en $NaCl$. Quelle est la concentration molaire ?

$$M_{NaCl} = 23{,}0 + 35{,}5 = 58{,}5 \\text{ g/mol}$$

$$C = \\frac{C_m}{M} = \\frac{9{,}0}{58{,}5} = 0{,}154 \\text{ mol/L} \\approx 0{,}15 \\text{ mol/L}$$

---

## Étalonnage — détermination d'une concentration inconnue

### Principe

On prépare plusieurs solutions de concentrations **connues** (solutions étalons) et on mesure une **propriété physique** qui varie avec la concentration (absorbance, conductivité, indice de réfraction…).

On trace la **courbe d'étalonnage** : propriété physique = $f(C)$.

On mesure ensuite cette même propriété sur la solution de concentration **inconnue** et on lit la concentration sur le graphique.

### Exemple : dosage par étalonnage colorimétrique

1. Préparer 5 solutions de permanganate de potassium $KMnO_4$ à $C_1 = 1{,}0 \\times 10^{-4}$, $C_2 = 2{,}0 \\times 10^{-4}$, …, $C_5 = 5{,}0 \\times 10^{-4}$ mol/L
2. Mesurer l'**absorbance** $A$ de chaque solution (spectrophotomètre à $\\lambda = 525$ nm)
3. Tracer $A = f(C)$ → droite passant par l'origine (loi de Beer-Lambert : $A = \\varepsilon \\cdot \\ell \\cdot C$)
4. Mesurer $A$ de la solution inconnue → lire $C$ sur le graphique

> **Loi de Beer-Lambert :** $A = \\varepsilon \\cdot \\ell \\cdot C$ où $\\varepsilon$ est le coefficient d'extinction molaire ($\\text{L} \\cdot \\text{mol}^{-1} \\cdot \\text{cm}^{-1}$), $\\ell$ la largeur de la cuve (cm) et $C$ la concentration (mol/L).

---

## À retenir

- **Concentration massique :** $C_m = \\frac{m_{\\text{soluté}}}{V_{\\text{solution}}}$ (en g/L).
- **Concentration molaire :** $C = \\frac{n_{\\text{soluté}}}{V_{\\text{solution}}}$ (en mol/L).
- Relation : $C = \\frac{C_m}{M}$ et $C_m = C \\times M$.
- L'**étalonnage** permet de déterminer la concentration d'une solution inconnue en comparant une propriété physique mesurée à une courbe de référence.
""",
                'quiz': {
                    'titre': 'Quiz — Concentration massique et concentration molaire',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Qu'est-ce que le soluté dans une solution ?",
                            'options': ["L'espèce chimique dissoute (minoritaire)", "L'espèce chimique majoritaire", "Le mélange final obtenu", "Le récipient utilisé"],
                            'reponse_correcte': '0',
                            'explication': "Le soluté est l'espèce chimique dissoute dans le solvant. Il est en quantité minoritaire dans la solution.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "La concentration massique Cm s'exprime en :",
                            'options': ["g/L", "mol/L", "g/mol", "L/mol"],
                            'reponse_correcte': '0',
                            'explication': "La concentration massique Cm = m(soluté) / V(solution) s'exprime en grammes par litre (g/L).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Quelle formule permet de calculer la concentration molaire C ?",
                            'options': ["C = n / V", "C = m / V", "C = n × V", "C = m × V"],
                            'reponse_correcte': '0',
                            'explication': "La concentration molaire C = n(soluté) / V(solution), avec n en mol et V en L.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Dans une solution aqueuse, le solvant est :",
                            'options': ["L'eau", "Le soluté", "Un gaz", "Un solide"],
                            'reponse_correcte': '0',
                            'explication': "Une solution aqueuse a l'eau comme solvant. 'Aqueuse' vient du latin aqua = eau.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Quelle relation lie Cm, C et M ?",
                            'options': ["Cm = C × M", "Cm = C / M", "Cm = C + M", "Cm = C − M"],
                            'reponse_correcte': '0',
                            'explication': "Cm = C × M, car Cm = m/V = (n × M)/V = C × M.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "On dissout 5,0 g de NaCl dans 250 mL de solution. Quelle est la concentration massique ?",
                            'options': ["20 g/L", "5,0 g/L", "2,0 g/L", "50 g/L"],
                            'reponse_correcte': '0',
                            'explication': "Cm = m / V = 5,0 / 0,250 = 20 g/L.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "L'unité de la concentration molaire est :",
                            'options': ["mol/L", "g/L", "g/mol", "L/mol"],
                            'reponse_correcte': '0',
                            'explication': "La concentration molaire C = n/V s'exprime en moles par litre (mol/L ou mol·L⁻¹).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Une solution est dite saturée lorsque :",
                            'options': ["Le solvant ne peut plus dissoudre de soluté supplémentaire", "La solution est très diluée", "Le soluté a entièrement disparu", "La température est de 0 °C"],
                            'reponse_correcte': '0',
                            'explication': "Une solution saturée a atteint la limite de solubilité : le solvant ne peut plus dissoudre de soluté à cette température.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Le sérum physiologique a Cm = 9,0 g/L en NaCl. Quelle masse de sel contient une poche de 500 mL ?",
                            'options': ["4,5 g", "9,0 g", "18 g", "0,45 g"],
                            'reponse_correcte': '0',
                            'explication': "m = Cm × V = 9,0 × 0,500 = 4,5 g.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "On dissout 0,10 mol de NaCl dans 500 mL de solution. Quelle est la concentration molaire ?",
                            'options': ["0,20 mol/L", "0,10 mol/L", "0,50 mol/L", "2,0 mol/L"],
                            'reponse_correcte': '0',
                            'explication': "C = n / V = 0,10 / 0,500 = 0,20 mol/L.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Le sérum physiologique a Cm = 9,0 g/L en NaCl (M = 58,5 g/mol). Quelle est la concentration molaire ?",
                            'options': ["0,15 mol/L", "9,0 mol/L", "58,5 mol/L", "0,90 mol/L"],
                            'reponse_correcte': '0',
                            'explication': "C = Cm / M = 9,0 / 58,5 ≈ 0,15 mol/L.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Quelle quantité de matière de glucose se trouve dans 200 mL de solution à C = 0,50 mol/L ?",
                            'options': ["0,10 mol", "0,50 mol", "1,0 mol", "0,25 mol"],
                            'reponse_correcte': '0',
                            'explication': "n = C × V = 0,50 × 0,200 = 0,10 mol.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Lors d'un dosage par étalonnage colorimétrique, on utilise :",
                            'options': ["Un spectrophotomètre pour mesurer l'absorbance", "Une balance pour mesurer la masse", "Un thermomètre pour mesurer la température", "Un pH-mètre pour mesurer le pH"],
                            'reponse_correcte': '0',
                            'explication': "Le dosage par étalonnage colorimétrique mesure l'absorbance de solutions étalons et de la solution inconnue à l'aide d'un spectrophotomètre.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "La loi de Beer-Lambert s'écrit A = ε × ℓ × C. L'absorbance A est proportionnelle à :",
                            'options': ["La concentration C du soluté", "La masse molaire M du soluté", "Le volume de la solution", "La température de la solution"],
                            'reponse_correcte': '0',
                            'explication': "D'après la loi de Beer-Lambert, l'absorbance est directement proportionnelle à la concentration C (à ε et ℓ constants).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Le volume V dans la formule Cm = m / V est le volume du solvant seul.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "V est le volume de la SOLUTION (solvant + soluté), pas du solvant seul.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La courbe d'étalonnage A = f(C) selon la loi de Beer-Lambert est une droite passant par l'origine.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "A = ε × ℓ × C est de la forme y = k × x : c'est bien une droite passant par l'origine (si ε et ℓ sont constants).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "On peut obtenir la concentration molaire à partir de la concentration massique en divisant par la masse molaire.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "C = Cm / M. On divise bien la concentration massique par la masse molaire pour obtenir la concentration molaire.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quelle masse (en g) de glucose faut-il pour préparer 500 mL de solution à Cm = 10 g/L ?",
                            'options': None,
                            'reponse_correcte': '5',
                            'tolerances': ['5,0', '5.0', '5 g', '5,0 g', '5.0 g'],
                            'explication': "m = Cm × V = 10 × 0,500 = 5,0 g.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on l'espèce chimique majoritaire dans une solution ?",
                            'options': None,
                            'reponse_correcte': 'solvant',
                            'tolerances': ['le solvant', 'Solvant', 'Le solvant'],
                            'explication': "Le solvant est l'espèce chimique majoritaire dans une solution (souvent l'eau pour les solutions aqueuses).",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Une solution de NaCl a C = 0,20 mol/L et M(NaCl) = 58,5 g/mol. Quelle est sa concentration massique Cm en g/L ?",
                            'options': None,
                            'reponse_correcte': '11,7',
                            'tolerances': ['11.7', '11,7 g/L', '11.7 g/L', '11,70', '11.70'],
                            'explication': "Cm = C × M = 0,20 × 58,5 = 11,7 g/L.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Préparation par dissolution et dilution',
                'duree': 35,
                'contenu': """# Préparation par dissolution et dilution

## Introduction

Au laboratoire, il est essentiel de savoir préparer des solutions de concentration précise. Deux techniques fondamentales permettent d'y parvenir : la **dissolution** d'un soluté solide dans un solvant, et la **dilution** d'une solution concentrée. Ce chapitre détaille les protocoles et les calculs associés.

---

## Préparation par dissolution

### Principe

La **dissolution** consiste à dissoudre une masse précise de soluté solide dans un solvant (eau) pour obtenir un volume donné de solution à la concentration souhaitée.

### Calcul préalable

Pour préparer un volume $V$ de solution de concentration molaire $C$, on calcule d'abord la **quantité de matière** de soluté nécessaire :

$$n = C \\times V$$

Puis la **masse** à peser :

$$m = n \\times M = C \\times V \\times M$$

> **Attention aux unités :** $C$ en mol/L, $V$ en L, $M$ en g/mol → $m$ en g.

Si la concentration souhaitée est massique ($C_m$), alors directement :

$$m = C_m \\times V$$

### Protocole expérimental (fiole jaugée)

La fiole jaugée est la verrerie de précision utilisée pour préparer un volume exact de solution.

**Étapes :**

1. **Calculer** la masse $m$ de soluté nécessaire.
2. **Peser** cette masse sur une balance de précision (coupelle de pesée ou verre de montre).
3. **Transférer** le soluté dans une fiole jaugée de volume $V$ à l'aide d'un entonnoir.
4. **Rincer** le verre de montre et l'entonnoir avec de l'eau distillée pour ne perdre aucun grain de soluté.
5. **Ajouter** de l'eau distillée jusqu'à environ la moitié de la fiole.
6. **Agiter** (boucher et retourner) jusqu'à dissolution complète du soluté.
7. **Compléter** avec de l'eau distillée jusqu'au **trait de jauge** (le bas du ménisque affleure le trait).
8. **Boucher** et **homogénéiser** en retournant plusieurs fois la fiole.

> **Points critiques :**
> - Ajuster au trait de jauge avec une **pipette Pasteur** pour les derniers millilitres.
> - Lire le trait de jauge à hauteur des yeux pour éviter l'erreur de parallaxe.
> - Le **ménisque** (surface courbée de l'eau) doit être tangent au trait de jauge par le bas.

### Exemple complet

**Énoncé :** Préparer $V = 250$ mL de solution de sulfate de cuivre $CuSO_4$ à la concentration $C = 0{,}10$ mol/L.

**Résolution :**

Masse molaire : $M_{CuSO_4} = 63{,}5 + 32{,}1 + 4 \\times 16{,}0 = 159{,}6$ g/mol

Quantité de matière : $n = C \\times V = 0{,}10 \\times 0{,}250 = 0{,}025$ mol

Masse à peser : $m = n \\times M = 0{,}025 \\times 159{,}6 = 3{,}99$ g $\\approx 4{,}0$ g

> On pèse $4{,}0$ g de $CuSO_4$, on les dissout dans une fiole jaugée de 250 mL, et on complète au trait de jauge avec de l'eau distillée.

---

## Préparation par dilution

### Principe

La **dilution** consiste à ajouter du solvant à une solution **concentrée** (solution mère) pour obtenir une solution **moins concentrée** (solution fille).

> **En diluant :** le volume de solution augmente, mais la quantité de matière de soluté **ne change pas** (on n'ajoute pas de soluté, seulement du solvant).

### Conservation de la quantité de matière

$$n_{\\text{prélevé}} = n_{\\text{obtenu}}$$

$$\\boxed{C_1 \\times V_1 = C_2 \\times V_2}$$

| Notation | Signification |
|----------|---------------|
| $C_1$ | Concentration de la solution mère (mol/L) |
| $V_1$ | Volume **prélevé** de la solution mère (L) |
| $C_2$ | Concentration de la solution fille (mol/L) |
| $V_2$ | Volume **total** de la solution fille (L) |

> Cette relation est aussi valable avec les concentrations massiques : $C_{m_1} \\times V_1 = C_{m_2} \\times V_2$.

### Facteur de dilution

Le **facteur de dilution** $F$ indique « par combien » on a divisé la concentration :

$$\\boxed{F = \\frac{C_1}{C_2} = \\frac{V_2}{V_1}}$$

> **Exemple :** si $F = 10$, la solution fille est **10 fois moins concentrée** que la solution mère.

### Protocole expérimental (pipette jaugée + fiole jaugée)

**Étapes :**

1. **Calculer** le volume $V_1$ à prélever : $V_1 = \\frac{C_2 \\times V_2}{C_1}$.
2. **Prélever** $V_1$ de la solution mère à l'aide d'une **pipette jaugée** (verrerie de précision pour les volumes).
3. **Verser** le prélèvement dans une fiole jaugée de volume $V_2$.
4. **Compléter** avec de l'eau distillée jusqu'au **trait de jauge**.
5. **Boucher** et **homogénéiser**.

> **Verrerie de précision :** on utilise une **pipette jaugée** pour prélever (volume exact), et une **fiole jaugée** pour le volume final (volume exact). Les béchers et éprouvettes graduées ne sont **pas assez précis** pour ces opérations.

### Exemple complet

**Énoncé :** On dispose d'une solution mère de $NaCl$ à $C_1 = 1{,}0$ mol/L. Préparer $V_2 = 100$ mL de solution fille à $C_2 = 0{,}10$ mol/L.

**Résolution :**

Facteur de dilution : $F = \\frac{C_1}{C_2} = \\frac{1{,}0}{0{,}10} = 10$

Volume à prélever : $V_1 = \\frac{C_2 \\times V_2}{C_1} = \\frac{0{,}10 \\times 100}{1{,}0} = 10$ mL

> On prélève $10$ mL de solution mère avec une pipette jaugée de $10$ mL, on les verse dans une fiole jaugée de $100$ mL, et on complète au trait de jauge avec de l'eau distillée.

---

## Dilutions en cascade (ou en série)

Pour obtenir des solutions très diluées, on effectue des **dilutions successives**. À chaque étape, la solution fille de l'étape précédente devient la solution mère de l'étape suivante.

### Exemple

Obtenir une solution à $C = 1{,}0 \\times 10^{-4}$ mol/L à partir d'une solution mère à $C_0 = 1{,}0$ mol/L.

Le facteur total est $F_{\\text{total}} = \\frac{1{,}0}{1{,}0 \\times 10^{-4}} = 10^4 = 10\\,000$.

On peut procéder en **deux dilutions** au facteur 100 chacune ($100 \\times 100 = 10\\,000$) :

1. Dilution 1 : $C_0 = 1{,}0$ → $C_1 = 0{,}010 = 1{,}0 \\times 10^{-2}$ mol/L (facteur 100)
2. Dilution 2 : $C_1 = 1{,}0 \\times 10^{-2}$ → $C_2 = 1{,}0 \\times 10^{-4}$ mol/L (facteur 100)

> **Avantage :** chaque étape ne nécessite que des volumes raisonnables et minimise les erreurs de mesure.

---

## Verrerie — précision et choix

| Verrerie | Type | Précision | Utilisation |
|----------|------|-----------|-------------|
| **Fiole jaugée** | Jaugée (un seul trait) | Très bonne | Préparer un volume **exact** de solution |
| **Pipette jaugée** | Jaugée (un ou deux traits) | Très bonne | Prélever un volume **exact** de liquide |
| **Burette graduée** | Graduée | Bonne | Verser un volume précis (titrages) |
| **Éprouvette graduée** | Graduée | Moyenne | Mesurer un volume approximatif |
| **Bécher** | Non graduée (graduations indicatives) | Faible | Contenir, agiter, chauffer |

> **Règle d'or :** pour la dissolution et la dilution, on utilise **toujours** de la verrerie **jaugée** (fiole + pipette) pour garantir la précision.

---

## Résumé des formules

| Opération | Formule clé | Ce qu'on calcule |
|-----------|-------------|-----------------|
| Dissolution | $m = C \\times V \\times M$ | Masse de soluté à peser |
| Dissolution (massique) | $m = C_m \\times V$ | Masse de soluté à peser |
| Dilution | $C_1 V_1 = C_2 V_2$ | Volume à prélever ($V_1$) |
| Facteur de dilution | $F = \\frac{C_1}{C_2} = \\frac{V_2}{V_1}$ | Rapport de concentrations |

---

## À retenir

- La **dissolution** : on pèse une masse de soluté, on la dissout dans une fiole jaugée et on complète au trait de jauge.
- La **dilution** : on prélève un volume de solution mère (pipette jaugée), on le verse dans une fiole jaugée et on complète au trait de jauge.
- Relation de dilution : $C_1 V_1 = C_2 V_2$ (conservation de la quantité de matière).
- Le **facteur de dilution** $F = \\frac{C_1}{C_2}$ indique par combien la concentration a été divisée.
- Toujours utiliser de la **verrerie jaugée** (fiole, pipette) pour une préparation précise.
""",
                'quiz': {
                    'titre': 'Quiz — Préparation par dissolution et dilution',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Qu'est-ce qu'une dissolution ?",
                            'options': ["Dissoudre un soluté solide dans un solvant pour obtenir une solution", "Ajouter du solvant à une solution pour la diluer", "Faire évaporer le solvant d'une solution", "Mélanger deux solutions de même concentration"],
                            'reponse_correcte': '0',
                            'explication': "La dissolution consiste à dissoudre une masse de soluté dans un solvant pour obtenir une solution de concentration choisie.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quelle est la verrerie de précision utilisée pour préparer un volume exact de solution lors d'une dissolution ?",
                            'options': ["La fiole jaugée", "Le bécher", "L'éprouvette graduée", "L'erlenmeyer"],
                            'reponse_correcte': '0',
                            'explication': "La fiole jaugée possède un trait de jauge qui permet de préparer un volume exact de solution.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Lors d'une dilution, que conserve-t-on ?",
                            'options': ["La quantité de matière de soluté", "La concentration de la solution", "Le volume de la solution", "La masse du solvant"],
                            'reponse_correcte': '0',
                            'explication': "En dilution, on ajoute du solvant : le volume augmente, la concentration diminue, mais la quantité de matière de soluté reste constante.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quelle relation caractérise la dilution ?",
                            'options': ["C₁V₁ = C₂V₂", "C₁ + V₁ = C₂ + V₂", "C₁/V₁ = C₂/V₂", "C₁ × C₂ = V₁ × V₂"],
                            'reponse_correcte': '0',
                            'explication': "La conservation de la quantité de matière lors d'une dilution s'écrit C₁V₁ = C₂V₂.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Le facteur de dilution F est défini par :",
                            'options': ["F = C₁ / C₂", "F = C₂ / C₁", "F = C₁ × C₂", "F = C₁ + C₂"],
                            'reponse_correcte': '0',
                            'explication': "Le facteur de dilution F = C₁/C₂ = V₂/V₁ indique par combien la concentration a été divisée.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Pour prélever un volume exact de solution mère lors d'une dilution, on utilise :",
                            'options': ["Une pipette jaugée", "Un bécher", "Une éprouvette graduée", "Un entonnoir"],
                            'reponse_correcte': '0',
                            'explication': "La pipette jaugée est la verrerie de précision utilisée pour prélever un volume exact de liquide.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "La formule pour calculer la masse de soluté à peser lors d'une dissolution est :",
                            'options': ["m = C × V × M", "m = C / (V × M)", "m = C × V / M", "m = V × M / C"],
                            'reponse_correcte': '0',
                            'explication': "n = C × V et m = n × M, donc m = C × V × M.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Lors de l'ajustement au trait de jauge d'une fiole jaugée, on ajuste :",
                            'options': ["Le bas du ménisque au trait de jauge", "Le haut du ménisque au trait de jauge", "Le milieu du ménisque au trait de jauge", "N'importe quelle partie du ménisque"],
                            'reponse_correcte': '0',
                            'explication': "On ajuste le bas du ménisque (la surface courbée de l'eau) au trait de jauge, en lisant à hauteur des yeux.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "On veut préparer 250 mL de solution de CuSO₄ à C = 0,10 mol/L (M = 159,6 g/mol). Quelle masse faut-il peser ?",
                            'options': ["4,0 g", "16,0 g", "40,0 g", "1,6 g"],
                            'reponse_correcte': '0',
                            'explication': "m = C × V × M = 0,10 × 0,250 × 159,6 = 3,99 ≈ 4,0 g.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "On dispose d'une solution mère à C₁ = 1,0 mol/L. On veut 100 mL de solution fille à C₂ = 0,10 mol/L. Quel volume prélever ?",
                            'options': ["10 mL", "100 mL", "1,0 mL", "50 mL"],
                            'reponse_correcte': '0',
                            'explication': "V₁ = C₂ × V₂ / C₁ = 0,10 × 100 / 1,0 = 10 mL.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Le facteur de dilution vaut F = 10. Cela signifie que la solution fille est :",
                            'options': ["10 fois moins concentrée que la solution mère", "10 fois plus concentrée que la solution mère", "De même concentration que la solution mère", "100 fois moins concentrée que la solution mère"],
                            'reponse_correcte': '0',
                            'explication': "F = C₁/C₂ = 10 signifie que la concentration a été divisée par 10.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Lors d'une dissolution, pourquoi rince-t-on le verre de montre et l'entonnoir avec de l'eau distillée ?",
                            'options': ["Pour ne perdre aucun grain de soluté", "Pour refroidir le matériel", "Pour sécher le matériel", "Pour vérifier la propreté"],
                            'reponse_correcte': '0',
                            'explication': "Le rinçage permet de transférer tout le soluté dans la fiole, sans en perdre un seul grain, ce qui garantit la précision de la concentration.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Pour passer d'une solution à C₀ = 1,0 mol/L à C = 1,0 × 10⁻⁴ mol/L, le facteur de dilution total est :",
                            'options': ["10 000", "1 000", "100", "100 000"],
                            'reponse_correcte': '0',
                            'explication': "F = C₀/C = 1,0 / 1,0 × 10⁻⁴ = 10⁴ = 10 000.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Quelle verrerie n'est PAS une verrerie jaugée ?",
                            'options': ["Le bécher", "La fiole jaugée", "La pipette jaugée", "La burette graduée"],
                            'reponse_correcte': '0',
                            'explication': "Le bécher possède des graduations indicatives mais n'est pas une verrerie de précision (jaugée). Ses graduations sont approximatives.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Lors d'une dilution, la quantité de matière de soluté change.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "Lors d'une dilution, on ajoute uniquement du solvant. La quantité de matière de soluté reste constante : n₁ = n₂ (soit C₁V₁ = C₂V₂).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "On peut utiliser une éprouvette graduée à la place d'une pipette jaugée pour une dilution précise.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "L'éprouvette graduée n'a pas la précision suffisante. Pour une dilution précise, on utilise toujours de la verrerie jaugée (pipette jaugée + fiole jaugée).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "La relation C₁V₁ = C₂V₂ est aussi valable avec les concentrations massiques.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "La relation de conservation s'applique aussi aux concentrations massiques : Cm₁ × V₁ = Cm₂ × V₂.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "On dilue une solution mère à C₁ = 2,0 mol/L. On prélève V₁ = 25 mL et on obtient V₂ = 250 mL de solution fille. Quelle est C₂ en mol/L ?",
                            'options': None,
                            'reponse_correcte': '0,20',
                            'tolerances': ['0.20', '0,2', '0.2', '0,20 mol/L', '0.20 mol/L'],
                            'explication': "C₂ = C₁ × V₁ / V₂ = 2,0 × 25 / 250 = 0,20 mol/L.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Quel est le facteur de dilution si C₁ = 0,50 mol/L et C₂ = 0,050 mol/L ?",
                            'options': None,
                            'reponse_correcte': '10',
                            'tolerances': ['10,0', '10.0', 'F = 10'],
                            'explication': "F = C₁ / C₂ = 0,50 / 0,050 = 10.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "On veut préparer 100 mL de solution de NaCl à C = 0,50 mol/L par dissolution (M = 58,5 g/mol). Quelle masse (en g) de NaCl faut-il peser ?",
                            'options': None,
                            'reponse_correcte': '2,93',
                            'tolerances': ['2.93', '2,9', '2.9', '2,93 g', '2.93 g', '2,925'],
                            'explication': "m = C × V × M = 0,50 × 0,100 × 58,5 = 2,925 ≈ 2,93 g.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 7 — Les transformations chimiques
    # ──────────────────────────────────────────────
    {
        'ordre': 7,
        'titre': 'Les transformations chimiques',
        'description': "Distinguer transformation chimique et transformation physique, modéliser une réaction par une équation bilan équilibrée et identifier les espèces spectatrices.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Réaction chimique — équation et conservation',
                'duree': 35,
                'contenu': """# Réaction chimique — équation et conservation

## Introduction

Lors d'une **transformation chimique**, des espèces chimiques disparaissent (les **réactifs**) et de nouvelles espèces apparaissent (les **produits**). Contrairement à une transformation physique (changement d'état), les **espèces chimiques sont modifiées** : des liaisons sont rompues et de nouvelles liaisons sont formées.

> **Exemple concret :** lorsqu'on fait brûler du méthane $CH_4$ dans le dioxygène $O_2$, il se forme du dioxyde de carbone $CO_2$ et de l'eau $H_2O$. Le méthane et le dioxygène disparaissent ; le dioxyde de carbone et l'eau apparaissent.

---

## Transformation chimique vs transformation physique

| Critère | Transformation physique | Transformation chimique |
|---------|------------------------|------------------------|
| **Espèces chimiques** | Conservées (même espèce avant/après) | Modifiées (nouvelles espèces formées) |
| **Exemple** | Fusion de la glace : $H_2O_{(s)} \\to H_2O_{(l)}$ | Combustion du carbone : $C + O_2 \\to CO_2$ |
| **Liaisons chimiques** | Inchangées | Rompues puis reformées |
| **Réversibilité** | Souvent facilement réversible | Souvent difficilement réversible |

---

## Réactifs, produits et espèces spectatrices

### Définitions

- **Réactif** : espèce chimique **consommée** lors de la transformation.
- **Produit** : espèce chimique **formée** lors de la transformation.
- **Espèce spectatrice** : espèce présente dans le milieu réactionnel mais qui **ne participe pas** à la réaction. Elle est présente en même quantité avant et après la transformation.

> **Exemple :** lorsqu'on verse de l'acide chlorhydrique ($H^+_{(aq)} + Cl^-_{(aq)}$) sur du zinc $Zn_{(s)}$, les ions chlorure $Cl^-$ ne participent pas à la réaction : ce sont des espèces spectatrices.

---

## Lois de conservation

Lors d'une transformation chimique, trois grandeurs sont **toujours conservées** :

### 1. Conservation des éléments chimiques

Chaque type d'atome est présent en **même quantité** dans les réactifs et les produits. Les atomes ne sont ni créés, ni détruits : ils sont **réarrangés**.

### 2. Conservation de la masse

Conséquence directe de la conservation des atomes :

$$m_{\\text{réactifs}} = m_{\\text{produits}}$$

> C'est la **loi de Lavoisier** (1789) : « Rien ne se perd, rien ne se crée, tout se transforme. »

### 3. Conservation de la charge électrique

La charge totale est la même des deux côtés de l'équation.

---

## L'équation de réaction

### Modélisation

Une **équation de réaction** (ou équation bilan) est l'écriture symbolique d'une transformation chimique. Elle indique les formules des réactifs (à gauche) et des produits (à droite), séparés par une flèche :

$$\\text{Réactifs} \\longrightarrow \\text{Produits}$$

### Coefficients stœchiométriques

Pour respecter la conservation des éléments et des charges, on place des **coefficients stœchiométriques** (nombres entiers) devant les formules chimiques.

> **Convention :** un coefficient de 1 n'est pas écrit.

### Exemple — combustion du méthane

Équation non équilibrée :
$$CH_4 + O_2 \\to CO_2 + H_2O$$

Vérification :
| Élément | Côté gauche | Côté droite |
|---------|-------------|-------------|
| C | 1 | 1 ✓ |
| H | 4 | 2 ✗ |
| O | 2 | 3 ✗ |

Équation **équilibrée** :
$$CH_4 + 2\\,O_2 \\longrightarrow CO_2 + 2\\,H_2O$$

Vérification :
| Élément | Côté gauche | Côté droite |
|---------|-------------|-------------|
| C | 1 | 1 ✓ |
| H | 4 | 4 ✓ |
| O | 4 | 4 ✓ |

---

## Méthode pour équilibrer une équation

1. **Écrire** les formules brutes des réactifs et des produits.
2. **Compter** le nombre d'atomes de chaque élément de chaque côté.
3. **Ajuster** les coefficients stœchiométriques pour égaliser le nombre d'atomes de chaque élément.
4. **Vérifier** l'ensemble (éléments + charges si ions).

> **Règle importante :** on ne modifie **jamais** les formules chimiques (les indices dans les formules). On ajuste uniquement les **coefficients** devant les formules.

### Exemple — combustion du propane

Le propane $C_3H_8$ brûle dans le dioxygène :

**Étape 1 :** $C_3H_8 + O_2 \\to CO_2 + H_2O$

**Étape 2 :** Comptage
- C : 3 à gauche, 1 à droite → coefficient 3 devant $CO_2$
- H : 8 à gauche, 2 à droite → coefficient 4 devant $H_2O$

**Étape 3 :** $C_3H_8 + O_2 \\to 3\\,CO_2 + 4\\,H_2O$
- O à droite : $3 \\times 2 + 4 \\times 1 = 10$ → coefficient 5 devant $O_2$

**Résultat :**
$$C_3H_8 + 5\\,O_2 \\longrightarrow 3\\,CO_2 + 4\\,H_2O$$

**Vérification :** C : 3 = 3 ✓ | H : 8 = 8 ✓ | O : 10 = 10 ✓

---

## Exemples de réactions chimiques courantes

### Combustions

| Combustible | Équation bilan | Type |
|-------------|---------------|------|
| Carbone (complète) | $C + O_2 \\to CO_2$ | Combustion complète |
| Carbone (incomplète) | $2\\,C + O_2 \\to 2\\,CO$ | Combustion incomplète |
| Méthane | $CH_4 + 2\\,O_2 \\to CO_2 + 2\\,H_2O$ | Combustion complète |
| Fer (dans l'air) | $3\\,Fe + 2\\,O_2 \\to Fe_3O_4$ | Combustion vive |

> **Combustion complète** : suffisamment de dioxygène → $CO_2$ et $H_2O$ uniquement.
> **Combustion incomplète** : dioxygène insuffisant → formation de $CO$ (monoxyde de carbone, toxique) ou de carbone $C$ (suie).

### Réaction acide-métal

$$Zn + 2\\,H^+ \\longrightarrow Zn^{2+} + H_2$$

Le zinc réagit avec les ions hydrogène pour former des ions zinc et du dihydrogène (effervescence).

---

## États physiques dans l'équation

On peut préciser l'état physique des espèces entre parenthèses :

| Symbole | État |
|---------|------|
| $(s)$ | Solide |
| $(l)$ | Liquide |
| $(g)$ | Gazeux |
| $(aq)$ | En solution aqueuse |

**Exemple :**
$$Zn_{(s)} + 2\\,H^+_{(aq)} \\longrightarrow Zn^{2+}_{(aq)} + H_{2\\,(g)}$$

---

## À retenir

- Une **transformation chimique** produit de nouvelles espèces chimiques (contrairement à une transformation physique).
- L'**équation de réaction** modélise la transformation : réactifs → produits.
- Les **coefficients stœchiométriques** assurent la conservation des éléments et des charges.
- La **masse totale** est conservée (loi de Lavoisier).
- On ne modifie **jamais** les formules des espèces chimiques, seulement les coefficients.
""",
                'quiz': {
                    'titre': 'Quiz — Réaction chimique, équation et conservation',
                    'score_minimum': 60.0,
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Lors d'une transformation chimique :",
                            'options': ["De nouvelles espèces chimiques sont formées", "Les espèces chimiques restent identiques", "Seule la température change", "Il y a toujours un changement d'état"],
                            'reponse_correcte': '0',
                            'explication': "Une transformation chimique produit de nouvelles espèces chimiques : les réactifs disparaissent et les produits apparaissent.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Les espèces chimiques consommées lors d'une transformation chimique sont appelées :",
                            'options': ["Les réactifs", "Les produits", "Les catalyseurs", "Les espèces spectatrices"],
                            'reponse_correcte': '0',
                            'explication': "Les réactifs sont les espèces consommées lors de la réaction. Les produits sont les espèces formées.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "La loi de Lavoisier stipule que lors d'une transformation chimique :",
                            'options': ["La masse totale est conservée", "Le volume total est conservé", "La température est conservée", "Le nombre de molécules est conservé"],
                            'reponse_correcte': '0',
                            'explication': "La loi de Lavoisier (1789) affirme la conservation de la masse : « Rien ne se perd, rien ne se crée, tout se transforme. »",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quel symbole indique qu'une espèce est en solution aqueuse dans une équation de réaction ?",
                            'options': ["(aq)", "(l)", "(s)", "(g)"],
                            'reponse_correcte': '0',
                            'explication': "(aq) signifie « aqueux », c'est-à-dire dissous dans l'eau. (l) = liquide, (s) = solide, (g) = gazeux.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Dans l'équation CH₄ + 2 O₂ → CO₂ + 2 H₂O, le coefficient 2 devant O₂ signifie :",
                            'options': ["Il faut 2 moles de O₂ par mole de CH₄", "La molécule d'O₂ contient 2 atomes d'oxygène", "La réaction produit 2 moles de O₂", "Il y a 2 types de réactifs"],
                            'reponse_correcte': '0',
                            'explication': "Le coefficient stœchiométrique 2 devant O₂ indique que 2 moles de dioxygène réagissent avec 1 mole de méthane.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quelle est l'équation correctement équilibrée pour la combustion du fer dans le dioxygène ?",
                            'options': ["3 Fe + 2 O₂ → Fe₃O₄", "Fe + O₂ → FeO₂", "2 Fe + 3 O₂ → Fe₂O₃", "4 Fe + 3 O₂ → 2 Fe₂O₃"],
                            'reponse_correcte': '0',
                            'explication': "3 Fe + 2 O₂ → Fe₃O₄ : Fe = 3/3 ✓, O = 4/4 ✓. C'est la formule de la magnétite formée lors de la combustion vive du fer.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "L'équation de la combustion complète du propane est C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O. Combien d'atomes d'oxygène y a-t-il du côté des produits ?",
                            'options': ["10", "7", "6", "12"],
                            'reponse_correcte': '0',
                            'explication': "Côté produits : 3 CO₂ → 3×2 = 6 atomes O, et 4 H₂O → 4×1 = 4 atomes O. Total = 6 + 4 = 10.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Lors de la réaction Zn + 2 H⁺ → Zn²⁺ + H₂, si l'acide utilisé est HCl, les ions Cl⁻ sont :",
                            'options': ["Des espèces spectatrices", "Des produits", "Des réactifs", "Des catalyseurs"],
                            'reponse_correcte': '0',
                            'explication': "Les ions Cl⁻ ne participent pas à la réaction : ils sont présents en même quantité avant et après. Ce sont des espèces spectatrices.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Pour équilibrer une équation de réaction, on peut modifier :",
                            'options': ["Les coefficients stœchiométriques devant les formules", "Les indices dans les formules chimiques", "Les symboles des éléments", "Le sens de la flèche de réaction"],
                            'reponse_correcte': '0',
                            'explication': "On ne modifie jamais les formules chimiques (indices). On ajuste uniquement les coefficients placés devant les formules.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quelle est la différence entre une combustion complète et une combustion incomplète ?",
                            'options': ["La combustion complète produit CO₂ et H₂O ; l'incomplète peut former CO ou C", "La complète est plus lente", "L'incomplète utilise plus de dioxygène", "Il n'y a aucune différence"],
                            'reponse_correcte': '0',
                            'explication': "En combustion complète (excès de O₂), on obtient CO₂ et H₂O. En combustion incomplète (défaut de O₂), il se forme du CO (toxique) ou du carbone C (suie).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Quelle est l'équation équilibrée de la combustion complète du butane C₄H₁₀ ?",
                            'options': ["2 C₄H₁₀ + 13 O₂ → 8 CO₂ + 10 H₂O", "C₄H₁₀ + 6 O₂ → 4 CO₂ + 5 H₂O", "C₄H₁₀ + 4 O₂ → 4 CO₂ + 5 H₂O", "2 C₄H₁₀ + 10 O₂ → 8 CO₂ + 10 H₂O"],
                            'reponse_correcte': '0',
                            'explication': "Vérification : C = 8/8 ✓, H = 20/20 ✓, O = 26/26 ✓. Le coefficient 13/2 devant O₂ impose de multiplier par 2.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "L'équation 2 Al + 3 CuSO₄ → Al₂(SO₄)₃ + 3 Cu est-elle équilibrée ? Combien d'atomes de soufre y a-t-il de chaque côté ?",
                            'options': ["Oui, 3 atomes de soufre de chaque côté", "Non, il y a 1 atome à gauche et 3 à droite", "Oui, 6 atomes de soufre de chaque côté", "Non, il y a 2 atomes à gauche et 3 à droite"],
                            'reponse_correcte': '0',
                            'explication': "Gauche : 3 CuSO₄ → 3 S. Droite : Al₂(SO₄)₃ → 3 S. L'équation est bien équilibrée.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 13,
                            'type': 'vrai_faux',
                            'texte': "La fusion de la glace est une transformation chimique.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "La fusion est une transformation physique : l'eau change d'état (solide → liquide) mais reste la même espèce chimique H₂O.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Dans une équation de réaction, les réactifs sont écrits à gauche de la flèche.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "Par convention, les réactifs sont à gauche de la flèche et les produits à droite : Réactifs → Produits.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Lors d'une combustion incomplète, il peut se former du monoxyde de carbone CO.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "En cas de déficit de dioxygène, la combustion est incomplète et produit du CO (monoxyde de carbone, gaz toxique) ou du carbone C (suie).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Le nombre total de molécules est toujours le même des deux côtés d'une équation de réaction.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "Ce sont les atomes de chaque élément qui sont conservés, pas le nombre de molécules. Exemple : CH₄ + 2 O₂ → CO₂ + 2 H₂O (3 molécules → 3, mais ce n'est pas une règle générale).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "L'équation N₂ + H₂ → NH₃ est correctement équilibrée.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "N : 2 à gauche, 1 à droite ✗. H : 2 à gauche, 3 à droite ✗. L'équation correcte est N₂ + 3 H₂ → 2 NH₃.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on les espèces chimiques formées lors d'une transformation chimique ?",
                            'options': None,
                            'reponse_correcte': 'produits',
                            'tolerances': ['les produits', 'Produits', 'Les produits', 'des produits'],
                            'explication': "Les espèces formées sont les produits ; les espèces consommées sont les réactifs.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Quelle est la formule chimique du gaz produit lors de la combustion complète du carbone dans le dioxygène ?",
                            'options': None,
                            'reponse_correcte': 'CO2',
                            'tolerances': ['co2', 'CO₂'],
                            'explication': "C + O₂ → CO₂. Le dioxyde de carbone est le produit de la combustion complète du carbone.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Équilibrer : 2 C₂H₆ + ? O₂ → 4 CO₂ + 6 H₂O. Quel est le coefficient devant O₂ ?",
                            'options': None,
                            'reponse_correcte': '7',
                            'tolerances': [],
                            'explication': "O à droite : 4×2 + 6×1 = 14 atomes. Donc ? × 2 = 14, soit un coefficient de 7 devant O₂.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': "État initial, état final et tableau d'avancement",
                'duree': 40,
                'contenu': """# État initial, état final et tableau d'avancement

## Introduction

Pour décrire quantitativement une transformation chimique, on utilise le **tableau d'avancement**. Cet outil permet de suivre l'évolution des quantités de matière de chaque espèce au cours de la réaction et de déterminer la composition du système à tout instant.

---

## État initial et état final

### Définitions

- **État initial (E.I.)** : état du système chimique **avant** le début de la transformation. On connaît les quantités de matière de chaque réactif et produit (souvent $n_{\\text{produits}} = 0$ au départ).
- **État final (E.F.)** : état du système **après** la transformation. Au moins un réactif a été **totalement consommé** (si la réaction est totale).

> **État intermédiaire** : état du système à un instant quelconque pendant la transformation.

---

## L'avancement de réaction $x$

### Définition

L'**avancement** $x$ (en mol) est une grandeur qui mesure la progression de la réaction. Il vaut :
- $x = 0$ à l'état initial
- $x = x_{\\text{max}}$ à l'état final (avancement maximal)

### Relation avec les quantités de matière

Pour une réaction générale :
$$a\\,A + b\\,B \\longrightarrow c\\,C + d\\,D$$

Les quantités de matière à un avancement $x$ quelconque s'expriment :

| Espèce | Quantité de matière |
|--------|--------------------|
| $A$ (réactif) | $n_A = n_{A,0} - a \\cdot x$ |
| $B$ (réactif) | $n_B = n_{B,0} - b \\cdot x$ |
| $C$ (produit) | $n_C = n_{C,0} + c \\cdot x$ |
| $D$ (produit) | $n_D = n_{D,0} + d \\cdot x$ |

Où $n_{A,0}$, $n_{B,0}$, etc. sont les quantités initiales et $a$, $b$, $c$, $d$ les coefficients stœchiométriques.

---

## Le tableau d'avancement

### Structure

Le tableau d'avancement résume l'évolution des quantités de matière :

| | Équation | $a\\,A$ | $+$ | $b\\,B$ | $\\to$ | $c\\,C$ | $+$ | $d\\,D$ |
|---|----------|--------|-----|--------|--------|--------|-----|--------|
| **E.I.** ($x=0$) | | $n_{A,0}$ | | $n_{B,0}$ | | $0$ | | $0$ |
| **E.int.** ($x$) | | $n_{A,0} - a\\,x$ | | $n_{B,0} - b\\,x$ | | $c\\,x$ | | $d\\,x$ |
| **E.F.** ($x_{max}$) | | $n_{A,0} - a\\,x_{max}$ | | $n_{B,0} - b\\,x_{max}$ | | $c\\,x_{max}$ | | $d\\,x_{max}$ |

---

## Détermination de l'avancement maximal $x_{max}$

### Principe

À l'état final, au moins un réactif est **totalement consommé** (sa quantité de matière atteint 0). Pour trouver $x_{max}$, on pose :

$$n_{A,0} - a \\cdot x_{max} = 0 \\quad \\Rightarrow \\quad x_{max,A} = \\frac{n_{A,0}}{a}$$

$$n_{B,0} - b \\cdot x_{max} = 0 \\quad \\Rightarrow \\quad x_{max,B} = \\frac{n_{B,0}}{b}$$

L'avancement maximal est le **plus petit** des deux :

$$\\boxed{x_{max} = \\min\\left(\\frac{n_{A,0}}{a},\\; \\frac{n_{B,0}}{b}\\right)}$$

---

## Réactif limitant et réactif en excès

### Définitions

- Le **réactif limitant** est celui qui est entièrement consommé en premier. Il impose la valeur de $x_{max}$.
- Le **réactif en excès** est celui qui n'est pas totalement consommé à l'état final.

### Comment l'identifier ?

On compare les quantités : $\\frac{n_{A,0}}{a}$ et $\\frac{n_{B,0}}{b}$.

- Si $\\frac{n_{A,0}}{a} < \\frac{n_{B,0}}{b}$ : **A** est le réactif limitant.
- Si $\\frac{n_{A,0}}{a} > \\frac{n_{B,0}}{b}$ : **B** est le réactif limitant.
- Si $\\frac{n_{A,0}}{a} = \\frac{n_{B,0}}{b}$ : les réactifs sont en **proportions stœchiométriques** (les deux sont totalement consommés).

---

## Application détaillée

### Énoncé

On fait réagir $n_{Fe} = 0{,}30$ mol de fer avec $n_{O_2} = 0{,}15$ mol de dioxygène selon :

$$3\\,Fe + 2\\,O_2 \\longrightarrow Fe_3O_4$$

### Étape 1 — Tableau d'avancement

| | $3\\,Fe$ | $+$ | $2\\,O_2$ | $\\to$ | $Fe_3O_4$ |
|---|---------|-----|----------|--------|----------|
| **E.I.** | $0{,}30$ | | $0{,}15$ | | $0$ |
| **E.int.** | $0{,}30 - 3x$ | | $0{,}15 - 2x$ | | $x$ |
| **E.F.** | $0{,}30 - 3x_{max}$ | | $0{,}15 - 2x_{max}$ | | $x_{max}$ |

### Étape 2 — Calcul de $x_{max}$

Pour le fer : $x_{max,Fe} = \\frac{0{,}30}{3} = 0{,}10$ mol

Pour le dioxygène : $x_{max,O_2} = \\frac{0{,}15}{2} = 0{,}075$ mol

$$x_{max} = \\min(0{,}10 \\;; 0{,}075) = 0{,}075 \\text{ mol}$$

> Le dioxygène $O_2$ est le **réactif limitant**.

### Étape 3 — Composition à l'état final

| Espèce | Quantité à l'E.F. (mol) |
|--------|------------------------|
| $Fe$ | $0{,}30 - 3 \\times 0{,}075 = 0{,}075$ (en excès) |
| $O_2$ | $0{,}15 - 2 \\times 0{,}075 = 0$ (totalement consommé) |
| $Fe_3O_4$ | $0{,}075$ |

---

## Proportions stœchiométriques

Les réactifs sont en **proportions stœchiométriques** lorsqu'ils sont tous totalement consommés à l'état final. Cela se produit quand :

$$\\frac{n_{A,0}}{a} = \\frac{n_{B,0}}{b}$$

> **Exemple :** pour $3\\,Fe + 2\\,O_2 \\to Fe_3O_4$, si on part de $0{,}30$ mol de $Fe$ et $0{,}20$ mol de $O_2$ :
> $$\\frac{0{,}30}{3} = 0{,}10 \\quad \\text{et} \\quad \\frac{0{,}20}{2} = 0{,}10$$
> Les deux quotients sont égaux : les réactifs sont en proportions stœchiométriques.

---

## À retenir

- Le **tableau d'avancement** suit l'évolution des quantités de matière grâce à l'**avancement** $x$.
- Les quantités de réactifs **diminuent** ($n_0 - \\nu \\cdot x$) et celles des produits **augmentent** ($\\nu \\cdot x$).
- L'**avancement maximal** $x_{max}$ est déterminé par le **réactif limitant** (le premier à être totalement consommé).
- On compare $\\frac{n_{A,0}}{a}$ et $\\frac{n_{B,0}}{b}$ pour identifier le réactif limitant.
- Si ces rapports sont égaux, les réactifs sont en **proportions stœchiométriques**.
""",
                'quiz': {
                    'titre': "Quiz — État initial, état final et tableau d'avancement",
                    'score_minimum': 60.0,
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "L'avancement x d'une réaction s'exprime en :",
                            'options': ["mol", "g", "L", "mol/L"],
                            'reponse_correcte': '0',
                            'explication': "L'avancement x est une quantité de matière qui mesure la progression de la réaction. Il s'exprime en mol.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "À l'état initial d'une transformation chimique, l'avancement vaut :",
                            'options': ["x = 0", "x = xmax", "x = 1", "x est indéterminé"],
                            'reponse_correcte': '0',
                            'explication': "Par définition, l'avancement vaut 0 à l'état initial (la réaction n'a pas encore débuté) et xmax à l'état final.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Le réactif limitant est celui qui :",
                            'options': ["Est entièrement consommé en premier", "Est en plus grande quantité", "A la plus grande masse molaire", "Est ajouté en dernier"],
                            'reponse_correcte': '0',
                            'explication': "Le réactif limitant est celui dont la quantité de matière atteint 0 en premier, imposant la valeur de xmax.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Dans le tableau d'avancement, la quantité d'un réactif A (coefficient a) à l'avancement x s'écrit :",
                            'options': ["nA,0 − a·x", "nA,0 + a·x", "nA,0 × a·x", "nA,0 / a"],
                            'reponse_correcte': '0',
                            'explication': "La quantité d'un réactif diminue : n(A) = nA,0 − a·x, où a est le coefficient stœchiométrique de A.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Si les réactifs sont en proportions stœchiométriques :",
                            'options': ["Ils sont tous totalement consommés à l'état final", "Il reste toujours un excès de l'un d'eux", "La réaction ne peut pas avoir lieu", "L'avancement maximal est nul"],
                            'reponse_correcte': '0',
                            'explication': "Les proportions stœchiométriques signifient que nA,0/a = nB,0/b : les deux réactifs sont totalement consommés.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Pour la réaction 2 H₂ + O₂ → 2 H₂O, si n(H₂)₀ = 0,4 mol et n(O₂)₀ = 0,3 mol :",
                            'options': ["H₂ est le réactif limitant, xmax = 0,2 mol", "O₂ est le réactif limitant, xmax = 0,3 mol", "Les réactifs sont en proportions stœchiométriques", "H₂ est le réactif limitant, xmax = 0,4 mol"],
                            'reponse_correcte': '0',
                            'explication': "n(H₂)/2 = 0,2 mol et n(O₂)/1 = 0,3 mol. Le plus petit est 0,2 (H₂), donc H₂ est le réactif limitant et xmax = 0,2 mol.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Pour la réaction N₂ + 3 H₂ → 2 NH₃, avec n(N₂)₀ = 0,1 mol et n(H₂)₀ = 0,6 mol, quel est le réactif limitant ?",
                            'options': ["N₂", "H₂", "NH₃", "Les deux sont limitants"],
                            'reponse_correcte': '0',
                            'explication': "n(N₂)/1 = 0,1 mol et n(H₂)/3 = 0,2 mol. Le plus petit est 0,1 (N₂), donc N₂ est le réactif limitant.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "On part de 0,30 mol de Fe et 0,15 mol de O₂ pour 3 Fe + 2 O₂ → Fe₃O₄. Quelle quantité de Fe₃O₄ est formée ?",
                            'options': ["0,075 mol", "0,10 mol", "0,15 mol", "0,30 mol"],
                            'reponse_correcte': '0',
                            'explication': "xmax,Fe = 0,30/3 = 0,10 ; xmax,O₂ = 0,15/2 = 0,075. Le limitant est O₂, xmax = 0,075 mol. n(Fe₃O₄) = xmax = 0,075 mol.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Un réactif en excès est un réactif qui :",
                            'options': ["N'est pas entièrement consommé à l'état final", "Est entièrement consommé en premier", "N'est pas présent à l'état initial", "Apparaît dans les produits"],
                            'reponse_correcte': '0',
                            'explication': "Le réactif en excès n'est pas totalement consommé : il en reste à l'état final, contrairement au réactif limitant.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Pour 2 Al + 3 Cl₂ → 2 AlCl₃, on part de 0,10 mol d'Al et 0,12 mol de Cl₂. La quantité d'Al restant à l'état final est :",
                            'options': ["0,02 mol", "0 mol", "0,10 mol", "0,06 mol"],
                            'reponse_correcte': '0',
                            'explication': "xmax,Al = 0,10/2 = 0,05 ; xmax,Cl₂ = 0,12/3 = 0,04. Limitant : Cl₂, xmax = 0,04. n(Al) restant = 0,10 − 2×0,04 = 0,02 mol.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Pour CH₄ + 2 O₂ → CO₂ + 2 H₂O, on mélange 0,5 mol de CH₄ et 0,8 mol de O₂. La quantité d'eau formée est :",
                            'options': ["0,8 mol", "1,0 mol", "0,4 mol", "0,5 mol"],
                            'reponse_correcte': '0',
                            'explication': "xmax,CH₄ = 0,5/1 = 0,5 ; xmax,O₂ = 0,8/2 = 0,4. Limitant : O₂, xmax = 0,4. n(H₂O) = 2 × 0,4 = 0,8 mol.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 12,
                            'type': 'vrai_faux',
                            'texte': "L'avancement maximal correspond à la consommation totale du réactif limitant.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "Par définition, xmax est atteint lorsque le réactif limitant est totalement consommé (sa quantité atteint 0).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'vrai_faux',
                            'texte': "Dans un tableau d'avancement, les quantités de matière des produits diminuent au cours de la réaction.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "Les quantités de produits augmentent (n = n₀ + ν·x). Ce sont les quantités de réactifs qui diminuent.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Si n(A)/a < n(B)/b, alors B est le réactif limitant.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "C'est l'inverse : le réactif limitant est celui dont le rapport n/coefficient est le plus petit. Ici, c'est A.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "À l'état final d'une réaction totale, il peut rester du réactif en excès dans le milieu.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "Si les réactifs ne sont pas en proportions stœchiométriques, le réactif en excès n'est pas complètement consommé.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Pour la réaction A + 2B → C, si on part de 1 mol de A et 2 mol de B, les réactifs sont en proportions stœchiométriques.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "n(A)/1 = 1 et n(B)/2 = 1. Les deux rapports sont égaux : les réactifs sont bien en proportions stœchiométriques.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on le réactif qui est entièrement consommé à la fin de la réaction ?",
                            'options': None,
                            'reponse_correcte': 'réactif limitant',
                            'tolerances': ['le réactif limitant', 'reactif limitant', 'Réactif limitant', 'Le réactif limitant'],
                            'explication': "Le réactif limitant est celui qui est entièrement consommé, imposant l'avancement maximal.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Pour la réaction A + 3B → 2C, avec n(A)₀ = 0,2 mol et n(B)₀ = 0,9 mol, quelle est la valeur de xmax en mol ?",
                            'options': None,
                            'reponse_correcte': '0,2',
                            'tolerances': ['0.2', '0,20', '0.20', '0,2 mol', '0.2 mol'],
                            'explication': "xmax,A = 0,2/1 = 0,2 ; xmax,B = 0,9/3 = 0,3. Le plus petit est 0,2, donc xmax = 0,2 mol.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Pour la réaction 2 H₂ + O₂ → 2 H₂O, on part de 0,6 mol de H₂ et 0,5 mol de O₂. Quel est le réactif limitant ?",
                            'options': None,
                            'reponse_correcte': 'H2',
                            'tolerances': ['H₂', 'h2', 'dihydrogène', 'le dihydrogène', 'Le dihydrogène'],
                            'explication': "n(H₂)/2 = 0,3 mol et n(O₂)/1 = 0,5 mol. Le plus petit rapport est 0,3 (H₂), donc H₂ est le réactif limitant.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Pour 3 Fe + 2 O₂ → Fe₃O₄, on part de 0,60 mol de Fe et 0,30 mol de O₂. Quelle quantité de fer (en mol) reste à l'état final ?",
                            'options': None,
                            'reponse_correcte': '0,15',
                            'tolerances': ['0.15', '0,15 mol', '0.15 mol'],
                            'explication': "xmax,Fe = 0,60/3 = 0,20 ; xmax,O₂ = 0,30/2 = 0,15. Limitant : O₂, xmax = 0,15. n(Fe) = 0,60 − 3×0,15 = 0,15 mol.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 8 — Réactions chimiques et stœchiométrie
    # ──────────────────────────────────────────────
    {
        'ordre': 8,
        'titre': 'Réactions chimiques et stœchiométrie',
        'description': "Exploiter quantitativement une équation de réaction pour réaliser des bilans de matière, calculer des masses et des volumes de gaz, et déterminer le rendement d'une réaction.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Bilan de matière — masses et volumes',
                'duree': 40,
                'contenu': """# Bilan de matière — masses et volumes

## Introduction

L'équation de réaction et le tableau d'avancement permettent de calculer les quantités de matière mises en jeu. Mais en pratique, au laboratoire, on mesure des **masses** (balance) et des **volumes** (éprouvette, seringue). Il faut donc savoir convertir les quantités de matière en masses et en volumes, et inversement.

---

## Rappels — relations fondamentales

### Quantité de matière et masse

$$n = \\frac{m}{M}$$

| Grandeur | Symbole | Unité |
|----------|---------|-------|
| Quantité de matière | $n$ | mol |
| Masse | $m$ | g |
| Masse molaire | $M$ | g/mol |

### Quantité de matière et volume (solutions)

$$n = C \\times V$$

| Grandeur | Symbole | Unité |
|----------|---------|-------|
| Quantité de matière | $n$ | mol |
| Concentration molaire | $C$ | mol/L |
| Volume de solution | $V$ | L |

### Quantité de matière et volume (gaz)

$$n = \\frac{V_{\\text{gaz}}}{V_m}$$

| Grandeur | Symbole | Unité |
|----------|---------|-------|
| Quantité de matière | $n$ | mol |
| Volume du gaz | $V_{\\text{gaz}}$ | L |
| Volume molaire | $V_m$ | L/mol |

> **Rappel :** $V_m = 24{,}0$ L/mol dans les conditions ambiantes (20 °C, $1{,}013 \\times 10^5$ Pa).

---

## Méthode générale — bilan de matière

Pour résoudre un problème de stœchiométrie, on suit ces étapes :

1. **Écrire et équilibrer** l'équation de réaction.
2. **Calculer** les quantités de matière initiales $n_0$ de chaque réactif.
3. **Construire** le tableau d'avancement.
4. **Déterminer** $x_{max}$ et le réactif limitant.
5. **Calculer** les quantités à l'état final.
6. **Convertir** en masses ou volumes selon ce qui est demandé.

---

## Application 1 — Combustion du méthane

### Énoncé

On brûle $V_{CH_4} = 2{,}4$ L de méthane $CH_4$ dans un excès de dioxygène. Calculer :

a) La quantité de matière de $CH_4$

b) Le volume de $CO_2$ produit

c) La masse d'eau produite

($V_m = 24{,}0$ L/mol, $M_{H_2O} = 18{,}0$ g/mol)

### Résolution

**Équation :**
$$CH_4 + 2\\,O_2 \\longrightarrow CO_2 + 2\\,H_2O$$

**a)** Quantité de méthane :
$$n_{CH_4} = \\frac{V_{CH_4}}{V_m} = \\frac{2{,}4}{24{,}0} = 0{,}10 \\text{ mol}$$

**b)** D'après l'équation, 1 mol de $CH_4$ produit 1 mol de $CO_2$ :
$$n_{CO_2} = n_{CH_4} = 0{,}10 \\text{ mol}$$
$$V_{CO_2} = n_{CO_2} \\times V_m = 0{,}10 \\times 24{,}0 = 2{,}4 \\text{ L}$$

**c)** D'après l'équation, 1 mol de $CH_4$ produit 2 mol de $H_2O$ :
$$n_{H_2O} = 2 \\times n_{CH_4} = 2 \\times 0{,}10 = 0{,}20 \\text{ mol}$$
$$m_{H_2O} = n_{H_2O} \\times M_{H_2O} = 0{,}20 \\times 18{,}0 = 3{,}6 \\text{ g}$$

---

## Application 2 — Réaction en solution

### Énoncé

On verse $V_1 = 20{,}0$ mL d'une solution d'acide chlorhydrique de concentration $C_1 = 0{,}50$ mol/L sur $m_{Zn} = 1{,}3$ g de zinc en poudre.

$$Zn + 2\\,H^+ \\longrightarrow Zn^{2+} + H_2$$

Déterminer le réactif limitant et le volume de dihydrogène dégagé.

($M_{Zn} = 65{,}4$ g/mol, $V_m = 24{,}0$ L/mol)

### Résolution

**Quantités initiales :**
$$n_{Zn} = \\frac{m_{Zn}}{M_{Zn}} = \\frac{1{,}3}{65{,}4} = 0{,}020 \\text{ mol}$$

$$n_{H^+} = C_1 \\times V_1 = 0{,}50 \\times 0{,}0200 = 0{,}010 \\text{ mol}$$

**Détermination du réactif limitant :**
$$\\frac{n_{Zn}}{1} = 0{,}020 \\quad ; \\quad \\frac{n_{H^+}}{2} = 0{,}005$$

$\\frac{n_{H^+}}{2} < \\frac{n_{Zn}}{1}$ donc $H^+$ est le **réactif limitant**.

$$x_{max} = 0{,}005 \\text{ mol}$$

**Volume de dihydrogène :**
$$n_{H_2} = x_{max} = 0{,}005 \\text{ mol}$$
$$V_{H_2} = n_{H_2} \\times V_m = 0{,}005 \\times 24{,}0 = 0{,}12 \\text{ L} = 120 \\text{ mL}$$

---

## Vérification par la conservation de la masse

On peut toujours vérifier un calcul stœchiométrique en contrôlant que :

$$\\sum m_{\\text{réactifs consommés}} = \\sum m_{\\text{produits formés}}$$

### Vérification de l'application 1

- $m_{CH_4} = 0{,}10 \\times 16{,}0 = 1{,}6$ g
- $m_{O_2} = 0{,}20 \\times 32{,}0 = 6{,}4$ g
- Total réactifs : $1{,}6 + 6{,}4 = 8{,}0$ g

- $m_{CO_2} = 0{,}10 \\times 44{,}0 = 4{,}4$ g
- $m_{H_2O} = 0{,}20 \\times 18{,}0 = 3{,}6$ g
- Total produits : $4{,}4 + 3{,}6 = 8{,}0$ g ✓

---

## À retenir

- Pour passer des quantités de matière aux grandeurs mesurables : $m = n \\times M$ (masse), $V = n \\times V_m$ (gaz), $n = C \\times V$ (solution).
- La **méthode générale** : équation → quantités initiales → tableau d'avancement → $x_{max}$ → quantités finales → conversion.
- On peut **vérifier** un calcul stœchiométrique par la conservation de la masse.
- Le $V_m = 24{,}0$ L/mol est valable dans les **conditions ambiantes** (20 °C, pression atmosphérique).
""",
                'quiz': {
                    'titre': 'Quiz — Bilan de matière, masses et volumes',
                    'score_minimum': 60.0,
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "La relation n = m/M permet de calculer :",
                            'options': ["La quantité de matière à partir de la masse et de la masse molaire", "La masse volumique d'un corps", "Le volume molaire d'un gaz", "La concentration molaire d'une solution"],
                            'reponse_correcte': '0',
                            'explication': "n = m/M relie la quantité de matière (mol), la masse (g) et la masse molaire (g/mol) de n'importe quelle espèce.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Le volume molaire Vm dans les conditions ambiantes (20 °C, 1 atm) vaut environ :",
                            'options': ["24,0 L/mol", "22,4 L/mol", "12,0 L/mol", "1,0 L/mol"],
                            'reponse_correcte': '0',
                            'explication': "Vm = 24,0 L/mol dans les conditions ambiantes. 22,4 L/mol correspond aux conditions normales (0 °C, 1 atm).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Pour un gaz, la quantité de matière se calcule par :",
                            'options': ["n = V / Vm", "n = m × M", "n = C / V", "n = Vm × V"],
                            'reponse_correcte': '0',
                            'explication': "Pour un gaz : n = V(gaz) / Vm, avec V en L et Vm en L/mol.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Pour une solution, la quantité de matière de soluté est :",
                            'options': ["n = C × V", "n = C / V", "n = V / C", "n = m × C"],
                            'reponse_correcte': '0',
                            'explication': "n = C × V, avec C la concentration molaire (mol/L) et V le volume de solution (L).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "On dispose de 3,6 g d'eau (M = 18,0 g/mol). La quantité de matière est :",
                            'options': ["0,20 mol", "0,36 mol", "18,0 mol", "0,50 mol"],
                            'reponse_correcte': '0',
                            'explication': "n = m / M = 3,6 / 18,0 = 0,20 mol.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Lors de la combustion CH₄ + 2 O₂ → CO₂ + 2 H₂O, 0,10 mol de CH₄ brûle. Le volume de CO₂ dégagé (Vm = 24,0 L/mol) est :",
                            'options': ["2,4 L", "4,8 L", "24,0 L", "0,24 L"],
                            'reponse_correcte': '0',
                            'explication': "1 mol CH₄ → 1 mol CO₂, donc n(CO₂) = 0,10 mol. V = n × Vm = 0,10 × 24,0 = 2,4 L.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "On verse 20,0 mL de solution HCl à C = 0,50 mol/L. La quantité de H⁺ introduite est :",
                            'options': ["0,010 mol", "0,10 mol", "10 mol", "0,001 mol"],
                            'reponse_correcte': '0',
                            'explication': "n = C × V = 0,50 × 0,0200 = 0,010 mol. Attention : V doit être converti en litres.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Pour vérifier un calcul stœchiométrique, on peut contrôler que :",
                            'options': ["La somme des masses des réactifs consommés égale celle des produits formés", "Le volume total est conservé", "La température ne change pas", "Les concentrations sont égales"],
                            'reponse_correcte': '0',
                            'explication': "La conservation de la masse (loi de Lavoisier) permet de vérifier : Σ m(réactifs consommés) = Σ m(produits formés).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "La masse de 0,50 mol de dioxyde de carbone CO₂ (M = 44,0 g/mol) est :",
                            'options': ["22,0 g", "44,0 g", "88,0 g", "11,0 g"],
                            'reponse_correcte': '0',
                            'explication': "m = n × M = 0,50 × 44,0 = 22,0 g.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "On brûle 4,8 L de propane C₃H₈ (Vm = 24,0 L/mol). D'après C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O, la masse d'eau formée (M = 18,0 g/mol) est :",
                            'options': ["14,4 g", "7,2 g", "3,6 g", "28,8 g"],
                            'reponse_correcte': '0',
                            'explication': "n(C₃H₈) = 4,8/24,0 = 0,20 mol. n(H₂O) = 4 × 0,20 = 0,80 mol. m = 0,80 × 18,0 = 14,4 g.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Zn + 2 H⁺ → Zn²⁺ + H₂. On fait réagir 1,3 g de Zn (M = 65,4 g/mol) avec 20,0 mL de HCl à 0,50 mol/L. Le volume de H₂ dégagé (Vm = 24,0 L/mol) est :",
                            'options': ["120 mL", "240 mL", "480 mL", "60 mL"],
                            'reponse_correcte': '0',
                            'explication': "n(Zn) = 0,020 mol, n(H⁺) = 0,010 mol. xmax = min(0,020 ; 0,005) = 0,005 mol (H⁺ limitant). V(H₂) = 0,005 × 24,0 = 0,12 L = 120 mL.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 12,
                            'type': 'vrai_faux',
                            'texte': "La relation n = m/M n'est valable que pour les gaz.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "n = m/M est universelle : elle s'applique à toute espèce chimique (solide, liquide ou gaz).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'vrai_faux',
                            'texte': "Le volume molaire Vm dépend des conditions de température et de pression.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "Vm vaut 22,4 L/mol à 0 °C et 1 atm (conditions normales) mais 24,0 L/mol à 20 °C et 1 atm (conditions ambiantes).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Lors d'une réaction chimique, le volume total des gaz est toujours conservé.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "C'est la masse qui est conservée, pas le volume. Le nombre total de moles de gaz peut changer (ex : N₂ + 3 H₂ → 2 NH₃ : 4 mol de gaz → 2 mol).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "La relation n = C × V est utilisée pour calculer la quantité de matière d'un soluté en solution.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "n = C × V, avec C la concentration molaire (mol/L) et V le volume de solution (L).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Si on consomme 2 mol de O₂ (M = 32,0 g/mol), la masse de O₂ consommée vaut 64,0 g.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "m = n × M = 2 × 32,0 = 64,0 g.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Quelle est l'unité de la masse molaire M ?",
                            'options': None,
                            'reponse_correcte': 'g/mol',
                            'tolerances': ['g.mol-1', 'g·mol⁻¹', 'g.mol⁻¹', 'gramme par mole'],
                            'explication': "La masse molaire s'exprime en grammes par mole (g/mol ou g·mol⁻¹).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "On dispose de 4,4 g de CO₂ (M = 44,0 g/mol). Quelle est la quantité de matière en mol ?",
                            'options': None,
                            'reponse_correcte': '0,10',
                            'tolerances': ['0.10', '0,1', '0.1', '0,10 mol', '0.10 mol'],
                            'explication': "n = m / M = 4,4 / 44,0 = 0,10 mol.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Quel est le volume occupé par 0,50 mol de gaz dans les conditions ambiantes (Vm = 24,0 L/mol), en L ?",
                            'options': None,
                            'reponse_correcte': '12',
                            'tolerances': ['12,0', '12.0', '12 L', '12,0 L'],
                            'explication': "V = n × Vm = 0,50 × 24,0 = 12,0 L.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "On brûle 1,2 L de méthane CH₄ (Vm = 24,0 L/mol). D'après CH₄ + 2 O₂ → CO₂ + 2 H₂O, quelle masse d'eau (en g) est produite ? (M = 18,0 g/mol)",
                            'options': None,
                            'reponse_correcte': '1,8',
                            'tolerances': ['1.8', '1,80', '1.80', '1,8 g', '1.8 g'],
                            'explication': "n(CH₄) = 1,2/24,0 = 0,050 mol. n(H₂O) = 2 × 0,050 = 0,10 mol. m = 0,10 × 18,0 = 1,8 g.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Rendement et transformations totales ou partielles',
                'duree': 35,
                'contenu': """# Rendement et transformations totales ou partielles

## Introduction

En théorie, une réaction chimique convertit les réactifs en produits selon les proportions dictées par l'équation bilan. En pratique, la quantité de produit réellement obtenue est souvent **inférieure** à la quantité prévue par le calcul. Le **rendement** permet de quantifier cette différence.

---

## Transformation totale et transformation non totale

### Transformation totale

Une transformation est **totale** lorsque le réactif limitant est **entièrement consommé**. L'avancement final est égal à l'avancement maximal :

$$x_{\\text{final}} = x_{max}$$

> La flèche simple $\\longrightarrow$ dans l'équation de réaction indique conventionnellement une transformation considérée comme totale.

### Transformation non totale (partielle)

Une transformation est **non totale** (ou partielle) lorsqu'elle s'arrête avant la consommation complète du réactif limitant. Il reste des réactifs et des produits coexistent dans le milieu.

$$x_{\\text{final}} < x_{max}$$

> On utilise alors la double flèche $\\rightleftharpoons$ pour signifier que la réaction est un **équilibre** (programme de Première et Terminale).

---

## Le rendement d'une réaction

### Définition

Le **rendement** $r$ (ou $\\eta$) d'une réaction est le rapport entre la quantité de produit **réellement obtenue** et la quantité de produit **théoriquement attendue** (calculée par le tableau d'avancement en supposant la réaction totale) :

$$\\boxed{r = \\frac{n_{\\text{obtenu}}}{n_{\\text{théorique}}} \\times 100\\%}$$

On peut aussi l'exprimer avec les masses :

$$r = \\frac{m_{\\text{obtenue}}}{m_{\\text{théorique}}} \\times 100\\%$$

- $r = 100\\%$ : la réaction est **totale** et sans pertes.
- $r < 100\\%$ : pertes lors de la manipulation ou réaction non totale.

---

## Causes d'un rendement inférieur à 100 %

Plusieurs facteurs expliquent que le rendement réel est souvent inférieur au rendement théorique :

| Cause | Explication |
|-------|-------------|
| **Réaction non totale** | La réaction s'arrête avant consommation complète du réactif limitant (équilibre chimique) |
| **Réactions parasites** | D'autres réactions se produisent simultanément, consommant une partie des réactifs |
| **Pertes lors des transferts** | Lors des transvasements, filtrations, etc., une partie de la matière reste sur la verrerie |
| **Purification** | Les étapes de purification (lavage, recristallisation) entraînent des pertes de produit |

---

## Application — synthèse de l'aspirine

### Énoncé

On fait réagir $m_1 = 2{,}0$ g d'acide salicylique ($M_1 = 138$ g/mol) avec un excès d'anhydride acétique pour synthétiser de l'aspirine (acide acétylsalicylique, $M_2 = 180$ g/mol) :

$$C_7H_6O_3 + C_4H_6O_3 \\longrightarrow C_9H_8O_4 + CH_3COOH$$

Après filtration et séchage, on recueille $m_{\\text{exp}} = 1{,}7$ g d'aspirine. Calculer le rendement.

### Résolution

**Étape 1 — Quantité initiale de réactif limitant :**

L'acide salicylique est le réactif limitant (l'anhydride acétique est en excès) :
$$n_1 = \\frac{m_1}{M_1} = \\frac{2{,}0}{138} = 1{,}45 \\times 10^{-2} \\text{ mol}$$

**Étape 2 — Quantité théorique d'aspirine :**

D'après l'équation, les coefficients sont tous égaux à 1, donc :
$$n_{\\text{théo}} = n_1 = 1{,}45 \\times 10^{-2} \\text{ mol}$$

**Étape 3 — Masse théorique :**
$$m_{\\text{théo}} = n_{\\text{théo}} \\times M_2 = 1{,}45 \\times 10^{-2} \\times 180 = 2{,}6 \\text{ g}$$

**Étape 4 — Rendement :**
$$r = \\frac{m_{\\text{exp}}}{m_{\\text{théo}}} \\times 100 = \\frac{1{,}7}{2{,}6} \\times 100 \\approx 65\\%$$

> Le rendement est de **65 %** : environ un tiers de la masse a été perdu lors des étapes de purification et de transfert.

---

## Optimisation du rendement

En chimie, on cherche à **maximiser le rendement** d'une synthèse. Les stratégies possibles sont :

| Stratégie | Principe |
|-----------|----------|
| **Excès d'un réactif** | Mettre l'un des réactifs en large excès pour forcer la consommation totale de l'autre |
| **Élimination d'un produit** | Retirer un produit du milieu au fur et à mesure (distillation, précipitation) pour déplacer l'équilibre |
| **Choix du solvant** | Un solvant adapté peut favoriser la réaction souhaitée |
| **Température et catalyseur** | Modifier les conditions pour accélérer la réaction et favoriser la transformation |
| **Soins expérimentaux** | Minimiser les pertes lors des transferts et de la purification |

---

## Bilan par un schéma

Pour résumer la démarche complète de résolution d'un problème de stœchiométrie :

**Données de l'énoncé** (masses, volumes, concentrations)

↓ Conversion ($n = m/M$, $n = C \\times V$, $n = V_{gaz}/V_m$)

**Quantités de matière initiales**

↓ Tableau d'avancement → $x_{max}$

**Quantités de matière finales**

↓ Conversion inverse ($m = n \\times M$, etc.)

**Résultats** (masses, volumes des produits)

↓ Comparaison avec l'expérience

**Rendement** : $r = \\frac{n_{obtenu}}{n_{théorique}} \\times 100\\%$

---

## À retenir

- Une **transformation totale** consomme entièrement le réactif limitant ($x_{final} = x_{max}$).
- Le **rendement** $r = \\frac{n_{\\text{obtenu}}}{n_{\\text{théorique}}} \\times 100\\%$ mesure l'efficacité de la réaction.
- Un rendement $< 100\\%$ s'explique par des pertes expérimentales, des réactions parasites ou une réaction non totale.
- En pratique, on optimise le rendement en travaillant avec un **excès de réactif**, en éliminant un produit, ou en améliorant le protocole.
""",
                'quiz': {
                    'titre': 'Quiz — Rendement et transformations totales ou partielles',
                    'score_minimum': 60.0,
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Une transformation est totale lorsque :",
                            'options': ["Le réactif limitant est entièrement consommé", "Aucun produit n'est formé", "Les réactifs restent intacts", "Le rendement est nul"],
                            'reponse_correcte': '0',
                            'explication': "Une transformation totale signifie que le réactif limitant est entièrement consommé : xfinal = xmax.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Le rendement d'une réaction se calcule par :",
                            'options': ["r = (n_obtenu / n_théorique) × 100 %", "r = n_théorique × n_obtenu", "r = (n_théorique / n_obtenu) × 100 %", "r = m × M × 100 %"],
                            'reponse_correcte': '0',
                            'explication': "Le rendement compare la quantité réellement obtenue à la quantité théoriquement attendue : r = (n_obtenu / n_théorique) × 100 %.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Un rendement de 100 % signifie que :",
                            'options': ["La réaction est totale et sans pertes expérimentales", "La réaction n'a pas eu lieu", "Il y a eu des pertes importantes", "La réaction est partielle"],
                            'reponse_correcte': '0',
                            'explication': "r = 100 % signifie que toute la quantité théorique de produit a été obtenue, sans aucune perte.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quelle est la cause la plus courante d'un rendement inférieur à 100 % au lycée ?",
                            'options': ["Les pertes lors des transferts et de la purification", "La température est trop élevée", "La balance est mal calibrée", "On utilise trop de réactifs"],
                            'reponse_correcte': '0',
                            'explication': "Au laboratoire, les pertes lors des transvasements, filtrations et purifications sont la cause principale d'un rendement inférieur à 100 %.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Une transformation non totale (partielle) est conventionnellement symbolisée par :",
                            'options': ["Une double flèche ⇌", "Une flèche simple →", "Un signe égal =", "Un signe plus +"],
                            'reponse_correcte': '0',
                            'explication': "La double flèche ⇌ indique un équilibre chimique, c'est-à-dire une réaction non totale (partielle).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "On obtient expérimentalement 1,7 g d'aspirine alors qu'on attendait théoriquement 2,6 g. Le rendement est environ :",
                            'options': ["65 %", "153 %", "35 %", "17 %"],
                            'reponse_correcte': '0',
                            'explication': "r = (1,7 / 2,6) × 100 ≈ 65 %.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Pour augmenter le rendement d'une réaction, on peut :",
                            'options': ["Mettre un réactif en large excès", "Diminuer la quantité de réactifs", "Ajouter de l'eau distillée", "Ne rien changer au protocole"],
                            'reponse_correcte': '0',
                            'explication': "Mettre un réactif en excès permet de favoriser la consommation totale de l'autre réactif et d'augmenter le rendement.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Lors d'une synthèse, l'étape de recristallisation sert à :",
                            'options': ["Purifier un produit solide", "Accélérer la réaction", "Augmenter la masse de produit", "Chauffer le milieu réactionnel"],
                            'reponse_correcte': '0',
                            'explication': "La recristallisation purifie un solide : on le dissout à chaud dans un solvant, puis on refroidit pour obtenir des cristaux purs.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Si une réaction est non totale (partielle), alors :",
                            'options': ["L'avancement final est inférieur à l'avancement maximal", "Tout le réactif limitant est consommé", "Le rendement est de 100 %", "Il n'y a pas de produit formé"],
                            'reponse_correcte': '0',
                            'explication': "Pour une réaction non totale : xfinal < xmax. Il reste du réactif limitant et les réactifs coexistent avec les produits.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "On fait réagir 2,0 g d'acide salicylique (M = 138 g/mol) avec un excès d'anhydride acétique pour former de l'aspirine (M = 180 g/mol, coeff. 1:1). La masse théorique d'aspirine est :",
                            'options': ["2,6 g", "1,5 g", "3,6 g", "0,26 g"],
                            'reponse_correcte': '0',
                            'explication': "n = 2,0/138 = 0,0145 mol. m_théo = 0,0145 × 180 = 2,6 g.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Un élève obtient 3,0 g de produit brut au lieu des 4,0 g théoriques. Après recristallisation, il n'a plus que 2,4 g de produit pur. Le rendement global est :",
                            'options': ["60 %", "75 %", "80 %", "30 %"],
                            'reponse_correcte': '0',
                            'explication': "Le rendement global se calcule avec la masse finale pure : r = (2,4 / 4,0) × 100 = 60 %.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 12,
                            'type': 'vrai_faux',
                            'texte': "Le rendement d'une réaction peut être supérieur à 100 %.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "Le rendement ne peut pas dépasser 100 %. Un résultat supérieur indiquerait des impuretés dans le produit ou une erreur expérimentale.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'vrai_faux',
                            'texte': "Un catalyseur est consommé pendant la réaction chimique.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "Un catalyseur accélère la réaction mais est retrouvé intact à la fin de la transformation. Il n'apparaît pas dans l'équation bilan.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Éliminer un produit du milieu réactionnel au fur et à mesure peut augmenter le rendement.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'vrai',
                            'explication': "Retirer un produit (par distillation, précipitation…) déplace l'équilibre dans le sens de la réaction et augmente le rendement.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Si la température de fusion mesurée est inférieure à la valeur tabulée, le produit est pur.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "Une Tf inférieure à la valeur tabulée ou une plage de fusion large indiquent la présence d'impuretés.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Pour une transformation non totale, l'avancement final xfinal est égal à xmax.",
                            'options': ['Vrai', 'Faux'],
                            'reponse_correcte': 'faux',
                            'explication': "Pour une transformation non totale, xfinal < xmax : la réaction s'arrête avant la consommation complète du réactif limitant.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on une réaction qui s'arrête avant la consommation complète du réactif limitant ?",
                            'options': None,
                            'reponse_correcte': 'transformation non totale',
                            'tolerances': ['réaction non totale', 'transformation partielle', 'réaction partielle', 'non totale', 'partielle'],
                            'explication': "Une transformation non totale (ou partielle) s'arrête avant que le réactif limitant ne soit entièrement consommé.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "On attend théoriquement 5,0 g de produit et on obtient 4,0 g. Quel est le rendement en % ?",
                            'options': None,
                            'reponse_correcte': '80',
                            'tolerances': ['80 %', '80%', '80,0', '80.0', '80,0 %'],
                            'explication': "r = (4,0 / 5,0) × 100 = 80 %.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Quel instrument de verrerie utilise-t-on lors du chauffage à reflux pour condenser les vapeurs et les renvoyer dans le ballon ?",
                            'options': None,
                            'reponse_correcte': 'réfrigérant',
                            'tolerances': ['un réfrigérant', 'réfrigérant à eau', 'le réfrigérant', 'le réfrigérant à eau', 'un réfrigérant à eau', 'condenseur'],
                            'explication': "Le réfrigérant à eau (vertical, au-dessus du ballon) condense les vapeurs qui retombent dans le ballon, évitant toute perte de matière.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "On synthétise un produit (M = 120 g/mol). La quantité théorique est 0,050 mol. On obtient expérimentalement 4,8 g. Quel est le rendement en % ?",
                            'options': None,
                            'reponse_correcte': '80',
                            'tolerances': ['80 %', '80%', '80,0', '80.0'],
                            'explication': "m_théo = 0,050 × 120 = 6,0 g. r = (4,8 / 6,0) × 100 = 80 %.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 9 — Synthèse chimique
    # ──────────────────────────────────────────────
    {
        'ordre': 9,
        'titre': 'Synthèse chimique',
        'description': "Comprendre le rôle de la chimie de synthèse, distinguer espèces naturelles et synthétiques, maîtriser un protocole de synthèse et les règles de sécurité au laboratoire.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Espèces chimiques naturelles et de synthèse',
                'duree': 30,
                'contenu': """# Espèces chimiques naturelles et de synthèse

## Introduction

La chimie joue un rôle essentiel dans notre quotidien : médicaments, matières plastiques, colorants, arômes, cosmétiques… De nombreuses espèces chimiques utilisées par l'Homme sont fabriquées par **synthèse chimique**. Mais la nature produit elle aussi une immense variété de molécules. Comment distinguer ces deux origines ? Et sont-elles réellement différentes ?

---

## Espèces chimiques naturelles

### Définition

Une **espèce chimique naturelle** est une espèce produite par un organisme vivant (animal, végétal, micro-organisme) ou formée par des processus géologiques, sans intervention humaine.

### Exemples

| Espèce chimique | Source naturelle | Utilisation |
|----------------|-----------------|-------------|
| Acide acétylsalicylique (aspirine) | Écorce de saule (salicine) | Médicament anti-douleur |
| Vanilline | Gousse de vanille | Arôme alimentaire |
| Caféine | Graines de café, feuilles de thé | Stimulant |
| Caoutchouc (polyisoprène) | Hévéa (arbre) | Élasticité, pneus |
| Pénicilline | Moisissure *Penicillium* | Antibiotique |
| Indigo | Plante indigotier | Colorant textile |

> **Remarque :** l'extraction d'espèces naturelles est parfois coûteuse, longue, et fournit de faibles quantités. C'est l'une des raisons du développement de la chimie de synthèse.

---

## Espèces chimiques de synthèse

### Définition

Une **espèce chimique de synthèse** est fabriquée par l'Homme au moyen de transformations chimiques, en laboratoire ou en usine.

On distingue deux cas :

### 1. Reproduction d'une espèce naturelle

L'espèce synthétisée est **identique** à l'espèce naturelle : même formule chimique, mêmes propriétés physiques et chimiques.

> **Exemple :** la vanilline de synthèse ($C_8H_8O_3$) est exactement la même molécule que la vanilline extraite de la gousse de vanille. Aucune analyse chimique ne peut les distinguer.

### 2. Création d'une espèce artificielle

L'espèce synthétisée **n'existe pas dans la nature**. On parle d'espèce **artificielle**.

> **Exemples :** le nylon, le polystyrène, l'aspartame (édulcorant), le téflon.

---

## Identité entre espèce naturelle et espèce de synthèse

### Principe fondamental

Une molécule est définie par sa **formule chimique** et sa **structure** (arrangement des atomes dans l'espace), **pas par son origine**.

> **Conséquence :** si une espèce de synthèse a la même formule et la même structure qu'une espèce naturelle, elles sont **rigoureusement identiques**. Leurs propriétés physiques ($T_f$, $T_{eb}$, $\\rho$, $n$) et chimiques (réactivité) sont les mêmes.

### Vérification expérimentale

On compare les propriétés de l'espèce naturelle et de l'espèce de synthèse :

| Méthode | Principe |
|---------|----------|
| **Température de fusion** | Même $T_f$ → même espèce |
| **Chromatographie (CCM)** | Même $R_f$ dans les mêmes conditions → même espèce |
| **Spectre IR** | Spectres superposables → même espèce |
| **Indice de réfraction** | Même $n$ → même espèce |

> **Conclusion :** la mention « naturel » sur un produit n'implique aucune supériorité chimique. La vitamine C d'un comprimé est identique à celle d'un citron.

---

## Pourquoi synthétiser ?

La chimie de synthèse répond à plusieurs enjeux :

| Enjeu | Explication | Exemple |
|-------|-------------|----------|
| **Coût** | La synthèse est souvent moins chère que l'extraction naturelle | Vanilline : 1 kg naturelle ≈ 1 200 € vs 15 € de synthèse |
| **Quantité** | La demande mondiale dépasse la capacité de la nature | Aspirine : 40 000 tonnes/an |
| **Disponibilité** | Certaines espèces naturelles sont rares ou menacées | Taxol (anticancéreux) issu de l'if du Pacifique |
| **Innovation** | Créer des matériaux aux propriétés nouvelles | Kevlar, Gore-Tex, silicones |
| **Pureté** | La synthèse contrôlée peut donner des espèces très pures | Principes actifs pharmaceutiques |

---

## Chimie verte — vers une synthèse responsable

La **chimie verte** (ou chimie durable) vise à concevoir des procédés chimiques plus respectueux de l'environnement et de la santé. Ses 12 principes fondateurs incluent :

1. **Prévention des déchets** plutôt que traitement après coup.
2. **Économie d'atomes** : maximiser l'incorporation des réactifs dans le produit final.
3. **Solvants et conditions plus sûrs** : remplacer les solvants toxiques par des alternatives vertes (eau, $CO_2$ supercritique).
4. **Efficacité énergétique** : travailler à température et pression ambiantes quand c'est possible.
5. **Utilisation de matières premières renouvelables**.

> **Enjeu sociétal :** la chimie de synthèse est indispensable, mais elle doit évoluer vers des pratiques plus durables pour limiter son impact environnemental.

---

## À retenir

- Une espèce chimique **naturelle** est produite par la nature ; une espèce **de synthèse** est fabriquée par l'Homme.
- Une espèce de synthèse peut être **identique** à l'espèce naturelle (même formule, mêmes propriétés) ou **artificielle** (n'existe pas dans la nature).
- On vérifie l'identité par comparaison des propriétés physiques ($T_f$, $R_f$, spectre IR…).
- La synthèse chimique permet de répondre aux besoins en quantité, en coût et en innovation.
- La **chimie verte** propose des principes pour rendre la synthèse plus respectueuse de l'environnement.
""",
                'quiz': {
                    'titre': 'Quiz — Espèces chimiques naturelles et de synthèse',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Qu'est-ce qu'une espèce chimique naturelle ?",
                            'options': ["Une espèce produite par un organisme vivant ou un processus géologique", "Une espèce fabriquée en laboratoire", "Une espèce qui n'existe pas dans la nature", "Une espèce toujours plus pure qu'une espèce de synthèse"],
                            'reponse_correcte': '0',
                            'explication': "Une espèce chimique naturelle est produite par un organisme vivant (animal, végétal, micro-organisme) ou par des processus géologiques, sans intervention humaine.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "La vanilline extraite de la gousse de vanille et la vanilline de synthèse sont :",
                            'options': ["Rigoureusement identiques (même formule, mêmes propriétés)", "Différentes car l'une est naturelle", "Identiques en formule mais différentes en propriétés", "Toujours distinguables par analyse chimique"],
                            'reponse_correcte': '0',
                            'explication': "La vanilline de synthèse (C₈H₈O₃) est exactement la même molécule que la vanilline naturelle. Aucune analyse chimique ne peut les distinguer.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Parmi ces espèces, laquelle est artificielle (n'existe pas dans la nature) ?",
                            'options': ["Le nylon", "La caféine", "La vanilline", "Le caoutchouc naturel"],
                            'reponse_correcte': '0',
                            'explication': "Le nylon est une espèce artificielle : il a été créé par l'Homme et n'existe pas dans la nature, contrairement à la caféine, la vanilline ou le caoutchouc.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quel est l'avantage principal de la synthèse chimique par rapport à l'extraction naturelle ?",
                            'options': ["Produire en grande quantité à moindre coût", "Obtenir des molécules toujours différentes des naturelles", "Éviter toute pollution", "Obtenir des espèces plus pures que dans la nature"],
                            'reponse_correcte': '0',
                            'explication': "La synthèse chimique permet de produire en grande quantité et à moindre coût. Par exemple, 1 kg de vanilline synthétique coûte environ 15 € contre 1 200 € pour la naturelle.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Comment vérifie-t-on qu'une espèce de synthèse est identique à l'espèce naturelle ?",
                            'options': ["En comparant leurs propriétés physiques (Tf, spectre IR, Rf)", "En regardant leur couleur", "En comparant leur prix", "En vérifiant leur date de fabrication"],
                            'reponse_correcte': '0',
                            'explication': "On compare les propriétés physiques : température de fusion, rapport frontal en CCM, spectre infrarouge. Si elles sont identiques, les espèces sont les mêmes.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "La pénicilline est une espèce chimique naturelle issue :",
                            'options': ["D'une moisissure (Penicillium)", "Du pétrole", "D'un minerai", "D'une réaction entre deux gaz"],
                            'reponse_correcte': '0',
                            'explication': "La pénicilline est un antibiotique naturel découvert par Alexander Fleming, produit par la moisissure Penicillium.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Qu'est-ce qui définit une molécule : son origine ou sa structure ?",
                            'options': ["Sa formule chimique et sa structure (arrangement des atomes)", "Son origine naturelle ou synthétique", "Sa couleur et son odeur", "Son prix sur le marché"],
                            'reponse_correcte': '0',
                            'explication': "Une molécule est définie par sa formule chimique et sa structure, pas par son origine. Naturelle ou synthétique, si la structure est la même, c'est la même molécule.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "L'aspartame est un édulcorant :",
                            'options': ["Artificiel (il n'existe pas dans la nature)", "Naturel (extrait de la canne à sucre)", "Identique au saccharose", "Extrait du miel"],
                            'reponse_correcte': '0',
                            'explication': "L'aspartame est une espèce artificielle créée par l'Homme. Il n'existe pas dans la nature et a été synthétisé pour remplacer le sucre.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "La chimie verte vise principalement à :",
                            'options': ["Concevoir des procédés chimiques plus respectueux de l'environnement", "Colorer les produits chimiques en vert", "Remplacer toute la chimie par des produits naturels", "Interdire la chimie de synthèse"],
                            'reponse_correcte': '0',
                            'explication': "La chimie verte (ou chimie durable) vise à concevoir des procédés chimiques plus respectueux de l'environnement et de la santé, selon ses 12 principes fondateurs.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quel principe de la chimie verte consiste à maximiser l'incorporation des réactifs dans le produit final ?",
                            'options': ["L'économie d'atomes", "La prévention des déchets", "L'efficacité énergétique", "L'utilisation de matières renouvelables"],
                            'reponse_correcte': '0',
                            'explication': "L'économie d'atomes vise à ce que le maximum d'atomes des réactifs se retrouve dans le produit final, minimisant ainsi les sous-produits et déchets.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Pourquoi la synthèse du taxol (anticancéreux) a-t-elle été développée ?",
                            'options': ["Car l'if du Pacifique (source naturelle) est rare et menacé", "Car le taxol naturel est toxique", "Car le taxol de synthèse est plus efficace", "Car l'extraction est instantanée"],
                            'reponse_correcte': '0',
                            'explication': "Le taxol naturel provient de l'écorce de l'if du Pacifique, un arbre rare. La synthèse permet d'obtenir le médicament sans menacer l'espèce.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "En CCM, si une espèce de synthèse et une espèce naturelle ont le même Rf dans les mêmes conditions, on peut conclure que :",
                            'options': ["Ce sont la même espèce chimique", "Elles ont des structures différentes", "L'espèce de synthèse est impure", "La CCM est mal réalisée"],
                            'reponse_correcte': '0',
                            'explication': "En CCM, un même Rf dans les mêmes conditions expérimentales indique que les deux espèces sont identiques.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Parmi ces affirmations sur les spectres IR, laquelle est correcte ?",
                            'options': ["Deux spectres IR superposables indiquent la même espèce chimique", "Chaque espèce a le même spectre IR quelle que soit sa concentration", "Le spectre IR ne dépend que de la masse molaire", "Le spectre IR est identique pour tous les isomères"],
                            'reponse_correcte': '0',
                            'explication': "Le spectre IR est une empreinte caractéristique d'une espèce chimique. Deux spectres superposables confirment qu'il s'agit de la même espèce.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Quelle méthode permet de vérifier la pureté d'un solide obtenu par synthèse ?",
                            'options': ["La mesure de la température de fusion", "La pesée de l'échantillon", "L'observation de sa couleur", "La mesure de son volume"],
                            'reponse_correcte': '0',
                            'explication': "Un corps pur solide a une température de fusion précise et constante. Si Tf est inférieure à la valeur tabulée ou si la plage de fusion est large, le produit contient des impuretés.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Un produit étiqueté 'naturel' est toujours chimiquement supérieur à son équivalent de synthèse.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La mention 'naturel' n'implique aucune supériorité chimique. Une espèce de synthèse identique à l'espèce naturelle a exactement les mêmes propriétés.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Le polystyrène est une espèce chimique artificielle.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Le polystyrène est une espèce artificielle : il a été créé par synthèse chimique et n'existe pas dans la nature.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "La chimie verte recommande de travailler à température et pression ambiantes quand c'est possible.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "L'efficacité énergétique est l'un des 12 principes de la chimie verte : on cherche à minimiser l'apport d'énergie en travaillant dans des conditions douces.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Donnez la formule chimique de la vanilline.",
                            'options': None,
                            'reponse_correcte': 'C8H8O3',
                            'tolerances': ['C₈H₈O₃', 'c8h8o3'],
                            'explication': "La vanilline a pour formule C₈H₈O₃, qu'elle soit d'origine naturelle ou synthétique.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on une espèce chimique de synthèse qui n'existe pas dans la nature ?",
                            'options': None,
                            'reponse_correcte': 'artificielle',
                            'tolerances': ['espèce artificielle', 'une espèce artificielle', 'espece artificielle'],
                            'explication': "Une espèce de synthèse qui n'existe pas dans la nature est qualifiée d'artificielle (ex : nylon, polystyrène, aspartame).",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quel est le prix approximatif de 1 kg de vanilline de synthèse (en euros) ?",
                            'options': None,
                            'reponse_correcte': '15',
                            'tolerances': ['15 euros', '15 €', 'environ 15', '15€'],
                            'explication': "La vanilline de synthèse coûte environ 15 € le kg, contre environ 1 200 € pour la vanilline naturelle extraite de la gousse de vanille.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Protocole de synthèse et sécurité au laboratoire',
                'duree': 35,
                'contenu': """# Protocole de synthèse et sécurité au laboratoire

## Introduction

Réaliser une synthèse chimique au laboratoire nécessite de suivre un **protocole expérimental** rigoureux et de respecter des **règles de sécurité** strictes. Cette leçon détaille les étapes d'une synthèse, les techniques courantes de purification et de caractérisation, ainsi que les précautions à prendre.

---

## Étapes d'une synthèse chimique

Une synthèse se déroule en trois grandes phases :

### Phase 1 — La transformation

C'est la **réaction chimique** proprement dite. On mélange les réactifs dans les proportions voulues et on apporte éventuellement de l'énergie (chauffage) ou un catalyseur.

#### Chauffage à reflux

De nombreuses synthèses nécessitent un **chauffage** pour accélérer la réaction. On utilise un montage à **reflux** pour éviter les pertes de matière par évaporation :

- Le **ballon** contient le mélange réactionnel, placé dans un chauffe-ballon.
- Le **réfrigérant à eau** (vertical, au-dessus du ballon) condense les vapeurs qui retombent dans le ballon.
- Des **grains de pierre ponce** (ou billes de verre) régularisent l'ébullition et évitent les projections (« bumping »).

> **Principe :** les vapeurs montent dans le réfrigérant, se condensent au contact de la paroi froide, et retombent dans le ballon. Rien ne s'échappe → la transformation peut durer longtemps sans perte de matière.

#### Rôle du catalyseur

Un **catalyseur** est une espèce chimique qui **accélère** la réaction sans être consommée. Il est retrouvé intact à la fin de la transformation.

> **Exemples :** acide sulfurique $H_2SO_4$ dans les estérifications, platine $Pt$ dans les hydrogénations.

---

### Phase 2 — Le traitement (isolement du produit brut)

Après la transformation, le milieu réactionnel contient le produit souhaité, mais aussi des réactifs en excès, des sous-produits et le solvant. Il faut **isoler** le produit.

#### Extraction liquide-liquide

Si le produit n'est pas miscible à l'eau, on utilise une **ampoule à décanter** :

1. Verser le mélange réactionnel et de l'eau dans l'ampoule.
2. Agiter, puis dégazer (ouvrir le robinet retourné).
3. Laisser décanter : deux phases se séparent.
4. Récupérer la phase qui contient le produit (phase organique, en général au-dessus si densité $< 1$).

> **Remarque :** la phase aqueuse est en dessous si elle est plus dense. On la soutire par le bas de l'ampoule.

#### Filtration

Si le produit est un **solide**, on le sépare du liquide par :
- **Filtration simple** (par gravité, entonnoir + papier filtre) — lente.
- **Filtration sous vide** (Büchner + fiole à vide) — rapide, produit plus sec.

#### Lavage

On lave le produit brut (liquide ou solide) pour éliminer les impuretés solubles dans l'eau.

#### Séchage

- Phase organique liquide : ajout d'un **desséchant** (sulfate de magnésium anhydre $MgSO_4$, sulfate de sodium anhydre $Na_2SO_4$), puis filtration pour retirer le desséchant.
- Solide : séchage à l'étuve ou à l'air libre.

---

### Phase 3 — La purification et l'analyse

#### Purification

| Technique | Type de produit | Principe |
|-----------|----------------|----------|
| **Recristallisation** | Solide | Dissolution à chaud dans un solvant minimum, puis refroidissement → cristaux purs |
| **Distillation** | Liquide | Séparation par différence de températures d'ébullition |

#### Caractérisation (vérification de la pureté et de l'identité)

| Méthode | Ce qu'on mesure | Critère d'identité |
|---------|----------------|-------------------|
| **Température de fusion** | $T_f$ (banc Kofler ou tube de Thiele) | Valeur précise = corps pur identifié |
| **Chromatographie CCM** | $R_f$ | Même $R_f$ que la référence |
| **Spectre IR** | Bandes d'absorption | Spectre superposable à la référence |
| **Indice de réfraction** | $n$ (réfractomètre) | Valeur concordante avec les tables |

> **Point clé :** si la $T_f$ mesurée est **inférieure** à la valeur tabulée ou si la plage de fusion est **large**, le produit contient encore des **impuretés**.

---

## Calcul du rendement

Rappel de la formule :

$$r = \\frac{m_{\\text{expérimentale}}}{m_{\\text{théorique}}} \\times 100\\%$$

Ou en quantité de matière :

$$r = \\frac{n_{\\text{obtenu}}}{n_{\\text{théorique}}} \\times 100\\%$$

> Un bon rendement au laboratoire de lycée se situe entre **50 %** et **80 %**. En industrie, les rendements sont optimisés à plus de **90 %**.

---

## Sécurité au laboratoire

### Les pictogrammes de danger (GHS)

Les produits chimiques portent des **pictogrammes de danger** normalisés (losange rouge sur fond blanc) :

| Pictogramme | Signification | Exemples |
|-------------|--------------|----------|
| **GHS02** — Flamme | Inflammable | Éthanol, acétone, éther |
| **GHS05** — Corrosion | Corrosif (attaque la peau et les métaux) | Acide chlorhydrique, soude concentrée |
| **GHS06** — Tête de mort | Toxicité aiguë (mortel ou très toxique) | Méthanol, cyanure |
| **GHS07** — Point d'exclamation | Irritant, nocif | Dichlorométhane, cyclohexane |
| **GHS08** — Silhouette | Danger pour la santé (cancérogène, mutagène…) | Benzène, formaldéhyde |
| **GHS09** — Environnement | Dangereux pour l'environnement aquatique | Pesticides, métaux lourds |

### Fiche de données de sécurité (FDS)

Chaque produit chimique est accompagné d'une **FDS** qui fournit :
- L'identification du produit et ses dangers.
- Les mesures de premiers secours.
- Les précautions de stockage et de manipulation.
- Les équipements de protection à utiliser.

### Équipements de protection individuelle (EPI)

| EPI | Protège contre |
|-----|---------------|
| **Blouse** en coton | Projections sur les vêtements |
| **Lunettes** de protection | Projections dans les yeux |
| **Gants** (nitrile, latex) | Contact cutané avec les produits |
| **Hotte aspirante** | Inhalation de vapeurs toxiques |

### Gestes de sécurité essentiels

1. **Toujours** porter blouse, lunettes et gants.
2. **Ne jamais** pipeter à la bouche (utiliser une propipette).
3. **Travailler sous hotte** pour les produits volatils ou toxiques.
4. **Ne jamais** chauffer un récipient clos (risque d'explosion).
5. **Rejeter** les déchets chimiques dans les **bidons** appropriés (pas dans l'évier).
6. **Lire** l'étiquette et la FDS **avant** d'utiliser un produit.
7. **Connaître** l'emplacement de la douche de sécurité, du rince-œil et de l'extincteur.

---

## Exemple complet — synthèse de l'aspirine

Résumons les étapes de la synthèse de l'aspirine au laboratoire :

### Équation bilan

$$C_7H_6O_3 + C_4H_6O_3 \\xrightarrow{H_2SO_4} C_9H_8O_4 + CH_3COOH$$

(Acide salicylique + anhydride acétique → aspirine + acide acétique)

| Phase | Action |
|-------|--------|
| **Transformation** | Chauffage à reflux (~80 °C, 15 min) avec quelques gouttes de $H_2SO_4$ (catalyseur) |
| **Isolement** | Refroidissement → cristallisation ; filtration sous vide (Büchner) |
| **Purification** | Recristallisation dans un mélange eau/éthanol |
| **Caractérisation** | Mesure de $T_f$ (attendu : 135 °C) ; CCM avec aspirine de référence |
| **Rendement** | Typiquement 60–70 % au lycée |

---

## À retenir

- Une synthèse comprend trois phases : **transformation** (réaction), **traitement** (isolement du produit brut), **purification et analyse**.
- Le **chauffage à reflux** permet de chauffer sans perdre de matière.
- On isole le produit par extraction (ampoule à décanter), filtration ou distillation.
- On vérifie la pureté par la $T_f$, la CCM ou le spectre IR.
- Le **rendement** mesure l'efficacité de la synthèse : $r = \\frac{m_{exp}}{m_{théo}} \\times 100\\%$.
- La **sécurité** est primordiale : EPI, pictogrammes GHS, FDS, gestes de prévention.
""",
                'quiz': {
                    'titre': 'Quiz — Protocole de synthèse et sécurité au laboratoire',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quelles sont les trois grandes phases d'une synthèse chimique ?",
                            'options': ["Transformation, traitement (isolement), purification et analyse", "Chauffage, refroidissement, filtration", "Dissolution, dilution, évaporation", "Extraction, distillation, chromatographie"],
                            'reponse_correcte': '0',
                            'explication': "Une synthèse comprend trois phases : la transformation (réaction chimique), le traitement (isolement du produit brut) et la purification suivie de l'analyse.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quel est le rôle du réfrigérant à eau dans un montage à reflux ?",
                            'options': ["Condenser les vapeurs pour qu'elles retombent dans le ballon", "Chauffer le mélange réactionnel", "Filtrer les impuretés", "Mesurer la température du mélange"],
                            'reponse_correcte': '0',
                            'explication': "Le réfrigérant à eau condense les vapeurs qui montent depuis le ballon : elles retombent dans le mélange, évitant toute perte de matière.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "À quoi servent les grains de pierre ponce dans un chauffage à reflux ?",
                            'options': ["À régulariser l'ébullition et éviter les projections", "À accélérer la réaction chimique", "À filtrer le mélange", "À colorer le mélange pour suivre la réaction"],
                            'reponse_correcte': '0',
                            'explication': "Les grains de pierre ponce (ou billes de verre) régularisent l'ébullition en créant des sites de nucléation, ce qui évite les projections brutales (bumping).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Qu'est-ce qu'un catalyseur ?",
                            'options': ["Une espèce qui accélère la réaction sans être consommée", "Un réactif qui est entièrement consommé", "Un produit formé pendant la réaction", "Un solvant utilisé pour dissoudre les réactifs"],
                            'reponse_correcte': '0',
                            'explication': "Un catalyseur accélère la réaction chimique sans être consommé : il est retrouvé intact à la fin de la transformation.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La filtration sous vide (Büchner) est préférée à la filtration simple car elle est :",
                            'options': ["Plus rapide et le produit obtenu est plus sec", "Moins chère et plus simple à mettre en place", "Plus lente mais plus précise", "Utilisée uniquement pour les liquides"],
                            'reponse_correcte': '0',
                            'explication': "La filtration sous vide avec un Büchner est plus rapide que la filtration par gravité et donne un produit solide plus sec.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quel instrument utilise-t-on pour séparer deux liquides non miscibles ?",
                            'options': ["Une ampoule à décanter", "Un réfrigérant à eau", "Un Büchner", "Un banc Kofler"],
                            'reponse_correcte': '0',
                            'explication': "L'ampoule à décanter permet de séparer deux liquides non miscibles en exploitant leur différence de densité.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Le pictogramme GHS02 (flamme) indique un produit :",
                            'options': ["Inflammable", "Corrosif", "Toxique", "Irritant"],
                            'reponse_correcte': '0',
                            'explication': "Le pictogramme GHS02 représente une flamme et signale un produit inflammable (ex : éthanol, acétone, éther).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Quel EPI protège les yeux contre les projections chimiques ?",
                            'options': ["Les lunettes de protection", "La blouse", "Les gants", "La hotte aspirante"],
                            'reponse_correcte': '0',
                            'explication': "Les lunettes de protection sont l'EPI spécifique pour protéger les yeux contre les projections de produits chimiques.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Lors de la synthèse de l'aspirine, quel montage est utilisé pour chauffer le mélange réactionnel ?",
                            'options': ["Un chauffage à reflux", "Un bain-marie simple", "Une distillation", "Une ampoule à décanter"],
                            'reponse_correcte': '0',
                            'explication': "La synthèse de l'aspirine utilise un chauffage à reflux (~80 °C, 15 min) pour accélérer la réaction sans perte de matière.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Que signifie une température de fusion mesurée inférieure à la valeur tabulée ?",
                            'options': ["Le produit contient encore des impuretés", "Le produit est plus pur que prévu", "Le thermomètre est mal calibré", "Le produit s'est décomposé"],
                            'reponse_correcte': '0',
                            'explication': "Si la Tf mesurée est inférieure à la valeur tabulée ou si la plage de fusion est large, le produit contient des impuretés qui abaissent le point de fusion.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "La recristallisation est une technique de purification pour :",
                            'options': ["Les produits solides", "Les produits liquides uniquement", "Les produits gazeux", "Tous les types de produits"],
                            'reponse_correcte': '0',
                            'explication': "La recristallisation purifie les solides : on dissout le produit à chaud dans un minimum de solvant, puis on refroidit pour obtenir des cristaux purs.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Dans la synthèse de l'aspirine, quel est le rôle de H₂SO₄ ?",
                            'options': ["Catalyseur", "Réactif principal", "Solvant", "Produit de la réaction"],
                            'reponse_correcte': '0',
                            'explication': "L'acide sulfurique H₂SO₄ est utilisé comme catalyseur dans la synthèse de l'aspirine : il accélère la réaction sans être consommé.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Le pictogramme GHS05 (corrosion) signale un produit qui :",
                            'options': ["Attaque la peau et les métaux", "Est inflammable", "Est nocif par inhalation", "Est dangereux pour l'environnement"],
                            'reponse_correcte': '0',
                            'explication': "Le pictogramme GHS05 (symbole de corrosion) signale un produit corrosif qui peut attaquer la peau et les métaux (ex : acide chlorhydrique, soude concentrée).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Quel desséchant utilise-t-on couramment pour sécher une phase organique liquide ?",
                            'options': ["Le sulfate de magnésium anhydre (MgSO₄)", "Le chlorure de sodium", "L'acide sulfurique", "Le carbonate de calcium"],
                            'reponse_correcte': '0',
                            'explication': "Le sulfate de magnésium anhydre (MgSO₄) ou le sulfate de sodium anhydre (Na₂SO₄) absorbent l'eau résiduelle d'une phase organique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Il est acceptable de pipeter à la bouche au laboratoire si le produit n'est pas toxique.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Il ne faut JAMAIS pipeter à la bouche, quel que soit le produit. On utilise toujours une propipette ou un pipeteur automatique.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La distillation permet de séparer des liquides en exploitant leurs différences de température d'ébullition.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "La distillation sépare les composants d'un mélange liquide grâce à leurs températures d'ébullition différentes : le composant le plus volatil s'évapore en premier.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Les déchets chimiques doivent être jetés dans l'évier pour être dilués par l'eau.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Les déchets chimiques doivent être collectés dans des bidons de récupération appropriés, jamais jetés dans l'évier, pour protéger l'environnement.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Donnez la formule du rendement d'une synthèse en fonction des masses (expérimentale et théorique).",
                            'options': None,
                            'reponse_correcte': 'r = m_exp / m_theo x 100',
                            'tolerances': ['m_exp/m_theo', 'r = (m_exp / m_théo) × 100', 'r = m_exp/m_théorique × 100%', 'masse expérimentale / masse théorique x 100'],
                            'explication': "Le rendement est r = (m_expérimentale / m_théorique) × 100 %. Il mesure l'efficacité de la synthèse.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on le document officiel qui accompagne chaque produit chimique et détaille ses dangers et précautions ?",
                            'options': None,
                            'reponse_correcte': 'fiche de données de sécurité',
                            'tolerances': ['FDS', 'fds', 'fiche de données de securité', 'fiche de securite', 'fiche de sécurité'],
                            'explication': "La Fiche de Données de Sécurité (FDS) accompagne chaque produit chimique et fournit les informations sur ses dangers, les mesures de premiers secours et les EPI à utiliser.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quelle est la température de fusion attendue pour l'aspirine pure (en °C) ?",
                            'options': None,
                            'reponse_correcte': '135',
                            'tolerances': ['135°C', '135 °C', '135 degrés'],
                            'explication': "La température de fusion de l'aspirine pure est de 135 °C. Une valeur inférieure indiquerait la présence d'impuretés.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 10 — Transformations physiques
    # ──────────────────────────────────────────────
    {
        'ordre': 10,
        'titre': 'Transformations physiques',
        'description': "Comprendre les changements d'état de la matière et les phénomènes de dissolution, en lien avec la conservation de la matière.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Changements d'état et conservation de la matière",
                'duree': 30,
                'contenu': """# Changements d'état et conservation de la matière

## Introduction

La matière peut exister sous trois **états physiques** : solide, liquide et gazeux. Le passage d'un état à un autre s'appelle un **changement d'état**. Ces transformations sont omniprésentes dans la vie quotidienne : la glace qui fond, l'eau qui bout, la buée sur une vitre froide… Comprendre ces phénomènes est essentiel en chimie comme en physique.

---

## Les trois états de la matière

### État solide

À l'état solide, les entités chimiques (atomes, molécules ou ions) sont **très proches** les unes des autres et occupent des positions **fixes**. Elles vibrent autour de leur position d'équilibre, mais ne se déplacent pas librement.

- Forme **propre** (ne dépend pas du récipient)
- Volume **propre** (quasi incompressible)

> **Exemples :** glace, fer, sel de cuisine ($NaCl$)

### État liquide

À l'état liquide, les entités sont **proches** mais peuvent **glisser** les unes sur les autres. L'ordre est partiel : on parle d'un **désordre local**.

- Pas de forme propre (prend la forme du récipient)
- Volume **propre** (quasi incompressible)

> **Exemples :** eau liquide, éthanol, mercure

### État gazeux

À l'état gazeux, les entités sont **très éloignées** les unes des autres et se déplacent de façon **désordonnée** à grande vitesse.

- Pas de forme propre
- Pas de volume propre (un gaz occupe tout le volume disponible)
- Compressible et expansible

> **Exemples :** vapeur d'eau, dioxygène $O_2$, dioxyde de carbone $CO_2$

---

## Les changements d'état

### Nomenclature

Les changements d'état portent des noms spécifiques selon les états de départ et d'arrivée :

| Transformation | État initial → État final | Exemple |
|---------------|--------------------------|---------|
| **Fusion** | Solide → Liquide | Glace qui fond |
| **Solidification** | Liquide → Solide | Eau qui gèle |
| **Vaporisation** | Liquide → Gaz | Eau qui bout |
| **Liquéfaction (condensation liquide)** | Gaz → Liquide | Buée sur une vitre |
| **Sublimation** | Solide → Gaz | Neige carbonique ($CO_2$ solide) |
| **Condensation solide** | Gaz → Solide | Givre sur une branche |

### Caractéristiques essentielles

1. **Un changement d'état est une transformation physique** : la nature chimique de la substance ne change pas. L'eau reste $H_2O$, qu'elle soit solide, liquide ou gazeuse.

2. **Conservation de la masse** : lors d'un changement d'état, la masse de l'échantillon se conserve.

$$m_{\\text{initial}} = m_{\\text{final}}$$

3. **Variation du volume** : le volume peut changer (l'eau liquide occupe moins de volume que la glace, ce qui est une exception remarquable pour la plupart des substances).

---

## Paliers de température

### Température de changement d'état

Pour un **corps pur**, le changement d'état s'effectue à **température constante** tant que les deux états coexistent. Cette température caractéristique s'appelle :

- **Température de fusion** $\\theta_f$ (ou point de fusion) pour la fusion/solidification
- **Température d'ébullition** $\\theta_{eb}$ (ou point d'ébullition) pour la vaporisation/liquéfaction

> **Exemple :** pour l'eau pure à pression atmosphérique normale ($P = 1{,}013 \\times 10^5 \\, Pa$) :
>
> $\\theta_f = 0 \\, °C$ et $\\theta_{eb} = 100 \\, °C$

### Courbe de température lors d'un changement d'état

Lorsqu'on chauffe un corps pur solide, on observe sur le graphique température en fonction du temps :

1. La température **augmente** (le solide se réchauffe)
2. La température **reste constante** au palier de fusion (les deux phases coexistent)
3. La température **augmente** à nouveau (le liquide se réchauffe)
4. La température **reste constante** au palier d'ébullition (les deux phases coexistent)
5. La température **augmente** (le gaz se réchauffe)

> **Point clé :** la présence d'un **palier de température** lors du changement d'état est caractéristique d'un **corps pur**. Un mélange change d'état sur un intervalle de températures.

---

## Cas des mélanges

Pour un **mélange**, le changement d'état ne se fait **pas à température constante**. On observe un changement progressif sur un **intervalle de températures**, sans véritable palier.

> **Exemple :** l'eau salée gèle en dessous de $0 \\, °C$, et la température de solidification dépend de la concentration en sel. C'est le principe du **salage des routes** en hiver.

---

## Diagramme d'états

Un **diagramme d'états** (ou diagramme de phases) représente les domaines d'existence des différents états d'un corps pur en fonction de la **température** et de la **pression**.

- Les **courbes** séparent les domaines solide, liquide et gazeux.
- Le **point triple** est le seul point où les trois états coexistent simultanément.
- Le **point critique** marque la limite au-delà de laquelle il n'y a plus de distinction entre liquide et gaz (état **supercritique**).

> **Pour l'eau :** le point triple se trouve à $T = 0{,}01 \\, °C$ et $P = 611 \\, Pa$, et le point critique à $T = 374 \\, °C$ et $P = 221 \\times 10^5 \\, Pa$.

---

## Énergie et changements d'état

Un changement d'état nécessite ou libère de l'**énergie thermique** (chaleur) :

- **Fusion, vaporisation, sublimation** : le corps **absorbe** de l'énergie → transformation **endothermique**
- **Solidification, liquéfaction, condensation solide** : le corps **libère** de l'énergie → transformation **exothermique**

L'énergie nécessaire pour faire fondre une masse $m$ de corps pur est :

$$Q = m \\times L_f$$

où $L_f$ est la **chaleur latente de fusion** (en $J \\cdot kg^{-1}$).

> **Exemple :** pour la glace, $L_f \\approx 334 \\, kJ \\cdot kg^{-1}$. Pour faire fondre $500 \\, g$ de glace :
>
> $Q = 0{,}500 \\times 334 \\times 10^3 = 167 \\times 10^3 \\, J = 167 \\, kJ$

---

## L'essentiel à retenir

- La matière existe sous trois états : **solide, liquide, gazeux**.
- Les changements d'état sont des **transformations physiques** (pas de changement de nature chimique).
- La **masse se conserve** lors d'un changement d'état.
- Pour un corps pur, le changement d'état se fait à **température constante** (palier).
- L'énergie est absorbée (endothermique) ou libérée (exothermique) selon le sens du changement.
""",
                'quiz': {
                    'titre': "Quiz — Changements d'état et conservation de la matière",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quel est le nom du passage de l'état solide à l'état liquide ?",
                            'options': ["La fusion", "La solidification", "La vaporisation", "La sublimation"],
                            'reponse_correcte': '0',
                            'explication': "La fusion est le passage de l'état solide à l'état liquide.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Comment appelle-t-on le passage de l'état gazeux à l'état liquide ?",
                            'options': ["La liquéfaction", "La vaporisation", "La solidification", "La sublimation"],
                            'reponse_correcte': '0',
                            'explication': "La liquéfaction (ou condensation liquide) est le passage de l'état gazeux à l'état liquide. Exemple : la buée sur une vitre froide.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Quelle propriété caractérise l'état solide ?",
                            'options': ["Forme propre et volume propre", "Pas de forme propre mais volume propre", "Ni forme propre ni volume propre", "Forme propre mais pas de volume propre"],
                            'reponse_correcte': '0',
                            'explication': "À l'état solide, la matière possède une forme propre (ne dépend pas du récipient) et un volume propre (quasi incompressible).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Lors d'un changement d'état, que se passe-t-il pour la masse de l'échantillon ?",
                            'options': ["Elle se conserve", "Elle augmente", "Elle diminue", "Elle dépend du type de changement d'état"],
                            'reponse_correcte': '0',
                            'explication': "Lors d'un changement d'état, la masse se conserve : m_initial = m_final.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La neige carbonique (CO₂ solide) qui passe directement à l'état gazeux est un exemple de :",
                            'options': ["Sublimation", "Vaporisation", "Fusion", "Liquéfaction"],
                            'reponse_correcte': '0',
                            'explication': "La sublimation est le passage direct de l'état solide à l'état gazeux, sans passer par l'état liquide.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quelle est la température d'ébullition de l'eau pure à pression atmosphérique normale ?",
                            'options': ["100 °C", "0 °C", "50 °C", "212 °C"],
                            'reponse_correcte': '0',
                            'explication': "La température d'ébullition de l'eau pure à pression atmosphérique normale (1,013 × 10⁵ Pa) est de 100 °C.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "À l'état gazeux, les molécules sont :",
                            'options': ["Très éloignées et en mouvement désordonné", "Très proches et en positions fixes", "Proches mais glissant les unes sur les autres", "Immobiles et très éloignées"],
                            'reponse_correcte': '0',
                            'explication': "À l'état gazeux, les entités sont très éloignées les unes des autres et se déplacent de façon désordonnée à grande vitesse.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Un changement d'état est une transformation :",
                            'options': ["Physique", "Chimique", "Nucléaire", "Biologique"],
                            'reponse_correcte': '0',
                            'explication': "Un changement d'état est une transformation physique : la nature chimique de la substance ne change pas. L'eau reste H₂O quel que soit son état.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Qu'observe-t-on sur la courbe de température lors du changement d'état d'un corps pur ?",
                            'options': ["Un palier de température", "Une augmentation continue de la température", "Une diminution continue de la température", "Des oscillations de température"],
                            'reponse_correcte': '0',
                            'explication': "Pour un corps pur, le changement d'état s'effectue à température constante : on observe un palier tant que les deux phases coexistent.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Pour un mélange, le changement d'état :",
                            'options': ["Se fait sur un intervalle de températures sans palier net", "Se fait à température constante comme un corps pur", "Ne peut pas se produire", "Se fait toujours à 0 °C"],
                            'reponse_correcte': '0',
                            'explication': "Pour un mélange, le changement d'état ne se fait pas à température constante : on observe un changement progressif sur un intervalle de températures.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "La chaleur latente de fusion de la glace vaut environ :",
                            'options': ["334 kJ·kg⁻¹", "34 kJ·kg⁻¹", "134 kJ·kg⁻¹", "534 kJ·kg⁻¹"],
                            'reponse_correcte': '0',
                            'explication': "La chaleur latente de fusion de la glace est d'environ 334 kJ·kg⁻¹.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Au point triple de l'eau, les trois états coexistent à :",
                            'options': ["T = 0,01 °C et P = 611 Pa", "T = 0 °C et P = 1 atm", "T = 100 °C et P = 1 atm", "T = 374 °C et P = 221 × 10⁵ Pa"],
                            'reponse_correcte': '0',
                            'explication': "Le point triple de l'eau se trouve à T = 0,01 °C et P = 611 Pa, où les trois états coexistent simultanément.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "La vaporisation et la fusion sont des transformations :",
                            'options': ["Endothermiques (le corps absorbe de l'énergie)", "Exothermiques (le corps libère de l'énergie)", "Athermiques (sans échange d'énergie)", "Parfois endothermiques, parfois exothermiques"],
                            'reponse_correcte': '0',
                            'explication': "La fusion, la vaporisation et la sublimation sont endothermiques : le corps absorbe de l'énergie pour passer à un état plus désordonné.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Quelle énergie faut-il pour faire fondre 500 g de glace (Lf ≈ 334 kJ·kg⁻¹) ?",
                            'options': ["167 kJ", "334 kJ", "668 kJ", "67 kJ"],
                            'reponse_correcte': '0',
                            'explication': "Q = m × Lf = 0,500 × 334 = 167 kJ.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "La sublimation est le passage direct de l'état solide à l'état gazeux.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "La sublimation est bien le passage direct de l'état solide à l'état gazeux (exemple : la neige carbonique CO₂).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La solidification est une transformation endothermique.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La solidification est exothermique : le corps libère de l'énergie en passant de l'état liquide à l'état solide.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "La présence d'un palier de température lors d'un changement d'état est caractéristique d'un corps pur.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Un corps pur change d'état à température constante (palier). Un mélange change d'état sur un intervalle de températures.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on le point du diagramme de phases où les trois états (solide, liquide, gazeux) coexistent simultanément ?",
                            'options': None,
                            'reponse_correcte': 'point triple',
                            'tolerances': ['le point triple', 'Point triple', 'pt triple'],
                            'explication': "Le point triple est le seul point du diagramme de phases où les trois états de la matière coexistent simultanément.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Quelle est la formule donnant l'énergie Q nécessaire pour faire fondre une masse m d'un corps pur, en fonction de la chaleur latente de fusion Lf ?",
                            'options': None,
                            'reponse_correcte': 'Q = m × Lf',
                            'tolerances': ['Q = m * Lf', 'Q=mLf', 'Q = mLf'],
                            'explication': "L'énergie nécessaire pour faire fondre une masse m de corps pur est Q = m × Lf, où Lf est la chaleur latente de fusion en J·kg⁻¹.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on le passage direct de l'état gazeux à l'état solide, sans passer par l'état liquide ?",
                            'options': None,
                            'reponse_correcte': 'condensation solide',
                            'tolerances': ['la condensation solide', 'Condensation solide', 'déposition'],
                            'explication': "La condensation solide (ou déposition) est le passage direct de l'état gazeux à l'état solide. Exemple : la formation de givre.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Dissolution et solubilité',
                'duree': 30,
                'contenu': """# Dissolution et solubilité

## Introduction

Lorsque l'on met un morceau de sucre dans un verre d'eau et que l'on agite, le sucre « disparaît » : il s'est **dissous**. La dissolution est une transformation physique fondamentale en chimie. Elle permet de préparer des **solutions**, omniprésentes dans la vie courante (eau salée, sirop, sérum physiologique…) comme au laboratoire.

---

## Vocabulaire de la dissolution

### Soluté, solvant, solution

- **Soluté** : l'espèce chimique qui est dissoute (le sucre, le sel, etc.)
- **Solvant** : le liquide dans lequel le soluté se dissout (l'eau, l'éthanol, etc.)
- **Solution** : le mélange homogène obtenu après dissolution

$$\\text{Soluté} + \\text{Solvant} \\longrightarrow \\text{Solution}$$

> Lorsque le solvant est l'eau, on parle de **solution aqueuse**.

### Solution saturée et non saturée

- Une **solution non saturée** peut encore dissoudre du soluté supplémentaire.
- Une **solution saturée** ne peut plus dissoudre de soluté : l'ajout de soluté entraîne la formation d'un **dépôt** (corps non dissous) au fond du récipient.

---

## Le processus de dissolution

### Dissolution d'un soluté moléculaire

Lorsqu'on dissout un soluté **moléculaire** (comme le sucre $C_{12}H_{22}O_{11}$), les molécules de soluté se **dispersent** parmi les molécules de solvant. Les molécules de soluté sont entourées de molécules de solvant : on parle de **solvatation** (ou **hydratation** si le solvant est l'eau).

### Dissolution d'un soluté ionique

Lorsqu'on dissout un soluté **ionique** (comme le chlorure de sodium $NaCl$), le cristal se dissocie en **ions** qui se dispersent dans le solvant :

$$NaCl_{(s)} \\xrightarrow{\\text{eau}} Na^+_{(aq)} + Cl^-_{(aq)}$$

L'indice $(aq)$ signifie que les ions sont **hydratés**, c'est-à-dire entourés de molécules d'eau.

> **Autre exemple :** dissolution du sulfate de cuivre :
>
> $$CuSO_{4(s)} \\xrightarrow{\\text{eau}} Cu^{2+}_{(aq)} + SO_4^{2-}_{(aq)}$$

### Conservation de la matière

Lors de la dissolution, la **masse totale se conserve** :

$$m_{\\text{solution}} = m_{\\text{soluté}} + m_{\\text{solvant}}$$

Les atomes ne sont ni créés ni détruits : ils changent simplement de répartition spatiale.

---

## Concentration en masse

### Définition

La **concentration en masse** $C_m$ d'un soluté dans une solution est la masse de soluté dissoute par litre de solution :

$$C_m = \\frac{m_{\\text{soluté}}}{V_{\\text{solution}}}$$

- $C_m$ en $g \\cdot L^{-1}$
- $m_{\\text{soluté}}$ en $g$
- $V_{\\text{solution}}$ en $L$

### Exemple

On dissout $9{,}0 \\, g$ de chlorure de sodium dans de l'eau pour obtenir $1{,}0 \\, L$ de solution (sérum physiologique) :

$$C_m = \\frac{9{,}0}{1{,}0} = 9{,}0 \\, g \\cdot L^{-1}$$

---

## Solubilité

### Définition

La **solubilité** $s$ d'un soluté dans un solvant donné est la **concentration en masse maximale** que l'on peut atteindre dans une solution saturée, à une température donnée.

$$s = C_{m, \\text{max}} \\quad (\\text{en } g \\cdot L^{-1})$$

### Exemples de solubilités dans l'eau à $20 \\, °C$

| Soluté | Solubilité ($g \\cdot L^{-1}$) |
|--------|-------------------------------|
| Chlorure de sodium $NaCl$ | $\\approx 360$ |
| Sucre (saccharose) $C_{12}H_{22}O_{11}$ | $\\approx 2000$ |
| Sulfate de cuivre $CuSO_4$ | $\\approx 320$ |
| Dioxyde de carbone $CO_2$ | $\\approx 1{,}7$ |

---

## Facteurs influençant la solubilité

### Température

Pour la plupart des solides, la solubilité **augmente** avec la température :

> En chauffant de l'eau, on peut dissoudre davantage de sucre.

Pour les **gaz**, c'est l'inverse : la solubilité **diminue** quand la température augmente.

> **Exemple concret :** une bouteille d'eau gazeuse pétille davantage quand on la sort du réfrigérateur (le $CO_2$ dissous s'échappe car sa solubilité diminue en se réchauffant).

### Nature du soluté et du solvant

La solubilité dépend de la **compatibilité chimique** entre le soluté et le solvant :

- Les solutés **polaires** ou **ioniques** se dissolvent bien dans les solvants **polaires** comme l'eau → « *qui se ressemble s'assemble* »
- Les solutés **apolaires** (huile, graisses) sont très peu solubles dans l'eau mais solubles dans des solvants organiques comme l'hexane ou l'éthanol

> **Application :** c'est pourquoi on utilise du **savon** pour laver les graisses. Le savon possède une partie polaire (hydrophile) et une partie apolaire (lipophile) qui « capture » les graisses.

### Pression (pour les gaz)

La solubilité d'un gaz dans un liquide **augmente** avec la pression :

> Les boissons gazeuses sont embouteillées sous pression pour dissoudre davantage de $CO_2$. À l'ouverture, la pression diminue et le gaz s'échappe sous forme de bulles.

---

## Préparation d'une solution par dissolution

### Protocole au laboratoire

Pour préparer un volume $V$ de solution à la concentration $C_m$ :

1. **Calculer** la masse de soluté nécessaire : $m = C_m \\times V$
2. **Peser** le soluté sur une balance de précision
3. **Introduire** le soluté dans une **fiole jaugée** de volume $V$
4. **Ajouter** de l'eau distillée (environ les 2/3 du volume)
5. **Agiter** jusqu'à dissolution complète
6. **Compléter** avec de l'eau distillée jusqu'au trait de jauge (ménisque tangent au trait)
7. **Boucher** et **homogénéiser** en retournant la fiole

### Exemple de calcul

On veut préparer $V = 250 \\, mL = 0{,}250 \\, L$ de solution de chlorure de sodium à $C_m = 20 \\, g \\cdot L^{-1}$.

$$m = C_m \\times V = 20 \\times 0{,}250 = 5{,}0 \\, g$$

Il faut peser $5{,}0 \\, g$ de $NaCl$.

---

## L'essentiel à retenir

- La **dissolution** est la dispersion d'un **soluté** dans un **solvant** pour former une **solution** homogène.
- Un soluté ionique se dissocie en **ions hydratés** ; un soluté moléculaire se disperse sous forme de molécules.
- La **masse se conserve** lors de la dissolution.
- La **concentration en masse** : $C_m = \\dfrac{m_{\\text{soluté}}}{V_{\\text{solution}}}$ (en $g \\cdot L^{-1}$).
- La **solubilité** $s$ est la concentration maximale en solution saturée.
- La solubilité dépend de la **température**, de la **nature** du soluté et du solvant, et de la **pression** (pour les gaz).
""",
                'quiz': {
                    'titre': 'Quiz — Dissolution et solubilité',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Dans une dissolution, comment appelle-t-on le liquide dans lequel le soluté se dissout ?",
                            'options': ["Le solvant", "La solution", "Le soluté", "Le précipité"],
                            'reponse_correcte': '0',
                            'explication': "Le solvant est le liquide dans lequel le soluté se dissout. Quand le solvant est l'eau, on parle de solution aqueuse.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Lors d'une dissolution, on obtient un mélange :",
                            'options': ["Homogène", "Hétérogène", "Biphasique", "Gazeux"],
                            'reponse_correcte': '0',
                            'explication': "La dissolution produit une solution, qui est un mélange homogène : on ne distingue qu'une seule phase.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "L'indice (aq) dans Na⁺(aq) signifie que l'ion est :",
                            'options': ["Hydraté (entouré de molécules d'eau)", "À l'état gazeux", "À l'état solide", "Non dissocié"],
                            'reponse_correcte': '0',
                            'explication': "L'indice (aq) signifie « aqueux » : l'ion est hydraté, c'est-à-dire entouré de molécules d'eau.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "La concentration en masse Cm s'exprime en :",
                            'options': ["g·L⁻¹", "mol·L⁻¹", "kg·m⁻³", "g·mol⁻¹"],
                            'reponse_correcte': '0',
                            'explication': "La concentration en masse Cm = m(soluté) / V(solution) s'exprime en g·L⁻¹.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Lors de la dissolution, la masse totale :",
                            'options': ["Se conserve", "Augmente", "Diminue", "Dépend du soluté"],
                            'reponse_correcte': '0',
                            'explication': "Lors de la dissolution, la masse se conserve : m(solution) = m(soluté) + m(solvant).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Le chlorure de sodium NaCl est un soluté :",
                            'options': ["Ionique", "Moléculaire", "Métallique", "Covalent pur"],
                            'reponse_correcte': '0',
                            'explication': "NaCl est un composé ionique. Lors de sa dissolution, il se dissocie en ions Na⁺(aq) et Cl⁻(aq).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Que se passe-t-il quand on ajoute du soluté à une solution déjà saturée ?",
                            'options': ["Un dépôt se forme au fond du récipient", "Le soluté se dissout normalement", "La solution change de couleur", "Le solvant s'évapore"],
                            'reponse_correcte': '0',
                            'explication': "Une solution saturée ne peut plus dissoudre de soluté supplémentaire : l'excès forme un dépôt (corps non dissous) au fond.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Le saccharose (sucre de table) est un soluté :",
                            'options': ["Moléculaire", "Ionique", "Métallique", "Gazeux"],
                            'reponse_correcte': '0',
                            'explication': "Le saccharose C₁₂H₂₂O₁₁ est un composé moléculaire. Lors de sa dissolution, les molécules se dispersent parmi les molécules d'eau.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "La solubilité du NaCl dans l'eau à 20 °C est d'environ :",
                            'options': ["360 g·L⁻¹", "36 g·L⁻¹", "3,6 g·L⁻¹", "3 600 g·L⁻¹"],
                            'reponse_correcte': '0',
                            'explication': "La solubilité du chlorure de sodium dans l'eau à 20 °C est d'environ 360 g·L⁻¹.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Pour la plupart des gaz dissous, lorsque la température augmente, la solubilité :",
                            'options': ["Diminue", "Augmente", "Reste constante", "Devient nulle"],
                            'reponse_correcte': '0',
                            'explication': "Pour les gaz, la solubilité diminue quand la température augmente. C'est pourquoi une boisson gazeuse pétille plus en se réchauffant.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Pour préparer 250 mL de solution de NaCl à 20 g·L⁻¹, quelle masse de sel faut-il peser ?",
                            'options': ["5,0 g", "20 g", "50 g", "2,5 g"],
                            'reponse_correcte': '0',
                            'explication': "m = Cm × V = 20 × 0,250 = 5,0 g.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Les solutés polaires ou ioniques se dissolvent bien dans :",
                            'options': ["Les solvants polaires comme l'eau", "Les solvants apolaires comme l'hexane", "N'importe quel solvant", "Les gaz uniquement"],
                            'reponse_correcte': '0',
                            'explication': "« Qui se ressemble s'assemble » : les solutés polaires/ioniques se dissolvent dans les solvants polaires, et les apolaires dans les solvants apolaires.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "La solubilité d'un gaz dans un liquide augmente lorsque :",
                            'options': ["La pression augmente", "La pression diminue", "La température augmente", "On agite la solution"],
                            'reponse_correcte': '0',
                            'explication': "La solubilité d'un gaz augmente avec la pression. C'est pourquoi les boissons gazeuses sont embouteillées sous pression.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Lors de la dissolution de CuSO₄ dans l'eau, on obtient :",
                            'options': ["Cu²⁺(aq) et SO₄²⁻(aq)", "Cu(aq) et SO₄(aq)", "CuSO₄(aq) non dissocié", "Cu²⁻(aq) et SO₄²⁺(aq)"],
                            'reponse_correcte': '0',
                            'explication': "Le sulfate de cuivre est un composé ionique. Il se dissocie en ions Cu²⁺(aq) et SO₄²⁻(aq) lors de sa dissolution dans l'eau.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "La dissolution est une transformation chimique.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La dissolution est une transformation physique : les espèces chimiques se dispersent dans le solvant mais ne changent pas de nature.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La solubilité de la plupart des solides dans l'eau augmente avec la température.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Pour la plupart des solides, la solubilité augmente avec la température. On peut dissoudre davantage de sucre dans de l'eau chaude.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Une solution saturée peut encore dissoudre du soluté supplémentaire.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Par définition, une solution saturée a atteint sa concentration maximale et ne peut plus dissoudre de soluté supplémentaire.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quelle est la formule de la concentration en masse Cm d'un soluté dans une solution ?",
                            'options': None,
                            'reponse_correcte': 'Cm = m / V',
                            'tolerances': ['Cm = m/V', 'C = m/V', 'Cm=m/V'],
                            'explication': "La concentration en masse est Cm = m(soluté) / V(solution), en g·L⁻¹.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on la concentration en masse maximale que l'on peut atteindre dans une solution, à une température donnée ?",
                            'options': None,
                            'reponse_correcte': 'solubilité',
                            'tolerances': ['la solubilité', 'Solubilité', 'solubilite'],
                            'explication': "La solubilité s est la concentration en masse maximale dans une solution saturée, à une température donnée.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quel type de verrerie de précision utilise-t-on au laboratoire pour préparer un volume exact de solution par dissolution ?",
                            'options': None,
                            'reponse_correcte': 'fiole jaugée',
                            'tolerances': ['une fiole jaugée', 'Fiole jaugée', 'la fiole jaugée'],
                            'explication': "La fiole jaugée est la verrerie de précision utilisée pour préparer un volume exact de solution. On complète jusqu'au trait de jauge.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 11 — Transformations nucléaires
    # ──────────────────────────────────────────────
    {
        'ordre': 11,
        'titre': 'Transformations nucléaires',
        'description': "Découvrir la structure du noyau atomique, les différents types de radioactivité, et les réactions de fission et de fusion nucléaires.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Noyau atomique et radioactivité',
                'duree': 30,
                'contenu': """# Noyau atomique et radioactivité

## Introduction

Au cœur de chaque atome se trouve le **noyau**, une structure extrêmement petite et dense qui contient l'essentiel de la masse de l'atome. Certains noyaux sont **instables** : ils se transforment spontanément en émettant des rayonnements. C'est le phénomène de **radioactivité**, découvert par Henri Becquerel en 1896. Comprendre la radioactivité est indispensable pour saisir les enjeux de l'énergie nucléaire, de l'imagerie médicale et de la datation en géologie.

---

## Le noyau atomique

### Composition

Le noyau est constitué de **nucléons** :

- **Protons** (charge positive $+e$) : leur nombre $Z$ est le **numéro atomique** (il définit l'élément chimique)
- **Neutrons** (charge nulle) : leur nombre est noté $N$

Le nombre total de nucléons est le **nombre de masse** :

$$A = Z + N$$

### Notation symbolique

Un noyau est noté :

$$^A_Z X$$

où $X$ est le symbole de l'élément chimique.

> **Exemples :**
>
> - Hydrogène : $^1_1 H$ (1 proton, 0 neutron)
> - Carbone 12 : $^{12}_{\\;6} C$ (6 protons, 6 neutrons)
> - Uranium 238 : $^{238}_{\\;92} U$ (92 protons, 146 neutrons)

---

## Isotopes

### Définition

Deux noyaux sont **isotopes** s'ils ont le **même numéro atomique** $Z$ (même élément chimique) mais un **nombre de masse** $A$ différent (nombre de neutrons différent).

> **Exemples d'isotopes du carbone :**
>
> | Isotope | Protons ($Z$) | Neutrons ($N$) | Masse ($A$) | Stabilité |
> |---------|:---:|:---:|:---:|-----------|
> | $^{12}_{\\;6} C$ | 6 | 6 | 12 | Stable |
> | $^{13}_{\\;6} C$ | 6 | 7 | 13 | Stable |
> | $^{14}_{\\;6} C$ | 6 | 8 | 14 | Radioactif |

Les isotopes d'un même élément ont les **mêmes propriétés chimiques** (même nombre d'électrons) mais des **propriétés nucléaires différentes**.

---

## Stabilité et instabilité nucléaire

### Vallée de stabilité

Les noyaux stables se trouvent dans une zone appelée **vallée de stabilité** sur un diagramme $N$ en fonction de $Z$ :

- Pour les noyaux légers ($Z \\leq 20$) : $N \\approx Z$ (autant de neutrons que de protons)
- Pour les noyaux lourds : $N > Z$ (il faut davantage de neutrons pour compenser la répulsion entre protons)

### Noyaux instables

Un noyau qui se trouve **en dehors** de la vallée de stabilité est **radioactif** : il se désintègre spontanément pour se rapprocher de la stabilité en émettant un rayonnement.

---

## Les trois types de radioactivité

### Radioactivité alpha ($\\alpha$)

Un noyau lourd émet un **noyau d'hélium** $^4_2 He$ (particule $\\alpha$) :

$$^A_Z X \\longrightarrow ^{A-4}_{Z-2} Y + ^4_2 He$$

> **Exemple :** désintégration de l'uranium 238 :
>
> $$^{238}_{\\;92} U \\longrightarrow ^{234}_{\\;90} Th + ^4_2 He$$

**Caractéristiques :** rayonnement peu pénétrant (arrêté par une feuille de papier), mais très ionisant.

### Radioactivité bêta moins ($\\beta^-$)

Un **neutron** du noyau se transforme en **proton** avec émission d'un **électron** $^{\\;\\;0}_{-1} e$ :

$$^A_Z X \\longrightarrow ^{\\;\\;A}_{Z+1} Y + ^{\\;\\;0}_{-1} e$$

> **Exemple :** désintégration du carbone 14 :
>
> $$^{14}_{\\;6} C \\longrightarrow ^{14}_{\\;7} N + ^{\\;\\;0}_{-1} e$$

**Caractéristiques :** concerne les noyaux avec un **excès de neutrons**.

### Radioactivité bêta plus ($\\beta^+$)

Un **proton** du noyau se transforme en **neutron** avec émission d'un **positon** $^{0}_{1} e$ :

$$^A_Z X \\longrightarrow ^{\\;\\;A}_{Z-1} Y + ^{0}_{1} e$$

> **Exemple :** désintégration du fluor 18 :
>
> $$^{18}_{\\;9} F \\longrightarrow ^{18}_{\\;8} O + ^{0}_{1} e$$

**Caractéristiques :** concerne les noyaux avec un **excès de protons**.

---

## Lois de conservation (lois de Soddy)

Lors d'une réaction nucléaire, deux grandeurs se conservent :

1. **Conservation du nombre de masse** $A$ :

$$\\sum A_{\\text{réactifs}} = \\sum A_{\\text{produits}}$$

2. **Conservation du numéro atomique** $Z$ (conservation de la charge) :

$$\\sum Z_{\\text{réactifs}} = \\sum Z_{\\text{produits}}$$

> **Application :** ces lois permettent d'identifier un noyau fils inconnu dans une équation de désintégration.
>
> Si $^{210}_{\\;84} Po \\longrightarrow ^{A}_{Z} X + ^4_2 He$, alors :
>
> $A = 210 - 4 = 206$ et $Z = 84 - 2 = 82$, donc $X = ^{206}_{\\;82} Pb$ (plomb 206).

---

## Demi-vie radioactive

### Définition

La **demi-vie** $t_{1/2}$ d'un isotope radioactif est la durée au bout de laquelle la **moitié** des noyaux radioactifs initialement présents se sont désintégrés.

### Loi de décroissance

Le nombre de noyaux radioactifs restants à l'instant $t$ est :

$$N(t) = N_0 \\times \\left(\\frac{1}{2}\\right)^{t / t_{1/2}}$$

où $N_0$ est le nombre initial de noyaux.

### Exemples de demi-vies

| Isotope | $t_{1/2}$ | Application |
|---------|-----------|-------------|
| $^{14}_{\\;6} C$ | $5730$ ans | Datation archéologique |
| $^{131}_{\\;53} I$ (iode 131) | $8{,}02$ jours | Traitement de la thyroïde |
| $^{238}_{\\;92} U$ | $4{,}5 \\times 10^9$ ans | Datation géologique |
| $^{222}_{\\;86} Rn$ (radon 222) | $3{,}8$ jours | Risque sanitaire (gaz naturel) |

> **Remarque :** après $n$ demi-vies, il reste $\\dfrac{N_0}{2^n}$ noyaux radioactifs. Après environ **10 demi-vies**, l'activité est divisée par $2^{10} = 1024 \\approx 1000$, et on considère que l'échantillon est pratiquement inactif.

---

## L'essentiel à retenir

- Le noyau $^A_Z X$ contient $Z$ protons et $N = A - Z$ neutrons.
- Des **isotopes** ont le même $Z$ mais un $A$ différent.
- Un noyau **instable** se désintègre par radioactivité : $\\alpha$, $\\beta^-$ ou $\\beta^+$.
- Les **lois de Soddy** imposent la conservation de $A$ et de $Z$.
- La **demi-vie** $t_{1/2}$ est le temps pour que la moitié des noyaux se désintègrent.
""",
                'quiz': {
                    'titre': 'Quiz — Noyau atomique et radioactivité',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Le noyau atomique est constitué de :",
                            'options': ["Protons et neutrons", "Protons et électrons", "Neutrons et électrons", "Protons, neutrons et électrons"],
                            'reponse_correcte': '0',
                            'explication': "Le noyau contient des protons (charge +) et des neutrons (charge nulle), appelés collectivement nucléons.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Le numéro atomique Z représente le nombre de :",
                            'options': ["Protons", "Neutrons", "Nucléons", "Électrons du noyau"],
                            'reponse_correcte': '0',
                            'explication': "Z est le numéro atomique, c'est-à-dire le nombre de protons dans le noyau. Il définit l'élément chimique.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Le nombre de masse A est égal à :",
                            'options': ["Z + N (protons + neutrons)", "Z − N", "Z × N", "N − Z"],
                            'reponse_correcte': '0',
                            'explication': "Le nombre de masse A est le nombre total de nucléons : A = Z + N.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Deux isotopes d'un même élément ont :",
                            'options': ["Le même Z mais un A différent", "Le même A mais un Z différent", "Le même Z et le même A", "Un Z et un A tous deux différents"],
                            'reponse_correcte': '0',
                            'explication': "Des isotopes ont le même numéro atomique Z (même élément) mais un nombre de masse A différent (nombre de neutrons différent).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Lors d'une désintégration alpha (α), le noyau émet :",
                            'options': ["Un noyau d'hélium ⁴₂He", "Un électron", "Un positon", "Un neutron"],
                            'reponse_correcte': '0',
                            'explication': "La radioactivité α consiste en l'émission d'un noyau d'hélium ⁴₂He (2 protons + 2 neutrons).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Le carbone 14 (¹⁴₆C) possède :",
                            'options': ["6 protons et 8 neutrons", "6 protons et 6 neutrons", "8 protons et 6 neutrons", "14 protons et 6 neutrons"],
                            'reponse_correcte': '0',
                            'explication': "¹⁴₆C : Z = 6 protons et N = A − Z = 14 − 6 = 8 neutrons.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "La demi-vie d'un isotope radioactif est :",
                            'options': ["La durée pour que la moitié des noyaux se désintègrent", "La durée pour que tous les noyaux se désintègrent", "La moitié de la durée de vie d'un noyau", "Le temps entre deux désintégrations successives"],
                            'reponse_correcte': '0',
                            'explication': "La demi-vie t₁/₂ est la durée au bout de laquelle la moitié des noyaux radioactifs initialement présents se sont désintégrés.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "La radioactivité bêta moins (β⁻) concerne les noyaux ayant :",
                            'options': ["Un excès de neutrons", "Un excès de protons", "Trop de nucléons", "Pas assez de nucléons"],
                            'reponse_correcte': '0',
                            'explication': "La radioactivité β⁻ concerne les noyaux avec un excès de neutrons : un neutron se transforme en proton avec émission d'un électron.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Lors de la désintégration α de ²¹⁰₈₄Po, quel est le noyau fils produit ?",
                            'options': ["²⁰⁶₈₂Pb (plomb 206)", "²⁰⁶₈₄Po", "²⁰⁶₈₆Rn", "²¹⁰₈₂Pb"],
                            'reponse_correcte': '0',
                            'explication': "Désintégration α : A diminue de 4 et Z de 2. Donc A = 210 − 4 = 206 et Z = 84 − 2 = 82, soit le plomb ²⁰⁶₈₂Pb.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Les lois de Soddy imposent la conservation de :",
                            'options': ["A (nombre de masse) et Z (numéro atomique)", "A uniquement", "Z uniquement", "La masse totale uniquement"],
                            'reponse_correcte': '0',
                            'explication': "Les lois de Soddy stipulent que lors d'une réaction nucléaire, le nombre de masse A et le numéro atomique Z se conservent.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "La demi-vie du carbone 14 est d'environ :",
                            'options': ["5 730 ans", "573 ans", "57 300 ans", "5,73 ans"],
                            'reponse_correcte': '0',
                            'explication': "La demi-vie du carbone 14 est de 5 730 ans, ce qui permet la datation archéologique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Après 3 demi-vies, quelle fraction des noyaux radioactifs initiaux reste-t-il ?",
                            'options': ["1/8", "1/3", "1/4", "1/6"],
                            'reponse_correcte': '0',
                            'explication': "Après n demi-vies, il reste N₀/2ⁿ noyaux. Pour n = 3 : N₀/2³ = N₀/8, soit 1/8 des noyaux initiaux.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Le rayonnement alpha (α) est arrêté par :",
                            'options': ["Une feuille de papier", "Une plaque de plomb uniquement", "Rien, il traverse tout", "Une feuille d'aluminium de quelques mm"],
                            'reponse_correcte': '0',
                            'explication': "Le rayonnement α est peu pénétrant : il est arrêté par une simple feuille de papier, mais il est très ionisant.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Pour les noyaux légers stables (Z ≤ 20), le nombre de neutrons N est environ :",
                            'options': ["Égal au nombre de protons (N ≈ Z)", "Le double du nombre de protons", "La moitié du nombre de protons", "Nul"],
                            'reponse_correcte': '0',
                            'explication': "Pour les noyaux légers stables, N ≈ Z. Pour les noyaux lourds, il faut davantage de neutrons (N > Z) pour la stabilité.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Les isotopes d'un même élément ont les mêmes propriétés chimiques.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Les isotopes ont le même Z donc le même nombre d'électrons, ce qui leur confère les mêmes propriétés chimiques.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Le rayonnement alpha est très pénétrant et difficile à arrêter.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le rayonnement α est peu pénétrant (arrêté par une feuille de papier), mais il est très ionisant.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Lors d'une désintégration β⁻, un neutron se transforme en proton avec émission d'un électron.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "En radioactivité β⁻, un neutron du noyau se transforme en proton, et un électron est émis. Le numéro atomique Z augmente de 1.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quelle est la formule de la loi de décroissance radioactive donnant le nombre N(t) de noyaux restants en fonction de N₀ et de la demi-vie t₁/₂ ?",
                            'options': None,
                            'reponse_correcte': 'N(t) = N0 × (1/2)^(t/t1/2)',
                            'tolerances': ['N = N0 × (1/2)^(t/t1/2)', 'N(t) = N0 * (1/2)^(t/t1/2)', 'N = N0(1/2)^(t/t1/2)'],
                            'explication': "La loi de décroissance radioactive est N(t) = N₀ × (1/2)^(t/t₁/₂), où N₀ est le nombre initial de noyaux.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Quel isotope radioactif, de demi-vie 5 730 ans, est utilisé pour la datation archéologique ?",
                            'options': None,
                            'reponse_correcte': 'carbone 14',
                            'tolerances': ['le carbone 14', 'C-14', '14C', 'C14'],
                            'explication': "Le carbone 14 (¹⁴C), de demi-vie 5 730 ans, permet de dater des échantillons organiques jusqu'à environ 50 000 ans.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on des noyaux ayant le même numéro atomique Z mais un nombre de masse A différent ?",
                            'options': None,
                            'reponse_correcte': 'isotopes',
                            'tolerances': ['des isotopes', 'Isotopes', 'les isotopes'],
                            'explication': "Des isotopes sont des noyaux ayant le même Z (même élément chimique) mais un A différent (nombre de neutrons différent).",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Fission, fusion et énergie nucléaire',
                'duree': 30,
                'contenu': """# Fission, fusion et énergie nucléaire

## Introduction

Les réactions nucléaires libèrent des quantités d'énergie **considérables**, bien supérieures à celles des réactions chimiques. C'est cette énergie qui alimente les **centrales nucléaires** et fait briller les **étoiles**. Il existe deux grands types de réactions nucléaires productrices d'énergie : la **fission** et la **fusion**.

---

## Rappel : énergie et masse

### Équivalence masse-énergie

Albert Einstein a montré en 1905 que la masse et l'énergie sont liées par la célèbre relation :

$$E = m \\times c^2$$

- $E$ : énergie (en joules, $J$)
- $m$ : masse (en kilogrammes, $kg$)
- $c$ : vitesse de la lumière dans le vide ($c \\approx 3{,}00 \\times 10^8 \\, m \\cdot s^{-1}$)

### Défaut de masse

La masse d'un noyau est toujours **inférieure** à la somme des masses de ses nucléons pris séparément. Cette différence est le **défaut de masse** :

$$\\Delta m = Z \\times m_p + N \\times m_n - m_{\\text{noyau}}$$

- $m_p \\approx 1{,}6726 \\times 10^{-27} \\, kg$ (masse du proton)
- $m_n \\approx 1{,}6749 \\times 10^{-27} \\, kg$ (masse du neutron)

Ce défaut de masse correspond à l'**énergie de liaison** du noyau :

$$E_{\\text{liaison}} = \\Delta m \\times c^2$$

Plus l'énergie de liaison **par nucléon** $\\dfrac{E_{\\text{liaison}}}{A}$ est grande, plus le noyau est **stable**.

---

## La fission nucléaire

### Principe

La **fission** est la cassure d'un noyau lourd en **deux noyaux plus légers** (appelés fragments de fission), accompagnée de l'émission de **neutrons** et d'une **grande quantité d'énergie**.

### Exemple : fission de l'uranium 235

Lorsqu'un noyau d'uranium 235 absorbe un **neutron lent**, il devient instable et se scinde :

$$^{235}_{\\;92} U + ^1_0 n \\longrightarrow ^{144}_{\\;56} Ba + ^{89}_{36} Kr + 3 \\, ^1_0 n + \\text{énergie}$$

> **Remarque :** cette réaction n'est qu'un exemple parmi de nombreuses fissions possibles de l'uranium 235. Les fragments de fission varient d'une réaction à l'autre.

### Réaction en chaîne

Les **neutrons produits** par une fission peuvent provoquer la fission d'**autres noyaux** d'uranium 235. C'est le principe de la **réaction en chaîne** :

- Si elle est **contrôlée** (en absorbant une partie des neutrons) → **centrale nucléaire**
- Si elle est **non contrôlée** (multiplication exponentielle) → **bombe atomique**

### Bilan énergétique

La fission d'un seul noyau d'uranium 235 libère environ :

$$E \\approx 200 \\, MeV \\approx 3{,}2 \\times 10^{-11} \\, J$$

C'est environ **un million de fois** plus d'énergie que la combustion d'un atome de carbone !

> Pour un kilogramme d'uranium 235, l'énergie libérée est de l'ordre de $8 \\times 10^{13} \\, J$, soit l'équivalent de la combustion de **2000 tonnes** de pétrole.

---

## La fusion nucléaire

### Principe

La **fusion** est l'assemblage de **deux noyaux légers** pour former un **noyau plus lourd**, avec libération d'énergie.

### Exemple : fusion de l'hydrogène

Dans les étoiles, le cycle principal est la fusion de noyaux d'hydrogène (protons) en hélium. L'une des réactions de la chaîne proton-proton est :

$$^2_1 H + ^3_1 H \\longrightarrow ^4_2 He + ^1_0 n + \\text{énergie}$$

où $^2_1 H$ est le **deutérium** et $^3_1 H$ le **tritium** (isotopes de l'hydrogène).

### Conditions nécessaires

La fusion nécessite des conditions **extrêmes** :

- **Température** de l'ordre de $10^7$ à $10^8 \\, °C$ pour vaincre la répulsion électrostatique entre les noyaux (tous positifs)
- **Pression** très élevée pour confiner les noyaux suffisamment proches

> Ces conditions existent naturellement au **cœur des étoiles**. Sur Terre, les scientifiques tentent de les reproduire dans des réacteurs expérimentaux comme le projet **ITER** (en construction à Cadarache, en France).

### Bilan énergétique

La fusion de deutérium et de tritium libère environ :

$$E \\approx 17{,}6 \\, MeV \\approx 2{,}8 \\times 10^{-12} \\, J$$

par réaction. Rapportée à la **masse de combustible**, la fusion libère environ **4 fois plus** d'énergie par kilogramme que la fission.

---

## Comparaison fission / fusion

| | **Fission** | **Fusion** |
|--|------------|-----------|
| **Principe** | Cassure d'un noyau lourd | Assemblage de noyaux légers |
| **Combustible** | Uranium 235, Plutonium 239 | Deutérium, Tritium |
| **Conditions** | Neutron lent incident | $T > 10^7 \\, °C$, haute pression |
| **Énergie/kg** | $\\sim 8 \\times 10^{13} \\, J$ | $\\sim 3 \\times 10^{14} \\, J$ |
| **Déchets** | Fragments radioactifs à vie longue | Hélium (non radioactif) + neutrons |
| **Application actuelle** | Centrales nucléaires | Étoiles (sur Terre : en recherche) |

---

## Applications de l'énergie nucléaire

### Les centrales nucléaires (fission)

Dans une centrale nucléaire :

1. La **fission** de l'uranium 235 chauffe de l'eau sous pression dans le **circuit primaire**
2. Cette chaleur est transférée au **circuit secondaire** où l'eau se transforme en vapeur
3. La vapeur fait tourner une **turbine** couplée à un **alternateur** qui produit de l'électricité
4. La vapeur est refroidie par un **circuit de refroidissement** (tours aéroréfrigérantes ou eau de rivière)

> **En France**, environ **70 %** de l'électricité est produite par les centrales nucléaires.

### L'énergie des étoiles (fusion)

Les étoiles comme le **Soleil** tirent leur énergie de la fusion nucléaire de l'hydrogène en hélium dans leur cœur, où la température atteint environ $15 \\times 10^6 \\, °C$.

> L'énergie solaire qui parvient à la Terre provient donc de réactions de **fusion nucléaire** !

### La médecine nucléaire

- **Imagerie** : la scintigraphie utilise des isotopes radioactifs (comme le technétium 99) injectés dans l'organisme pour observer le fonctionnement des organes.
- **Thérapie** : la radiothérapie utilise des rayonnements pour détruire les cellules cancéreuses.
- **TEP** (Tomographie par Émission de Positons) : utilise des isotopes émetteurs $\\beta^+$ comme le fluor 18.

---

## Enjeux et risques

### Avantages de l'énergie nucléaire

- Pas d'émission directe de $CO_2$ (lutte contre le changement climatique)
- Grande quantité d'énergie produite pour peu de combustible
- Production continue (indépendante de la météo)

### Inconvénients et risques

- **Déchets radioactifs** : certains restent dangereux pendant des milliers d'années
- **Risque d'accident** : Tchernobyl (1986), Fukushima (2011)
- **Matières fissiles** : risque de prolifération nucléaire

---

## L'essentiel à retenir

- La **fission** est la cassure d'un noyau lourd → réaction en chaîne → centrales nucléaires.
- La **fusion** est l'assemblage de noyaux légers → énergie des étoiles → projet ITER.
- $E = mc^2$ relie masse et énergie : le **défaut de masse** correspond à l'énergie libérée.
- Les **lois de conservation** ($A$ et $Z$) s'appliquent à toutes les réactions nucléaires.
- L'énergie nucléaire présente des **avantages** (pas de $CO_2$, grande densité énergétique) et des **risques** (déchets, accidents).
""",
                'quiz': {
                    'titre': 'Quiz — Fission, fusion et énergie nucléaire',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "La fission nucléaire est :",
                            'options': ["La cassure d'un noyau lourd en noyaux plus légers", "L'assemblage de noyaux légers en un noyau plus lourd", "La désintégration radioactive naturelle", "L'absorption d'un photon par un noyau"],
                            'reponse_correcte': '0',
                            'explication': "La fission est la cassure d'un noyau lourd (comme l'uranium 235) en deux noyaux plus légers, avec émission de neutrons et d'énergie.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "La fusion nucléaire est :",
                            'options': ["L'assemblage de noyaux légers en un noyau plus lourd", "La cassure d'un noyau lourd", "Un changement d'état de la matière", "La désintégration alpha"],
                            'reponse_correcte': '0',
                            'explication': "La fusion nucléaire est l'assemblage de deux noyaux légers (comme le deutérium et le tritium) pour former un noyau plus lourd avec libération d'énergie.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "La relation d'Einstein reliant masse et énergie est :",
                            'options': ["E = mc²", "E = mv²", "E = mgh", "E = ½mv²"],
                            'reponse_correcte': '0',
                            'explication': "La relation d'Einstein E = mc² montre l'équivalence entre masse et énergie, avec c la vitesse de la lumière.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quel est le combustible principal utilisé dans les centrales nucléaires actuelles ?",
                            'options': ["L'uranium 235", "L'hydrogène", "Le plutonium 240", "L'hélium"],
                            'reponse_correcte': '0',
                            'explication': "Les centrales nucléaires actuelles fonctionnent par fission de l'uranium 235.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Les étoiles comme le Soleil tirent leur énergie de :",
                            'options': ["La fusion nucléaire", "La fission nucléaire", "La combustion chimique", "La radioactivité naturelle"],
                            'reponse_correcte': '0',
                            'explication': "Les étoiles produisent leur énergie par fusion nucléaire de l'hydrogène en hélium, à des températures de l'ordre de 15 millions de °C.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Le défaut de masse d'un noyau est :",
                            'options': ["La différence entre la masse des nucléons séparés et la masse du noyau", "La masse du noyau entier", "La masse des électrons", "La masse perdue par radioactivité"],
                            'reponse_correcte': '0',
                            'explication': "Le défaut de masse Δm = Z×mp + N×mn − m(noyau) correspond à la masse « manquante » convertie en énergie de liaison.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "En France, la part de l'électricité produite par les centrales nucléaires est d'environ :",
                            'options': ["70 %", "30 %", "50 %", "90 %"],
                            'reponse_correcte': '0',
                            'explication': "En France, environ 70 % de l'électricité est produite par les centrales nucléaires (fission de l'uranium).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Lors d'une réaction en chaîne de fission :",
                            'options': ["Les neutrons produits provoquent de nouvelles fissions", "Les protons provoquent de nouvelles fissions", "Les électrons provoquent de nouvelles fissions", "La réaction s'arrête spontanément après une fission"],
                            'reponse_correcte': '0',
                            'explication': "Dans une réaction en chaîne, les neutrons émis par une fission peuvent provoquer la fission d'autres noyaux d'uranium 235.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "L'énergie libérée par la fission d'un seul noyau d'uranium 235 est d'environ :",
                            'options': ["200 MeV", "20 MeV", "2 MeV", "2 000 MeV"],
                            'reponse_correcte': '0',
                            'explication': "La fission d'un noyau d'uranium 235 libère environ 200 MeV, soit environ un million de fois plus qu'une réaction chimique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "La fusion nucléaire nécessite des températures de l'ordre de :",
                            'options': ["10⁷ à 10⁸ °C", "10³ à 10⁴ °C", "10⁵ à 10⁶ °C", "10⁹ à 10¹⁰ °C"],
                            'reponse_correcte': '0',
                            'explication': "La fusion nécessite des températures de 10⁷ à 10⁸ °C pour vaincre la répulsion électrostatique entre les noyaux positifs.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Rapportée à la masse de combustible, la fusion libère par rapport à la fission :",
                            'options': ["Environ 4 fois plus d'énergie", "La même quantité d'énergie", "Environ 4 fois moins d'énergie", "Environ 100 fois plus d'énergie"],
                            'reponse_correcte': '0',
                            'explication': "La fusion libère environ 4 fois plus d'énergie par kilogramme de combustible que la fission.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Le deutérium (²₁H) et le tritium (³₁H) sont :",
                            'options': ["Des isotopes de l'hydrogène", "Des isotopes de l'hélium", "Des éléments chimiques différents", "Des ions de l'hydrogène"],
                            'reponse_correcte': '0',
                            'explication': "Le deutérium (²₁H) et le tritium (³₁H) ont le même Z = 1 que l'hydrogène mais des A différents : ce sont des isotopes de l'hydrogène.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Plus l'énergie de liaison par nucléon est grande, plus le noyau est :",
                            'options': ["Stable", "Instable", "Radioactif", "Lourd"],
                            'reponse_correcte': '0',
                            'explication': "L'énergie de liaison par nucléon mesure la cohésion du noyau : plus elle est élevée, plus le noyau est stable.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Le projet international ITER, en construction à Cadarache, vise à :",
                            'options': ["Reproduire la fusion nucléaire sur Terre", "Construire une nouvelle centrale à fission", "Stocker les déchets nucléaires", "Développer la radioactivité médicale"],
                            'reponse_correcte': '0',
                            'explication': "ITER est un projet international de réacteur expérimental à fusion, en construction à Cadarache en France.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "La fission de l'uranium 235 produit des déchets radioactifs à vie longue.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "La fission produit des fragments radioactifs dont certains ont des demi-vies de milliers d'années, posant un problème de gestion des déchets.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La fusion nucléaire du deutérium et du tritium produit de l'hélium, qui est radioactif.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "L'hélium 4 produit par la fusion est un gaz noble stable et non radioactif. C'est un avantage majeur de la fusion.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Les centrales nucléaires émettent directement du CO₂ lors de la production d'électricité.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Les réactions nucléaires ne produisent pas de CO₂. L'énergie nucléaire n'émet pas directement de gaz à effet de serre.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quelle est la célèbre formule d'Einstein reliant l'énergie E à la masse m ?",
                            'options': None,
                            'reponse_correcte': 'E = mc²',
                            'tolerances': ['E=mc²', 'E = m × c²', 'E=mc^2', 'E = mc^2'],
                            'explication': "La relation d'Einstein E = mc² montre qu'une masse m est équivalente à une énergie E, avec c ≈ 3,00 × 10⁸ m·s⁻¹.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Comment appelle-t-on le phénomène où les neutrons produits par une fission provoquent d'autres fissions en cascade ?",
                            'options': None,
                            'reponse_correcte': 'réaction en chaîne',
                            'tolerances': ['une réaction en chaîne', 'Réaction en chaîne', 'reaction en chaine'],
                            'explication': "La réaction en chaîne se produit quand les neutrons émis par une fission provoquent la fission d'autres noyaux, et ainsi de suite.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quel est le nom du projet international de réacteur à fusion nucléaire en construction à Cadarache, en France ?",
                            'options': None,
                            'reponse_correcte': 'ITER',
                            'tolerances': ['le projet ITER', 'Iter', 'iter', 'projet ITER'],
                            'explication': "ITER (International Thermonuclear Experimental Reactor) est le projet de réacteur expérimental à fusion en construction à Cadarache.",
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
    help = "Seed Chimie Seconde — chapitres 1-11, leçons et quiz."

    def handle(self, *args, **options):
        matiere, created = Matiere.objects.get_or_create(
            nom='chimie',
            defaults={
                'description': "La chimie au lycée : structure de la matière, transformations chimiques, solutions et synthèse.",
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
                niveau='seconde',
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
            f"\n✅ Chimie Seconde — {len(CHAPITRES)} chapitres, {total_lecons} leçons, {total_quizzes} quiz traités."
        ))
