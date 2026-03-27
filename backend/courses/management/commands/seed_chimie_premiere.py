"""
Seed Chimie Première — chapitres 1-10, leçons uniquement (sans quiz).
Usage : python manage.py seed_chimie_premiere
"""

from django.core.management.base import BaseCommand
from courses.models import Matiere, Chapitre, Lecon

CHAPITRES = [
    # ──────────────────────────────────────────────
    # CHAPITRE 1 — Structure et propriétés de la matière
    # ──────────────────────────────────────────────
    {
        'ordre': 1,
        'titre': 'Structure et propriétés de la matière',
        'description': "Comprendre la structure microscopique de la matière, les liaisons chimiques et les propriétés qui en découlent.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Modèles atomiques et structure électronique',
                'duree': 35,
                'contenu': """# Modèles atomiques et structure électronique

## Modèle de l’atome

Un **atome** est constitué d’un noyau (protons et neutrons) et d’électrons gravitant autour. Le numéro atomique $Z$ correspond au nombre de protons.

- **Proton** : charge $+e$
- **Neutron** : charge $0$
- **Électron** : charge $-e$

La masse de l’atome est concentrée dans le noyau.

## Structure électronique

Les électrons occupent des **couches électroniques** ($K$, $L$, $M$...) selon la règle de remplissage ($2n^2$ électrons max par couche).

- Couche $K$ : 2 électrons max
- Couche $L$ : 8 électrons max
- Couche $M$ : 18 électrons max

**Exemple :** $Z=11$ (sodium) : $K^2L^8M^1$

## Notion d’ion

Un **ion** est un atome ou un groupe d’atomes ayant gagné ou perdu un ou plusieurs électrons :
- **Cation** : ion positif (perte d’électrons)
- **Anion** : ion négatif (gain d’électrons)

---
""",
                'quiz': {
                    'titre': 'Quiz — Modèles atomiques et structure électronique',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Quel est le numéro atomique du sodium ?", 'options': ["11", "12", "23", "8"], 'reponse_correcte': '0', 'explication': "Le sodium a $Z=11$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Où se concentre la masse d'un atome ?", 'options': ["Dans le noyau", "Dans les électrons", "Dans la couche K", "Dans la couche M"], 'reponse_correcte': '0', 'explication': "La masse est concentrée dans le noyau.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Combien d'électrons maximum peut contenir la couche L ?", 'options': ["8", "2", "18", "32"], 'reponse_correcte': '0', 'explication': "La couche L peut contenir 8 électrons.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Un cation est :", 'options': ["Un ion positif", "Un ion négatif", "Un atome neutre", "Un électron"], 'reponse_correcte': '0', 'explication': "Un cation est un ion positif.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Quel est le symbole de la charge élémentaire ?", 'options': ["e", "p", "n", "q"], 'reponse_correcte': '0', 'explication': "La charge élémentaire est notée $e$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Un atome de $Z=8$ a combien de protons ?", 'options': ["8", "16", "2", "0"], 'reponse_correcte': '0', 'explication': "Le numéro atomique donne le nombre de protons.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Un anion est :", 'options': ["Un ion négatif", "Un ion positif", "Un atome neutre", "Un proton"], 'reponse_correcte': '0', 'explication': "Un anion est un ion négatif.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "La couche K peut contenir au maximum :", 'options': ["2 électrons", "8 électrons", "18 électrons", "1 électron"], 'reponse_correcte': '0', 'explication': "La couche K = 2 électrons max.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Quelle est la configuration électronique du sodium ($Z=11$) ?", 'options': ["K2L8M1", "K2L8M2", "K2L7M2", "K2L8M8"], 'reponse_correcte': '0', 'explication': "$Z=11$ : K2L8M1.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Quel est le nombre de neutrons dans $^{23}_{11}Na$ ?", 'options': ["12", "11", "23", "8"], 'reponse_correcte': '0', 'explication': "23-11=12 neutrons.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Un ion $Cl^-$ possède :", 'options': ["Un électron de plus que l'atome neutre", "Un électron de moins", "Un proton de plus", "Un neutron de moins"], 'reponse_correcte': '0', 'explication': "Cl- a gagné un électron.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "La charge d'un proton est :", 'options': ["+e", "-e", "0", "+2e"], 'reponse_correcte': '0', 'explication': "Le proton porte la charge élémentaire positive.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Quel est le nombre d'électrons dans $O^{2-}$ ? ($Z=8$)", 'options': ["10", "8", "6", "12"], 'reponse_correcte': '0', 'explication': "8+2=10 électrons.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "La masse d'un électron est :", 'options': ["Négligeable devant celle du proton", "Égale à celle du proton", "Égale à celle du neutron", "Double de celle du proton"], 'reponse_correcte': '0', 'explication': "La masse de l'électron est très faible.", 'difficulte': 'moyen', 'points': 1},
                        # 3 vrai/faux
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Un atome est électriquement neutre.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "Le nombre de protons = nombre d'électrons.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Un ion est toujours négatif.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Un ion peut être positif (cation) ou négatif (anion).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "La couche M peut contenir jusqu'à 18 électrons.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "C'est la règle 2n².", 'difficulte': 'moyen', 'points': 1},
                        # 3 texte_libre
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner la définition d'un cation.", 'reponse_correcte': "Ion positif", 'tolerances': ["cation positif", "ion chargé positivement"], 'explication': "Un cation est un ion ayant perdu un ou plusieurs électrons.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Quelle est la charge d'un électron ?", 'reponse_correcte': "-e", 'tolerances': ["charge négative", "moins e"], 'explication': "L'électron porte la charge élémentaire négative.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Compléter : la configuration électronique de l'atome de carbone ($Z=6$) est ...", 'reponse_correcte': "K2L4", 'tolerances': ["K2 L4", "K 2 L 4"], 'explication': "Le carbone : 6 électrons = K2L4.", 'difficulte': 'difficile', 'points': 1},
                    ]
                },
            },
            {
                'ordre': 2,
                'titre': 'Liaisons chimiques et molécules',
                'duree': 35,
                'contenu': """# Liaisons chimiques et molécules

## Liaison covalente

Une **liaison covalente** correspond à la mise en commun de deux électrons entre deux atomes pour former une molécule.

- **Schéma de Lewis** : permet de représenter les liaisons et doublets non liants.
- **Règle de l’octet** : les atomes tendent à acquérir 8 électrons sur leur couche externe (2 pour $H$, $He$).

**Exemple :** $H_2O$ : l’oxygène forme deux liaisons simples avec deux hydrogènes.

## Géométrie des molécules

La forme d’une molécule dépend du nombre de liaisons et de doublets non liants (méthode VSEPR) :
- $CO_2$ : linéaire
- $H_2O$ : coudée
- $CH_4$ : tétraédrique

## Propriétés physiques

Les propriétés (température de fusion, solubilité, etc.) dépendent de la structure et des interactions entre molécules (liaisons hydrogène, Van der Waals).

---
""",
                'quiz': {
                    'titre': 'Quiz — Liaisons chimiques et molécules',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Qu'est-ce qu'une liaison covalente ?", 'options': ["Mise en commun de deux électrons", "Transfert d'un électron", "Attraction entre ions", "Interaction de Van der Waals"], 'reponse_correcte': '0', 'explication': "Une liaison covalente est une mise en commun d'électrons.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Quel schéma permet de représenter les doublets non liants ?", 'options': ["Schéma de Lewis", "Schéma de Bohr", "Diagramme de phases", "Schéma de Rutherford"], 'reponse_correcte': '0', 'explication': "Le schéma de Lewis montre les doublets liants et non liants.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Combien de liaisons simples l'oxygène forme-t-il dans $H_2O$ ?", 'options': ["2", "1", "3", "4"], 'reponse_correcte': '0', 'explication': "L'oxygène forme 2 liaisons simples dans l'eau.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Quelle est la géométrie de $CO_2$ ?", 'options': ["Linéaire", "Coudée", "Tétraédrique", "Pyramidale"], 'reponse_correcte': '0', 'explication': "$CO_2$ est linéaire.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "La règle de l’octet concerne :", 'options': ["8 électrons sur la couche externe", "2 électrons sur la couche K", "18 électrons sur la couche M", "4 électrons sur la couche L"], 'reponse_correcte': '0', 'explication': "La règle de l’octet = 8 électrons sur la couche externe.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Quelle interaction explique la température d’ébullition élevée de l’eau ?", 'options': ["Liaison hydrogène", "Liaison covalente", "Interaction ionique", "Van der Waals"], 'reponse_correcte': '0', 'explication': "Les liaisons hydrogène expliquent la forte température d’ébullition de l’eau.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "La forme du méthane ($CH_4$) est :", 'options': ["Tétraédrique", "Linéaire", "Coudée", "Plane"], 'reponse_correcte': '0', 'explication': "$CH_4$ est tétraédrique.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Les interactions de Van der Waals sont :", 'options': ["Faibles", "Forts", "Toujours ioniques", "Toujours covalentes"], 'reponse_correcte': '0', 'explication': "Les interactions de Van der Waals sont faibles.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Combien de doublets non liants possède l’oxygène dans $H_2O$ ?", 'options': ["2", "1", "0", "3"], 'reponse_correcte': '0', 'explication': "L’oxygène a 2 doublets non liants dans l’eau.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Quelle molécule est coudée ?", 'options': ["H_2O", "CO_2", "CH_4", "C_2H_6"], 'reponse_correcte': '0', 'explication': "$H_2O$ est coudée.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "La température de fusion dépend de :", 'options': ["La structure et des interactions", "La masse molaire uniquement", "La couleur", "Le nombre d’atomes"], 'reponse_correcte': '0', 'explication': "La structure et les interactions influencent la fusion.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "La liaison hydrogène existe entre :", 'options': ["O-H...O", "C-H...C", "N-H...N uniquement", "F-H...F uniquement"], 'reponse_correcte': '0', 'explication': "Liaison hydrogène : O-H...O, N-H...N, F-H...F.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "La solubilité dépend de :", 'options': ["La nature des interactions", "La température uniquement", "La pression uniquement", "La couleur du solvant"], 'reponse_correcte': '0', 'explication': "La solubilité dépend de la nature des interactions.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "La molécule $CO_2$ est :", 'options': ["Linéaire et apolaire", "Coudée et polaire", "Tétraédrique et polaire", "Plane et polaire"], 'reponse_correcte': '0', 'explication': "$CO_2$ est linéaire et apolaire.", 'difficulte': 'moyen', 'points': 1},
                        # 3 vrai/faux
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "La règle de l’octet s’applique à tous les atomes.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Certains atomes (H, He) suivent la règle du duet.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Les liaisons hydrogène sont plus fortes que les liaisons covalentes.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Les liaisons covalentes sont plus fortes.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "La molécule d’eau est polaire.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "La molécule d’eau est polaire.", 'difficulte': 'facile', 'points': 1},
                        # 3 texte_libre
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner la définition d’une liaison covalente.", 'reponse_correcte': "Mise en commun de deux électrons", 'tolerances': ["partage d’électrons", "partage de deux électrons"], 'explication': "Une liaison covalente est une mise en commun de deux électrons.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Compléter : la molécule $CH_4$ est ...", 'reponse_correcte': "tétraédrique", 'tolerances': ["forme tétraédrique", "structure tétraédrique"], 'explication': "$CH_4$ est tétraédrique.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Quelle interaction explique la solubilité de l’éthanol dans l’eau ?", 'reponse_correcte': "liaison hydrogène", 'tolerances': ["liaisons hydrogène", "hydrogène"], 'explication': "La liaison hydrogène explique la solubilité de l’éthanol dans l’eau.", 'difficulte': 'difficile', 'points': 1},
                    ]
                },
            },
            {
                'ordre': 3,
                'titre': 'Solides, liquides et gaz : organisation et propriétés',
                'duree': 30,
                'contenu': """# Solides, liquides et gaz : organisation et propriétés

## États de la matière

- **Solide** : particules ordonnées, fortes interactions, forme propre
- **Liquide** : particules désordonnées, interactions modérées, forme du récipient
- **Gaz** : particules très dispersées, interactions faibles, compressible

## Changement d’état

- **Fusion** : solide → liquide
- **Vaporisation** : liquide → gaz
- **Condensation** : gaz → liquide
- **Solidification** : liquide → solide

## Diagramme d’état

Un **diagramme de phases** représente les domaines de stabilité des états en fonction de la température et de la pression.

---
""",
                'quiz': {
                    'titre': 'Quiz — Solides, liquides et gaz : organisation et propriétés',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Quel état de la matière a une forme propre ?", 'options': ["Solide", "Liquide", "Gaz", "Plasma"], 'reponse_correcte': '0', 'explication': "Le solide a une forme propre.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Dans quel état les particules sont-elles très dispersées ?", 'options': ["Gaz", "Solide", "Liquide", "Plasma"], 'reponse_correcte': '0', 'explication': "Dans l'état gazeux, les particules sont très dispersées.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Quel changement d’état correspond à liquide → gaz ?", 'options': ["Vaporisation", "Fusion", "Condensation", "Solidification"], 'reponse_correcte': '0', 'explication': "Liquide → gaz = vaporisation.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Quel changement d’état correspond à solide → liquide ?", 'options': ["Fusion", "Vaporisation", "Condensation", "Solidification"], 'reponse_correcte': '0', 'explication': "Solide → liquide = fusion.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Quel état est compressible ?", 'options': ["Gaz", "Solide", "Liquide", "Plasma"], 'reponse_correcte': '0', 'explication': "Le gaz est compressible.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Dans quel état les interactions sont-elles les plus fortes ?", 'options': ["Solide", "Liquide", "Gaz", "Plasma"], 'reponse_correcte': '0', 'explication': "Les interactions sont les plus fortes dans le solide.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Un diagramme de phases représente :", 'options': ["Les domaines de stabilité des états", "La masse des particules", "La couleur des substances", "La densité du solide"], 'reponse_correcte': '0', 'explication': "Il montre les domaines de stabilité des états.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Quel état n’a pas de forme propre ?", 'options': ["Liquide", "Solide", "Gaz", "Plasma"], 'reponse_correcte': '0', 'explication': "Le liquide n’a pas de forme propre.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Quel changement d’état correspond à gaz → liquide ?", 'options': ["Condensation", "Fusion", "Vaporisation", "Solidification"], 'reponse_correcte': '0', 'explication': "Gaz → liquide = condensation.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Quel changement d’état correspond à liquide → solide ?", 'options': ["Solidification", "Fusion", "Vaporisation", "Condensation"], 'reponse_correcte': '0', 'explication': "Liquide → solide = solidification.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Dans quel état la matière est-elle la moins dense ?", 'options': ["Gaz", "Solide", "Liquide", "Plasma"], 'reponse_correcte': '0', 'explication': "Le gaz est le moins dense.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Quel état prend la forme de son récipient ?", 'options': ["Liquide", "Solide", "Gaz", "Plasma"], 'reponse_correcte': '0', 'explication': "Le liquide prend la forme du récipient.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Quel état est le plus ordonné ?", 'options': ["Solide", "Liquide", "Gaz", "Plasma"], 'reponse_correcte': '0', 'explication': "Le solide est le plus ordonné.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Quel état est le plus désordonné ?", 'options': ["Gaz", "Solide", "Liquide", "Plasma"], 'reponse_correcte': '0', 'explication': "Le gaz est le plus désordonné.", 'difficulte': 'moyen', 'points': 1},
                        # 3 vrai/faux
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Le solide est compressible.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Le solide n’est pas compressible.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Le gaz n’a pas de forme propre.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "Le gaz prend la forme du récipient.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Le liquide est plus dense que le solide.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Le solide est généralement plus dense.", 'difficulte': 'moyen', 'points': 1},
                        # 3 texte_libre
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner la définition d’un diagramme de phases.", 'reponse_correcte': "Représentation des domaines de stabilité des états", 'tolerances': ["diagramme des états", "stabilité des états"], 'explication': "Un diagramme de phases montre les domaines de stabilité.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Compléter : solide → liquide = ...", 'reponse_correcte': "fusion", 'tolerances': ["la fusion"], 'explication': "Solide → liquide = fusion.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Quel état est compressible ?", 'reponse_correcte': "gaz", 'tolerances': ["le gaz"], 'explication': "Le gaz est compressible.", 'difficulte': 'facile', 'points': 1},
                    ]
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 2 — Réactions d’oxydo-réduction
    # ──────────────────────────────────────────────
    {
        'ordre': 2,
        'titre': 'Réactions d’oxydo-réduction',
        'description': "Identifier et écrire les réactions d’oxydo-réduction, comprendre les transferts d’électrons.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Couples oxydant/réducteur et demi-équations',
                'duree': 35,
                'contenu': """# Couples oxydant/réducteur et demi-équations

## Définitions

- **Oxydant** : espèce chimique susceptible de capter un ou plusieurs électrons.
- **Réducteur** : espèce chimique susceptible de céder un ou plusieurs électrons.

Un **couple oxydant/réducteur** s’écrit $Ox/Réd$.

## Demi-équation électronique

- Réduction : $Ox + ne^- \to Réd$
- Oxydation : $Réd \to Ox + ne^-$

**Exemple :** $Fe^{3+} + e^- \to Fe^{2+}$

## Équilibrage

On équilibre d’abord les éléments autres que $O$ et $H$, puis $O$ avec $H_2O$, $H$ avec $H^+$, et enfin les charges avec $e^-$.

---
""",
                'quiz': {
                    'titre': 'Quiz — Couples oxydant/réducteur et demi-équations',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Qu'est-ce qu'un oxydant ?", 'options': ["Espèce qui capte des électrons", "Espèce qui cède des électrons", "Un ion négatif", "Un gaz inerte"], 'reponse_correcte': '0', 'explication': "Un oxydant capte des électrons.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Qu'est-ce qu'un réducteur ?", 'options': ["Espèce qui cède des électrons", "Espèce qui capte des électrons", "Un ion positif", "Un gaz noble"], 'reponse_correcte': '0', 'explication': "Un réducteur cède des électrons.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Comment s’écrit un couple oxydant/réducteur ?", 'options': ["Ox/Réd", "Réd/Ox", "Ox+Réd", "Réd-Ox"], 'reponse_correcte': '0', 'explication': "On note Ox/Réd.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Dans la demi-équation $Fe^{3+} + e^- \to Fe^{2+}$, $Fe^{3+}$ est :", 'options': ["L’oxydant", "Le réducteur", "Un gaz", "Un solvant"], 'reponse_correcte': '0', 'explication': "$Fe^{3+}$ capte un électron, c’est l’oxydant.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Que représente $e^-$ dans une demi-équation ?", 'options': ["Un électron", "Un proton", "Un neutron", "Un atome"], 'reponse_correcte': '0', 'explication': "$e^-$ est un électron.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Quel est le rôle du réducteur dans une réaction ?", 'options': ["Il cède des électrons", "Il capte des électrons", "Il ne réagit pas", "Il change d’état"], 'reponse_correcte': '0', 'explication': "Le réducteur cède des électrons.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Dans $Cu^{2+} + 2e^- \to Cu$, $Cu^{2+}$ est :", 'options': ["L’oxydant", "Le réducteur", "Un gaz", "Un acide"], 'reponse_correcte': '0', 'explication': "$Cu^{2+}$ capte des électrons, c’est l’oxydant.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Dans $Zn \to Zn^{2+} + 2e^-$, $Zn$ est :", 'options': ["Le réducteur", "L’oxydant", "Un solvant", "Un gaz"], 'reponse_correcte': '0', 'explication': "$Zn$ cède des électrons, c’est le réducteur.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Quel est le produit de la réduction de $Fe^{3+}$ ?", 'options': ["Fe^{2+}", "Fe", "Fe^{4+}", "FeO"], 'reponse_correcte': '0', 'explication': "$Fe^{3+}$ + e- → $Fe^{2+}$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Dans la demi-équation $Réd \to Ox + ne^-$, que se passe-t-il ?", 'options': ["Oxydation", "Réduction", "Neutralisation", "Précipitation"], 'reponse_correcte': '0', 'explication': "C’est une oxydation.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Comment équilibre-t-on l’oxygène dans une demi-équation ?", 'options': ["Avec $H_2O$", "Avec $H^+$", "Avec $e^-$", "Avec $O_2$"], 'reponse_correcte': '0', 'explication': "On équilibre O avec $H_2O$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Comment équilibre-t-on l’hydrogène ?", 'options': ["Avec $H^+$", "Avec $H_2O$", "Avec $e^-$", "Avec $O_2$"], 'reponse_correcte': '0', 'explication': "On équilibre H avec $H^+$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Comment équilibre-t-on les charges ?", 'options': ["Avec $e^-$", "Avec $H^+$", "Avec $H_2O$", "Avec $O_2$"], 'reponse_correcte': '0', 'explication': "On équilibre les charges avec les électrons.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Un couple oxydant/réducteur correspond à :", 'options': ["Deux formes d’un même élément à des états d’oxydation différents", "Deux éléments différents", "Un ion et une molécule", "Deux gaz"], 'reponse_correcte': '0', 'explication': "C’est le même élément à deux états d’oxydation.", 'difficulte': 'moyen', 'points': 1},
                        # 3 vrai/faux
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Un oxydant capte des électrons.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "C’est la définition d’un oxydant.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Un réducteur capte des électrons.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Un réducteur cède des électrons.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "On équilibre toujours les charges avec $H^+$.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "On équilibre les charges avec les électrons.", 'difficulte': 'moyen', 'points': 1},
                        # 3 texte_libre
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner la définition d’un oxydant.", 'reponse_correcte': "Espèce qui capte des électrons", 'tolerances': ["accepte des électrons", "reçoit des électrons"], 'explication': "Un oxydant capte des électrons.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Compléter : $Fe^{3+} + e^- \to$ ...", 'reponse_correcte': "Fe^{2+}", 'tolerances': ["Fe2+", "fer(II)"], 'explication': "La réduction de $Fe^{3+}$ donne $Fe^{2+}$.", 'difficulte': 'difficile', 'points': 1},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Comment équilibre-t-on l’oxygène dans une demi-équation ?", 'reponse_correcte': "Avec H_2O", 'tolerances': ["H2O", "eau"], 'explication': "On équilibre O avec $H_2O$.", 'difficulte': 'difficile', 'points': 1},
                    ]
                },
            },
            {
                'ordre': 2,
                'titre': 'Réactions d’oxydo-réduction et prévision',
                'duree': 35,
                'contenu': """# Réactions d’oxydo-réduction et prévision

## Réaction d’oxydo-réduction

Une **réaction d’oxydo-réduction** met en jeu un transfert d’électrons entre un oxydant et un réducteur.

**Exemple :**
$$
Zn + Cu^{2+} \to Zn^{2+} + Cu
$$

- $Zn$ est le réducteur (il s’oxyde)
- $Cu^{2+}$ est l’oxydant (il se réduit)

## Prévision du sens de la réaction

La réaction se fait entre l’oxydant le plus fort et le réducteur le plus fort (règle du gamma).

## Nombre d’oxydation

Le **nombre d’oxydation** (NO) permet de suivre les transferts d’électrons :
- Monoatomique : NO = charge de l’ion
- Molécule : somme des NO = 0
- Ion polyatomique : somme des NO = charge de l’ion

---
""",
                'quiz': {
                    'titre': 'Quiz — Réactions d’oxydo-réduction et prévision',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Qu’est-ce qu’une réaction d’oxydo-réduction ?", 'options': ["Transfert d’électrons", "Transfert de protons", "Changement d’état", "Dissolution"], 'reponse_correcte': '0', 'explication': "C’est un transfert d’électrons.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Dans $Zn + Cu^{2+} \to Zn^{2+} + Cu$, qui est l’oxydant ?", 'options': ["Cu^{2+}", "Zn", "Zn^{2+}", "Cu"], 'reponse_correcte': '0', 'explication': "$Cu^{2+}$ capte des électrons.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Dans la réaction ci-dessus, qui est le réducteur ?", 'options': ["Zn", "Cu^{2+}", "Zn^{2+}", "Cu"], 'reponse_correcte': '0', 'explication': "$Zn$ cède des électrons.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "La règle du gamma permet de :", 'options': ["Prévoir le sens de la réaction", "Calculer la masse molaire", "Déterminer la solubilité", "Écrire une équation de Lewis"], 'reponse_correcte': '0', 'explication': "La règle du gamma prédit le sens de la réaction.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Le nombre d’oxydation d’un ion monoatomique est :", 'options': ["Égal à sa charge", "Toujours zéro", "Égal au nombre de protons", "Égal au nombre de neutrons"], 'reponse_correcte': '0', 'explication': "NO = charge de l’ion.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Dans une molécule, la somme des nombres d’oxydation est :", 'options': ["0", "1", "Égal à la charge", "Toujours négative"], 'reponse_correcte': '0', 'explication': "Dans une molécule, somme NO = 0.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Dans un ion polyatomique, la somme des NO est :", 'options': ["Égale à la charge de l’ion", "Toujours 0", "Toujours positive", "Toujours négative"], 'reponse_correcte': '0', 'explication': "Dans un ion polyatomique, somme NO = charge.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Le réducteur est l’espèce qui :", 'options': ["Cède des électrons", "Capte des électrons", "Change d’état", "Est un gaz"], 'reponse_correcte': '0', 'explication': "Le réducteur cède des électrons.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Dans $Fe^{3+} + e^- \to Fe^{2+}$, que fait $Fe^{3+}$ ?", 'options': ["Il se réduit", "Il s’oxyde", "Il change d’état", "Il précipite"], 'reponse_correcte': '0', 'explication': "$Fe^{3+}$ capte un électron, il se réduit.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Dans $Zn \to Zn^{2+} + 2e^-$, que fait $Zn$ ?", 'options': ["Il s’oxyde", "Il se réduit", "Il précipite", "Il change d’état"], 'reponse_correcte': '0', 'explication': "$Zn$ cède des électrons, il s’oxyde.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Le nombre d’oxydation de $O$ dans $H_2O$ est :", 'options': ["-2", "+2", "0", "+1"], 'reponse_correcte': '0', 'explication': "Dans $H_2O$, NO de O = -2.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Le nombre d’oxydation de $H$ dans $H_2O$ est :", 'options': ["+1", "-1", "0", "+2"], 'reponse_correcte': '0', 'explication': "Dans $H_2O$, NO de H = +1.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Dans $SO_4^{2-}$, la somme des NO est :", 'options': ["-2", "0", "+2", "+4"], 'reponse_correcte': '0', 'explication': "Dans $SO_4^{2-}$, somme NO = -2.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Dans $NO_3^-$, la somme des NO est :", 'options': ["-1", "0", "+1", "+3"], 'reponse_correcte': '0', 'explication': "Dans $NO_3^-$, somme NO = -1.", 'difficulte': 'moyen', 'points': 1},
                        # 3 vrai/faux
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Le sens de la réaction dépend de la règle du gamma.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "La règle du gamma prédit le sens.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Un oxydant cède des électrons.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Un oxydant capte des électrons.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Le nombre d’oxydation d’un atome dans une molécule est toujours positif.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Il peut être négatif, nul ou positif.", 'difficulte': 'moyen', 'points': 1},
                        # 3 texte_libre
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner la définition d’une réaction d’oxydo-réduction.", 'reponse_correcte': "Transfert d’électrons", 'tolerances': ["échange d’électrons", "transfert d’e-"], 'explication': "C’est un transfert d’électrons.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Compléter : dans $Zn + Cu^{2+} \to$ ...", 'reponse_correcte': "Zn^{2+} + Cu", 'tolerances': ["Zn2+ + Cu", "ion zinc(II) et cuivre"], 'explication': "On obtient $Zn^{2+}$ et $Cu$.", 'difficulte': 'difficile', 'points': 1},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Comment calcule-t-on le nombre d’oxydation d’un ion monoatomique ?", 'reponse_correcte': "Égal à la charge", 'tolerances': ["charge de l’ion", "valeur de la charge"], 'explication': "NO = charge de l’ion.", 'difficulte': 'difficile', 'points': 1},
                    ]
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 3 — Quantité de matière en solution
    # ──────────────────────────────────────────────
    {
        'ordre': 3,
        'titre': 'Quantité de matière en solution',
        'description': "Calculer la quantité de matière, préparer une solution, utiliser la concentration molaire.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Quantité de matière et concentration',
                'duree': 30,
                'contenu': """# Quantité de matière et concentration

## Quantité de matière

La **quantité de matière** $n$ (en mol) est liée au nombre d’entités $N$ par :
$$
n = \frac{N}{N_A}
$$
avec $N_A = 6{,}02 \times 10^{23}$ mol$^{-1}$ (constante d’Avogadro).

## Masse et volume molaire

- $n = \frac{m}{M}$ avec $m$ la masse (g), $M$ la masse molaire (g/mol)
- $n = \frac{V}{V_m}$ pour un gaz ($V_m = 24{,}0$ L/mol à 20°C)

## Concentration molaire

La **concentration molaire** $C$ (en mol/L) :
$$
C = \frac{n}{V}
$$
avec $V$ en L.

---
""",
                'quiz': {
                    'titre': 'Quiz — Quantité de matière et concentration',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Quelle est la valeur de la constante d'Avogadro ?", 'options': ["6,02 × 10²³ mol⁻¹", "6,02 × 10²² mol⁻¹", "6,02 × 10²⁴ mol⁻¹", "3,00 × 10²³ mol⁻¹"], 'reponse_correcte': '0', 'explication': "$N_A = 6{,}02 \\times 10^{23}$ mol$^{-1}$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Quelle est la formule de la quantité de matière à partir de la masse ?", 'options': ["n = m / M", "n = M / m", "n = m × M", "n = M × V"], 'reponse_correcte': '0', 'explication': "$n = m / M$ avec $m$ en g et $M$ en g/mol.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Quelle est l'unité de la quantité de matière ?", 'options': ["mol", "g", "L", "mol/L"], 'reponse_correcte': '0', 'explication': "La quantité de matière s'exprime en moles.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Quelle est l'unité de la concentration molaire ?", 'options': ["mol/L", "g/L", "mol", "L/mol"], 'reponse_correcte': '0', 'explication': "La concentration molaire s'exprime en mol/L.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Quelle est la formule de la concentration molaire ?", 'options': ["C = n / V", "C = V / n", "C = n × V", "C = m / V"], 'reponse_correcte': '0', 'explication': "$C = n / V$ avec $V$ en L.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Le volume molaire d'un gaz à 20 °C vaut :", 'options': ["24,0 L/mol", "22,4 L/mol", "12,0 L/mol", "48,0 L/mol"], 'reponse_correcte': '0', 'explication': "$V_m = 24{,}0$ L/mol à 20 °C.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "La masse molaire de l'eau ($H_2O$) vaut environ :", 'options': ["18 g/mol", "16 g/mol", "20 g/mol", "2 g/mol"], 'reponse_correcte': '0', 'explication': "$M(H_2O) = 2 \\times 1 + 16 = 18$ g/mol.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "1 mol de particules contient :", 'options': ["6,02 × 10²³ entités", "6,02 × 10²² entités", "1 000 entités", "10⁶ entités"], 'reponse_correcte': '0', 'explication': "1 mol = $N_A$ = $6{,}02 \\times 10^{23}$ entités.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Quelle masse de NaCl ($M = 58{,}5$ g/mol) faut-il pour préparer 500 mL d'une solution à 0,10 mol/L ?", 'options': ["2,93 g", "5,85 g", "0,585 g", "29,3 g"], 'reponse_correcte': '0', 'explication': "$n = C \\times V = 0{,}10 \\times 0{,}500 = 0{,}050$ mol ; $m = n \\times M = 0{,}050 \\times 58{,}5 = 2{,}93$ g.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Quelle est la quantité de matière dans 9,0 g d'eau ($M = 18$ g/mol) ?", 'options': ["0,50 mol", "0,25 mol", "1,0 mol", "2,0 mol"], 'reponse_correcte': '0', 'explication': "$n = 9{,}0 / 18 = 0{,}50$ mol.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Un gaz occupe 4,8 L à 20 °C. Sa quantité de matière vaut :", 'options': ["0,20 mol", "0,48 mol", "4,8 mol", "2,0 mol"], 'reponse_correcte': '0', 'explication': "$n = V / V_m = 4{,}8 / 24{,}0 = 0{,}20$ mol.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "On dissout 0,20 mol de glucose dans 250 mL d'eau. La concentration est :", 'options': ["0,80 mol/L", "0,20 mol/L", "0,50 mol/L", "0,050 mol/L"], 'reponse_correcte': '0', 'explication': "$C = 0{,}20 / 0{,}250 = 0{,}80$ mol/L.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "La masse molaire du dioxygène ($O_2$) est :", 'options': ["32 g/mol", "16 g/mol", "48 g/mol", "64 g/mol"], 'reponse_correcte': '0', 'explication': "$M(O_2) = 2 \\times 16 = 32$ g/mol.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Combien de molécules contient 0,50 mol d'eau ?", 'options': ["3,01 × 10²³", "6,02 × 10²³", "1,20 × 10²⁴", "3,01 × 10²²"], 'reponse_correcte': '0', 'explication': "$N = n \\times N_A = 0{,}50 \\times 6{,}02 \\times 10^{23} = 3{,}01 \\times 10^{23}$.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Le volume molaire d'un gaz dépend de la nature du gaz.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "Le volume molaire ne dépend que de la température et de la pression, pas de la nature du gaz.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "La masse molaire du CO₂ est 44 g/mol.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'vrai', 'explication': "$M(CO_2) = 12 + 2 \\times 16 = 44$ g/mol.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "La quantité de matière est un nombre sans dimension.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "La quantité de matière s'exprime en moles (mol).", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Calculer la quantité de matière dans 11,2 L de diazote ($N_2$) à 20 °C ($V_m = 24{,}0$ L/mol). Donner le résultat en mol, arrondi au centième.", 'options': None, 'reponse_correcte': '0,47 mol', 'tolerances': ['0,47', '0.47 mol', '0.47'], 'explication': "$n = 11{,}2 / 24{,}0 \\approx 0{,}47$ mol.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Donner la formule reliant la quantité de matière $n$, le nombre d'entités $N$ et la constante d'Avogadro $N_A$.", 'options': None, 'reponse_correcte': 'n = N / NA', 'tolerances': ['n = N/NA', 'n=N/Na', 'n = N / N_A'], 'explication': "$n = N / N_A$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "On prépare 200 mL d'une solution de sulfate de cuivre à $C = 0{,}050$ mol/L. Quelle masse de $CuSO_4$ ($M = 160$ g/mol) faut-il peser ? Donner la réponse en grammes.", 'options': None, 'reponse_correcte': '1,6 g', 'tolerances': ['1,6', '1.6 g', '1.6'], 'explication': "$n = C \\times V = 0{,}050 \\times 0{,}200 = 0{,}010$ mol ; $m = 0{,}010 \\times 160 = 1{,}6$ g.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Préparation et dilution d’une solution',
                'duree': 30,
                'contenu': """# Préparation et dilution d’une solution

## Préparation d’une solution

Pour préparer une solution de concentration $C$ :
- Peser la masse $m$ de soluté
- Dissoudre dans un volume $V$ de solvant
- Homogénéiser

## Dilution

Pour obtenir une solution diluée ($C_f$) à partir d’une solution mère ($C_i$) :
$$
C_i \times V_i = C_f \times V_f
$$

On prélève $V_i$ de la solution mère, on complète à $V_f$ avec le solvant.

## Verrerie utilisée

- Fiole jaugée (volume précis)
- Pipette jaugée (prélèvement précis)
- Bécher, éprouvette

---
""",
                'quiz': {
                    'titre': "Quiz — Préparation et dilution d'une solution",
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Quelle verrerie permet de mesurer un volume précis pour une solution ?", 'options': ["Fiole jaugée", "Bécher", "Erlenmeyer", "Ballon à fond rond"], 'reponse_correcte': '0', 'explication': "La fiole jaugée permet de mesurer un volume précis.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Quelle verrerie sert à prélever un volume précis de solution ?", 'options': ["Pipette jaugée", "Éprouvette graduée", "Bécher", "Burette"], 'reponse_correcte': '0', 'explication': "La pipette jaugée permet un prélèvement précis.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Lors d'une dilution, on ajoute :", 'options': ["Du solvant", "Du soluté", "Un indicateur", "Un catalyseur"], 'reponse_correcte': '0', 'explication': "Diluer = ajouter du solvant.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Quelle est la relation de dilution ?", 'options': ["Ci × Vi = Cf × Vf", "Ci / Vi = Cf / Vf", "Ci + Vi = Cf + Vf", "Ci × Vf = Cf × Vi"], 'reponse_correcte': '0', 'explication': "$C_i \\times V_i = C_f \\times V_f$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Lors d'une dilution, la quantité de matière de soluté :", 'options': ["Reste constante", "Augmente", "Diminue", "Double"], 'reponse_correcte': '0', 'explication': "Le nombre de moles de soluté ne change pas lors d'une dilution.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "On complète à $V_f$ avec :", 'options': ["Le solvant", "Le soluté", "Un acide", "Une base"], 'reponse_correcte': '0', 'explication': "On complète le volume final avec du solvant.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Le facteur de dilution $F$ est défini par :", 'options': ["F = Ci / Cf", "F = Cf / Ci", "F = Vi / Vf", "F = Ci × Cf"], 'reponse_correcte': '0', 'explication': "$F = C_i / C_f = V_f / V_i$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Pour préparer une solution par dissolution, la première étape est :", 'options': ["Peser le soluté", "Ajouter le solvant", "Agiter", "Chauffer"], 'reponse_correcte': '0', 'explication': "On commence par peser la masse de soluté nécessaire.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "On dilue 10 fois une solution mère à 0,50 mol/L. La concentration fille est :", 'options': ["0,050 mol/L", "0,50 mol/L", "5,0 mol/L", "0,005 mol/L"], 'reponse_correcte': '0', 'explication': "$C_f = C_i / F = 0{,}50 / 10 = 0{,}050$ mol/L.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Pour préparer 100 mL de solution à 0,10 mol/L à partir d'une solution mère à 1,0 mol/L, quel volume prélever ?", 'options': ["10 mL", "1 mL", "100 mL", "50 mL"], 'reponse_correcte': '0', 'explication': "$V_i = C_f \\times V_f / C_i = 0{,}10 \\times 100 / 1{,}0 = 10$ mL.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Quelle est la différence entre une éprouvette graduée et une pipette jaugée ?", 'options': ["La pipette jaugée est plus précise", "L'éprouvette est plus précise", "Elles sont identiques", "La pipette mesure la masse"], 'reponse_correcte': '0', 'explication': "La pipette jaugée offre une précision supérieure.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Le facteur de dilution d'une solution passant de 2,0 mol/L à 0,10 mol/L est :", 'options': ["20", "10", "2", "200"], 'reponse_correcte': '0', 'explication': "$F = 2{,}0 / 0{,}10 = 20$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "On prélève 5,0 mL d'une solution à 0,20 mol/L et on complète à 100 mL. La concentration finale est :", 'options': ["0,010 mol/L", "0,020 mol/L", "0,10 mol/L", "0,001 mol/L"], 'reponse_correcte': '0', 'explication': "$C_f = C_i \\times V_i / V_f = 0{,}20 \\times 5{,}0 / 100 = 0{,}010$ mol/L.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Pourquoi faut-il homogénéiser la solution après dissolution ?", 'options': ["Pour que la concentration soit uniforme", "Pour augmenter la température", "Pour diminuer le volume", "Pour changer le solvant"], 'reponse_correcte': '0', 'explication': "L'homogénéisation assure une concentration uniforme dans toute la solution.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Lors d'une dilution, la concentration de la solution augmente.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "Lors d'une dilution, la concentration diminue.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "La fiole jaugée est utilisée pour mesurer un volume précis.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'vrai', 'explication': "La fiole jaugée est un instrument de verrerie de précision.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Lors d'une dilution, on ajoute du soluté pour diminuer la concentration.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "On ajoute du solvant, pas du soluté.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "On veut préparer 250 mL d'une solution de NaCl à 0,20 mol/L à partir d'une solution mère à 2,0 mol/L. Quel volume de solution mère faut-il prélever ?", 'options': None, 'reponse_correcte': '25 mL', 'tolerances': ['25', '25,0 mL', '0,025 L'], 'explication': "$V_i = C_f \\times V_f / C_i = 0{,}20 \\times 250 / 2{,}0 = 25$ mL.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Énoncer la relation de conservation lors d'une dilution.", 'options': None, 'reponse_correcte': 'Ci × Vi = Cf × Vf', 'tolerances': ['CiVi = CfVf', 'Ci.Vi = Cf.Vf', 'C1V1 = C2V2'], 'explication': "La quantité de matière de soluté est conservée : $C_i V_i = C_f V_f$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Quel est le facteur de dilution si l'on passe de 0,50 mol/L à 0,025 mol/L ?", 'options': None, 'reponse_correcte': '20', 'tolerances': ['F = 20', 'facteur 20', 'x20'], 'explication': "$F = 0{,}50 / 0{,}025 = 20$.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 4 — Réactions acido-basiques
    # ──────────────────────────────────────────────
    {
        'ordre': 4,
        'titre': 'Réactions acido-basiques',
        'description': "Définir acide et base, écrire les équations de réaction, comprendre le pH et les dosages acido-basiques.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Définitions : acides, bases et couples',
                'duree': 30,
                'contenu': """# Définitions : acides, bases et couples

## Acide et base (selon Brønsted)

- **Acide** : espèce capable de céder un proton $H^+$
- **Base** : espèce capable de capter un proton $H^+$

Un **couple acide/base** s’écrit $AH/A^-$.

**Exemple :** $CH_3COOH/CH_3COO^-$

## Réaction acido-basique

Transfert de proton entre un acide et une base :
$$
AH + B \to A^- + BH^+
$$

---
""",
                'quiz': {
                    'titre': 'Quiz — Définitions : acides, bases et couples',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Selon Brønsted, un acide est une espèce qui :", 'options': ["Cède un proton H⁺", "Capte un proton H⁺", "Cède un électron", "Capte un électron"], 'reponse_correcte': '0', 'explication': "Un acide de Brønsted cède un proton $H^+$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Selon Brønsted, une base est une espèce qui :", 'options': ["Capte un proton H⁺", "Cède un proton H⁺", "Cède un électron", "Capte un électron"], 'reponse_correcte': '0', 'explication': "Une base de Brønsted capte un proton $H^+$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Comment s'écrit un couple acide/base ?", 'options': ["AH / A⁻", "A⁻ / AH", "AH + A⁻", "AH × A⁻"], 'reponse_correcte': '0', 'explication': "On note le couple acide/base $AH/A^-$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Dans le couple $CH_3COOH / CH_3COO^-$, l'acide est :", 'options': ["CH₃COOH", "CH₃COO⁻", "H⁺", "H₂O"], 'reponse_correcte': '0', 'explication': "$CH_3COOH$ est l'acide (il cède $H^+$).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Une réaction acido-basique correspond à :", 'options': ["Un transfert de proton", "Un transfert d'électron", "Un changement d'état", "Une dissolution"], 'reponse_correcte': '0', 'explication': "C'est un transfert de proton $H^+$ entre un acide et une base.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Quel est le couple acide/base de l'eau agissant comme acide ?", 'options': ["H₂O / OH⁻", "H₃O⁺ / H₂O", "OH⁻ / H₂O", "H₂O / H₃O⁺"], 'reponse_correcte': '0', 'explication': "L'eau cède un proton : $H_2O \\to OH^- + H^+$, couple $H_2O/OH^-$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "L'ion $NH_4^+$ est :", 'options': ["Un acide", "Une base", "Neutre", "Un oxydant"], 'reponse_correcte': '0', 'explication': "$NH_4^+$ peut céder un proton ($NH_4^+ \\to NH_3 + H^+$), c'est un acide.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "L'ammoniac $NH_3$ est :", 'options': ["Une base", "Un acide", "Neutre", "Un réducteur"], 'reponse_correcte': '0', 'explication': "$NH_3$ capte un proton ($NH_3 + H^+ \\to NH_4^+$), c'est une base.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Quel couple acide/base fait intervenir l'acide éthanoïque ?", 'options': ["CH₃COOH / CH₃COO⁻", "C₂H₅OH / C₂H₅O⁻", "HCl / Cl⁻", "H₂SO₄ / HSO₄⁻"], 'reponse_correcte': '0', 'explication': "L'acide éthanoïque a pour couple $CH_3COOH/CH_3COO^-$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "L'eau est une espèce :", 'options': ["Amphotère (amphiprotique)", "Toujours acide", "Toujours basique", "Ni acide ni basique"], 'reponse_correcte': '0', 'explication': "L'eau peut céder ou capter un proton, elle est amphotère.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "La demi-équation acido-basique de l'acide chlorhydrique est :", 'options': ["HCl → H⁺ + Cl⁻", "HCl + H⁺ → H₂Cl⁺", "Cl⁻ → HCl + e⁻", "HCl + OH⁻ → Cl⁻"], 'reponse_correcte': '0', 'explication': "$HCl \\to H^+ + Cl^-$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Dans la réaction $NH_3 + H_2O \\to NH_4^+ + OH^-$, $H_2O$ joue le rôle de :", 'options': ["Acide", "Base", "Solvant uniquement", "Oxydant"], 'reponse_correcte': '0', 'explication': "L'eau cède un proton à $NH_3$, elle agit comme acide.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Le couple $H_3O^+ / H_2O$ met en jeu :", 'options': ["L'ion oxonium comme acide", "L'eau comme acide", "L'ion hydroxyde comme base", "L'ion oxonium comme base"], 'reponse_correcte': '0', 'explication': "$H_3O^+$ est l'acide du couple $H_3O^+/H_2O$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "La base conjuguée de $H_2SO_4$ est :", 'options': ["HSO₄⁻", "SO₄²⁻", "H₃SO₄⁺", "H₂O"], 'reponse_correcte': '0', 'explication': "$H_2SO_4 \\to H^+ + HSO_4^-$, donc $HSO_4^-$ est la base conjuguée.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Un couple acide/base met toujours en jeu un transfert de proton.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'vrai', 'explication': "C'est la définition de Brønsted : transfert de $H^+$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "L'eau ne peut jamais jouer le rôle d'acide.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "L'eau est amphotère : elle peut être acide ou base.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "L'ion hydroxyde $OH^-$ est la base conjuguée de $H_2O$.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'vrai', 'explication': "Couple $H_2O/OH^-$ : l'eau cède $H^+$ pour donner $OH^-$.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Écrire la demi-équation acido-basique du couple $CH_3COOH / CH_3COO^-$.", 'options': None, 'reponse_correcte': 'CH3COOH = CH3COO- + H+', 'tolerances': ['CH3COOH -> CH3COO- + H+', 'CH₃COOH → CH₃COO⁻ + H⁺', 'CH3COOH = H+ + CH3COO-'], 'explication': "$CH_3COOH \\rightleftharpoons CH_3COO^- + H^+$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Quelle est la base conjuguée de l'acide nitrique $HNO_3$ ?", 'options': None, 'reponse_correcte': 'NO3-', 'tolerances': ['NO₃⁻', 'ion nitrate', 'nitrate'], 'explication': "$HNO_3 \\to H^+ + NO_3^-$, la base conjuguée est $NO_3^-$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Donner la définition d'une espèce amphotère (amphiprotique).", 'options': None, 'reponse_correcte': "Espèce pouvant être acide ou base", 'tolerances': ["espèce qui peut céder ou capter un proton", "ampholyte", "peut jouer le rôle d'acide ou de base"], 'explication': "Une espèce amphotère peut céder ou capter un proton selon la réaction.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'pH, force des acides et bases',
                'duree': 30,
                'contenu': """# pH, force des acides et bases

## Définition du pH

Le **pH** mesure l’acidité d’une solution :
$$
pH = -\log_{10}[H_3O^+]
$$

- $pH < 7$ : solution acide
- $pH = 7$ : solution neutre
- $pH > 7$ : solution basique

## Force des acides et bases

- **Acide fort** : totalement dissocié en solution ($HCl$, $HNO_3$)
- **Acide faible** : partiellement dissocié ($CH_3COOH$)
- **Base forte** : totalement dissociée ($NaOH$)
- **Base faible** : partiellement dissociée ($NH_3$)

## Calcul de $[H_3O^+]$ et $[OH^-]$

Dans l’eau pure à 25°C :
$$
[H_3O^+] = [OH^-] = 1,0 \times 10^{-7}\ \text{mol/L}
$$

---
""",
                'quiz': {
                    'titre': 'Quiz — pH, force des acides et bases',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Un pH inférieur à 7 correspond à une solution :", 'options': ["Acide", "Basique", "Neutre", "Saturée"], 'reponse_correcte': '0', 'explication': "$pH < 7$ : solution acide.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Un pH égal à 7 correspond à une solution :", 'options': ["Neutre", "Acide", "Basique", "Concentrée"], 'reponse_correcte': '0', 'explication': "$pH = 7$ : solution neutre.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Un pH supérieur à 7 correspond à une solution :", 'options': ["Basique", "Acide", "Neutre", "Diluée"], 'reponse_correcte': '0', 'explication': "$pH > 7$ : solution basique.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "L'acide chlorhydrique ($HCl$) est un acide :", 'options': ["Fort", "Faible", "Amphotère", "Neutre"], 'reponse_correcte': '0', 'explication': "$HCl$ est totalement dissocié en solution, c'est un acide fort.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "L'acide éthanoïque ($CH_3COOH$) est un acide :", 'options': ["Faible", "Fort", "Neutre", "Amphotère"], 'reponse_correcte': '0', 'explication': "$CH_3COOH$ est partiellement dissocié, c'est un acide faible.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "La soude ($NaOH$) est une base :", 'options': ["Forte", "Faible", "Neutre", "Acide"], 'reponse_correcte': '0', 'explication': "$NaOH$ est totalement dissociée : base forte.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "La formule du pH est :", 'options': ["pH = -log[H₃O⁺]", "pH = log[H₃O⁺]", "pH = -log[OH⁻]", "pH = [H₃O⁺]"], 'reponse_correcte': '0', 'explication': "$pH = -\\log_{10}[H_3O^+]$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Dans l'eau pure à 25 °C, $[H_3O^+]$ vaut :", 'options': ["1,0 × 10⁻⁷ mol/L", "1,0 × 10⁻¹⁴ mol/L", "7,0 mol/L", "1,0 mol/L"], 'reponse_correcte': '0', 'explication': "Dans l'eau pure à 25 °C, $[H_3O^+] = 10^{-7}$ mol/L.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Une solution a un pH de 3. La concentration en $H_3O^+$ est :", 'options': ["10⁻³ mol/L", "10⁻⁷ mol/L", "3 mol/L", "10³ mol/L"], 'reponse_correcte': '0', 'explication': "$[H_3O^+] = 10^{-pH} = 10^{-3}$ mol/L.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Le pH d'une solution de $HCl$ à $10^{-2}$ mol/L est :", 'options': ["2", "12", "7", "0,01"], 'reponse_correcte': '0', 'explication': "$HCl$ acide fort : $[H_3O^+] = 10^{-2}$, donc $pH = 2$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "L'ammoniac ($NH_3$) est une base :", 'options': ["Faible", "Forte", "Neutre", "Acide"], 'reponse_correcte': '0', 'explication': "$NH_3$ est partiellement dissocié : base faible.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Le produit ionique de l'eau à 25 °C vaut :", 'options': ["10⁻¹⁴", "10⁻⁷", "10⁷", "1"], 'reponse_correcte': '0', 'explication': "$K_e = [H_3O^+][OH^-] = 10^{-14}$ à 25 °C.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Si $[OH^-] = 10^{-3}$ mol/L à 25 °C, le pH vaut :", 'options': ["11", "3", "7", "14"], 'reponse_correcte': '0', 'explication': "$[H_3O^+] = K_e / [OH^-] = 10^{-14}/10^{-3} = 10^{-11}$, $pH = 11$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Un acide fort de concentration $C$ donne un pH :", 'options': ["pH = -log C", "pH = log C", "pH = 14 + log C", "pH = 7"], 'reponse_correcte': '0', 'explication': "Pour un acide fort : $[H_3O^+] = C$, donc $pH = -\\log C$.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Plus le pH est bas, plus la solution est acide.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'vrai', 'explication': "Un pH bas signifie une concentration élevée en $H_3O^+$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Un acide faible est totalement dissocié en solution.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "Un acide faible n'est que partiellement dissocié.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Le pH d'une solution de NaOH à 0,01 mol/L est 12.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'vrai', 'explication': "$[OH^-] = 0{,}01$ ; $pOH = 2$ ; $pH = 14 - 2 = 12$.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Calculer le pH d'une solution d'acide chlorhydrique à $5{,}0 \\times 10^{-3}$ mol/L.", 'options': None, 'reponse_correcte': '2,3', 'tolerances': ['2.3', 'pH = 2,3', 'pH = 2.3'], 'explication': "$pH = -\\log(5{,}0 \\times 10^{-3}) \\approx 2{,}3$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Donner la relation entre $[H_3O^+]$ et le pH.", 'options': None, 'reponse_correcte': '[H3O+] = 10^(-pH)', 'tolerances': ['[H3O+]=10^-pH', 'H3O+ = 10 puissance -pH', 'concentration = 10^(-pH)'], 'explication': "$[H_3O^+] = 10^{-pH}$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Comment distingue-t-on expérimentalement un acide fort d'un acide faible de même concentration ?", 'options': None, 'reponse_correcte': "Le pH de l'acide fort est plus bas", 'tolerances': ["pH plus faible pour l'acide fort", "acide fort a un pH inférieur", "mesure du pH"], 'explication': "À même concentration, un acide fort a un pH plus bas qu'un acide faible car il est totalement dissocié.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 5 — Énergie et transformations chimiques
    # ──────────────────────────────────────────────
    {
        'ordre': 5,
        'titre': 'Énergie et transformations chimiques',
        'description': "Comprendre les échanges d'énergie lors des réactions chimiques, calculer l'enthalpie et interpréter les bilans énergétiques.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Énergie de liaison et enthalpie de réaction",
                'duree': 35,
                'contenu': """# Énergie de liaison et enthalpie de réaction\n\n## Énergie de liaison\n\nL'**énergie de liaison** ($E_l$) est l'énergie nécessaire pour rompre une liaison covalente entre deux atomes (exprimée en kJ·mol$^{-1}$).\n\n- Plus la liaison est forte, plus $E_l$ est élevée.\n- Pour rompre toutes les liaisons d'une mole de molécules, il faut fournir $E_l$ pour chaque liaison.\n\n## Enthalpie de réaction\n\nL'**enthalpie de réaction** ($\Delta H$) mesure l'échange d'énergie thermique à pression constante lors d'une réaction chimique :\n$$\n\Delta H = \sum E_l(\text{liaisons rompues}) - \sum E_l(\text{liaisons formées})\n$$\n\n- $\Delta H < 0$ : réaction **exothermique** (dégage de la chaleur)\n- $\Delta H > 0$ : réaction **endothermique** (absorbe de la chaleur)\n\n## Loi de Hess\n\nL'enthalpie globale d'une transformation est la somme des enthalpies des étapes élémentaires.\n\n---\n""",
                'quiz': {
                    'titre': "Quiz — Énergie de liaison et enthalpie de réaction",
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "L'énergie de liaison correspond à :", 'options': ["L'énergie pour rompre une liaison", "L'énergie pour former une liaison", "L'énergie cinétique des atomes", "L'énergie potentielle du noyau"], 'reponse_correcte': '0', 'explication': "C'est l'énergie nécessaire pour rompre une liaison covalente.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "L'unité de l'énergie de liaison est :", 'options': ["kJ/mol", "mol/L", "J", "g/mol"], 'reponse_correcte': '0', 'explication': "L'énergie de liaison s'exprime en kJ·mol$^{-1}$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Une réaction exothermique a un $\\Delta H$ :", 'options': ["Négatif", "Positif", "Nul", "Infini"], 'reponse_correcte': '0', 'explication': "$\\Delta H < 0$ : la réaction libère de l'énergie.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Une réaction endothermique :", 'options': ["Absorbe de la chaleur", "Dégage de la chaleur", "Ne produit pas d'énergie", "Est toujours spontanée"], 'reponse_correcte': '0', 'explication': "Endothermique = absorbe de l'énergie thermique.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Plus une liaison est forte :", 'options': ["Plus son énergie de liaison est élevée", "Plus elle se rompt facilement", "Plus la molécule est instable", "Moins la réaction est exothermique"], 'reponse_correcte': '0', 'explication': "Liaison forte = énergie de liaison élevée.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "La loi de Hess stipule que :", 'options': ["L'enthalpie globale = somme des enthalpies des étapes", "L'énergie se crée", "La masse varie", "La température est constante"], 'reponse_correcte': '0', 'explication': "La loi de Hess : $\\Delta H$ global = somme des $\\Delta H$ intermédiaires.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Pour calculer $\\Delta H$, on fait :", 'options': ["Σ E(liaisons rompues) − Σ E(liaisons formées)", "Σ E(liaisons formées) − Σ E(liaisons rompues)", "Σ E(liaisons rompues) + Σ E(liaisons formées)", "Σ E(liaisons rompues) × Σ E(liaisons formées)"], 'reponse_correcte': '0', 'explication': "$\\Delta H = \\sum E_l(\\text{rompues}) - \\sum E_l(\\text{formées})$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Si $\\Delta H > 0$, la réaction est :", 'options': ["Endothermique", "Exothermique", "Athermique", "Impossible"], 'reponse_correcte': '0', 'explication': "$\\Delta H > 0$ signifie que la réaction absorbe de l'énergie.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "L'énergie de la liaison $O=O$ est 498 kJ/mol et celle de $O-H$ est 463 kJ/mol. Pour rompre toutes les liaisons de $H_2O$ :", 'options': ["Il faut 2 × 463 = 926 kJ/mol", "Il faut 463 kJ/mol", "Il faut 498 kJ/mol", "Il faut 926 + 498 kJ/mol"], 'reponse_correcte': '0', 'explication': "$H_2O$ a 2 liaisons $O-H$ : $2 \\times 463 = 926$ kJ/mol.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Si les liaisons formées sont plus fortes que celles rompues, la réaction est :", 'options': ["Exothermique", "Endothermique", "Neutre", "Impossible à déterminer"], 'reponse_correcte': '0', 'explication': "Plus d'énergie libérée (formation) que consommée (rupture) → exothermique.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "L'énergie de liaison $C-H$ (413 kJ/mol) est comparée à $C=O$ (799 kJ/mol). La liaison la plus forte est :", 'options': ["C=O", "C-H", "Elles sont égales", "On ne peut pas comparer"], 'reponse_correcte': '0', 'explication': "799 > 413, la liaison $C=O$ est plus forte.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "La loi de Hess permet de :", 'options': ["Calculer ΔH d'une réaction à partir d'étapes intermédiaires", "Mesurer la température d'une réaction", "Déterminer la masse molaire", "Calculer la concentration"], 'reponse_correcte': '0', 'explication': "La loi de Hess relie les enthalpies des étapes successives.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Rompre une liaison chimique nécessite :", 'options': ["Un apport d'énergie", "Une libération d'énergie", "Aucune énergie", "Une diminution de température"], 'reponse_correcte': '0', 'explication': "La rupture de liaison est toujours endothermique.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Former une liaison chimique :", 'options': ["Libère de l'énergie", "Nécessite de l'énergie", "N'échange pas d'énergie", "Absorbe toujours plus qu'elle ne libère"], 'reponse_correcte': '0', 'explication': "La formation de liaison est exothermique.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "La rupture d'une liaison est un processus exothermique.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "La rupture de liaison est endothermique (il faut fournir de l'énergie).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Si $\\Delta H < 0$, la réaction libère de la chaleur.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'vrai', 'explication': "$\\Delta H < 0$ correspond à une réaction exothermique.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "La loi de Hess ne s'applique qu'aux réactions en solution.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "La loi de Hess est valable pour tout type de réaction.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "On rompt 4 liaisons C-H (413 kJ/mol chacune) et 2 liaisons O=O (498 kJ/mol chacune). Calculer l'énergie totale nécessaire en kJ/mol.", 'options': None, 'reponse_correcte': '2648 kJ/mol', 'tolerances': ['2648', '2 648 kJ/mol', '2648 kJ'], 'explication': "$4 \\times 413 + 2 \\times 498 = 1652 + 996 = 2648$ kJ/mol.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Donner la formule de l'enthalpie de réaction en fonction des énergies de liaison.", 'options': None, 'reponse_correcte': 'ΔH = Σ E(rompues) - Σ E(formées)', 'tolerances': ['delta H = somme E rompues - somme E formees', 'ΔrH = ΣEl(rompues) - ΣEl(formées)', 'DeltaH = E rompues - E formees'], 'explication': "$\\Delta H = \\sum E_l(\\text{rompues}) - \\sum E_l(\\text{formées})$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Comment qualifie-t-on une réaction dont $\\Delta H > 0$ ?", 'options': None, 'reponse_correcte': 'endothermique', 'tolerances': ['réaction endothermique', 'endo-thermique', 'endo thermique'], 'explication': "$\\Delta H > 0$ : réaction endothermique (absorbe de la chaleur).", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': "Combustion et bilans énergétiques",
                'duree': 35,
                'contenu': """# Combustion et bilans énergétiques\n\n## Réaction de combustion\n\nLa **combustion** est une réaction chimique entre un combustible et le dioxygène ($O_2$), produisant de l'énergie thermique.\n\n**Exemples :**\n- $C + O_2 \to CO_2$\n- $CH_4 + 2O_2 \to CO_2 + 2H_2O$\n\n## Pouvoir calorifique\n\nLe **pouvoir calorifique inférieur** ($PCI$) est l'énergie libérée par la combustion complète d'une unité de masse ou de volume d'un combustible.\n\n## Bilan énergétique\n\nLe bilan énergétique global d'une réaction tient compte de toutes les énergies absorbées et libérées.\n\n- Conversion entre kJ/mol, kJ/g, kJ/L selon la nature du combustible.\n- Application de la loi de Hess pour des réactions en plusieurs étapes.\n\n---\n""",
                'quiz': {
                    'titre': "Quiz — Combustion et bilans énergétiques",
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Une combustion met en jeu un combustible et :", 'options': ["Le dioxygène", "Le diazote", "Le dioxyde de carbone", "L'eau"], 'reponse_correcte': '0', 'explication': "La combustion est une réaction avec $O_2$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Le produit de la combustion complète du carbone est :", 'options': ["CO₂", "CO", "C₂O", "H₂O"], 'reponse_correcte': '0', 'explication': "$C + O_2 \\to CO_2$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "La combustion complète du méthane produit :", 'options': ["CO₂ et H₂O", "CO et H₂O", "CO₂ et H₂", "C et H₂O"], 'reponse_correcte': '0', 'explication': "$CH_4 + 2O_2 \\to CO_2 + 2H_2O$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Une combustion est une réaction :", 'options': ["Exothermique", "Endothermique", "Athermique", "Réversible"], 'reponse_correcte': '0', 'explication': "Les combustions dégagent de la chaleur.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Le pouvoir calorifique mesure :", 'options': ["L'énergie libérée par unité de masse de combustible", "La masse du combustible", "La température de flamme", "Le volume de gaz produit"], 'reponse_correcte': '0', 'explication': "Le PCI est l'énergie libérée par combustion complète d'une unité de masse.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Quel gaz est nécessaire pour qu'une combustion ait lieu ?", 'options': ["O₂", "N₂", "CO₂", "H₂"], 'reponse_correcte': '0', 'explication': "Le dioxygène est le comburant.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Le bilan énergétique tient compte de :", 'options': ["Toutes les énergies absorbées et libérées", "Seulement l'énergie absorbée", "Seulement l'énergie libérée", "La masse des produits"], 'reponse_correcte': '0', 'explication': "Le bilan global inclut toutes les contributions énergétiques.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "La combustion incomplète peut produire :", 'options': ["Du monoxyde de carbone (CO)", "Uniquement du CO₂", "De l'azote", "De l'hydrogène"], 'reponse_correcte': '0', 'explication': "Une combustion incomplète (manque de $O_2$) peut former du $CO$ toxique.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "La combustion de l'éthanol $C_2H_6O$ produit :", 'options': ["2 CO₂ + 3 H₂O", "CO₂ + H₂O", "2 CO + 3 H₂O", "CO₂ + 2 H₂O"], 'reponse_correcte': '0', 'explication': "$C_2H_6O + 3O_2 \\to 2CO_2 + 3H_2O$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Le pouvoir calorifique du méthane (890 kJ/mol, $M = 16$ g/mol) en kJ/g vaut environ :", 'options': ["55,6 kJ/g", "890 kJ/g", "16 kJ/g", "445 kJ/g"], 'reponse_correcte': '0', 'explication': "$890 / 16 \\approx 55{,}6$ kJ/g.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Combien de moles de $O_2$ faut-il pour la combustion complète de 1 mol de $CH_4$ ?", 'options': ["2 mol", "1 mol", "3 mol", "4 mol"], 'reponse_correcte': '0', 'explication': "$CH_4 + 2O_2 \\to CO_2 + 2H_2O$ : 2 mol de $O_2$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Pourquoi le monoxyde de carbone est-il dangereux ?", 'options': ["Il se fixe sur l'hémoglobine à la place de O₂", "Il est explosif", "Il sent mauvais", "Il est acide"], 'reponse_correcte': '0', 'explication': "Le $CO$ se fixe sur l'hémoglobine, empêchant le transport de $O_2$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Pour convertir le PCI de kJ/mol en kJ/g, on :", 'options': ["Divise par la masse molaire", "Multiplie par la masse molaire", "Divise par le volume molaire", "Multiplie par NA"], 'reponse_correcte': '0', 'explication': "PCI (kJ/g) = PCI (kJ/mol) / $M$ (g/mol).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "La loi de Hess permet de calculer $\\Delta H$ d'une combustion :", 'options': ["À partir d'enthalpies de formation tabulées", "Uniquement par expérience", "Seulement pour les gaz", "Seulement à haute température"], 'reponse_correcte': '0', 'explication': "La loi de Hess permet de combiner des données thermodynamiques tabulées.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Toute combustion est exothermique.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'vrai', 'explication': "Les combustions libèrent toujours de l'énergie.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "La combustion incomplète ne produit que du $CO_2$.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "La combustion incomplète peut former du $CO$ ou du carbone (suie).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Le pouvoir calorifique est toujours exprimé en kJ/mol.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "Il peut être exprimé en kJ/mol, kJ/g ou kJ/L.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Écrire l'équation de combustion complète du propane $C_3H_8$.", 'options': None, 'reponse_correcte': 'C3H8 + 5O2 -> 3CO2 + 4H2O', 'tolerances': ['C3H8 + 5 O2 → 3 CO2 + 4 H2O', 'C3H8 + 5O2 = 3CO2 + 4H2O', 'C₃H₈ + 5O₂ → 3CO₂ + 4H₂O'], 'explication': "$C_3H_8 + 5O_2 \\to 3CO_2 + 4H_2O$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Le PCI du méthane est 890 kJ/mol. Quelle énergie libère la combustion de 3,0 mol de méthane ?", 'options': None, 'reponse_correcte': '2670 kJ', 'tolerances': ['2670', '2 670 kJ', '2670 kJ/mol'], 'explication': "$3{,}0 \\times 890 = 2670$ kJ.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Quel est le comburant dans une réaction de combustion ?", 'options': None, 'reponse_correcte': 'dioxygène', 'tolerances': ['O2', 'le dioxygène', 'oxygène'], 'explication': "Le comburant est le dioxygène $O_2$.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 6 — Chimie organique : nomenclature et groupes caractéristiques
    # ──────────────────────────────────────────────
    {
        'ordre': 6,
        'titre': 'Chimie organique : nomenclature et groupes caractéristiques',
        'description': "Identifier les groupes caractéristiques, nommer les molécules organiques et reconnaître les principales familles.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Groupes caractéristiques et familles organiques",
                'duree': 35,
                'contenu': """# Groupes caractéristiques et familles organiques\n\n## Chimie organique\n\nLa **chimie organique** étudie les composés du carbone (hors $CO_2$, $CO$, carbonates).\n\n## Squelette carboné\n\n- Chaîne linéaire, ramifiée ou cyclique\n- Atomes d'hydrogène, d'oxygène, d'azote, d'halogènes\n\n## Groupes caractéristiques\n\n- **Alcool** : $-OH$ (hydroxyle)\n- **Aldéhyde** : $-CHO$ (carbonyle terminal)\n- **Cétone** : $>C=O$ (carbonyle interne)\n- **Acide carboxylique** : $-COOH$\n- **Ester** : $-COO-$\n- **Amine** : $-NH_2$\n- **Amide** : $-CONH_2$\n\n## Familles\n\n- Alcools, aldéhydes, cétones, acides carboxyliques, esters, amines, amides\n\n---\n""",
                'quiz': {
                    'titre': "Quiz — Groupes caractéristiques et familles organiques",
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Le groupe caractéristique $-OH$ correspond à la famille des :", 'options': ["Alcools", "Aldéhydes", "Cétones", "Acides carboxyliques"], 'reponse_correcte': '0', 'explication': "Le groupe hydroxyle $-OH$ caractérise les alcools.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Le groupe $-COOH$ correspond à la famille des :", 'options': ["Acides carboxyliques", "Alcools", "Esters", "Amines"], 'reponse_correcte': '0', 'explication': "Le groupe carboxyle $-COOH$ caractérise les acides carboxyliques.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Le groupe $-CHO$ correspond à la famille des :", 'options': ["Aldéhydes", "Cétones", "Alcools", "Esters"], 'reponse_correcte': '0', 'explication': "Le groupe carbonyle terminal $-CHO$ caractérise les aldéhydes.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "La chimie organique étudie les composés du :", 'options': ["Carbone", "Fer", "Sodium", "Oxygène"], 'reponse_correcte': '0', 'explication': "La chimie organique étudie les composés du carbone.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Le groupe $>C=O$ (carbonyle interne) correspond à la famille des :", 'options': ["Cétones", "Aldéhydes", "Alcools", "Amides"], 'reponse_correcte': '0', 'explication': "Le carbonyle interne caractérise les cétones.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Le groupe $-NH_2$ correspond à la famille des :", 'options': ["Amines", "Amides", "Alcools", "Aldéhydes"], 'reponse_correcte': '0', 'explication': "Le groupe amino $-NH_2$ caractérise les amines.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Le groupe $-COO-$ correspond à la famille des :", 'options': ["Esters", "Acides carboxyliques", "Amides", "Cétones"], 'reponse_correcte': '0', 'explication': "Le groupe ester $-COO-$ caractérise les esters.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Le squelette carboné peut être :", 'options': ["Linéaire, ramifié ou cyclique", "Uniquement linéaire", "Uniquement cyclique", "Toujours ramifié"], 'reponse_correcte': '0', 'explication': "Le squelette carboné admet trois types de chaînes.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "L'éthanol ($CH_3CH_2OH$) appartient à la famille des :", 'options': ["Alcools", "Aldéhydes", "Acides carboxyliques", "Esters"], 'reponse_correcte': '0', 'explication': "La présence du groupe $-OH$ en fait un alcool.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "L'acide éthanoïque ($CH_3COOH$) possède le groupe :", 'options': ["-COOH", "-OH", "-CHO", "-COO-"], 'reponse_correcte': '0', 'explication': "L'acide éthanoïque possède le groupe carboxyle $-COOH$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "La propanone ($CH_3COCH_3$) est :", 'options': ["Une cétone", "Un aldéhyde", "Un alcool", "Un ester"], 'reponse_correcte': '0', 'explication': "La propanone possède un groupe carbonyle interne : c'est une cétone.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Le méthanal ($HCHO$) est :", 'options': ["Un aldéhyde", "Une cétone", "Un alcool", "Un acide carboxylique"], 'reponse_correcte': '0', 'explication': "Le méthanal possède le groupe $-CHO$ : c'est un aldéhyde.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Le groupe $-CONH_2$ caractérise la famille des :", 'options': ["Amides", "Amines", "Esters", "Aldéhydes"], 'reponse_correcte': '0', 'explication': "Le groupe amide $-CONH_2$ caractérise les amides.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Parmi ces composés, lequel est un ester ?", 'options': ["CH₃COOCH₃", "CH₃COOH", "CH₃CHO", "CH₃OH"], 'reponse_correcte': '0', 'explication': "$CH_3COOCH_3$ contient le groupe $-COO-$ : c'est un ester.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Le $CO_2$ est un composé organique.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "$CO_2$ est exclu de la chimie organique.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Un alcool contient obligatoirement le groupe $-OH$.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'vrai', 'explication': "Le groupe hydroxyle $-OH$ est le groupe caractéristique des alcools.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Les aldéhydes et les cétones possèdent le même groupe fonctionnel.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "L'aldéhyde a un carbonyle terminal ($-CHO$), la cétone un carbonyle interne ($>C=O$).", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Quel est le groupe caractéristique de la famille des acides carboxyliques ?", 'options': None, 'reponse_correcte': '-COOH', 'tolerances': ['COOH', 'groupe carboxyle', 'carboxyle'], 'explication': "Le groupe carboxyle $-COOH$ caractérise les acides carboxyliques.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "À quelle famille appartient une molécule possédant le groupe $-CHO$ ?", 'options': None, 'reponse_correcte': 'aldéhyde', 'tolerances': ['aldéhydes', 'les aldéhydes', 'famille des aldéhydes'], 'explication': "Le groupe $-CHO$ (carbonyle terminal) caractérise les aldéhydes.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Citer trois familles de composés organiques oxygénés.", 'options': None, 'reponse_correcte': 'alcools, aldéhydes, cétones', 'tolerances': ['alcool aldéhyde cétone', 'alcools aldéhydes acides carboxyliques', 'alcools cétones esters'], 'explication': "Exemples : alcools, aldéhydes, cétones, acides carboxyliques, esters.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': "Nomenclature des molécules organiques",
                'duree': 35,
                'contenu': """# Nomenclature des molécules organiques\n\n## Règles générales\n\n- Préfixe selon le nombre de carbones : méth-, éth-, prop-, but-, pent-, hex-, hept-, oct-, non-, déc-\n- Suffixe selon le groupe caractéristique :\n    - Alcane : -ane\n    - Alcool : -ol\n    - Aldéhyde : -al\n    - Cétone : -one\n    - Acide carboxylique : acide ...-oïque\n    - Ester : ...-oate d'alkyle\n    - Amine : -amine\n    - Amide : -amide\n\n## Exemples\n\n- $CH_3CH_2OH$ : éthanol\n- $CH_3COOH$ : acide éthanoïque\n- $CH_3COOCH_3$ : méthanoate de méthyle\n- $CH_3CH_2NH_2$ : éthylamine\n\n## Isomérie\n\n- **Isomérie de chaîne** : ramification différente\n- **Isomérie de position** : groupe caractéristique à un endroit différent\n- **Isomérie de fonction** : groupes caractéristiques différents\n\n---\n""",
                'quiz': {
                    'titre': "Quiz — Nomenclature des molécules organiques",
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Le préfixe « méth- » correspond à :", 'options': ["1 carbone", "2 carbones", "3 carbones", "4 carbones"], 'reponse_correcte': '0', 'explication': "Méth- = 1 atome de carbone.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Le suffixe « -ol » correspond à la famille des :", 'options': ["Alcools", "Alcanes", "Aldéhydes", "Cétones"], 'reponse_correcte': '0', 'explication': "Le suffixe -ol caractérise les alcools.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Le préfixe « éth- » correspond à :", 'options': ["2 carbones", "1 carbone", "3 carbones", "4 carbones"], 'reponse_correcte': '0', 'explication': "Éth- = 2 atomes de carbone.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Le suffixe « -al » correspond à la famille des :", 'options': ["Aldéhydes", "Alcools", "Alcanes", "Esters"], 'reponse_correcte': '0', 'explication': "Le suffixe -al caractérise les aldéhydes.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Le nom IUPAC de $CH_3CH_2OH$ est :", 'options': ["Éthanol", "Méthanol", "Propanol", "Butanol"], 'reponse_correcte': '0', 'explication': "2 carbones (éth-) + alcool (-ol) = éthanol.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Le préfixe « prop- » correspond à :", 'options': ["3 carbones", "2 carbones", "4 carbones", "5 carbones"], 'reponse_correcte': '0', 'explication': "Prop- = 3 atomes de carbone.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Le suffixe « -one » correspond à la famille des :", 'options': ["Cétones", "Alcools", "Aldéhydes", "Amines"], 'reponse_correcte': '0', 'explication': "Le suffixe -one caractérise les cétones.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Le préfixe « but- » correspond à :", 'options': ["4 carbones", "3 carbones", "5 carbones", "6 carbones"], 'reponse_correcte': '0', 'explication': "But- = 4 atomes de carbone.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Le nom IUPAC de $CH_3COOH$ est :", 'options': ["Acide éthanoïque", "Acide méthanoïque", "Acide propanoïque", "Éthanol"], 'reponse_correcte': '0', 'explication': "2 carbones + acide carboxylique = acide éthanoïque.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "L'isomérie de chaîne correspond à :", 'options': ["Des ramifications différentes du squelette carboné", "Un groupe fonctionnel à une position différente", "Des groupes fonctionnels différents", "Des formules brutes différentes"], 'reponse_correcte': '0', 'explication': "Les isomères de chaîne diffèrent par la ramification.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Le butan-1-ol et le butan-2-ol sont des isomères de :", 'options': ["Position", "Chaîne", "Fonction", "Configuration"], 'reponse_correcte': '0', 'explication': "Le groupe $-OH$ est à des positions différentes : isomères de position.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Le propanal et la propanone sont des isomères de :", 'options': ["Fonction", "Position", "Chaîne", "Stéréoisomérie"], 'reponse_correcte': '0', 'explication': "Aldéhyde vs cétone : groupes fonctionnels différents, même formule brute.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Le nom IUPAC de $CH_3CH_2NH_2$ est :", 'options': ["Éthylamine", "Méthylamine", "Propylamine", "Éthanamide"], 'reponse_correcte': '0', 'explication': "2 carbones + amine = éthylamine.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Le suffixe « acide ...-oïque » caractérise :", 'options': ["Les acides carboxyliques", "Les esters", "Les amides", "Les alcools"], 'reponse_correcte': '0', 'explication': "Acide ...-oïque = acide carboxylique.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Deux isomères ont toujours la même formule brute.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'vrai', 'explication': "Par définition, les isomères ont la même formule brute mais des structures différentes.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Le préfixe « pent- » correspond à 6 carbones.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "Pent- = 5 carbones ; hex- = 6 carbones.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Le méthanol et l'éthanol sont des isomères.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "Ils n'ont pas la même formule brute ($CH_4O$ vs $C_2H_6O$).", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Donner le nom IUPAC de $CH_3CH_2CH_2OH$.", 'options': None, 'reponse_correcte': 'propan-1-ol', 'tolerances': ['propanol', '1-propanol', 'propan-1-ol'], 'explication': "3 carbones (prop-) + alcool en position 1 = propan-1-ol.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Quel est le suffixe IUPAC d'un acide carboxylique ?", 'options': None, 'reponse_correcte': '-oïque', 'tolerances': ['oïque', 'acide -oïque', 'acide ...oïque'], 'explication': "Les acides carboxyliques ont le suffixe « acide ...-oïque ».", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Donner le nom IUPAC de la cétone à 3 carbones.", 'options': None, 'reponse_correcte': 'propanone', 'tolerances': ['propan-2-one', 'acétone', 'la propanone'], 'explication': "3 carbones (prop-) + cétone (-one) = propanone.", 'difficulte': 'difficile', 'points': 2},
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 7 — Réactivité en chimie organique
    # ──────────────────────────────────────────────
    {
        'ordre': 7,
        'titre': 'Réactivité en chimie organique',
        'description': "Comprendre les principales réactions organiques (estérification, hydrolyse), les techniques de synthèse et de purification.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Réactions d’estérification et d’hydrolyse",
                'duree': 35,
                'contenu': """# Réactions d’estérification et d’hydrolyse\n\n## Estérification\n\nRéaction entre un acide carboxylique et un alcool :\n$$\n\text{Acide} + \text{Alcool} \rightleftharpoons \text{Ester} + \text{Eau}\n$$\n\n- Réaction lente, limitée par l'équilibre\n- Catalyse acide ($H^+$)\n- Taux d'estérification à l'équilibre $\approx 67\%$ pour 1 mol d'acide + 1 mol d'alcool\n\n## Hydrolyse\n\nRéaction inverse :\n$$\n\text{Ester} + \text{Eau} \rightleftharpoons \text{Acide} + \text{Alcool}\n$$\n\n- Peut être catalysée par un acide ou une base\n\n## Déplacement de l’équilibre\n\n- Excès d’un réactif\n- Élimination d’un produit\n\n---\n""",
                'quiz': {
                    'titre': "Quiz — Réactions d'estérification et d'hydrolyse",
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "L'estérification est la réaction entre :", 'options': ["Un acide carboxylique et un alcool", "Un alcool et une amine", "Deux acides carboxyliques", "Un ester et un acide"], 'reponse_correcte': '0', 'explication': "L'estérification fait réagir un acide carboxylique avec un alcool.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Quel produit se forme en plus de l'ester lors de l'estérification ?", 'options': ["De l'eau", "Du dioxyde de carbone", "Du dihydrogène", "Un alcool"], 'reponse_correcte': '0', 'explication': "L'estérification produit un ester et de l'eau.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "L'hydrolyse d'un ester produit :", 'options': ["Un acide carboxylique et un alcool", "Deux esters", "Un ester et de l'eau", "Un alcool et du CO₂"], 'reponse_correcte': '0', 'explication': "L'hydrolyse d'un ester régénère l'acide et l'alcool.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "L'estérification est une réaction :", 'options': ["Lente et limitée", "Rapide et totale", "Rapide et limitée", "Instantanée"], 'reponse_correcte': '0', 'explication': "L'estérification est lente et limitée par un équilibre.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Quel catalyseur est utilisé pour accélérer l'estérification ?", 'options': ["L'acide sulfurique (H⁺)", "Le platine", "L'hydroxyde de sodium", "Le permanganate de potassium"], 'reponse_correcte': '0', 'explication': "L'estérification est catalysée par les ions H⁺ (acide sulfurique).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "L'estérification et l'hydrolyse sont des réactions :", 'options': ["Inverses l'une de l'autre", "Identiques", "Irréversibles", "Sans lien"], 'reponse_correcte': '0', 'explication': "L'estérification et l'hydrolyse sont les deux sens de la même réaction réversible.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Le groupe fonctionnel caractéristique d'un ester est :", 'options': ["-COO-", "-COOH", "-OH", "-CO-"], 'reponse_correcte': '0', 'explication': "Le groupe ester est -COO- (liaison C-O-C avec un C=O).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Un catalyseur modifie :", 'options': ["La vitesse de réaction", "L'état d'équilibre", "Le rendement final", "La composition à l'équilibre"], 'reponse_correcte': '0', 'explication': "Un catalyseur accélère la réaction mais ne modifie pas l'équilibre.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Quel est le taux d'avancement à l'équilibre pour un mélange équimolaire acide + alcool ?", 'options': ["Environ 67 %", "100 %", "50 %", "33 %"], 'reponse_correcte': '0', 'explication': "Le taux d'estérification à l'équilibre vaut environ 67 % pour un mélange équimolaire.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Pour déplacer l'équilibre vers la formation de l'ester, on peut :", 'options': ["Ajouter un excès d'alcool", "Ajouter de l'eau", "Diminuer la température", "Retirer de l'alcool"], 'reponse_correcte': '0', 'explication': "Un excès de réactif déplace l'équilibre vers les produits.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "L'hydrolyse basique (saponification) est :", 'options': ["Totale et irréversible", "Limitée et réversible", "Lente et limitée", "Rapide et réversible"], 'reponse_correcte': '0', 'explication': "La saponification (hydrolyse basique) est une réaction totale.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "L'élimination d'un produit du milieu réactionnel permet de :", 'options': ["Déplacer l'équilibre vers les produits", "Ralentir la réaction", "Diminuer le rendement", "Atteindre l'équilibre plus vite sans le modifier"], 'reponse_correcte': '0', 'explication': "Retirer un produit déplace l'équilibre dans le sens de sa formation (loi de Le Chatelier).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Le produit de la réaction entre l'acide éthanoïque et l'éthanol est :", 'options': ["L'éthanoate d'éthyle", "L'éthanol", "L'acide propanoïque", "Le propanoate de méthyle"], 'reponse_correcte': '0', 'explication': "Acide éthanoïque + éthanol → éthanoate d'éthyle + eau.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "La constante d'équilibre K de l'estérification équimolaire vaut environ :", 'options': ["4", "1", "10", "0,25"], 'reponse_correcte': '0', 'explication': "Pour un mélange équimolaire, K ≈ 4 (taux ≈ 67 %).", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Un catalyseur modifie la composition du mélange à l'équilibre.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Un catalyseur accélère l'atteinte de l'équilibre mais ne modifie pas sa composition.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "L'estérification est une réaction totale.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "L'estérification est limitée par l'équilibre, elle n'est pas totale.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "L'hydrolyse d'un ester en milieu acide est une réaction limitée.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "L'hydrolyse acide d'un ester est limitée, comme l'estérification.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Nommer le produit de la réaction entre l'acide méthanoïque et le propan-1-ol.", 'reponse_correcte': "méthanoate de propyle", 'tolerances': ["methanoate de propyle", "formiate de propyle", "ester méthanoate de propyle"], 'explication': "Acide méthanoïque + propan-1-ol → méthanoate de propyle + eau.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Comment appelle-t-on l'hydrolyse d'un ester en milieu basique ?", 'reponse_correcte': "saponification", 'tolerances': ["la saponification", "réaction de saponification"], 'explication': "L'hydrolyse basique d'un ester est la saponification.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Quelle est la formule semi-développée du groupe ester ?", 'reponse_correcte': "-COO-", 'tolerances': ["R-COO-R'", "RCOOR'", "-CO-O-"], 'explication': "Le groupe fonctionnel ester s'écrit -COO- (ou R-COO-R').", 'difficulte': 'difficile', 'points': 2},
                    ]
                },
            },
            {
                'ordre': 2,
                'titre': "Techniques de synthèse et purification",
                'duree': 35,
                'contenu': """# Techniques de synthèse et purification\n\n## Chauffage à reflux\n\nPermet de chauffer un mélange réactionnel sans perte de matière par évaporation.\n\n## Distillation\n\nSéparation des constituants selon leur température d’ébullition.\n\n## Extraction liquide-liquide\n\nUtilise deux solvants non miscibles pour séparer les produits.\n\n## Recristallisation\n\nPurification d’un solide par dissolution à chaud puis cristallisation à froid.\n\n## Lavage\n\nPermet d’éliminer les impuretés (acides, bases, solvants).\n\n## Rendement\n\n$$\nr = \frac{n_{\text{produit expérimental}}}{n_{\text{produit théorique}}} \times 100\%\n$$\n\n---\n""",
                'quiz': {
                    'titre': 'Quiz — Techniques de synthèse et purification',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Le chauffage à reflux permet de :", 'options': ["Chauffer sans perte de matière", "Refroidir le mélange", "Filtrer les impuretés", "Cristalliser un solide"], 'reponse_correcte': '0', 'explication': "Le chauffage à reflux chauffe le mélange tout en condensant les vapeurs.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "La distillation sépare les constituants selon :", 'options': ["Leur température d'ébullition", "Leur couleur", "Leur masse", "Leur taille"], 'reponse_correcte': '0', 'explication': "La distillation utilise les différences de température d'ébullition.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "L'extraction liquide-liquide utilise :", 'options': ["Deux solvants non miscibles", "Un seul solvant", "Un filtre", "Un évaporateur rotatif"], 'reponse_correcte': '0', 'explication': "L'extraction liquide-liquide repose sur deux solvants non miscibles.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "La recristallisation est une technique de :", 'options': ["Purification d'un solide", "Synthèse d'un liquide", "Séparation de gaz", "Mesure de température"], 'reponse_correcte': '0', 'explication': "La recristallisation purifie un solide par dissolution à chaud et cristallisation à froid.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Dans un montage à reflux, le réfrigérant sert à :", 'options': ["Condenser les vapeurs", "Chauffer le mélange", "Filtrer le produit", "Mesurer le volume"], 'reponse_correcte': '0', 'explication': "Le réfrigérant condense les vapeurs pour les renvoyer dans le ballon.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Le rendement d'une synthèse est exprimé en :", 'options': ["Pourcentage", "Moles", "Grammes", "Litres"], 'reponse_correcte': '0', 'explication': "Le rendement est un rapport sans dimension exprimé en pourcentage.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Le lavage d'un produit organique à l'eau permet d'éliminer :", 'options': ["Les impuretés solubles dans l'eau", "Les impuretés insolubles", "Le solvant organique", "Les cristaux"], 'reponse_correcte': '0', 'explication': "Le lavage à l'eau élimine les espèces hydrosolubles (acides, sels).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "L'ampoule à décanter est utilisée pour :", 'options': ["Séparer deux liquides non miscibles", "Chauffer un mélange", "Mesurer un volume précis", "Peser un solide"], 'reponse_correcte': '0', 'explication': "L'ampoule à décanter sépare deux phases liquides non miscibles.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Un rendement de 75 % signifie que :", 'options': ["On a obtenu 75 % du produit théorique", "La réaction dure 75 minutes", "75 % du réactif est en excès", "Il reste 75 % de réactif"], 'reponse_correcte': '0', 'explication': "Le rendement compare la quantité obtenue à la quantité théorique.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Lors d'une extraction, la phase organique se situe :", 'options': ["Au-dessus si sa densité est inférieure à celle de l'eau", "Toujours en dessous", "Toujours au-dessus", "Au milieu"], 'reponse_correcte': '0', 'explication': "La position dépend de la densité relative : moins dense = au-dessus.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Le séchage d'une phase organique sur sulfate de magnésium anhydre élimine :", 'options': ["Les traces d'eau", "Les impuretés organiques", "Le solvant", "Les cristaux"], 'reponse_correcte': '0', 'explication': "Le sulfate de magnésium anhydre absorbe l'eau résiduelle.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "La pierre ponce dans un montage à reflux sert à :", 'options': ["Régulariser l'ébullition", "Catalyser la réaction", "Filtrer les impuretés", "Refroidir le mélange"], 'reponse_correcte': '0', 'explication': "La pierre ponce évite les soubresauts d'ébullition (bumping).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Lors de la recristallisation, on dissout le solide :", 'options': ["À chaud dans un solvant adapté", "À froid dans l'eau", "À température ambiante dans l'éther", "Sous vide"], 'reponse_correcte': '0', 'explication': "On dissout le solide à chaud puis on laisse cristalliser à froid.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "La filtration sous vide (Büchner) est plus rapide car :", 'options': ["La différence de pression accélère le passage du liquide", "Le filtre est plus grand", "Le solvant s'évapore", "Le solide fond"], 'reponse_correcte': '0', 'explication': "La trompe à vide crée une dépression qui accélère la filtration.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Le chauffage à reflux provoque une perte de matière par évaporation.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Le réfrigérant condense les vapeurs, il n'y a pas de perte de matière.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Un rendement supérieur à 100 % est possible en pratique.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Le rendement ne peut pas dépasser 100 % ; une valeur supérieure indiquerait des impuretés ou une erreur.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "L'extraction liquide-liquide nécessite deux solvants miscibles.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Les deux solvants doivent être non miscibles pour former deux phases distinctes.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Comment appelle-t-on la verrerie utilisée pour séparer deux liquides non miscibles ?", 'reponse_correcte': "ampoule à décanter", 'tolerances': ["ampoule a decanter", "ampoule de décantation", "ampoule de decantation"], 'explication': "L'ampoule à décanter permet de séparer deux phases liquides non miscibles.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Quelle est la formule du rendement d'une synthèse ?", 'reponse_correcte': "r = n(exp) / n(théo) × 100", 'tolerances': ["n obtenu / n théorique fois 100", "quantité obtenue sur quantité théorique", "r = n expérimental / n théorique"], 'explication': "Le rendement r = (quantité obtenue / quantité théorique) × 100 %.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Quel agent desséchant courant utilise-t-on pour sécher une phase organique ?", 'reponse_correcte': "sulfate de magnésium anhydre", 'tolerances': ["MgSO4 anhydre", "sulfate de magnésium", "MgSO4"], 'explication': "Le sulfate de magnésium anhydre (MgSO₄) est un desséchant classique en chimie organique.", 'difficulte': 'difficile', 'points': 2},
                    ]
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 8 — Dosages et titrages
    # ──────────────────────────────────────────────
    {
        'ordre': 8,
        'titre': 'Dosages et titrages',
        'description': "Maîtriser les méthodes de dosage par étalonnage et titrage, savoir exploiter une courbe de titrage.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Dosage par étalonnage",
                'duree': 35,
                'contenu': """# Dosage par étalonnage\n\n## Principe\n\nOn mesure une grandeur physique (absorbance, conductivité) pour déterminer la concentration d’une espèce en solution à l’aide d’une courbe d’étalonnage.\n\n## Courbe d’étalonnage\n\n- Préparer des solutions étalons de concentration connue\n- Mesurer la grandeur physique pour chaque étalon\n- Tracer la courbe (ex : absorbance $A$ en fonction de $C$)\n- Utiliser la courbe pour déterminer la concentration inconnue\n\n## Loi de Beer-Lambert\n\n$$\nA = \varepsilon \cdot l \cdot C\n$$\n\n- $A$ : absorbance\n- $\varepsilon$ : coefficient d’extinction molaire\n- $l$ : longueur de la cuve (cm)\n- $C$ : concentration (mol/L)\n\n---\n""",
                'quiz': {
                    'titre': "Quiz — Dosage par étalonnage",
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Quelle grandeur physique mesure-t-on en spectrophotométrie ?", 'options': ["L'absorbance", "La masse", "La température", "La pression"], 'reponse_correcte': '0', 'explication': "Le spectrophotomètre mesure l'absorbance d'une solution.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Que représente une courbe d'étalonnage ?", 'options': ["La relation entre une grandeur mesurée et la concentration", "La variation de température en fonction du temps", "La masse en fonction du volume", "Le pH en fonction du volume versé"], 'reponse_correcte': '0', 'explication': "La courbe d'étalonnage relie la grandeur physique mesurée à la concentration.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Dans la loi de Beer-Lambert, que représente $\\varepsilon$ ?", 'options': ["Le coefficient d'extinction molaire", "La longueur de la cuve", "La concentration", "L'absorbance"], 'reponse_correcte': '0', 'explication': "$\\varepsilon$ est le coefficient d'extinction molaire, caractéristique de l'espèce et de la longueur d'onde.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Quelle est l'unité de la concentration molaire ?", 'options': ["mol/L", "g/L", "mol", "L/mol"], 'reponse_correcte': '0', 'explication': "La concentration molaire s'exprime en mol/L (ou mol·L⁻¹).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "La loi de Beer-Lambert s'écrit :", 'options': ["$A = \\varepsilon \\cdot l \\cdot C$", "$A = m / V$", "$A = C / \\varepsilon$", "$A = l / (\\varepsilon \\cdot C)$"], 'reponse_correcte': '0', 'explication': "La loi de Beer-Lambert relie l'absorbance au produit $\\varepsilon \\cdot l \\cdot C$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Qu'est-ce qu'une solution étalon ?", 'options': ["Une solution de concentration connue", "Une solution incolore", "Une solution saturée", "Une solution de concentration inconnue"], 'reponse_correcte': '0', 'explication': "Une solution étalon a une concentration précisément connue.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "La courbe d'étalonnage est tracée à partir de :", 'options': ["Mesures sur des solutions étalons", "Une seule mesure sur la solution inconnue", "Des calculs théoriques uniquement", "La masse molaire du soluté"], 'reponse_correcte': '0', 'explication': "On mesure la grandeur physique pour chaque solution étalon afin de tracer la courbe.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "L'absorbance est une grandeur :", 'options': ["Sans unité", "En mol/L", "En mètres", "En watts"], 'reponse_correcte': '0', 'explication': "L'absorbance est un nombre sans dimension.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Si l'absorbance d'une solution double, que devient sa concentration (loi de Beer-Lambert) ?", 'options': ["Elle double", "Elle est divisée par deux", "Elle reste identique", "Elle quadruple"], 'reponse_correcte': '0', 'explication': "$A$ est proportionnelle à $C$ : si $A$ double, $C$ double.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Pour une cuve de 1 cm et $\\varepsilon = 200$ L·mol⁻¹·cm⁻¹, quelle est l'absorbance d'une solution à $C = 0{,}01$ mol/L ?", 'options': ["$A = 2$", "$A = 0{,}2$", "$A = 20$", "$A = 0{,}02$"], 'reponse_correcte': '0', 'explication': "$A = 200 \\times 1 \\times 0{,}01 = 2$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Comment détermine-t-on la concentration d'une solution inconnue par étalonnage ?", 'options': ["Par lecture graphique sur la courbe d'étalonnage", "En pesant la solution", "En mesurant son volume", "En calculant sa masse molaire"], 'reponse_correcte': '0', 'explication': "On reporte la valeur mesurée sur la courbe et on lit la concentration correspondante.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "La loi de Beer-Lambert est valable :", 'options': ["Pour des solutions diluées", "Uniquement pour des gaz", "Pour toute concentration", "Seulement en lumière blanche"], 'reponse_correcte': '0', 'explication': "La loi de Beer-Lambert n'est vérifiée que pour des solutions suffisamment diluées.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Un spectrophotomètre mesure :", 'options': ["L'absorbance d'une solution à une longueur d'onde donnée", "La température d'une solution", "La masse d'un soluté", "Le volume d'une solution"], 'reponse_correcte': '0', 'explication': "Le spectrophotomètre envoie un faisceau lumineux monochromatique et mesure l'absorbance.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Si on augmente la longueur $l$ de la cuve, l'absorbance :", 'options': ["Augmente", "Diminue", "Reste constante", "Devient nulle"], 'reponse_correcte': '0', 'explication': "$A = \\varepsilon \\cdot l \\cdot C$ : $A$ est proportionnelle à $l$.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "La loi de Beer-Lambert montre que l'absorbance est proportionnelle à la concentration.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'vrai', 'explication': "$A = \\varepsilon \\cdot l \\cdot C$ : relation de proportionnalité.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "L'absorbance d'une solution peut être négative.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "L'absorbance est toujours positive ou nulle (le blanc est réglé à 0).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Les solutions étalons doivent toutes avoir la même concentration.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "Les solutions étalons ont des concentrations différentes pour tracer la courbe.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Écrire la loi de Beer-Lambert (sous la forme A = ...).", 'reponse_correcte': "A = epsilon l C", 'tolerances': ["A=εlC", "A = ε.l.C", "A = epsilon.l.C"], 'explication': "La loi de Beer-Lambert s'écrit $A = \\varepsilon \\cdot l \\cdot C$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Quelle grandeur physique mesure un conductimètre ?", 'reponse_correcte': "conductivité", 'tolerances': ["la conductivité", "conductance", "la conductance"], 'explication': "Un conductimètre mesure la conductivité (ou la conductance) d'une solution.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Comment appelle-t-on les solutions de concentration connue utilisées pour tracer la courbe d'étalonnage ?", 'reponse_correcte': "solutions étalons", 'tolerances': ["solution étalon", "étalons", "solutions étalon"], 'explication': "Ce sont les solutions étalons, préparées à des concentrations précisément connues.", 'difficulte': 'difficile', 'points': 2},
                    ]
                },
            },
            {
                'ordre': 2,
                'titre': "Titrage direct — équivalence et calcul",
                'duree': 35,
                'contenu': """# Titrage direct — équivalence et calcul\n\n## Principe du titrage\n\nOn fait réagir une solution de concentration inconnue avec un réactif de concentration connue (titrant) jusqu’à l’équivalence.\n\n## Point d’équivalence\n\nÀ l’équivalence, les quantités de matière sont en proportions stœchiométriques :\n$$\n\frac{C_a \cdot V_a}{a} = \frac{C_b \cdot V_{b,eq}}{b}\n$$\n\n- $C_a$, $V_a$ : concentration et volume de l’espèce à doser\n- $C_b$, $V_{b,eq}$ : concentration et volume de titrant à l’équivalence\n- $a$, $b$ : coefficients stœchiométriques\n\n## Détection de l’équivalence\n\n- Changement de couleur (indicateur)\n- Saut de pH (titrage acido-basique)\n- Saut de conductivité ou de potentiel\n\n## Exploitation de la courbe de titrage\n\n- pH = f($V_{\text{titrant}}$) ou $E = f(V)$\n- L’équivalence correspond au point d’inflexion\n\n---\n""",
                'quiz': {
                    'titre': "Quiz — Titrage direct — équivalence et calcul",
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Le réactif titrant est celui dont on connaît :", 'options': ["La concentration", "La couleur", "La masse molaire uniquement", "Le volume final"], 'reponse_correcte': '0', 'explication': "Le réactif titrant a une concentration précisément connue.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "À l'équivalence, les réactifs sont :", 'options': ["En proportions stœchiométriques", "En excès", "Tous consommés", "Tous à la même concentration"], 'reponse_correcte': '0', 'explication': "À l'équivalence, les quantités de matière des réactifs respectent les proportions stœchiométriques.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Un indicateur coloré change de couleur :", 'options': ["Au voisinage de l'équivalence", "Dès le début du titrage", "Seulement en milieu acide", "Quand on arrête de verser"], 'reponse_correcte': '0', 'explication': "L'indicateur coloré vire dans sa zone de virage, choisie pour encadrer le pH à l'équivalence.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Le volume équivalent est le volume de :", 'options': ["Réactif titrant versé à l'équivalence", "Solution titrée dans l'erlenmeyer", "Solvant ajouté", "Solution totale après mélange"], 'reponse_correcte': '0', 'explication': "$V_{b,eq}$ est le volume de titrant versé pour atteindre l'équivalence.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Un titrage acido-basique met en jeu :", 'options': ["Un acide et une base", "Deux acides", "Deux bases", "Un oxydant et un réducteur"], 'reponse_correcte': '0', 'explication': "Un titrage acido-basique repose sur une réaction entre un acide et une base.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "La burette graduée contient :", 'options': ["Le réactif titrant", "La solution à doser", "L'indicateur coloré", "De l'eau distillée"], 'reponse_correcte': '0', 'explication': "La burette contient le réactif titrant que l'on verse progressivement.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "L'erlenmeyer contient :", 'options': ["La solution à doser (titrée)", "Le réactif titrant", "Le solvant pur", "L'indicateur seul"], 'reponse_correcte': '0', 'explication': "L'erlenmeyer reçoit la solution dont on veut déterminer la concentration.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "On repère l'équivalence sur une courbe de titrage pH-métrique par :", 'options': ["Un saut de pH", "Une droite horizontale", "Une diminution régulière du pH", "Un plateau constant"], 'reponse_correcte': '0', 'explication': "L'équivalence se manifeste par un saut brutal de pH.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "D'après la relation à l'équivalence $C_a V_a / a = C_b V_{b,eq} / b$, l'expression de $C_a$ est :", 'options': ["$C_a = C_b \\cdot V_{b,eq} \\cdot a / (b \\cdot V_a)$", "$C_a = C_b \\cdot V_a / V_{b,eq}$", "$C_a = C_b \\cdot b / a$", "$C_a = V_{b,eq} / (C_b \\cdot V_a)$"], 'reponse_correcte': '0', 'explication': "On isole $C_a$ : $C_a = C_b \\cdot V_{b,eq} \\cdot a / (b \\cdot V_a)$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "On titre 20,0 mL d'un monoacide par de la soude à 0,10 mol/L. Le volume équivalent est 15,0 mL. La concentration de l'acide est :", 'options': ["0,075 mol/L", "0,10 mol/L", "0,15 mol/L", "0,030 mol/L"], 'reponse_correcte': '0', 'explication': "$C_a = C_b \\cdot V_{b,eq} / V_a = 0{,}10 \\times 15{,}0 / 20{,}0 = 0{,}075$ mol/L.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Le point d'équivalence correspond à :", 'options': ["Le point d'inflexion de la courbe pH = f(V)", "Le début du titrage", "Le point où pH = 7", "Le point où le volume versé est maximal"], 'reponse_correcte': '0', 'explication': "Le point d'équivalence est le point d'inflexion (pente maximale) de la courbe de titrage.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Avant l'équivalence, le réactif limitant est :", 'options': ["Le réactif titrant", "Le réactif titré", "Les deux réactifs", "Aucun réactif"], 'reponse_correcte': '0', 'explication': "Avant l'équivalence, le titrant versé est entièrement consommé : c'est le réactif limitant.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Pour un titrage colorimétrique, on choisit un indicateur dont :", 'options': ["La zone de virage contient le pH à l'équivalence", "La couleur est toujours rouge", "Le pKa est très éloigné du pH à l'équivalence", "Le volume ajouté est minimal"], 'reponse_correcte': '0', 'explication': "L'indicateur doit virer au pH correspondant à l'équivalence.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "La méthode des tangentes permet de :", 'options': ["Déterminer le volume équivalent sur la courbe de titrage", "Calculer la masse molaire", "Mesurer l'absorbance", "Tracer la courbe d'étalonnage"], 'reponse_correcte': '0', 'explication': "La méthode des tangentes (ou de la dérivée) localise le point d'inflexion, donc l'équivalence.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "À l'équivalence, il reste un excès de réactif titrant dans le mélange.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "À l'équivalence, les réactifs ont été introduits en proportions stœchiométriques : pas d'excès.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Le volume équivalent dépend de la concentration de la solution titrée.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'vrai', 'explication': "$V_{b,eq} = C_a \\cdot V_a \\cdot b / (a \\cdot C_b)$ : il dépend bien de $C_a$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Un titrage nécessite toujours un indicateur coloré.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "On peut repérer l'équivalence par pH-métrie, conductimétrie ou potentiométrie, sans indicateur.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Écrire la relation à l'équivalence pour un titrage (avec les coefficients stœchiométriques a et b).", 'reponse_correcte': "CaVa/a = CbVb,eq/b", 'tolerances': ["Ca.Va/a = Cb.Vb/b", "Ca Va / a = Cb Vb / b", "CaVa/a=CbVbeq/b"], 'explication': "La relation à l'équivalence s'écrit $C_a V_a / a = C_b V_{b,eq} / b$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Comment appelle-t-on le point de la courbe pH = f(V) où la pente est maximale ?", 'reponse_correcte': "point d'équivalence", 'tolerances': ["équivalence", "point d'inflexion", "le point d'équivalence"], 'explication': "Le point d'inflexion de la courbe de titrage correspond au point d'équivalence.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Quel instrument de verrerie permet de verser précisément le réactif titrant ?", 'reponse_correcte': "burette graduée", 'tolerances': ["burette", "la burette", "la burette graduée"], 'explication': "La burette graduée permet un ajout précis et contrôlé du réactif titrant.", 'difficulte': 'difficile', 'points': 2},
                    ]
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 9 — La transformation chimique
    # ──────────────────────────────────────────────
    {
        'ordre': 9,
        'titre': 'La transformation chimique',
        'description': "Modéliser une transformation chimique par une équation de réaction, maîtriser le tableau d'avancement et déterminer le réactif limitant.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Modélisation d'une transformation chimique",
                'duree': 35,
                'contenu': """# Modélisation d'une transformation chimique

## Système chimique

Un **système chimique** est l'ensemble des espèces chimiques présentes dans un milieu réactionnel à un instant donné. On distingue :

- Les **réactifs** : espèces consommées au cours de la transformation.
- Les **produits** : espèces formées au cours de la transformation.
- Les **espèces spectatrices** : présentes mais ne participant pas à la réaction.

## Écriture d'une équation chimique

Une **équation chimique** modélise une transformation chimique. Elle s'écrit sous la forme :

$$
a\,A + b\,B \longrightarrow c\,C + d\,D
$$

où $a$, $b$, $c$, $d$ sont les **coefficients stœchiométriques** (nombres entiers les plus petits possibles).

**Exemple :** combustion du méthane :
$$
CH_4 + 2\,O_2 \longrightarrow CO_2 + 2\,H_2O
$$

## Ajustement des coefficients stœchiométriques

Pour équilibrer une équation, on applique deux lois de conservation :

1. **Conservation des éléments** : chaque élément chimique apparaît en même quantité dans les réactifs et les produits.
2. **Conservation de la charge** : la somme des charges est identique de chaque côté de l'équation (importante pour les réactions en solution ionique).

**Méthode pratique :**
- Écrire les formules brutes des réactifs et produits.
- Compter les atomes de chaque élément de part et d'autre.
- Ajuster les coefficients pour équilibrer.

**Exemple détaillé :** équilibrer la combustion de l'éthanol :
$$
C_2H_6O + 3\,O_2 \longrightarrow 2\,CO_2 + 3\,H_2O
$$

- Carbone : $2 = 2$ ✓
- Hydrogène : $6 = 6$ ✓
- Oxygène : $1 + 6 = 2 \times 2 + 3 = 7$ ✓

## Transformation totale et limitée

- **Transformation totale** : au moins un réactif est entièrement consommé.
- **Transformation limitée** : la réaction s'arrête avant la disparition complète des réactifs (équilibre chimique).

---
""",
                'quiz': {
                    'titre': "Quiz — Modélisation d'une transformation chimique",
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Dans une transformation chimique, les espèces consommées sont appelées :", 'options': ["Les réactifs", "Les produits", "Les espèces spectatrices", "Les catalyseurs"], 'reponse_correcte': '0', 'explication': "Les réactifs sont les espèces consommées au cours de la transformation.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "Les espèces formées au cours d'une transformation chimique sont :", 'options': ["Les produits", "Les réactifs", "Les ions spectateurs", "Les solvants"], 'reponse_correcte': '0', 'explication': "Les produits sont les espèces formées lors de la transformation.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Une espèce spectatrice est une espèce qui :", 'options': ["Est présente mais ne participe pas à la réaction", "Est entièrement consommée", "Est formée en fin de réaction", "Accélère la réaction"], 'reponse_correcte': '0', 'explication': "Les espèces spectatrices sont présentes mais ne participent pas à la réaction.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Dans l'équation $CH_4 + 2\\,O_2 \\longrightarrow CO_2 + 2\\,H_2O$, le coefficient de $O_2$ est :", 'options': ["2", "1", "3", "4"], 'reponse_correcte': '0', 'explication': "Le coefficient stœchiométrique devant $O_2$ est 2.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "Les coefficients stœchiométriques doivent être :", 'options': ["Les entiers les plus petits possibles", "Des nombres décimaux", "Des fractions", "Des puissances de dix"], 'reponse_correcte': '0', 'explication': "Les coefficients stœchiométriques sont les entiers les plus petits possibles.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Lors de l'équilibrage d'une équation chimique, on conserve :", 'options': ["Le nombre d'atomes de chaque élément", "Le nombre total de molécules", "La masse d'un seul élément", "Le volume des réactifs"], 'reponse_correcte': '0', 'explication': "On conserve le nombre d'atomes de chaque élément de chaque côté.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Dans une équation chimique, la flèche sépare :", 'options': ["Les réactifs des produits", "Les solides des liquides", "Les ions des molécules", "Les coefficients des formules"], 'reponse_correcte': '0', 'explication': "La flèche indique le sens de la transformation : réactifs → produits.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Un système chimique est constitué :", 'options': ["De toutes les espèces présentes dans le milieu réactionnel", "Uniquement des réactifs", "Uniquement des produits", "Du solvant uniquement"], 'reponse_correcte': '0', 'explication': "Le système chimique comprend réactifs, produits et espèces spectatrices.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Pour la combustion de l'éthanol $C_2H_6O + a\\,O_2 \\longrightarrow 2\\,CO_2 + 3\\,H_2O$, quelle est la valeur de $a$ ?", 'options': ["3", "2", "4", "5"], 'reponse_correcte': '0', 'explication': "Bilan O : $1 + 2a = 4 + 3 = 7$, donc $a = 3$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Quelle équation est correctement équilibrée ?", 'options': ["$4\\,Fe + 3\\,O_2 \\longrightarrow 2\\,Fe_2O_3$", "$2\\,Fe + 3\\,O_2 \\longrightarrow 2\\,Fe_2O_3$", "$Fe + O_2 \\longrightarrow Fe_2O_3$", "$4\\,Fe + 2\\,O_2 \\longrightarrow 2\\,Fe_2O_3$"], 'reponse_correcte': '0', 'explication': "4 Fe = 4, 6 O = 6 : équilibrée.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Dans $C_3H_8 + 5\\,O_2 \\longrightarrow 3\\,CO_2 + 4\\,H_2O$, combien d'atomes O du côté des produits ?", 'options': ["10", "7", "8", "12"], 'reponse_correcte': '0', 'explication': "$3 \\times 2 + 4 \\times 1 = 10$ atomes O.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Pour équilibrer $Al + Cl_2 \\longrightarrow AlCl_3$, les coefficients sont :", 'options': ["2, 3, 2", "1, 3, 1", "3, 2, 3", "2, 2, 2"], 'reponse_correcte': '0', 'explication': "$2\\,Al + 3\\,Cl_2 \\longrightarrow 2\\,AlCl_3$ : Al = 2/2, Cl = 6/6.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Lors d'une transformation limitée :", 'options': ["La réaction s'arrête avant la consommation totale des réactifs", "Tous les réactifs sont entièrement consommés", "Un seul produit est formé", "La réaction est irréversible"], 'reponse_correcte': '0', 'explication': "Une transformation limitée s'arrête avant que tous les réactifs ne soient consommés.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "La conservation de la charge lors de l'équilibrage est importante pour :", 'options': ["Les réactions en solution ionique", "Les combustions en phase gazeuse", "Les changements d'état", "Les dissolutions de gaz"], 'reponse_correcte': '0', 'explication': "La conservation de la charge est essentielle pour les réactions ioniques.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Les coefficients stœchiométriques peuvent être des nombres décimaux.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "Les coefficients doivent être les entiers les plus petits possibles.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Dans une transformation totale, au moins un réactif est entièrement consommé.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'vrai', 'explication': "Par définition, une transformation totale consomme entièrement au moins un réactif.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Les espèces spectatrices apparaissent dans l'équation chimique équilibrée.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "Les espèces spectatrices ne figurent pas dans l'équation chimique.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Quel est le coefficient stœchiométrique de $O_2$ dans : $C_2H_6O + ?\\,O_2 \\longrightarrow 2\\,CO_2 + 3\\,H_2O$ ?", 'options': None, 'reponse_correcte': '3', 'tolerances': ["trois", "3 mol", "3,0"], 'explication': "Bilan O : $1 + 2a = 7$, donc $a = 3$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Comment appelle-t-on une transformation chimique qui s'arrête avant la consommation totale des réactifs ?", 'options': None, 'reponse_correcte': 'transformation limitée', 'tolerances': ["limitée", "réaction limitée", "transformation non totale"], 'explication': "Une transformation limitée s'arrête avant la disparition complète des réactifs.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Équilibrer : $?\\,Fe + ?\\,O_2 \\longrightarrow ?\\,Fe_2O_3$. Donner les trois coefficients séparés par des virgules.", 'options': None, 'reponse_correcte': '4, 3, 2', 'tolerances': ["4,3,2", "4 3 2", "4; 3; 2"], 'explication': "$4\\,Fe + 3\\,O_2 \\longrightarrow 2\\,Fe_2O_3$.", 'difficulte': 'difficile', 'points': 2},
                    ]
                },
            },
            {
                'ordre': 2,
                'titre': "Avancement et bilan de matière",
                'duree': 35,
                'contenu': """# Avancement et bilan de matière

## Avancement de réaction

L'**avancement** $x$ (en mol) est une grandeur qui mesure la progression d'une transformation chimique. Pour la réaction :
$$
a\,A + b\,B \longrightarrow c\,C + d\,D
$$

les quantités de matière à un instant donné s'expriment :

| Espèce | Quantité initiale | Quantité à l'instant $t$ |
|--------|-------------------|--------------------------|
| $A$ | $n_A^0$ | $n_A^0 - a \cdot x$ |
| $B$ | $n_B^0$ | $n_B^0 - b \cdot x$ |
| $C$ | $0$ | $c \cdot x$ |
| $D$ | $0$ | $d \cdot x$ |

## Tableau d'avancement

Le **tableau d'avancement** résume l'évolution des quantités de matière :

| État | Avancement | $a\,A$ | $b\,B$ | $c\,C$ | $d\,D$ |
|------|-----------|--------|--------|--------|--------|
| Initial | $x = 0$ | $n_A^0$ | $n_B^0$ | $0$ | $0$ |
| En cours | $x$ | $n_A^0 - a\,x$ | $n_B^0 - b\,x$ | $c\,x$ | $d\,x$ |
| Final | $x_{\max}$ | $n_A^0 - a\,x_{\max}$ | $n_B^0 - b\,x_{\max}$ | $c\,x_{\max}$ | $d\,x_{\max}$ |

## Avancement maximal et réactif limitant

L'**avancement maximal** $x_{\max}$ est la plus grande valeur de $x$ pour laquelle la quantité d'au moins un réactif s'annule :
$$
x_{\max} = \min\left(\frac{n_A^0}{a}\,;\,\frac{n_B^0}{b}\right)
$$

Le **réactif limitant** est celui dont la quantité s'annule en premier (celui qui impose $x_{\max}$). L'autre réactif est dit **en excès**.

## Exemple complet

Soit la réaction : $2\,H_2 + O_2 \longrightarrow 2\,H_2O$

Avec $n_{H_2}^0 = 6$ mol et $n_{O_2}^0 = 2$ mol :

- $x_{\max}(H_2) = \frac{6}{2} = 3$ mol
- $x_{\max}(O_2) = \frac{2}{1} = 2$ mol

Donc $x_{\max} = 2$ mol et $O_2$ est le réactif limitant.

**Bilan final :**
- $n_{H_2} = 6 - 2 \times 2 = 2$ mol (en excès)
- $n_{O_2} = 2 - 1 \times 2 = 0$ mol (entièrement consommé)
- $n_{H_2O} = 2 \times 2 = 4$ mol

## Composition de l'état final

À l'état final, on connaît toutes les quantités de matière. On peut alors calculer :
- Les **concentrations** si la réaction a lieu en solution : $C = \frac{n}{V}$
- Les **masses** des produits formés : $m = n \times M$
- Le **volume** d'un gaz produit (à 25 °C, 1 bar) : $V = n \times V_m$ avec $V_m \approx 24$ L·mol$^{-1}$

---
""",
                'quiz': {
                    'titre': "Quiz — Avancement et bilan de matière",
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "L'avancement d'une réaction chimique est noté :", 'options': ["$x$", "$n$", "$m$", "$V$"], 'reponse_correcte': '0', 'explication': "L'avancement est noté $x$ et s'exprime en mol.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "L'unité de l'avancement est :", 'options': ["La mole", "Le litre", "Le gramme", "Le joule"], 'reponse_correcte': '0', 'explication': "L'avancement $x$ s'exprime en mol.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Le réactif limitant est celui qui :", 'options': ["Est entièrement consommé en premier", "Est en excès à l'état final", "A le plus grand coefficient stœchiométrique", "A la plus grande masse molaire"], 'reponse_correcte': '0', 'explication': "Le réactif limitant est celui dont la quantité s'annule en premier.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Dans un tableau d'avancement, l'état initial correspond à :", 'options': ["$x = 0$", "$x = x_{max}$", "$x = 1$", "$x = n$"], 'reponse_correcte': '0', 'explication': "L'état initial correspond à un avancement nul : $x = 0$.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "L'avancement maximal est atteint lorsque :", 'options': ["Au moins un réactif est entièrement consommé", "Tous les produits sont formés", "La température est maximale", "Le volume est maximal"], 'reponse_correcte': '0', 'explication': "L'avancement maximal correspond à la consommation totale d'au moins un réactif.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Un réactif en excès est un réactif qui :", 'options': ["N'est pas entièrement consommé à l'état final", "Est entièrement consommé", "Ne participe pas à la réaction", "Est ajouté après la réaction"], 'reponse_correcte': '0', 'explication': "Le réactif en excès reste partiellement à l'état final.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Le tableau d'avancement permet de :", 'options': ["Suivre l'évolution des quantités de matière", "Mesurer la température", "Calculer la vitesse de réaction", "Déterminer la masse molaire"], 'reponse_correcte': '0', 'explication': "Le tableau d'avancement récapitule les quantités de matière à chaque état.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Pour $a\\,A + b\\,B \\longrightarrow c\\,C + d\\,D$, la quantité de $C$ formée est :", 'options': ["$c \\cdot x$", "$c - x$", "$c + x$", "$c / x$"], 'reponse_correcte': '0', 'explication': "La quantité de produit $C$ à l'instant $t$ est $c \\cdot x$.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Pour $2\\,H_2 + O_2 \\longrightarrow 2\\,H_2O$ avec $n_{H_2}^0 = 6$ mol et $n_{O_2}^0 = 2$ mol, $x_{max}$ vaut :", 'options': ["2 mol", "3 mol", "6 mol", "1 mol"], 'reponse_correcte': '0', 'explication': "$x_{max} = \\min(6/2\\,;\\,2/1) = \\min(3\\,;\\,2) = 2$ mol.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "Dans le même exemple, le réactif limitant est :", 'options': ["$O_2$", "$H_2$", "$H_2O$", "Les deux à la fois"], 'reponse_correcte': '0', 'explication': "$O_2$ impose $x_{max} = 2$ mol, c'est le réactif limitant.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Pour $N_2 + 3\\,H_2 \\longrightarrow 2\\,NH_3$ avec $n_{N_2}^0 = 1$ mol et $n_{H_2}^0 = 6$ mol, $x_{max}$ vaut :", 'options': ["1 mol", "2 mol", "3 mol", "6 mol"], 'reponse_correcte': '0', 'explication': "$x_{max} = \\min(1/1\\,;\\,6/3) = \\min(1\\,;\\,2) = 1$ mol.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Pour $2\\,H_2 + O_2 \\longrightarrow 2\\,H_2O$ avec $x_{max} = 2$ mol, la quantité de $H_2O$ formée est :", 'options': ["4 mol", "2 mol", "6 mol", "1 mol"], 'reponse_correcte': '0', 'explication': "$n_{H_2O} = 2 \\times x_{max} = 4$ mol.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Le volume molaire d'un gaz à 25 °C et 1 bar vaut environ :", 'options': ["24 L·mol⁻¹", "22,4 L·mol⁻¹", "12 L·mol⁻¹", "48 L·mol⁻¹"], 'reponse_correcte': '0', 'explication': "À 25 °C et 1 bar, $V_m \\approx 24$ L·mol⁻¹.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "Pour calculer la masse d'un produit à partir de sa quantité de matière :", 'options': ["$m = n \\times M$", "$m = C \\times V$", "$m = n / V$", "$m = n \\times V_m$"], 'reponse_correcte': '0', 'explication': "La relation masse-quantité est $m = n \\times M$.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "L'avancement maximal est toujours égal à la plus petite quantité initiale de réactif.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "Il faut diviser chaque quantité initiale par son coefficient stœchiométrique avant de comparer.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Les quantités de produits augmentent quand l'avancement augmente.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'vrai', 'explication': "Les quantités de produits sont de la forme $c \\cdot x$, croissantes avec $x$.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "Le réactif limitant est toujours celui introduit en plus petite quantité de matière.", 'options': ['Vrai', 'Faux'], 'reponse_correcte': 'faux', 'explication': "Cela dépend du rapport quantité/coefficient stœchiométrique.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Pour $2\\,H_2 + O_2 \\longrightarrow 2\\,H_2O$ avec $n_{H_2}^0 = 6$ mol et $n_{O_2}^0 = 2$ mol, quelle quantité de $H_2$ reste à l'état final (en mol) ?", 'options': None, 'reponse_correcte': '2', 'tolerances': ["2 mol", "deux", "2,0"], 'explication': "$n_{H_2} = 6 - 2 \\times 2 = 2$ mol.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Donner la formule de $x_{max}$ pour $a\\,A + b\\,B \\longrightarrow c\\,C + d\\,D$.", 'options': None, 'reponse_correcte': 'min(nA/a, nB/b)', 'tolerances': ["xmax = min(nA/a, nB/b)", "min(nA/a ; nB/b)", "xmax = min(nA/a ; nB/b)"], 'explication': "$x_{max} = \\min(n_A^0/a\\,;\\,n_B^0/b)$.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Pour $N_2 + 3\\,H_2 \\longrightarrow 2\\,NH_3$ avec $n_{N_2}^0 = 2$ mol et $n_{H_2}^0 = 3$ mol, quel est le réactif limitant ?", 'options': None, 'reponse_correcte': 'H2', 'tolerances': ["dihydrogène", "le dihydrogène", "H₂"], 'explication': "$x_{max}(N_2) = 2$, $x_{max}(H_2) = 1$ : $H_2$ est limitant.", 'difficulte': 'difficile', 'points': 2},
                    ]
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 10 — Cohésion de la matière et mélanges
    # ──────────────────────────────────────────────
    {
        'ordre': 10,
        'titre': 'Cohésion de la matière et mélanges',
        'description': "Comprendre les interactions intermoléculaires responsables de la cohésion de la matière et les phénomènes de solubilité et miscibilité.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Interactions intermoléculaires et cohésion",
                'duree': 35,
                'contenu': """# Interactions intermoléculaires et cohésion

## Les interactions de Van der Waals

Les **interactions de Van der Waals** sont des forces attractives de faible intensité entre molécules. Elles regroupent trois contributions :

### Interaction de Keesom (dipôle permanent – dipôle permanent)

Entre deux molécules **polaires**, les dipôles permanents s'attirent mutuellement. Plus le moment dipolaire $\mu$ est élevé, plus l'interaction est forte.

### Interaction de Debye (dipôle permanent – dipôle induit)

Une molécule polaire **polarise** une molécule voisine (même apolaire), créant un dipôle induit. L'attraction résultante est l'interaction de Debye.

### Interaction de London (dipôle instantané – dipôle induit)

Même entre molécules **apolaires**, des fluctuations instantanées du nuage électronique créent des dipôles temporaires qui induisent des dipôles dans les molécules voisines. L'interaction de London existe dans **toutes** les molécules.

## La liaison hydrogène

La **liaison hydrogène** est une interaction intermoléculaire plus forte que les forces de Van der Waals. Elle se forme lorsqu'un atome d'hydrogène, lié à un atome très électronégatif ($O$, $N$, $F$), interagit avec un autre atome électronégatif porteur d'un doublet non liant :

$$
X-H \cdots Y \quad \text{avec } X, Y \in \{O, N, F\}
$$

**Exemples :**
- Dans l'eau : $O-H \cdots O$
- Dans l'ADN : $N-H \cdots O$ et $N-H \cdots N$

Énergie typique d'une liaison hydrogène : $10$ à $40$ kJ·mol$^{-1}$ (contre $< 5$ kJ·mol$^{-1}$ pour Van der Waals).

## Influence sur les propriétés physiques

Les interactions intermoléculaires déterminent les propriétés macroscopiques de la matière :

### Température d'ébullition

- Plus les interactions sont fortes, plus la température d'ébullition est **élevée**.
- L'eau ($T_{eb} = 100$ °C) bout bien plus haut que le sulfure d'hydrogène $H_2S$ ($T_{eb} = -60$ °C), grâce aux liaisons hydrogène.

### Viscosité

- Plus les interactions intermoléculaires sont intenses, plus le liquide est **visqueux** (résistance à l'écoulement).
- Le glycérol (3 groupes $-OH$, nombreuses liaisons H) est très visqueux comparé à l'éthanol.

### Ordre de grandeur des interactions

| Type d'interaction | Énergie typique (kJ·mol$^{-1}$) |
|---|---|
| London | $0{,}5$ à $5$ |
| Keesom / Debye | $1$ à $10$ |
| Liaison hydrogène | $10$ à $40$ |
| Liaison covalente | $150$ à $800$ |

---
""",
                'quiz': {
                    'titre': 'Quiz — Interactions intermoléculaires et cohésion',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Les interactions de Van der Waals regroupent :", 'options': ["Keesom, Debye et London", "Keesom et liaison hydrogène", "London et liaison covalente", "Debye et liaison ionique"], 'reponse_correcte': '0', 'explication': "Les trois contributions de Van der Waals sont Keesom, Debye et London.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "L'interaction de London existe :", 'options': ["Dans toutes les molécules", "Uniquement entre molécules polaires", "Uniquement entre ions", "Uniquement entre molécules apolaires"], 'reponse_correcte': '0', 'explication': "L'interaction de London existe dans toutes les molécules, polaires ou apolaires.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "La liaison hydrogène se forme entre un atome H lié à un atome très électronégatif et :", 'options': ["Un autre atome électronégatif porteur d'un doublet non liant", "Un atome de carbone", "Un proton libre", "Un électron libre"], 'reponse_correcte': '0', 'explication': "La liaison hydrogène nécessite un doublet non liant sur l'atome accepteur.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "Quels atomes peuvent participer à une liaison hydrogène (notés X ou Y dans X−H···Y) ?", 'options': ["O, N et F", "C, H et O", "S, P et Cl", "Na, K et Ca"], 'reponse_correcte': '0', 'explication': "Les atomes suffisamment électronégatifs pour former des liaisons H sont O, N et F.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "L'interaction de Keesom a lieu entre :", 'options': ["Deux dipôles permanents", "Deux dipôles induits", "Un dipôle permanent et un dipôle induit", "Deux ions"], 'reponse_correcte': '0', 'explication': "L'interaction de Keesom est l'attraction entre deux molécules polaires (dipôles permanents).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "Plus les interactions intermoléculaires sont fortes, la température d'ébullition est :", 'options': ["Plus élevée", "Plus basse", "Inchangée", "Nulle"], 'reponse_correcte': '0', 'explication': "Des interactions plus fortes nécessitent plus d'énergie pour vaporiser, donc T_eb augmente.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "L'interaction de Debye met en jeu :", 'options': ["Un dipôle permanent et un dipôle induit", "Deux dipôles permanents", "Deux dipôles instantanés", "Un ion et un dipôle"], 'reponse_correcte': '0', 'explication': "L'interaction de Debye est l'attraction entre un dipôle permanent et un dipôle induit.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "Le glycérol est très visqueux car il possède :", 'options': ["De nombreuses liaisons hydrogène grâce à ses groupes −OH", "Des liaisons covalentes très fortes", "Une masse molaire très élevée", "Des interactions de London très intenses"], 'reponse_correcte': '0', 'explication': "Le glycérol a 3 groupes −OH permettant de nombreuses liaisons H, d'où sa forte viscosité.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "L'eau ($T_{eb} = 100$ °C) bout à température bien plus élevée que $H_2S$ ($T_{eb} = -60$ °C) car :", 'options': ["L'eau forme des liaisons hydrogène, pas H₂S", "L'eau a une masse molaire plus élevée", "H₂S est un gaz noble", "L'eau a des interactions de London plus fortes"], 'reponse_correcte': '0', 'explication': "L'eau forme des liaisons hydrogène (O−H···O), contrairement à H₂S où S est moins électronégatif.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "L'énergie typique d'une liaison hydrogène est de l'ordre de :", 'options': ["10 à 40 kJ·mol⁻¹", "0,5 à 5 kJ·mol⁻¹", "150 à 800 kJ·mol⁻¹", "100 à 150 kJ·mol⁻¹"], 'reponse_correcte': '0', 'explication': "La liaison hydrogène a une énergie typique de 10 à 40 kJ·mol⁻¹.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "Parmi ces interactions, laquelle est la plus forte ?", 'options': ["Liaison hydrogène", "Interaction de London", "Interaction de Keesom", "Interaction de Debye"], 'reponse_correcte': '0', 'explication': "La liaison hydrogène (10-40 kJ·mol⁻¹) est plus forte que les forces de Van der Waals (<10 kJ·mol⁻¹).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "Dans l'ADN, les liaisons hydrogène se forment entre :", 'options': ["N−H···O et N−H···N", "C−H···C et C−H···O", "S−H···O et S−H···N", "O−H···C et N−H···C"], 'reponse_correcte': '0', 'explication': "Dans l'ADN, les liaisons H sont de type N−H···O et N−H···N entre les bases complémentaires.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "L'énergie typique des interactions de London est :", 'options': ["0,5 à 5 kJ·mol⁻¹", "10 à 40 kJ·mol⁻¹", "150 à 800 kJ·mol⁻¹", "50 à 100 kJ·mol⁻¹"], 'reponse_correcte': '0', 'explication': "Les interactions de London sont les plus faibles : 0,5 à 5 kJ·mol⁻¹.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "La viscosité d'un liquide augmente quand :", 'options': ["Les interactions intermoléculaires sont plus intenses", "La température augmente", "La masse molaire diminue", "Le liquide est apolaire"], 'reponse_correcte': '0', 'explication': "Des interactions plus fortes augmentent la résistance à l'écoulement (viscosité).", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "La liaison hydrogène est plus forte que les interactions de Van der Waals.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "La liaison H (10-40 kJ·mol⁻¹) est nettement plus forte que les forces de Van der Waals (<10 kJ·mol⁻¹).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Les interactions de London n'existent que dans les molécules apolaires.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Les interactions de London existent dans toutes les molécules, polaires ou apolaires.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "L'atome de soufre (S) peut participer à la formation de liaisons hydrogène en tant que X ou Y.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "Seuls O, N et F sont suffisamment électronégatifs pour former des liaisons hydrogène.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Nommer les trois contributions aux interactions de Van der Waals.", 'reponse_correcte': "Keesom, Debye et London", 'tolerances': ["Keesom Debye London", "London Debye Keesom", "London, Keesom, Debye"], 'explication': "Les trois contributions sont : Keesom (dipôle-dipôle), Debye (dipôle-dipôle induit) et London (dipôle instantané-dipôle induit).", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Quels sont les trois atomes électronégatifs pouvant former une liaison hydrogène (X ou Y dans X−H···Y) ?", 'reponse_correcte': "O, N et F", 'tolerances': ["O N F", "oxygène azote fluor", "N, O et F"], 'explication': "Seuls O, N et F sont suffisamment électronégatifs pour former des liaisons hydrogène.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Quel est l'ordre de grandeur de l'énergie d'une liaison hydrogène (en kJ·mol⁻¹) ?", 'reponse_correcte': "10 à 40", 'tolerances': ["10-40", "10 a 40", "entre 10 et 40"], 'explication': "L'énergie typique d'une liaison hydrogène est de 10 à 40 kJ·mol⁻¹.", 'difficulte': 'difficile', 'points': 2},
                    ]
                },
            },
            {
                'ordre': 2,
                'titre': "Solubilité et miscibilité",
                'duree': 30,
                'contenu': """# Solubilité et miscibilité

## Dissolution

Lors de la **dissolution** d'un soluté dans un solvant, des interactions s'établissent entre les molécules de soluté et celles de solvant (solvatation). On distingue :

- **Soluté** : espèce dissoute (solide, liquide ou gaz).
- **Solvant** : espèce en excès qui constitue le milieu.
- **Solution** : mélange homogène obtenu.

## Solubilité

La **solubilité** $s$ d'un soluté dans un solvant est la masse maximale (en g) que l'on peut dissoudre dans un volume donné de solvant (généralement 1 L), à une température donnée.

$$
s = \frac{m_{\text{soluté dissous}}}{V_{\text{solvant}}}
$$

Unité courante : g·L$^{-1}$.

On peut aussi exprimer la solubilité en concentration molaire :
$$
C_{\text{sat}} = \frac{s}{M}
$$
où $M$ est la masse molaire du soluté.

## Paramètres influençant la solubilité

- **Température** : en général, la solubilité des solides dans les liquides **augmente** avec la température. Pour les gaz, elle **diminue** avec la température.
- **Nature du soluté et du solvant** : la règle fondamentale est « **le semblable dissout le semblable** ».

## La règle « le semblable dissout le semblable »

- Un soluté **polaire** ou **ionique** se dissout bien dans un solvant **polaire** (ex : $NaCl$ dans l'eau).
- Un soluté **apolaire** se dissout bien dans un solvant **apolaire** (ex : graisse dans l'hexane).
- Un soluté apolaire se dissout **mal** dans un solvant polaire (ex : huile dans eau).

## Miscibilité de deux liquides

Deux liquides sont **miscibles** s'ils forment un mélange homogène en toutes proportions.

**Exemples :**
- Eau et éthanol : **miscibles** (interactions O−H similaires)
- Eau et cyclohexane : **non miscibles** (polarités très différentes)

Lorsque deux liquides sont non miscibles, ils forment deux **phases** distinctes. Le liquide le moins dense se place au-dessus.

## Extraction liquide-liquide

L'**extraction liquide-liquide** utilise la différence de solubilité d'une espèce entre deux solvants non miscibles.

**Protocole :**
1. Introduire la solution aqueuse et le solvant organique dans une ampoule à décanter.
2. Agiter vigoureusement puis dégazer.
3. Laisser décanter : deux phases se séparent.
4. Récupérer la phase contenant l'espèce d'intérêt.

**Choix du solvant extracteur :**
- Non miscible avec le solvant initial.
- L'espèce à extraire y est **plus soluble** que dans le solvant initial.
- Si possible, facilement évaporable pour récupérer le soluté pur.

---
""",
                'quiz': {
                    'titre': 'Quiz — Solubilité et miscibilité',
                    'questions': [
                        # 8 QCM facile
                        {'ordre': 1, 'type': 'qcm', 'texte': "Le solvant est :", 'options': ["L'espèce en excès dans la solution", "L'espèce dissoute", "Le mélange obtenu", "Le résidu solide"], 'reponse_correcte': '0', 'explication': "Le solvant est l'espèce présente en excès qui constitue le milieu.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 2, 'type': 'qcm', 'texte': "La solubilité s'exprime couramment en :", 'options': ["g·L⁻¹", "mol·L⁻¹", "kg·m⁻³", "Pa"], 'reponse_correcte': '0', 'explication': "La solubilité est généralement exprimée en g·L⁻¹.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 3, 'type': 'qcm', 'texte': "Deux liquides miscibles forment :", 'options': ["Un mélange homogène", "Deux phases distinctes", "Un précipité", "Un gaz"], 'reponse_correcte': '0', 'explication': "Deux liquides miscibles se mélangent en un mélange homogène en toutes proportions.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 4, 'type': 'qcm', 'texte': "L'eau et l'éthanol sont :", 'options': ["Miscibles", "Non miscibles", "Partiellement miscibles à froid", "Miscibles uniquement à chaud"], 'reponse_correcte': '0', 'explication': "L'eau et l'éthanol sont miscibles grâce à leurs interactions O−H similaires.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 5, 'type': 'qcm', 'texte': "La dissolution produit :", 'options': ["Une solution", "Un précipité", "Un gaz", "Un cristal"], 'reponse_correcte': '0', 'explication': "La dissolution d'un soluté dans un solvant produit une solution (mélange homogène).", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 6, 'type': 'qcm', 'texte': "L'eau et le cyclohexane sont :", 'options': ["Non miscibles", "Miscibles", "Partiellement miscibles", "Miscibles à chaud uniquement"], 'reponse_correcte': '0', 'explication': "L'eau (polaire) et le cyclohexane (apolaire) ne sont pas miscibles.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 7, 'type': 'qcm', 'texte': "Lorsque deux liquides non miscibles sont mélangés, le liquide le moins dense se place :", 'options': ["Au-dessus", "Au-dessous", "Au milieu", "De manière aléatoire"], 'reponse_correcte': '0', 'explication': "Le liquide le moins dense flotte et se place au-dessus.", 'difficulte': 'facile', 'points': 1},
                        {'ordre': 8, 'type': 'qcm', 'texte': "L'appareil utilisé pour une extraction liquide-liquide est :", 'options': ["Une ampoule à décanter", "Un erlenmeyer", "Un ballon à fond rond", "Un cristallisoir"], 'reponse_correcte': '0', 'explication': "L'ampoule à décanter permet de séparer deux phases liquides non miscibles.", 'difficulte': 'facile', 'points': 1},
                        # 6 QCM moyen
                        {'ordre': 9, 'type': 'qcm', 'texte': "Selon la règle « le semblable dissout le semblable », le NaCl se dissout bien dans :", 'options': ["L'eau (solvant polaire)", "L'hexane (solvant apolaire)", "Le cyclohexane", "L'huile"], 'reponse_correcte': '0', 'explication': "NaCl est ionique, il se dissout dans un solvant polaire comme l'eau.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 10, 'type': 'qcm', 'texte': "En général, la solubilité des solides dans les liquides quand la température augmente :", 'options': ["Augmente", "Diminue", "Reste constante", "S'annule"], 'reponse_correcte': '0', 'explication': "La solubilité des solides dans les liquides augmente généralement avec la température.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 11, 'type': 'qcm', 'texte': "La solubilité des gaz dans les liquides quand la température augmente :", 'options': ["Diminue", "Augmente", "Reste constante", "Double"], 'reponse_correcte': '0', 'explication': "La solubilité des gaz diminue avec la température (agitation thermique facilite le dégazage).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 12, 'type': 'qcm', 'texte': "La concentration à saturation $C_{sat}$ est reliée à la solubilité $s$ et à la masse molaire $M$ par :", 'options': ["C_sat = s / M", "C_sat = s × M", "C_sat = M / s", "C_sat = s + M"], 'reponse_correcte': '0', 'explication': "$C_{sat} = s / M$ où $s$ est en g·L⁻¹ et $M$ en g·mol⁻¹.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 13, 'type': 'qcm', 'texte': "Pour une extraction liquide-liquide, le solvant extracteur doit être :", 'options': ["Non miscible avec le solvant initial et meilleur solvant pour l'espèce à extraire", "Miscible avec le solvant initial", "De même densité que le solvant initial", "De même polarité que le solvant initial"], 'reponse_correcte': '0', 'explication': "Le solvant extracteur doit être non miscible et l'espèce doit y être plus soluble.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 14, 'type': 'qcm', 'texte': "La graisse se dissout bien dans l'hexane car :", 'options': ["Les deux sont apolaires", "Les deux sont polaires", "L'hexane est ionique", "La graisse est ionique"], 'reponse_correcte': '0', 'explication': "La graisse (apolaire) se dissout dans l'hexane (apolaire) : le semblable dissout le semblable.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Vrai/Faux moyen
                        {'ordre': 15, 'type': 'vrai_faux', 'texte': "Un soluté apolaire se dissout facilement dans l'eau.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'faux', 'explication': "L'eau est polaire ; un soluté apolaire s'y dissout mal (ex : huile dans eau).", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 16, 'type': 'vrai_faux', 'texte': "Lors d'une extraction liquide-liquide, on doit dégazer après agitation.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "Après agitation, il faut dégazer pour évacuer la surpression avant de laisser décanter.", 'difficulte': 'moyen', 'points': 1},
                        {'ordre': 17, 'type': 'vrai_faux', 'texte': "La solubilité est la masse maximale de soluté que l'on peut dissoudre dans un volume donné de solvant à température donnée.", 'options': ["Vrai", "Faux"], 'reponse_correcte': 'vrai', 'explication': "C'est la définition exacte de la solubilité.", 'difficulte': 'moyen', 'points': 1},
                        # 3 Texte libre difficile
                        {'ordre': 18, 'type': 'texte_libre', 'texte': "Énoncer la règle fondamentale de la solubilité.", 'reponse_correcte': "Le semblable dissout le semblable", 'tolerances': ["le semblable dissout le semblable", "semblable dissout semblable", "like dissolves like"], 'explication': "Un soluté polaire se dissout dans un solvant polaire, un soluté apolaire dans un solvant apolaire.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 19, 'type': 'texte_libre', 'texte': "Donner la formule reliant la concentration à saturation $C_{sat}$, la solubilité $s$ et la masse molaire $M$.", 'reponse_correcte': "C_sat = s / M", 'tolerances': ["Csat = s/M", "C = s / M", "C_sat=s/M"], 'explication': "$C_{sat} = s / M$ avec $s$ en g·L⁻¹ et $M$ en g·mol⁻¹.", 'difficulte': 'difficile', 'points': 2},
                        {'ordre': 20, 'type': 'texte_libre', 'texte': "Quel appareil utilise-t-on pour réaliser une extraction liquide-liquide ?", 'reponse_correcte': "Ampoule à décanter", 'tolerances': ["ampoule a decanter", "une ampoule à décanter", "ampoule de décantation"], 'explication': "L'ampoule à décanter permet de séparer deux liquides non miscibles.", 'difficulte': 'difficile', 'points': 2},
                    ]
                },
            },
        ],
    },
]

class Command(BaseCommand):
    help = "Recrée entièrement les chapitres 1 à 10 de Chimie Première (avec quiz pour ch.1-10)."

    def handle(self, *args, **options):
        from courses.models import Matiere, Chapitre, Lecon, Quiz, Question

        chimie = Matiere.objects.get(nom="chimie")

        deleted, _ = Chapitre.objects.filter(
            matiere=chimie, niveau="premiere"
        ).delete()
        self.stdout.write(f"  🗑  {deleted} chapitres supprimés")

        for chap_data in CHAPITRES:
            chapitre = Chapitre.objects.create(
                matiere=chimie,
                niveau="premiere",
                ordre=chap_data["ordre"],
                titre=chap_data["titre"],
                description=chap_data.get("description", ""),
                score_minimum_deblocage=chap_data.get("score_minimum", 60.0),
            )
            self.stdout.write(f"  ✔ Ch.{chap_data['ordre']} {chap_data['titre']}")

            for lecon_data in chap_data["lecons"]:
                lecon = Lecon.objects.create(
                    chapitre=chapitre,
                    ordre=lecon_data["ordre"],
                    titre=lecon_data["titre"],
                    contenu=lecon_data["contenu"],
                    duree_estimee=lecon_data.get("duree", 30),
                )
                # Quiz et questions
                if "quiz" in lecon_data:
                    quiz_data = lecon_data["quiz"]
                    quiz = Quiz.objects.create(
                        lecon=lecon,
                        titre=quiz_data.get("titre", f"Quiz — {lecon.titre}"),
                        score_minimum=quiz_data.get("score_minimum", 60.0),
                    )
                    for q in quiz_data["questions"]:
                        Question.objects.create(
                            quiz=quiz,
                            ordre=q["ordre"],
                            texte=q["texte"],
                            type=q.get("type", "qcm"),
                            options=q.get("options"),
                            reponse_correcte=str(q["reponse_correcte"]),
                            tolerances=q.get("tolerances"),
                            explication=q.get("explication", ""),
                            difficulte=q.get("difficulte", "moyen"),
                            points=q.get("points", 1),
                        )

        self.stdout.write(self.style.SUCCESS("✅ Chimie Première (ch.1-10) recréée avec succès."))
