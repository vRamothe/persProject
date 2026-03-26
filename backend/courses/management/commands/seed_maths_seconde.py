"""
Seed Mathématiques Seconde — 12 chapitres, leçons uniquement (sans quiz).
Usage : python manage.py seed_maths_seconde
"""

from django.core.management.base import BaseCommand
from courses.models import Matiere, Chapitre, Lecon, Quiz, Question

CHAPITRES = [
    # ──────────────────────────────────────────────
    # CHAPITRE 1 — Algorithmes et Python
    # ──────────────────────────────────────────────
    {
        'ordre': 1,
        'titre': 'Algorithmes et Python',
        'description': "Découverte de l'algorithmique et de la programmation en Python : variables, conditions, boucles et fonctions.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Variables, affectation et entrées/sorties',
                'duree': 30,
                'contenu': """# Variables, affectation et entrées/sorties

## Qu'est-ce qu'un algorithme ?

Un **algorithme** est une suite finie d'instructions précises permettant de résoudre un problème ou d'effectuer un calcul. On peut le comparer à une recette de cuisine : chaque étape est clairement décrite et s'exécute dans un ordre donné.

En informatique, on traduit un algorithme en **programme** grâce à un langage de programmation. En classe de Seconde, nous utilisons **Python**.

---

## Les variables

### Définition

Une **variable** est un nom (un identifiant) associé à une valeur stockée dans la mémoire de l'ordinateur. On peut voir une variable comme une **boîte étiquetée** dans laquelle on range une donnée.

### Règles de nommage en Python

- Un nom de variable commence par une **lettre** ou un **underscore** `_`.
- Il ne peut contenir que des lettres, chiffres et underscores.
- Python est **sensible à la casse** : `age` et `Age` sont deux variables différentes.
- On évite les accents et les mots réservés (`if`, `for`, `while`, etc.).

> **Bonne pratique :** choisir des noms explicites. Préférer `note_eleve` à `n`.

---

## L'affectation

L'**affectation** consiste à donner une valeur à une variable.

**En pseudo-code :**

```
a ← 5
```

**En Python :**

```python
a = 5
```

> ⚠️ Le signe `=` en Python est l'opérateur d'**affectation**, pas l'égalité mathématique. L'égalité mathématique se teste avec `==`.

### Affectations successives

Quand on affecte une nouvelle valeur à une variable, l'ancienne valeur est **remplacée** :

```python
x = 10
x = x + 3   # x vaut maintenant 13
```

| Instruction | Valeur de `x` |
|-------------|---------------|
| `x = 10`   | 10            |
| `x = x + 3`| 13            |
| `x = x * 2`| 26            |

---

## Les types de données

Python gère automatiquement le **type** d'une variable. Les principaux types sont :

| Type      | Nom Python | Exemple          |
|-----------|------------|------------------|
| Entier    | `int`      | `42`, `-7`       |
| Décimal   | `float`    | `3.14`, `-0.5`   |
| Chaîne    | `str`      | `"Bonjour"`      |
| Booléen   | `bool`     | `True`, `False`  |

On peut vérifier le type d'une variable avec la fonction `type()` :

```python
x = 3.14
print(type(x))   # <class 'float'>
```

---

## Les entrées : `input()`

La fonction `input()` permet de demander une valeur à l'utilisateur. Elle renvoie **toujours une chaîne de caractères** (`str`).

```python
prenom = input("Quel est ton prénom ? ")
print("Bonjour", prenom)
```

Pour obtenir un nombre, il faut **convertir** la chaîne :

```python
age = int(input("Quel âge as-tu ? "))     # entier
taille = float(input("Ta taille en m ? ")) # décimal
```

> ⚠️ Si l'utilisateur tape autre chose qu'un nombre, la conversion échoue et le programme provoque une erreur.

---

## Les sorties : `print()`

La fonction `print()` affiche un ou plusieurs éléments à l'écran :

```python
nom = "Alice"
note = 17.5
print("Élève :", nom, "— Note :", note)
```

Résultat : `Élève : Alice — Note : 17.5`

### Les f-strings (chaînes formatées)

Depuis Python 3.6, on peut insérer des expressions directement dans une chaîne :

```python
rayon = 5
aire = 3.14159 * rayon ** 2
print(f"L'aire du cercle de rayon {rayon} est {aire:.2f}")
```

Résultat : `L'aire du cercle de rayon 5 est 78.54`

---

## Les opérations arithmétiques

| Opérateur | Signification       | Exemple           | Résultat |
|-----------|---------------------|-------------------|----------|
| `+`       | Addition            | `7 + 3`           | `10`     |
| `-`       | Soustraction        | `7 - 3`           | `4`      |
| `*`       | Multiplication      | `7 * 3`           | `21`     |
| `/`       | Division décimale   | `7 / 3`           | `2.333…` |
| `//`      | Division entière    | `7 // 3`          | `2`      |
| `%`       | Modulo (reste)      | `7 % 3`           | `1`      |
| `**`      | Puissance           | `2 ** 10`         | `1024`   |

> **Astuce :** pour tester si un nombre $n$ est pair, on vérifie `n % 2 == 0`.

---

## Exemple complet

Voici un programme qui calcule l'aire d'un rectangle à partir des dimensions saisies par l'utilisateur :

```python
longueur = float(input("Longueur du rectangle : "))
largeur = float(input("Largeur du rectangle : "))

aire = longueur * largeur
perimetre = 2 * (longueur + largeur)

print(f"Aire = {aire} unités²")
print(f"Périmètre = {perimetre} unités")
```

---

## À retenir

- Une **variable** stocke une valeur en mémoire ; l'**affectation** (`=`) lui donne sa valeur.
- `input()` lit une **chaîne** depuis le clavier ; `int()` ou `float()` convertissent en nombre.
- `print()` affiche des résultats à l'écran.
- Python distingue quatre types fondamentaux : `int`, `float`, `str`, `bool`.
""",
                'quiz': {
                    'titre': "Quiz — Variables, affectation et entrées/sorties",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Qu'est-ce qu'une variable en Python ?",
                            'options': ["Un nom associé à une valeur en mémoire", "Une opération mathématique", "Un type de boucle", "Une fonction intégrée"],
                            'reponse_correcte': '0',
                            'explication': "Une variable est un identifiant (un nom) associé à une valeur stockée dans la mémoire de l'ordinateur.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Quel est le résultat de l'instruction a = 7 en Python ?",
                            'options': ["La variable a reçoit la valeur 7", "On teste si a est égal à 7", "On affiche 7", "On crée une fonction a"],
                            'reponse_correcte': '0',
                            'explication': "Le signe = en Python est l'opérateur d'affectation : il attribue la valeur 7 à la variable a.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Quel est le type de la valeur 3.14 en Python ?",
                            'options': ["float", "int", "str", "bool"],
                            'reponse_correcte': '0',
                            'explication': "3.14 est un nombre décimal (à virgule flottante), donc de type float.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Que renvoie la fonction input() en Python ?",
                            'options': ["Toujours une chaîne de caractères (str)", "Un entier (int)", "Un nombre décimal (float)", "Un booléen (bool)"],
                            'reponse_correcte': '0',
                            'explication': "La fonction input() renvoie toujours une chaîne de caractères, même si l'utilisateur tape un nombre.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Quel opérateur permet de calculer le reste de la division euclidienne en Python ?",
                            'options': ["%", "//", "/", "**"],
                            'reponse_correcte': '0',
                            'explication': "L'opérateur % (modulo) donne le reste de la division euclidienne. Par exemple, 7 % 3 = 1.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'vrai_faux',
                            'texte': "En Python, le signe = est l'opérateur d'égalité mathématique.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le signe = est l'opérateur d'affectation. L'égalité mathématique se teste avec ==.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'vrai_faux',
                            'texte': "En Python, les noms de variables sont sensibles à la casse : age et Age sont deux variables différentes.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Python distingue les majuscules des minuscules. age, Age et AGE sont trois variables différentes.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'texte_libre',
                            'texte': "Quelle fonction Python permet d'afficher du texte à l'écran ?",
                            'options': None,
                            'reponse_correcte': 'print',
                            'tolerances': ["print()"],
                            'explication': "La fonction print() affiche un ou plusieurs éléments à l'écran.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Que vaut 7 // 3 en Python ?",
                            'options': ["2", "2.33", "1", "3"],
                            'reponse_correcte': '0',
                            'explication': "L'opérateur // effectue la division entière. 7 // 3 = 2 (le quotient sans la partie décimale).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "On exécute x = 5 puis x = x + 3. Que vaut x ?",
                            'options': ["8", "5", "3", "53"],
                            'reponse_correcte': '0',
                            'explication': "x reçoit d'abord 5, puis x + 3 = 5 + 3 = 8. L'ancienne valeur est remplacée.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Comment convertir la chaîne \"42\" en entier en Python ?",
                            'options': ['int("42")', 'str(42)', 'float("42")', 'bool("42")'],
                            'reponse_correcte': '0',
                            'explication': "La fonction int() convertit une chaîne de caractères représentant un nombre entier en type int.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Quel est le résultat de 2 ** 4 en Python ?",
                            'options': ["16", "8", "6", "24"],
                            'reponse_correcte': '0',
                            'explication': "L'opérateur ** calcule la puissance. 2 ** 4 = 2⁴ = 16.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Quelle est la valeur de type(True) en Python ?",
                            'options': ["<class 'bool'>", "<class 'int'>", "<class 'str'>", "<class 'float'>"],
                            'reponse_correcte': '0',
                            'explication': "True est une valeur booléenne, son type est bool.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "L'instruction n = int(input('Entrez un nombre : ')) permet de stocker un entier saisi par l'utilisateur dans la variable n.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "input() renvoie une chaîne, puis int() la convertit en entier. Le résultat est stocké dans la variable n.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'texte_libre',
                            'texte': "Que vaut 10 % 3 en Python ? (répondre par un nombre)",
                            'options': None,
                            'reponse_correcte': '1',
                            'tolerances': ["1"],
                            'explication': "10 = 3 × 3 + 1, donc le reste de la division euclidienne de 10 par 3 est 1.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'texte_libre',
                            'texte': "Quel est le type Python d'une variable contenant la valeur \"Bonjour\" ? (répondre en un mot)",
                            'options': None,
                            'reponse_correcte': 'str',
                            'tolerances': ["string", "chaine", "chaîne"],
                            'explication': "\"Bonjour\" est entouré de guillemets, c'est donc une chaîne de caractères (str).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "On exécute : a = 2, b = a, a = 5. Que vaut b ?",
                            'options': ["2", "5", "a", "Erreur"],
                            'reponse_correcte': '0',
                            'explication': "b reçoit la valeur de a au moment de l'affectation (c'est-à-dire 2). Modifier ensuite a ne change pas b.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'qcm',
                            'texte': "Que se passe-t-il si on exécute int('abc') en Python ?",
                            'options': ["Une erreur (ValueError)", "On obtient 0", "On obtient 'abc'", "On obtient False"],
                            'reponse_correcte': '0',
                            'explication': "'abc' ne représente pas un nombre entier, donc int('abc') provoque une erreur de type ValueError.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'vrai_faux',
                            'texte': "En Python, 10 / 3 donne un résultat de type int.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "L'opérateur / effectue une division décimale et renvoie toujours un float. Pour obtenir un entier, il faut utiliser //.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Que vaut 17 % 5 en Python ? (répondre par un nombre)",
                            'options': None,
                            'reponse_correcte': '2',
                            'tolerances': ["2"],
                            'explication': "17 = 5 × 3 + 2, donc le reste de la division euclidienne de 17 par 5 est 2.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Instructions conditionnelles et boucles',
                'duree': 35,
                'contenu': """# Instructions conditionnelles et boucles

## Les instructions conditionnelles

### Le `if`

L'instruction `if` (« si ») permet d'exécuter un bloc de code **uniquement si une condition est vraie** :

```python
age = int(input("Ton âge : "))
if age >= 18:
    print("Tu es majeur.")
```

> **Attention à l'indentation !** En Python, le bloc de code à l'intérieur d'un `if` doit être **indenté** (décalé de 4 espaces).

### Le `if … else`

On peut ajouter un bloc `else` (« sinon ») exécuté lorsque la condition est **fausse** :

```python
note = float(input("Ta note : "))
if note >= 10:
    print("Bravo, tu as la moyenne !")
else:
    print("Courage, il faut réviser.")
```

### Le `if … elif … else`

Pour tester plusieurs conditions en chaîne, on utilise `elif` (contraction de « else if ») :

```python
note = float(input("Ta note : "))
if note >= 16:
    print("Très bien !")
elif note >= 14:
    print("Bien !")
elif note >= 10:
    print("Assez bien.")
else:
    print("Il faut retravailler.")
```

> Les conditions sont évaluées **de haut en bas**. Dès qu'une condition est vraie, le bloc correspondant s'exécute et les autres sont ignorés.

---

## Les opérateurs de comparaison

| Opérateur | Signification       | Exemple        |
|-----------|---------------------|----------------|
| `==`      | Égal à              | `x == 5`       |
| `!=`      | Différent de        | `x != 0`       |
| `<`       | Strictement inférieur | `x < 10`     |
| `>`       | Strictement supérieur | `x > 0`      |
| `<=`      | Inférieur ou égal   | `x <= 20`      |
| `>=`      | Supérieur ou égal   | `x >= 10`      |

### Les opérateurs logiques

On peut combiner plusieurs conditions avec `and`, `or` et `not` :

```python
age = 16
if age >= 12 and age < 18:
    print("Tu es adolescent.")
```

| Opérateur | Signification              |
|-----------|----------------------------|
| `and`     | Vrai si **les deux** conditions sont vraies |
| `or`      | Vrai si **au moins une** condition est vraie |
| `not`     | Inverse la condition       |

---

## La boucle `for` (boucle bornée)

La boucle `for` répète un bloc d'instructions un **nombre déterminé** de fois.

### La fonction `range()`

```python
for i in range(5):
    print(i)
# Affiche : 0, 1, 2, 3, 4
```

| Appel               | Valeurs produites        |
|---------------------|--------------------------|
| `range(n)`          | $0, 1, 2, \\ldots, n-1$  |
| `range(a, b)`       | $a, a+1, \\ldots, b-1$   |
| `range(a, b, pas)`  | $a, a+\\text{pas}, a+2\\text{pas}, \\ldots$ (tant que < $b$) |

### Exemple : calcul d'une somme

Calculons $S = 1 + 2 + 3 + \\cdots + 100$ :

```python
S = 0
for i in range(1, 101):
    S = S + i
print(f"La somme vaut {S}")   # 5050
```

> On retrouve la formule : $S = \\frac{n(n+1)}{2} = \\frac{100 \\times 101}{2} = 5050$.

---

## La boucle `while` (boucle non bornée)

La boucle `while` (« tant que ») répète un bloc **tant qu'une condition est vraie**. On ne connaît pas à l'avance le nombre de répétitions.

```python
n = 1
while n <= 10:
    print(n)
    n = n + 1
```

> ⚠️ Il faut s'assurer que la condition finira par devenir fausse, sinon le programme tourne **indéfiniment** (boucle infinie).

### Exemple : recherche du plus petit $n$ tel que $2^n > 1000$

```python
n = 0
while 2 ** n <= 1000:
    n = n + 1
print(f"Le plus petit n tel que 2^n > 1000 est n = {n}")
# Résultat : n = 10 (car 2^10 = 1024 > 1000)
```

---

## Les fonctions

### Définir une fonction

Une **fonction** regroupe un bloc d'instructions que l'on peut appeler plusieurs fois :

```python
def saluer(prenom):
    print(f"Bonjour {prenom} !")

saluer("Alice")    # Affiche : Bonjour Alice !
saluer("Bob")      # Affiche : Bonjour Bob !
```

### Le mot-clé `return`

Une fonction peut **renvoyer** une valeur grâce à `return` :

```python
def carre(x):
    return x ** 2

resultat = carre(7)
print(resultat)   # 49
```

> Après un `return`, l'exécution de la fonction s'arrête immédiatement.

### Fonction à plusieurs paramètres

```python
def aire_rectangle(longueur, largeur):
    return longueur * largeur

print(aire_rectangle(5, 3))   # 15
```

---

## Algorithmes classiques

### Recherche du maximum dans une liste

```python
def maximum(liste):
    maxi = liste[0]
    for element in liste:
        if element > maxi:
            maxi = element
    return maxi

notes = [12, 17, 8, 15, 20, 11]
print(f"La meilleure note est {maximum(notes)}")   # 20
```

### Test de primalité

Un nombre $n \\geq 2$ est **premier** s'il n'est divisible que par 1 et par lui-même :

```python
def est_premier(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(est_premier(17))   # True
print(est_premier(15))   # False
```

---

## À retenir

- **`if` / `elif` / `else`** : exécuter du code selon une condition.
- **`for i in range(n):`** : répéter $n$ fois (boucle bornée).
- **`while condition:`** : répéter tant que la condition est vraie (boucle non bornée).
- **`def` / `return`** : définir une fonction réutilisable.
- Toujours penser à **indenter** le code à l'intérieur des blocs.
""",
                'quiz': {
                    'titre': "Quiz — Instructions conditionnelles et boucles",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quel mot-clé Python introduit une condition ?",
                            'options': ["if", "for", "def", "while"],
                            'reponse_correcte': '0',
                            'explication': "Le mot-clé if (« si ») permet de tester une condition et d'exécuter un bloc de code si elle est vraie.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Que signifie l'opérateur != en Python ?",
                            'options': ["Différent de", "Égal à", "Inférieur à", "Supérieur à"],
                            'reponse_correcte': '0',
                            'explication': "L'opérateur != teste si deux valeurs sont différentes. Par exemple, 3 != 5 est True.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Combien de fois s'exécute la boucle for i in range(5) ?",
                            'options': ["5 fois", "4 fois", "6 fois", "1 fois"],
                            'reponse_correcte': '0',
                            'explication': "range(5) produit les valeurs 0, 1, 2, 3, 4, soit 5 itérations.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quel mot-clé permet de renvoyer une valeur depuis une fonction ?",
                            'options': ["return", "print", "def", "input"],
                            'reponse_correcte': '0',
                            'explication': "Le mot-clé return renvoie une valeur et termine l'exécution de la fonction.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Quelle est la première valeur produite par range(3) ?",
                            'options': ["0", "1", "3", "-1"],
                            'reponse_correcte': '0',
                            'explication': "range(n) commence toujours à 0. Ainsi range(3) produit 0, 1, 2.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'vrai_faux',
                            'texte': "Le bloc de code à l'intérieur d'un if doit être indenté en Python.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "En Python, l'indentation (généralement 4 espaces) est obligatoire pour délimiter les blocs de code.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'vrai_faux',
                            'texte': "La boucle while est une boucle bornée dont on connaît le nombre d'itérations à l'avance.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La boucle while est une boucle non bornée : elle se répète tant que la condition est vraie. La boucle for est la boucle bornée.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'texte_libre',
                            'texte': "Quel mot-clé Python permet de définir une fonction ?",
                            'options': None,
                            'reponse_correcte': 'def',
                            'tolerances': ["def"],
                            'explication': "On définit une fonction en Python avec le mot-clé def suivi du nom de la fonction et de ses paramètres.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Soit x = 15. Avec les conditions : if x > 20 → affiche 'A', elif x > 10 → affiche 'B', else → affiche 'C'. Qu'est-ce qui s'affiche ?",
                            'options': ["B", "A", "C", "A et B"],
                            'reponse_correcte': '0',
                            'explication': "x = 15 : la première condition x > 20 est fausse, la seconde x > 10 est vraie, donc on affiche 'B'.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "On exécute S = 0, puis for i in range(1, 5): S = S + i. Que vaut S ?",
                            'options': ["10", "15", "6", "4"],
                            'reponse_correcte': '0',
                            'explication': "range(1, 5) produit 1, 2, 3, 4. La somme est S = 1 + 2 + 3 + 4 = 10.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Que fait l'opérateur and entre deux conditions ?",
                            'options': ["Renvoie True si les deux conditions sont vraies", "Renvoie True si au moins une condition est vraie", "Inverse la condition", "Compare deux nombres"],
                            'reponse_correcte': '0',
                            'explication': "L'opérateur and (« et ») renvoie True uniquement si les deux conditions sont simultanément vraies.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Quelles valeurs produit range(2, 10, 3) ?",
                            'options': ["2, 5, 8", "2, 5, 8, 11", "3, 6, 9", "2, 4, 6, 8"],
                            'reponse_correcte': '0',
                            'explication': "range(2, 10, 3) commence à 2, avance de 3 en 3, et s'arrête avant 10 : 2, 5, 8.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "On définit def carre(x): return x ** 2. Que renvoie carre(5) ?",
                            'options': ["25", "10", "5", "32"],
                            'reponse_correcte': '0',
                            'explication': "La fonction calcule x ** 2 = 5² = 25.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "L'instruction for i in range(0, 10, 2) parcourt les nombres pairs de 0 à 8.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "range(0, 10, 2) produit 0, 2, 4, 6, 8 — ce sont bien les nombres pairs de 0 à 8 (10 exclu).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'texte_libre',
                            'texte': "Combien de fois s'exécute la boucle for i in range(1, 8) ? (répondre par un nombre)",
                            'options': None,
                            'reponse_correcte': '7',
                            'tolerances': ["7 fois", "sept"],
                            'explication': "range(1, 8) produit les valeurs 1, 2, 3, 4, 5, 6, 7, soit 7 itérations (8 est exclu).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'texte_libre',
                            'texte': "On exécute n = 0, puis while 2**n <= 1000: n = n + 1. Quelle est la valeur finale de n ?",
                            'options': None,
                            'reponse_correcte': '10',
                            'tolerances': ["10", "dix"],
                            'explication': "La boucle incrémente n tant que 2^n ≤ 1000. On a 2^9 = 512 ≤ 1000 et 2^10 = 1024 > 1000, donc n = 10.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "On définit def f(a, b): return a + b. Que vaut f(3, 4) * 2 ?",
                            'options': ["14", "7", "34", "Erreur"],
                            'reponse_correcte': '0',
                            'explication': "f(3, 4) renvoie 3 + 4 = 7, puis 7 × 2 = 14.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'qcm',
                            'texte': "On exécute compteur = 0, puis for i in range(100): if i % 2 == 0: compteur += 1. Que vaut compteur ?",
                            'options': ["50", "100", "49", "51"],
                            'reponse_correcte': '0',
                            'explication': "range(100) produit 0 à 99. Les nombres pairs sont 0, 2, 4, …, 98, soit 50 nombres.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'vrai_faux',
                            'texte': "Si une fonction ne contient pas de return, elle renvoie automatiquement None.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "En Python, une fonction sans return (ou avec un return sans valeur) renvoie implicitement None.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "On exécute S = 0, puis for i in range(1, 6): S = S + i**2. Que vaut S ?",
                            'options': None,
                            'reponse_correcte': '55',
                            'tolerances': ["55"],
                            'explication': "S = 1² + 2² + 3² + 4² + 5² = 1 + 4 + 9 + 16 + 25 = 55.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },

    # ──────────────────────────────────────────────
    # CHAPITRE 2 — Les nombres
    # ──────────────────────────────────────────────
    {
        'ordre': 2,
        'titre': 'Les nombres',
        'description': "Ensembles de nombres, valeur absolue, divisibilité, nombres premiers et décomposition en facteurs premiers.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Ensembles de nombres et représentations',
                'duree': 30,
                'contenu': """# Ensembles de nombres et représentations

## Les grands ensembles de nombres

En mathématiques, les nombres sont classés dans des **ensembles** emboîtés les uns dans les autres :

$$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}$$

### L'ensemble $\\mathbb{N}$ — Les entiers naturels

$$\\mathbb{N} = \\{0,\\; 1,\\; 2,\\; 3,\\; \\ldots\\}$$

Ce sont les nombres entiers **positifs ou nuls**. On les utilise pour compter.

### L'ensemble $\\mathbb{Z}$ — Les entiers relatifs

$$\\mathbb{Z} = \\{\\ldots,\\; -3,\\; -2,\\; -1,\\; 0,\\; 1,\\; 2,\\; 3,\\; \\ldots\\}$$

$\\mathbb{Z}$ contient tous les entiers, positifs **et négatifs**. On a : $\\mathbb{N} \\subset \\mathbb{Z}$.

### L'ensemble $\\mathbb{Q}$ — Les nombres rationnels

$$\\mathbb{Q} = \\left\\{\\frac{p}{q} \\;\\middle|\\; p \\in \\mathbb{Z},\\; q \\in \\mathbb{N}^* \\right\\}$$

Un nombre est **rationnel** s'il peut s'écrire comme une fraction d'entiers. Tout entier est rationnel (par exemple $3 = \\frac{3}{1}$).

> **Propriété :** Un nombre est rationnel **si et seulement si** son écriture décimale est **finie** ou **périodique**.

**Exemples :**
- $\\frac{1}{3} = 0{,}333\\ldots = 0{,}\\overline{3}$ (période : 3)
- $\\frac{7}{4} = 1{,}75$ (écriture décimale finie)
- $\\frac{1}{7} = 0{,}\\overline{142857}$ (période de longueur 6)

### L'ensemble $\\mathbb{R}$ — Les nombres réels

$\\mathbb{R}$ contient **tous** les nombres qui peuvent être placés sur une droite graduée. Il comprend les rationnels et les **irrationnels**.

---

## Les nombres irrationnels

Un nombre **irrationnel** est un nombre réel qui **n'est pas rationnel** : il ne peut pas s'écrire sous forme de fraction et son écriture décimale est **infinie et non périodique**.

**Exemples célèbres :**

| Nombre       | Valeur approchée       |
|-------------|------------------------|
| $\\sqrt{2}$  | $1{,}41421356\\ldots$  |
| $\\sqrt{3}$  | $1{,}73205080\\ldots$  |
| $\\pi$       | $3{,}14159265\\ldots$  |

> **Théorème :** $\\sqrt{2}$ est irrationnel. Cela se démontre par l'absurde (on suppose $\\sqrt{2} = \\frac{p}{q}$ irréductible et on aboutit à une contradiction).

### Règle pratique

$\\sqrt{n}$ est rationnel **si et seulement si** $n$ est un **carré parfait** ($1, 4, 9, 16, 25, \\ldots$).

---

## La valeur absolue

### Définition

La **valeur absolue** d'un nombre réel $x$, notée $|x|$, est définie par :

$$|x| = \\begin{cases} x & \\text{si } x \\geq 0 \\\\ -x & \\text{si } x < 0 \\end{cases}$$

**Exemples :** $|5| = 5$, $|-3| = 3$, $|0| = 0$.

### Interprétation géométrique

$|x|$ représente la **distance** entre le point $x$ et l'origine 0 sur la droite des réels.

Plus généralement, $|a - b|$ est la **distance** entre les points $a$ et $b$ :

$$d(a, b) = |a - b|$$

> **Exemple :** la distance entre $-2$ et $5$ vaut $|-2 - 5| = |-7| = 7$.

### Propriétés

Pour tous réels $a$ et $b$ :

- $|a| \\geq 0$ et $|a| = 0 \\Leftrightarrow a = 0$
- $|ab| = |a| \\times |b|$
- $|a + b| \\leq |a| + |b|$ (inégalité triangulaire)

---

## Droite graduée et repérage

Chaque nombre réel correspond à un **unique** point sur une droite graduée (droite des réels).

- L'**abscisse** d'un point sur cette droite est le nombre réel qui lui est associé.
- La longueur du segment $[A; B]$ où $A$ a pour abscisse $a$ et $B$ a pour abscisse $b$ est $|b - a|$.

---

## À retenir

- $\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}$ : chaque ensemble « contient » le précédent.
- Un nombre est **rationnel** si son écriture décimale est finie ou périodique.
- Un nombre **irrationnel** a une écriture décimale infinie non périodique (ex : $\\sqrt{2}$, $\\pi$).
- La **valeur absolue** $|x|$ donne la distance à zéro ; $|a-b|$ donne la distance entre $a$ et $b$.
""",
                'quiz': {
                    'titre': "Quiz — Ensembles de nombres et représentations",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quel ensemble contient les entiers naturels 0, 1, 2, 3, … ?",
                            'options': ["ℕ", "ℤ", "ℚ", "ℝ"],
                            'reponse_correcte': '0',
                            'explication': "ℕ est l'ensemble des entiers naturels : 0, 1, 2, 3, …",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Le nombre −5 appartient à quel plus petit ensemble de nombres ?",
                            'options': ["ℤ", "ℕ", "ℚ uniquement", "ℝ uniquement"],
                            'reponse_correcte': '0',
                            'explication': "−5 est un entier négatif. Il appartient à ℤ (entiers relatifs) mais pas à ℕ (entiers naturels).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Quelle est la valeur absolue de −7 ?",
                            'options': ["7", "−7", "0", "14"],
                            'reponse_correcte': '0',
                            'explication': "|−7| = 7 car la valeur absolue d'un nombre négatif est son opposé.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Un nombre rationnel peut s'écrire sous la forme :",
                            'options': ["p/q avec p entier et q entier non nul", "Uniquement comme un entier", "Un nombre dont l'écriture décimale est infinie non périodique", "Un nombre toujours négatif"],
                            'reponse_correcte': '0',
                            'explication': "Un nombre rationnel est un nombre qui peut s'écrire comme fraction p/q avec p ∈ ℤ et q ∈ ℕ*.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Quelle est la distance entre les points d'abscisses 3 et 8 sur la droite des réels ?",
                            'options': ["5", "11", "−5", "24"],
                            'reponse_correcte': '0',
                            'explication': "La distance est |8 − 3| = |5| = 5.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'vrai_faux',
                            'texte': "Tout entier naturel est un nombre rationnel.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Tout entier n peut s'écrire n/1, c'est donc un rationnel. On a ℕ ⊂ ℤ ⊂ ℚ.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'vrai_faux',
                            'texte': "Le nombre π est un nombre rationnel.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "π est irrationnel : son écriture décimale est infinie et non périodique.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'texte_libre',
                            'texte': "Quelle est la valeur absolue de −12 ? (répondre par un nombre)",
                            'options': None,
                            'reponse_correcte': '12',
                            'tolerances': ["12"],
                            'explication': "|−12| = 12. La valeur absolue d'un nombre négatif est son opposé.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Parmi ces nombres, lequel est irrationnel ?",
                            'options': ["√2", "3/4", "0,5", "−8"],
                            'reponse_correcte': '0',
                            'explication': "√2 ≈ 1,41421… a une écriture décimale infinie non périodique. Les autres sont rationnels.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "L'écriture décimale de 1/3 est :",
                            'options': ["0,333… (périodique)", "0,33 (finie)", "0,3 (finie)", "Infinie non périodique"],
                            'reponse_correcte': '0',
                            'explication': "1/3 = 0,333… avec le chiffre 3 qui se répète indéfiniment. C'est un développement décimal périodique.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Que vaut |−3 − 4| ?",
                            'options': ["7", "1", "−7", "−1"],
                            'reponse_correcte': '0',
                            'explication': "|−3 − 4| = |−7| = 7. C'est aussi la distance entre −3 et 4 sur la droite des réels.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Parmi ces affirmations, laquelle est correcte ?",
                            'options': ["ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ", "ℝ ⊂ ℚ ⊂ ℤ ⊂ ℕ", "ℤ ⊂ ℕ ⊂ ℚ ⊂ ℝ", "ℕ ⊂ ℚ ⊂ ℤ ⊂ ℝ"],
                            'reponse_correcte': '0',
                            'explication': "Les ensembles de nombres sont emboîtés : ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "√9 est-il rationnel ou irrationnel ?",
                            'options': ["Rationnel, car √9 = 3", "Irrationnel", "Ni l'un ni l'autre", "On ne peut pas le déterminer"],
                            'reponse_correcte': '0',
                            'explication': "9 est un carré parfait (9 = 3²), donc √9 = 3 qui est un entier, et donc un rationnel.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "La distance entre deux points d'abscisses a et b sur la droite des réels est |a − b|.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Par définition, d(a, b) = |a − b|. La valeur absolue garantit un résultat positif ou nul.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'texte_libre',
                            'texte': "Dans quel plus petit ensemble de nombres se trouve 3/5 ? (répondre par la lettre : N, Z, Q ou R)",
                            'options': None,
                            'reponse_correcte': 'Q',
                            'tolerances': ["ℚ", "q", "rationnels", "rationnel"],
                            'explication': "3/5 = 0,6 n'est pas un entier, mais c'est une fraction d'entiers, donc il appartient à ℚ.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'texte_libre',
                            'texte': "Quelle est la distance entre −4 et 3 sur la droite des réels ? (répondre par un nombre)",
                            'options': None,
                            'reponse_correcte': '7',
                            'tolerances': ["7"],
                            'explication': "|−4 − 3| = |−7| = 7.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "Parmi ces nombres, lequel est rationnel ?",
                            'options': ["0,121212… (période 12)", "√5", "π", "√3"],
                            'reponse_correcte': '0',
                            'explication': "0,121212… a un développement décimal périodique, c'est donc un rationnel (égal à 12/99 = 4/33). Les autres sont irrationnels.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'qcm',
                            'texte': "L'inégalité triangulaire affirme que pour tous réels a et b :",
                            'options': ["|a + b| ≤ |a| + |b|", "|a + b| = |a| + |b|", "|a × b| ≤ |a| × |b|", "|a − b| ≥ |a| + |b|"],
                            'reponse_correcte': '0',
                            'explication': "Pour tous réels a et b, |a + b| ≤ |a| + |b|. C'est l'inégalité triangulaire.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'vrai_faux',
                            'texte': "√7 est un nombre rationnel.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "7 n'est pas un carré parfait, donc √7 est irrationnel. Son écriture décimale est infinie et non périodique.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Donner la fraction irréductible égale à 0,666… (le 6 se répète) sous la forme p/q.",
                            'options': None,
                            'reponse_correcte': '2/3',
                            'tolerances': ["2/3", "deux tiers"],
                            'explication': "Si x = 0,666…, alors 10x = 6,666…, donc 9x = 6, soit x = 6/9 = 2/3.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Divisibilité et décomposition en facteurs premiers',
                'duree': 35,
                'contenu': """# Divisibilité et décomposition en facteurs premiers

## Divisibilité dans $\\mathbb{Z}$

### Définition

Soient $a$ et $b$ deux entiers avec $a \\neq 0$. On dit que $a$ **divise** $b$ (noté $a \\mid b$) s'il existe un entier $k$ tel que :

$$b = k \\times a$$

On dit aussi que $b$ est un **multiple** de $a$, ou que $a$ est un **diviseur** de $b$.

> **Exemples :**
> - $3 \\mid 12$ car $12 = 4 \\times 3$
> - $5 \\mid 35$ car $35 = 7 \\times 5$
> - $4 \\nmid 10$ car $10 = 2 \\times 4 + 2$ (il reste 2)

### Critères de divisibilité

| Diviseur | Critère                                              | Exemple                                |
|----------|------------------------------------------------------|----------------------------------------|
| 2        | Le dernier chiffre est **pair** (0, 2, 4, 6, 8)     | $1\\,346$ : oui (6 pair)                |
| 3        | La **somme des chiffres** est divisible par 3        | $612$ : $6+1+2=9$ divisible par 3      |
| 4        | Les **deux derniers chiffres** forment un multiple de 4 | $1\\,324$ : $24 = 4 \\times 6$ oui   |
| 5        | Le dernier chiffre est **0 ou 5**                    | $1\\,235$ : oui                         |
| 9        | La **somme des chiffres** est divisible par 9        | $729$ : $7+2+9=18$ divisible par 9     |
| 10       | Le dernier chiffre est **0**                         | $1\\,230$ : oui                         |

---

## La division euclidienne

Pour tout entier $a \\geq 0$ et tout entier $b > 0$, il existe un **unique** couple $(q, r)$ tel que :

$$a = b \\times q + r \\quad \\text{avec} \\quad 0 \\leq r < b$$

- $q$ est le **quotient** de la division euclidienne.
- $r$ est le **reste**.

> **Exemple :** $47 = 6 \\times 7 + 5$, donc le quotient de $47$ par $6$ est $7$ et le reste est $5$.

En Python : `47 // 6` donne `7` (quotient) et `47 % 6` donne `5` (reste).

---

## PGCD — Plus Grand Commun Diviseur

### Définition

Le **PGCD** de deux entiers $a$ et $b$ (non tous deux nuls) est le plus grand entier qui divise à la fois $a$ et $b$.

### Algorithme d'Euclide

On effectue des divisions euclidiennes successives. Le PGCD est le **dernier reste non nul**.

> **Exemple :** PGCD(48, 18)
>
> | Division          | Quotient | Reste |
> |-------------------|----------|-------|
> | $48 = 18 \\times 2 + 12$ | 2 | 12 |
> | $18 = 12 \\times 1 + 6$  | 1 | 6  |
> | $12 = 6 \\times 2 + 0$   | 2 | 0  |
>
> Donc $\\text{PGCD}(48, 18) = 6$.

### PPCM — Plus Petit Commun Multiple

$$\\text{PPCM}(a, b) = \\frac{a \\times b}{\\text{PGCD}(a, b)}$$

> **Exemple :** $\\text{PPCM}(48, 18) = \\frac{48 \\times 18}{6} = 144$.

---

## Les nombres premiers

### Définition

Un entier $n \\geq 2$ est **premier** si ses seuls diviseurs positifs sont $1$ et $n$ lui-même.

**Premiers nombres premiers :** $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, \\ldots$

> **Remarques :**
> - $1$ n'est **pas** premier (par convention).
> - $2$ est le seul nombre premier **pair**.

### Test de primalité

Pour vérifier si $n$ est premier, il suffit de tester la divisibilité par tous les entiers de $2$ à $\\sqrt{n}$ :

Si aucun de ces entiers ne divise $n$, alors $n$ est premier.

> **Exemple :** $37$ est-il premier ?
> $\\sqrt{37} \\approx 6{,}08$ → on teste $2, 3, 4, 5, 6$.
> Aucun ne divise $37$, donc $37$ est premier.

---

## Décomposition en facteurs premiers

### Théorème fondamental de l'arithmétique

> **Tout entier $n \\geq 2$ se décompose de façon **unique** en un produit de nombres premiers** (à l'ordre près).

### Méthode pratique

On divise successivement par les nombres premiers $2, 3, 5, 7, 11, \\ldots$

> **Exemple :** Décomposons $360$.
>
> | Étape | Division        | Résultat |
> |-------|-----------------|----------|
> | 1     | $360 \\div 2 = 180$ | $2$  |
> | 2     | $180 \\div 2 = 90$  | $2$  |
> | 3     | $90 \\div 2 = 45$   | $2$  |
> | 4     | $45 \\div 3 = 15$   | $3$  |
> | 5     | $15 \\div 3 = 5$    | $3$  |
> | 6     | $5 \\div 5 = 1$     | $5$  |
>
> Donc : $360 = 2^3 \\times 3^2 \\times 5$

### Application : simplification de fractions

Pour simplifier $\\frac{48}{180}$, on décompose :
- $48 = 2^4 \\times 3$
- $180 = 2^2 \\times 3^2 \\times 5$

Le PGCD est $2^2 \\times 3 = 12$, donc :

$$\\frac{48}{180} = \\frac{48 \\div 12}{180 \\div 12} = \\frac{4}{15}$$

---

## À retenir

- $a \\mid b$ signifie qu'il existe $k \\in \\mathbb{Z}$ tel que $b = ka$.
- Les **critères de divisibilité** permettent de tester rapidement si un nombre est divisible par 2, 3, 5 ou 9.
- L'**algorithme d'Euclide** calcule le PGCD par des divisions euclidiennes successives.
- Tout entier $\\geq 2$ se décompose de manière **unique** en produit de facteurs premiers.
- Un nombre est premier s'il n'est divisible par aucun entier de $2$ à $\\sqrt{n}$.
""",
                'quiz': {
                    'titre': "Quiz — Divisibilité et décomposition en facteurs premiers",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Que signifie « 3 divise 12 » ?",
                            'options': ["Il existe un entier k tel que 12 = 3k", "12 est supérieur à 3", "12 − 3 = 9", "12 / 3 est un nombre décimal"],
                            'reponse_correcte': '0',
                            'explication': "3 | 12 signifie qu'il existe un entier k (ici k = 4) tel que 12 = 3 × 4.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Parmi ces nombres, lequel est divisible par 3 ?",
                            'options': ["126", "125", "128", "131"],
                            'reponse_correcte': '0',
                            'explication': "1 + 2 + 6 = 9 qui est divisible par 3, donc 126 est divisible par 3.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Un nombre est divisible par 5 si son dernier chiffre est :",
                            'options': ["0 ou 5", "Pair", "Impair", "Inférieur à 5"],
                            'reponse_correcte': '0',
                            'explication': "Le critère de divisibilité par 5 est que le dernier chiffre du nombre soit 0 ou 5.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Le nombre 1 est-il un nombre premier ?",
                            'options': ["Non", "Oui", "Cela dépend", "Oui, c'est le plus petit premier"],
                            'reponse_correcte': '0',
                            'explication': "Par convention, 1 n'est pas considéré comme un nombre premier. Les nombres premiers commencent à 2.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Quel est le reste de la division euclidienne de 17 par 5 ?",
                            'options': ["2", "3", "5", "12"],
                            'reponse_correcte': '0',
                            'explication': "17 = 5 × 3 + 2, donc le quotient est 3 et le reste est 2.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'vrai_faux',
                            'texte': "2 est le seul nombre premier pair.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "2 est pair et premier. Tout autre nombre pair est divisible par 2, donc n'est pas premier.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'vrai_faux',
                            'texte': "15 est un nombre premier.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "15 = 3 × 5, il a d'autres diviseurs que 1 et lui-même, donc il n'est pas premier.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'texte_libre',
                            'texte': "Quel est le quotient de la division euclidienne de 23 par 4 ? (répondre par un nombre)",
                            'options': None,
                            'reponse_correcte': '5',
                            'tolerances': ["5"],
                            'explication': "23 = 4 × 5 + 3. Le quotient est 5 et le reste est 3.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Quelle est la décomposition en facteurs premiers de 60 ?",
                            'options': ["2² × 3 × 5", "2 × 3 × 10", "4 × 15", "2³ × 5"],
                            'reponse_correcte': '0',
                            'explication': "60 = 2 × 30 = 2 × 2 × 15 = 2 × 2 × 3 × 5 = 2² × 3 × 5.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Pour calculer le PGCD de deux nombres, on utilise :",
                            'options': ["L'algorithme d'Euclide", "Le théorème de Pythagore", "Le crible d'Ératosthène", "La règle de trois"],
                            'reponse_correcte': '0',
                            'explication': "L'algorithme d'Euclide consiste à effectuer des divisions euclidiennes successives jusqu'à obtenir un reste nul.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Quel est le PGCD de 36 et 24 ?",
                            'options': ["12", "6", "4", "36"],
                            'reponse_correcte': '0',
                            'explication': "Par l'algorithme d'Euclide : 36 = 24 × 1 + 12, puis 24 = 12 × 2 + 0. Le dernier reste non nul est 12.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Quel est le PPCM de 12 et 18 ?",
                            'options': ["36", "6", "216", "72"],
                            'reponse_correcte': '0',
                            'explication': "PGCD(12, 18) = 6, donc PPCM(12, 18) = (12 × 18) / 6 = 216 / 6 = 36.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Pour vérifier si 53 est premier, jusqu'à quel nombre faut-il tester la divisibilité ?",
                            'options': ["7 (car √53 ≈ 7,3)", "53", "26", "10"],
                            'reponse_correcte': '0',
                            'explication': "On teste les diviseurs de 2 à √53 ≈ 7,3, soit jusqu'à 7. Aucun ne divise 53, donc 53 est premier.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "La somme des chiffres de 729 est divisible par 9.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "7 + 2 + 9 = 18, et 18 est bien divisible par 9. Donc 729 est divisible par 9.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'texte_libre',
                            'texte': "Quelle est la décomposition en facteurs premiers de 36 ? (écrire sous la forme a² × b²)",
                            'options': None,
                            'reponse_correcte': '2^2 x 3^2',
                            'tolerances': ["2² × 3²", "2^2 * 3^2", "2**2 * 3**2", "4 x 9", "2^2 x 3^2"],
                            'explication': "36 = 4 × 9 = 2² × 3².",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'texte_libre',
                            'texte': "Quel est le PGCD de 48 et 18 ? (répondre par un nombre)",
                            'options': None,
                            'reponse_correcte': '6',
                            'tolerances': ["6"],
                            'explication': "48 = 18 × 2 + 12, 18 = 12 × 1 + 6, 12 = 6 × 2 + 0. Le PGCD est 6.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "Simplifiez la fraction 84/126 en fraction irréductible.",
                            'options': ["2/3", "4/6", "7/9", "14/21"],
                            'reponse_correcte': '0',
                            'explication': "PGCD(84, 126) = 42. Donc 84/126 = (84÷42)/(126÷42) = 2/3.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'qcm',
                            'texte': "Combien de diviseurs positifs possède le nombre 2³ × 5² ?",
                            'options': ["12", "6", "8", "15"],
                            'reponse_correcte': '0',
                            'explication': "Le nombre de diviseurs de p^a × q^b est (a+1)(b+1) = (3+1)(2+1) = 4 × 3 = 12.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'vrai_faux',
                            'texte': "Tout entier supérieur ou égal à 2 admet une unique décomposition en facteurs premiers (à l'ordre près).",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est le théorème fondamental de l'arithmétique : tout entier ≥ 2 se décompose de façon unique en produit de facteurs premiers.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Quel est le PPCM de 15 et 20 ? (répondre par un nombre)",
                            'options': None,
                            'reponse_correcte': '60',
                            'tolerances': ["60"],
                            'explication': "PGCD(15, 20) = 5, donc PPCM = (15 × 20) / 5 = 300 / 5 = 60.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },

    # ──────────────────────────────────────────────
    # CHAPITRE 3 — Équations du premier degré
    # ──────────────────────────────────────────────
    {
        'ordre': 3,
        'titre': 'Équations du premier degré',
        'description': "Résolution d'équations du premier degré, équations avec fractions, valeur absolue et mises en équation de problèmes.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Résoudre une équation du premier degré",
                'duree': 30,
                'contenu': """# Résoudre une équation du premier degré

## Qu'est-ce qu'une équation ?

Une **équation** est une égalité comportant un ou plusieurs nombres inconnus, souvent notés $x$.

**Résoudre** une équation, c'est trouver toutes les valeurs de $x$ qui rendent l'égalité vraie. Ces valeurs sont les **solutions** de l'équation.

> **Exemple :** L'équation $2x + 3 = 11$ a pour solution $x = 4$, car $2 \\times 4 + 3 = 11$.

---

## Équation du premier degré : $ax + b = 0$

Une équation du **premier degré** à une inconnue $x$ est de la forme :

$$ax + b = 0$$

où $a$ et $b$ sont des nombres réels donnés.

### Résolution

**Cas 1 : $a \\neq 0$**

$$ax + b = 0 \\iff ax = -b \\iff x = -\\frac{b}{a}$$

L'équation admet une **unique solution** : $x = -\\dfrac{b}{a}$.

**Cas 2 : $a = 0$ et $b \\neq 0$**

L'équation devient $0 \\cdot x + b = 0$, soit $b = 0$ ce qui est **faux**. Pas de solution ($S = \\emptyset$).

**Cas 3 : $a = 0$ et $b = 0$**

L'équation devient $0 = 0$, qui est **toujours vraie**. Tout réel est solution ($S = \\mathbb{R}$).

---

## Règles de transformation

Pour résoudre une équation, on applique des **transformations élémentaires** qui conservent l'ensemble des solutions.

### Règle 1 : Ajouter ou soustraire le même nombre des deux côtés

$$A = B \\iff A + c = B + c$$

> **Exemple :** $x - 7 = 3 \\iff x = 3 + 7 \\iff x = 10$

### Règle 2 : Multiplier ou diviser les deux côtés par un même nombre **non nul**

$$A = B \\iff c \\cdot A = c \\cdot B \\quad (c \\neq 0)$$

> **Exemple :** $\\frac{x}{4} = 5 \\iff x = 5 \\times 4 \\iff x = 20$

---

## Méthode de résolution détaillée

Résolvons $3x - 5 = 2x + 7$ :

| Étape | Action | Résultat |
|-------|--------|----------|
| 1 | On soustrait $2x$ des deux côtés | $3x - 2x - 5 = 7$ |
| 2 | On simplifie | $x - 5 = 7$ |
| 3 | On ajoute $5$ des deux côtés | $x = 12$ |

**Vérification :** $3 \\times 12 - 5 = 31$ et $2 \\times 12 + 7 = 31$. ✓

---

## Équation produit nul

> **Propriété fondamentale :** Un produit de facteurs est nul si et seulement si **l'un au moins des facteurs est nul**.
>
> $$A \\times B = 0 \\iff A = 0 \\text{ ou } B = 0$$

**Exemple :** Résolvons $(2x - 6)(x + 4) = 0$ :

$$2x - 6 = 0 \\iff x = 3 \\quad \\text{ou} \\quad x + 4 = 0 \\iff x = -4$$

L'ensemble des solutions est $S = \\{-4 \\,;\\, 3\\}$.

---

## Mise en équation d'un problème

### Méthode

1. **Identifier** l'inconnue et la nommer (ex : $x$).
2. **Traduire** l'énoncé en une équation mathématique.
3. **Résoudre** l'équation.
4. **Vérifier** que la solution a un sens dans le contexte du problème.

### Exemple

> « Paul a le triple de l'âge de sa fille. La somme de leurs âges est 48 ans. Quel est l'âge de la fille ? »

Soit $x$ l'âge de la fille. L'âge de Paul est $3x$.

$$x + 3x = 48 \\iff 4x = 48 \\iff x = 12$$

La fille a **12 ans** et Paul a $36$ ans. Vérification : $12 + 36 = 48$. ✓

---

## À retenir

- L'équation $ax + b = 0$ a une **unique solution** $x = -\\frac{b}{a}$ lorsque $a \\neq 0$.
- On résout en **isolant** $x$ par des opérations identiques des deux côtés.
- L'équation produit nul $A \\times B = 0$ se résout en posant $A = 0$ **ou** $B = 0$.
- Pour un problème concret : nommer l'inconnue → traduire → résoudre → vérifier.
""",
                'quiz': {
                    'titre': "Quiz — Résoudre une équation du premier degré",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quelle est la solution de l'équation 2x = 10 ?",
                            'options': ["x = 5", "x = 10", "x = 2", "x = 20"],
                            'reponse_correcte': '0',
                            'explication': "On divise les deux membres par 2 : x = 10/2 = 5.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Résoudre une équation, c'est :",
                            'options': ["Trouver les valeurs de l'inconnue qui rendent l'égalité vraie", "Calculer une somme", "Simplifier une expression", "Tracer un graphique"],
                            'reponse_correcte': '0',
                            'explication': "Résoudre une équation consiste à trouver toutes les valeurs de l'inconnue pour lesquelles l'égalité est vérifiée.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Quelle est la solution de x + 7 = 12 ?",
                            'options': ["x = 5", "x = 19", "x = 7", "x = −5"],
                            'reponse_correcte': '0',
                            'explication': "On soustrait 7 des deux côtés : x = 12 − 7 = 5.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "L'équation 3x − 6 = 0 a pour solution :",
                            'options': ["x = 2", "x = 6", "x = −2", "x = 3"],
                            'reponse_correcte': '0',
                            'explication': "3x = 6, donc x = 6/3 = 2.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La propriété du produit nul dit que A × B = 0 implique :",
                            'options': ["A = 0 ou B = 0", "A = 0 et B = 0", "A + B = 0", "A = B"],
                            'reponse_correcte': '0',
                            'explication': "Un produit est nul si et seulement si l'un au moins des facteurs est nul.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'vrai_faux',
                            'texte': "L'équation 0x + 5 = 0 n'a aucune solution.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "L'équation devient 5 = 0, ce qui est faux. Aucune valeur de x ne peut rendre cette égalité vraie.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'vrai_faux',
                            'texte': "Si on ajoute le même nombre aux deux membres d'une équation, l'ensemble des solutions ne change pas.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est une règle fondamentale : ajouter ou soustraire une même quantité des deux côtés conserve les solutions.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'texte_libre',
                            'texte': "Quelle est la solution de 5x = 30 ? (répondre par un nombre)",
                            'options': None,
                            'reponse_correcte': '6',
                            'tolerances': ["x = 6", "x=6", "6"],
                            'explication': "On divise par 5 : x = 30/5 = 6.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Résolvez 3x − 5 = 2x + 7.",
                            'options': ["x = 12", "x = 2", "x = −12", "x = 7"],
                            'reponse_correcte': '0',
                            'explication': "3x − 2x = 7 + 5, soit x = 12.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Les solutions de (x − 3)(2x + 4) = 0 sont :",
                            'options': ["x = 3 ou x = −2", "x = −3 ou x = 2", "x = 3 ou x = 4", "x = 3 uniquement"],
                            'reponse_correcte': '0',
                            'explication': "x − 3 = 0 donne x = 3, ou 2x + 4 = 0 donne x = −2.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "L'équation 4(x − 1) = 2(x + 3) a pour solution :",
                            'options': ["x = 5", "x = 3", "x = −5", "x = 1"],
                            'reponse_correcte': '0',
                            'explication': "4x − 4 = 2x + 6, soit 2x = 10, donc x = 5.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Un père a le double de l'âge de son fils. La somme de leurs âges est 45. Quel est l'âge du fils ?",
                            'options': ["15 ans", "30 ans", "22 ans", "10 ans"],
                            'reponse_correcte': '0',
                            'explication': "Soit x l'âge du fils. Le père a 2x ans. x + 2x = 45, donc 3x = 45, x = 15.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "L'équation 0x = 0 a :",
                            'options': ["Une infinité de solutions (tout réel)", "Une seule solution x = 0", "Aucune solution", "Deux solutions"],
                            'reponse_correcte': '0',
                            'explication': "0x = 0 est vérifié pour tout x ∈ ℝ, car 0 × x = 0 est toujours vrai.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "L'équation 5x + 2 = 5x − 3 a une unique solution.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "En simplifiant, on obtient 2 = −3, ce qui est faux. L'équation n'a aucune solution.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'texte_libre',
                            'texte': "Résolvez 4x + 3 = 19. (répondre par un nombre)",
                            'options': None,
                            'reponse_correcte': '4',
                            'tolerances': ["x = 4", "x=4", "4"],
                            'explication': "4x = 19 − 3 = 16, donc x = 16/4 = 4.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'texte_libre',
                            'texte': "Quelles sont les solutions de (x − 5)(x + 1) = 0 ? (séparer par « et »)",
                            'options': None,
                            'reponse_correcte': '5 et -1',
                            'tolerances': ["x = 5 et x = -1", "5 et -1", "-1 et 5", "x=5 et x=-1", "5 ; -1", "-1 ; 5"],
                            'explication': "x − 5 = 0 donne x = 5, ou x + 1 = 0 donne x = −1.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "L'équation 2(3x − 1) − 4(x + 2) = 3x − 15 a pour solution :",
                            'options': ["x = 5", "x = 3", "x = −5", "Aucune solution"],
                            'reponse_correcte': '0',
                            'explication': "6x − 2 − 4x − 8 = 3x − 15, soit 2x − 10 = 3x − 15, donc −x = −5, x = 5.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'qcm',
                            'texte': "Les solutions de x² = 9 sont :",
                            'options': ["x = 3 ou x = −3", "x = 3 uniquement", "x = 9 ou x = −9", "x = 81"],
                            'reponse_correcte': '0',
                            'explication': "x² = 9 ⟺ x² − 9 = 0 ⟺ (x−3)(x+3) = 0, donc x = 3 ou x = −3.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'vrai_faux',
                            'texte': "Si on multiplie les deux membres d'une équation par 0, on obtient une équation équivalente.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Multiplier par 0 donne 0 = 0, qui est toujours vraie. On perd l'information sur les solutions. La multiplication doit se faire par un nombre non nul.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "La somme de trois nombres entiers consécutifs est 72. Quel est le plus petit de ces trois nombres ?",
                            'options': None,
                            'reponse_correcte': '23',
                            'tolerances': ["23"],
                            'explication': "Soit x le plus petit. x + (x+1) + (x+2) = 72, soit 3x + 3 = 72, 3x = 69, x = 23.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Équations avec fractions et valeur absolue',
                'duree': 30,
                'contenu': """# Équations avec fractions et valeur absolue

## Équations avec fractions

### Principe

Pour résoudre une équation contenant des fractions, on peut :

1. **Mettre au même dénominateur** pour transformer l'équation.
2. Ou **multiplier les deux membres** par le dénominateur commun pour « éliminer » les fractions.

> ⚠️ Avant de résoudre, vérifier les **valeurs interdites** : les valeurs de $x$ qui annulent un dénominateur sont à exclure.

### Exemple 1 : Sans valeur interdite

Résolvons $\\dfrac{2x+1}{3} = \\dfrac{x-2}{5}$

On multiplie les deux membres par $15$ (PPCM de $3$ et $5$) :

$$15 \\times \\frac{2x+1}{3} = 15 \\times \\frac{x-2}{5}$$

$$5(2x+1) = 3(x-2)$$

$$10x + 5 = 3x - 6$$

$$7x = -11$$

$$x = -\\frac{11}{7}$$

### Exemple 2 : Avec valeur interdite

Résolvons $\\dfrac{3}{x-1} = \\dfrac{5}{x+2}$

**Valeurs interdites :** $x \\neq 1$ et $x \\neq -2$ (car ces valeurs annulent les dénominateurs).

On effectue le **produit en croix** :

$$3(x+2) = 5(x-1)$$

$$3x + 6 = 5x - 5$$

$$11 = 2x$$

$$x = \\frac{11}{2} = 5{,}5$$

Comme $5{,}5 \\neq 1$ et $5{,}5 \\neq -2$, la solution est valide : $S = \\left\\{\\dfrac{11}{2}\\right\\}$.

### Exemple 3 : Solution = valeur interdite

Résolvons $\\dfrac{x}{x-3} = \\dfrac{3}{x-3} + 1$

**Valeur interdite :** $x \\neq 3$.

On multiplie par $(x-3)$ :

$$x = 3 + (x-3) = x$$

On obtient $x = x$, une identité. Mais la seule « solution » $x = 3$ est **interdite**. Donc $S = \\emptyset$.

---

## Équations avec valeur absolue

### Rappel

$$|X| = c \\quad (c \\geq 0) \\iff X = c \\text{ ou } X = -c$$

Si $c < 0$, l'équation $|X| = c$ n'a **aucune solution** (car une valeur absolue est toujours $\\geq 0$).

### Résolution de $|ax + b| = c$

Pour $c \\geq 0$ :

$$|ax + b| = c \\iff ax + b = c \\quad \\text{ou} \\quad ax + b = -c$$

On résout les **deux équations** séparément.

### Exemple 1

Résolvons $|2x - 5| = 3$ :

**Cas 1 :** $2x - 5 = 3 \\iff 2x = 8 \\iff x = 4$

**Cas 2 :** $2x - 5 = -3 \\iff 2x = 2 \\iff x = 1$

$$S = \\{1 \\,;\\, 4\\}$$

**Vérification :** $|2 \\times 4 - 5| = |3| = 3$ ✓ et $|2 \\times 1 - 5| = |-3| = 3$ ✓

### Exemple 2

Résolvons $|3x + 1| = -2$ :

La valeur absolue est toujours positive ou nulle, donc $|3x+1| \\geq 0 > -2$ pour tout $x$.

$$S = \\emptyset$$

### Équation du type $|A| = |B|$

$$|A| = |B| \\iff A = B \\text{ ou } A = -B$$

> **Exemple :** $|x-3| = |2x+1|$
>
> **Cas 1 :** $x - 3 = 2x + 1 \\iff -x = 4 \\iff x = -4$
>
> **Cas 2 :** $x - 3 = -(2x+1) \\iff x - 3 = -2x - 1 \\iff 3x = 2 \\iff x = \\frac{2}{3}$
>
> $S = \\left\\{-4 \\,;\\, \\frac{2}{3}\\right\\}$

---

## Interprétation géométrique de $|x - a| = d$

L'équation $|x - a| = d$ (avec $d > 0$) signifie : la **distance** entre $x$ et $a$ sur la droite des réels vaut $d$.

Les solutions sont donc $x = a + d$ et $x = a - d$.

> **Exemple :** $|x - 3| = 5 \\iff x = 8$ ou $x = -2$ (les deux points à distance 5 de 3).

---

## À retenir

- Pour une équation avec fractions : mettre au même dénominateur ou multiplier par le dénominateur commun. **Toujours vérifier les valeurs interdites.**
- $|X| = c$ avec $c \\geq 0$ donne deux équations : $X = c$ ou $X = -c$.
- $|X| = c$ avec $c < 0$ n'a **aucune solution**.
- $|A| = |B|$ se résout en $A = B$ ou $A = -B$.
""",
                'quiz': {
                    'titre': "Quiz — Équations avec fractions et valeur absolue",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Pour résoudre une équation avec fractions, on peut :",
                            'options': ["Multiplier les deux membres par le dénominateur commun", "Diviser les deux membres par zéro", "Ignorer les dénominateurs", "Ajouter les numérateurs entre eux"],
                            'reponse_correcte': '0',
                            'explication': "On multiplie les deux membres par le dénominateur commun (PPCM des dénominateurs) pour éliminer les fractions.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Que vaut |5| ?",
                            'options': ["5", "−5", "0", "25"],
                            'reponse_correcte': '0',
                            'explication': "|5| = 5 car 5 est déjà positif. La valeur absolue d'un positif ne change pas.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Que vaut |−8| ?",
                            'options': ["8", "−8", "0", "16"],
                            'reponse_correcte': '0',
                            'explication': "|−8| = 8 car la valeur absolue d'un négatif est son opposé.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Dans l'équation 3/(x−1) = 6, la valeur interdite est :",
                            'options': ["x = 1", "x = 0", "x = 6", "x = −1"],
                            'reponse_correcte': '0',
                            'explication': "Le dénominateur x − 1 ne peut pas être nul, donc x ≠ 1. C'est la valeur interdite.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "L'équation |x| = 3 a pour solutions :",
                            'options': ["x = 3 ou x = −3", "x = 3 uniquement", "x = −3 uniquement", "Aucune solution"],
                            'reponse_correcte': '0',
                            'explication': "|x| = 3 signifie que x est à distance 3 de 0, donc x = 3 ou x = −3.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'vrai_faux',
                            'texte': "L'équation |x| = −2 n'a aucune solution.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "La valeur absolue est toujours positive ou nulle, donc |x| ne peut jamais valoir −2.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'vrai_faux',
                            'texte': "Avant de résoudre une équation avec des fractions, il faut vérifier les valeurs interdites.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Les valeurs qui annulent un dénominateur sont interdites car la division par zéro est impossible.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'texte_libre',
                            'texte': "Que vaut |−15| ? (répondre par un nombre)",
                            'options': None,
                            'reponse_correcte': '15',
                            'tolerances': ["15"],
                            'explication': "|−15| = 15. La valeur absolue supprime le signe négatif.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Résolvez x/3 = 4.",
                            'options': ["x = 12", "x = 4/3", "x = 7", "x = 1"],
                            'reponse_correcte': '0',
                            'explication': "On multiplie les deux côtés par 3 : x = 4 × 3 = 12.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Les solutions de |2x − 5| = 3 sont :",
                            'options': ["x = 4 ou x = 1", "x = 4 uniquement", "x = 1 uniquement", "x = −1 ou x = 4"],
                            'reponse_correcte': '0',
                            'explication': "2x − 5 = 3 donne x = 4, ou 2x − 5 = −3 donne x = 1.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Résolvez (2x+1)/3 = (x−2)/5.",
                            'options': ["x = −11/7", "x = 11/7", "x = −1", "x = 7/11"],
                            'reponse_correcte': '0',
                            'explication': "On multiplie par 15 : 5(2x+1) = 3(x−2), soit 10x + 5 = 3x − 6, donc 7x = −11, x = −11/7.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "L'équation |x − 3| = 5 signifie que x est à distance 5 de :",
                            'options': ["3", "5", "0", "−3"],
                            'reponse_correcte': '0',
                            'explication': "|x − 3| = 5 signifie que la distance entre x et 3 vaut 5, donc x = 8 ou x = −2.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Résolvez 3/(x−1) = 5/(x+2) (attention aux valeurs interdites).",
                            'options': ["x = 11/2", "x = 1", "x = −2", "x = 2"],
                            'reponse_correcte': '0',
                            'explication': "Produit en croix : 3(x+2) = 5(x−1), soit 3x + 6 = 5x − 5, donc 11 = 2x, x = 11/2.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "|A| = |B| se résout en A = B ou A = −B.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Deux nombres ont la même valeur absolue si et seulement s'ils sont égaux ou opposés.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'texte_libre',
                            'texte': "Quelles sont les solutions de |x| = 5 ? (séparer par « et »)",
                            'options': None,
                            'reponse_correcte': '5 et -5',
                            'tolerances': ["-5 et 5", "x = 5 et x = -5", "5 ; -5", "-5 ; 5"],
                            'explication': "|x| = 5 donne x = 5 ou x = −5.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'texte_libre',
                            'texte': "Résolvez x/2 + x/3 = 5. (répondre par un nombre)",
                            'options': None,
                            'reponse_correcte': '6',
                            'tolerances': ["x = 6", "x=6", "6"],
                            'explication': "x/2 + x/3 = 3x/6 + 2x/6 = 5x/6 = 5, donc x = 5 × 6/5 = 6.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "Résolvez |x − 3| = |2x + 1|.",
                            'options': ["x = 2/3 ou x = −4", "x = 2/3 uniquement", "x = 4 ou x = −2", "Aucune solution"],
                            'reponse_correcte': '0',
                            'explication': "Cas 1 : x−3 = 2x+1 donne x = −4. Cas 2 : x−3 = −(2x+1) donne 3x = 2, x = 2/3.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'qcm',
                            'texte': "L'équation 4/(x−3) = (x+1)/(x−3) a pour ensemble de solutions :",
                            'options': ["L'ensemble vide (∅)", "{3}", "{4}", "ℝ"],
                            'reponse_correcte': '0',
                            'explication': "Valeur interdite : x ≠ 3. En multipliant par (x−3), on obtient 4 = x + 1, soit x = 3. Mais 3 est une valeur interdite, donc S = ∅.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'vrai_faux',
                            'texte': "L'équation |3x + 1| = −5 a deux solutions.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La valeur absolue est toujours ≥ 0, donc |3x + 1| ne peut pas être égale à −5. L'équation n'a aucune solution.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Résolvez |x − 3| = 5. Donner les deux solutions séparées par « et ».",
                            'options': None,
                            'reponse_correcte': '8 et -2',
                            'tolerances': ["-2 et 8", "x = 8 et x = -2", "8 ; -2", "-2 ; 8", "x=-2 et x=8"],
                            'explication': "x − 3 = 5 donne x = 8, ou x − 3 = −5 donne x = −2.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },

    # ──────────────────────────────────────────────
    # CHAPITRE 4 — Inéquations du premier degré
    # ──────────────────────────────────────────────
    {
        'ordre': 4,
        'titre': 'Inéquations du premier degré',
        'description': "Résolution d'inéquations, représentation sur la droite des réels, intervalles, encadrements et tableaux de signes.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Résoudre une inéquation et représenter l'ensemble solution",
                'duree': 30,
                'contenu': """# Résoudre une inéquation et représenter l'ensemble solution

## Qu'est-ce qu'une inéquation ?

Une **inéquation** est une inégalité contenant une inconnue (généralement $x$). Résoudre une inéquation, c'est trouver toutes les valeurs de $x$ pour lesquelles l'inégalité est vraie.

À la différence d'une équation qui a souvent un nombre fini de solutions, une inéquation a généralement une **infinité de solutions** formant un **intervalle** (ou une réunion d'intervalles).

---

## Règles de résolution

Les règles sont les mêmes que pour les équations, avec une **exception cruciale** :

### Règle 1 : Ajouter ou soustraire le même nombre

On peut ajouter ou soustraire le même nombre aux deux membres **sans changer le sens** de l'inégalité :

$$A < B \\iff A + c < B + c$$

### Règle 2 : Multiplier ou diviser par un nombre **positif**

Le sens de l'inégalité est **conservé** :

$$A < B \\iff k \\cdot A < k \\cdot B \\quad (k > 0)$$

### Règle 3 : Multiplier ou diviser par un nombre **négatif**

> ⚠️ **Le sens de l'inégalité est INVERSÉ :**

$$A < B \\iff k \\cdot A > k \\cdot B \\quad (k < 0)$$

> **Exemples :** Si $x < 3$, alors $-2x > -6$ (on multiplie par $-2$ et on inverse le sens).

---

## Résolution pas à pas

### Exemple 1 : $3x - 7 \\leq 2x + 5$

| Étape | Action | Résultat |
|-------|--------|----------|
| 1 | On soustrait $2x$ des deux côtés | $x - 7 \\leq 5$ |
| 2 | On ajoute $7$ des deux côtés | $x \\leq 12$ |

$$S = ]-\\infty \\,;\\, 12]$$

### Exemple 2 : $-4x + 3 > 11$

| Étape | Action | Résultat |
|-------|--------|----------|
| 1 | On soustrait $3$ | $-4x > 8$ |
| 2 | On divise par $-4$ (**on inverse !**) | $x < -2$ |

$$S = ]-\\infty \\,;\\, -2[$$

### Exemple 3 : Double inégalité

Résolvons $-3 < 2x + 1 \\leq 7$ :

On isole $x$ en traitant les **trois membres** simultanément :

$$-3 - 1 < 2x \\leq 7 - 1$$
$$-4 < 2x \\leq 6$$
$$-2 < x \\leq 3$$

$$S = ]-2 \\,;\\, 3]$$

---

## Représentation graphique

On représente l'ensemble solution sur une **droite des réels** :

- Un **crochet fermé** $[$ ou $]$ signifie que la borne est **incluse** (inégalité large $\\leq$ ou $\\geq$).
- Un **crochet ouvert** $]$ ou $[$ signifie que la borne est **exclue** (inégalité stricte $<$ ou $>$).
- On hachure ou colore la partie de la droite qui correspond aux solutions.

---

## Inéquation-produit : tableau de signes

Pour résoudre $(2x - 6)(x + 1) \\leq 0$, on étudie le **signe de chaque facteur** :

**Facteur 1 :** $2x - 6 = 0 \\iff x = 3$ ; positif pour $x > 3$, négatif pour $x < 3$

**Facteur 2 :** $x + 1 = 0 \\iff x = -1$ ; positif pour $x > -1$, négatif pour $x < -1$

**Tableau de signes :**

| $x$               | $-\\infty$ |   | $-1$  |   | $3$  |   | $+\\infty$ |
|--------------------|-----------|---|-------|---|------|---|-----------|
| $2x-6$             |    $-$    |   | $-$   |   | $0$  |   |   $+$     |
| $x+1$              |    $-$    |   | $0$   |   | $+$  |   |   $+$     |
| $(2x-6)(x+1)$      |    $+$    |   | $0$   |   | $0$  |   |   $+$     |

Le produit est **négatif** entre $-1$ et $3$ : $S = [-1 \\,;\\, 3]$.

> **Règle des signes :** $(-) \\times (-) = (+)$ ; $(+) \\times (-) = (-)$ ; $(+) \\times (+) = (+)$.

---

## Inéquation-quotient

Pour $\\dfrac{A}{B} \\leq 0$, on dresse le tableau de signes de $A$ et $B$.

> ⚠️ Le quotient n'est **pas défini** quand $B = 0$. La valeur qui annule le dénominateur est toujours **exclue** de l'ensemble solution.

---

## À retenir

- On résout une inéquation comme une équation, mais **on inverse le sens si on multiplie/divise par un nombre négatif**.
- L'ensemble solution est un intervalle (ou une réunion d'intervalles).
- Pour les inéquations-produits ou quotients, on utilise un **tableau de signes**.
- Le quotient $\\frac{A}{B}$ n'est jamais défini pour $B = 0$ : ces valeurs sont toujours exclues.
""",
                'quiz': {
                    'titre': "Quiz — Résoudre une inéquation",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quelle est la solution de $2x > 6$ ?",
                            'options': ["$x > 3$", "$x < 3$", "$x > 6$", "$x < 6$"],
                            'reponse_correcte': '0',
                            'explication': "On divise les deux membres par 2 (positif, le sens est conservé) : $x > 3$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "En résolvant $x + 5 \\leq 8$, on obtient :",
                            'options': ["$x \\leq 3$", "$x \\geq 3$", "$x \\leq 13$", "$x \\geq 13$"],
                            'reponse_correcte': '0',
                            'explication': "On soustrait 5 des deux côtés : $x \\leq 3$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Que se passe-t-il lorsqu'on multiplie les deux membres d'une inéquation par un nombre négatif ?",
                            'options': ["Le sens de l'inégalité est inversé", "Le sens est conservé", "L'inéquation n'a plus de solution", "Les deux membres deviennent nuls"],
                            'reponse_correcte': '0',
                            'explication': "Multiplier ou diviser par un nombre négatif inverse le sens de l'inégalité.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "L'ensemble solution de $x < 5$ s'écrit en notation intervalle :",
                            'options': ["$]-\\infty \\,;\\, 5[$", "$]-\\infty \\,;\\, 5]$", "$[5 \\,;\\, +\\infty[$", "$]5 \\,;\\, +\\infty[$"],
                            'reponse_correcte': '0',
                            'explication': "$x < 5$ signifie tous les réels strictement inférieurs à 5, soit $]-\\infty \\,;\\, 5[$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Résoudre $3x - 9 \\geq 0$ :",
                            'options': ["$x \\geq 3$", "$x \\leq 3$", "$x \\geq 9$", "$x \\leq -3$"],
                            'reponse_correcte': '0',
                            'explication': "$3x \\geq 9$, donc $x \\geq 3$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Résoudre $-x > 4$ :",
                            'options': ["$x < -4$", "$x > -4$", "$x < 4$", "$x > 4$"],
                            'reponse_correcte': '0',
                            'explication': "On multiplie par $-1$ et on inverse le sens : $x < -4$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "L'ensemble solution de $x \\geq -2$ est :",
                            'options': ["$[-2 \\,;\\, +\\infty[$", "$]-2 \\,;\\, +\\infty[$", "$]-\\infty \\,;\\, -2]$", "$]-\\infty \\,;\\, -2[$"],
                            'reponse_correcte': '0',
                            'explication': "$x \\geq -2$ inclut la borne $-2$ (crochet fermé) et va vers $+\\infty$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'vrai_faux',
                            'texte': "L'inéquation $5x \\leq 15$ a pour solution $x \\leq 3$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "On divise par 5 (positif, le sens est conservé) : $x \\leq 3$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Résoudre $-3x + 2 > 11$ :",
                            'options': ["$x < -3$", "$x > -3$", "$x < 3$", "$x > 3$"],
                            'reponse_correcte': '0',
                            'explication': "$-3x > 9$, on divise par $-3$ et on inverse : $x < -3$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "L'ensemble solution de $5 - 2x \\geq 1$ est :",
                            'options': ["$]-\\infty \\,;\\, 2]$", "$[2 \\,;\\, +\\infty[$", "$]-\\infty \\,;\\, -2]$", "$[-2 \\,;\\, +\\infty[$"],
                            'reponse_correcte': '0',
                            'explication': "$-2x \\geq -4$, on divise par $-2$ et on inverse : $x \\leq 2$, soit $]-\\infty \\,;\\, 2]$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "La double inéquation $-1 < 2x + 3 \\leq 9$ donne :",
                            'options': ["$-2 < x \\leq 3$", "$-2 \\leq x < 3$", "$1 < x \\leq 6$", "$-1 < x \\leq 3$"],
                            'reponse_correcte': '0',
                            'explication': "On soustrait 3 : $-4 < 2x \\leq 6$, puis on divise par 2 : $-2 < x \\leq 3$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Quel est le signe du produit $(x - 2)(x + 3)$ pour $x \\in ]-3 \\,;\\, 2[$ ?",
                            'options': ["Négatif", "Positif", "Nul", "On ne peut pas savoir"],
                            'reponse_correcte': '0',
                            'explication': "Entre les racines $-3$ et $2$, les deux facteurs sont de signes opposés, donc le produit est négatif.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Pour résoudre une inéquation-produit comme $(x - 1)(x + 4) \\leq 0$, on utilise :",
                            'options': ["Un tableau de signes", "La formule du discriminant", "Une mise au carré", "Le théorème de Pythagore"],
                            'reponse_correcte': '0',
                            'explication': "On étudie le signe de chaque facteur, puis on en déduit le signe du produit via un tableau de signes.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Si on divise les deux membres de $-4x \\leq 8$ par $-4$, on obtient $x \\leq -2$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "En divisant par $-4$ (négatif), on inverse l'inégalité : $x \\geq -2$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "L'ensemble solution de $(x - 1)(x - 5) \\leq 0$ est $[1 \\,;\\, 5]$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Le produit est négatif ou nul entre les racines 1 et 5, bornes incluses : $S = [1 \\,;\\, 5]$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'qcm',
                            'texte': "L'ensemble solution de $\\frac{x - 1}{x + 2} \\geq 0$ est :",
                            'options': ["$]-\\infty \\,;\\, -2[ \\cup [1 \\,;\\, +\\infty[$", "$[-2 \\,;\\, 1]$", "$]-\\infty \\,;\\, -2] \\cup [1 \\,;\\, +\\infty[$", "$]-2 \\,;\\, 1[$"],
                            'reponse_correcte': '0',
                            'explication': "Le numérateur s'annule en $x = 1$, le dénominateur en $x = -2$ (valeur interdite). Par tableau de signes, le quotient est $\\geq 0$ sur $]-\\infty;-2[ \\cup [1;+\\infty[$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "Résoudre $-2x + 3 > 4x - 9$ :",
                            'options': ["$x < 2$", "$x > 2$", "$x < -2$", "$x > -2$"],
                            'reponse_correcte': '0',
                            'explication': "$-2x - 4x > -9 - 3$, soit $-6x > -12$, on divise par $-6$ et on inverse : $x < 2$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Résoudre $4x - 8 > 0$. Quelle est la valeur seuil (la borne de l'intervalle solution) ?",
                            'options': None,
                            'reponse_correcte': '2',
                            'tolerances': ["2,0", "2.0"],
                            'explication': "$4x > 8$, soit $x > 2$. La valeur seuil est $2$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "On résout $\\frac{2x + 6}{3} \\leq 4$. Quelle est la borne supérieure de l'ensemble solution ?",
                            'options': None,
                            'reponse_correcte': '3',
                            'tolerances': ["3,0", "3.0"],
                            'explication': "$2x + 6 \\leq 12$, soit $2x \\leq 6$, donc $x \\leq 3$. La borne supérieure est $3$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Le produit $(x - 3)(x + 1)$ est négatif ou nul sur l'intervalle $[a \\,;\\, b]$. Quelle est la valeur de $a$ ?",
                            'options': None,
                            'reponse_correcte': '-1',
                            'tolerances': ["-1,0", "-1.0"],
                            'explication': "Les racines sont $x = -1$ et $x = 3$. Le produit est $\\leq 0$ sur $[-1 \\,;\\, 3]$, donc $a = -1$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Intervalles et encadrements',
                'duree': 25,
                'contenu': """# Intervalles et encadrements

## Les intervalles de $\\mathbb{R}$

Un **intervalle** est un sous-ensemble de $\\mathbb{R}$ « sans trou » : il contient tous les réels compris entre deux bornes.

### Notation et types d'intervalles

Soient $a$ et $b$ deux réels avec $a < b$ :

| Notation         | Ensemble                      | Description                 |
|-----------------|-------------------------------|-----------------------------|
| $[a \\,;\\, b]$   | $\\{x \\in \\mathbb{R} \\mid a \\leq x \\leq b\\}$ | Intervalle fermé          |
| $]a \\,;\\, b[$   | $\\{x \\in \\mathbb{R} \\mid a < x < b\\}$ | Intervalle ouvert                   |
| $[a \\,;\\, b[$   | $\\{x \\in \\mathbb{R} \\mid a \\leq x < b\\}$ | Fermé à gauche, ouvert à droite |
| $]a \\,;\\, b]$   | $\\{x \\in \\mathbb{R} \\mid a < x \\leq b\\}$ | Ouvert à gauche, fermé à droite |
| $[a \\,;\\, +\\infty[$ | $\\{x \\in \\mathbb{R} \\mid x \\geq a\\}$ | Demi-droite fermée       |
| $]a \\,;\\, +\\infty[$ | $\\{x \\in \\mathbb{R} \\mid x > a\\}$ | Demi-droite ouverte       |
| $]-\\infty \\,;\\, b]$ | $\\{x \\in \\mathbb{R} \\mid x \\leq b\\}$ | Demi-droite fermée       |
| $]-\\infty \\,;\\, b[$ | $\\{x \\in \\mathbb{R} \\mid x < b\\}$ | Demi-droite ouverte       |
| $]-\\infty \\,;\\, +\\infty[$ | $\\mathbb{R}$ | La droite réelle entière |

> **Remarques :**
> - $+\\infty$ et $-\\infty$ ne sont **pas des nombres réels** ; le crochet est toujours **ouvert** de leur côté.
> - Un crochet **fermé** $[$ ou $]$ signifie que la borne est **incluse**.
> - Un crochet **ouvert** $]$ ou $[$ signifie que la borne est **exclue**.

---

## Intersection et réunion d'intervalles

### Intersection : $\\cap$

L'**intersection** de deux ensembles est l'ensemble des éléments qui appartiennent aux **deux** ensembles.

> **Exemple :** $[-3 \\,;\\, 5] \\cap [2 \\,;\\, 8] = [2 \\,;\\, 5]$

Si deux intervalles ne se chevauchent pas, leur intersection est vide :

> $[1 \\,;\\, 3] \\cap [5 \\,;\\, 7] = \\emptyset$

### Réunion : $\\cup$

La **réunion** de deux ensembles est l'ensemble des éléments qui appartiennent à **l'un ou l'autre** (ou aux deux).

> **Exemple :** $]-\\infty \\,;\\, -1] \\cup [3 \\,;\\, +\\infty[$ représente tous les réels sauf ceux de $]-1 \\,;\\, 3[$.

---

## Encadrements

### Définition

Un **encadrement** d'un nombre $x$ est une double inégalité :

$$a \\leq x \\leq b$$

On dit que $x$ est encadré entre $a$ et $b$ ; l'**amplitude** (ou précision) de cet encadrement est $b - a$.

> **Exemple :** $3{,}14 \\leq \\pi \\leq 3{,}15$ est un encadrement de $\\pi$ d'amplitude $0{,}01$.

### Opérations sur les encadrements

Si $a \\leq x \\leq b$ et $c \\leq y \\leq d$ :

**Addition :**
$$a + c \\leq x + y \\leq b + d$$

**Soustraction :**
$$a - d \\leq x - y \\leq b - c$$

> ⚠️ On « croise » les bornes pour la soustraction.

**Multiplication par un scalaire :**

Si $k > 0$ : $ka \\leq kx \\leq kb$

Si $k < 0$ : $kb \\leq kx \\leq ka$ (on inverse !)

### Exemple

Sachant que $2 \\leq x \\leq 5$ et $-1 \\leq y \\leq 3$, encadrer $x + y$ et $x - y$ :

$$2 + (-1) \\leq x + y \\leq 5 + 3 \\implies 1 \\leq x + y \\leq 8$$

$$2 - 3 \\leq x - y \\leq 5 - (-1) \\implies -1 \\leq x - y \\leq 6$$

---

## Valeur approchée

Une **valeur approchée** d'un nombre $x$ est un nombre « proche » de $x$.

- **Par défaut** (troncature) : on arrondit vers le bas → $3{,}141$ pour $\\pi$ au millième.
- **Par excès** : on arrondit vers le haut → $3{,}142$ pour $\\pi$ au millième.

> **Précision :** la valeur approchée $a$ est à $10^{-n}$ près si $|x - a| \\leq 10^{-n}$.

---

## À retenir

- Un **intervalle** est une partie de $\\mathbb{R}$ sans trou, défini par ses bornes et le type de crochet (ouvert/fermé).
- L'**intersection** ($\\cap$) est le « et » : les éléments communs. La **réunion** ($\\cup$) est le « ou ».
- Un **encadrement** $a \\leq x \\leq b$ signifie que $x \\in [a;b]$.
- On peut additionner et soustraire des encadrements en respectant les règles sur les bornes.
""",
                'quiz': {
                    'titre': "Quiz — Intervalles et encadrements",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "L'intervalle $[2 \\,;\\, 7]$ contient :",
                            'options': ["Tous les réels $x$ tels que $2 \\leq x \\leq 7$", "Tous les réels $x$ tels que $2 < x < 7$", "Uniquement les entiers de 2 à 7", "Tous les réels sauf 2 et 7"],
                            'reponse_correcte': '0',
                            'explication': "Les crochets fermés $[$ et $]$ signifient que les bornes 2 et 7 sont incluses.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "La notation $]3 \\,;\\, +\\infty[$ signifie :",
                            'options': ["Tous les réels strictement supérieurs à 3", "Tous les réels supérieurs ou égaux à 3", "Tous les réels inférieurs à 3", "L'ensemble vide"],
                            'reponse_correcte': '0',
                            'explication': "Le crochet ouvert du côté de 3 exclut cette valeur : $x > 3$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Pourquoi le crochet est-il toujours ouvert du côté de $+\\infty$ ou $-\\infty$ ?",
                            'options': ["$+\\infty$ et $-\\infty$ ne sont pas des nombres réels", "Les intervalles sont toujours ouverts", "C'est une convention arbitraire", "Les bornes infinies sont incluses"],
                            'reponse_correcte': '0',
                            'explication': "$+\\infty$ et $-\\infty$ ne sont pas des nombres réels, on ne peut donc pas les « inclure ».",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "L'intersection $[1 \\,;\\, 5] \\cap [3 \\,;\\, 8]$ est :",
                            'options': ["$[3 \\,;\\, 5]$", "$[1 \\,;\\, 8]$", "$[1 \\,;\\, 3]$", "$[5 \\,;\\, 8]$"],
                            'reponse_correcte': '0',
                            'explication': "L'intersection contient les éléments communs : les réels entre 3 et 5.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La réunion $[1 \\,;\\, 4] \\cup [4 \\,;\\, 7]$ est :",
                            'options': ["$[1 \\,;\\, 7]$", "$\\{4\\}$", "$[1 \\,;\\, 4[$", "$]4 \\,;\\, 7]$"],
                            'reponse_correcte': '0',
                            'explication': "Les deux intervalles se rejoignent en 4, leur réunion couvre $[1 \\,;\\, 7]$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "L'intervalle $]-\\infty \\,;\\, 0[$ contient-il le nombre 0 ?",
                            'options': ["Non", "Oui", "Seulement si l'intervalle est fermé", "Cela dépend du contexte"],
                            'reponse_correcte': '0',
                            'explication': "Le crochet ouvert du côté de 0 signifie que 0 est exclu : $x < 0$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "L'amplitude de l'encadrement $3 \\leq x \\leq 7$ est :",
                            'options': ["4", "10", "3", "7"],
                            'reponse_correcte': '0',
                            'explication': "L'amplitude est la différence entre les bornes : $7 - 3 = 4$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'vrai_faux',
                            'texte': "L'intersection de deux intervalles disjoints est l'ensemble vide.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Deux intervalles disjoints n'ont aucun élément en commun, leur intersection est $\\emptyset$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "L'intersection $]-1 \\,;\\, 4] \\cap [0 \\,;\\, 6[$ est :",
                            'options': ["$[0 \\,;\\, 4]$", "$]-1 \\,;\\, 6[$", "$]0 \\,;\\, 4[$", "$[-1 \\,;\\, 6]$"],
                            'reponse_correcte': '0',
                            'explication': "On prend le plus grand des minima ($0$, fermé) et le plus petit des maxima ($4$, fermé) : $[0 \\,;\\, 4]$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Si $2 \\leq x \\leq 5$ et $1 \\leq y \\leq 3$, alors $x + y$ appartient à :",
                            'options': ["$[3 \\,;\\, 8]$", "$[1 \\,;\\, 5]$", "$[2 \\,;\\, 3]$", "$[3 \\,;\\, 5]$"],
                            'reponse_correcte': '0',
                            'explication': "On additionne les bornes : $2 + 1 = 3$ et $5 + 3 = 8$, donc $x + y \\in [3 \\,;\\, 8]$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Si $2 \\leq x \\leq 5$ et $1 \\leq y \\leq 3$, alors $x - y$ appartient à :",
                            'options': ["$[-1 \\,;\\, 4]$", "$[1 \\,;\\, 2]$", "$[-3 \\,;\\, 4]$", "$[0 \\,;\\, 5]$"],
                            'reponse_correcte': '0',
                            'explication': "On croise les bornes : $2 - 3 = -1$ et $5 - 1 = 4$, donc $x - y \\in [-1 \\,;\\, 4]$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "La réunion $]-\\infty \\,;\\, 2] \\cup [5 \\,;\\, +\\infty[$ représente tous les réels sauf :",
                            'options': ["$]2 \\,;\\, 5[$", "$[2 \\,;\\, 5]$", "$]-\\infty \\,;\\, 2[$", "$]5 \\,;\\, +\\infty[$"],
                            'reponse_correcte': '0',
                            'explication': "Les réels manquants sont ceux strictement entre 2 et 5 : $]2 \\,;\\, 5[$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Si $-3 \\leq x \\leq 1$, alors $-2x$ appartient à :",
                            'options': ["$[-2 \\,;\\, 6]$", "$[-6 \\,;\\, 2]$", "$[2 \\,;\\, 6]$", "$[-6 \\,;\\, -2]$"],
                            'reponse_correcte': '0',
                            'explication': "On multiplie par $-2$ et on inverse : $-2 \\times 1 = -2$ et $-2 \\times (-3) = 6$, donc $-2x \\in [-2 \\,;\\, 6]$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Si $1 \\leq x \\leq 4$ et $2 \\leq y \\leq 5$, alors $x - y \\in [-1 \\,;\\, 2]$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "$x - y \\in [1 - 5 \\,;\\, 4 - 2] = [-4 \\,;\\, 2]$, pas $[-1 \\,;\\, 2]$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "L'intervalle $]2 \\,;\\, 2[$ est l'ensemble vide.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Il n'existe aucun réel strictement compris entre 2 et 2.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'qcm',
                            'texte': "Soit $1 \\leq x \\leq 3$ et $2 \\leq y \\leq 4$. L'encadrement de $2x - y$ est :",
                            'options': ["$[-2 \\,;\\, 4]$", "$[0 \\,;\\, 2]$", "$[-4 \\,;\\, 6]$", "$[0 \\,;\\, 4]$"],
                            'reponse_correcte': '0',
                            'explication': "$2x \\in [2 \\,;\\, 6]$. On soustrait $y \\in [2 \\,;\\, 4]$ en croisant : $2 - 4 = -2$ et $6 - 2 = 4$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "L'ensemble $]-\\infty \\,;\\, -1[ \\cup ]3 \\,;\\, +\\infty[$ est le complémentaire dans $\\mathbb{R}$ de :",
                            'options': ["$[-1 \\,;\\, 3]$", "$]-1 \\,;\\, 3[$", "$[-1 \\,;\\, 3[$", "$]-1 \\,;\\, 3]$"],
                            'reponse_correcte': '0',
                            'explication': "Le complémentaire contient tous les réels non présents, soit $[-1 \\,;\\, 3]$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Quelle est l'amplitude de l'encadrement $-2{,}5 \\leq x \\leq 1{,}5$ ?",
                            'options': None,
                            'reponse_correcte': '4',
                            'tolerances': ["4,0", "4.0"],
                            'explication': "Amplitude $= 1{,}5 - (-2{,}5) = 4$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Si $3 \\leq x \\leq 5$, quel est le minimum de $-3x$ ?",
                            'options': None,
                            'reponse_correcte': '-15',
                            'tolerances': ["-15,0", "-15.0"],
                            'explication': "La fonction $x \\mapsto -3x$ est décroissante. Le minimum est atteint pour $x = 5$ : $-3 \\times 5 = -15$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "L'intersection $[-4 \\,;\\, 3] \\cap [-1 \\,;\\, 7]$ est l'intervalle $[a \\,;\\, b]$. Quelle est la valeur de $a + b$ ?",
                            'options': None,
                            'reponse_correcte': '2',
                            'tolerances': ["2,0", "2.0"],
                            'explication': "L'intersection est $[-1 \\,;\\, 3]$, donc $a = -1$ et $b = 3$, soit $a + b = 2$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },

    # ──────────────────────────────────────────────
    # CHAPITRE 5 — Fonctions et fonctions affines
    # ──────────────────────────────────────────────
    {
        'ordre': 5,
        'titre': 'Fonctions et fonctions affines',
        'description': "Notion de fonction, image, antécédent, courbe représentative, variations. Fonctions affines et linéaires.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Notion de fonction — image, antécédent, domaine',
                'duree': 30,
                'contenu': """# Notion de fonction — image, antécédent, domaine

## Qu'est-ce qu'une fonction ?

Une **fonction** $f$ est un procédé qui, à chaque nombre $x$ d'un ensemble de départ, associe **un unique** nombre noté $f(x)$.

On écrit :

$$f : x \\longmapsto f(x)$$

On lit : « $f$ est la fonction qui à $x$ associe $f(x)$ ».

> **Exemple :** $f : x \\longmapsto 2x + 3$. Alors $f(1) = 5$, $f(0) = 3$, $f(-2) = -1$.

---

## Vocabulaire fondamental

### Image

L'**image** de $a$ par la fonction $f$ est le nombre $f(a)$.

Pour la calculer, on **remplace** $x$ par $a$ dans l'expression de $f(x)$.

> **Exemple :** Si $f(x) = x^2 - 4x + 1$, l'image de $3$ est :
> $f(3) = 3^2 - 4 \\times 3 + 1 = 9 - 12 + 1 = -2$

### Antécédent

Un **antécédent** de $b$ par la fonction $f$ est un nombre $a$ tel que $f(a) = b$.

Pour le trouver, on **résout l'équation** $f(x) = b$.

> **Exemple :** Si $f(x) = 2x + 3$, cherchons les antécédents de 9 :
> $2x + 3 = 9 \\iff 2x = 6 \\iff x = 3$.
> Le nombre $3$ est l'antécédent de $9$ par $f$.

> ⚠️ Un nombre peut avoir **0, 1 ou plusieurs** antécédents.

### Domaine de définition

Le **domaine de définition** $D_f$ de $f$ est l'ensemble des valeurs de $x$ pour lesquelles $f(x)$ est définie.

**Exemples de restrictions :**
- $f(x) = \\frac{1}{x-2}$ : $D_f = \\mathbb{R} \\setminus \\{2\\}$ (dénominateur ≠ 0)
- $g(x) = \\sqrt{x}$ : $D_g = [0 \\,;\\, +\\infty[$ (radicande ≥ 0)

---

## Courbe représentative

### Définition

La **courbe représentative** (ou **représentation graphique**) de $f$ est l'ensemble des points $M(x \\,;\\, y)$ du plan tels que $y = f(x)$.

On la note $\\mathcal{C}_f$.

### Lecture graphique

Sur la courbe $\\mathcal{C}_f$ :
- L'**image** de $a$ par $f$ est l'**ordonnée** du point de la courbe d'abscisse $a$.
- Les **antécédents** de $b$ par $f$ sont les **abscisses** des points de la courbe d'ordonnée $b$.

> **Méthode :** Pour trouver l'image de $a$, on trace la droite verticale $x = a$ ; elle coupe $\\mathcal{C}_f$ en un point dont l'ordonnée est $f(a)$.
> Pour trouver les antécédents de $b$, on trace la droite horizontale $y = b$ ; ses intersections avec $\\mathcal{C}_f$ donnent les antécédents.

---

## Tableau de variation

Le **tableau de variation** résume le comportement d'une fonction sur son domaine.

### Fonction croissante

$f$ est **croissante** sur un intervalle $I$ si, pour tous $a, b \\in I$ :

$$a < b \\implies f(a) < f(b)$$

Plus $x$ augmente, plus $f(x)$ augmente → la courbe « monte ».

### Fonction décroissante

$f$ est **décroissante** sur un intervalle $I$ si, pour tous $a, b \\in I$ :

$$a < b \\implies f(a) > f(b)$$

Plus $x$ augmente, plus $f(x)$ diminue → la courbe « descend ».

### Maximum et minimum

- $f$ admet un **maximum** $M$ sur $I$ si $f(x) \\leq M$ pour tout $x \\in I$, et $M$ est atteint.
- $f$ admet un **minimum** $m$ sur $I$ si $f(x) \\geq m$ pour tout $x \\in I$, et $m$ est atteint.

---

## Résolution graphique d'équations et inéquations

### Équation $f(x) = k$

On trace la droite horizontale $y = k$ et on lit les abscisses des points d'intersection avec $\\mathcal{C}_f$.

### Inéquation $f(x) \\leq k$

Les solutions sont les valeurs de $x$ pour lesquelles la courbe est **en dessous** de la droite $y = k$ (ou sur la droite).

### Inéquation $f(x) \\geq g(x)$

Les solutions sont les valeurs de $x$ pour lesquelles la courbe de $f$ est **au-dessus** de celle de $g$.

---

## À retenir

- Une **fonction** associe à chaque $x$ une unique image $f(x)$.
- L'**image** se calcule (on substitue $x$) ; l'**antécédent** se trouve en résolvant $f(x) = b$.
- La **courbe représentative** $\\mathcal{C}_f$ est l'ensemble des points $(x, f(x))$.
- Le **tableau de variation** indique les intervalles de croissance et de décroissance.
""",
                'quiz': {
                    'titre': "Quiz — Notion de fonction",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Si $f(x) = 3x - 1$, quelle est l'image de 2 par $f$ ?",
                            'options': ["5", "7", "6", "1"],
                            'reponse_correcte': '0',
                            'explication': "$f(2) = 3 \\times 2 - 1 = 5$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "L'image d'un nombre $a$ par une fonction $f$ est :",
                            'options': ["$f(a)$", "$a$", "Le domaine de $f$", "L'antécédent de $a$"],
                            'reponse_correcte': '0',
                            'explication': "L'image de $a$ par $f$ est la valeur $f(a)$ obtenue en remplaçant $x$ par $a$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Un antécédent de 7 par $f(x) = 2x + 1$ est :",
                            'options': ["3", "15", "7", "4"],
                            'reponse_correcte': '0',
                            'explication': "On résout $2x + 1 = 7$, soit $2x = 6$, donc $x = 3$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Le domaine de définition de $f(x) = \\frac{1}{x - 3}$ est :",
                            'options': ["$\\mathbb{R} \\setminus \\{3\\}$", "$\\mathbb{R}$", "$\\mathbb{R} \\setminus \\{0\\}$", "$[3 \\,;\\, +\\infty[$"],
                            'reponse_correcte': '0',
                            'explication': "Le dénominateur $x - 3$ ne doit pas être nul, donc $x \\neq 3$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Sur la courbe d'une fonction, l'image de $a$ se lit :",
                            'options': ["Sur l'axe des ordonnées", "Sur l'axe des abscisses", "À l'origine du repère", "Sur la bissectrice"],
                            'reponse_correcte': '0',
                            'explication': "L'image $f(a)$ est l'ordonnée du point de la courbe d'abscisse $a$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Le domaine de définition de $g(x) = \\sqrt{x - 2}$ est :",
                            'options': ["$[2 \\,;\\, +\\infty[$", "$]2 \\,;\\, +\\infty[$", "$\\mathbb{R}$", "$]-\\infty \\,;\\, 2]$"],
                            'reponse_correcte': '0',
                            'explication': "Il faut $x - 2 \\geq 0$, soit $x \\geq 2$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Si $f(x) = x^2$, combien d'antécédents a le nombre 4 ?",
                            'options': ["2", "1", "0", "4"],
                            'reponse_correcte': '0',
                            'explication': "$x^2 = 4$ donne $x = 2$ ou $x = -2$, soit deux antécédents.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'vrai_faux',
                            'texte': "Un nombre peut avoir plusieurs antécédents par une même fonction.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Par exemple, pour $f(x) = x^2$, le nombre 9 a deux antécédents : 3 et $-3$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Si $f(x) = x^2 - 4x + 3$, quelle est l'image de 1 ?",
                            'options': ["0", "1", "$-1$", "2"],
                            'reponse_correcte': '0',
                            'explication': "$f(1) = 1 - 4 + 3 = 0$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Une fonction $f$ est dite croissante sur un intervalle $I$ si :",
                            'options': ["Pour tous $a < b$ dans $I$, $f(a) < f(b)$", "Pour tous $a < b$ dans $I$, $f(a) > f(b)$", "Sa courbe passe par l'origine", "$f(x) > 0$ pour tout $x$"],
                            'reponse_correcte': '0',
                            'explication': "Croissante signifie que l'image augmente quand $x$ augmente.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Le domaine de $h(x) = \\frac{\\sqrt{x}}{x - 1}$ est :",
                            'options': ["$[0 \\,;\\, 1[ \\cup ]1 \\,;\\, +\\infty[$", "$\\mathbb{R} \\setminus \\{1\\}$", "$[0 \\,;\\, +\\infty[$", "$]0 \\,;\\, +\\infty[$"],
                            'reponse_correcte': '0',
                            'explication': "Il faut $x \\geq 0$ (racine carrée) et $x \\neq 1$ (dénominateur non nul).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Pour résoudre graphiquement $f(x) = 3$, on trace :",
                            'options': ["La droite horizontale $y = 3$", "La droite verticale $x = 3$", "La tangente en $x = 3$", "La bissectrice $y = x$"],
                            'reponse_correcte': '0',
                            'explication': "On cherche les abscisses des points d'intersection entre la courbe et la droite $y = 3$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Si $f$ est décroissante sur $[1 \\,;\\, 5]$ avec $f(1) = 8$ et $f(5) = 2$, le maximum de $f$ sur cet intervalle est :",
                            'options': ["8", "2", "5", "1"],
                            'reponse_correcte': '0',
                            'explication': "$f$ est décroissante, donc le maximum est atteint au début de l'intervalle : $f(1) = 8$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Le nombre 0 a toujours un antécédent par n'importe quelle fonction.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La fonction constante $f(x) = 5$ n'a aucun antécédent pour 0.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Toute fonction définie sur $\\mathbb{R}$ est soit croissante soit décroissante.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Par exemple $f(x) = x^2$ est décroissante sur $]-\\infty \\,;\\, 0]$ puis croissante sur $[0 \\,;\\, +\\infty[$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'qcm',
                            'texte': "Si $f(x) = \\frac{1}{x - 1} + 2$, quelle est l'image de 2 par $f$ ?",
                            'options': ["3", "1", "2", "0"],
                            'reponse_correcte': '0',
                            'explication': "$f(2) = \\frac{1}{2 - 1} + 2 = 1 + 2 = 3$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "Si $f$ est croissante sur $[-3 \\,;\\, 5]$ avec $f(-3) = -4$ et $f(5) = 6$, combien de solutions a $f(x) = 0$ sur $[-3 \\,;\\, 5]$ ?",
                            'options': ["Exactement 1", "0", "2", "Une infinité"],
                            'reponse_correcte': '0',
                            'explication': "$f$ est croissante continue, $f(-3) = -4 < 0$ et $f(5) = 6 > 0$ : par le théorème des valeurs intermédiaires, il existe exactement une solution.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Si $f(x) = 5x - 3$, calculer $f(4)$.",
                            'options': None,
                            'reponse_correcte': '17',
                            'tolerances': ["17,0", "17.0"],
                            'explication': "$f(4) = 5 \\times 4 - 3 = 20 - 3 = 17$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Si $f(x) = 2x + 5$, quel est l'antécédent de 11 par $f$ ?",
                            'options': None,
                            'reponse_correcte': '3',
                            'tolerances': ["3,0", "3.0"],
                            'explication': "$2x + 5 = 11$, soit $2x = 6$, donc $x = 3$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Le domaine de $f(x) = \\sqrt{5 - x}$ est $]-\\infty \\,;\\, a]$. Quelle est la valeur de $a$ ?",
                            'options': None,
                            'reponse_correcte': '5',
                            'tolerances': ["5,0", "5.0"],
                            'explication': "Il faut $5 - x \\geq 0$, soit $x \\leq 5$. Donc $a = 5$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Fonctions affines f(x) = ax + b',
                'duree': 30,
                'contenu': """# Fonctions affines $f(x) = ax + b$

## Définition

Une **fonction affine** est une fonction de la forme :

$$f(x) = ax + b$$

où $a$ et $b$ sont deux constantes réelles.

- $a$ est le **coefficient directeur** (ou **pente**).
- $b$ est l'**ordonnée à l'origine** (la valeur de $f(0)$).

### Cas particuliers

| Condition | Type de fonction | Représentation graphique |
|-----------|-----------------|--------------------------|
| $b = 0$   | **Fonction linéaire** $f(x) = ax$ | Droite passant par l'origine |
| $a = 0$   | **Fonction constante** $f(x) = b$ | Droite horizontale |

---

## Représentation graphique

La courbe représentative d'une fonction affine est une **droite**.

### Tracer la droite

**Méthode :** deux points suffisent pour tracer une droite.

Pour $f(x) = 2x - 3$ :
- $f(0) = -3$ → le point $(0 \\,;\\, -3)$
- $f(2) = 1$ → le point $(2 \\,;\\, 1)$

On place ces deux points et on trace la droite qui les relie.

### Lire l'ordonnée à l'origine

$b = f(0)$ est le point où la droite **coupe l'axe des ordonnées** (l'axe vertical).

---

## Le coefficient directeur (pente)

### Définition

Le **coefficient directeur** (ou pente) mesure l'inclinaison de la droite. On le calcule à partir de deux points $(x_1, y_1)$ et $(x_2, y_2)$ de la droite :

$$a = \\frac{y_2 - y_1}{x_2 - x_1} = \\frac{\\Delta y}{\\Delta x}$$

### Interprétation

- Si $a > 0$ : la droite **monte** (de gauche à droite) → $f$ est **croissante**.
- Si $a < 0$ : la droite **descend** → $f$ est **décroissante**.
- Si $a = 0$ : la droite est **horizontale** → $f$ est **constante**.

> **Interprétation concrète :** $a$ représente la variation de $f(x)$ quand $x$ augmente de 1. Si $a = 3$, alors quand $x$ augmente de 1, $f(x)$ augmente de 3.

---

## Taux de variation

Le **taux de variation** de $f$ entre $x_1$ et $x_2$ est :

$$\\tau = \\frac{f(x_2) - f(x_1)}{x_2 - x_1}$$

Pour une fonction affine $f(x) = ax + b$, le taux de variation est **constant** et égal à $a$, quel que soit le choix de $x_1$ et $x_2$.

> **Propriété caractéristique :** « $f$ est affine $\\iff$ son taux de variation est constant. »

---

## Variations

| Coefficient directeur | Sens de variation | Tableau |
|----------------------|-------------------|---------|
| $a > 0$ | Croissante sur $\\mathbb{R}$ | Flèche montante $\\nearrow$ |
| $a < 0$ | Décroissante sur $\\mathbb{R}$ | Flèche descendante $\\searrow$ |
| $a = 0$ | Constante sur $\\mathbb{R}$ | Flèche horizontale $\\rightarrow$ |

---

## Déterminer une fonction affine

### Connaissant la pente et un point

Si la pente est $a$ et la droite passe par $(x_0, y_0)$ :

$$f(x) = a(x - x_0) + y_0$$

> **Exemple :** pente $a = -2$, passant par $(1, 5)$ :
> $f(x) = -2(x - 1) + 5 = -2x + 2 + 5 = -2x + 7$

### Connaissant deux points

On calcule d'abord la pente $a = \\frac{y_2 - y_1}{x_2 - x_1}$, puis on utilise un des points.

> **Exemple :** Points $(2, 3)$ et $(5, 9)$ :
> $a = \\frac{9 - 3}{5 - 2} = \\frac{6}{3} = 2$
>
> $f(x) = 2(x - 2) + 3 = 2x - 1$

---

## Signe d'une fonction affine

Pour $f(x) = ax + b$ avec $a \\neq 0$ :

- **Racine :** $f(x) = 0 \\iff x = -\\frac{b}{a}$
- Si $a > 0$ : $f(x) < 0$ pour $x < -\\frac{b}{a}$ et $f(x) > 0$ pour $x > -\\frac{b}{a}$
- Si $a < 0$ : $f(x) > 0$ pour $x < -\\frac{b}{a}$ et $f(x) < 0$ pour $x > -\\frac{b}{a}$

> **Règle mnémotechnique :** le signe de $f(x)$ est celui de $a$ « à droite » de la racine.

---

## À retenir

- $f(x) = ax + b$ : $a$ est la pente, $b$ l'ordonnée à l'origine.
- La représentation graphique est une **droite**.
- $a = \\frac{y_2 - y_1}{x_2 - x_1}$ (pente entre deux points).
- $a > 0$ → croissante ; $a < 0$ → décroissante ; $a = 0$ → constante.
- Le taux de variation d'une fonction affine est **constant** et égal à $a$.
""",
                'quiz': {
                    'titre': "Quiz — Fonctions affines",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Dans $f(x) = 3x + 2$, le coefficient directeur est :",
                            'options': ["3", "2", "5", "1"],
                            'reponse_correcte': '0',
                            'explication': "Dans $f(x) = ax + b$, le coefficient directeur est $a = 3$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "L'ordonnée à l'origine de $f(x) = -4x + 7$ est :",
                            'options': ["7", "$-4$", "4", "$-7$"],
                            'reponse_correcte': '0',
                            'explication': "$b = f(0) = 7$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "La représentation graphique d'une fonction affine est :",
                            'options': ["Une droite", "Une parabole", "Une hyperbole", "Un cercle"],
                            'reponse_correcte': '0',
                            'explication': "Toute fonction affine $f(x) = ax + b$ a pour courbe une droite.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Si $a > 0$ dans $f(x) = ax + b$, la fonction est :",
                            'options': ["Croissante", "Décroissante", "Constante", "Non définie"],
                            'reponse_correcte': '0',
                            'explication': "Un coefficient directeur positif signifie que la droite monte : $f$ est croissante.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La fonction $f(x) = 5x$ est appelée :",
                            'options': ["Fonction linéaire", "Fonction constante", "Fonction carré", "Fonction inverse"],
                            'reponse_correcte': '0',
                            'explication': "$f(x) = ax$ avec $b = 0$ : c'est une fonction linéaire (droite passant par l'origine).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "La pente de la droite passant par $A(1 \\,;\\, 3)$ et $B(3 \\,;\\, 7)$ est :",
                            'options': ["2", "4", "3", "5"],
                            'reponse_correcte': '0',
                            'explication': "$a = \\frac{7 - 3}{3 - 1} = \\frac{4}{2} = 2$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Si $f(x) = -2x + 6$, quelle est la valeur de $f(0)$ ?",
                            'options': ["6", "$-2$", "0", "4"],
                            'reponse_correcte': '0',
                            'explication': "$f(0) = -2 \\times 0 + 6 = 6$ : c'est l'ordonnée à l'origine.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'vrai_faux',
                            'texte': "La droite représentant $f(x) = 4$ est horizontale.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$f(x) = 4$ est une fonction constante ($a = 0$), sa droite est horizontale à hauteur $y = 4$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Le taux de variation de $f(x) = -3x + 1$ entre $x = 2$ et $x = 5$ est :",
                            'options': ["$-3$", "3", "$-9$", "1"],
                            'reponse_correcte': '0',
                            'explication': "Pour une fonction affine, le taux de variation est constant et égal à $a = -3$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "La droite passant par $A(0 \\,;\\, -1)$ et $B(2 \\,;\\, 5)$ a pour équation :",
                            'options': ["$y = 3x - 1$", "$y = 2x - 1$", "$y = 3x + 1$", "$y = -3x + 5$"],
                            'reponse_correcte': '0',
                            'explication': "$a = \\frac{5 - (-1)}{2 - 0} = 3$ et $b = -1$ (ordonnée de $A$). Donc $y = 3x - 1$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "La racine (zéro) de $f(x) = 2x - 8$ est :",
                            'options': ["4", "$-4$", "8", "2"],
                            'reponse_correcte': '0',
                            'explication': "$2x - 8 = 0$, soit $x = 4$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Si $f(x) = -x + 3$, sur quel intervalle $f(x) > 0$ ?",
                            'options': ["$]-\\infty \\,;\\, 3[$", "$]3 \\,;\\, +\\infty[$", "$]-\\infty \\,;\\, -3[$", "$[-3 \\,;\\, 3]$"],
                            'reponse_correcte': '0',
                            'explication': "$-x + 3 > 0 \\iff x < 3$, soit $]-\\infty \\,;\\, 3[$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Soit $f$ affine telle que $f(1) = 4$ et $f(3) = 10$. L'expression de $f(x)$ est :",
                            'options': ["$3x + 1$", "$2x + 2$", "$3x + 4$", "$5x - 1$"],
                            'reponse_correcte': '0',
                            'explication': "$a = \\frac{10 - 4}{3 - 1} = 3$. $f(x) = 3x + b$, $f(1) = 3 + b = 4$ donc $b = 1$. $f(x) = 3x + 1$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Le taux de variation d'une fonction affine dépend de l'intervalle choisi.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le taux de variation d'une fonction affine est constant, toujours égal au coefficient directeur $a$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Deux droites parallèles (non verticales) ont le même coefficient directeur.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Deux droites non verticales sont parallèles si et seulement si elles ont la même pente.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'qcm',
                            'texte': "La droite de pente $-2$ passant par le point $(3 \\,;\\, 1)$ a pour ordonnée à l'origine :",
                            'options': ["7", "$-5$", "1", "3"],
                            'reponse_correcte': '0',
                            'explication': "$y = -2x + b$. En $(3 \\,;\\, 1)$ : $1 = -6 + b$, donc $b = 7$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "Si $f(x) = ax + b$ avec $f(2) = 1$ et $f(-1) = 7$, la valeur de $a$ est :",
                            'options': ["$-2$", "2", "$-3$", "3"],
                            'reponse_correcte': '0',
                            'explication': "$a = \\frac{7 - 1}{-1 - 2} = \\frac{6}{-3} = -2$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer $f(3)$ pour $f(x) = -2x + 11$.",
                            'options': None,
                            'reponse_correcte': '5',
                            'tolerances': ["5,0", "5.0"],
                            'explication': "$f(3) = -6 + 11 = 5$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "La droite $y = ax + 3$ passe par le point $(4 \\,;\\, -5)$. Quelle est la valeur de $a$ ?",
                            'options': None,
                            'reponse_correcte': '-2',
                            'tolerances': ["-2,0", "-2.0"],
                            'explication': "$-5 = 4a + 3$, soit $4a = -8$, donc $a = -2$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "La racine de $f(x) = 5x - 15$ est $x = $ ?",
                            'options': None,
                            'reponse_correcte': '3',
                            'tolerances': ["3,0", "3.0"],
                            'explication': "$5x - 15 = 0$, soit $x = 3$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },

    # ──────────────────────────────────────────────
    # CHAPITRE 6 — Fonctions carré et inverse
    # ──────────────────────────────────────────────
    {
        'ordre': 6,
        'titre': 'Fonctions carré et inverse',
        'description': "Étude des fonctions carré, inverse et racine carrée. Forme canonique d'un trinôme du second degré.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Fonction carré f(x) = x²',
                'duree': 30,
                'contenu': """# Fonction carré $f(x) = x^2$

## Définition et propriétés de base

La **fonction carré** est définie sur $\\mathbb{R}$ par :

$$f(x) = x^2$$

Elle associe à chaque nombre réel son **carré**.

**Valeurs remarquables :**

| $x$    | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|--------|------|------|------|-----|-----|-----|-----|
| $f(x)$ | $9$  | $4$  | $1$  | $0$ | $1$ | $4$ | $9$ |

---

## Courbe représentative : la parabole

La courbe de la fonction carré est une **parabole** dont le sommet est à l'origine $O(0;0)$.

Elle a la forme d'un « U » ouvert vers le haut.

### Propriétés de la courbe

- **Domaine de définition :** $D_f = \\mathbb{R}$.
- **Ensemble image :** $f(\\mathbb{R}) = [0 \\,;\\, +\\infty[$ (un carré est toujours positif ou nul).
- **Sommet de la parabole :** $O(0;0)$, le minimum de $f$.

---

## Parité

La fonction carré est **paire** :

$$f(-x) = (-x)^2 = x^2 = f(x)$$

pour tout $x \\in \\mathbb{R}$.

**Conséquence géométrique :** la parabole est **symétrique par rapport à l'axe des ordonnées** (la droite $x = 0$).

> **Interprétation :** $(-3)^2 = 9 = 3^2$. Les nombres opposés ont la même image par la fonction carré.

---

## Variations

La fonction carré est :

- **Décroissante** sur $]-\\infty \\,;\\, 0]$ : si $a < b \\leq 0$, alors $a^2 > b^2$.
- **Croissante** sur $[0 \\,;\\, +\\infty[$ : si $0 \\leq a < b$, alors $a^2 < b^2$.

**Tableau de variation :**

| $x$    | $-\\infty$ |       | $0$ |       | $+\\infty$ |
|--------|-----------|-------|-----|-------|-----------|
| $f(x)$ |           | $\\searrow$ | $0$ | $\\nearrow$ |           |

> **Attention :** On ne peut **pas** comparer $a^2$ et $b^2$ directement si $a$ et $b$ ne sont pas du même signe. Par exemple, $(-5)^2 = 25 > 4 = 2^2$, mais $-5 < 2$.

---

## Comparaison de carrés

### Si $a$ et $b$ sont positifs

$$0 \\leq a < b \\implies a^2 < b^2$$

### Si $a$ et $b$ sont négatifs

$$a < b \\leq 0 \\implies a^2 > b^2$$

> L'ordre est **inversé** pour les nombres négatifs.

---

## La fonction $f(x) = ax^2$ (parabole homothétique)

Pour $a > 0$ :
- Plus $a$ est grand, plus la parabole est **resserrée** (étroite).
- Plus $a$ est petit (proche de 0), plus elle est **aplatie** (évasée).

Pour $a < 0$ : la parabole est **retournée** (ouverte vers le bas).

---

## Résolution graphique de $x^2 = k$

Pour un réel $k$ :

| Valeur de $k$ | Solutions de $x^2 = k$              |
|---------------|-------------------------------------|
| $k < 0$       | Aucune solution                     |
| $k = 0$       | $x = 0$ (solution unique)           |
| $k > 0$       | $x = \\sqrt{k}$ ou $x = -\\sqrt{k}$ |

---

## Inéquations avec la fonction carré

**Résoudre $x^2 \\leq 9$ :**

$$x^2 \\leq 9 \\iff x^2 - 9 \\leq 0 \\iff (x-3)(x+3) \\leq 0 \\iff -3 \\leq x \\leq 3$$

$$S = [-3 \\,;\\, 3]$$

**Résoudre $x^2 > 4$ :**

$$x^2 > 4 \\iff x < -2 \\text{ ou } x > 2$$

$$S = ]-\\infty \\,;\\, -2[ \\cup ]2 \\,;\\, +\\infty[$$

---

## À retenir

- $f(x) = x^2$ est une **parabole** de sommet $O(0;0)$.
- Fonction **paire** : $f(-x) = f(x)$ → symétrie par rapport à l'axe des ordonnées.
- **Décroissante** sur $]-\\infty; 0]$ et **croissante** sur $[0; +\\infty[$.
- Un carré est toujours $\\geq 0$.
- $x^2 = k$ a deux solutions (si $k > 0$), une (si $k = 0$), aucune (si $k < 0$).
""",
                'quiz': {
                    'titre': "Quiz — Fonction carré",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "La fonction $f(x) = x^2$ est définie sur :",
                            'options': ["$\\mathbb{R}$ (tous les réels)", "$[0 \\,;\\, +\\infty[$", "$\\mathbb{R}^*$", "$]-\\infty \\,;\\, 0]$"],
                            'reponse_correcte': '0',
                            'explication': "On peut calculer le carré de tout nombre réel.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "L'image de $-3$ par la fonction carré est :",
                            'options': ["9", "$-9$", "6", "$-6$"],
                            'reponse_correcte': '0',
                            'explication': "$(-3)^2 = 9$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "La courbe de la fonction carré est :",
                            'options': ["Une parabole", "Une droite", "Une hyperbole", "Un cercle"],
                            'reponse_correcte': '0',
                            'explication': "La courbe de $f(x) = x^2$ est une parabole de sommet $O(0;0)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "La fonction carré est paire, ce qui signifie :",
                            'options': ["$f(-x) = f(x)$ pour tout $x$", "$f(-x) = -f(x)$ pour tout $x$", "$f(0) = 0$", "Elle est toujours croissante"],
                            'reponse_correcte': '0',
                            'explication': "Paire signifie $f(-x) = f(x)$ : la courbe est symétrique par rapport à l'axe des ordonnées.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "L'ensemble des images de la fonction carré est :",
                            'options': ["$[0 \\,;\\, +\\infty[$", "$\\mathbb{R}$", "$]0 \\,;\\, +\\infty[$", "$]-\\infty \\,;\\, 0]$"],
                            'reponse_correcte': '0',
                            'explication': "Un carré est toujours positif ou nul, et tout réel positif est atteint.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Sur quel intervalle la fonction carré est-elle croissante ?",
                            'options': ["$[0 \\,;\\, +\\infty[$", "$]-\\infty \\,;\\, 0]$", "$\\mathbb{R}$", "$]-1 \\,;\\, 1[$"],
                            'reponse_correcte': '0',
                            'explication': "La fonction carré est croissante sur $[0 \\,;\\, +\\infty[$ et décroissante sur $]-\\infty \\,;\\, 0]$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Le sommet de la parabole $y = x^2$ est :",
                            'options': ["$(0 \\,;\\, 0)$", "$(1 \\,;\\, 1)$", "$(0 \\,;\\, 1)$", "$(1 \\,;\\, 0)$"],
                            'reponse_correcte': '0',
                            'explication': "Le minimum de $x^2$ est $0$, atteint en $x = 0$ : le sommet est $(0;0)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'vrai_faux',
                            'texte': "$(-5)^2 = 5^2$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$(-5)^2 = 25 = 5^2$. C'est la propriété de parité de la fonction carré : $f(-x) = f(x)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Si $a$ et $b$ sont négatifs avec $a < b$, alors :",
                            'options': ["$a^2 > b^2$", "$a^2 < b^2$", "$a^2 = b^2$", "On ne peut pas comparer"],
                            'reponse_correcte': '0',
                            'explication': "Pour des négatifs, l'ordre est inversé par la fonction carré : si $a < b \\leq 0$, alors $a^2 > b^2$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Les solutions de $x^2 = 16$ sont :",
                            'options': ["$x = 4$ ou $x = -4$", "$x = 4$ uniquement", "$x = 16$", "$x = 8$ ou $x = -8$"],
                            'reponse_correcte': '0',
                            'explication': "$x^2 = 16$ donne $x = \\sqrt{16} = 4$ ou $x = -\\sqrt{16} = -4$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "L'ensemble solution de $x^2 \\leq 25$ est :",
                            'options': ["$[-5 \\,;\\, 5]$", "$[0 \\,;\\, 5]$", "$]-\\infty \\,;\\, 5]$", "$[5 \\,;\\, +\\infty[$"],
                            'reponse_correcte': '0',
                            'explication': "$x^2 \\leq 25 \\iff -5 \\leq x \\leq 5$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "L'ensemble solution de $x^2 > 1$ est :",
                            'options': ["$]-\\infty \\,;\\, -1[ \\cup ]1 \\,;\\, +\\infty[$", "$]-1 \\,;\\, 1[$", "$[1 \\,;\\, +\\infty[$", "$]-\\infty \\,;\\, -1]$"],
                            'reponse_correcte': '0',
                            'explication': "$x^2 > 1 \\iff x < -1$ ou $x > 1$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Pour $a > 0$, si $a$ augmente, la parabole $y = ax^2$ :",
                            'options': ["Se resserre (devient plus étroite)", "S'aplatit (devient plus évasée)", "Se déplace vers la droite", "Se retourne"],
                            'reponse_correcte': '0',
                            'explication': "Plus $a$ est grand, plus la parabole est resserrée autour de l'axe des ordonnées.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Si $a < 0$, la parabole $y = ax^2$ est ouverte vers le bas.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Quand $a < 0$, la parabole est retournée et ouverte vers le bas.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "La fonction carré est décroissante sur $]-\\infty \\,;\\, 0]$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Pour $a < b \\leq 0$, on a $a^2 > b^2$ : la fonction carré est bien décroissante sur $]-\\infty \\,;\\, 0]$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'qcm',
                            'texte': "L'équation $x^2 = -4$ a :",
                            'options': ["Aucune solution réelle", "Deux solutions", "Une solution", "Une infinité de solutions"],
                            'reponse_correcte': '0',
                            'explication': "Un carré est toujours $\\geq 0$, donc $x^2 = -4$ n'a aucune solution dans $\\mathbb{R}$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "Si $-2 \\leq x \\leq 3$, quel est le maximum de $x^2$ ?",
                            'options': ["9", "4", "3", "0"],
                            'reponse_correcte': '0',
                            'explication': "On compare les carrés aux bornes : $(-2)^2 = 4$ et $3^2 = 9$. Le maximum est $9$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer $(-7)^2$.",
                            'options': None,
                            'reponse_correcte': '49',
                            'tolerances': ["49,0", "49.0"],
                            'explication': "$(-7)^2 = (-7) \\times (-7) = 49$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "L'équation $x^2 = 36$ a deux solutions. Quelle est la solution négative ?",
                            'options': None,
                            'reponse_correcte': '-6',
                            'tolerances': ["-6,0", "-6.0"],
                            'explication': "$x^2 = 36$ donne $x = 6$ ou $x = -6$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Si $-3 \\leq x \\leq 5$, quel est le minimum de $x^2$ ?",
                            'options': None,
                            'reponse_correcte': '0',
                            'tolerances': ["0,0", "0.0"],
                            'explication': "Comme $0 \\in [-3 \\,;\\, 5]$ et que $x^2 \\geq 0$, le minimum est $0^2 = 0$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Fonction inverse et forme canonique',
                'duree': 35,
                'contenu': """# Fonction inverse et forme canonique

## La fonction inverse : $g(x) = \\frac{1}{x}$

### Définition et domaine

La **fonction inverse** est définie par :

$$g(x) = \\frac{1}{x}$$

**Domaine de définition :** $D_g = \\mathbb{R}^* = \\mathbb{R} \\setminus \\{0\\}$ (on ne peut pas diviser par 0).

**Valeurs remarquables :**

| $x$    | $-4$   | $-2$   | $-1$ | $-0{,}5$ | $0{,}5$ | $1$ | $2$   | $4$    |
|--------|--------|--------|------|----------|---------|-----|-------|--------|
| $g(x)$ | $-0{,}25$ | $-0{,}5$ | $-1$ | $-2$  | $2$     | $1$ | $0{,}5$ | $0{,}25$ |

---

### Imparité

La fonction inverse est **impaire** :

$$g(-x) = \\frac{1}{-x} = -\\frac{1}{x} = -g(x)$$

**Conséquence géométrique :** la courbe (une **hyperbole**) est symétrique par rapport à l'**origine** $O$.

---

### Variations

La fonction inverse est **strictement décroissante** sur chacun de ses intervalles de définition :

- Décroissante sur $]-\\infty \\,;\\, 0[$
- Décroissante sur $]0 \\,;\\, +\\infty[$

> ⚠️ On ne peut **pas** dire que $g$ est décroissante sur $\\mathbb{R}^*$ tout entier. Par exemple $g(-1) = -1 < 1 = g(1)$ alors que $-1 < 1$ : l'ordre n'est pas inversé entre les deux intervalles.

**Tableau de variation :**

| $x$    | $-\\infty$ |                 | $0$          |                 | $+\\infty$ |
|--------|-----------|-----------------|--------------|-----------------|-----------|
| $g(x)$ | $0$       | $\\searrow$      | $\\pm\\infty$ | $\\searrow$      | $0$       |

---

### Asymptotes

La courbe de la fonction inverse possède deux **asymptotes** :

- **Asymptote verticale** $x = 0$ : quand $x$ tend vers 0, $g(x)$ tend vers $\\pm\\infty$.
- **Asymptote horizontale** $y = 0$ : quand $x$ tend vers $\\pm\\infty$, $g(x)$ tend vers 0.

> La courbe se **rapproche** de ces droites sans jamais les toucher.

---

### Comparaison

Pour deux réels **positifs** $a$ et $b$ :

$$0 < a < b \\implies \\frac{1}{a} > \\frac{1}{b}$$

> L'ordre est **inversé** en passant à l'inverse (pour des nombres de même signe).

---

## La fonction racine carrée : $h(x) = \\sqrt{x}$

### Définition

$$h(x) = \\sqrt{x}$$

**Domaine :** $D_h = [0 \\,;\\, +\\infty[$ (on ne peut calculer la racine carrée que de nombres positifs ou nuls).

### Propriétés

- $\\sqrt{x} \\geq 0$ pour tout $x \\geq 0$.
- $(\\sqrt{x})^2 = x$ et $\\sqrt{x^2} = |x|$.
- $\\sqrt{ab} = \\sqrt{a} \\times \\sqrt{b}$ pour $a, b \\geq 0$.
- $\\sqrt{\\frac{a}{b}} = \\frac{\\sqrt{a}}{\\sqrt{b}}$ pour $a \\geq 0,\\; b > 0$.

### Variations

La fonction racine carrée est **strictement croissante** sur $[0 \\,;\\, +\\infty[$ :

$$0 \\leq a < b \\implies \\sqrt{a} < \\sqrt{b}$$

---

## Forme canonique d'un trinôme du second degré

### Trinôme du second degré

On appelle **trinôme du second degré** toute fonction de la forme :

$$f(x) = ax^2 + bx + c \\quad \\text{avec } a \\neq 0$$

Sa courbe représentative est une **parabole**.

### Forme canonique

Tout trinôme $ax^2 + bx + c$ peut s'écrire sous la **forme canonique** :

$$f(x) = a(x - h)^2 + k$$

avec :

$$h = -\\frac{b}{2a} \\qquad \\text{et} \\qquad k = f(h) = c - \\frac{b^2}{4a}$$

### Interprétation graphique

Le point $(h, k)$ est le **sommet** de la parabole.

- Si $a > 0$ : la parabole est ouverte **vers le haut** → $k$ est le **minimum** de $f$.
- Si $a < 0$ : la parabole est ouverte **vers le bas** → $k$ est le **maximum** de $f$.

La droite $x = h$ est l'**axe de symétrie** de la parabole.

### Exemple

Mettons $f(x) = 2x^2 - 12x + 22$ sous forme canonique.

$$h = -\\frac{-12}{2 \\times 2} = \\frac{12}{4} = 3$$

$$k = f(3) = 2 \\times 9 - 12 \\times 3 + 22 = 18 - 36 + 22 = 4$$

$$f(x) = 2(x-3)^2 + 4$$

**Vérification par développement :**
$2(x-3)^2 + 4 = 2(x^2 - 6x + 9) + 4 = 2x^2 - 12x + 18 + 4 = 2x^2 - 12x + 22$ ✓

Le sommet est $(3, 4)$ et comme $a = 2 > 0$, le minimum de $f$ est $4$, atteint en $x = 3$.

### Variations du trinôme

Si $a > 0$ : $f$ **décroissante** sur $]-\\infty; h]$, **croissante** sur $[h; +\\infty[$.

Si $a < 0$ : $f$ **croissante** sur $]-\\infty; h]$, **décroissante** sur $[h; +\\infty[$.

---

## À retenir

- $g(x) = \\frac{1}{x}$ est définie sur $\\mathbb{R}^*$, **impaire**, décroissante sur chaque intervalle de son domaine.
- La courbe de la fonction inverse est une **hyperbole** avec des asymptotes $x=0$ et $y=0$.
- $h(x) = \\sqrt{x}$ est définie sur $[0;+\\infty[$, **croissante**.
- La **forme canonique** $a(x-h)^2 + k$ donne le sommet $(h,k)$ de la parabole.
- $h = -\\frac{b}{2a}$ et $k = f(h)$.
""",
                'quiz': {
                    'titre': "Quiz — Fonction inverse et forme canonique",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Le domaine de définition de $g(x) = \\frac{1}{x}$ est :",
                            'options': ["$\\mathbb{R}^* = \\mathbb{R} \\setminus \\{0\\}$", "$\\mathbb{R}$", "$[0 \\,;\\, +\\infty[$", "$]0 \\,;\\, +\\infty[$"],
                            'reponse_correcte': '0',
                            'explication': "On ne peut pas diviser par 0, donc $x \\neq 0$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "La fonction inverse est :",
                            'options': ["Impaire", "Paire", "Ni paire ni impaire", "Constante"],
                            'reponse_correcte': '0',
                            'explication': "$g(-x) = \\frac{1}{-x} = -\\frac{1}{x} = -g(x)$ : la fonction est impaire.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "La valeur de $\\frac{1}{2}$ est :",
                            'options': ["$0{,}5$", "2", "0", "1"],
                            'reponse_correcte': '0',
                            'explication': "$\\frac{1}{2} = 0{,}5$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "La courbe de la fonction inverse possède une asymptote verticale d'équation :",
                            'options': ["$x = 0$", "$y = 0$", "$x = 1$", "$y = 1$"],
                            'reponse_correcte': '0',
                            'explication': "Quand $x$ tend vers 0, $\\frac{1}{x}$ tend vers $\\pm\\infty$ : l'asymptote verticale est $x = 0$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Le domaine de la fonction racine carrée $h(x) = \\sqrt{x}$ est :",
                            'options': ["$[0 \\,;\\, +\\infty[$", "$\\mathbb{R}$", "$\\mathbb{R}^*$", "$]0 \\,;\\, +\\infty[$"],
                            'reponse_correcte': '0',
                            'explication': "On ne peut calculer la racine carrée que de nombres positifs ou nuls.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "La courbe de la fonction inverse est appelée :",
                            'options': ["Une hyperbole", "Une parabole", "Une droite", "Un cercle"],
                            'reponse_correcte': '0',
                            'explication': "La courbe de $g(x) = \\frac{1}{x}$ est une hyperbole.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Si $0 < a < b$, alors :",
                            'options': ["$\\frac{1}{a} > \\frac{1}{b}$", "$\\frac{1}{a} < \\frac{1}{b}$", "$\\frac{1}{a} = \\frac{1}{b}$", "On ne peut pas comparer"],
                            'reponse_correcte': '0',
                            'explication': "Pour des réels strictement positifs, l'ordre est inversé en passant à l'inverse.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'vrai_faux',
                            'texte': "La fonction $h(x) = \\sqrt{x}$ est croissante sur son domaine.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Pour $0 \\leq a < b$, on a $\\sqrt{a} < \\sqrt{b}$ : la fonction racine carrée est croissante.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Pour le trinôme $f(x) = 2x^2 - 8x + 3$, la valeur de $h = -\\frac{b}{2a}$ est :",
                            'options': ["2", "$-2$", "4", "$-4$"],
                            'reponse_correcte': '0',
                            'explication': "$h = -\\frac{-8}{2 \\times 2} = \\frac{8}{4} = 2$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "La forme canonique de $f(x) = x^2 - 6x + 11$ est :",
                            'options': ["$(x - 3)^2 + 2$", "$(x + 3)^2 + 2$", "$(x - 3)^2 - 2$", "$(x - 6)^2 + 11$"],
                            'reponse_correcte': '0',
                            'explication': "$h = 3$, $k = f(3) = 9 - 18 + 11 = 2$. Donc $f(x) = (x - 3)^2 + 2$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Le sommet de la parabole $f(x) = -x^2 + 4x - 1$ est :",
                            'options': ["$(2 \\,;\\, 3)$", "$(2 \\,;\\, -3)$", "$(-2 \\,;\\, 3)$", "$(4 \\,;\\, -1)$"],
                            'reponse_correcte': '0',
                            'explication': "$h = -\\frac{4}{2 \\times (-1)} = 2$, $k = f(2) = -4 + 8 - 1 = 3$. Sommet $(2 \\,;\\, 3)$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Si $a > 0$ dans $f(x) = a(x - h)^2 + k$, le sommet $(h \\,;\\, k)$ correspond à :",
                            'options': ["Le minimum de $f$", "Le maximum de $f$", "Un point d'inflexion", "L'ordonnée à l'origine"],
                            'reponse_correcte': '0',
                            'explication': "Quand $a > 0$, la parabole est ouverte vers le haut et le sommet est le point le plus bas.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "La fonction inverse est décroissante sur :",
                            'options': ["$]-\\infty \\,;\\, 0[$ et sur $]0 \\,;\\, +\\infty[$ séparément", "$\\mathbb{R}$ tout entier", "$\\mathbb{R}^*$ tout entier", "Uniquement $[1 \\,;\\, +\\infty[$"],
                            'reponse_correcte': '0',
                            'explication': "La fonction inverse est décroissante sur chacun des deux intervalles de son domaine, mais pas sur $\\mathbb{R}^*$ entier.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "$\\sqrt{a \\times b} = \\sqrt{a} \\times \\sqrt{b}$ pour tous réels $a \\geq 0$ et $b \\geq 0$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est une propriété fondamentale de la racine carrée, valide pour $a \\geq 0$ et $b \\geq 0$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "$\\sqrt{x^2} = x$ pour tout réel $x$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "$\\sqrt{x^2} = |x|$. Par exemple $\\sqrt{(-3)^2} = \\sqrt{9} = 3 \\neq -3$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'qcm',
                            'texte': "La forme canonique de $f(x) = 3x^2 + 12x + 7$ est :",
                            'options': ["$3(x + 2)^2 - 5$", "$3(x - 2)^2 + 5$", "$3(x + 2)^2 + 7$", "$3(x + 4)^2 - 5$"],
                            'reponse_correcte': '0',
                            'explication': "$h = -\\frac{12}{6} = -2$, $k = f(-2) = 12 - 24 + 7 = -5$. Donc $f(x) = 3(x + 2)^2 - 5$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 17,
                            'type': 'qcm',
                            'texte': "La parabole $f(x) = -2(x - 1)^2 + 8$ a son maximum en :",
                            'options': ["$(1 \\,;\\, 8)$", "$(-1 \\,;\\, 8)$", "$(1 \\,;\\, -8)$", "$(2 \\,;\\, 8)$"],
                            'reponse_correcte': '0',
                            'explication': "$a = -2 < 0$, donc le sommet $(1 \\,;\\, 8)$ est un maximum.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer $\\frac{1}{4}$ sous forme décimale.",
                            'options': None,
                            'reponse_correcte': '0,25',
                            'tolerances': ["0.25", "1/4", "0,250"],
                            'explication': "$\\frac{1}{4} = 0{,}25$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Soit $f(x) = x^2 - 10x + 21$. Calculer $h = -\\frac{b}{2a}$.",
                            'options': None,
                            'reponse_correcte': '5',
                            'tolerances': ["5,0", "5.0"],
                            'explication': "$h = -\\frac{-10}{2 \\times 1} = \\frac{10}{2} = 5$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Le sommet de $f(x) = (x - 4)^2 - 9$ est $(h \\,;\\, k)$. Quelle est la valeur de $k$ ?",
                            'options': None,
                            'reponse_correcte': '-9',
                            'tolerances': ["-9,0", "-9.0"],
                            'explication': "La forme canonique $a(x - h)^2 + k$ donne directement $h = 4$ et $k = -9$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 7 — Statistiques et probabilités
    # ──────────────────────────────────────────────
    {
        'ordre': 7,
        'titre': 'Statistiques et probabilités',
        'description': "Indicateurs statistiques (moyenne, médiane, écart-type), pourcentages d'évolution, vocabulaire des probabilités et calculs élémentaires.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Statistiques descriptives — indicateurs de position et de dispersion',
                'duree': 40,
                'contenu': """# Statistiques descriptives — indicateurs de position et de dispersion

## Introduction

Les **statistiques descriptives** permettent de résumer et d'analyser un ensemble de données numériques. Plutôt que de lire des centaines de valeurs, on calcule quelques nombres clés — les **indicateurs** — qui caractérisent la série.

On distingue deux familles d'indicateurs :

- les **indicateurs de position** (ou de tendance centrale) : ils indiquent *où* se situent les données ;
- les **indicateurs de dispersion** : ils mesurent *comment* les données sont réparties autour de la valeur centrale.

---

## Vocabulaire

### Série statistique

Une **série statistique** est un ensemble de données collectées lors d'une étude. Chaque donnée est une valeur prise par un **caractère** (ou variable statistique).

| Terme | Signification |
|-------|---------------|
| **Population** | Ensemble des individus étudiés |
| **Caractère** | Propriété observée (ex : note, taille) |
| **Modalité / valeur** | Valeur possible du caractère |
| **Effectif** $n_i$ | Nombre d'individus ayant la valeur $x_i$ |
| **Effectif total** $N$ | $N = \\sum n_i$ |
| **Fréquence** $f_i$ | $f_i = \\dfrac{n_i}{N}$ (proportion) |
| **Effectif cumulé croissant (ECC)** | Somme des effectifs des valeurs $\\leq x_i$ |

---

## Indicateurs de position

### Moyenne arithmétique

La **moyenne** $\\bar{x}$ d'une série de valeurs $x_1, x_2, \\ldots, x_p$ ayant les effectifs $n_1, n_2, \\ldots, n_p$ est :

$$\\bar{x} = \\frac{\\sum_{i=1}^{p} n_i \\, x_i}{N} = \\frac{n_1 x_1 + n_2 x_2 + \\cdots + n_p x_p}{N}$$

> La moyenne est sensible aux **valeurs extrêmes** : une seule donnée très grande ou très petite peut la faire varier fortement.

#### Exemple

Un élève obtient les notes suivantes en mathématiques :

| Note $x_i$ | 8 | 12 | 14 | 16 |
|------------|---|----|----|-----|
| Effectif $n_i$ | 1 | 3 | 4 | 2 |

$$\\bar{x} = \\frac{1 \\times 8 + 3 \\times 12 + 4 \\times 14 + 2 \\times 16}{1+3+4+2} = \\frac{8 + 36 + 56 + 32}{10} = \\frac{132}{10} = 13{,}2$$

### Médiane

La **médiane** $Me$ est la valeur qui partage la série **ordonnée** en deux groupes de même effectif : 50 % des valeurs sont inférieures ou égales à $Me$, 50 % sont supérieures ou égales.

**Méthode de calcul :**

1. Ranger les $N$ valeurs par **ordre croissant**.
2. Si $N$ est **impair** : $Me$ est la valeur de rang $\\dfrac{N+1}{2}$.
3. Si $N$ est **pair** : $Me$ est la **demi-somme** des valeurs de rangs $\\dfrac{N}{2}$ et $\\dfrac{N}{2}+1$.

#### Exemple (N impair)

Série ordonnée : $3, 5, 7, 9, 11$ → $N = 5$ → rang $\\frac{5+1}{2} = 3$ → $Me = 7$.

#### Exemple (N pair)

Série ordonnée : $4, 6, 8, 10, 12, 14$ → $N = 6$ → rangs 3 et 4 → $Me = \\frac{8+10}{2} = 9$.

> Contrairement à la moyenne, la médiane est **robuste** face aux valeurs extrêmes.

### Mode

Le **mode** est la valeur ayant le **plus grand effectif** (la plus fréquente). Une série peut être **bimodale** (deux modes) ou **amodale** (toutes les valeurs ont le même effectif).

---

## Indicateurs de dispersion

### Étendue

L'**étendue** $e$ est la différence entre la plus grande et la plus petite valeur :

$$e = x_{\\max} - x_{\\min}$$

C'est un indicateur simple mais très sensible aux valeurs extrêmes.

### Quartiles et écart interquartile

Les **quartiles** partagent la série ordonnée en quatre groupes de même effectif (environ 25 % chacun) :

| Quartile | Notation | Signification |
|----------|----------|---------------|
| Premier quartile | $Q_1$ | 25 % des valeurs sont $\\leq Q_1$ |
| Deuxième quartile | $Q_2 = Me$ | 50 % des valeurs sont $\\leq Q_2$ |
| Troisième quartile | $Q_3$ | 75 % des valeurs sont $\\leq Q_3$ |

**Pour trouver $Q_1$ :** c'est la plus petite valeur $x$ telle que au moins 25 % des données soient inférieures ou égales à $x$.

**Pour trouver $Q_3$ :** c'est la plus petite valeur $x$ telle que au moins 75 % des données soient inférieures ou égales à $x$.

L'**écart interquartile** est :

$$\\text{IQR} = Q_3 - Q_1$$

Il mesure la dispersion des 50 % centraux de la série. Plus il est petit, plus les valeurs sont concentrées.

### Variance et écart-type

La **variance** $V$ mesure la dispersion des valeurs autour de la moyenne :

$$V = \\frac{1}{N} \\sum_{i=1}^{p} n_i (x_i - \\bar{x})^2$$

C'est la **moyenne des carrés des écarts à la moyenne**.

L'**écart-type** $\\sigma$ est la racine carrée de la variance :

$$\\sigma = \\sqrt{V}$$

> L'écart-type est exprimé dans la **même unité** que les données, ce qui le rend plus facile à interpréter que la variance.

#### Exemple

Reprenons la série de notes ($\\bar{x} = 13{,}2$) :

$$V = \\frac{1 \\times (8-13{,}2)^2 + 3 \\times (12-13{,}2)^2 + 4 \\times (14-13{,}2)^2 + 2 \\times (16-13{,}2)^2}{10}$$

$$V = \\frac{27{,}04 + 4{,}32 + 2{,}56 + 15{,}68}{10} = \\frac{49{,}6}{10} = 4{,}96$$

$$\\sigma = \\sqrt{4{,}96} \\approx 2{,}23$$

Les notes s'écartent en moyenne d'environ $2{,}2$ points de la moyenne.

---

## Diagramme en boîte (box-plot)

Le **diagramme en boîte** résume visuellement une série grâce aux cinq valeurs clés :

$$x_{\\min}, \\quad Q_1, \\quad Me, \\quad Q_3, \\quad x_{\\max}$$

La « boîte » va de $Q_1$ à $Q_3$ (contient 50 % des données), un trait marque la médiane à l'intérieur, et les « moustaches » s'étendent jusqu'aux extrema.

---

## Pourcentages et évolution

### Proportion et pourcentage

Une **proportion** est un nombre entre 0 et 1. Un **pourcentage** est une proportion multipliée par 100.

$$\\text{Proportion} = \\frac{\\text{effectif du sous-groupe}}{\\text{effectif total}} \\qquad \\text{Pourcentage} = \\text{Proportion} \\times 100$$

### Taux d'évolution

Le **taux d'évolution** (ou variation relative) entre une valeur initiale $V_i$ et une valeur finale $V_f$ est :

$$t = \\frac{V_f - V_i}{V_i}$$

- Si $t > 0$ : **augmentation** de $|t| \\times 100$ %.
- Si $t < 0$ : **diminution** de $|t| \\times 100$ %.

### Coefficient multiplicateur

Le **coefficient multiplicateur** est :

$$CM = 1 + t = \\frac{V_f}{V_i}$$

On passe de $V_i$ à $V_f$ en multipliant par $CM$ : $V_f = CM \\times V_i$.

#### Exemples

- Un prix passe de 80 € à 100 € : $t = \\frac{100-80}{80} = 0{,}25$ → augmentation de **25 %**, $CM = 1{,}25$.
- Un prix passe de 120 € à 96 € : $t = \\frac{96-120}{120} = -0{,}2$ → diminution de **20 %**, $CM = 0{,}8$.

### Évolutions successives

Si on applique deux évolutions de coefficients $CM_1$ et $CM_2$ successivement, le coefficient global est :

$$CM_{\\text{global}} = CM_1 \\times CM_2$$

> ⚠️ Les taux **ne s'additionnent pas** ! Une hausse de 10 % suivie d'une baisse de 10 % ne ramène **pas** à la valeur initiale.

**Exemple :** hausse de 20 % puis baisse de 10 % → $CM = 1{,}2 \\times 0{,}9 = 1{,}08$ → hausse globale de 8 %.

---

## À retenir

- La **moyenne** est la somme pondérée des valeurs divisée par l'effectif total : $\\bar{x} = \\frac{\\sum n_i x_i}{N}$.
- La **médiane** partage la série ordonnée en deux moitiés égales.
- La **variance** $V = \\frac{\\sum n_i(x_i - \\bar{x})^2}{N}$ et l'**écart-type** $\\sigma = \\sqrt{V}$ mesurent la dispersion.
- Les **quartiles** $Q_1$, $Me$, $Q_3$ et l'**écart interquartile** $Q_3 - Q_1$ résistent mieux aux valeurs extrêmes.
- Le **taux d'évolution** est $t = \\frac{V_f - V_i}{V_i}$ et le **coefficient multiplicateur** est $CM = 1 + t$.
""",
                'quiz': {
                    'titre': "Quiz — Statistiques descriptives",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Comment calcule-t-on la moyenne arithmétique d'une série statistique ?",
                            'options': ["Somme des valeurs pondérées divisée par l'effectif total", "Valeur la plus fréquente de la série", "Valeur qui partage la série ordonnée en deux", "Différence entre la plus grande et la plus petite valeur"],
                            'reponse_correcte': '0',
                            'explication': "La moyenne arithmétique est $\\bar{x} = \\frac{\\sum n_i x_i}{N}$, c'est-à-dire la somme des valeurs pondérées par leurs effectifs, divisée par l'effectif total.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Qu'est-ce que la médiane d'une série statistique ?",
                            'options': ["La valeur qui partage la série ordonnée en deux effectifs égaux", "La moyenne des valeurs extrêmes", "La valeur la plus fréquente", "La moitié de l'étendue"],
                            'reponse_correcte': '0',
                            'explication': "La médiane sépare la série ordonnée en deux parties de même effectif : 50 % des valeurs sont en-dessous et 50 % au-dessus.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "L'étendue d'une série se calcule par :",
                            'options': ["$x_{max} - x_{min}$", "$\\bar{x} - Me$", "$Q_3 - Q_1$", "$\\sigma^2$"],
                            'reponse_correcte': '0',
                            'explication': "L'étendue est la différence entre la plus grande et la plus petite valeur de la série.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "En statistiques, que désigne le mode ?",
                            'options': ["La valeur ayant le plus grand effectif", "La valeur centrale de la série", "La moyenne des quartiles", "L'écart-type de la série"],
                            'reponse_correcte': '0',
                            'explication': "Le mode est la valeur (ou modalité) qui apparaît le plus souvent dans la série statistique.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "On considère la série : 2, 5, 5, 7, 8, 10, 12. Quelle est la médiane ?",
                            'options': ["7", "5", "8", "6"],
                            'reponse_correcte': '0',
                            'explication': "La série ordonnée a 7 valeurs. La médiane est la 4ᵉ valeur : 7.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quelle formule donne la variance d'une série statistique ?",
                            'options': ["$V = \\frac{\\sum n_i (x_i - \\bar{x})^2}{N}$", "$V = \\frac{\\sum n_i x_i}{N}$", "$V = x_{max} - x_{min}$", "$V = Q_3 - Q_1$"],
                            'reponse_correcte': '0',
                            'explication': "La variance mesure la dispersion : c'est la moyenne des carrés des écarts à la moyenne.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Un article coûtait 80 € et passe à 100 €. Quel est le taux d'évolution ?",
                            'options': ["25 %", "20 %", "80 %", "125 %"],
                            'reponse_correcte': '0',
                            'explication': "Le taux d'évolution est $t = \\frac{100 - 80}{80} = \\frac{20}{80} = 0{,}25 = 25\\%$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Le coefficient multiplicateur associé à une hausse de 30 % est :",
                            'options': ["1,30", "0,30", "1,03", "0,70"],
                            'reponse_correcte': '0',
                            'explication': "Le coefficient multiplicateur est $CM = 1 + t = 1 + 0{,}30 = 1{,}30$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Quels sont les quartiles qui délimitent l'écart interquartile ?",
                            'options': ["$Q_1$ et $Q_3$", "$Q_1$ et $Q_2$", "$Q_2$ et $Q_3$", "$x_{min}$ et $x_{max}$"],
                            'reponse_correcte': '0',
                            'explication': "L'écart interquartile est $Q_3 - Q_1$. Il contient 50 % des valeurs centrales de la série.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Si la variance d'une série est 16, que vaut l'écart-type ?",
                            'options': ["4", "16", "8", "256"],
                            'reponse_correcte': '0',
                            'explication': "L'écart-type est la racine carrée de la variance : $\\sigma = \\sqrt{16} = 4$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Un prix baisse de 200 € à 150 €. Le coefficient multiplicateur est :",
                            'options': ["0,75", "0,25", "1,25", "0,50"],
                            'reponse_correcte': '0',
                            'explication': "$CM = \\frac{150}{200} = 0{,}75$. On peut vérifier : $t = 0{,}75 - 1 = -0{,}25$, soit une baisse de 25 %.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Pour une série de 20 valeurs ordonnées, le premier quartile $Q_1$ est la valeur de rang :",
                            'options': ["5", "4", "6", "10"],
                            'reponse_correcte': '0',
                            'explication': "Pour $N = 20$, le rang de $Q_1$ est le plus petit entier $\\geq \\frac{N}{4} = 5$. $Q_1$ est donc la 5ᵉ valeur.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'vrai_faux',
                            'texte': "La médiane et la moyenne d'une série statistique sont toujours égales.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La médiane et la moyenne peuvent être différentes. Elles ne coïncident que dans certains cas particuliers (distribution symétrique).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "L'écart-type est toujours positif ou nul.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "L'écart-type est la racine carrée de la variance (qui est une somme de carrés, donc positive ou nulle). Il est nul seulement si toutes les valeurs sont identiques.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Appliquer deux hausses successives de 10 % revient à une hausse totale de 20 %.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Non, on multiplie les coefficients : $1{,}10 \\times 1{,}10 = 1{,}21$, soit une hausse globale de 21 %, pas 20 %.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'texte_libre',
                            'texte': "La série de notes est : 10, 12, 14, 14, 15. Calculez la moyenne.",
                            'options': None,
                            'reponse_correcte': '13',
                            'tolerances': ['13,0', '13.0'],
                            'explication': "$\\bar{x} = \\frac{10+12+14+14+15}{5} = \\frac{65}{5} = 13$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Un objet coûtait 50 € et coûte maintenant 60 €. Donnez le taux d'évolution en pourcentage (nombre entier).",
                            'options': None,
                            'reponse_correcte': '20',
                            'tolerances': ['20%', '20 %', '+20'],
                            'explication': "$t = \\frac{60 - 50}{50} = \\frac{10}{50} = 0{,}20 = 20\\%$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "La série ordonnée de 9 valeurs est : 3, 5, 7, 8, 10, 12, 14, 16, 20. Quelle est la médiane ?",
                            'options': None,
                            'reponse_correcte': '10',
                            'tolerances': ['10,0', '10.0'],
                            'explication': "Il y a 9 valeurs ; la médiane est la 5ᵉ valeur dans l'ordre croissant, soit 10.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'qcm',
                            'texte': "Après une baisse de 20 %, quel taux de hausse faut-il appliquer pour retrouver le prix initial ?",
                            'options': ["25 %", "20 %", "80 %", "120 %"],
                            'reponse_correcte': '0',
                            'explication': "Après une baisse de 20 %, le CM est 0,80. Pour revenir au prix initial : $\\frac{1}{0{,}80} = 1{,}25$, soit une hausse de 25 %.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'qcm',
                            'texte': "La variance d'une série est 0. Que peut-on en conclure ?",
                            'options': ["Toutes les valeurs de la série sont identiques", "La série ne contient qu'une seule valeur", "La moyenne est nulle", "La médiane vaut 0"],
                            'reponse_correcte': '0',
                            'explication': "Si $V = 0$, alors chaque écart $(x_i - \\bar{x})^2 = 0$, donc toutes les valeurs sont égales à la moyenne.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Probabilités — événements et calcul',
                'duree': 40,
                'contenu': """# Probabilités — événements et calcul

## Introduction

Les **probabilités** constituent le cadre mathématique permettant de modéliser le **hasard**. On les utilise pour prédire la fréquence d'un événement lorsqu'on répète une expérience un grand nombre de fois.

> **Idée fondamentale :** si on lance un dé équilibré un très grand nombre de fois, chaque face apparaît environ $\\frac{1}{6}$ du temps. Cette proportion est la **probabilité** d'obtenir cette face.

---

## Vocabulaire des probabilités

### Expérience aléatoire

Une **expérience aléatoire** est une expérience dont on ne peut pas prévoir le résultat avec certitude, mais dont on connaît tous les résultats possibles.

**Exemples :** lancer un dé, tirer une carte, choisir un élève au hasard.

### Univers

L'**univers** $\\Omega$ est l'ensemble de tous les résultats possibles (appelés **issues** ou **éventualités**).

- Lancer d'un dé : $\\Omega = \\{1, 2, 3, 4, 5, 6\\}$
- Lancer d'une pièce : $\\Omega = \\{\\text{pile}, \\text{face}\\}$

### Événement

Un **événement** est une partie (un sous-ensemble) de l'univers $\\Omega$.

| Type | Notation | Définition |
|------|----------|------------|
| **Événement élémentaire** | $\\{\\omega\\}$ | Contient une seule issue |
| **Événement certain** | $\\Omega$ | Se réalise toujours |
| **Événement impossible** | $\\varnothing$ | Ne se réalise jamais |
| **Événement contraire** | $\\bar{A}$ | « $A$ ne se réalise pas » |

#### Exemples avec un dé

- $A$ = « obtenir un nombre pair » = $\\{2, 4, 6\\}$
- $\\bar{A}$ = « obtenir un nombre impair » = $\\{1, 3, 5\\}$
- $B$ = « obtenir un nombre supérieur à 4 » = $\\{5, 6\\}$

---

## Opérations sur les événements

### Intersection $A \\cap B$

$A \\cap B$ (lire « $A$ inter $B$ ») est l'événement « $A$ **et** $B$ se réalisent en même temps ».

**Exemple :** avec le dé, $A \\cap B = \\{6\\}$ (pair **et** supérieur à 4).

### Réunion $A \\cup B$

$A \\cup B$ (lire « $A$ union $B$ ») est l'événement « $A$ **ou** $B$ (ou les deux) se réalise ».

**Exemple :** $A \\cup B = \\{2, 4, 5, 6\\}$ (pair **ou** supérieur à 4).

### Événements incompatibles (disjoints)

Deux événements sont **incompatibles** si $A \\cap B = \\varnothing$ : ils ne peuvent pas se produire simultanément.

**Exemple :** « obtenir 1 » et « obtenir 6 » sont incompatibles.

---

## Définition de la probabilité

### Axiomes

Une **probabilité** $P$ sur l'univers $\\Omega$ est une fonction qui associe à chaque événement $A$ un nombre $P(A)$ vérifiant :

1. $0 \\leq P(A) \\leq 1$ pour tout événement $A$.
2. $P(\\Omega) = 1$ (il se passe toujours quelque chose).
3. Si $A$ et $B$ sont **incompatibles** : $P(A \\cup B) = P(A) + P(B)$.

### Conséquences immédiates

- $P(\\varnothing) = 0$ (l'événement impossible a une probabilité nulle).
- $P(\\bar{A}) = 1 - P(A)$ (probabilité de l'événement contraire).

---

## Équiprobabilité

On dit qu'il y a **équiprobabilité** lorsque toutes les issues ont la **même probabilité**. Si $\\Omega$ a $n$ issues :

$$P(\\{\\omega\\}) = \\frac{1}{n} \\qquad \\text{pour chaque issue } \\omega$$

Dans ce cas, pour tout événement $A$ :

$$\\boxed{P(A) = \\frac{\\text{nombre d'issues favorables à } A}{\\text{nombre total d'issues}} = \\frac{|A|}{|\\Omega|}}$$

#### Exemples

**Dé équilibré :** $P(\\text{obtenir 3}) = \\frac{1}{6}$.

$A$ = « obtenir un nombre pair » : $P(A) = \\frac{3}{6} = \\frac{1}{2}$.

**Tirage d'une carte dans un jeu de 52 :** $P(\\text{as de pique}) = \\frac{1}{52}$, $P(\\text{un as}) = \\frac{4}{52} = \\frac{1}{13}$.

---

## Formule de la probabilité de la réunion

Pour **deux événements quelconques** $A$ et $B$ :

$$\\boxed{P(A \\cup B) = P(A) + P(B) - P(A \\cap B)}$$

On soustrait $P(A \\cap B)$ pour ne pas compter deux fois les issues communes.

**Cas particulier :** si $A$ et $B$ sont incompatibles ($A \\cap B = \\varnothing$) :

$$P(A \\cup B) = P(A) + P(B)$$

#### Exemple

On tire une carte dans un jeu de 52. Soit $A$ = « obtenir un cœur » (13 cartes) et $B$ = « obtenir un roi » (4 cartes).

$A \\cap B$ = « obtenir le roi de cœur » → 1 carte.

$$P(A \\cup B) = \\frac{13}{52} + \\frac{4}{52} - \\frac{1}{52} = \\frac{16}{52} = \\frac{4}{13}$$

---

## Arbres de probabilités

Un **arbre de probabilités** est un outil graphique pour organiser les issues d'une expérience en plusieurs étapes.

### Règles de construction

1. Chaque **nœud** correspond à une étape ; les **branches** mènent aux issues possibles.
2. La somme des probabilités des branches issues d'un même nœud vaut **1**.
3. La probabilité d'un **chemin** est le **produit** des probabilités le long de ce chemin.
4. La probabilité d'un événement est la **somme** des probabilités des chemins qui y mènent.

### Exemple : deux lancers de pièce

Pièce équilibrée, deux lancers successifs.

- Premier lancer : pile ($\\frac{1}{2}$) ou face ($\\frac{1}{2}$).
- Deuxième lancer : idem.

$\\Omega = \\{PP, PF, FP, FF\\}$, chaque issue a la probabilité $\\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{4}$.

$P(\\text{au moins un pile}) = P(PP) + P(PF) + P(FP) = \\frac{3}{4}$.

Ou bien : $P(\\text{au moins un pile}) = 1 - P(\\text{aucun pile}) = 1 - P(FF) = 1 - \\frac{1}{4} = \\frac{3}{4}$.

---

## Modéliser une situation par les probabilités

### Étapes de résolution

1. **Identifier** l'expérience aléatoire et l'univers $\\Omega$.
2. **Définir** la loi de probabilité (équiprobabilité ou non).
3. **Traduire** l'événement cherché en sous-ensemble de $\\Omega$.
4. **Calculer** la probabilité avec les formules adéquates.

### Exemple complet

Un sac contient 5 boules rouges, 3 boules vertes et 2 boules bleues. On tire une boule au hasard.

$\\Omega$ : 10 boules, **équiprobabilité** (tirage au hasard).

- $P(\\text{rouge}) = \\frac{5}{10} = \\frac{1}{2}$
- $P(\\text{verte}) = \\frac{3}{10}$
- $P(\\text{bleue}) = \\frac{2}{10} = \\frac{1}{5}$
- $P(\\text{rouge ou verte}) = \\frac{5}{10} + \\frac{3}{10} = \\frac{8}{10} = \\frac{4}{5}$ (événements incompatibles)
- $P(\\text{pas bleue}) = 1 - \\frac{1}{5} = \\frac{4}{5}$

---

## À retenir

- L'**univers** $\\Omega$ est l'ensemble de toutes les issues ; un **événement** est un sous-ensemble de $\\Omega$.
- $P(A) \\in [0; 1]$, $P(\\Omega) = 1$, $P(\\bar{A}) = 1 - P(A)$.
- En **équiprobabilité** : $P(A) = \\frac{|A|}{|\\Omega|}$.
- Formule de la réunion : $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$.
- Un **arbre** organise les expériences à plusieurs étapes : on **multiplie** le long des branches et on **additionne** les chemins favorables.
""",
                'quiz': {
                    'titre': "Quiz — Probabilités",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Qu'est-ce que l'univers $\\Omega$ d'une expérience aléatoire ?",
                            'options': ["L'ensemble de toutes les issues possibles", "L'événement le plus probable", "L'ensemble des événements impossibles", "Le résultat de l'expérience"],
                            'reponse_correcte': '0',
                            'explication': "L'univers $\\Omega$ est l'ensemble de toutes les issues (résultats) possibles d'une expérience aléatoire.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Si $P(A) = 0{,}3$, que vaut $P(\\bar{A})$ ?",
                            'options': ["0,7", "0,3", "1,3", "0"],
                            'reponse_correcte': '0',
                            'explication': "$P(\\bar{A}) = 1 - P(A) = 1 - 0{,}3 = 0{,}7$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "On lance un dé équilibré à 6 faces. Quelle est la probabilité d'obtenir un nombre pair ?",
                            'options': ["$\\frac{1}{2}$", "$\\frac{1}{3}$", "$\\frac{1}{6}$", "$\\frac{2}{3}$"],
                            'reponse_correcte': '0',
                            'explication': "Les nombres pairs sont 2, 4, 6, soit 3 issues sur 6 : $P = \\frac{3}{6} = \\frac{1}{2}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Deux événements sont incompatibles si :",
                            'options': ["$A \\cap B = \\varnothing$", "$A \\cup B = \\varnothing$", "$P(A) + P(B) = 1$", "$P(A \\cup B) = 0$"],
                            'reponse_correcte': '0',
                            'explication': "Deux événements sont incompatibles (disjoints) lorsqu'ils ne peuvent pas se réaliser en même temps, c'est-à-dire $A \\cap B = \\varnothing$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "En situation d'équiprobabilité, $P(A)$ se calcule par :",
                            'options': ["$\\frac{\\text{nombre de cas favorables}}{\\text{nombre total de cas}}$", "$\\frac{\\text{nombre total de cas}}{\\text{nombre de cas favorables}}$", "$1 - \\frac{|A|}{|\\Omega|}$", "$|A| \\times |\\Omega|$"],
                            'reponse_correcte': '0',
                            'explication': "En équiprobabilité : $P(A) = \\frac{|A|}{|\\Omega|}$, c'est le rapport du nombre de cas favorables au nombre total d'issues.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quelle est la formule de la probabilité de la réunion de deux événements quelconques ?",
                            'options': ["$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$", "$P(A \\cup B) = P(A) + P(B)$", "$P(A \\cup B) = P(A) \\times P(B)$", "$P(A \\cup B) = P(A) - P(B)$"],
                            'reponse_correcte': '0',
                            'explication': "La formule générale est $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$. On retranche l'intersection pour ne pas la compter deux fois.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "On tire une carte dans un jeu de 52. Quelle est la probabilité d'obtenir un as ?",
                            'options': ["$\\frac{1}{13}$", "$\\frac{1}{52}$", "$\\frac{4}{13}$", "$\\frac{1}{4}$"],
                            'reponse_correcte': '0',
                            'explication': "Il y a 4 as dans un jeu de 52 cartes : $P = \\frac{4}{52} = \\frac{1}{13}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Dans un arbre de probabilités, la probabilité d'un chemin se calcule en :",
                            'options': ["Multipliant les probabilités le long des branches", "Additionnant les probabilités le long des branches", "Prenant la plus grande probabilité", "Divisant par le nombre de branches"],
                            'reponse_correcte': '0',
                            'explication': "La probabilité d'un chemin dans un arbre est le produit des probabilités des branches successives.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Un sac contient 4 boules rouges et 6 boules bleues. Quelle est $P(\\text{rouge})$ ?",
                            'options': ["$\\frac{2}{5}$", "$\\frac{4}{6}$", "$\\frac{3}{5}$", "$\\frac{1}{4}$"],
                            'reponse_correcte': '0',
                            'explication': "Il y a 10 boules au total. $P(\\text{rouge}) = \\frac{4}{10} = \\frac{2}{5}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Si $P(A) = 0{,}5$, $P(B) = 0{,}4$ et $P(A \\cap B) = 0{,}1$, que vaut $P(A \\cup B)$ ?",
                            'options': ["0,8", "0,9", "0,1", "0,5"],
                            'reponse_correcte': '0',
                            'explication': "$P(A \\cup B) = 0{,}5 + 0{,}4 - 0{,}1 = 0{,}8$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "On lance deux pièces équilibrées. Quelle est la probabilité d'obtenir exactement un pile ?",
                            'options': ["$\\frac{1}{2}$", "$\\frac{1}{4}$", "$\\frac{3}{4}$", "$\\frac{1}{3}$"],
                            'reponse_correcte': '0',
                            'explication': "$\\Omega = \\{PP, PF, FP, FF\\}$. L'événement « exactement un pile » = $\\{PF, FP\\}$ → $P = \\frac{2}{4} = \\frac{1}{2}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Que vaut $P(\\Omega)$ pour toute expérience aléatoire ?",
                            'options': ["1", "0", "0,5", "Cela dépend de l'expérience"],
                            'reponse_correcte': '0',
                            'explication': "L'événement certain $\\Omega$ se réalise toujours, donc $P(\\Omega) = 1$ par définition.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'vrai_faux',
                            'texte': "Si $A$ et $B$ sont incompatibles, alors $P(A \\cup B) = P(A) + P(B)$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Quand $A \\cap B = \\varnothing$, la formule se simplifie : $P(A \\cup B) = P(A) + P(B) - 0 = P(A) + P(B)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "La probabilité d'un événement peut être supérieure à 1.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Par définition, $0 \\leq P(A) \\leq 1$ pour tout événement $A$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "L'événement contraire de « obtenir un nombre pair » avec un dé est « obtenir un nombre impair ».",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "L'événement contraire contient toutes les issues qui ne sont pas dans $A$. Les non-pairs (parmi 1 à 6) sont les impairs.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'texte_libre',
                            'texte': "On lance un dé équilibré à 6 faces. Quelle est la probabilité d'obtenir 3 ? Donnez la réponse sous forme de fraction irréductible.",
                            'options': None,
                            'reponse_correcte': '1/6',
                            'tolerances': ['1/6'],
                            'explication': "En équiprobabilité avec 6 issues : $P(\\{3\\}) = \\frac{1}{6}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Un sac contient 3 boules rouges et 7 boules vertes. Quelle est $P(\\text{verte})$ ? Donnez une fraction irréductible.",
                            'options': None,
                            'reponse_correcte': '7/10',
                            'tolerances': ['7/10', '0.7', '0,7'],
                            'explication': "$P(\\text{verte}) = \\frac{7}{10}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "On lance deux dés équilibrés. Combien d'issues contient l'univers $\\Omega$ ?",
                            'options': None,
                            'reponse_correcte': '36',
                            'tolerances': ['36'],
                            'explication': "Chaque dé a 6 faces : $|\\Omega| = 6 \\times 6 = 36$ issues.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'qcm',
                            'texte': "On tire une carte d'un jeu de 52. Soit $A$ = « cœur » et $B$ = « roi ». Que vaut $P(A \\cup B)$ ?",
                            'options': ["$\\frac{16}{52}$", "$\\frac{17}{52}$", "$\\frac{13}{52}$", "$\\frac{4}{52}$"],
                            'reponse_correcte': '0',
                            'explication': "$P(A) = \\frac{13}{52}$, $P(B) = \\frac{4}{52}$, $P(A \\cap B) = \\frac{1}{52}$. Donc $P(A \\cup B) = \\frac{13+4-1}{52} = \\frac{16}{52}$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'qcm',
                            'texte': "On lance une pièce 3 fois. Quelle est la probabilité d'obtenir au moins un pile ?",
                            'options': ["$\\frac{7}{8}$", "$\\frac{3}{8}$", "$\\frac{1}{2}$", "$\\frac{1}{8}$"],
                            'reponse_correcte': '0',
                            'explication': "$P(\\text{au moins un pile}) = 1 - P(\\text{aucun pile}) = 1 - P(FFF) = 1 - \\frac{1}{8} = \\frac{7}{8}$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 8 — Géométrie dans le plan
    # ──────────────────────────────────────────────
    {
        'ordre': 8,
        'titre': 'Géométrie dans le plan',
        'description': "Théorèmes fondamentaux sur les triangles et quadrilatères : milieux, médiatrices, parallélogrammes et configurations remarquables.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Théorèmes sur les triangles (milieux, médiatrices)',
                'duree': 40,
                'contenu': """# Théorèmes sur les triangles (milieux, médiatrices)

## Introduction

La géométrie euclidienne étudie les figures du plan à l'aide de propriétés métriques (distances, angles). En classe de Seconde, on approfondit les résultats fondamentaux sur les **triangles** : théorème des milieux, droites remarquables et leurs points de concours.

---

## Théorème des milieux

### Énoncé (théorème direct)

Dans un triangle $ABC$, si $M$ est le milieu de $[AB]$ et $N$ le milieu de $[AC]$, alors :

1. $(MN) \\parallel (BC)$
2. $MN = \\dfrac{BC}{2}$

> Le segment joignant les milieux de deux côtés d'un triangle est **parallèle** au troisième côté et mesure la **moitié** de sa longueur.

### Exemple

Dans le triangle $ABC$, on donne $BC = 8$ cm. Si $M$ est le milieu de $[AB]$ et $N$ le milieu de $[AC]$, alors :

$$MN = \\frac{BC}{2} = \\frac{8}{2} = 4 \\text{ cm} \\qquad \\text{et} \\qquad (MN) \\parallel (BC)$$

### Réciproque

Dans un triangle $ABC$, si $M$ est le milieu de $[AB]$ et si la droite passant par $M$ parallèle à $(BC)$ coupe $[AC]$ en $N$, alors $N$ est le milieu de $[AC]$.

> Cette réciproque est très utile pour **démontrer qu'un point est un milieu**.

---

## Droites remarquables d'un triangle

Un triangle $ABC$ possède quatre familles de droites remarquables. Chacune fournit un **point de concours** (les trois droites de même nature se coupent en un seul point).

### Médianes et centre de gravité

La **médiane** issue d'un sommet est le segment reliant ce sommet au **milieu du côté opposé**.

Les trois médianes d'un triangle sont **concourantes** en un point $G$ appelé **centre de gravité**.

**Propriété fondamentale :** le centre de gravité $G$ divise chaque médiane dans le rapport $\\frac{2}{3}$ depuis le sommet :

$$AG = \\frac{2}{3} \\, AA' \\qquad \\text{où } A' \\text{ est le milieu de } [BC]$$

> En physique, $G$ est le point d'équilibre du triangle (si on le découpe dans un matériau homogène).

#### Coordonnées du centre de gravité

Si $A(x_A; y_A)$, $B(x_B; y_B)$, $C(x_C; y_C)$, alors :

$$G\\left(\\frac{x_A + x_B + x_C}{3} \\; ; \\; \\frac{y_A + y_B + y_C}{3}\\right)$$

### Médiatrices et cercle circonscrit

La **médiatrice** d'un segment $[AB]$ est la droite **perpendiculaire** à $[AB]$ passant par son **milieu**.

**Propriété caractéristique :** un point $M$ appartient à la médiatrice de $[AB]$ si et seulement si $MA = MB$.

Les trois médiatrices d'un triangle sont **concourantes** en un point $O$ appelé **centre du cercle circonscrit**. Ce cercle passe par les trois sommets du triangle.

$$OA = OB = OC = R \\qquad (\\text{rayon du cercle circonscrit})$$

### Hauteurs et orthocentre

La **hauteur** issue d'un sommet est la droite passant par ce sommet et **perpendiculaire** au côté opposé.

Les trois hauteurs sont **concourantes** en un point $H$ appelé **orthocentre**.

- Triangle **acutangle** (tous les angles aigus) : $H$ est à l'**intérieur** du triangle.
- Triangle **rectangle** en $A$ : $H = A$ (le sommet de l'angle droit).
- Triangle **obtusangle** : $H$ est à l'**extérieur** du triangle.

### Bissectrices et cercle inscrit

La **bissectrice** d'un angle est la demi-droite qui partage cet angle en **deux angles égaux**.

Les trois bissectrices intérieures sont **concourantes** en un point $I$ appelé **centre du cercle inscrit**. Ce cercle est tangent aux trois côtés du triangle.

---

## Droite d'Euler

Dans tout triangle non équilatéral, le centre de gravité $G$, l'orthocentre $H$ et le centre du cercle circonscrit $O$ sont **alignés** sur une droite appelée **droite d'Euler**.

De plus : $\\vec{OH} = 3\\,\\vec{OG}$, c'est-à-dire que $G$ divise $[OH]$ dans le rapport $\\frac{1}{3}$ depuis $O$.

---

## Théorème de Pythagore et sa réciproque

### Théorème direct

Dans un triangle $ABC$ **rectangle en $C$** :

$$AB^2 = AC^2 + BC^2$$

L'hypoténuse est le côté **opposé** à l'angle droit et c'est le **plus grand** côté.

#### Exemple

Si $AC = 3$ et $BC = 4$ : $AB^2 = 9 + 16 = 25$, donc $AB = 5$.

### Réciproque

Si dans un triangle $ABC$ on a $AB^2 = AC^2 + BC^2$, alors le triangle est **rectangle en $C$**.

### Contraposée

Si $AB^2 \\neq AC^2 + BC^2$, alors le triangle $ABC$ n'est **pas** rectangle en $C$.

---

## Résumé des points de concours

| Droites | Point de concours | Propriété |
|---------|-------------------|-----------|
| Médianes | Centre de gravité $G$ | Divise chaque médiane en $\\frac{2}{3}$ – $\\frac{1}{3}$ |
| Médiatrices | Centre du cercle circonscrit $O$ | $OA = OB = OC$ |
| Hauteurs | Orthocentre $H$ | — |
| Bissectrices | Centre du cercle inscrit $I$ | Équidistant des trois côtés |

---

## À retenir

- **Théorème des milieux** : le segment des milieux est parallèle au 3ᵉ côté et vaut sa moitié.
- Un triangle possède **4 familles** de droites remarquables, chacune avec un point de concours.
- Le **centre de gravité** $G$ a pour coordonnées la moyenne des coordonnées des sommets.
- Le **cercle circonscrit** passe par les 3 sommets ; le **cercle inscrit** est tangent aux 3 côtés.
- **Pythagore** : $AB^2 = AC^2 + BC^2$ ⟺ triangle rectangle en $C$.
""",
                'quiz': {
                    'titre': "Quiz — Théorèmes sur les triangles",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Dans un triangle $ABC$, $M$ milieu de $[AB]$ et $N$ milieu de $[AC]$. Que peut-on affirmer ?",
                            'options': ["$(MN) \\parallel (BC)$ et $MN = \\frac{BC}{2}$", "$(MN) \\perp (BC)$", "$MN = BC$", "$(MN) \\parallel (AB)$"],
                            'reponse_correcte': '0',
                            'explication': "C'est le théorème des milieux : le segment joignant les milieux de deux côtés est parallèle au troisième et vaut la moitié de sa longueur.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Les trois médianes d'un triangle sont concourantes en un point appelé :",
                            'options': ["Centre de gravité", "Orthocentre", "Centre du cercle circonscrit", "Centre du cercle inscrit"],
                            'reponse_correcte': '0',
                            'explication': "Les trois médianes se coupent au centre de gravité $G$, qui divise chaque médiane dans le rapport $\\frac{2}{3}$ depuis le sommet.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Les trois médiatrices d'un triangle sont concourantes au :",
                            'options': ["Centre du cercle circonscrit", "Centre de gravité", "Orthocentre", "Centre du cercle inscrit"],
                            'reponse_correcte': '0',
                            'explication': "Les médiatrices se coupent au centre du cercle circonscrit, qui passe par les trois sommets du triangle.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Qu'est-ce qu'une médiane d'un triangle ?",
                            'options': ["Le segment reliant un sommet au milieu du côté opposé", "Le segment reliant un sommet au pied de la hauteur", "La perpendiculaire à un côté passant par son milieu", "La bissectrice d'un angle du triangle"],
                            'reponse_correcte': '0',
                            'explication': "Une médiane joint un sommet au milieu du côté opposé.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Dans un triangle $ABC$, si $BC = 12$ cm, $M$ milieu de $[AB]$, $N$ milieu de $[AC]$, que vaut $MN$ ?",
                            'options': ["6 cm", "12 cm", "24 cm", "3 cm"],
                            'reponse_correcte': '0',
                            'explication': "Par le théorème des milieux : $MN = \\frac{BC}{2} = \\frac{12}{2} = 6$ cm.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Les trois hauteurs d'un triangle sont concourantes en un point appelé :",
                            'options': ["Orthocentre", "Centre de gravité", "Centre du cercle inscrit", "Centre du cercle circonscrit"],
                            'reponse_correcte': '0',
                            'explication': "L'orthocentre $H$ est le point d'intersection des trois hauteurs du triangle.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Les trois bissectrices d'un triangle sont concourantes au centre du :",
                            'options': ["Cercle inscrit", "Cercle circonscrit", "Parallélogramme", "Triangle"],
                            'reponse_correcte': '0',
                            'explication': "Le point de concours des trois bissectrices est le centre du cercle inscrit, tangent aux trois côtés.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Le centre de gravité divise chaque médiane dans le rapport :",
                            'options': ["$\\frac{2}{3}$ depuis le sommet", "$\\frac{1}{2}$ depuis le sommet", "$\\frac{1}{3}$ depuis le sommet", "$\\frac{3}{4}$ depuis le sommet"],
                            'reponse_correcte': '0',
                            'explication': "Le centre de gravité $G$ est situé aux $\\frac{2}{3}$ de chaque médiane à partir du sommet (et $\\frac{1}{3}$ depuis le milieu du côté opposé).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Dans un triangle rectangle en $C$, le théorème de Pythagore s'écrit :",
                            'options': ["$AB^2 = AC^2 + BC^2$", "$AC^2 = AB^2 + BC^2$", "$BC^2 = AB^2 + AC^2$", "$AB = AC + BC$"],
                            'reponse_correcte': '0',
                            'explication': "Si le triangle est rectangle en $C$, l'hypoténuse est $[AB]$ et on a $AB^2 = AC^2 + BC^2$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Quel est le rôle de la réciproque du théorème des milieux ?",
                            'options': ["Démontrer qu'un point est un milieu", "Calculer la longueur d'un côté", "Prouver qu'un angle est droit", "Trouver le centre de gravité"],
                            'reponse_correcte': '0',
                            'explication': "La réciproque permet de démontrer qu'un point est le milieu d'un segment, à condition de savoir qu'une droite passant par le milieu d'un côté est parallèle à un autre côté.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Le cercle circonscrit à un triangle rectangle a pour diamètre :",
                            'options': ["L'hypoténuse", "Le plus petit côté", "La médiane", "La hauteur"],
                            'reponse_correcte': '0',
                            'explication': "Dans un triangle rectangle, l'hypoténuse est un diamètre du cercle circonscrit (le centre est le milieu de l'hypoténuse).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Les coordonnées du centre de gravité $G$ d'un triangle $ABC$ sont :",
                            'options': ["$G\\left(\\frac{x_A+x_B+x_C}{3}; \\frac{y_A+y_B+y_C}{3}\\right)$", "$G\\left(\\frac{x_A+x_B}{2}; \\frac{y_A+y_B}{2}\\right)$", "$G(x_A+x_B+x_C; y_A+y_B+y_C)$", "$G\\left(\\frac{x_A \\cdot x_B \\cdot x_C}{3}; \\frac{y_A \\cdot y_B \\cdot y_C}{3}\\right)$"],
                            'reponse_correcte': '0',
                            'explication': "Le centre de gravité a pour coordonnées la moyenne arithmétique des coordonnées des trois sommets.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'vrai_faux',
                            'texte': "La médiatrice d'un segment est la droite perpendiculaire à ce segment passant par son milieu.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est exactement la définition de la médiatrice : droite perpendiculaire au segment en son milieu.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Dans tout triangle, l'orthocentre est toujours à l'intérieur du triangle.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "L'orthocentre peut être à l'extérieur du triangle (triangle obtusangle) ou sur un sommet (triangle rectangle).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Si un triangle a ses côtés de longueurs 3, 4 et 5, alors il est rectangle.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$3^2 + 4^2 = 9 + 16 = 25 = 5^2$. Par la réciproque du théorème de Pythagore, le triangle est rectangle.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'texte_libre',
                            'texte': "Dans un triangle $ABC$ rectangle en $C$ avec $AC = 3$ cm et $BC = 4$ cm, calculez $AB$ (en cm).",
                            'options': None,
                            'reponse_correcte': '5',
                            'tolerances': ['5 cm', '5,0', '5.0'],
                            'explication': "$AB^2 = AC^2 + BC^2 = 9 + 16 = 25$, donc $AB = \\sqrt{25} = 5$ cm.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Dans un triangle $ABC$ avec $A(1;2)$, $B(5;6)$, $C(3;0)$, quelles sont les coordonnées du centre de gravité $G$ ? Donnez l'abscisse.",
                            'options': None,
                            'reponse_correcte': '3',
                            'tolerances': ['3,0', '3.0'],
                            'explication': "$x_G = \\frac{1+5+3}{3} = \\frac{9}{3} = 3$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Combien de familles de droites remarquables un triangle possède-t-il ? (nombre entier)",
                            'options': None,
                            'reponse_correcte': '4',
                            'tolerances': ['quatre', '4'],
                            'explication': "Les 4 familles sont : médianes, hauteurs, médiatrices et bissectrices.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 19,
                            'type': 'qcm',
                            'texte': "Dans un triangle $ABC$ avec $A(0;0)$, $B(6;0)$, $C(0;8)$, le milieu $M$ de $[BC]$ a pour coordonnées :",
                            'options': ["$(3; 4)$", "$(6; 8)$", "$(0; 4)$", "$(3; 0)$"],
                            'reponse_correcte': '0',
                            'explication': "$M\\left(\\frac{6+0}{2}; \\frac{0+8}{2}\\right) = (3; 4)$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'qcm',
                            'texte': "Un triangle $ABC$ a $M$ milieu de $[AB]$. La droite passant par $M$ et parallèle à $(BC)$ coupe $[AC]$ en $N$. Alors :",
                            'options': ["$N$ est le milieu de $[AC]$", "$N$ est le milieu de $[BC]$", "$MN = BC$", "$(MN) \\perp (BC)$"],
                            'reponse_correcte': '0',
                            'explication': "C'est la réciproque du théorème des milieux : si une droite passe par le milieu d'un côté et est parallèle à un autre, elle coupe le troisième en son milieu.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Quadrilatères et configurations remarquables',
                'duree': 35,
                'contenu': """# Quadrilatères et configurations remarquables

## Introduction

Un **quadrilatère** est un polygone à quatre côtés. Parmi les quadrilatères, certains possèdent des propriétés remarquables qui les rendent particulièrement utiles en géométrie. Ce cours étudie la hiérarchie des quadrilatères particuliers et leurs propriétés caractéristiques.

---

## Le parallélogramme

### Définition

Un **parallélogramme** est un quadrilatère dont les **côtés opposés sont parallèles** deux à deux.

$ABCD$ est un parallélogramme ⟺ $(AB) \\parallel (DC)$ et $(AD) \\parallel (BC)$.

### Propriétés

Un parallélogramme $ABCD$ vérifie :

1. Les **côtés opposés** sont de **même longueur** : $AB = DC$ et $AD = BC$.
2. Les **angles opposés** sont **égaux** : $\\widehat{A} = \\widehat{C}$ et $\\widehat{B} = \\widehat{D}$.
3. Les **angles consécutifs** sont **supplémentaires** : $\\widehat{A} + \\widehat{B} = 180°$.
4. Les **diagonales** se coupent en leur **milieu** : si $O = [AC] \\cap [BD]$, alors $OA = OC$ et $OB = OD$.

### Caractérisations (pour démontrer qu'un quadrilatère est un parallélogramme)

Un quadrilatère $ABCD$ est un parallélogramme si et seulement si **l'une** des conditions suivantes est vérifiée :

- Les côtés opposés sont parallèles deux à deux.
- Les côtés opposés sont de même longueur deux à deux.
- Deux côtés opposés sont **parallèles et de même longueur**.
- Les diagonales se coupent en leur milieu.
- Les angles opposés sont égaux.

---

## Le rectangle

### Définition

Un **rectangle** est un parallélogramme ayant un **angle droit**.

> Comme les angles consécutifs d'un parallélogramme sont supplémentaires, si l'un vaut 90°, **les quatre** valent 90°.

### Propriétés

En plus des propriétés du parallélogramme, le rectangle vérifie :

- Les **quatre angles** sont droits (90°).
- Les **diagonales** sont de **même longueur** : $AC = BD$.

### Caractérisations

Un parallélogramme est un rectangle si et seulement si :
- Il a un angle droit, **ou**
- Ses diagonales sont de même longueur.

Un quadrilatère ayant ses quatre angles droits est un rectangle.

---

## Le losange

### Définition

Un **losange** est un parallélogramme ayant **deux côtés consécutifs égaux**.

> Comme les côtés opposés d'un parallélogramme sont égaux, les **quatre côtés** d'un losange sont de même longueur.

### Propriétés

En plus des propriétés du parallélogramme, le losange vérifie :

- Les **quatre côtés** sont de **même longueur**.
- Les **diagonales** sont **perpendiculaires** : $(AC) \\perp (BD)$.
- Chaque **diagonale** est **bissectrice** des angles qu'elle joint.

### Caractérisations

Un parallélogramme est un losange si et seulement si :
- II a deux côtés consécutifs égaux, **ou**
- Ses diagonales sont perpendiculaires.

---

## Le carré

### Définition

Un **carré** est un quadrilatère qui est **à la fois** un rectangle et un losange.

### Propriétés

Le carré cumule toutes les propriétés :

- Quatre **côtés égaux** et quatre **angles droits**.
- Diagonales de **même longueur**, **perpendiculaires**, se coupant en leur **milieu**.
- Chaque diagonale est **bissectrice** des angles qu'elle joint.

### Caractérisations

Un parallélogramme est un carré si :
- C'est un rectangle avec deux côtés consécutifs égaux, **ou**
- C'est un losange avec un angle droit, **ou**
- Ses diagonales sont égales et perpendiculaires.

---

## Hiérarchie des quadrilatères

$$\\text{Carré} \\subset \\text{Rectangle} \\subset \\text{Parallélogramme} \\subset \\text{Quadrilatère}$$
$$\\text{Carré} \\subset \\text{Losange} \\subset \\text{Parallélogramme}$$

> Tout carré est un rectangle (et un losange), tout rectangle est un parallélogramme, mais les réciproques sont fausses en général.

---

## Le trapèze

### Définition

Un **trapèze** est un quadrilatère ayant (au moins) **deux côtés parallèles**, appelés les **bases**. Les deux autres côtés sont les **côtés non parallèles** (ou « jambes »).

### Cas particuliers

- **Trapèze isocèle** : les côtés non parallèles sont de **même longueur**. Ses diagonales sont aussi de même longueur.
- **Trapèze rectangle** : un des côtés non parallèles est **perpendiculaire** aux bases.

---

## Configurations remarquables dans les problèmes

### Milieux et parallélisme

**Théorème de la droite des milieux (cas du trapèze) :** dans un trapèze $ABCD$ de bases $[AB]$ et $[DC]$, le segment joignant les milieux des côtés non parallèles est **parallèle** aux bases et sa longueur vaut la **demi-somme** des bases :

$$EF = \\frac{AB + DC}{2}$$

### Vecteurs et parallélogramme

On peut démontrer qu'un quadrilatère $ABCD$ est un parallélogramme en utilisant les vecteurs :

$$ABCD \\text{ est un parallélogramme} \\Longleftrightarrow \\vec{AB} = \\vec{DC}$$

Ce critère vectoriel est souvent le plus rapide en géométrie analytique.

### Symétrie centrale

Un parallélogramme admet un **centre de symétrie** : le point d'intersection de ses diagonales. Un rectangle et un losange aussi. Le carré admet en plus **quatre axes de symétrie**.

| Figure | Centre de symétrie | Axes de symétrie |
|--------|--------------------|------------------|
| Parallélogramme | Oui (intersection diag.) | 0 (en général) |
| Rectangle | Oui | 2 (médiatrices des côtés) |
| Losange | Oui | 2 (les diagonales) |
| Carré | Oui | 4 (diagonales + médiatrices) |

---

## À retenir

- Un **parallélogramme** a ses côtés opposés parallèles et égaux ; ses diagonales se coupent en leur milieu.
- Un **rectangle** = parallélogramme + angle droit → diagonales de même longueur.
- Un **losange** = parallélogramme + côtés tous égaux → diagonales perpendiculaires.
- Un **carré** = rectangle + losange → diagonales égales, perpendiculaires, se coupant en leur milieu.
- Pour prouver qu'un quadrilatère est un parallélogramme, on peut utiliser le critère vectoriel $\\vec{AB} = \\vec{DC}$.
""",
                'quiz': {
                    'titre': "Quiz — Quadrilatères et configurations",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quelle propriété caractérise les diagonales d'un parallélogramme ?",
                            'options': ["Elles se coupent en leur milieu", "Elles sont perpendiculaires", "Elles sont de même longueur", "Elles ne se coupent pas"],
                            'reponse_correcte': '0',
                            'explication': "Dans un parallélogramme, les diagonales se coupent en leur milieu. C'est même une caractérisation.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Un rectangle est un parallélogramme qui possède en plus :",
                            'options': ["Un angle droit", "Quatre côtés égaux", "Des diagonales perpendiculaires", "Un centre de symétrie d'ordre 4"],
                            'reponse_correcte': '0',
                            'explication': "Un rectangle est un parallélogramme ayant (au moins) un angle droit. Les quatre angles sont alors droits.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Les diagonales d'un losange sont :",
                            'options': ["Perpendiculaires", "De même longueur", "Parallèles", "De longueur nulle"],
                            'reponse_correcte': '0',
                            'explication': "Les diagonales d'un losange sont perpendiculaires et se coupent en leur milieu.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Combien d'axes de symétrie possède un carré ?",
                            'options': ["4", "2", "1", "0"],
                            'reponse_correcte': '0',
                            'explication': "Le carré a 4 axes de symétrie : les 2 diagonales et les 2 médiatrices des côtés.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Un carré est à la fois :",
                            'options': ["Un rectangle et un losange", "Un rectangle et un trapèze", "Un losange et un cerf-volant", "Un trapèze et un losange"],
                            'reponse_correcte': '0',
                            'explication': "Le carré combine les propriétés du rectangle (angles droits, diagonales égales) et du losange (côtés égaux, diagonales perpendiculaires).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quelle condition vectorielle caractérise un parallélogramme $ABCD$ ?",
                            'options': ["$\\vec{AB} = \\vec{DC}$", "$\\vec{AB} = \\vec{CD}$", "$\\vec{AB} + \\vec{CD} = \\vec{0}$", "$\\vec{AC} = \\vec{BD}$"],
                            'reponse_correcte': '0',
                            'explication': "$ABCD$ est un parallélogramme si et seulement si $\\vec{AB} = \\vec{DC}$ (les côtés opposés sont des translations l'un de l'autre).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Parmi ces propositions, laquelle n'est PAS une caractérisation du parallélogramme ?",
                            'options': ["Les diagonales sont perpendiculaires", "Les côtés opposés sont parallèles deux à deux", "Les diagonales se coupent en leur milieu", "Deux côtés opposés sont parallèles et de même longueur"],
                            'reponse_correcte': '0',
                            'explication': "Avoir les diagonales perpendiculaires est une propriété du losange, pas de tout parallélogramme.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Les diagonales d'un rectangle sont :",
                            'options': ["De même longueur", "Perpendiculaires", "De longueurs différentes", "Parallèles"],
                            'reponse_correcte': '0',
                            'explication': "Dans un rectangle, les diagonales sont de même longueur et se coupent en leur milieu.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Les angles consécutifs d'un parallélogramme sont :",
                            'options': ["Supplémentaires (somme = 180°)", "Complémentaires (somme = 90°)", "Égaux", "Opposés"],
                            'reponse_correcte': '0',
                            'explication': "Dans un parallélogramme, deux angles consécutifs sont supplémentaires : leur somme vaut 180°.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Un parallélogramme qui a ses quatre côtés égaux est un :",
                            'options': ["Losange", "Rectangle", "Trapèze", "Cerf-volant"],
                            'reponse_correcte': '0',
                            'explication': "Un losange est un parallélogramme dont les quatre côtés sont de même longueur.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Le trapèze est un quadrilatère qui possède :",
                            'options': ["Exactement deux côtés parallèles", "Quatre côtés parallèles deux à deux", "Quatre angles droits", "Quatre côtés de même longueur"],
                            'reponse_correcte': '0',
                            'explication': "Un trapèze possède exactement une paire de côtés parallèles (les bases).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Le milieu du segment joignant les milieux des diagonales d'un trapèze est aussi le milieu de :",
                            'options': ["La droite des milieux des côtés non parallèles", "L'une des bases", "Les deux bases", "Aucune de ces propositions"],
                            'reponse_correcte': '0',
                            'explication': "Dans un trapèze, le segment joignant les milieux des côtés non parallèles (segment médian) est parallèle aux bases et a pour longueur la demi-somme des bases.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'vrai_faux',
                            'texte': "Tout rectangle est un parallélogramme.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Un rectangle est un cas particulier de parallélogramme (avec un angle droit en plus).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Un losange a toujours ses diagonales de même longueur.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Les diagonales d'un losange sont perpendiculaires mais pas nécessairement de même longueur. Elles ne sont égales que si le losange est aussi un carré.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Un parallélogramme possède un centre de symétrie.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Le point d'intersection des diagonales est le centre de symétrie du parallélogramme.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'texte_libre',
                            'texte': "Combien d'axes de symétrie possède un rectangle (non carré) ?",
                            'options': None,
                            'reponse_correcte': '2',
                            'tolerances': ['deux', '2'],
                            'explication': "Un rectangle (non carré) possède 2 axes de symétrie : les médiatrices de chaque paire de côtés opposés.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Un parallélogramme $ABCD$ a pour côtés $AB = 5$ cm et $BC = 8$ cm. Quel est son périmètre en cm ?",
                            'options': None,
                            'reponse_correcte': '26',
                            'tolerances': ['26 cm', '26,0', '26.0'],
                            'explication': "Dans un parallélogramme, les côtés opposés sont égaux : périmètre = $2(5 + 8) = 26$ cm.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Dans un trapèze de bases $a = 6$ cm et $b = 10$ cm, quelle est la longueur du segment médian (en cm) ?",
                            'options': None,
                            'reponse_correcte': '8',
                            'tolerances': ['8 cm', '8,0', '8.0'],
                            'explication': "Le segment médian d'un trapèze a pour longueur la demi-somme des bases : $\\frac{6+10}{2} = 8$ cm.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'qcm',
                            'texte': "Un losange a des diagonales de longueur 6 cm et 8 cm. Quelle est la longueur de chaque côté ?",
                            'options': ["5 cm", "7 cm", "10 cm", "4 cm"],
                            'reponse_correcte': '0',
                            'explication': "Les demi-diagonales mesurent 3 et 4. Par Pythagore : côté $= \\sqrt{3^2 + 4^2} = \\sqrt{25} = 5$ cm.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'qcm',
                            'texte': "Pour prouver que $ABCD$ est un rectangle, on peut montrer que c'est un parallélogramme ayant :",
                            'options': ["Des diagonales de même longueur", "Des diagonales perpendiculaires", "Quatre côtés de même longueur", "Un seul angle obtus"],
                            'reponse_correcte': '0',
                            'explication': "Un parallélogramme dont les diagonales sont de même longueur est un rectangle.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 9 — Vecteurs
    # ──────────────────────────────────────────────
    {
        'ordre': 9,
        'titre': 'Vecteurs',
        'description': "Notion de vecteur, opérations, coordonnées dans un repère, colinéarité et applications à la géométrie analytique.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Vecteurs — définition, égalité, opérations',
                'duree': 40,
                'contenu': """# Vecteurs — définition, égalité, opérations

## Introduction

En géométrie, un **vecteur** est un objet mathématique qui modélise un **déplacement** (ou une translation). Contrairement à un simple nombre (qui mesure une grandeur), un vecteur possède trois caractéristiques : une **direction**, un **sens** et une **norme** (longueur).

Les vecteurs sont un outil fondamental pour la géométrie analytique et la physique.

---

## Définition d'un vecteur

### Translation

Une **translation** de vecteur $\\vec{u}$ est une transformation qui déplace chaque point $M$ du plan en un point $M'$ tel que $MM'$ a une direction, un sens et une longueur fixés.

### Vecteur associé à un bipoint

Étant donnés deux points $A$ et $B$, le **vecteur** $\\vec{AB}$ est caractérisé par :

- **Direction** : celle de la droite $(AB)$.
- **Sens** : de $A$ vers $B$.
- **Norme** : la distance $AB$, notée $\\|\\vec{AB}\\|$ ou $|\\vec{AB}|$.

On représente un vecteur par une **flèche** allant de son origine à son extrémité.

### Vecteur nul

Le **vecteur nul** $\\vec{0}$ est le vecteur $\\vec{AA}$ (pour tout point $A$). Il a une norme nulle et n'a pas de direction définie.

$$\\|\\vec{0}\\| = 0 \\qquad \\text{et} \\qquad \\vec{AA} = \\vec{BB} = \\vec{0}$$

---

## Égalité de deux vecteurs

### Définition

Deux vecteurs $\\vec{AB}$ et $\\vec{CD}$ sont **égaux** s'ils ont la **même direction**, le **même sens** et la **même norme** :

$$\\vec{AB} = \\vec{CD} \\Longleftrightarrow ABDC \\text{ est un parallélogramme (éventuellement aplati)}$$

> ⚠️ L'ordre des lettres est important : $ABDC$ (et non $ABCD$) !

### Représentant d'un vecteur

Un vecteur n'est **pas attaché à un point** : on peut le représenter n'importe où dans le plan. On dit que $\\vec{AB}$, $\\vec{CD}$, etc. sont des **représentants** du même vecteur $\\vec{u}$ s'ils sont égaux.

Pour tout point $M$ du plan et tout vecteur $\\vec{u}$, il existe un **unique** point $M'$ tel que $\\vec{MM'} = \\vec{u}$.

---

## Vecteur opposé

Le **vecteur opposé** de $\\vec{AB}$ est le vecteur $\\vec{BA}$ :

$$\\vec{BA} = -\\vec{AB}$$

Il a la **même direction** et la **même norme** que $\\vec{AB}$, mais un **sens contraire**.

---

## Addition de deux vecteurs

### Relation de Chasles

Pour tous points $A$, $B$, $C$ :

$$\\boxed{\\vec{AB} + \\vec{BC} = \\vec{AC}}$$

C'est la **relation de Chasles** : on « enchaîne » les déplacements.

**Cas particulier :** $\\vec{AB} + \\vec{BA} = \\vec{AA} = \\vec{0}$.

### Règle du parallélogramme

Pour additionner deux vecteurs $\\vec{u}$ et $\\vec{v}$ ayant la **même origine** $A$ :

1. On trace $\\vec{AB} = \\vec{u}$ et $\\vec{AC} = \\vec{v}$.
2. On complète le parallélogramme $ABDC$.
3. Le vecteur somme est $\\vec{AD} = \\vec{u} + \\vec{v}$.

### Propriétés de l'addition

L'addition des vecteurs est :

- **Commutative** : $\\vec{u} + \\vec{v} = \\vec{v} + \\vec{u}$
- **Associative** : $(\\vec{u} + \\vec{v}) + \\vec{w} = \\vec{u} + (\\vec{v} + \\vec{w})$
- **Élément neutre** : $\\vec{u} + \\vec{0} = \\vec{u}$
- **Opposé** : $\\vec{u} + (-\\vec{u}) = \\vec{0}$

### Soustraction

$$\\vec{u} - \\vec{v} = \\vec{u} + (-\\vec{v})$$

---

## Multiplication par un scalaire

### Définition

Soit $\\vec{u}$ un vecteur **non nul** et $k$ un nombre réel (un **scalaire**). Le vecteur $k\\vec{u}$ a :

- La **même direction** que $\\vec{u}$.
- La **même sens** si $k > 0$, le **sens contraire** si $k < 0$.
- Une **norme** égale à $|k| \\times \\|\\vec{u}\\|$.

**Cas particuliers :**

| Scalaire | Résultat |
|----------|----------|
| $k = 1$ | $1 \\cdot \\vec{u} = \\vec{u}$ |
| $k = 0$ | $0 \\cdot \\vec{u} = \\vec{0}$ |
| $k = -1$ | $(-1) \\cdot \\vec{u} = -\\vec{u}$ |
| $k = 2$ | $2\\vec{u}$ : même direction, même sens, norme doublée |
| $k = -\\frac{1}{2}$ | Sens contraire, norme divisée par 2 |

### Propriétés

Pour tous vecteurs $\\vec{u}$, $\\vec{v}$ et tous réels $k$, $k'$ :

- $k(\\vec{u} + \\vec{v}) = k\\vec{u} + k\\vec{v}$ (distributivité sur les vecteurs)
- $(k + k')\\vec{u} = k\\vec{u} + k'\\vec{u}$ (distributivité sur les scalaires)
- $(kk')\\vec{u} = k(k'\\vec{u})$ (associativité)

---

## Milieu d'un segment

Le **milieu** $I$ de $[AB]$ vérifie :

$$\\vec{AI} = \\frac{1}{2}\\vec{AB} \\qquad \\text{ou de façon équivalente} \\qquad \\vec{IA} + \\vec{IB} = \\vec{0}$$

---

## Colinéarité

### Définition

Deux vecteurs $\\vec{u}$ et $\\vec{v}$ sont **colinéaires** s'il existe un réel $k$ tel que $\\vec{v} = k\\vec{u}$ (ou $\\vec{u} = \\vec{0}$).

> Géométriquement, deux vecteurs colinéaires ont la **même direction** (ou l'un d'eux est nul).

### Applications de la colinéarité

- **Trois points alignés** : $A$, $B$, $C$ sont alignés ⟺ $\\vec{AB}$ et $\\vec{AC}$ sont colinéaires.
- **Droites parallèles** : $(AB) \\parallel (CD)$ ⟺ $\\vec{AB}$ et $\\vec{CD}$ sont colinéaires.

---

## Exemples d'application

### Exemple 1 : démontrer un parallélisme

Soit $A(1;3)$, $B(4;7)$, $C(2;1)$, $D(5;5)$.

$\\vec{AB} = (3;4)$ et $\\vec{CD} = (3;4)$.

$\\vec{AB} = \\vec{CD}$ donc $ABDC$ est un parallélogramme, et en particulier $(AB) \\parallel (CD)$.

### Exemple 2 : trouver le milieu

Soit $A(2;6)$ et $B(8;-2)$. Le milieu $I$ vérifie $\\vec{AI} = \\frac{1}{2}\\vec{AB}$.

$\\vec{AB} = (6;-8)$ donc $\\vec{AI} = (3;-4)$, d'où $I(2+3; 6-4) = I(5;2)$.

---

## À retenir

- Un **vecteur** $\\vec{AB}$ a une direction, un sens et une norme.
- $\\vec{AB} = \\vec{CD}$ ⟺ $ABDC$ est un parallélogramme.
- **Relation de Chasles** : $\\vec{AB} + \\vec{BC} = \\vec{AC}$.
- $k\\vec{u}$ a la même direction que $\\vec{u}$, avec une norme $|k| \\|\\vec{u}\\|$.
- Deux vecteurs sont **colinéaires** s'ils ont même direction : on l'utilise pour prouver l'alignement ou le parallélisme.
""",
                'quiz': {
                    'titre': "Quiz — Vecteurs : définition et opérations",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Un vecteur $\\vec{AB}$ est caractérisé par :",
                            'options': ["Sa direction, son sens et sa norme", "Uniquement sa norme", "Uniquement sa direction", "Sa position dans le plan"],
                            'reponse_correcte': '0',
                            'explication': "Un vecteur est défini par trois éléments : une direction (droite support), un sens (de $A$ vers $B$) et une norme (longueur $AB$).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Que signifie $\\vec{AB} = \\vec{CD}$ ?",
                            'options': ["$ABDC$ est un parallélogramme", "$ABCD$ est un rectangle", "$AB = CD$ seulement", "$A = C$ et $B = D$"],
                            'reponse_correcte': '0',
                            'explication': "L'égalité de deux vecteurs signifie même direction, même sens, même norme : la translation qui envoie $A$ sur $B$ envoie $C$ sur $D$, donc $ABDC$ est un parallélogramme.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Quelle est la norme du vecteur nul $\\vec{0}$ ?",
                            'options': ["0", "1", "Indéfinie", "$-1$"],
                            'reponse_correcte': '0',
                            'explication': "Le vecteur nul $\\vec{0}$ a une norme égale à 0 et n'a ni direction ni sens définis.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "L'opposé du vecteur $\\vec{AB}$ est :",
                            'options': ["$\\vec{BA}$", "$\\vec{AB}$", "$\\vec{0}$", "$2\\vec{AB}$"],
                            'reponse_correcte': '0',
                            'explication': "L'opposé de $\\vec{AB}$ est $\\vec{BA} = -\\vec{AB}$ : même direction, même norme, mais sens contraire.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La relation de Chasles affirme que :",
                            'options': ["$\\vec{AB} + \\vec{BC} = \\vec{AC}$", "$\\vec{AB} + \\vec{AC} = \\vec{BC}$", "$\\vec{AB} - \\vec{BC} = \\vec{AC}$", "$\\vec{AB} \\times \\vec{BC} = \\vec{AC}$"],
                            'reponse_correcte': '0',
                            'explication': "La relation de Chasles permet de « chaîner » les vecteurs : $\\vec{AB} + \\vec{BC} = \\vec{AC}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Que vaut $\\vec{AB} + \\vec{BA}$ ?",
                            'options': ["$\\vec{0}$", "$2\\vec{AB}$", "$\\vec{AA}$", "$\\vec{BB}$"],
                            'reponse_correcte': '0',
                            'explication': "Par la relation de Chasles : $\\vec{AB} + \\vec{BA} = \\vec{AA} = \\vec{0}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Si $k < 0$, le vecteur $k\\vec{u}$ a :",
                            'options': ["Le sens opposé à $\\vec{u}$", "Le même sens que $\\vec{u}$", "Une direction différente de $\\vec{u}$", "Une norme nulle"],
                            'reponse_correcte': '0',
                            'explication': "Quand $k < 0$, $k\\vec{u}$ a la même direction que $\\vec{u}$ mais le sens opposé, avec une norme $|k| \\|\\vec{u}\\|$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Deux vecteurs sont colinéaires si et seulement si :",
                            'options': ["L'un est un multiple de l'autre", "Ils ont la même norme", "Ils sont perpendiculaires", "Leur somme est nulle"],
                            'reponse_correcte': '0',
                            'explication': "$\\vec{u}$ et $\\vec{v}$ sont colinéaires s'il existe $k \\in \\mathbb{R}$ tel que $\\vec{v} = k\\vec{u}$ (ou $\\vec{u} = \\vec{0}$). Ils ont la même direction.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "La somme de deux vecteurs peut se construire graphiquement par :",
                            'options': ["La règle du parallélogramme", "La règle du compas", "Le produit de leurs normes", "La médiatrice"],
                            'reponse_correcte': '0',
                            'explication': "On place les deux vecteurs au même point, puis on complète le parallélogramme : la diagonale donne le vecteur somme.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Si $I$ est le milieu de $[AB]$, alors $\\vec{AI}$ = :",
                            'options': ["$\\frac{1}{2}\\vec{AB}$", "$\\vec{AB}$", "$2\\vec{AB}$", "$-\\vec{AB}$"],
                            'reponse_correcte': '0',
                            'explication': "Le milieu $I$ de $[AB]$ vérifie $\\vec{AI} = \\frac{1}{2}\\vec{AB}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Si $\\vec{u}$ a pour norme 5 et $k = -3$, quelle est la norme de $k\\vec{u}$ ?",
                            'options': ["15", "$-15$", "5", "3"],
                            'reponse_correcte': '0',
                            'explication': "$\\|k\\vec{u}\\| = |k| \\times \\|\\vec{u}\\| = |-3| \\times 5 = 15$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "On dit que trois points $A$, $B$, $C$ sont alignés si :",
                            'options': ["$\\vec{AB}$ et $\\vec{AC}$ sont colinéaires", "$\\vec{AB} = \\vec{AC}$", "$\\vec{AB} + \\vec{AC} = \\vec{0}$", "$\\|\\vec{AB}\\| = \\|\\vec{AC}\\|$"],
                            'reponse_correcte': '0',
                            'explication': "Trois points sont alignés si et seulement si les vecteurs $\\vec{AB}$ et $\\vec{AC}$ sont colinéaires (même direction).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'vrai_faux',
                            'texte': "Le vecteur $\\vec{AB}$ et le vecteur $\\vec{BA}$ ont la même direction.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$\\vec{AB}$ et $\\vec{BA} = -\\vec{AB}$ ont la même direction (même droite support) mais des sens opposés.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Deux vecteurs de même norme sont toujours égaux.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Deux vecteurs égaux doivent avoir même direction, même sens ET même norme. La norme seule ne suffit pas.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "La relation de Chasles est valable pour n'importe quels trois points du plan.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Pour tous points $A$, $B$, $C$ du plan : $\\vec{AB} + \\vec{BC} = \\vec{AC}$. La relation est universelle.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'texte_libre',
                            'texte': "Simplifiez $\\vec{MA} + \\vec{AB} + \\vec{BN}$ en un seul vecteur. Écrivez la réponse sous la forme vec(XY).",
                            'options': None,
                            'reponse_correcte': 'vec(MN)',
                            'tolerances': ['MN', 'vec(MN)', 'vecteur MN'],
                            'explication': "Par la relation de Chasles : $\\vec{MA} + \\vec{AB} + \\vec{BN} = \\vec{MN}$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Si $\\vec{u}$ a pour norme 4, que vaut $\\|2\\vec{u}\\|$ ?",
                            'options': None,
                            'reponse_correcte': '8',
                            'tolerances': ['8,0', '8.0'],
                            'explication': "$\\|2\\vec{u}\\| = |2| \\times \\|\\vec{u}\\| = 2 \\times 4 = 8$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Soit $\\vec{u}(3; -1)$ et $\\vec{v}(-6; 2)$. Le déterminant $\\det(\\vec{u}, \\vec{v}) = x \\cdot y' - x' \\cdot y$. Que vaut-il ?",
                            'options': None,
                            'reponse_correcte': '0',
                            'tolerances': ['0', '0,0', '0.0'],
                            'explication': "$\\det(\\vec{u}, \\vec{v}) = 3 \\times 2 - (-1) \\times (-6) = 6 - 6 = 0$. Les vecteurs sont colinéaires.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'qcm',
                            'texte': "Si $\\vec{u} = 3\\vec{i} - 2\\vec{j}$ et $\\vec{v} = -\\vec{i} + 4\\vec{j}$, alors $\\vec{u} + \\vec{v}$ = :",
                            'options': ["$2\\vec{i} + 2\\vec{j}$", "$4\\vec{i} - 6\\vec{j}$", "$2\\vec{i} - 2\\vec{j}$", "$-3\\vec{i} + 2\\vec{j}$"],
                            'reponse_correcte': '0',
                            'explication': "$\\vec{u} + \\vec{v} = (3-1)\\vec{i} + (-2+4)\\vec{j} = 2\\vec{i} + 2\\vec{j}$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'qcm',
                            'texte': "On considère $A(1;3)$ et $B(4;7)$. Le vecteur $\\vec{AB}$ a pour coordonnées :",
                            'options': ["$(3; 4)$", "$(4; 7)$", "$(5; 10)$", "$(1; 3)$"],
                            'reponse_correcte': '0',
                            'explication': "$\\vec{AB} = (x_B - x_A; y_B - y_A) = (4-1; 7-3) = (3; 4)$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Coordonnées et applications analytiques',
                'duree': 40,
                'contenu': """# Coordonnées et applications analytiques

## Introduction

En associant un **repère** au plan, on peut traduire les objets géométriques (points, vecteurs, droites) en **coordonnées numériques**. Cette traduction permet de résoudre des problèmes de géométrie par le **calcul** : c'est la **géométrie analytique**.

---

## Le repère du plan

### Définition

Un **repère** du plan est défini par un point $O$ (l'**origine**) et deux vecteurs $\\vec{i}$ et $\\vec{j}$ non colinéaires (la **base**).

On le note $(O; \\vec{i}, \\vec{j})$.

- **Repère orthogonal** : $\\vec{i} \\perp \\vec{j}$.
- **Repère orthonormé (orthonormal)** : $\\vec{i} \\perp \\vec{j}$ et $\\|\\vec{i}\\| = \\|\\vec{j}\\| = 1$.

Sauf mention contraire, on travaille dans un repère **orthonormé**.

### Coordonnées d'un point

Tout point $M$ du plan s'écrit de façon unique :

$$\\vec{OM} = x\\,\\vec{i} + y\\,\\vec{j}$$

Le couple $(x; y)$ est constitué des **coordonnées** de $M$ : $x$ est l'**abscisse**, $y$ l'**ordonnée**.

---

## Coordonnées d'un vecteur

### Définition

Si $A(x_A; y_A)$ et $B(x_B; y_B)$, alors le vecteur $\\vec{AB}$ a pour coordonnées :

$$\\vec{AB} = \\begin{pmatrix} x_B - x_A \\\\ y_B - y_A \\end{pmatrix}$$

### Opérations en coordonnées

Soient $\\vec{u}(x; y)$ et $\\vec{v}(x'; y')$, et $k \\in \\mathbb{R}$ :

| Opération | Résultat |
|-----------|----------|
| $\\vec{u} + \\vec{v}$ | $(x + x' \\;;\\; y + y')$ |
| $\\vec{u} - \\vec{v}$ | $(x - x' \\;;\\; y - y')$ |
| $k\\vec{u}$ | $(kx \\;;\\; ky)$ |

### Égalité

$$\\vec{u} = \\vec{v} \\Longleftrightarrow x = x' \\text{ et } y = y'$$

---

## Distance entre deux points

Dans un repère **orthonormé**, la distance entre $A(x_A; y_A)$ et $B(x_B; y_B)$ est :

$$\\boxed{AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}}$$

C'est une conséquence directe du **théorème de Pythagore**.

### Norme d'un vecteur

$$\\|\\vec{u}\\| = \\sqrt{x^2 + y^2} \\qquad \\text{pour } \\vec{u}(x; y)$$

#### Exemple

$A(1; 3)$ et $B(4; 7)$ :

$$AB = \\sqrt{(4-1)^2 + (7-3)^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$$

---

## Coordonnées du milieu

Le **milieu** $I$ du segment $[AB]$ a pour coordonnées :

$$\\boxed{I\\left(\\frac{x_A + x_B}{2} \\;;\\; \\frac{y_A + y_B}{2}\\right)}$$

#### Exemple

$A(2; 6)$, $B(8; -2)$ : $I\\left(\\frac{2+8}{2}; \\frac{6+(-2)}{2}\\right) = I(5; 2)$.

---

## Colinéarité en coordonnées

### Déterminant

Soyens $\\vec{u}(x; y)$ et $\\vec{v}(x'; y')$. Le **déterminant** de $\\vec{u}$ et $\\vec{v}$ est :

$$\\det(\\vec{u}, \\vec{v}) = xy' - x'y$$

### Critère de colinéarité

$$\\boxed{\\vec{u} \\text{ et } \\vec{v} \\text{ sont colinéaires} \\Longleftrightarrow \\det(\\vec{u}, \\vec{v}) = 0 \\Longleftrightarrow xy' - x'y = 0}$$

#### Exemple

$\\vec{u}(3; -2)$ et $\\vec{v}(-6; 4)$ :

$$\\det(\\vec{u}, \\vec{v}) = 3 \\times 4 - (-2) \\times (-6) = 12 - 12 = 0$$

Les vecteurs sont colinéaires. En effet, $\\vec{v} = -2\\vec{u}$.

---

## Application : alignement de trois points

Pour montrer que $A$, $B$, $C$ sont alignés, on vérifie :

$$\\det(\\vec{AB}, \\vec{AC}) = 0$$

#### Exemple

$A(1;2)$, $B(3;6)$, $C(5;10)$ :

$\\vec{AB} = (2;4)$, $\\vec{AC} = (4;8)$.

$\\det(\\vec{AB}, \\vec{AC}) = 2 \\times 8 - 4 \\times 4 = 16 - 16 = 0$

Les points $A$, $B$, $C$ sont alignés. ✓

---

## Application : démontrer qu'un quadrilatère est un parallélogramme

$ABCD$ est un parallélogramme ⟺ $\\vec{AB} = \\vec{DC}$.

#### Exemple

$A(0;1)$, $B(3;5)$, $C(7;3)$, $D(4;-1)$ :

$\\vec{AB} = (3;4)$ et $\\vec{DC} = (7-4; 3-(-1)) = (3;4)$.

$\\vec{AB} = \\vec{DC}$ ✓ → $ABCD$ est un parallélogramme.

---

## Application : trouver un point à partir d'une relation vectorielle

### Exemple

On cherche le point $D$ tel que $ABCD$ soit un parallélogramme, avec $A(1;2)$, $B(4;6)$, $C(6;3)$.

On doit avoir $\\vec{AB} = \\vec{DC}$ :

$\\vec{AB} = (3;4)$, et $\\vec{DC} = (x_C - x_D; y_C - y_D) = (6-x_D; 3-y_D)$.

$$6 - x_D = 3 \\implies x_D = 3 \\qquad \\text{et} \\qquad 3 - y_D = 4 \\implies y_D = -1$$

Donc $D(3; -1)$.

---

## Décomposition d'un vecteur dans une base

Toute paire de vecteurs **non colinéaires** $(\\vec{u}, \\vec{v})$ forme une **base** du plan. Tout vecteur $\\vec{w}$ s'écrit alors :

$$\\vec{w} = a\\,\\vec{u} + b\\,\\vec{v}$$

avec un **unique** couple $(a, b)$.

Pour trouver $a$ et $b$, on résout un **système de deux équations** à deux inconnues en identifiant les coordonnées.

#### Exemple

Décomposer $\\vec{w}(7; 1)$ dans la base $(\\vec{u}(2; 1), \\vec{v}(1; 3))$.

On cherche $a$ et $b$ tels que $a\\vec{u} + b\\vec{v} = \\vec{w}$ :

$$\\begin{cases} 2a + b = 7 \\\\ a + 3b = 1 \\end{cases}$$

De la 2ᵉ équation : $a = 1 - 3b$. En substituant : $2(1-3b) + b = 7 \\implies 2 - 6b + b = 7 \\implies -5b = 5 \\implies b = -1$.

Donc $a = 1 - 3(-1) = 4$.

$\\vec{w} = 4\\vec{u} - \\vec{v}$. **Vérification** : $4(2;1) + (-1)(1;3) = (8-1; 4-3) = (7;1)$ ✓

---

## À retenir

- Dans un repère $(O; \\vec{i}, \\vec{j})$, tout vecteur $\\vec{AB}$ a des coordonnées $(x_B - x_A; y_B - y_A)$.
- **Distance** : $AB = \\sqrt{(x_B-x_A)^2 + (y_B-y_A)^2}$ (repère orthonormé).
- **Milieu** : $I\\left(\\frac{x_A+x_B}{2}; \\frac{y_A+y_B}{2}\\right)$.
- **Colinéarité** : $\\vec{u}$ et $\\vec{v}$ colinéaires ⟺ $xy' - x'y = 0$.
- Pour prouver un alignement, on calcule $\\det(\\vec{AB}, \\vec{AC})$ ; pour un parallélogramme, on vérifie $\\vec{AB} = \\vec{DC}$.
""",
                'quiz': {
                    'titre': "Quiz — Coordonnées et applications analytiques",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Le vecteur $\\vec{AB}$ avec $A(2;5)$ et $B(7;3)$ a pour coordonnées :",
                            'options': ["$(5; -2)$", "$(7; 3)$", "$(9; 8)$", "$(-5; 2)$"],
                            'reponse_correcte': '0',
                            'explication': "$\\vec{AB} = (x_B - x_A; y_B - y_A) = (7-2; 3-5) = (5; -2)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "La distance entre $A(1;2)$ et $B(4;6)$ dans un repère orthonormé est :",
                            'options': ["5", "7", "25", "$\\sqrt{7}$"],
                            'reponse_correcte': '0',
                            'explication': "$AB = \\sqrt{(4-1)^2 + (6-2)^2} = \\sqrt{9+16} = \\sqrt{25} = 5$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Le milieu $I$ de $[AB]$ avec $A(2;8)$ et $B(6;4)$ a pour coordonnées :",
                            'options': ["$(4; 6)$", "$(8; 12)$", "$(2; 2)$", "$(4; 4)$"],
                            'reponse_correcte': '0',
                            'explication': "$I\\left(\\frac{2+6}{2}; \\frac{8+4}{2}\\right) = (4; 6)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Si $\\vec{u}(3;6)$, alors la norme $\\|\\vec{u}\\|$ vaut :",
                            'options': ["$3\\sqrt{5}$", "9", "45", "$\\sqrt{9}$"],
                            'reponse_correcte': '0',
                            'explication': "$\\|\\vec{u}\\| = \\sqrt{3^2+6^2} = \\sqrt{9+36} = \\sqrt{45} = 3\\sqrt{5}$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Deux vecteurs $\\vec{u}(a;b)$ et $\\vec{v}(a';b')$ sont colinéaires si et seulement si :",
                            'options': ["$ab' - a'b = 0$", "$a + a' = 0$", "$ab' + a'b = 0$", "$aa' + bb' = 0$"],
                            'reponse_correcte': '0',
                            'explication': "Le critère de colinéarité par le déterminant : $\\det(\\vec{u}, \\vec{v}) = ab' - a'b = 0$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Si $\\vec{u}(2;-1)$ et $\\vec{v}(4;-2)$, ces vecteurs sont :",
                            'options': ["Colinéaires", "Perpendiculaires", "De même norme", "Opposés"],
                            'reponse_correcte': '0',
                            'explication': "$\\det(\\vec{u},\\vec{v}) = 2 \\times (-2) - (-1) \\times 4 = -4 + 4 = 0$. Ils sont colinéaires ($\\vec{v} = 2\\vec{u}$).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "La somme $\\vec{u}(1;3) + \\vec{v}(4;-2)$ donne le vecteur :",
                            'options': ["$(5; 1)$", "$(3; 5)$", "$(4; -6)$", "$(5; 5)$"],
                            'reponse_correcte': '0',
                            'explication': "$\\vec{u} + \\vec{v} = (1+4; 3+(-2)) = (5; 1)$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "$3\\vec{u}$ avec $\\vec{u}(-2; 5)$ a pour coordonnées :",
                            'options': ["$(-6; 15)$", "$(6; -15)$", "$(-6; -15)$", "$(-2; 15)$"],
                            'reponse_correcte': '0',
                            'explication': "$3\\vec{u} = 3(-2; 5) = (-6; 15)$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Pour montrer que $ABCD$ est un parallélogramme, on vérifie que :",
                            'options': ["$\\vec{AB} = \\vec{DC}$", "$\\vec{AB} = \\vec{BC}$", "$AB = CD$", "$\\vec{AC} = \\vec{BD}$"],
                            'reponse_correcte': '0',
                            'explication': "$ABCD$ est un parallélogramme ⟺ $\\vec{AB} = \\vec{DC}$ (les côtés opposés sont des translations).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Si $\\vec{u}(1;2)$ et $\\vec{v}(3;-1)$, que vaut $\\det(\\vec{u}, \\vec{v})$ ?",
                            'options': ["$-7$", "7", "5", "$-5$"],
                            'reponse_correcte': '0',
                            'explication': "$\\det(\\vec{u},\\vec{v}) = 1 \\times (-1) - 2 \\times 3 = -1 - 6 = -7$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "La distance entre $C(0;0)$ et $D(5;12)$ est :",
                            'options': ["13", "17", "$\\sqrt{17}$", "7"],
                            'reponse_correcte': '0',
                            'explication': "$CD = \\sqrt{25+144} = \\sqrt{169} = 13$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Les points $A(1;1)$, $B(3;5)$ et $C(2;3)$ sont-ils alignés ?",
                            'options': ["Oui", "Non", "Impossible à déterminer", "Seulement si $AB = BC$"],
                            'reponse_correcte': '0',
                            'explication': "$\\vec{AB}(2;4)$, $\\vec{AC}(1;2)$. $\\det = 2 \\times 2 - 4 \\times 1 = 0$. Les vecteurs sont colinéaires, donc les points sont alignés.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'vrai_faux',
                            'texte': "La distance $AB$ est toujours positive ou nulle.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$AB = \\sqrt{(x_B-x_A)^2 + (y_B-y_A)^2} \\geq 0$. La racine carrée est toujours positive ou nulle.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'vrai_faux',
                            'texte': "Si $\\det(\\vec{u}, \\vec{v}) \\neq 0$, alors $\\vec{u}$ et $\\vec{v}$ ne sont pas colinéaires.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "La colinéarité est équivalente à un déterminant nul. Si le déterminant est non nul, les vecteurs ne sont pas colinéaires.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Le milieu de $[AB]$ est le seul point $I$ tel que $\\vec{IA} + \\vec{IB} = \\vec{0}$.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "$\\vec{IA} + \\vec{IB} = \\vec{0}$ est la caractérisation vectorielle du milieu de $[AB]$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'texte_libre',
                            'texte': "Calculez la distance entre $A(0;0)$ et $B(3;4)$.",
                            'options': None,
                            'reponse_correcte': '5',
                            'tolerances': ['5,0', '5.0'],
                            'explication': "$AB = \\sqrt{3^2 + 4^2} = \\sqrt{9+16} = \\sqrt{25} = 5$.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'texte_libre',
                            'texte': "Soit $A(-1; 3)$ et $B(5; 7)$. Donnez l'ordonnée du milieu de $[AB]$.",
                            'options': None,
                            'reponse_correcte': '5',
                            'tolerances': ['5,0', '5.0'],
                            'explication': "$y_I = \\frac{3+7}{2} = \\frac{10}{2} = 5$.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Soit $\\vec{u}(2;3)$ et $\\vec{v}(4;k)$. Pour quelle valeur de $k$ ces vecteurs sont-ils colinéaires ?",
                            'options': None,
                            'reponse_correcte': '6',
                            'tolerances': ['6,0', '6.0'],
                            'explication': "Colinéaires ⟺ $\\det = 2k - 3 \\times 4 = 0 \\Rightarrow 2k = 12 \\Rightarrow k = 6$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'qcm',
                            'texte': "Soit $A(1;2)$, $B(3;6)$, $C(5;2)$ et $D(3;-2)$. Le quadrilatère $ABCD$ est-il un parallélogramme ?",
                            'options': ["Oui", "Non", "On ne peut pas savoir", "Seulement si $AB = CD$"],
                            'reponse_correcte': '0',
                            'explication': "$\\vec{AB}(2;4)$ et $\\vec{DC}(3-5; -2-2) = (-2;-4) = -\\vec{AB}$. Donc $\\vec{AB} \\neq \\vec{DC}$. Vérifions $\\vec{AD}(2;-4)$ et $\\vec{BC}(2;-4)$. $\\vec{AD} = \\vec{BC}$ donc $ABCD$ est un parallélogramme (autre ordre de lecture).",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'qcm',
                            'texte': "Les vecteurs $\\vec{u}(2;5)$ et $\\vec{v}(-4;-10)$ sont colinéaires. Quel est le coefficient $k$ tel que $\\vec{v} = k\\vec{u}$ ?",
                            'options': ["$-2$", "2", "$-\\frac{1}{2}$", "$\\frac{1}{2}$"],
                            'reponse_correcte': '0',
                            'explication': "$\\vec{v} = (-4;-10) = -2(2;5) = -2\\vec{u}$, donc $k = -2$.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 10 — Droites dans le plan
    # ──────────────────────────────────────────────
    {
        'ordre': 10,
        'titre': 'Droites dans le plan',
        'description': "Équations de droites sous différentes formes, positions relatives et systèmes d'équations linéaires à deux inconnues.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': "Équations de droites",
                'duree': 35,
                'contenu': """# Équations de droites

## Introduction

Dans un repère du plan $(O; \\vec{i}, \\vec{j})$, toute droite peut être décrite par une **équation** reliant les coordonnées $(x; y)$ de ses points. Selon la situation, on utilise l'**équation réduite** ou l'**équation cartésienne**.

---

## 1. Équation réduite d'une droite

### Définition

Une droite **non verticale** admet une unique **équation réduite** de la forme :

$$y = ax + b$$

où :

- $a$ est le **coefficient directeur** (ou pente) de la droite,
- $b$ est l'**ordonnée à l'origine** (c'est-à-dire $y$ quand $x = 0$).

> **Cas particulier :** une droite **verticale** d'abscisse $k$ a pour équation $x = k$. Elle n'admet pas d'équation réduite.

### Calcul de la pente

Si deux points $A(x_A; y_A)$ et $B(x_B; y_B)$ appartiennent à une droite **non verticale** (i.e. $x_A \\neq x_B$), alors :

$$a = \\frac{y_B - y_A}{x_B - x_A}$$

**Interprétation :** la pente mesure l'inclinaison de la droite.

| Valeur de $a$ | Comportement |
|----------------|-------------|
| $a > 0$ | La droite « monte » (de gauche à droite) |
| $a < 0$ | La droite « descend » |
| $a = 0$ | La droite est **horizontale** ($y = b$) |

### Déterminer l'équation réduite

**Méthode :** connaissant un point $A(x_A; y_A)$ et la pente $a$, on écrit :

$$y - y_A = a(x - x_A)$$

puis on développe pour obtenir la forme $y = ax + b$.

**Exemple :** Trouver l'équation de la droite passant par $A(2; 5)$ de pente $a = -3$.

$$y - 5 = -3(x - 2) \\implies y = -3x + 6 + 5 \\implies y = -3x + 11$$

---

## 2. Équation cartésienne d'une droite

### Définition

Toute droite du plan (y compris les droites verticales) admet une **équation cartésienne** :

$$\\alpha x + \\beta y + \\gamma = 0 \\qquad (\\alpha; \\beta) \\neq (0; 0)$$

> On note souvent les coefficients $a$, $b$, $c$ au lieu de $\\alpha$, $\\beta$, $\\gamma$. Attention à ne pas confondre le $a$ de l'équation cartésienne avec la pente.

### Passage d'une forme à l'autre

| De … | Vers … | Méthode |
|-------|--------|---------|
| $y = ax + b$ | $\\alpha x + \\beta y + \\gamma = 0$ | $ax - y + b = 0$ |
| $\\alpha x + \\beta y + \\gamma = 0$ ($\\beta \\neq 0$) | $y = ax + b$ | $y = -\\frac{\\alpha}{\\beta}x - \\frac{\\gamma}{\\beta}$ |

### Vecteur directeur et vecteur normal

Pour une droite d'équation $\\alpha x + \\beta y + \\gamma = 0$ :

- Un **vecteur directeur** est $\\vec{u}(-\\beta; \\alpha)$.
- Un **vecteur normal** est $\\vec{n}(\\alpha; \\beta)$.

> Le vecteur normal est **perpendiculaire** à la droite ; le vecteur directeur lui est **parallèle**.

---

## 3. Positions relatives de deux droites

Soient deux droites $d_1 : y = a_1 x + b_1$ et $d_2 : y = a_2 x + b_2$.

| Condition | Position relative |
|-----------|-------------------|
| $a_1 = a_2$ et $b_1 = b_2$ | Droites **confondues** |
| $a_1 = a_2$ et $b_1 \\neq b_2$ | Droites **strictement parallèles** |
| $a_1 \\neq a_2$ | Droites **sécantes** (un unique point d'intersection) |

### Cas de la perpendicularité

Deux droites non verticales de pentes $a_1$ et $a_2$ sont **perpendiculaires** si et seulement si :

$$a_1 \\times a_2 = -1$$

**Exemple :** Si $d_1$ a pour pente $a_1 = 2$, toute droite perpendiculaire a pour pente $a_2 = -\\frac{1}{2}$.

---

## 4. Droite passant par deux points

Connaissant $A(x_A; y_A)$ et $B(x_B; y_B)$ avec $x_A \\neq x_B$ :

1. Calculer $a = \\frac{y_B - y_A}{x_B - x_A}$
2. Utiliser $y - y_A = a(x - x_A)$

**Exemple :** Droite passant par $A(1; 3)$ et $B(4; -6)$ :

$$a = \\frac{-6 - 3}{4 - 1} = \\frac{-9}{3} = -3$$

$$y - 3 = -3(x - 1) \\implies y = -3x + 6$$

Si $x_A = x_B$, la droite est verticale : $x = x_A$.

---

## 5. Intersection de deux droites (lecture graphique)

Graphiquement, le point d'intersection de deux droites sécantes se lit aux coordonnées du point commun. Algébriquement, on résout le **système** formé par les deux équations (voir leçon suivante).

---

## À retenir

- Une droite **non verticale** a une équation réduite $y = ax + b$ (pente $a$, ordonnée à l'origine $b$).
- Une droite **quelconque** a une équation cartésienne $\\alpha x + \\beta y + \\gamma = 0$.
- La **pente** entre deux points : $a = \\frac{y_B - y_A}{x_B - x_A}$.
- Deux droites sont **parallèles** ⟺ même pente ; **perpendiculaires** ⟺ $a_1 a_2 = -1$.
- Un vecteur directeur de $\\alpha x + \\beta y + \\gamma = 0$ est $\\vec{u}(-\\beta; \\alpha)$.
""",
                'quiz': {
                    'titre': 'Quiz — Équations de droites',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Quelle est la forme de l'équation réduite d'une droite non verticale ?",
                            'options': ["y = ax + b", "ax + by + c = 0", "x = k", "y² = ax + b"],
                            'reponse_correcte': '0',
                            'explication': "L'équation réduite d'une droite non verticale s'écrit y = ax + b, où a est la pente et b l'ordonnée à l'origine.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Dans l'équation y = ax + b, que représente b ?",
                            'options': ["L'ordonnée à l'origine", "La pente de la droite", "L'abscisse à l'origine", "Le vecteur directeur"],
                            'reponse_correcte': '0',
                            'explication': "b est la valeur de y quand x = 0, c'est-à-dire l'ordonnée à l'origine.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "Quelle est la pente de la droite d'équation y = 3x − 2 ?",
                            'options': ["3", "-2", "3/2", "-3"],
                            'reponse_correcte': '0',
                            'explication': "Dans y = ax + b, le coefficient a est la pente. Ici a = 3.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Quelle équation représente une droite verticale ?",
                            'options': ["x = 5", "y = 5", "y = 5x", "x + y = 5"],
                            'reponse_correcte': '0',
                            'explication': "Une droite verticale a pour équation x = k (constante). Elle n'admet pas d'équation réduite.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Quelle est la pente de la droite passant par A(1 ; 2) et B(3 ; 6) ?",
                            'options': ["2", "4", "1/2", "3"],
                            'reponse_correcte': '0',
                            'explication': "a = (6 − 2) / (3 − 1) = 4 / 2 = 2.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Quelle est l'ordonnée à l'origine de la droite y = −x + 5 ?",
                            'options': ["5", "-1", "-5", "1"],
                            'reponse_correcte': '0',
                            'explication': "L'ordonnée à l'origine est b = 5 (valeur de y quand x = 0).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "L'équation y = 4 représente :",
                            'options': ["Une droite horizontale", "Une droite verticale", "Un point", "Une parabole"],
                            'reponse_correcte': '0',
                            'explication': "y = 4 est de la forme y = 0·x + 4 : pente nulle, donc droite horizontale.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Un vecteur directeur de la droite y = 2x + 1 est :",
                            'options': ["(1 ; 2)", "(2 ; 1)", "(1 ; -2)", "(-2 ; 1)"],
                            'reponse_correcte': '0',
                            'explication': "Pour y = ax + b, un vecteur directeur est (1 ; a). Ici (1 ; 2).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "La droite passant par A(1 ; 3) de pente −2 a pour équation :",
                            'options': ["y = -2x + 5", "y = -2x + 3", "y = -2x + 1", "y = 2x + 1"],
                            'reponse_correcte': '0',
                            'explication': "y − 3 = −2(x − 1) → y = −2x + 2 + 3 = −2x + 5.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Deux droites de pentes respectives 3 et −1/3 sont :",
                            'options': ["Perpendiculaires", "Parallèles", "Confondues", "Sécantes non perpendiculaires"],
                            'reponse_correcte': '0',
                            'explication': "Le produit des pentes vaut 3 × (−1/3) = −1, donc les droites sont perpendiculaires.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "La droite d'équation cartésienne 2x − 3y + 6 = 0 a pour pente :",
                            'options': ["2/3", "-2/3", "3/2", "-3/2"],
                            'reponse_correcte': '0',
                            'explication': "2x − 3y + 6 = 0 → 3y = 2x + 6 → y = (2/3)x + 2. La pente est 2/3.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Un vecteur normal à la droite 3x + 4y − 7 = 0 est :",
                            'options': ["(3 ; 4)", "(-4 ; 3)", "(4 ; -3)", "(3 ; -4)"],
                            'reponse_correcte': '0',
                            'explication': "Pour αx + βy + γ = 0, un vecteur normal est (α ; β). Ici (3 ; 4).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "L'équation réduite de la droite passant par (0 ; −1) et (2 ; 3) est :",
                            'options': ["y = 2x − 1", "y = 2x + 1", "y = -2x − 1", "y = x − 1"],
                            'reponse_correcte': '0',
                            'explication': "a = (3 − (−1)) / (2 − 0) = 4/2 = 2 et b = −1 (ordonnée pour x = 0). Donc y = 2x − 1.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Les droites y = 2x + 1 et y = 2x − 3 sont :",
                            'options': ["Strictement parallèles", "Sécantes", "Confondues", "Perpendiculaires"],
                            'reponse_correcte': '0',
                            'explication': "Même pente a = 2 mais ordonnées à l'origine différentes (1 ≠ −3) : parallèles distinctes.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "La droite d'équation x = 3 admet une équation réduite de la forme y = ax + b.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Une droite verticale n'admet pas d'équation réduite car elle n'est pas le graphe d'une fonction.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "Si deux droites non verticales sont perpendiculaires, le produit de leurs pentes vaut −1.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est la condition de perpendicularité : a₁ × a₂ = −1.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Le vecteur (2 ; −1) est un vecteur directeur de la droite x + 2y − 3 = 0.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Pour αx + βy + γ = 0, un vecteur directeur est (−β ; α) = (−2 ; 1). Or (2 ; −1) = −1 × (−2 ; 1), c'est donc aussi un vecteur directeur.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Calculer la pente de la droite passant par A(−1 ; 4) et B(3 ; −2). Donner le résultat sous forme de fraction.",
                            'options': None,
                            'reponse_correcte': '-3/2',
                            'tolerances': ["-3/2", "-1.5", "-1,5"],
                            'explication': "a = (−2 − 4) / (3 − (−1)) = −6 / 4 = −3/2.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Déterminer la valeur de b pour que la droite y = 2x + b passe par le point (3 ; 1).",
                            'options': None,
                            'reponse_correcte': '-5',
                            'tolerances': ["-5"],
                            'explication': "1 = 2 × 3 + b → b = 1 − 6 = −5.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "La droite d a pour équation 4x − 2y + 6 = 0. Quelle est son ordonnée à l'origine ?",
                            'options': None,
                            'reponse_correcte': '3',
                            'tolerances': ["3"],
                            'explication': "4x − 2y + 6 = 0 → 2y = 4x + 6 → y = 2x + 3. L'ordonnée à l'origine est b = 3.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': "Systèmes d'équations linéaires",
                'duree': 35,
                'contenu': """# Systèmes d'équations linéaires

## Introduction

Un **système de deux équations à deux inconnues** est un ensemble de deux conditions que doivent vérifier simultanément les valeurs de $x$ et $y$. Résoudre un tel système, c'est trouver **tous les couples** $(x; y)$ solutions.

---

## 1. Forme générale

Un système linéaire de deux équations à deux inconnues s'écrit :

$$\\begin{cases} a_1 x + b_1 y = c_1 \\\\ a_2 x + b_2 y = c_2 \\end{cases}$$

**Interprétation graphique :** chaque équation représente une droite. Résoudre le système revient à trouver le(s) point(s) d'intersection des deux droites.

---

## 2. Trois cas possibles

| Cas | Droites | Nombre de solutions |
|-----|---------|---------------------|
| 1 | Sécantes | **Exactement une** solution |
| 2 | Strictement parallèles | **Aucune** solution |
| 3 | Confondues | **Infinité** de solutions |

---

## 3. Méthode par substitution

**Principe :** on isole une inconnue dans l'une des équations, puis on remplace dans l'autre.

**Exemple :**

$$\\begin{cases} 2x + y = 7 \\\\ x - 3y = -6 \\end{cases}$$

**Étape 1 :** On isole $y$ dans la première équation :

$$y = 7 - 2x$$

**Étape 2 :** On remplace dans la seconde :

$$x - 3(7 - 2x) = -6$$

$$x - 21 + 6x = -6$$

$$7x = 15$$

$$x = \\frac{15}{7}$$

**Étape 3 :** On calcule $y$ :

$$y = 7 - 2 \\times \\frac{15}{7} = 7 - \\frac{30}{7} = \\frac{49 - 30}{7} = \\frac{19}{7}$$

**Solution :** $\\left(\\frac{15}{7}; \\frac{19}{7}\\right)$.

> **Conseil :** la substitution est efficace quand un coefficient vaut $1$ ou $-1$.

---

## 4. Méthode par combinaison linéaire

**Principe :** on multiplie les équations par des coefficients choisis pour **éliminer** une inconnue lorsqu'on additionne les deux équations.

**Exemple :**

$$\\begin{cases} 3x + 2y = 12 \\\\ 5x - 2y = 4 \\end{cases}$$

En additionnant membre à membre :

$$8x = 16 \\implies x = 2$$

On remplace : $3(2) + 2y = 12 \\implies 2y = 6 \\implies y = 3$.

**Solution :** $(2; 3)$.

**Autre exemple :** si les coefficients ne s'annulent pas directement, on les ajuste.

$$\\begin{cases} 2x + 3y = 1 \\quad (L_1) \\\\ 5x + 4y = -2 \\quad (L_2) \\end{cases}$$

Pour éliminer $x$ : on calcule $5 \\times (L_1) - 2 \\times (L_2)$ :

$$10x + 15y - 10x - 8y = 5 - (-4)$$

$$7y = 9 \\implies y = \\frac{9}{7}$$

Puis on calcule $x$ en reportant.

---

## 5. Cas sans solution et cas d'infinité de solutions

### Aucune solution

$$\\begin{cases} x + 2y = 3 \\\\ 2x + 4y = 8 \\end{cases}$$

La seconde équation est $2 \\times$ la première avec un second membre différent ($8 \\neq 6$). Les droites sont **parallèles** et distinctes : le système est **incompatible**.

### Infinité de solutions

$$\\begin{cases} x + 2y = 3 \\\\ 2x + 4y = 6 \\end{cases}$$

La seconde équation est exactement $2 \\times$ la première. Les droites sont **confondues** : tout point de la droite $x + 2y = 3$ est solution. Le système est dit **indéterminé**.

---

## 6. Mise en équation de problèmes

La résolution de systèmes est un outil puissant pour les problèmes concrets.

**Exemple :** Dans une boulangerie, 3 croissants et 2 pains au chocolat coûtent 5,30 €, tandis que 2 croissants et 5 pains au chocolat coûtent 8,50 €. Quel est le prix de chaque viennoiserie ?

On pose $x$ = prix d'un croissant, $y$ = prix d'un pain au chocolat :

$$\\begin{cases} 3x + 2y = 5{,}30 \\\\ 2x + 5y = 8{,}50 \\end{cases}$$

Par combinaison (multiplier $L_1$ par $5$ et $L_2$ par $-2$) :

$$15x + 10y - 4x - 10y = 26{,}50 - 17{,}00$$

$$11x = 9{,}50 \\implies x \\approx 0{,}86 \\text{ €}$$

Puis $y = \\frac{5{,}30 - 3(0{,}86)}{2} \\approx 1{,}36 \\text{ €}$.

---

## 7. Vérification des solutions

Il est **essentiel** de vérifier la solution en la substituant dans les **deux** équations du système. Cela permet de détecter les erreurs de calcul.

---

## À retenir

- Un système $2 \\times 2$ peut avoir **une**, **zéro** ou **une infinité** de solutions.
- **Substitution** : on isole une variable, on remplace dans l'autre équation.
- **Combinaison linéaire** : on multiplie les équations pour éliminer une inconnue.
- Graphiquement : une solution = point d'intersection de deux droites.
- Toujours **vérifier** la solution dans les deux équations.
""",
                'quiz': {
                    'titre': "Quiz — Systèmes d'équations linéaires",
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Résoudre un système de deux équations à deux inconnues, c'est trouver :",
                            'options': ["Tous les couples (x ; y) vérifiant les deux équations", "Une seule valeur de x", "La pente de chaque droite", "Le produit des deux équations"],
                            'reponse_correcte': '0',
                            'explication': "Un système cherche tous les couples (x ; y) qui satisfont simultanément les deux équations.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "Combien de solutions possède un système dont les droites sont sécantes ?",
                            'options': ["Exactement une", "Aucune", "Deux", "Une infinité"],
                            'reponse_correcte': '0',
                            'explication': "Deux droites sécantes se coupent en un unique point : le système a exactement une solution.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "On considère le système {x + y = 5 ; x − y = 1}. En additionnant les deux équations, on obtient :",
                            'options': ["2x = 6", "2y = 6", "2x = 4", "x + y = 6"],
                            'reponse_correcte': '0',
                            'explication': "(x + y) + (x − y) = 5 + 1, soit 2x = 6.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "La méthode qui consiste à isoler une variable dans une équation puis à la remplacer dans l'autre s'appelle :",
                            'options': ["La substitution", "La combinaison linéaire", "La factorisation", "L'élimination graphique"],
                            'reponse_correcte': '0',
                            'explication': "La méthode de substitution consiste à exprimer une inconnue en fonction de l'autre, puis à reporter.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "Si deux droites sont parallèles et distinctes, le système a :",
                            'options': ["Aucune solution", "Exactement une solution", "Une infinité de solutions", "Deux solutions"],
                            'reponse_correcte': '0',
                            'explication': "Des droites parallèles distinctes ne se coupent jamais : le système est incompatible.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Le couple (2 ; 3) est-il solution du système {2x + y = 7 ; x − y = −1} ?",
                            'options': ["Oui", "Non, il ne vérifie que la première", "Non, il ne vérifie que la seconde", "Non, il ne vérifie aucune"],
                            'reponse_correcte': '0',
                            'explication': "2(2) + 3 = 7 ✓ et 2 − 3 = −1 ✓. Le couple vérifie les deux équations.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Dans la méthode par combinaison linéaire, on cherche à :",
                            'options': ["Éliminer une inconnue en additionnant les équations", "Isoler x dans la première équation", "Multiplier les deux équations entre elles", "Tracer le graphique des droites"],
                            'reponse_correcte': '0',
                            'explication': "On multiplie les équations par des coefficients adaptés pour éliminer une inconnue en les additionnant.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Deux droites confondues donnent un système ayant :",
                            'options': ["Une infinité de solutions", "Aucune solution", "Exactement une solution", "Exactement deux solutions"],
                            'reponse_correcte': '0',
                            'explication': "Des droites confondues ont tous leurs points en commun : le système est indéterminé (infinité de solutions).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Résoudre {2x + 3y = 12 ; x − y = 1}. La solution est :",
                            'options': ["(3 ; 2)", "(2 ; 3)", "(1 ; 0)", "(4 ; 1)"],
                            'reponse_correcte': '0',
                            'explication': "x = 1 + y → 2(1 + y) + 3y = 12 → 2 + 5y = 12 → y = 2 → x = 3.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Le système {3x + 2y = 8 ; 6x + 4y = 16} a :",
                            'options': ["Une infinité de solutions", "Exactement une solution", "Aucune solution", "Exactement deux solutions"],
                            'reponse_correcte': '0',
                            'explication': "La seconde équation est exactement 2 fois la première : les droites sont confondues.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Résoudre {x + 2y = 5 ; 3x − y = 1}. La solution est :",
                            'options': ["(1 ; 2)", "(2 ; 1)", "(3 ; 1)", "(1 ; 3)"],
                            'reponse_correcte': '0',
                            'explication': "x = 5 − 2y → 3(5 − 2y) − y = 1 → 15 − 7y = 1 → y = 2 → x = 1.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Le système {2x + y = 7 ; 4x + 2y = 10} a :",
                            'options': ["Aucune solution", "Exactement une solution", "Une infinité de solutions", "Deux solutions"],
                            'reponse_correcte': '0',
                            'explication': "4x + 2y devrait valoir 2 × 7 = 14, or le second membre est 10 ≠ 14 : contradiction, aucune solution.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "La somme de deux nombres est 10 et leur différence est 4. Ces nombres sont :",
                            'options': ["7 et 3", "8 et 2", "6 et 4", "9 et 1"],
                            'reponse_correcte': '0',
                            'explication': "{x + y = 10 ; x − y = 4} → 2x = 14 → x = 7, y = 3.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "Résoudre {5x − 3y = −1 ; 2x + 3y = 8}. En additionnant, on obtient :",
                            'options': ["7x = 7, donc x = 1 et y = 2", "7x = 9, donc x = 9/7", "3x = 7, donc x = 7/3", "7x = −9, donc x = −9/7"],
                            'reponse_correcte': '0',
                            'explication': "(5x − 3y) + (2x + 3y) = −1 + 8 → 7x = 7 → x = 1 → 2 + 3y = 8 → y = 2.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Un système de deux équations linéaires à deux inconnues a toujours au moins une solution.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Un système de deux droites parallèles distinctes n'a aucune solution.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "La méthode par combinaison linéaire consiste à multiplier les équations par des coefficients adaptés puis à les additionner pour éliminer une inconnue.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est exactement le principe de la combinaison linéaire.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Le système {x + y = 3 ; 2x + 2y = 6} a exactement une solution.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La seconde équation est 2 fois la première : les droites sont confondues, le système a une infinité de solutions.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Résoudre {x + y = 10 ; x − y = 4}. Donner la valeur de x.",
                            'options': None,
                            'reponse_correcte': '7',
                            'tolerances': ["7"],
                            'explication': "En additionnant : 2x = 14, donc x = 7.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Résoudre {3x + y = 7 ; x + 2y = 4}. Donner la valeur de y.",
                            'options': None,
                            'reponse_correcte': '1',
                            'tolerances': ["1"],
                            'explication': "y = 7 − 3x → x + 2(7 − 3x) = 4 → −5x = −10 → x = 2 → y = 7 − 6 = 1.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Le système {2x − 4y = 6 ; −x + 2y = 1} a combien de solutions ? Répondre par un nombre.",
                            'options': None,
                            'reponse_correcte': '0',
                            'tolerances': ["0", "aucune", "zéro"],
                            'explication': "En multipliant la 2ᵉ par 2 : −2x + 4y = 2. Addition avec la 1ʳᵉ : 0 = 8, impossible. Aucune solution.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 11 — Probabilités et échantillonnage
    # ──────────────────────────────────────────────
    {
        'ordre': 11,
        'titre': 'Probabilités et échantillonnage',
        'description': "Modélisation probabiliste, calcul de probabilités, événements, et introduction à l'échantillonnage et la simulation.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Vocabulaire et calcul de probabilités',
                'duree': 35,
                'contenu': """# Vocabulaire et calcul de probabilités

## Introduction

Les **probabilités** permettent de modéliser le hasard et de quantifier les chances qu'un événement se réalise. Elles interviennent dans de nombreux domaines : météorologie, médecine, jeux, assurances, etc.

---

## 1. Expérience aléatoire et univers

### Définitions

- Une **expérience aléatoire** est une expérience dont on ne peut pas prévoir le résultat avec certitude, mais dont on connaît l'ensemble des résultats possibles.
- L'**univers** $\\Omega$ (oméga) est l'ensemble de **tous** les résultats (ou issues) possibles.

**Exemples :**

| Expérience | Univers $\\Omega$ |
|------------|-------------------|
| Lancer un dé à 6 faces | $\\{1; 2; 3; 4; 5; 6\\}$ |
| Lancer une pièce | $\\{\\text{Pile}; \\text{Face}\\}$ |
| Tirer une carte d'un jeu de 32 | 32 issues possibles |

---

## 2. Événements

### Définition

Un **événement** est un sous-ensemble de l'univers $\\Omega$.

### Vocabulaire

| Terme | Signification |
|-------|---------------|
| Événement **élémentaire** | Contient une seule issue (singleton) |
| Événement **certain** | Contient toutes les issues ($\\Omega$) |
| Événement **impossible** | Ne contient aucune issue ($\\varnothing$) |
| Événement **contraire** de $A$ | $\\bar{A}$ : les issues qui ne sont pas dans $A$ |

**Exemple (dé à 6 faces) :**

- $A$ = « obtenir un nombre pair » = $\\{2; 4; 6\\}$
- $\\bar{A}$ = « obtenir un nombre impair » = $\\{1; 3; 5\\}$

### Opérations sur les événements

| Opération | Notation | Signification |
|-----------|----------|---------------|
| Intersection | $A \\cap B$ | $A$ **et** $B$ se réalisent |
| Réunion | $A \\cup B$ | $A$ **ou** $B$ (ou les deux) se réalise(nt) |
| Incompatibilité | $A \\cap B = \\varnothing$ | $A$ et $B$ ne peuvent pas arriver en même temps |

---

## 3. Probabilité d'un événement

### Axiomes fondamentaux

Une **probabilité** $P$ sur $\\Omega$ vérifie :

1. Pour tout événement $A$ : $0 \\leq P(A) \\leq 1$
2. $P(\\Omega) = 1$ (l'événement certain a une probabilité de 1)
3. $P(\\varnothing) = 0$ (l'événement impossible a une probabilité de 0)

### Probabilité du contraire

$$P(\\bar{A}) = 1 - P(A)$$

> Très utile lorsqu'il est plus facile de calculer la probabilité que $A$ **ne** se produise **pas**.

### Formule de la réunion

$$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$$

Si $A$ et $B$ sont **incompatibles** ($A \\cap B = \\varnothing$) :

$$P(A \\cup B) = P(A) + P(B)$$

---

## 4. Équiprobabilité

### Définition

On dit qu'il y a **équiprobabilité** lorsque toutes les issues de $\\Omega$ ont la **même probabilité**.

Si $\\Omega$ contient $n$ issues en équiprobabilité, chaque issue a une probabilité de $\\frac{1}{n}$.

### Formule fondamentale

$$P(A) = \\frac{\\text{nombre d'issues favorables à } A}{\\text{nombre total d'issues}} = \\frac{\\text{card}(A)}{\\text{card}(\\Omega)}$$

**Exemple :** On lance un dé équilibré. Quelle est la probabilité d'obtenir un multiple de 3 ?

$$A = \\{3; 6\\} \\quad \\Rightarrow \\quad P(A) = \\frac{2}{6} = \\frac{1}{3}$$

---

## 5. Loi de probabilité

### Définition

Une **loi de probabilité** associe à chaque issue $\\omega_i$ de $\\Omega$ une probabilité $p_i$ telle que :

$$\\sum_{i=1}^{n} p_i = 1$$

On la présente souvent sous forme de **tableau** :

| Issue $\\omega_i$ | $\\omega_1$ | $\\omega_2$ | $\\cdots$ | $\\omega_n$ |
|-------------------|-------------|-------------|-----------|-------------|
| Probabilité $p_i$ | $p_1$ | $p_2$ | $\\cdots$ | $p_n$ |

**Exemple :** Un dé truqué a la loi suivante :

| Face | 1 | 2 | 3 | 4 | 5 | 6 |
|------|---|---|---|---|---|---|
| $P$ | $0{,}1$ | $0{,}1$ | $0{,}2$ | $0{,}2$ | $0{,}2$ | $0{,}2$ |

Vérification : $0{,}1 + 0{,}1 + 0{,}2 + 0{,}2 + 0{,}2 + 0{,}2 = 1$ ✓

---

## 6. Arbre de probabilités

Pour des expériences à **plusieurs étapes**, on utilise un **arbre pondéré** :

- Chaque branche porte une probabilité.
- La probabilité d'un **chemin** est le **produit** des probabilités des branches empruntées.
- La probabilité d'un événement est la **somme** des probabilités des chemins qui y mènent.

**Exemple :** On lance une pièce, puis un dé si c'est Pile, ou on tire une carte si c'est Face.

> La somme des probabilités des branches issues d'un même nœud vaut **toujours** 1.

---

## 7. Exemples de calculs

### Exemple 1 — Tirage de boules

Une urne contient 4 boules rouges, 3 bleues et 2 vertes. On tire une boule au hasard.

- $P(\\text{Rouge}) = \\frac{4}{9}$
- $P(\\text{Bleue}) = \\frac{3}{9} = \\frac{1}{3}$
- $P(\\text{Rouge ou Bleue}) = \\frac{4}{9} + \\frac{3}{9} = \\frac{7}{9}$
- $P(\\text{pas Verte}) = 1 - \\frac{2}{9} = \\frac{7}{9}$

### Exemple 2 — Deux lancers de dé

On lance deux fois un dé. Quelle est la probabilité que la somme soit 7 ?

$\\Omega$ contient $6 \\times 6 = 36$ issues. Les couples dont la somme vaut 7 sont :

$(1;6), (2;5), (3;4), (4;3), (5;2), (6;1)$ → 6 issues favorables.

$$P(S = 7) = \\frac{6}{36} = \\frac{1}{6}$$

---

## À retenir

- L'**univers** $\\Omega$ est l'ensemble de toutes les issues possibles.
- Un **événement** est un sous-ensemble de $\\Omega$ ; son **contraire** vérifie $P(\\bar{A}) = 1 - P(A)$.
- **Équiprobabilité** : $P(A) = \\frac{\\text{card}(A)}{\\text{card}(\\Omega)}$.
- **Réunion** : $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$.
- Un **arbre pondéré** : on multiplie le long des branches, on additionne les chemins.
""",
                'quiz': {
                    'titre': 'Quiz — Vocabulaire et calcul de probabilités',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "L'univers Ω d'une expérience aléatoire est :",
                            'options': ["L'ensemble de toutes les issues possibles", "L'ensemble des événements certains", "Un seul résultat", "La probabilité maximale"],
                            'reponse_correcte': '0',
                            'explication': "L'univers Ω regroupe toutes les issues possibles de l'expérience aléatoire.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "P(A) + P(Ā) = ?",
                            'options': ["1", "0", "2", "P(A)"],
                            'reponse_correcte': '0',
                            'explication': "La somme des probabilités d'un événement et de son contraire vaut toujours 1.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "On lance un dé équilibré à 6 faces. Quelle est la probabilité d'obtenir 3 ?",
                            'options': ["1/6", "1/3", "3/6", "1"],
                            'reponse_correcte': '0',
                            'explication': "Il y a 6 issues équiprobables et une seule favorable : P = 1/6.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "La probabilité d'un événement impossible est :",
                            'options': ["0", "1", "1/2", "-1"],
                            'reponse_correcte': '0',
                            'explication': "Un événement impossible ne se réalise jamais, sa probabilité est 0.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La probabilité d'un événement certain est :",
                            'options': ["1", "0", "1/2", "Impossible à calculer"],
                            'reponse_correcte': '0',
                            'explication': "Un événement certain se réalise toujours, sa probabilité est 1.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "On lance une pièce équilibrée. Quel est l'univers ?",
                            'options': ["{Pile ; Face}", "{1 ; 2}", "{Pile}", "{Face ; Pile ; Tranche}"],
                            'reponse_correcte': '0',
                            'explication': "Une pièce équilibrée a deux issues : Pile et Face.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Si A et B sont deux événements incompatibles, alors P(A ∪ B) = ?",
                            'options': ["P(A) + P(B)", "P(A) × P(B)", "P(A) + P(B) − P(A ∩ B)", "P(A) − P(B)"],
                            'reponse_correcte': '0',
                            'explication': "Quand A et B sont incompatibles (A ∩ B = ∅), P(A ∪ B) = P(A) + P(B).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "On tire une carte au hasard dans un jeu de 32 cartes. L'univers a :",
                            'options': ["32 issues", "52 issues", "4 issues", "13 issues"],
                            'reponse_correcte': '0',
                            'explication': "Un jeu de 32 cartes contient 32 cartes, donc 32 issues possibles.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "On lance deux dés équilibrés à 6 faces. Combien d'issues possibles y a-t-il ?",
                            'options': ["36", "12", "6", "66"],
                            'reponse_correcte': '0',
                            'explication': "Chaque dé a 6 faces : 6 × 6 = 36 issues possibles.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "La formule P(A ∪ B) = P(A) + P(B) − P(A ∩ B) s'applique :",
                            'options': ["Toujours", "Uniquement si A et B sont incompatibles", "Uniquement si A et B sont certains", "Jamais"],
                            'reponse_correcte': '0',
                            'explication': "C'est la formule générale de la réunion, valable pour tous événements A et B.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "On lance un dé équilibré. P(obtenir un nombre pair) = ?",
                            'options': ["1/2", "1/3", "2/3", "1/6"],
                            'reponse_correcte': '0',
                            'explication': "Nombres pairs : {2, 4, 6}, soit 3 issues favorables sur 6. P = 3/6 = 1/2.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "P(A) = 0,3 ; P(B) = 0,5 ; P(A ∩ B) = 0,1. Alors P(A ∪ B) = ?",
                            'options': ["0,7", "0,8", "0,9", "0,15"],
                            'reponse_correcte': '0',
                            'explication': "P(A ∪ B) = P(A) + P(B) − P(A ∩ B) = 0,3 + 0,5 − 0,1 = 0,7.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "On lance un dé équilibré. P(obtenir au moins 3) = ?",
                            'options': ["4/6", "3/6", "2/6", "5/6"],
                            'reponse_correcte': '0',
                            'explication': "Issues ≥ 3 : {3, 4, 5, 6}, soit 4 issues favorables sur 6. P = 4/6 = 2/3.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "On tire une carte d'un jeu de 32. P(obtenir un roi) = ?",
                            'options': ["4/32", "1/32", "8/32", "2/32"],
                            'reponse_correcte': '0',
                            'explication': "Il y a 4 rois dans un jeu de 32 cartes : P = 4/32 = 1/8.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Si P(A) = 0, alors A est l'événement impossible.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "Un événement de probabilité nulle est l'événement impossible (dans le cadre fini étudié en Seconde).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "P(A ∪ B) = P(A) + P(B) est toujours vrai, même si A et B ne sont pas incompatibles.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Cette formule n'est valable que si A et B sont incompatibles. Sinon il faut soustraire P(A ∩ B).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Si P(A) = 0,4 et P(B) = 0,7, alors A et B peuvent être incompatibles.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Si A et B étaient incompatibles, P(A ∪ B) = 0,4 + 0,7 = 1,1 > 1, ce qui est impossible.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Un sac contient 3 boules rouges, 5 bleues et 2 vertes. On tire une boule au hasard. Quelle est P(rouge) ? Donner sous forme de fraction.",
                            'options': None,
                            'reponse_correcte': '3/10',
                            'tolerances': ["3/10", "0.3", "0,3"],
                            'explication': "Il y a 10 boules au total et 3 rouges : P(rouge) = 3/10.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "P(A) = 0,5 ; P(B) = 0,4 ; P(A ∩ B) = 0,2. Calculer P(A ∪ B).",
                            'options': None,
                            'reponse_correcte': '0,7',
                            'tolerances': ["0,7", "0.7", "7/10"],
                            'explication': "P(A ∪ B) = 0,5 + 0,4 − 0,2 = 0,7.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "On lance un dé équilibré. Quelle est la probabilité d'obtenir un nombre premier ? (Les nombres premiers entre 1 et 6 sont 2, 3 et 5.) Donner sous forme de fraction.",
                            'options': None,
                            'reponse_correcte': '1/2',
                            'tolerances': ["1/2", "3/6", "0.5", "0,5"],
                            'explication': "Nombres premiers entre 1 et 6 : {2, 3, 5}, soit 3 issues sur 6. P = 3/6 = 1/2.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Échantillonnage et simulation',
                'duree': 30,
                'contenu': """# Échantillonnage et simulation

## Introduction

L'**échantillonnage** consiste à prélever une partie (un **échantillon**) d'une population pour en déduire des informations sur l'ensemble. La **simulation** utilise l'informatique pour reproduire un grand nombre de fois une expérience aléatoire afin d'estimer des probabilités.

---

## 1. Échantillon et population

### Définitions

- La **population** est l'ensemble complet des individus étudiés.
- Un **échantillon de taille $n$** est un sous-ensemble de $n$ individus prélevés dans la population.

> **Remarque :** un échantillon doit être le plus **représentatif** possible de la population, ce qui suppose un prélèvement **aléatoire**.

### Caractère étudié

On observe un **caractère** (ou variable) sur l'échantillon :

- **Quantitatif** : une valeur numérique (taille, note, âge…)
- **Qualitatif** : une catégorie (couleur, oui/non…)

---

## 2. Fréquence observée et probabilité

### Fréquence

Si dans un échantillon de taille $n$, un événement $A$ se réalise $k$ fois, la **fréquence observée** est :

$$f = \\frac{k}{n}$$

### Loi des grands nombres (version intuitive)

Lorsque la taille $n$ de l'échantillon augmente, la fréquence observée $f$ **se rapproche** de la probabilité théorique $P(A)$.

$$f \\xrightarrow[n \\to +\\infty]{} P(A)$$

**Exemple :** On lance une pièce équilibrée 10 fois, puis 100 fois, puis 10 000 fois. La fréquence de « Pile » se rapproche de $0{,}5$.

| Nombre de lancers | 10 | 100 | 1 000 | 10 000 |
|-------------------|----|-----|-------|--------|
| Fréquence de Pile (exemple) | 0,40 | 0,47 | 0,503 | 0,4998 |

---

## 3. Fluctuation d'échantillonnage

### Observation

Si on prélève **plusieurs échantillons** de même taille $n$, les fréquences observées $f$ **varient** d'un échantillon à l'autre. C'est la **fluctuation d'échantillonnage**.

### Intervalle de fluctuation au seuil de 95 %

Pour une probabilité théorique $p$ et un échantillon de taille $n$ (avec $n \\geq 25$, $0{,}2 \\leq p \\leq 0{,}8$), la fréquence observée $f$ appartient « en général » à l'intervalle :

$$I = \\left[ p - \\frac{1}{\\sqrt{n}} \\;; \\; p + \\frac{1}{\\sqrt{n}} \\right]$$

au seuil de **95 %** (c'est-à-dire dans 95 % des échantillons en moyenne).

**Exemple :** On sait qu'un dé est équilibré ($p = \\frac{1}{6} \\approx 0{,}167$). Pour $n = 100$ lancers :

$$I = \\left[ 0{,}167 - \\frac{1}{\\sqrt{100}} \\;; \\; 0{,}167 + \\frac{1}{\\sqrt{100}} \\right] = [0{,}067 \\;; \\; 0{,}267]$$

Si la fréquence observée d'une face est **en dehors** de cet intervalle, on peut mettre en doute l'équilibre du dé.

---

## 4. Prise de décision

L'intervalle de fluctuation sert à **tester une hypothèse** :

1. On suppose que $p$ est la probabilité théorique (hypothèse).
2. On observe la fréquence $f$ sur un échantillon de taille $n$.
3. Si $f \\notin I$, on **rejette** l'hypothèse au seuil de 95 %.
4. Si $f \\in I$, on **ne rejette pas** l'hypothèse (mais on ne la prouve pas).

**Exemple :** Un fabricant affirme que 5 % de ses pièces sont défectueuses ($p = 0{,}05$). Sur un lot de 400 pièces, on en trouve 32 défectueuses, soit $f = \\frac{32}{400} = 0{,}08$.

$$I = \\left[ 0{,}05 - \\frac{1}{\\sqrt{400}} \\;; \\; 0{,}05 + \\frac{1}{\\sqrt{400}} \\right] = [0{,}00 \\;; \\; 0{,}10]$$

Comme $0{,}08 \\in I$, on ne rejette pas l'affirmation du fabricant.

---

## 5. Simulation avec Python

La simulation permet d'estimer une probabilité en reproduisant l'expérience un grand nombre de fois.

### Outils Python

```python
import random

# Lancer un dé
random.randint(1, 6)

# Tirage pile/face (0 = Pile, 1 = Face)
random.randint(0, 1)

# Choisir un élément dans une liste
random.choice(["rouge", "bleu", "vert"])
```

### Exemple : estimer $P(\\text{somme} = 7)$ avec deux dés

```python
import random

nb_simulations = 10000
compteur = 0

for _ in range(nb_simulations):
    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)
    if de1 + de2 == 7:
        compteur += 1

frequence = compteur / nb_simulations
print(f"Fréquence observée : {frequence}")
# Résultat attendu : environ 0.167 (≈ 1/6)
```

### Exemple : simuler la fluctuation d'échantillonnage

```python
import random

p = 0.5         # probabilité théorique (pièce équilibrée)
n = 100         # taille de l'échantillon
nb_echantillons = 50

for i in range(nb_echantillons):
    nb_piles = sum(random.randint(0, 1) for _ in range(n))
    f = nb_piles / n
    dans_intervalle = abs(f - p) <= 1 / n**0.5
    print(f"Échantillon {i+1} : f = {f:.2f} {'✓' if dans_intervalle else '✗'}")
```

---

## 6. Lien entre statistiques et probabilités

| Statistiques | Probabilités |
|--------------|-------------|
| Fréquence observée $f$ | Probabilité théorique $p$ |
| On **observe** des données | On **modélise** le hasard |
| Résultats dépendent de l'échantillon | Valeurs « exactes » du modèle |

La **loi des grands nombres** fait le pont : quand $n$ est grand, les statistiques rejoignent le modèle probabiliste.

---

## À retenir

- Un **échantillon** est un sous-ensemble de la population ; sa **fréquence** $f = \\frac{k}{n}$.
- **Loi des grands nombres** : $f \\to P(A)$ quand $n \\to +\\infty$.
- **Fluctuation** : plusieurs échantillons donnent des fréquences différentes.
- **Intervalle de fluctuation** (seuil 95 %) : $\\left[ p - \\frac{1}{\\sqrt{n}} ; p + \\frac{1}{\\sqrt{n}} \\right]$.
- On **rejette** l'hypothèse si $f \\notin I$ ; on **ne rejette pas** si $f \\in I$.
- La **simulation** en Python (`random`) permet d'estimer des probabilités expérimentalement.
""",
                'quiz': {
                    'titre': 'Quiz — Échantillonnage et simulation',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Un échantillon est :",
                            'options': ["Un sous-ensemble d'individus prélevés dans la population", "L'ensemble de la population", "Un résultat d'expérience", "Une probabilité théorique"],
                            'reponse_correcte': '0',
                            'explication': "Un échantillon est un sous-ensemble de la population, prélevé pour l'étudier.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "La fréquence observée f d'un événement ayant eu lieu k fois sur n tirages est :",
                            'options': ["f = k/n", "f = n/k", "f = k × n", "f = k + n"],
                            'reponse_correcte': '0',
                            'explication': "La fréquence observée est le rapport du nombre de réalisations sur le nombre total de tirages.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "La loi des grands nombres affirme que lorsque n augmente :",
                            'options': ["La fréquence observée se rapproche de la probabilité théorique", "La fréquence observée s'éloigne de la probabilité théorique", "La fréquence observée reste constante", "La probabilité théorique augmente"],
                            'reponse_correcte': '0',
                            'explication': "La loi des grands nombres dit que f → P(A) quand n → +∞.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "En Python, random.randint(1, 6) simule :",
                            'options': ["Un lancer de dé à 6 faces", "Un tirage pile/face", "Un nombre décimal entre 1 et 6", "Un lancer de deux dés"],
                            'reponse_correcte': '0',
                            'explication': "random.randint(1, 6) renvoie un entier aléatoire entre 1 et 6 inclus.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "La fluctuation d'échantillonnage désigne :",
                            'options': ["La variation des fréquences entre différents échantillons", "La probabilité exacte d'un événement", "Le nombre d'échantillons possibles", "La taille de la population"],
                            'reponse_correcte': '0',
                            'explication': "Plusieurs échantillons de même taille donnent des fréquences différentes : c'est la fluctuation.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "On rejette l'hypothèse au seuil de 95 % quand la fréquence observée est :",
                            'options': ["En dehors de l'intervalle de fluctuation", "Dans l'intervalle de fluctuation", "Égale à p", "Supérieure à 0,95"],
                            'reponse_correcte': '0',
                            'explication': "Si f ∉ I, on rejette l'hypothèse au seuil de 95 %.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "En Python, random.choice(['a', 'b', 'c']) renvoie :",
                            'options': ["Un élément choisi au hasard dans la liste", "Toujours le premier élément", "La longueur de la liste", "Un nombre aléatoire"],
                            'reponse_correcte': '0',
                            'explication': "random.choice sélectionne aléatoirement un élément de la liste.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "Pour n = 100 et p = 0,5, l'intervalle de fluctuation au seuil 95 % est :",
                            'options': ["[0,4 ; 0,6]", "[0,45 ; 0,55]", "[0,0 ; 1,0]", "[0,5 ; 0,5]"],
                            'reponse_correcte': '0',
                            'explication': "I = [p − 1/√n ; p + 1/√n] = [0,5 − 0,1 ; 0,5 + 0,1] = [0,4 ; 0,6].",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "Pour n = 400 et p = 0,3, l'intervalle de fluctuation au seuil 95 % est :",
                            'options': ["[0,25 ; 0,35]", "[0,20 ; 0,40]", "[0,28 ; 0,32]", "[0,30 ; 0,30]"],
                            'reponse_correcte': '0',
                            'explication': "I = [0,3 − 1/√400 ; 0,3 + 1/√400] = [0,3 − 0,05 ; 0,3 + 0,05] = [0,25 ; 0,35].",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "Sur 200 lancers d'une pièce, on obtient 120 fois pile. La fréquence observée est :",
                            'options': ["0,60", "0,50", "0,40", "1,20"],
                            'reponse_correcte': '0',
                            'explication': "f = 120/200 = 0,60.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "n = 25, p = 0,5. L'intervalle de fluctuation est [0,3 ; 0,7]. Une fréquence observée de 0,28 est :",
                            'options': ["En dehors de l'intervalle", "Dans l'intervalle", "Au centre de l'intervalle", "Égale à p"],
                            'reponse_correcte': '0',
                            'explication': "0,28 < 0,3, donc la fréquence est en dehors de l'intervalle.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "En Python, sum(random.randint(0,1) for _ in range(100)) compte :",
                            'options': ["Le nombre de 1 obtenus sur 100 tirages", "La somme de 100 nombres entre 0 et 100", "Le nombre de 0 obtenus", "Un seul tirage aléatoire"],
                            'reponse_correcte': '0',
                            'explication': "Chaque tirage vaut 0 ou 1. La somme donne le nombre total de 1 obtenus.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "Si p = 0,2 et n = 100, l'intervalle de fluctuation au seuil 95 % est :",
                            'options': ["[0,1 ; 0,3]", "[0,15 ; 0,25]", "[0,0 ; 0,4]", "[0,2 ; 0,2]"],
                            'reponse_correcte': '0',
                            'explication': "I = [0,2 − 1/√100 ; 0,2 + 1/√100] = [0,2 − 0,1 ; 0,2 + 0,1] = [0,1 ; 0,3].",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "On observe f = 0,42 avec n = 100 et p = 0,5. L'intervalle est [0,4 ; 0,6]. On :",
                            'options': ["Ne rejette pas l'hypothèse", "Rejette l'hypothèse", "Ne peut rien conclure", "Accepte l'hypothèse avec certitude"],
                            'reponse_correcte': '0',
                            'explication': "0,42 ∈ [0,4 ; 0,6], donc on ne rejette pas l'hypothèse.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Un grand échantillon donne toujours une fréquence exactement égale à la probabilité théorique.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "La fréquence se rapproche de p mais ne l'atteint pas forcément exactement.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "L'intervalle de fluctuation au seuil de 95 % est centré sur p.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "L'intervalle [p − 1/√n ; p + 1/√n] est symétrique par rapport à p.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Si la fréquence observée est dans l'intervalle de fluctuation, on a prouvé que l'hypothèse est vraie.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "On ne rejette pas l'hypothèse, mais on ne la prouve pas pour autant.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Pour n = 400 et p = 0,5, calculer la borne supérieure de l'intervalle de fluctuation au seuil 95 %.",
                            'options': None,
                            'reponse_correcte': '0,55',
                            'tolerances': ["0,55", "0.55"],
                            'explication': "Borne sup = p + 1/√n = 0,5 + 1/20 = 0,5 + 0,05 = 0,55.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "Sur 500 lancers d'un dé, on obtient 280 fois un nombre pair. Calculer la fréquence observée.",
                            'options': None,
                            'reponse_correcte': '0,56',
                            'tolerances': ["0,56", "0.56", "28/50", "14/25"],
                            'explication': "f = 280/500 = 0,56.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "n = 100, p = 0,3. L'intervalle de fluctuation est [0,2 ; 0,4]. On observe f = 0,15. Rejette-t-on l'hypothèse ? Répondre par oui ou non.",
                            'options': None,
                            'reponse_correcte': 'oui',
                            'tolerances': ["oui", "Oui", "OUI"],
                            'explication': "0,15 ∉ [0,2 ; 0,4], on rejette l'hypothèse au seuil de 95 %.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
        ],
    },
    # ──────────────────────────────────────────────
    # CHAPITRE 12 — Trigonométrie
    # ──────────────────────────────────────────────
    {
        'ordre': 12,
        'titre': 'Trigonométrie',
        'description': "Cosinus et sinus dans le triangle rectangle, cercle trigonométrique, angles orientés et formules fondamentales.",
        'score_minimum': 60.0,
        'lecons': [
            {
                'ordre': 1,
                'titre': 'Trigonométrie dans le triangle rectangle',
                'duree': 30,
                'contenu': """# Trigonométrie dans le triangle rectangle

## Introduction

La **trigonométrie** (du grec *trigonon* = triangle et *metron* = mesure) étudie les relations entre les angles et les côtés d'un triangle. En classe de Seconde, on commence par le **triangle rectangle**, qui est la base de toute la trigonométrie.

---

## 1. Rappel : le théorème de Pythagore

Dans un triangle $ABC$ **rectangle en $C$** :

$$AB^2 = AC^2 + BC^2$$

où $AB$ est l'**hypoténuse** (le plus grand côté, opposé à l'angle droit).

**Exemple :** Si $AC = 3$ et $BC = 4$, alors $AB = \\sqrt{9 + 16} = \\sqrt{25} = 5$.

---

## 2. Cosinus, sinus et tangente

### Définitions

Dans un triangle $ABC$ rectangle en $C$, pour l'angle $\\widehat{A}$ :

$$\\cos(\\widehat{A}) = \\frac{\\text{côté adjacent à } \\widehat{A}}{\\text{hypoténuse}} = \\frac{AC}{AB}$$

$$\\sin(\\widehat{A}) = \\frac{\\text{côté opposé à } \\widehat{A}}{\\text{hypoténuse}} = \\frac{BC}{AB}$$

$$\\tan(\\widehat{A}) = \\frac{\\text{côté opposé à } \\widehat{A}}{\\text{côté adjacent à } \\widehat{A}} = \\frac{BC}{AC} = \\frac{\\sin(\\widehat{A})}{\\cos(\\widehat{A})}$$

> **Moyen mnémotechnique :** **SOH-CAH-TOA**
> - **S**in = **O**pposé / **H**ypoténuse
> - **C**os = **A**djacent / **H**ypoténuse
> - **T**an = **O**pposé / **A**djacent

### Domaine de valeurs

Pour un angle aigu $\\widehat{A}$ (entre $0°$ et $90°$) :

$$0 < \\cos(\\widehat{A}) < 1 \\qquad 0 < \\sin(\\widehat{A}) < 1 \\qquad \\tan(\\widehat{A}) > 0$$

---

## 3. L'identité fondamentale

Pour tout angle $\\alpha$ :

$$\\cos^2(\\alpha) + \\sin^2(\\alpha) = 1$$

**Démonstration (dans le triangle rectangle en $C$) :**

$$\\cos^2(\\widehat{A}) + \\sin^2(\\widehat{A}) = \\frac{AC^2}{AB^2} + \\frac{BC^2}{AB^2} = \\frac{AC^2 + BC^2}{AB^2} = \\frac{AB^2}{AB^2} = 1$$

par le théorème de Pythagore.

---

## 4. Valeurs remarquables

| Angle $\\alpha$ | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ |
|-----------------|------|-------|-------|-------|-------|
| $\\cos(\\alpha)$ | $1$ | $\\frac{\\sqrt{3}}{2}$ | $\\frac{\\sqrt{2}}{2}$ | $\\frac{1}{2}$ | $0$ |
| $\\sin(\\alpha)$ | $0$ | $\\frac{1}{2}$ | $\\frac{\\sqrt{2}}{2}$ | $\\frac{\\sqrt{3}}{2}$ | $1$ |
| $\\tan(\\alpha)$ | $0$ | $\\frac{\\sqrt{3}}{3}$ | $1$ | $\\sqrt{3}$ | — |

> Il est **indispensable** de connaître ces valeurs par cœur.

**Vérification :** $\\cos^2(30°) + \\sin^2(30°) = \\frac{3}{4} + \\frac{1}{4} = 1$ ✓

---

## 5. Calculer un côté

**Méthode :** on identifie l'angle connu, le côté recherché et le côté connu, puis on choisit la bonne formule (cos, sin ou tan).

**Exemple 1 :** Triangle rectangle avec $\\widehat{A} = 35°$ et $AB = 10$ cm. Calculer $AC$.

$$\\cos(35°) = \\frac{AC}{AB} \\implies AC = AB \\times \\cos(35°) = 10 \\times \\cos(35°) \\approx 8{,}19 \\text{ cm}$$

**Exemple 2 :** Même triangle. Calculer $BC$.

$$\\sin(35°) = \\frac{BC}{AB} \\implies BC = 10 \\times \\sin(35°) \\approx 5{,}74 \\text{ cm}$$

---

## 6. Calculer un angle

Si on connaît les longueurs des côtés, on utilise les **fonctions réciproques** :

$$\\alpha = \\arccos\\left(\\frac{\\text{adjacent}}{\\text{hypoténuse}}\\right)$$

$$\\alpha = \\arcsin\\left(\\frac{\\text{opposé}}{\\text{hypoténuse}}\\right)$$

$$\\alpha = \\arctan\\left(\\frac{\\text{opposé}}{\\text{adjacent}}\\right)$$

**Exemple :** Dans un triangle rectangle, le côté opposé mesure 7 cm et le côté adjacent mesure 10 cm.

$$\\alpha = \\arctan\\left(\\frac{7}{10}\\right) \\approx 34{,}99° \\approx 35°$$

> Sur la calculatrice, les touches sont notées $\\cos^{-1}$, $\\sin^{-1}$, $\\tan^{-1}$.

---

## 7. Applications concrètes

### Hauteur d'un bâtiment

Un observateur situé à 50 m d'un bâtiment voit son sommet sous un angle d'élévation de $28°$.

$$\\tan(28°) = \\frac{h}{50} \\implies h = 50 \\times \\tan(28°) \\approx 26{,}6 \\text{ m}$$

### Pente d'une route

Une route s'élève de 8 m sur une distance horizontale de 100 m.

$$\\tan(\\alpha) = \\frac{8}{100} = 0{,}08 \\implies \\alpha = \\arctan(0{,}08) \\approx 4{,}6°$$

On dit que la pente est de **8 %**.

---

## À retenir

- $\\cos = \\frac{\\text{adjacent}}{\\text{hypoténuse}}$ ; $\\sin = \\frac{\\text{opposé}}{\\text{hypoténuse}}$ ; $\\tan = \\frac{\\text{opposé}}{\\text{adjacent}}$.
- **Identité fondamentale** : $\\cos^2 \\alpha + \\sin^2 \\alpha = 1$.
- Connaître les **valeurs remarquables** pour $0°$, $30°$, $45°$, $60°$, $90°$.
- Pour trouver un côté : identifier l'angle et les côtés, appliquer cos/sin/tan.
- Pour trouver un angle : utiliser $\\arccos$, $\\arcsin$ ou $\\arctan$.
""",
                'quiz': {
                    'titre': 'Quiz — Trigonométrie dans le triangle rectangle',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Dans un triangle rectangle, cos(A) est égal à :",
                            'options': ["Côté adjacent / Hypoténuse", "Côté opposé / Hypoténuse", "Côté opposé / Côté adjacent", "Hypoténuse / Côté adjacent"],
                            'reponse_correcte': '0',
                            'explication': "cos(A) = côté adjacent à A / hypoténuse (CAH dans SOH-CAH-TOA).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "sin(A) dans un triangle rectangle est égal à :",
                            'options': ["Côté opposé / Hypoténuse", "Côté adjacent / Hypoténuse", "Hypoténuse / Côté opposé", "Côté adjacent / Côté opposé"],
                            'reponse_correcte': '0',
                            'explication': "sin(A) = côté opposé à A / hypoténuse (SOH dans SOH-CAH-TOA).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "tan(A) dans un triangle rectangle est égal à :",
                            'options': ["Côté opposé / Côté adjacent", "Côté adjacent / Côté opposé", "Côté opposé / Hypoténuse", "Hypoténuse / Côté opposé"],
                            'reponse_correcte': '0',
                            'explication': "tan(A) = côté opposé / côté adjacent (TOA dans SOH-CAH-TOA).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "Dans un triangle rectangle, le plus grand côté est :",
                            'options': ["L'hypoténuse", "Le côté opposé à l'angle aigu", "Le côté adjacent à l'angle aigu", "Cela dépend du triangle"],
                            'reponse_correcte': '0',
                            'explication': "L'hypoténuse est le côté opposé à l'angle droit et c'est toujours le plus grand côté.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "cos²(A) + sin²(A) = ?",
                            'options': ["1", "0", "2", "cos(2A)"],
                            'reponse_correcte': '0',
                            'explication': "C'est l'identité fondamentale de la trigonométrie : cos² + sin² = 1.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "Le moyen mnémotechnique SOH-CAH-TOA signifie :",
                            'options': ["Sin=Opposé/Hyp, Cos=Adjacent/Hyp, Tan=Opposé/Adjacent", "Sin=Adjacent/Hyp, Cos=Opposé/Hyp, Tan=Adjacent/Opposé", "Sin=Hyp/Opposé, Cos=Hyp/Adjacent, Tan=Adjacent/Opposé", "Aucune de ces réponses"],
                            'reponse_correcte': '0',
                            'explication': "SOH : Sin = Opposé/Hypoténuse ; CAH : Cos = Adjacent/Hypoténuse ; TOA : Tan = Opposé/Adjacent.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "Triangle rectangle de côtés 3 et 4 (côtés de l'angle droit). L'hypoténuse vaut :",
                            'options': ["5", "7", "12", "25"],
                            'reponse_correcte': '0',
                            'explication': "c = √(3² + 4²) = √(9 + 16) = √25 = 5.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "tan(45°) = ?",
                            'options': ["1", "0", "√2/2", "√2"],
                            'reponse_correcte': '0',
                            'explication': "tan(45°) = sin(45°)/cos(45°) = (√2/2)/(√2/2) = 1.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "cos(60°) = ?",
                            'options': ["1/2", "√3/2", "√2/2", "0"],
                            'reponse_correcte': '0',
                            'explication': "Valeur remarquable : cos(60°) = 1/2.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "sin(30°) = ?",
                            'options': ["1/2", "√3/2", "√2/2", "1"],
                            'reponse_correcte': '0',
                            'explication': "Valeur remarquable : sin(30°) = 1/2.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "Triangle ABC rectangle en C avec AC = 4 et AB = 5. Alors BC = ?",
                            'options': ["3", "4", "√41", "1"],
                            'reponse_correcte': '0',
                            'explication': "BC = √(AB² − AC²) = √(25 − 16) = √9 = 3.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "Si sin(A) = 0,6 (A angle aigu), alors cos(A) = ?",
                            'options': ["0,8", "0,4", "0,36", "0,6"],
                            'reponse_correcte': '0',
                            'explication': "cos²(A) = 1 − sin²(A) = 1 − 0,36 = 0,64. Donc cos(A) = 0,8.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "tan(A) = 3/4 et le côté adjacent mesure 8. Le côté opposé mesure :",
                            'options': ["6", "8", "4", "12"],
                            'reponse_correcte': '0',
                            'explication': "Opposé = adjacent × tan(A) = 8 × 3/4 = 6.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "cos(45°) = ?",
                            'options': ["√2/2", "1/2", "√3/2", "1"],
                            'reponse_correcte': '0',
                            'explication': "Valeur remarquable : cos(45°) = √2/2 ≈ 0,707.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "Le sinus d'un angle dans un triangle rectangle peut être supérieur à 1.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "sin(A) = opposé/hypoténuse ≤ 1 car l'hypoténuse est le plus grand côté.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "tan(A) = sin(A) / cos(A).",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est la relation fondamentale : tangente = sinus / cosinus.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "Si sin(A) = cos(A) dans un triangle rectangle, alors A = 45°.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "sin(A) = cos(A) ⇔ tan(A) = 1 ⇔ A = 45° (pour un angle aigu).",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Triangle ABC rectangle en C avec AC = 5 et BC = 12. Calculer AB.",
                            'options': None,
                            'reponse_correcte': '13',
                            'tolerances': ["13"],
                            'explication': "AB = √(AC² + BC²) = √(25 + 144) = √169 = 13.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "cos(A) = 4/5 (A angle aigu). Calculer sin(A). Donner sous forme de fraction.",
                            'options': None,
                            'reponse_correcte': '3/5',
                            'tolerances': ["3/5", "0.6", "0,6"],
                            'explication': "sin²(A) = 1 − cos²(A) = 1 − 16/25 = 9/25. Donc sin(A) = 3/5.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Triangle rectangle en C, AB = 10 et angle A = 30°. Calculer BC.",
                            'options': None,
                            'reponse_correcte': '5',
                            'tolerances': ["5"],
                            'explication': "BC = AB × sin(30°) = 10 × 1/2 = 5.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                    ],
                },
            },
            {
                'ordre': 2,
                'titre': 'Le cercle trigonométrique',
                'duree': 35,
                'contenu': """# Le cercle trigonométrique

## Introduction

Le **cercle trigonométrique** permet d'étendre les notions de cosinus et sinus à **tous les angles**, et pas seulement aux angles aigus d'un triangle rectangle. C'est un outil fondamental pour la suite du lycée.

---

## 1. Définition du cercle trigonométrique

Le **cercle trigonométrique** est le cercle :

- de **centre** $O$ (l'origine du repère),
- de **rayon** $1$,
- muni d'un **sens positif** (le sens inverse des aiguilles d'une montre, dit **sens trigonométrique** ou **sens direct**).

Dans le repère orthonormé $(O; \\vec{i}, \\vec{j})$, un point $M$ du cercle est repéré par un angle $\\theta$ mesuré depuis le point $I(1; 0)$.

---

## 2. Mesure en radians

### Définition

Le **radian** est l'unité de mesure d'angle définie par :

$$1 \\text{ rad} = \\text{l'angle qui intercepte un arc de longueur } 1 \\text{ sur un cercle de rayon } 1$$

### Conversion degrés ↔ radians

$$\\pi \\text{ rad} = 180°$$

| Degrés | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $120°$ | $180°$ | $270°$ | $360°$ |
|--------|------|-------|-------|-------|-------|--------|--------|--------|--------|
| Radians | $0$ | $\\frac{\\pi}{6}$ | $\\frac{\\pi}{4}$ | $\\frac{\\pi}{3}$ | $\\frac{\\pi}{2}$ | $\\frac{2\\pi}{3}$ | $\\pi$ | $\\frac{3\\pi}{2}$ | $2\\pi$ |

**Formules de conversion :**

$$\\text{radians} = \\text{degrés} \\times \\frac{\\pi}{180} \\qquad \\text{degrés} = \\text{radians} \\times \\frac{180}{\\pi}$$

---

## 3. Cosinus et sinus sur le cercle

### Définition

Soit $M$ le point du cercle trigonométrique associé à l'angle $\\theta$. Les coordonnées de $M$ sont :

$$M(\\cos\\theta \\;; \\sin\\theta)$$

Autrement dit :

- $\\cos\\theta$ est l'**abscisse** du point $M$,
- $\\sin\\theta$ est l'**ordonnée** du point $M$.

### Conséquences immédiates

- $-1 \\leq \\cos\\theta \\leq 1$ et $-1 \\leq \\sin\\theta \\leq 1$ (le point est sur un cercle de rayon 1).
- $\\cos^2\\theta + \\sin^2\\theta = 1$ (équation du cercle $x^2 + y^2 = 1$).

---

## 4. Valeurs remarquables sur le cercle

| $\\theta$ | $0$ | $\\frac{\\pi}{6}$ | $\\frac{\\pi}{4}$ | $\\frac{\\pi}{3}$ | $\\frac{\\pi}{2}$ | $\\pi$ | $\\frac{3\\pi}{2}$ | $2\\pi$ |
|-----------|-----|------|------|------|------|------|------|------|
| $\\cos\\theta$ | $1$ | $\\frac{\\sqrt{3}}{2}$ | $\\frac{\\sqrt{2}}{2}$ | $\\frac{1}{2}$ | $0$ | $-1$ | $0$ | $1$ |
| $\\sin\\theta$ | $0$ | $\\frac{1}{2}$ | $\\frac{\\sqrt{2}}{2}$ | $\\frac{\\sqrt{3}}{2}$ | $1$ | $0$ | $-1$ | $0$ |

**Points remarquables sur le cercle :**

| Point | Coordonnées | Angle |
|-------|-------------|-------|
| $I$ | $(1; 0)$ | $0$ |
| $J$ | $(0; 1)$ | $\\frac{\\pi}{2}$ |
| $I'$ | $(-1; 0)$ | $\\pi$ |
| $J'$ | $(0; -1)$ | $\\frac{3\\pi}{2}$ |

---

## 5. Propriétés de symétrie

Les symétries du cercle donnent des relations importantes entre cos et sin :

### Angles opposés (symétrie par rapport à l'axe des abscisses)

$$\\cos(-\\theta) = \\cos\\theta \\qquad \\sin(-\\theta) = -\\sin\\theta$$

> Le cosinus est une fonction **paire**, le sinus une fonction **impaire**.

### Angles supplémentaires (symétrie par rapport à l'axe des ordonnées)

$$\\cos(\\pi - \\theta) = -\\cos\\theta \\qquad \\sin(\\pi - \\theta) = \\sin\\theta$$

### Angles complémentaires

$$\\cos\\left(\\frac{\\pi}{2} - \\theta\\right) = \\sin\\theta \\qquad \\sin\\left(\\frac{\\pi}{2} - \\theta\\right) = \\cos\\theta$$

### Décalage de $\\pi$ (symétrie centrale par rapport à $O$)

$$\\cos(\\theta + \\pi) = -\\cos\\theta \\qquad \\sin(\\theta + \\pi) = -\\sin\\theta$$

---

## 6. Résoudre des équations trigonométriques

### Équation $\\cos\\theta = a$ (avec $-1 \\leq a \\leq 1$)

Les solutions sont :

$$\\theta = \\alpha + 2k\\pi \\quad \\text{ou} \\quad \\theta = -\\alpha + 2k\\pi \\qquad (k \\in \\mathbb{Z})$$

où $\\alpha$ est un angle tel que $\\cos\\alpha = a$.

**Exemple :** $\\cos\\theta = \\frac{1}{2}$

$\\alpha = \\frac{\\pi}{3}$, donc $\\theta = \\frac{\\pi}{3} + 2k\\pi$ ou $\\theta = -\\frac{\\pi}{3} + 2k\\pi$.

### Équation $\\sin\\theta = a$ (avec $-1 \\leq a \\leq 1$)

Les solutions sont :

$$\\theta = \\alpha + 2k\\pi \\quad \\text{ou} \\quad \\theta = \\pi - \\alpha + 2k\\pi \\qquad (k \\in \\mathbb{Z})$$

où $\\alpha$ est un angle tel que $\\sin\\alpha = a$.

**Exemple :** $\\sin\\theta = \\frac{\\sqrt{2}}{2}$

$\\alpha = \\frac{\\pi}{4}$, donc $\\theta = \\frac{\\pi}{4} + 2k\\pi$ ou $\\theta = \\frac{3\\pi}{4} + 2k\\pi$.

---

## 7. Signe du cosinus et du sinus selon le quadrant

Le plan est divisé en **quatre quadrants** :

| Quadrant | Angle $\\theta$ | $\\cos\\theta$ | $\\sin\\theta$ |
|----------|-----------------|----------------|----------------|
| I | $0 < \\theta < \\frac{\\pi}{2}$ | $+$ | $+$ |
| II | $\\frac{\\pi}{2} < \\theta < \\pi$ | $-$ | $+$ |
| III | $\\pi < \\theta < \\frac{3\\pi}{2}$ | $-$ | $-$ |
| IV | $\\frac{3\\pi}{2} < \\theta < 2\\pi$ | $+$ | $-$ |

> Retenir : « **Tout** le monde **S**ait **T**rès bien **C**hanter » → Quadrants I (Tout +), II (Sin +), III (Tan +), IV (Cos +).

---

## 8. Longueur d'un arc de cercle

Sur un cercle de rayon $r$, la longueur d'un arc intercepté par un angle $\\theta$ (en radians) est :

$$\\ell = r \\times \\theta$$

**Exemple :** Sur un cercle de rayon $r = 5$ cm, un angle de $\\frac{\\pi}{3}$ rad intercepte un arc de longueur :

$$\\ell = 5 \\times \\frac{\\pi}{3} = \\frac{5\\pi}{3} \\approx 5{,}24 \\text{ cm}$$

---

## À retenir

- Le **cercle trigonométrique** a pour centre $O$, rayon $1$, orienté dans le sens direct.
- $M(\\cos\\theta; \\sin\\theta)$ : l'abscisse est le cosinus, l'ordonnée est le sinus.
- **Radian** : $\\pi$ rad $= 180°$.
- **Identité** : $\\cos^2\\theta + \\sin^2\\theta = 1$.
- **Parité** : $\\cos(-\\theta) = \\cos\\theta$ ; $\\sin(-\\theta) = -\\sin\\theta$.
- **Supplémentaires** : $\\cos(\\pi - \\theta) = -\\cos\\theta$ ; $\\sin(\\pi - \\theta) = \\sin\\theta$.
- Connaître les valeurs remarquables et le signe par quadrant.
""",
                'quiz': {
                    'titre': 'Quiz — Le cercle trigonométrique',
                    'questions': [
                        {
                            'ordre': 1,
                            'type': 'qcm',
                            'texte': "Le rayon du cercle trigonométrique est :",
                            'options': ["1", "2", "π", "0"],
                            'reponse_correcte': '0',
                            'explication': "Le cercle trigonométrique est le cercle de centre O et de rayon 1.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 2,
                            'type': 'qcm',
                            'texte': "π radians correspond à :",
                            'options': ["180°", "90°", "360°", "60°"],
                            'reponse_correcte': '0',
                            'explication': "Par définition, π rad = 180° (un demi-tour).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 3,
                            'type': 'qcm',
                            'texte': "cos(0) = ?",
                            'options': ["1", "0", "-1", "π"],
                            'reponse_correcte': '0',
                            'explication': "Le point associé à l'angle 0 est (1 ; 0), donc cos(0) = 1.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 4,
                            'type': 'qcm',
                            'texte': "sin(π/2) = ?",
                            'options': ["1", "0", "-1", "1/2"],
                            'reponse_correcte': '0',
                            'explication': "Le point associé à π/2 est (0 ; 1), donc sin(π/2) = 1.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 5,
                            'type': 'qcm',
                            'texte': "cos(π) = ?",
                            'options': ["-1", "1", "0", "π"],
                            'reponse_correcte': '0',
                            'explication': "Le point associé à π est (−1 ; 0), donc cos(π) = −1.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 6,
                            'type': 'qcm',
                            'texte': "sin(0) = ?",
                            'options': ["0", "1", "-1", "π"],
                            'reponse_correcte': '0',
                            'explication': "Le point associé à l'angle 0 est (1 ; 0), donc sin(0) = 0.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 7,
                            'type': 'qcm',
                            'texte': "90° en radians vaut :",
                            'options': ["π/2", "π", "2π", "π/4"],
                            'reponse_correcte': '0',
                            'explication': "90° = 90 × π/180 = π/2.",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 8,
                            'type': 'qcm',
                            'texte': "cos(−θ) = ?",
                            'options': ["cos(θ)", "−cos(θ)", "sin(θ)", "−sin(θ)"],
                            'reponse_correcte': '0',
                            'explication': "Le cosinus est une fonction paire : cos(−θ) = cos(θ).",
                            'difficulte': 'facile',
                            'points': 1,
                        },
                        {
                            'ordre': 9,
                            'type': 'qcm',
                            'texte': "cos(π/3) = ?",
                            'options': ["1/2", "√3/2", "√2/2", "-1/2"],
                            'reponse_correcte': '0',
                            'explication': "Valeur remarquable : cos(π/3) = cos(60°) = 1/2.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 10,
                            'type': 'qcm',
                            'texte': "sin(π/6) = ?",
                            'options': ["1/2", "√3/2", "√2/2", "0"],
                            'reponse_correcte': '0',
                            'explication': "Valeur remarquable : sin(π/6) = sin(30°) = 1/2.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 11,
                            'type': 'qcm',
                            'texte': "cos(π/4) = ?",
                            'options': ["√2/2", "1/2", "√3/2", "1"],
                            'reponse_correcte': '0',
                            'explication': "Valeur remarquable : cos(π/4) = cos(45°) = √2/2.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 12,
                            'type': 'qcm',
                            'texte': "sin(π − θ) = ?",
                            'options': ["sin(θ)", "−sin(θ)", "cos(θ)", "−cos(θ)"],
                            'reponse_correcte': '0',
                            'explication': "Formule des angles supplémentaires : sin(π − θ) = sin(θ).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 13,
                            'type': 'qcm',
                            'texte': "60° en radians vaut :",
                            'options': ["π/3", "π/6", "π/4", "2π/3"],
                            'reponse_correcte': '0',
                            'explication': "60° = 60 × π/180 = π/3.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 14,
                            'type': 'qcm',
                            'texte': "sin(π) = ?",
                            'options': ["0", "1", "-1", "π"],
                            'reponse_correcte': '0',
                            'explication': "Le point associé à π est (−1 ; 0), donc sin(π) = 0.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 15,
                            'type': 'vrai_faux',
                            'texte': "cos²(θ) + sin²(θ) = 1 pour tout angle θ.",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "C'est l'identité fondamentale, valable pour tout angle.",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 16,
                            'type': 'vrai_faux',
                            'texte': "sin(−θ) = sin(θ).",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'faux',
                            'explication': "Le sinus est une fonction impaire : sin(−θ) = −sin(θ), pas sin(θ).",
                            'difficulte': 'moyen',
                            'points': 1,
                        },
                        {
                            'ordre': 17,
                            'type': 'vrai_faux',
                            'texte': "cos(π + θ) = −cos(θ) et sin(π + θ) = −sin(θ).",
                            'options': ["Vrai", "Faux"],
                            'reponse_correcte': 'vrai',
                            'explication': "La symétrie centrale par rapport à O donne cos(π + θ) = −cos(θ) et sin(π + θ) = −sin(θ).",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 18,
                            'type': 'texte_libre',
                            'texte': "Convertir 120° en radians. Donner la réponse sous forme simplifiée avec π.",
                            'options': None,
                            'reponse_correcte': '2π/3',
                            'tolerances': ["2π/3", "2pi/3", "2*pi/3"],
                            'explication': "120° = 120 × π/180 = 2π/3.",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 19,
                            'type': 'texte_libre',
                            'texte': "cos(θ) = −1/2 et 0 ≤ θ ≤ π. Quelle est la valeur de θ ? Répondre avec π.",
                            'options': None,
                            'reponse_correcte': '2π/3',
                            'tolerances': ["2π/3", "2pi/3", "2*pi/3", "120°", "120"],
                            'explication': "cos(θ) = −1/2 et θ ∈ [0 ; π] → θ = 2π/3 (= 120°).",
                            'difficulte': 'difficile',
                            'points': 2,
                        },
                        {
                            'ordre': 20,
                            'type': 'texte_libre',
                            'texte': "Calculer la longueur d'un arc de cercle de rayon 3 cm intercepté par un angle de π/4 radians. Donner le résultat exact avec π.",
                            'options': None,
                            'reponse_correcte': '3π/4',
                            'tolerances': ["3π/4", "3pi/4", "3*pi/4"],
                            'explication': "ℓ = r × θ = 3 × π/4 = 3π/4 cm.",
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
    help = "Seed Mathématiques Seconde — 12 chapitres, leçons (sans quiz)."

    def handle(self, *args, **options):
        matiere, created = Matiere.objects.get_or_create(
            nom='mathematiques',
            defaults={
                'description': "Les mathématiques au lycée : algèbre, analyse, géométrie, probabilités et algorithmique.",
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
            f"\n✅ Mathématiques Seconde — {len(CHAPITRES)} chapitres, {total_lecons} leçons, {total_quizzes} quiz traités."
        ))
