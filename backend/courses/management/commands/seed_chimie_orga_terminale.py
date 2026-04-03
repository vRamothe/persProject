"""
Seed Chimie organique — Terminale chimie, chapitre 13.
3 leçons, 60 questions. Idempotent (update_or_create).
Usage : python manage.py seed_chimie_orga_terminale
"""

from django.core.management.base import BaseCommand
from django.utils.text import slugify


class Command(BaseCommand):
    help = "Charge le chapitre Chimie organique (terminale chimie, ch.13)."

    def handle(self, *args, **options):
        from courses.models import Matiere, Chapitre, Lecon, Quiz, Question

        matiere, _ = Matiere.objects.get_or_create(
            nom="chimie",
            defaults={"description": "Chimie — programme lycée"},
        )

        # ── Chapitre 13 ─────────────────────────────────────────────
        chapitre, created = Chapitre.objects.get_or_create(
            matiere=matiere,
            niveau="terminale",
            ordre=13,
            defaults={
                "titre": "Chimie organique — Représentations, nomenclature et isomérie",
                "description": (
                    "Représentations des molécules organiques, groupes caractéristiques, "
                    "nomenclature IUPAC (mono- et polyfonctionnelle), isomérie de constitution "
                    "et stéréoisomérie (Z/E, chiralité)."
                ),
                "score_minimum_deblocage": 60.0,
            },
        )
        if not created:
            chapitre.titre = "Chimie organique — Représentations, nomenclature et isomérie"
            chapitre.description = (
                "Représentations des molécules organiques, groupes caractéristiques, "
                "nomenclature IUPAC (mono- et polyfonctionnelle), isomérie de constitution "
                "et stéréoisomérie (Z/E, chiralité)."
            )
            chapitre.score_minimum_deblocage = 60.0
            chapitre.save(update_fields=["titre", "description", "score_minimum_deblocage"])

        # ╔══════════════════════════════════════════════════════════════╗
        # ║  LEÇON 1 — Représentations et groupes caractéristiques     ║
        # ╚══════════════════════════════════════════════════════════════╝
        lecon1, _ = Lecon.objects.update_or_create(
            chapitre=chapitre,
            ordre=1,
            defaults={
                "titre": "Représentations et groupes caractéristiques",
                "slug": slugify("Représentations et groupes caractéristiques"),
                "duree_estimee": 35,
                "contenu": LECON1_CONTENU,
            },
        )
        quiz1, _ = Quiz.objects.update_or_create(
            lecon=lecon1,
            defaults={
                "titre": "Quiz — Représentations et groupes caractéristiques",
                "score_minimum": 60.0,
            },
        )
        for q in QUIZ1_QUESTIONS:
            Question.objects.update_or_create(
                quiz=quiz1,
                ordre=q["ordre"],
                defaults={
                    "texte": q["texte"],
                    "type": q["type"],
                    "options": q.get("options"),
                    "reponse_correcte": str(q["reponse_correcte"]),
                    "tolerances": q.get("tolerances"),
                    "explication": q.get("explication", ""),
                    "difficulte": q["difficulte"],
                    "points": q["points"],
                },
            )

        # ╔══════════════════════════════════════════════════════════════╗
        # ║  LEÇON 2 — Nomenclature en chimie organique                ║
        # ╚══════════════════════════════════════════════════════════════╝
        lecon2, _ = Lecon.objects.update_or_create(
            chapitre=chapitre,
            ordre=2,
            defaults={
                "titre": "Nomenclature en chimie organique",
                "slug": slugify("Nomenclature en chimie organique"),
                "duree_estimee": 35,
                "contenu": LECON2_CONTENU,
            },
        )
        quiz2, _ = Quiz.objects.update_or_create(
            lecon=lecon2,
            defaults={
                "titre": "Quiz — Nomenclature en chimie organique",
                "score_minimum": 60.0,
            },
        )
        for q in QUIZ2_QUESTIONS:
            Question.objects.update_or_create(
                quiz=quiz2,
                ordre=q["ordre"],
                defaults={
                    "texte": q["texte"],
                    "type": q["type"],
                    "options": q.get("options"),
                    "reponse_correcte": str(q["reponse_correcte"]),
                    "tolerances": q.get("tolerances"),
                    "explication": q.get("explication", ""),
                    "difficulte": q["difficulte"],
                    "points": q["points"],
                },
            )

        # ╔══════════════════════════════════════════════════════════════╗
        # ║  LEÇON 3 — Isomérie de constitution et stéréoisomérie      ║
        # ╚══════════════════════════════════════════════════════════════╝
        lecon3, _ = Lecon.objects.update_or_create(
            chapitre=chapitre,
            ordre=3,
            defaults={
                "titre": "Isomérie de constitution et stéréoisomérie",
                "slug": slugify("Isomérie de constitution et stéréoisomérie"),
                "duree_estimee": 35,
                "contenu": LECON3_CONTENU,
            },
        )
        quiz3, _ = Quiz.objects.update_or_create(
            lecon=lecon3,
            defaults={
                "titre": "Quiz — Isomérie de constitution et stéréoisomérie",
                "score_minimum": 60.0,
            },
        )
        for q in QUIZ3_QUESTIONS:
            Question.objects.update_or_create(
                quiz=quiz3,
                ordre=q["ordre"],
                defaults={
                    "texte": q["texte"],
                    "type": q["type"],
                    "options": q.get("options"),
                    "reponse_correcte": str(q["reponse_correcte"]),
                    "tolerances": q.get("tolerances"),
                    "explication": q.get("explication", ""),
                    "difficulte": q["difficulte"],
                    "points": q["points"],
                },
            )

        self.stdout.write(
            self.style.SUCCESS("✅ Chapitre Chimie organique (terminale, ch.13) chargé.")
        )


# ═════════════════════════════════════════════════════════════════════════
#  CONTENU DES LEÇONS
# ═════════════════════════════════════════════════════════════════════════

