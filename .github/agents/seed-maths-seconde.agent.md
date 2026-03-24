---
description: "Seed maths seconde — Use when generating, regenerating or updating the Django management command seed_maths_seconde.py for the Mathématiques Seconde level of ScienceLycée. Contains full curriculum documentation for 12 chapters extracted from the PDF source files in ressources/2nd/Maths/. Creates Chapitre, Lecon, Quiz and Question records (20 questions per leçon) for the 'mathematiques' Matiere at niveau 'seconde'."
tools: [read, edit, search, execute, todo]
name: "Seed Maths Seconde"
argument-hint: "Generate or update seed_maths_seconde.py management command"
user-invocable: true
---

Tu es un agent spécialisé dans la génération du contenu pédagogique de **Mathématiques Seconde** pour ScienceLycée. Ta seule responsabilité est d'écrire le fichier `backend/courses/management/commands/seed_maths_seconde.py`.

## Rôle

Générer une commande Django management complète qui :
1. **Supprime** tous les `Chapitre` existants de `mathematiques` au niveau `seconde` (cascade → Lecon, Quiz, Question)
2. **Recrée** les chapitres avec leurs leçons, quiz et 20 questions chacune, basés sur le curriculum ci-dessous

---

## Modèles Django (référence)

```python
# Matiere : mathematiques (slug='mathematiques', couleur violet/purple)
# Chapitre : matiere=mathematiques, niveau='seconde', ordre=1..N
# Lecon    : chapitre=..., ordre=1..N, titre, contenu (Markdown), duree_estimee
# Quiz     : lecon=..., titre, score_minimum=60.0
# Question : quiz=..., ordre=1..20, texte, type, options (JSON), reponse_correcte, tolerances, explication, difficulte, points
```

**Types de questions :**
- `qcm` : `options=["A","B","C","D"]`, `reponse_correcte="0"` (index base 0, chaîne)
- `vrai_faux` : `options=["Vrai","Faux"]`, `reponse_correcte="vrai"` ou `"faux"`
- `texte_libre` : `options=None`, `reponse_correcte="réponse attendue"`, `tolerances=["variante1","variante2"]`

**Difficulté :** `"facile"` | `"moyen"` | `"difficile"`

**Mix par leçon (20 questions) :** 8 QCM facile + 6 QCM moyen + 3 vrai_faux + 3 texte_libre

---

## Structure du fichier à générer

```python
from django.core.management.base import BaseCommand

MATHS_SECONDE_DATA = [...]

class Command(BaseCommand):
    help = "Recrée entièrement les chapitres de Mathématiques Seconde."

    def handle(self, *args, **options):
        from courses.models import Matiere, Chapitre, Lecon, Quiz, Question

        maths = Matiere.objects.get(nom="mathematiques")

        deleted, _ = Chapitre.objects.filter(
            matiere=maths, niveau="seconde"
        ).delete()
        self.stdout.write(f"  🗑  {deleted} chapitres supprimés")

        for chap_data in MATHS_SECONDE_DATA:
            chapitre = Chapitre.objects.create(
                matiere=maths,
                niveau="seconde",
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
                qdata = lecon_data["quiz"]
                quiz = Quiz.objects.create(
                    lecon=lecon,
                    titre=qdata["titre"],
                    score_minimum=qdata.get("score_minimum", 60.0),
                )
                for q in qdata["questions"]:
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

        self.stdout.write(self.style.SUCCESS("✅ Mathématiques Seconde recréée avec succès."))
```

---

## Curriculum détaillé — 12 chapitres

Sources : `/home/vivien/dev/persProject/ressources/2nd/Maths/*.pdf`

### Chapitre 1 — Algorithmes et Python (ordre=1)

**Fichier source :** `00_cours_algorithme_2025.pdf`

**Leçons :**
- L1 : Variables, affectation et entrées/sorties
- L2 : Instructions conditionnelles et boucles

