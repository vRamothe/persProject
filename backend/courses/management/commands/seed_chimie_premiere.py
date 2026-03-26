"""
Seed Chimie Première — chapitres 1-4, leçons uniquement (sans quiz).
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
"""
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
"""
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
"""
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
"""
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
                'contenu': """# Énergie de liaison et enthalpie de réaction\n\n## Énergie de liaison\n\nL'**énergie de liaison** ($E_l$) est l'énergie nécessaire pour rompre une liaison covalente entre deux atomes (exprimée en kJ·mol$^{-1}$).\n\n- Plus la liaison est forte, plus $E_l$ est élevée.\n- Pour rompre toutes les liaisons d'une mole de molécules, il faut fournir $E_l$ pour chaque liaison.\n\n## Enthalpie de réaction\n\nL'**enthalpie de réaction** ($\Delta H$) mesure l'échange d'énergie thermique à pression constante lors d'une réaction chimique :\n$$\n\Delta H = \sum E_l(\text{liaisons rompues}) - \sum E_l(\text{liaisons formées})\n$$\n\n- $\Delta H < 0$ : réaction **exothermique** (dégage de la chaleur)\n- $\Delta H > 0$ : réaction **endothermique** (absorbe de la chaleur)\n\n## Loi de Hess\n\nL'enthalpie globale d'une transformation est la somme des enthalpies des étapes élémentaires.\n\n---\n"""
            },
            {
                'ordre': 2,
                'titre': "Combustion et bilans énergétiques",
                'duree': 35,
                'contenu': """# Combustion et bilans énergétiques\n\n## Réaction de combustion\n\nLa **combustion** est une réaction chimique entre un combustible et le dioxygène ($O_2$), produisant de l'énergie thermique.\n\n**Exemples :**\n- $C + O_2 \to CO_2$\n- $CH_4 + 2O_2 \to CO_2 + 2H_2O$\n\n## Pouvoir calorifique\n\nLe **pouvoir calorifique inférieur** ($PCI$) est l'énergie libérée par la combustion complète d'une unité de masse ou de volume d'un combustible.\n\n## Bilan énergétique\n\nLe bilan énergétique global d'une réaction tient compte de toutes les énergies absorbées et libérées.\n\n- Conversion entre kJ/mol, kJ/g, kJ/L selon la nature du combustible.\n- Application de la loi de Hess pour des réactions en plusieurs étapes.\n\n---\n"""
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
                'contenu': """# Groupes caractéristiques et familles organiques\n\n## Chimie organique\n\nLa **chimie organique** étudie les composés du carbone (hors $CO_2$, $CO$, carbonates).\n\n## Squelette carboné\n\n- Chaîne linéaire, ramifiée ou cyclique\n- Atomes d'hydrogène, d'oxygène, d'azote, d'halogènes\n\n## Groupes caractéristiques\n\n- **Alcool** : $-OH$ (hydroxyle)\n- **Aldéhyde** : $-CHO$ (carbonyle terminal)\n- **Cétone** : $>C=O$ (carbonyle interne)\n- **Acide carboxylique** : $-COOH$\n- **Ester** : $-COO-$\n- **Amine** : $-NH_2$\n- **Amide** : $-CONH_2$\n\n## Familles\n\n- Alcools, aldéhydes, cétones, acides carboxyliques, esters, amines, amides\n\n---\n"""
            },
            {
                'ordre': 2,
                'titre': "Nomenclature des molécules organiques",
                'duree': 35,
                'contenu': """# Nomenclature des molécules organiques\n\n## Règles générales\n\n- Préfixe selon le nombre de carbones : méth-, éth-, prop-, but-, pent-, hex-, hept-, oct-, non-, déc-\n- Suffixe selon le groupe caractéristique :\n    - Alcane : -ane\n    - Alcool : -ol\n    - Aldéhyde : -al\n    - Cétone : -one\n    - Acide carboxylique : acide ...-oïque\n    - Ester : ...-oate d'alkyle\n    - Amine : -amine\n    - Amide : -amide\n\n## Exemples\n\n- $CH_3CH_2OH$ : éthanol\n- $CH_3COOH$ : acide éthanoïque\n- $CH_3COOCH_3$ : méthanoate de méthyle\n- $CH_3CH_2NH_2$ : éthylamine\n\n## Isomérie\n\n- **Isomérie de chaîne** : ramification différente\n- **Isomérie de position** : groupe caractéristique à un endroit différent\n- **Isomérie de fonction** : groupes caractéristiques différents\n\n---\n"""
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
                'contenu': """# Réactions d’estérification et d’hydrolyse\n\n## Estérification\n\nRéaction entre un acide carboxylique et un alcool :\n$$\n\text{Acide} + \text{Alcool} \rightleftharpoons \text{Ester} + \text{Eau}\n$$\n\n- Réaction lente, limitée par l'équilibre\n- Catalyse acide ($H^+$)\n- Taux d'estérification à l'équilibre $\approx 67\%$ pour 1 mol d'acide + 1 mol d'alcool\n\n## Hydrolyse\n\nRéaction inverse :\n$$\n\text{Ester} + \text{Eau} \rightleftharpoons \text{Acide} + \text{Alcool}\n$$\n\n- Peut être catalysée par un acide ou une base\n\n## Déplacement de l’équilibre\n\n- Excès d’un réactif\n- Élimination d’un produit\n\n---\n"""
            },
            {
                'ordre': 2,
                'titre': "Techniques de synthèse et purification",
                'duree': 35,
                'contenu': """# Techniques de synthèse et purification\n\n## Chauffage à reflux\n\nPermet de chauffer un mélange réactionnel sans perte de matière par évaporation.\n\n## Distillation\n\nSéparation des constituants selon leur température d’ébullition.\n\n## Extraction liquide-liquide\n\nUtilise deux solvants non miscibles pour séparer les produits.\n\n## Recristallisation\n\nPurification d’un solide par dissolution à chaud puis cristallisation à froid.\n\n## Lavage\n\nPermet d’éliminer les impuretés (acides, bases, solvants).\n\n## Rendement\n\n$$\nr = \frac{n_{\text{produit expérimental}}}{n_{\text{produit théorique}}} \times 100\%\n$$\n\n---\n"""
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
                'contenu': """# Dosage par étalonnage\n\n## Principe\n\nOn mesure une grandeur physique (absorbance, conductivité) pour déterminer la concentration d’une espèce en solution à l’aide d’une courbe d’étalonnage.\n\n## Courbe d’étalonnage\n\n- Préparer des solutions étalons de concentration connue\n- Mesurer la grandeur physique pour chaque étalon\n- Tracer la courbe (ex : absorbance $A$ en fonction de $C$)\n- Utiliser la courbe pour déterminer la concentration inconnue\n\n## Loi de Beer-Lambert\n\n$$\nA = \varepsilon \cdot l \cdot C\n$$\n\n- $A$ : absorbance\n- $\varepsilon$ : coefficient d’extinction molaire\n- $l$ : longueur de la cuve (cm)\n- $C$ : concentration (mol/L)\n\n---\n"""
            },
            {
                'ordre': 2,
                'titre': "Titrage direct — équivalence et calcul",
                'duree': 35,
                'contenu': """# Titrage direct — équivalence et calcul\n\n## Principe du titrage\n\nOn fait réagir une solution de concentration inconnue avec un réactif de concentration connue (titrant) jusqu’à l’équivalence.\n\n## Point d’équivalence\n\nÀ l’équivalence, les quantités de matière sont en proportions stœchiométriques :\n$$\n\frac{C_a \cdot V_a}{a} = \frac{C_b \cdot V_{b,eq}}{b}\n$$\n\n- $C_a$, $V_a$ : concentration et volume de l’espèce à doser\n- $C_b$, $V_{b,eq}$ : concentration et volume de titrant à l’équivalence\n- $a$, $b$ : coefficients stœchiométriques\n\n## Détection de l’équivalence\n\n- Changement de couleur (indicateur)\n- Saut de pH (titrage acido-basique)\n- Saut de conductivité ou de potentiel\n\n## Exploitation de la courbe de titrage\n\n- pH = f($V_{\text{titrant}}$) ou $E = f(V)$\n- L’équivalence correspond au point d’inflexion\n\n---\n"""
            },
        ],
    },
]

class Command(BaseCommand):
    help = "Recrée entièrement les chapitres 1 à 4 de Chimie Première (avec quiz pour ch.1-2)."

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
                # Quiz et questions pour chapitres 1 et 2 uniquement
                if chap_data["ordre"] in (1, 2) and "quiz" in lecon_data:
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

        self.stdout.write(self.style.SUCCESS("✅ Chimie Première (ch.1-4) recréée avec succès."))