LECON1_CONTENU = r"""# Représentations et groupes caractéristiques

## 1. L'atome de carbone en chimie organique

Le **carbone** (symbole $C$, numéro atomique $Z = 6$) possède la configuration électronique $1s^2\,2s^2\,2p^2$. Sa couche externe contient **4 électrons de valence**, ce qui lui permet de former **4 liaisons covalentes** : c'est la **tétravalence du carbone**.

Cette propriété explique l'extraordinaire diversité des molécules organiques : le carbone peut se lier à d'autres atomes de carbone pour former des **chaînes** (linéaires, ramifiées, cycliques) et des **liaisons multiples** (doubles $C=C$, triples $C \equiv C$).

> **Rappel :** l'hydrogène forme **1 liaison**, l'oxygène **2 liaisons**, l'azote **3 liaisons** et les halogènes (F, Cl, Br, I) **1 liaison**.

---

## 2. Représentations des molécules organiques

### 2.1 Formule brute

La formule brute indique la **nature et le nombre** de chaque atome dans la molécule, sans information sur l'enchaînement.

**Exemple :** $C_2H_6O$ peut représenter l'éthanol **ou** le méthoxyméthane.

### 2.2 Formule développée (Lewis)

On représente **toutes les liaisons covalentes** et les **doublets non liants**. Chaque trait correspond à un doublet liant (2 électrons partagés).

**Exemple — éthanol :**

$$H - \underset{\displaystyle H}{\overset{\displaystyle H}{|}} C - \underset{\displaystyle H}{\overset{\displaystyle H}{|}} C - O - H$$

### 2.3 Formule semi-développée

On écrit les liaisons $C-C$ et $C-O$, $C-N$, etc., mais on **regroupe les atomes d'hydrogène** sur le carbone porteur.

| Molécule | Formule semi-développée |
|---|---|
| Éthanol | CH₃–CH₂–OH |
| Propanone | CH₃–CO–CH₃ |
| Acide éthanoïque | CH₃–COOH |
| Éthanal | CH₃–CHO |

### 2.4 Formule topologique

Seul le **squelette carboné** est tracé sous forme de ligne brisée. Chaque sommet ou extrémité représente un atome de carbone (et ses hydrogènes implicites). Les hétéroatomes ($O$, $N$, $Cl$…) sont écrits explicitement.

**Conventions :**
- Chaque segment = une liaison $C-C$
- Chaque angle = un atome de carbone
- Les hydrogènes portés par les carbones ne sont pas écrits

**Exemples :**
- Le **butan-1-ol** : une ligne brisée de 4 carbones terminée par –OH
- La **propanone** : un angle central portant le groupe $C=O$

---

## 3. Groupes caractéristiques et familles fonctionnelles

Un **groupe caractéristique** (ou groupe fonctionnel) est un arrangement particulier d'atomes responsable des propriétés chimiques de la molécule. La présence d'un groupe caractéristique définit la **famille fonctionnelle**.

| Famille | Groupe caractéristique | Formule | Exemple |
|---|---|---|---|
| **Alcool** | Hydroxyle | $-OH$ | Éthanol CH₃CH₂OH |
| **Aldéhyde** | Carbonyle terminal | $-CHO$ | Éthanal CH₃CHO |
| **Cétone** | Carbonyle interne | $>C=O$ | Propanone CH₃COCH₃ |
| **Acide carboxylique** | Carboxyle | $-COOH$ | Acide éthanoïque CH₃COOH |
| **Amine** | Amino | $-NH_2$ | Éthanamine CH₃CH₂NH₂ |
| **Ester** | Ester | $-COO-$ | Éthanoate d'éthyle CH₃COOC₂H₅ |
| **Amide** | Amide | $-CONH_2$ | Éthanamide CH₃CONH₂ |
| **Halogénoalcane** | Halogéno | $-X$ (X = F, Cl, Br, I) | Chlorométhane CH₃Cl |

### Comment identifier la famille fonctionnelle ?

1. Repérer les **hétéroatomes** (O, N, halogènes) dans la molécule.
2. Identifier l'**arrangement** de ces atomes autour du carbone.
3. En déduire le **groupe caractéristique** et la **famille**.

> **Attention :** un aldéhyde possède le groupe $C=O$ en **bout de chaîne** ($-CHO$), tandis qu'une cétone le possède **à l'intérieur** de la chaîne ($>C=O$ lié à deux carbones).

### Molécules polyfonctionnelles

Une molécule peut porter **plusieurs groupes caractéristiques**. Par exemple, un **acide aminé** porte à la fois un groupe amino ($-NH_2$) et un groupe carboxyle ($-COOH$).

$$H_2N - CHR - COOH$$

où $R$ est la chaîne latérale de l'acide aminé.

---
"""