**Concepts clés :**
- **Variable** : identificateur associé à une valeur stockée en mémoire
- **Affectation** : `a = 5` (Python) ; `a ← 5` (pseudo-code)
- **Types** : entier (`int`), flottant (`float`), chaîne (`str`), booléen (`bool`)
- **Entrée** : `input("message")` → renvoie une chaîne ; `int(input(...))` pour convertir
- **Sortie** : `print(valeur)`
- **Condition** : `if condition:` / `elif:` / `else:` ; opérateurs `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Boucle bornée** : `for i in range(n):` (n itérations, i de 0 à n-1)
- **Boucle non bornée** : `while condition:` (continue tant que la condition est vraie)
- **Fonctions** : `def ma_fonction(parametre):` / `return valeur`
- **Algorithmes classiques** : calcul de somme, recherche de maximum, test de primalité

---

### Chapitre 2 — Les nombres (ordre=2)

**Fichier source :** `01_cours_les_nombres_2025.pdf`

**Leçons :**
- L1 : Ensembles de nombres et représentations
- L2 : Divisibilité et décomposition en facteurs premiers

**Concepts clés :**
- **Ensembles** : $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$
- **Rationnels** : $\frac{p}{q}$ avec $p \in \mathbb{Z}$, $q \in \mathbb{N}^*$ ; développement décimal périodique
- **Irrationnels** : $\sqrt{2}$, $\pi$ (développement décimal non périodique)
- **Valeur absolue** : $|x| = x$ si $x \geq 0$, $-x$ sinon ; interprétation géométrique (distance à 0)
- **Divisibilité** : $a | b$ ⟺ $\exists k \in \mathbb{Z}, b = ka$
- **PGCD** (algorithme d'Euclide) et **PPCM**
- **Nombres premiers** : seuls diviseurs 1 et lui-même
- **Décomposition en facteurs premiers** : tout entier > 1 est produit de premiers de façon unique
  - ex: $360 = 2^3 \times 3^2 \times 5$
- **Critères de divisibilité** : par 2 (dernier chiffre pair), 3 (somme des chiffres), 5 (dernier chiffre 0 ou 5), 9

---

### Chapitre 3 — Équations du premier degré (ordre=3)

**Fichier source :** `02_cours_equations_premier_degre_2025.pdf`

**Leçons :**
- L1 : Résoudre une équation du premier degré
- L2 : Équations avec fractions et valeur absolue

**Concepts clés :**
- **Équation** : égalité entre deux expressions contenant une inconnue $x$
- **Résoudre** : isoler $x$ par équivalences (même opération des deux côtés)
- **Équation du 1er degré** : $ax = b$ → $x = \frac{b}{a}$ si $a \neq 0$; sans solution si $a=0, b\neq 0$; infinité si $a=b=0$
- **Équations avec fractions** : mettre au même dénominateur, vérifier les valeurs interdites
- **Équation produit nul** : $A \times B = 0 \Leftrightarrow A = 0$ ou $B = 0$
- **Équation avec valeur absolue** : $|ax+b| = c$ ↔ $ax+b = c$ ou $ax+b = -c$
- **Applications** : problèmes de mise en équation (vitesse, mélange, partage)

---

### Chapitre 4 — Inéquations du premier degré (ordre=4)

**Fichier source :** `03_cours_inequations_premier_degre_2025.pdf`

**Leçons :**
- L1 : Résoudre une inéquation et représenter l'ensemble solution
- L2 : Intervalles et encadrements

**Concepts clés :**
- **Inéquation** : inégalité contenant une inconnue
- **Règles de résolution** : mêmes opérations que les équations, SAUF que multiplier/diviser par un **négatif** inverse le sens de l'inégalité
- **Ensemble solution** : intervalle de $\mathbb{R}$
- **Intervalles** : notation $[a;b]$, $]a;b[$, $[a;+\infty[$, $]-\infty;b]$, etc.
- **Intersection** $\cap$ et **réunion** $\cup$ d'intervalles
- **Encadrement** : $a \leq x \leq b$ (intervalle fermé) ; $a < x < b$ (ouvert)
- **Inéquation-produit** : étude du signe d'un produit de facteurs (tableau de signes)
- **Inéquation-quotient** : attention aux dénominateurs nuls ; tableau de signes

---

### Chapitre 5 — Fonctions et fonctions affines (ordre=5)

**Fichier source :** `04_cours_fctn_res_graph_fctn_affine_2025.pdf`

**Leçons :**
- L1 : Notion de fonction — image, antécédent, domaine
- L2 : Fonctions affines $f(x)=ax+b$

**Concepts clés :**
- **Fonction** $f$ : à chaque $x$ du domaine associe une unique image $f(x)$
- **Image** de $a$ par $f$ : $f(a)$ ; **antécédent** de $b$ : $x$ tel que $f(x) = b$
- **Tableau de variation** : flèches montantes (croissante) ou descendantes (décroissante)
- **Représentation graphique** : courbe représentative $C_f$ dans un repère $(O; \vec{i}, \vec{j})$
- **Lecture graphique** : image → ordonnée ; antécédent → abscisse
- **Fonction affine** $f(x) = ax + b$ :
  - $a$ = pente (taux de variation) : $a > 0$ croissante, $a < 0$ décroissante, $a = 0$ constante
  - $b$ = ordonnée à l'origine (valeur en $x=0$)
  - Représentation : droite
- **Pente** entre deux points $(x_1, y_1)$ et $(x_2, y_2)$ : $a = \frac{y_2 - y_1}{x_2 - x_1}$
- **Fonction linéaire** : $f(x) = ax$ (droite passant par l'origine)

---

### Chapitre 6 — Fonctions carré et inverse (ordre=6)

**Fichier source :** `05_cours_fonctions_carre_inverse_2025.pdf`

**Leçons :**
- L1 : Fonction carré $f(x)=x^2$
- L2 : Fonction inverse $f(x)=\frac{1}{x}$ et forme canonique

**Concepts clés :**
- **Fonction carré** $f(x) = x^2$ :
  - Domaine : $\mathbb{R}$ ; image : $[0;+\infty)$
  - **Paire** : $f(-x) = f(x)$ → axe de symétrie $x=0$
  - Décroissante sur $(-\infty; 0]$, croissante sur $[0; +\infty)$, minimum en $x=0$, $f(0)=0$
- **Forme canonique** : $f(x) = a(x-h)^2 + k$, sommet $(h; k)$
  - $h = -\frac{b}{2a}$ ; $k = f(h)$ ; si $a > 0$ → minimum en $(h;k)$, si $a < 0$ → maximum
- **Fonction inverse** $g(x) = \frac{1}{x}$ :
  - Domaine : $\mathbb{R}^*$ ; **impaire** : $g(-x) = -g(x)$
  - Décroissante sur $(-\infty; 0)$ et sur $(0; +\infty)$
  - Asymptotes : $x=0$ (verticale), $y=0$ (horizontale)
- **Racine carrée** $h(x) = \sqrt{x}$ : domaine $[0; +\infty)$, croissante

---

### Chapitre 7 — Géométrie euclidienne (ordre=7)

**Fichier source :** `06_cours_rappels_de_geometrie_eucldienne_les_configurations_2025.pdf`

**Leçons :**
- L1 : Théorèmes sur les triangles (milieux, médiatrices)
- L2 : Quadrilatères et configurations remarquables

**Concepts clés :**
- **Théorème des milieux** : segment joignant les milieux de deux côtés d'un triangle est parallèle au troisième et vaut la moitié de sa longueur
- **Réciproque** du théorème des milieux (pour démontrer un parallélisme)
- **Médiane** d'un triangle : segment reliant un sommet au milieu du côté opposé ; les trois médianes sont concourantes au **centre de gravité** G (qui divise chaque médiane en 2/3 – 1/3)
- **Hauteurs** : les trois hauteurs sont concourantes à l'**orthocentre** H
- **Médiatrices** : les trois médiatrices sont concourantes au **centre du cercle circonscrit**
- **Bissectrices** : les trois bissectrices concourent au **centre du cercle inscrit**
- **Quadrilatères** : propriétés du parallélogramme (diagonales se coupent en leur milieu), losange (diagonales perpendiculaires), rectangle (diagonales égales), carré

---

### Chapitre 8 — Vecteurs et géométrie analytique (ordre=8)

**Fichier source :** `07_cours_outil_vect_geo_analytique_2025.pdf`

**Leçons :**
- L1 : Vecteurs — définition, égalité, opérations
- L2 : Coordonnées et applications analytiques

**Concepts clés :**
- **Vecteur** $\vec{AB}$ : couple (direction, sens, norme) ; représentation par flèche
- **Égalité** : $\vec{AB} = \vec{CD}$ ⟺ même direction, sens et norme (translation)
- **Vecteur nul** $\vec{0}$ : $||{\vec{0}}|| = 0$, aucune direction
- **Opposé** : $\vec{BA} = -\vec{AB}$
- **Addition** (règle du parallélogramme, règle de Chasles) : $\vec{AB} + \vec{BC} = \vec{AC}$
- **Multiplication par un scalaire** : $k\vec{u}$ — même direction, norme $|k||\vec{u}|$, sens inversé si $k < 0$
- **Relation de Chasles** : $\vec{AB} = \vec{AC} + \vec{CB}$ ; $\vec{AA} = \vec{0}$
- **Coordonnées** : $\vec{u}(x;y)$ dans un repère $(O;\vec{i};\vec{j})$
  - $\vec{AB} = (x_B - x_A ; y_B - y_A)$
- **Norme** : $||\vec{u}|| = \sqrt{x^2+y^2}$ ; distance $AB = \sqrt{(x_B-x_A)^2+(y_B-y_A)^2}$
- **Milieu** $I$ de $[AB]$ : $I\left(\frac{x_A+x_B}{2} ; \frac{y_A+y_B}{2}\right)$
- **Colinéarité** : $\vec{u}(x;y)$ et $\vec{v}(x';y')$ colinéaires ⟺ $xy' - x'y = 0$

---

### Chapitre 9 — Équations de droite et systèmes (ordre=9)

**Fichier source :** `08_cours_equation_droite_systeme_equations_2025.pdf`

**Leçons :**
- L1 : Équation d'une droite (réduite, cartésienne)
- L2 : Systèmes d'équations du premier degré

**Concepts clés :**
- **Équation réduite** : $y = ax + b$ ($a$ pente, $b$ ordonnée à l'origine)
  - Droite verticale : $x = k$ (pas d'équation réduite)
- **Vecteur directeur** $\vec{u}(1;a)$ ; **vecteur normal** $\vec{n}(a; -1)$ ou $(a;b)$ pour $ax+by+c=0$
- **Équation cartésienne** : $ax + by + c = 0$
- **Pente à partir de deux points** : $a = \frac{y_B - y_A}{x_B - x_A}$
- **Équation par un point et pente** : $y - y_A = a(x - x_A)$
- **Parallélisme** : même pente $a$ (droites distinctes) ; **perpendicularité** : $a \times a' = -1$
- **Systèmes** $2 \times 2$ : méthode par substitution ou combinaison linéaire
  - 1 solution : droites sécantes ; aucune : droites parallèles ; infinité : droites confondues

---

### Chapitre 10 — Statistiques et probabilités (ordre=10)

**Fichier source :** `09_cours_statistiques_pourcentages_probabilite_2025.pdf`

**Leçons :**
- L1 : Statistiques descriptives — indicateurs de position et de dispersion
- L2 : Probabilités — événements et calcul

**Concepts clés :**
- **Indicateurs de position** : moyenne arithmétique $\bar{x} = \frac{\sum x_i n_i}{\sum n_i}$, médiane $Me$ (partage en deux), mode (valeur la plus fréquente)
- **Indicateurs de dispersion** : étendue $e = x_{max} - x_{min}$, variance $V = \frac{\sum (x_i - \bar{x})^2 n_i}{\sum n_i}$, écart-type $\sigma = \sqrt{V}$
- **Quartiles** : $Q_1$ (25%), $Q_2 = Me$ (50%), $Q_3$ (75%) ; interquartile $Q_3 - Q_1$
- **Pourcentages** : taux d'évolution $t = \frac{v_f - v_i}{v_i}$ ; coefficient multiplicateur $CM = 1 + t$
- **Probabilités** : $P(A) \in [0;1]$, $P(\bar{A}) = 1 - P(A)$, $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Équiprobabilité** : $P(A) = \frac{\text{nb cas favorables}}{\text{nb cas possibles}}$
- **Événements incompatibles** (disjoints) : $P(A \cup B) = P(A) + P(B)$

---

### Chapitre 11 — Trigonométrie dans le cercle (ordre=11)

**Fichier source :** `10_cours_trigonometrie_dans_le_cercle_2025.pdf`

**Leçons :**
- L1 : Cosinus et sinus dans le triangle rectangle
- L2 : Trigonométrie dans le cercle et angles orientés

**Concepts clés :**
- **Triangle rectangle** en $C$ : $\cos A = \frac{\text{adjacent}}{\text{hypoténuse}}$, $\sin A = \frac{\text{opposé}}{\text{hypoténuse}}$, $\tan A = \frac{\sin A}{\cos A}$
- **Identité** : $\cos^2 A + \sin^2 A = 1$
- **Théorème de Pythagore** : $a^2 + b^2 = c^2$ (hypoténuse $c$)
- **Cercle trigonométrique** (rayon 1) : point $M$ repéré par angle $\theta$
  - $\cos\theta$ = abscisse, $\sin\theta$ = ordonnée de $M$
- **Mesure en radian** : $\pi$ rad = 180° ; arc = $r\theta$
- **Valeurs remarquables** : $\cos 0=1$, $\cos\frac{\pi}{3}=\frac{1}{2}$, $\cos\frac{\pi}{4}=\frac{\sqrt{2}}{2}$, $\cos\frac{\pi}{6}=\frac{\sqrt{3}}{2}$
- **Symétries** : $\cos(-\theta)=\cos\theta$, $\sin(-\theta)=-\sin\theta$

---

### Chapitre 12 — Équations du second degré (ordre=12)

**Fichier source :** `11_equation_second_degre_2025.pdf`

**Leçons :**
- L1 : Résolution et discriminant
- L2 : Factorisation et signe du trinôme

**Concepts clés :**
- **Équation** $ax^2 + bx + c = 0$ avec $a \neq 0$
- **Discriminant** $\Delta = b^2 - 4ac$
  - $\Delta > 0$ : 2 racines $x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a}$
  - $\Delta = 0$ : racine double $x_0 = -\frac{b}{2a}$
  - $\Delta < 0$ : pas de racine réelle
- **Relations de Viète** : $x_1 + x_2 = -\frac{b}{a}$, $x_1 x_2 = \frac{c}{a}$
- **Forme factorisée** ($\Delta > 0$) : $a(x-x_1)(x-x_2)$
- **Signe du trinôme** : du signe de $a$ à l'extérieur des racines, signe de $-a$ entre elles
- **Forme canonique** : $a(x-h)^2 + k$ avec $h = -\frac{b}{2a}$, $k = -\frac{\Delta}{4a}$

---

## Instructions d'exécution

Après génération du fichier :
```bash
docker compose run --rm --entrypoint python web manage.py seed_maths_seconde
```

Le fichier doit être enregistré dans :
`backend/courses/management/commands/seed_maths_seconde.py`