LECON2_CONTENU = r"""# Nomenclature en chimie organique

## 1. Principes généraux de la nomenclature IUPAC

La nomenclature **IUPAC** (Union Internationale de Chimie Pure et Appliquée) permet de nommer de manière **univoque** toute molécule organique. Le nom systématique d'une molécule est construit en trois parties :

$$\text{préfixe(s) substituant(s)} + \text{chaîne principale} + \text{suffixe (fonction principale)}$$

### Étapes de la nomenclature

1. **Identifier la chaîne carbonée la plus longue** contenant la fonction principale → elle donne le nom de base (méth-, éth-, prop-, but-, pent-, hex-, hept-, oct-…).
2. **Numéroter les carbones** de cette chaîne de façon à donner le **plus petit indice** à la fonction principale.
3. **Nommer les substituants** (groupes alkyle ou fonctions secondaires) en indiquant leur position.
4. **Ajouter le suffixe** correspondant à la fonction principale.

| Nombre de C | Préfixe |
|---|---|
| 1 | méth- |
| 2 | éth- |
| 3 | prop- |
| 4 | but- |
| 5 | pent- |
| 6 | hex- |
| 7 | hept- |
| 8 | oct- |

---

## 2. Suffixes et préfixes par famille fonctionnelle

Le tableau ci-dessous résume les **terminaisons** (quand la fonction est principale) et les **préfixes** (quand la fonction est substituant) utilisés en nomenclature IUPAC :

| Famille | Suffixe (fonction principale) | Préfixe (substituant) |
|---|---|---|
| **Alcool** | -ol | hydroxy- |
| **Aldéhyde** | -al | oxo- |
| **Cétone** | -one | oxo- |
| **Acide carboxylique** | acide ...-oïque | — |
| **Amine** | -amine | amino- |
| **Ester** | -oate de ...-yle | — |
| **Amide** | -amide | — |
| **Halogénoalcane** | — | fluoro-, chloro-, bromo-, iodo- |

**Exemples simples :**
- CH₃CH₂OH → **éthanol** (chaîne de 2 C, fonction alcool → suffixe -ol)
- CH₃CHO → **éthanal** (chaîne de 2 C, fonction aldéhyde → suffixe -al)
- CH₃COCH₃ → **propanone** (chaîne de 3 C, fonction cétone → suffixe -one)
- CH₃COOH → **acide éthanoïque** (chaîne de 2 C, fonction acide → acide ...-oïque)
- CH₃CH₂NH₂ → **éthanamine** (chaîne de 2 C, fonction amine → suffixe -amine)
- CH₃COOC₂H₅ → **éthanoate d'éthyle** (ester, -oate de ...-yle)
- CH₃CONH₂ → **éthanamide** (amide → suffixe -amide)
- CH₃Cl → **chlorométhane** (halogénoalcane, préfixe chloro-)

---

## 3. Nomenclature des molécules polyfonctionnelles

Lorsqu'une molécule possède **plusieurs groupes fonctionnels**, il faut déterminer lequel est la **fonction principale** (nommée par un suffixe) et lesquels sont les **fonctions secondaires** (nommées par un préfixe).

### Ordre de priorité des fonctions

L'ordre de priorité décroissante est le suivant :

$$\text{acide carboxylique} > \text{ester} > \text{amide} > \text{aldéhyde} > \text{cétone} > \text{alcool} > \text{amine}$$

La fonction de **plus haute priorité** est la fonction principale ; les autres sont traitées comme substituants.

### Règles pour la chaîne principale

- La chaîne principale doit être la **plus longue chaîne carbonée** contenant le carbone porteur de la **fonction principale**.
- La numérotation donne le **plus petit indice** possible à la fonction principale.

### Exemples détaillés

**Exemple 1 : acide 3-hydroxypropanoïque**

$$HO - CH_2 - CH_2 - COOH$$

- Fonction principale : acide carboxylique (suffixe : acide ...-oïque)
- Fonction secondaire : alcool (préfixe : hydroxy-)
- Chaîne de 3 carbones → prop-
- Le groupe $-OH$ est sur le carbone 3
- **Nom :** acide 3-hydroxypropanoïque

**Exemple 2 : 4-aminobutan-2-one**

$$H_2N - CH_2 - CH_2 - CO - CH_3$$

- Fonction principale : cétone (suffixe : -one) — prioritaire sur l'amine
- Fonction secondaire : amine (préfixe : amino-)
- Chaîne de 4 carbones → but-
- Le groupe $C=O$ est sur le carbone 2, le groupe $-NH_2$ sur le carbone 4
- **Nom :** 4-aminobutan-2-one

**Exemple 3 : 3-oxopentanal**

$$CH_3 - CH_2 - CO - CH_2 - CHO$$

- Fonction principale : aldéhyde (suffixe : -al) — prioritaire sur la cétone
- Fonction secondaire : cétone (préfixe : oxo-)
- Chaîne de 5 carbones → pent-
- Le groupe aldéhyde impose C-1, le $C=O$ interne est sur C-3
- **Nom :** 3-oxopentanal

> **Astuce :** pour les aldéhydes et les acides carboxyliques, le carbone du groupe fonctionnel est **toujours** le carbone n°1 de la chaîne.

---
"""

LECON3_CONTENU = r"""# Isomérie de constitution et stéréoisomérie

## 1. Isomérie de constitution

Des **isomères de constitution** sont des molécules qui possèdent la **même formule brute** mais des **enchaînements d'atomes différents**. On distingue trois types :

### 1a. Isomérie de chaîne

Les isomères diffèrent par la **structure du squelette carboné** (linéaire vs ramifié).

**Exemple — $C_4H_{10}$ :**
- **Butane** : CH₃–CH₂–CH₂–CH₃ (chaîne linéaire)
- **Méthylpropane** (ou 2-méthylpropane) : (CH₃)₃CH (chaîne ramifiée)

### 1b. Isomérie de position

Les isomères ont le **même squelette carboné** et le **même groupe fonctionnel**, mais celui-ci est fixé à des **positions différentes** sur la chaîne.

**Exemple — $C_4H_{10}O$ (alcool) :**
- **Butan-1-ol** : CH₃CH₂CH₂CH₂OH (–OH sur le carbone 1)
- **Butan-2-ol** : CH₃CH(OH)CH₂CH₃ (–OH sur le carbone 2)

### 1c. Isomérie de fonction

Les isomères possèdent la **même formule brute** mais des **groupes fonctionnels différents** (donc des familles différentes).

**Exemple — $C_2H_6O$ :**
- **Éthanol** : CH₃CH₂OH (alcool)
- **Méthoxyméthane** : CH₃OCH₃ (éther-oxyde)

> **Remarque :** l'éthanol et le méthoxyméthane ont la même formule brute $C_2H_6O$ mais des propriétés chimiques très différentes.

---

## 2. Stéréoisomérie Z/E

La **stéréoisomérie** concerne des molécules qui ont le **même enchaînement d'atomes** mais des **dispositions spatiales différentes**.

### 2a. Condition d'existence

La stéréoisomérie $Z/E$ existe autour d'une **double liaison** $C=C$ lorsque chaque carbone de la double liaison porte **deux substituants différents**.

La double liaison empêche la **rotation libre**, ce qui fige la position relative des substituants.

### 2b. Nomenclature Z / E

On utilise les **règles de priorité CIP** (Cahn-Ingold-Prelog) pour classer les substituants sur chaque carbone de la double liaison :

> Le substituant de **numéro atomique le plus élevé** est **prioritaire**.

- **Z** (*zusammen*, « ensemble ») : les deux substituants prioritaires sont du **même côté** de la double liaison.
- **E** (*entgegen*, « opposé ») : les deux substituants prioritaires sont de **côtés opposés**.

### 2c. Exemple : but-2-ène

Le **but-2-ène** ($CH_3-CH=CH-CH_3$) existe sous deux stéréoisomères :

- **(Z)-but-2-ène** : les deux groupes $-CH_3$ sont du même côté
- **(E)-but-2-ène** : les deux groupes $-CH_3$ sont de côtés opposés

Ces deux molécules ont des **propriétés physiques différentes** (températures de fusion et d'ébullition).

| Propriété | (Z)-but-2-ène | (E)-but-2-ène |
|---|---|---|
| $T_{eb}$ (°C) | 3,7 | 0,9 |
| $T_f$ (°C) | −138,9 | −105,5 |

---

## 3. Chiralité

### 3a. Carbone asymétrique

Un **carbone asymétrique** (noté $C^*$) est un atome de carbone lié à **quatre substituants tous différents**.

**Exemple :** dans le **butan-2-ol**, le carbone 2 porte : $-H$, $-OH$, $-CH_3$ et $-CH_2CH_3$. C'est un carbone asymétrique.

$$CH_3 - \underset{*}{C}H(OH) - CH_2 - CH_3$$

### 3b. Molécule chirale

Une molécule est **chirale** si elle n'est **pas superposable à son image dans un miroir plan**. La présence d'un seul carbone asymétrique suffit (en général) à rendre la molécule chirale.

> **Analogie :** la main gauche et la main droite sont l'image l'une de l'autre dans un miroir, mais elles ne sont pas superposables → elles sont **chirales**.

### 3c. Énantiomères

Deux **énantiomères** sont des stéréoisomères qui sont l'**image l'un de l'autre dans un miroir plan** et qui ne sont **pas superposables**.

**Propriétés des énantiomères :**
- Mêmes propriétés physiques (température de fusion, solubilité, spectre IR, etc.)
- **Activité optique opposée** : l'un dévie la lumière polarisée vers la droite (dextrogyre, noté $+$), l'autre vers la gauche (lévogyre, noté $-$)
- Même réactivité chimique vis-à-vis de réactifs achiraux

### 3d. Diastéréoisomères

Des **diastéréoisomères** sont des stéréoisomères qui **ne sont pas** énantiomères. Ils peuvent résulter :
- de la stéréoisomérie $Z/E$ autour d'une double liaison
- de la présence de **plusieurs** carbones asymétriques

Les diastéréoisomères ont des **propriétés physiques et chimiques différentes**.

### 3e. Mélange racémique

Un **mélange racémique** est un mélange équimolaire (50/50) des deux énantiomères d'une molécule chirale. Il est **optiquement inactif** car les effets de rotation de chaque énantiomère se compensent exactement.

$$[\alpha]_{mélange} = 0$$

> **Application :** de nombreux médicaments sont commercialisés sous forme d'un seul énantiomère actif plutôt qu'en mélange racémique, car les deux énantiomères peuvent avoir des effets biologiques différents (ex : ibuprofène, thalidomide).

---
"""


# ═════════════════════════════════════════════════════════════════════════
#  QUESTIONS — QUIZ 1 (Représentations et groupes caractéristiques)
# ═════════════════════════════════════════════════════════════════════════

QUIZ1_QUESTIONS = [
    # ── 8 QCM facile (points=2) ──────────────────────────────────────
    {
        "ordre": 1,
        "type": "qcm",
        "texte": "Combien de liaisons covalentes l'atome de carbone peut-il former ?",
        "options": ["4", "2", "3", "6"],
        "reponse_correcte": "0",
        "explication": "Le carbone possède 4 électrons de valence et forme 4 liaisons covalentes (tétravalence).",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 2,
        "type": "qcm",
        "texte": "Comment appelle-t-on la propriété du carbone à former 4 liaisons ?",
        "options": ["Tétravalence", "Bivalence", "Trivalence", "Monovalence"],
        "reponse_correcte": "0",
        "explication": "La tétravalence du carbone signifie qu'il forme toujours 4 liaisons covalentes.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 3,
        "type": "qcm",
        "texte": "Dans une formule topologique, que représente chaque sommet de la ligne brisée ?",
        "options": [
            "Un atome de carbone",
            "Un atome d'oxygène",
            "Un atome d'hydrogène",
            "Une liaison double",
        ],
        "reponse_correcte": "0",
        "explication": "En représentation topologique, chaque sommet ou extrémité correspond à un atome de carbone.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 4,
        "type": "qcm",
        "texte": "Quel est le groupe caractéristique de la famille des alcools ?",
        "options": ["–OH (hydroxyle)", "–CHO (carbonyle)", "–COOH (carboxyle)", "–NH₂ (amino)"],
        "reponse_correcte": "0",
        "explication": "Le groupe hydroxyle –OH définit la famille des alcools.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 5,
        "type": "qcm",
        "texte": "Quelle est la formule semi-développée de l'éthanol ?",
        "options": ["CH₃–CH₂–OH", "CH₃–CHO", "CH₃–COOH", "CH₃–CO–CH₃"],
        "reponse_correcte": "0",
        "explication": "L'éthanol est un alcool à 2 carbones : CH₃–CH₂–OH.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 6,
        "type": "qcm",
        "texte": "À quelle famille appartient la propanone (CH₃COCH₃) ?",
        "options": ["Cétone", "Aldéhyde", "Alcool", "Ester"],
        "reponse_correcte": "0",
        "explication": "La propanone possède un groupe C=O interne (carbonyle entre deux carbones) : c'est une cétone.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 7,
        "type": "qcm",
        "texte": "Quel groupe caractéristique définit un acide carboxylique ?",
        "options": ["–COOH (carboxyle)", "–OH (hydroxyle)", "–CHO (carbonyle)", "–NH₂ (amino)"],
        "reponse_correcte": "0",
        "explication": "Le groupe carboxyle –COOH définit la famille des acides carboxyliques.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 8,
        "type": "qcm",
        "texte": "À quelle famille appartient CH₃CH₂NH₂ ?",
        "options": ["Amine", "Amide", "Alcool", "Aldéhyde"],
        "reponse_correcte": "0",
        "explication": "Le groupe –NH₂ fixé sur un carbone non lié à un C=O définit une amine.",
        "difficulte": "facile",
        "points": 2,
    },
    # ── 6 QCM moyen (points=1) ───────────────────────────────────────
    {
        "ordre": 9,
        "type": "qcm",
        "texte": "Quelle est la différence entre un aldéhyde et une cétone ?",
        "options": [
            "L'aldéhyde a le C=O en bout de chaîne, la cétone à l'intérieur",
            "L'aldéhyde est cyclique, la cétone est linéaire",
            "L'aldéhyde contient de l'azote, pas la cétone",
            "Il n'y a aucune différence",
        ],
        "reponse_correcte": "0",
        "explication": "Le groupe carbonyle est terminal (–CHO) dans un aldéhyde et interne (>C=O) dans une cétone.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 10,
        "type": "qcm",
        "texte": "Quelle formule brute peut correspondre à la fois à un alcool et à un éther-oxyde ?",
        "options": ["C₂H₆O", "C₂H₄O₂", "C₃H₈", "CH₄O₂"],
        "reponse_correcte": "0",
        "explication": "C₂H₆O correspond à l'éthanol (alcool) et au méthoxyméthane (éther-oxyde).",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 11,
        "type": "qcm",
        "texte": "Quel est le groupe caractéristique d'un ester ?",
        "options": ["–COO–", "–COOH", "–CHO", "–CONH₂"],
        "reponse_correcte": "0",
        "explication": "Le groupe ester est –COO–, c'est-à-dire un C=O lié à un O relié à un groupe alkyle.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 12,
        "type": "qcm",
        "texte": "Combien de liaisons covalentes l'azote forme-t-il habituellement ?",
        "options": ["3", "2", "4", "1"],
        "reponse_correcte": "0",
        "explication": "L'azote possède 5 électrons de valence et forme habituellement 3 liaisons covalentes.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 13,
        "type": "qcm",
        "texte": "Quelle information une formule semi-développée ne donne-t-elle PAS ?",
        "options": [
            "La géométrie spatiale de la molécule",
            "L'enchaînement des atomes",
            "Les liaisons C–C",
            "La nature des atomes présents",
        ],
        "reponse_correcte": "0",
        "explication": "La formule semi-développée montre l'enchaînement mais pas la géométrie 3D.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 14,
        "type": "qcm",
        "texte": "Quel groupe caractéristique porte l'éthanamide (CH₃CONH₂) ?",
        "options": ["–CONH₂ (amide)", "–NH₂ (amino)", "–CHO (carbonyle)", "–COO– (ester)"],
        "reponse_correcte": "0",
        "explication": "L'éthanamide porte le groupe amide –CONH₂ (un C=O lié à un –NH₂).",
        "difficulte": "moyen",
        "points": 1,
    },
    # ── 3 vrai/faux moyen (points=1) ─────────────────────────────────
    {
        "ordre": 15,
        "type": "vrai_faux",
        "texte": "Dans une formule topologique, les atomes d'hydrogène liés aux carbones sont écrits explicitement.",
        "options": ["Vrai", "Faux"],
        "reponse_correcte": "faux",
        "explication": "En formule topologique, les hydrogènes liés aux carbones sont implicites ; seuls les hétéroatomes sont écrits.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 16,
        "type": "vrai_faux",
        "texte": "Un acide aminé possède à la fois un groupe amino et un groupe carboxyle.",
        "options": ["Vrai", "Faux"],
        "reponse_correcte": "vrai",
        "explication": "Un acide aminé porte un groupe –NH₂ (amino) et un groupe –COOH (carboxyle).",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 17,
        "type": "vrai_faux",
        "texte": "Un halogénoalcane contient obligatoirement un atome d'oxygène.",
        "options": ["Vrai", "Faux"],
        "reponse_correcte": "faux",
        "explication": "Un halogénoalcane contient un halogène (F, Cl, Br, I), pas nécessairement d'oxygène.",
        "difficulte": "moyen",
        "points": 1,
    },
    # ── 3 texte_libre difficile (points=2) ────────────────────────────
    {
        "ordre": 18,
        "type": "texte_libre",
        "texte": "Quel est le nom de la propriété du carbone qui lui permet de former exactement 4 liaisons covalentes ?",
        "options": None,
        "reponse_correcte": "tétravalence",
        "tolerances": ["tetravalence", "la tétravalence", "la tetravalence", "tétra-valence"],
        "explication": "La tétravalence du carbone découle de ses 4 électrons de valence.",
        "difficulte": "difficile",
        "points": 2,
    },
    {
        "ordre": 19,
        "type": "texte_libre",
        "texte": "Donner le nom de la famille fonctionnelle dont le groupe caractéristique est –CHO.",
        "options": None,
        "reponse_correcte": "aldéhyde",
        "tolerances": ["aldehyde", "les aldéhydes", "famille des aldéhydes", "un aldéhyde"],
        "explication": "Le groupe –CHO (carbonyle terminal) définit la famille des aldéhydes.",
        "difficulte": "difficile",
        "points": 2,
    },
    {
        "ordre": 20,
        "type": "texte_libre",
        "texte": "Quelle est la formule semi-développée de l'acide éthanoïque ?",
        "options": None,
        "reponse_correcte": "CH₃COOH",
        "tolerances": ["CH3COOH", "CH3-COOH", "CH₃–COOH", "CH₃-COOH"],
        "explication": "L'acide éthanoïque (acide acétique) a pour formule CH₃COOH.",
        "difficulte": "difficile",
        "points": 2,
    },
]


# ═════════════════════════════════════════════════════════════════════════
#  QUESTIONS — QUIZ 2 (Nomenclature en chimie organique)
# ═════════════════════════════════════════════════════════════════════════

QUIZ2_QUESTIONS = [
    # ── 8 QCM facile (points=2) ──────────────────────────────────────
    {
        "ordre": 1,
        "type": "qcm",
        "texte": "Quel suffixe IUPAC désigne la fonction alcool ?",
        "options": ["-ol", "-al", "-one", "-amine"],
        "reponse_correcte": "0",
        "explication": "Le suffixe -ol est utilisé pour nommer les alcools.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 2,
        "type": "qcm",
        "texte": "Quel est le nom IUPAC de CH₃CHO ?",
        "options": ["Éthanal", "Éthanol", "Propanone", "Acide éthanoïque"],
        "reponse_correcte": "0",
        "explication": "CH₃CHO est un aldéhyde à 2 carbones : éthanal (suffixe -al).",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 3,
        "type": "qcm",
        "texte": "Quel préfixe correspond à une chaîne de 3 atomes de carbone ?",
        "options": ["Prop-", "Éth-", "Méth-", "But-"],
        "reponse_correcte": "0",
        "explication": "Le préfixe prop- indique une chaîne de 3 carbones.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 4,
        "type": "qcm",
        "texte": "Quel est le nom IUPAC de CH₃COCH₃ ?",
        "options": ["Propanone", "Éthanal", "Propanal", "Éthanol"],
        "reponse_correcte": "0",
        "explication": "CH₃COCH₃ possède une fonction cétone sur 3 carbones : propanone.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 5,
        "type": "qcm",
        "texte": "Quel suffixe correspond à la fonction acide carboxylique ?",
        "options": ["acide ...-oïque", "-ol", "-al", "-amide"],
        "reponse_correcte": "0",
        "explication": "Les acides carboxyliques se nomment « acide + chaîne + oïque ».",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 6,
        "type": "qcm",
        "texte": "Quel est le nom IUPAC de CH₃CH₂OH ?",
        "options": ["Éthanol", "Méthanol", "Propanol", "Éthanal"],
        "reponse_correcte": "0",
        "explication": "Chaîne de 2 C + fonction alcool = éthanol.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 7,
        "type": "qcm",
        "texte": "Comment nomme-t-on CH₃Cl en nomenclature IUPAC ?",
        "options": ["Chlorométhane", "Méthylchlorure", "Chloroéthane", "Fluorométhane"],
        "reponse_correcte": "0",
        "explication": "Un halogène fixé sur un méthane : préfixe chloro- + méthane = chlorométhane.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 8,
        "type": "qcm",
        "texte": "Quel est le nom IUPAC de CH₃COOC₂H₅ ?",
        "options": [
            "Éthanoate d'éthyle",
            "Acide éthanoïque",
            "Éthanal",
            "Propanoate de méthyle",
        ],
        "reponse_correcte": "0",
        "explication": "C'est un ester : la partie acide est l'acide éthanoïque, le groupe alkyle est éthyle → éthanoate d'éthyle.",
        "difficulte": "facile",
        "points": 2,
    },
    # ── 6 QCM moyen (points=1) ───────────────────────────────────────
    {
        "ordre": 9,
        "type": "qcm",
        "texte": "Quelle fonction est prioritaire entre une cétone et un alcool ?",
        "options": ["Cétone", "Alcool", "Elles sont de même priorité", "Amine"],
        "reponse_correcte": "0",
        "explication": "Dans l'ordre de priorité IUPAC, la cétone est prioritaire sur l'alcool.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 10,
        "type": "qcm",
        "texte": "Quel est le nom IUPAC de HO–CH₂–CH₂–COOH ?",
        "options": [
            "Acide 3-hydroxypropanoïque",
            "3-hydroxypropanol",
            "Acide 2-hydroxypropanoïque",
            "Propane-1,3-diol",
        ],
        "reponse_correcte": "0",
        "explication": "Fonction principale : acide carboxylique (prioritaire sur l'alcool). Chaîne de 3 C. OH sur C-3.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 11,
        "type": "qcm",
        "texte": "Quel préfixe utilise-t-on lorsque la fonction alcool est un substituant ?",
        "options": ["Hydroxy-", "Oxo-", "Amino-", "Chloro-"],
        "reponse_correcte": "0",
        "explication": "Quand l'alcool n'est pas la fonction principale, on utilise le préfixe hydroxy-.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 12,
        "type": "qcm",
        "texte": "Quel est le nom IUPAC de H₂N–CH₂–CH₂–CO–CH₃ ?",
        "options": [
            "4-aminobutan-2-one",
            "1-aminobutan-3-one",
            "4-aminobutanal",
            "Butan-2-one-4-amine",
        ],
        "reponse_correcte": "0",
        "explication": "La cétone est prioritaire sur l'amine. Chaîne de 4 C, C=O en position 2, NH₂ en position 4.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 13,
        "type": "qcm",
        "texte": "Pourquoi numérote-t-on la chaîne pour donner le plus petit indice à la fonction principale ?",
        "options": [
            "C'est une règle IUPAC pour un nom univoque",
            "Pour raccourcir le nom de la molécule",
            "Par convention esthétique uniquement",
            "Pour faciliter le calcul de la masse molaire",
        ],
        "reponse_correcte": "0",
        "explication": "La règle du plus petit indice permet d'obtenir un seul nom possible pour chaque molécule.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 14,
        "type": "qcm",
        "texte": "Quel préfixe indique un substituant C=O (cétone ou aldéhyde secondaire) ?",
        "options": ["Oxo-", "Hydroxy-", "Amino-", "Méthyl-"],
        "reponse_correcte": "0",
        "explication": "Le préfixe oxo- désigne un groupe C=O utilisé comme substituant.",
        "difficulte": "moyen",
        "points": 1,
    },
    # ── 3 vrai/faux moyen (points=1) ─────────────────────────────────
    {
        "ordre": 15,
        "type": "vrai_faux",
        "texte": "L'acide carboxylique est la fonction de plus haute priorité en nomenclature IUPAC (parmi les fonctions courantes du programme).",
        "options": ["Vrai", "Faux"],
        "reponse_correcte": "vrai",
        "explication": "L'ordre de priorité place l'acide carboxylique au sommet : acide > ester > amide > aldéhyde > cétone > alcool > amine.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 16,
        "type": "vrai_faux",
        "texte": "Le carbone du groupe aldéhyde (–CHO) porte toujours le numéro 1 dans la chaîne.",
        "options": ["Vrai", "Faux"],
        "reponse_correcte": "vrai",
        "explication": "Par convention, le carbone de l'aldéhyde est toujours en position 1 de la chaîne principale.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 17,
        "type": "vrai_faux",
        "texte": "Le préfixe « amino- » est utilisé lorsque la fonction amine est la fonction principale de la molécule.",
        "options": ["Vrai", "Faux"],
        "reponse_correcte": "faux",
        "explication": "Quand l'amine est la fonction principale, on utilise le suffixe -amine. Le préfixe amino- s'utilise quand l'amine est substituant.",
        "difficulte": "moyen",
        "points": 1,
    },
    # ── 3 texte_libre difficile (points=2) ────────────────────────────
    {
        "ordre": 18,
        "type": "texte_libre",
        "texte": "Donner le nom IUPAC de la molécule CH₃CH₂CH₂COOH.",
        "options": None,
        "reponse_correcte": "acide butanoïque",
        "tolerances": ["acide butanoique", "acide butanoïque", "Acide butanoïque", "Acide butanoique"],
        "explication": "Chaîne de 4 carbones + groupe carboxyle = acide butanoïque.",
        "difficulte": "difficile",
        "points": 2,
    },
    {
        "ordre": 19,
        "type": "texte_libre",
        "texte": "Quel suffixe utilise-t-on pour nommer un amide en nomenclature IUPAC ?",
        "options": None,
        "reponse_correcte": "-amide",
        "tolerances": ["amide", "le suffixe -amide", "le suffixe amide"],
        "explication": "Les amides portent le suffixe -amide (ex : éthanamide).",
        "difficulte": "difficile",
        "points": 2,
    },
    {
        "ordre": 20,
        "type": "texte_libre",
        "texte": "Donner le nom IUPAC de CH₃CH₂CO–CH₂CHO (un pentanal avec un C=O en position 3).",
        "options": None,
        "reponse_correcte": "3-oxopentanal",
        "tolerances": ["3-oxo-pentanal", "3-oxopentanal"],
        "explication": "Fonction principale aldéhyde (suffixe -al), C=O secondaire en position 3 (préfixe oxo-), chaîne de 5 C.",
        "difficulte": "difficile",
        "points": 2,
    },
]


# ═════════════════════════════════════════════════════════════════════════
#  QUESTIONS — QUIZ 3 (Isomérie de constitution et stéréoisomérie)
# ═════════════════════════════════════════════════════════════════════════

QUIZ3_QUESTIONS = [
    # ── 8 QCM facile (points=2) ──────────────────────────────────────
    {
        "ordre": 1,
        "type": "qcm",
        "texte": "Des isomères de constitution possèdent :",
        "options": [
            "La même formule brute mais des enchaînements différents",
            "La même formule développée",
            "La même disposition spatiale",
            "Des formules brutes différentes",
        ],
        "reponse_correcte": "0",
        "explication": "Les isomères de constitution partagent la même formule brute mais diffèrent par l'enchaînement des atomes.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 2,
        "type": "qcm",
        "texte": "Le butane et le méthylpropane sont des isomères :",
        "options": ["De chaîne", "De position", "De fonction", "Z/E"],
        "reponse_correcte": "0",
        "explication": "Ils ont la même formule brute C₄H₁₀ mais des chaînes carbonées différentes (linéaire vs ramifiée).",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 3,
        "type": "qcm",
        "texte": "Le butan-1-ol et le butan-2-ol sont des isomères :",
        "options": ["De position", "De chaîne", "De fonction", "Z/E"],
        "reponse_correcte": "0",
        "explication": "Le groupe –OH est sur le C1 dans le butan-1-ol et sur le C2 dans le butan-2-ol : isomérie de position.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 4,
        "type": "qcm",
        "texte": "Que signifie la lettre Z dans la notation Z/E ?",
        "options": [
            "Zusammen (ensemble, même côté)",
            "Zentral (central)",
            "Zéro (pas de rotation)",
            "Zone (proche)",
        ],
        "reponse_correcte": "0",
        "explication": "Z vient de l'allemand « zusammen » signifiant « ensemble » : les groupes prioritaires sont du même côté.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 5,
        "type": "qcm",
        "texte": "Qu'est-ce qu'un carbone asymétrique ?",
        "options": [
            "Un carbone portant 4 substituants tous différents",
            "Un carbone portant 2 substituants identiques",
            "Un carbone formant une double liaison",
            "Un carbone en bout de chaîne",
        ],
        "reponse_correcte": "0",
        "explication": "Un carbone asymétrique (C*) est lié à 4 groupes substituants tous différents.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 6,
        "type": "qcm",
        "texte": "Deux énantiomères sont :",
        "options": [
            "Images l'un de l'autre dans un miroir et non superposables",
            "Des molécules de formules brutes différentes",
            "Des molécules identiques",
            "Des isomères de constitution",
        ],
        "reponse_correcte": "0",
        "explication": "Des énantiomères sont des stéréoisomères images miroir non superposables.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 7,
        "type": "qcm",
        "texte": "L'éthanol (CH₃CH₂OH) et le méthoxyméthane (CH₃OCH₃) sont des isomères :",
        "options": ["De fonction", "De chaîne", "De position", "Z/E"],
        "reponse_correcte": "0",
        "explication": "Même formule brute C₂H₆O, mais groupes fonctionnels différents (alcool vs éther) : isomérie de fonction.",
        "difficulte": "facile",
        "points": 2,
    },
    {
        "ordre": 8,
        "type": "qcm",
        "texte": "Qu'est-ce qu'un mélange racémique ?",
        "options": [
            "Un mélange 50/50 des deux énantiomères",
            "Un mélange d'isomères de chaîne",
            "Un mélange d'isomères Z et E",
            "Une solution saturée",
        ],
        "reponse_correcte": "0",
        "explication": "Un mélange racémique contient les deux énantiomères en proportions égales ; il est optiquement inactif.",
        "difficulte": "facile",
        "points": 2,
    },
    # ── 6 QCM moyen (points=1) ───────────────────────────────────────
    {
        "ordre": 9,
        "type": "qcm",
        "texte": "Quelle condition est nécessaire pour observer une stéréoisomérie Z/E ?",
        "options": [
            "Une double liaison C=C avec 2 substituants différents sur chaque carbone",
            "Un carbone asymétrique",
            "Une triple liaison",
            "Une liaison simple C–C avec rotation libre",
        ],
        "reponse_correcte": "0",
        "explication": "La stéréoisomérie Z/E nécessite une C=C (pas de rotation libre) et deux substituants différents sur chaque C.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 10,
        "type": "qcm",
        "texte": "Le (Z)-but-2-ène et le (E)-but-2-ène sont :",
        "options": [
            "Des diastéréoisomères",
            "Des énantiomères",
            "Des isomères de constitution",
            "La même molécule",
        ],
        "reponse_correcte": "0",
        "explication": "Ce sont des stéréoisomères qui ne sont pas images miroir l'un de l'autre : ce sont des diastéréoisomères.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 11,
        "type": "qcm",
        "texte": "Selon les règles CIP, quel atome est prioritaire entre Cl et O ?",
        "options": [
            "Cl (Z=17 > Z=8)",
            "O (Z=8 > Z=17)",
            "Ils sont de même priorité",
            "On ne peut pas les comparer",
        ],
        "reponse_correcte": "0",
        "explication": "En CIP, le numéro atomique le plus élevé est prioritaire : Cl (Z=17) > O (Z=8).",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 12,
        "type": "qcm",
        "texte": "Deux énantiomères ont :",
        "options": [
            "Les mêmes propriétés physiques mais une activité optique opposée",
            "Des propriétés physiques différentes",
            "La même activité optique",
            "Des formules brutes différentes",
        ],
        "reponse_correcte": "0",
        "explication": "Les énantiomères partagent les mêmes propriétés physiques mais dévient la lumière polarisée en sens opposés.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 13,
        "type": "qcm",
        "texte": "Le butan-2-ol possède-t-il un carbone asymétrique ?",
        "options": [
            "Oui, le carbone 2 porte 4 substituants différents",
            "Non, tous les carbones sont identiques",
            "Oui, le carbone 1",
            "Non, il n'y a pas de double liaison",
        ],
        "reponse_correcte": "0",
        "explication": "Le C2 du butan-2-ol porte –H, –OH, –CH₃ et –CH₂CH₃ : 4 substituants différents → C*.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 14,
        "type": "qcm",
        "texte": "Des diastéréoisomères ont :",
        "options": [
            "Des propriétés physiques et chimiques différentes",
            "Les mêmes propriétés physiques",
            "Toujours la même température de fusion",
            "La même activité optique",
        ],
        "reponse_correcte": "0",
        "explication": "Contrairement aux énantiomères, les diastéréoisomères ont des propriétés physiques et chimiques différentes.",
        "difficulte": "moyen",
        "points": 1,
    },
    # ── 3 vrai/faux moyen (points=1) ─────────────────────────────────
    {
        "ordre": 15,
        "type": "vrai_faux",
        "texte": "Un mélange racémique est optiquement actif.",
        "options": ["Vrai", "Faux"],
        "reponse_correcte": "faux",
        "explication": "Un mélange racémique (50/50) est optiquement inactif : les rotations des deux énantiomères se compensent.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 16,
        "type": "vrai_faux",
        "texte": "Deux isomères de constitution ont toujours la même formule brute.",
        "options": ["Vrai", "Faux"],
        "reponse_correcte": "vrai",
        "explication": "Par définition, des isomères de constitution ont la même formule brute mais des enchaînements différents.",
        "difficulte": "moyen",
        "points": 1,
    },
    {
        "ordre": 17,
        "type": "vrai_faux",
        "texte": "La stéréoisomérie Z/E peut exister autour d'une liaison simple C–C.",
        "options": ["Vrai", "Faux"],
        "reponse_correcte": "faux",
        "explication": "La rotation libre autour d'une liaison simple empêche l'existence de stéréoisomères Z/E ; il faut une double liaison C=C.",
        "difficulte": "moyen",
        "points": 1,
    },
    # ── 3 texte_libre difficile (points=2) ────────────────────────────
    {
        "ordre": 18,
        "type": "texte_libre",
        "texte": "Comment appelle-t-on deux stéréoisomères qui sont images l'un de l'autre dans un miroir plan et non superposables ?",
        "options": None,
        "reponse_correcte": "énantiomères",
        "tolerances": ["enantiomeres", "des énantiomères", "des enantiomères", "énantiomère", "enantiomere"],
        "explication": "Deux stéréoisomères liés par une relation objet/image miroir non superposable sont des énantiomères.",
        "difficulte": "difficile",
        "points": 2,
    },
    {
        "ordre": 19,
        "type": "texte_libre",
        "texte": "Quel critère permet de déterminer la priorité des substituants dans les règles CIP ?",
        "options": None,
        "reponse_correcte": "numéro atomique",
        "tolerances": [
            "le numéro atomique",
            "numero atomique",
            "le numero atomique",
            "numéro atomique le plus élevé",
            "Z le plus élevé",
        ],
        "explication": "Les règles CIP (Cahn-Ingold-Prelog) classent les substituants par numéro atomique décroissant.",
        "difficulte": "difficile",
        "points": 2,
    },
    {
        "ordre": 20,
        "type": "texte_libre",
        "texte": "Donner le nom du type d'isomérie entre le butan-1-ol et le butan-2-ol.",
        "options": None,
        "reponse_correcte": "isomérie de position",
        "tolerances": [
            "isomerie de position",
            "isomérie de position",
            "position",
            "isomères de position",
        ],
        "explication": "Même squelette, même fonction alcool, mais position différente du –OH : isomérie de position.",
        "difficulte": "difficile",
        "points": 2,
    },
]
