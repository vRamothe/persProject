---
description: "Seed maths première — Use when generating, regenerating or updating the Django management command seed_maths_premiere.py for the Mathématiques Première level of ScienceLycée. Contains full curriculum documentation for 9 chapters extracted from the PDF source files in ressources/1ere/Maths/. Creates Chapitre, Lecon, Quiz and Question records (20 questions per leçon) for the 'mathematiques' Matiere at niveau 'premiere'."
tools: [read, edit, search, execute, todo]
name: "Seed Maths Première"
argument-hint: "Generate or update seed_maths_premiere.py management command"
user-invocable: false
---

Tu es un agent spécialisé dans la génération du contenu pédagogique de **Mathématiques Première** pour ScienceLycée. Ta seule responsabilité est d'écrire le fichier `backend/courses/management/commands/seed_maths_premiere.py`.

## Rôle

Générer une commande Django management complète qui :
1. **Supprime** tous les `Chapitre` existants de `mathematiques` au niveau `premiere` (cascade → Lecon, Quiz, Question)
2. **Recrée** les chapitres avec leurs leçons, quiz et 20 questions chacune, basés sur le curriculum ci-dessous

## Référence Codebase Obligatoire

1. **Lire `CODEBASE_REFERENCE.md`** (sections 1.4–1.8) en premier pour connaître la structure des modèles `Matiere`, `Chapitre`, `Lecon`, `Quiz`, `Question`.
2. **Ne lire les fichiers source** que si la structure des modèles a changé et que la référence semble obsolète.

---

## Modèles Django (référence)

```python
# Matiere : mathematiques (slug='mathematiques', couleur violet/purple)
# Chapitre : matiere=mathematiques, niveau='premiere', ordre=1..N
# Lecon    : chapitre=..., ordre=1..N, titre, contenu (Markdown), duree_estimee
# Quiz     : lecon=..., titre, score_minimum=60.0
# Question : quiz=..., ordre=1..20, texte, type, options (JSON), reponse_correcte, tolerances, explication, difficulte, points
```

**Types de questions :**
- `qcm` : `options=["A","B","C","D"]`, `reponse_correcte="0"` (index base 0, chaîne)
- `vrai_faux` : `options=["Vrai","Faux"]`, `reponse_correcte="vrai"` ou `"faux"`
- `texte_libre` : `options=None`, `reponse_correcte="réponse attendue"`, `tolerances=["variante1","variante2"]`

**Difficulté :** `"facile"` | `"moyen"` | `"difficile"`

**Mix par leçon (20 questions) :** 8 QCM facile + 6 QCM moyen + 3 vrai_faux + 3 texte_libre (certaines difficile)

---

## Structure du fichier à générer

```python
from django.core.management.base import BaseCommand

MATHS_PREMIERE_DATA = [
    {
        "ordre": 1,
        "titre": "...",
        "description": "...",
        "score_minimum": 60.0,
        "lecons": [
            {
                "ordre": 1,
                "titre": "...",
                "duree": 30,
                "contenu": "# ...\n\n## ...\n\n...",
                "quiz": {
                    "titre": "Quiz — ...",
                    "score_minimum": 60.0,
                    "questions": [
                        {
                            "ordre": 1,
                            "type": "qcm",
                            "texte": "...",
                            "options": ["A", "B", "C", "D"],
                            "reponse_correcte": "2",
                            "explication": "...",
                            "difficulte": "facile",
                            "points": 1,
                        },
                        # … 20 questions au total
                    ],
                },
            },
        ],
    },
]

class Command(BaseCommand):
    help = "Recrée entièrement les chapitres de Mathématiques Première."

    def handle(self, *args, **options):
        from courses.models import Matiere, Chapitre, Lecon, Quiz, Question

        maths = Matiere.objects.get(nom="mathematiques")

        deleted, _ = Chapitre.objects.filter(
            matiere=maths, niveau="premiere"
        ).delete()
        self.stdout.write(f"  🗑  {deleted} chapitres supprimés")

        for chap_data in MATHS_PREMIERE_DATA:
            chapitre = Chapitre.objects.create(
                matiere=maths,
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

        self.stdout.write(self.style.SUCCESS("✅ Mathématiques Première recréée avec succès."))
```

---

## Curriculum détaillé — 8 chapitres

Sources : `/home/vivien/dev/persProject/ressources/1ere/Maths/*.pdf`

### Chapitre 1 — Second degré (ordre=1)

**Fichier source :** `01_cours_second_degre.pdf`

**Leçons :**
- L1 : Le trinôme du second degré
- L2 : Résolution, factorisation et signe

**Concepts clés :**
- Trinôme $ax^2 + bx + c$, $a \neq 0$
- Discriminant $\Delta = b^2 - 4ac$
  - $\Delta > 0$ : deux racines réelles $x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a}$
  - $\Delta = 0$ : racine double $x_0 = -\frac{b}{2a}$
  - $\Delta < 0$ : aucune racine réelle
- Forme factorisée : $a(x - x_1)(x - x_2)$
- Forme canonique : $a\left(x + \frac{b}{2a}\right)^2 - \frac{\Delta}{4a}$
- Sommet de la parabole : $S\left(-\frac{b}{2a} ; -\frac{\Delta}{4a}\right)$
- Signe : du signe de $a$ à l'extérieur des racines
- Somme et produit des racines : $x_1 + x_2 = -\frac{b}{a}$, $x_1 x_2 = \frac{c}{a}$

---

### Chapitre 2 — Suites numériques (ordre=2)

**Fichiers sources :** `02_cours_suites.pdf`, `02_cours_suite_fibonacci.pdf`

**Leçons :**
- L1 : Définition, modes de génération et monotonie
- L2 : Suites arithmétiques et géométriques
- L3 : Suite de Fibonacci et suites récurrentes

**Concepts clés :**
- Suite : fonction $u : \mathbb{N} \to \mathbb{R}$
- Définition explicite $u_n = f(n)$ vs récurrente $u_{n+1} = f(u_n)$
- Monotonie : signe de $u_{n+1} - u_n$ (ou rapport pour les géométriques)
- **Suite arithmétique** de raison $r$ : $u_n = u_0 + nr$ ; somme $S_n = (n+1)\frac{u_0 + u_n}{2}$
- **Suite géométrique** de raison $q$ : $u_n = u_0 q^n$ ; somme $S_n = u_0 \frac{1 - q^{n+1}}{1 - q}$
- **Suite de Fibonacci** : $u_0=1, u_1=1, u_{n+2} = u_{n+1} + u_n$ ; formule de Binet : $u_n = \frac{\phi^n - \psi^n}{\sqrt{5}}$ avec $\phi = \frac{1+\sqrt{5}}{2}$
- Suite bornée, majorée, minorée
- Suites arithmético-géométriques : $u_{n+1} = au_n + b$ → trouver le point fixe $l = \frac{b}{1-a}$, puis $v_n = u_n - l$ est géométrique

---

### Chapitre 3 — Généralités sur les fonctions (ordre=3)

**Fichiers sources :** `03_cours_generalites_fonctions.pdf`, `03_cours_complement_valeur_absolue.pdf`

**Leçons :**
- L1 : Ensemble de définition, image, tableau de variation
- L2 : Fonctions de référence et parité
- L3 : Valeur absolue

**Concepts clés :**
- Ensemble de définition $D_f$, image $f(a)$, antécédent
- Tableau de variation : flèche croissante/décroissante avec extrema
- **Fonctions de référence** :
  - Affine $f(x) = ax + b$ : droite de pente $a$
  - Carré $f(x) = x^2$ : paire, décroissante sur $(-\infty,0]$, croissante sur $[0,+\infty)$
  - Inverse $f(x) = \frac{1}{x}$ : impaire, décroissante sur $(-\infty,0)$ et $(0,+\infty)$
  - Racine carrée $f(x) = \sqrt{x}$ : $D_f = [0,+\infty)$, croissante
- **Parité** : paire $f(-x)=f(x)$ (symétrie axe $Oy$) ; impaire $f(-x)=-f(x)$ (symétrie origine)
- **Valeur absolue** : $|x| = x$ si $x \geq 0$, $-x$ sinon ; $|u(x)| = |v(x)| \Leftrightarrow u=v$ ou $u=-v$

---

### Chapitre 4 — La dérivée (ordre=4)

**Fichier source :** `04_cours_fonction_derivee.pdf`

**Leçons :**
- L1 : Nombre dérivé et dérivées usuelles
- L2 : Règles de dérivation (somme, produit, quotient)
- L3 : Dérivée composée et applications

**Concepts clés :**
- Nombre dérivé en $a$ : $f'(a) = \lim_{h\to 0} \frac{f(a+h)-f(a)}{h}$ → pente de la tangente
- **Dérivées usuelles** : $(x^n)'=nx^{n-1}$, $(\sqrt{x})'=\frac{1}{2\sqrt{x}}$, $\left(\frac{1}{x}\right)'=-\frac{1}{x^2}$
- **Règles** : $(u+v)'=u'+v'$, $(ku)'=ku'$, $(uv)'=u'v+uv'$, $\left(\frac{u}{v}\right)'=\frac{u'v-uv'}{v^2}$
- **Dérivée composée** : $(g \circ u)' = u' \cdot (g' \circ u)$
  ex: $(u^n)' = nu'u^{n-1}$, $(\sqrt{u})' = \frac{u'}{2\sqrt{u}}$
- Équation tangente en $x_0$ : $y = f'(x_0)(x - x_0) + f(x_0)$
- Monotonie : $f' > 0 \Rightarrow$ croissante ; $f' < 0 \Rightarrow$ décroissante
- Extremum local en $x_0$ : $f'(x_0)=0$ et changement de signe de $f'$

---

### Chapitre 5 — Fonction exponentielle (ordre=5)

**Fichier source :** `05_Cours_fonction_exponentielle.pdf`

**Leçons :**
- L1 : Définition et propriétés algébriques
- L2 : Dérivée, variations et croissances comparées
- L3 : Modèles exponentiels (croissance, décroissance, équations différentielles)

**Concepts clés :**
- Définition : unique fonction $f$ dérivable sur $\mathbb{R}$ telle que $f' = f$ et $f(0) = 1$
- Notation : $e^x$ ; $e \approx 2{,}718$
- **Propriétés algébriques** : $e^{a+b} = e^a \cdot e^b$, $e^{a-b} = \frac{e^a}{e^b}$, $e^{-a} = \frac{1}{e^a}$, $(e^a)^n = e^{na}$
- Dérivée : $(e^x)' = e^x$ ; dérivée composée : $(e^{u(x)})' = u'(x) e^{u(x)}$
- Strictement positive, strictement croissante, $e^x > 0$ pour tout $x$
- **Croissances comparées** : $\lim_{x\to+\infty} \frac{e^x}{x^n} = +\infty$ et $\lim_{x\to-\infty} x^n e^x = 0$
- Équation différentielle $y' = ay$ : solution $y = Ce^{ax}$
- **Modèles** : croissance bactérienne $N(t) = N_0 e^{kt}$, décroissance radioactive $N(t) = N_0 e^{-\lambda t}$, temps de demi-vie $t_{1/2} = \frac{\ln 2}{\lambda}$

---

### Chapitre 6 — Trigonométrie (ordre=6)

**Fichier source :** `06_cours_trigo_sin_cos.pdf`

**Leçons :**
- L1 : Angles orientés, radian et cercle trigonométrique
- L2 : Cosinus, sinus et valeurs remarquables
- L3 : Équations et identités trigonométriques

**Concepts clés :**
- Mesure d'angle en **radian** : $\pi$ rad = 180° ; $\frac{\pi}{6}=30°$, $\frac{\pi}{4}=45°$, $\frac{\pi}{3}=60°$, $\frac{\pi}{2}=90°$
- Cercle trigonométrique : $M$ associé à l'angle $\theta$, $\cos\theta$ abscisse, $\sin\theta$ ordonnée
- **Valeurs remarquables** :

| $\theta$ | 0 | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ |
|----------|---|---------|---------|---------|---------|
| $\cos\theta$ | 1 | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | 0 |
| $\sin\theta$ | 0 | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | 1 |

- **Identité fondamentale** : $\cos^2\theta + \sin^2\theta = 1$
- **Relations de symétrie** : $\cos(-\theta)=\cos\theta$, $\sin(-\theta)=-\sin\theta$, $\cos(\pi-\theta)=-\cos\theta$, $\sin(\pi-\theta)=\sin\theta$
- **Déphasages** : $\cos(\theta+\frac{\pi}{2})=-\sin\theta$, $\sin(\theta+\frac{\pi}{2})=\cos\theta$
- **Équations** : $\cos x = \cos\alpha \Leftrightarrow x = \pm\alpha + 2k\pi$ ; $\sin x = \sin\alpha \Leftrightarrow x = \alpha + 2k\pi$ ou $x = \pi - \alpha + 2k\pi$

---

### Chapitre 7 — Produit scalaire et géométrie (ordre=7)

**Fichier source :** `07_cours_prod_scalaire_geo_reperee.pdf`

**Leçons :**
- L1 : Produit scalaire — définitions et propriétés
- L2 : Applications géométriques et repérée

**Concepts clés :**
- **Définitions du produit scalaire** $\vec{u} \cdot \vec{v}$ :
  - Géométrique : $|\vec{u}||\vec{v}|\cos\theta$ où $\theta$ est l'angle entre les vecteurs
  - Analytique : $\vec{u}(x;y)$, $\vec{v}(x';y')$ → $\vec{u}\cdot\vec{v} = xx' + yy'$
  - Via normes : $\vec{u}\cdot\vec{v} = \frac{1}{2}(|\vec{u}+\vec{v}|^2 - |\vec{u}|^2 - |\vec{v}|^2)$
- **Propriétés** : bilinéarité, symétrie, $\vec{u}\cdot\vec{u}=|\vec{u}|^2$
- Vecteurs orthogonaux : $\vec{u}\perp\vec{v} \Leftrightarrow \vec{u}\cdot\vec{v}=0$
- Norme : $|\vec{u}| = \sqrt{x^2+y^2}$
- **Formule d'Al-Kashi** : $a^2 = b^2 + c^2 - 2bc\cos A$
- Droite de vecteur normal $\vec{n}(a;b)$ passant par $A(x_0;y_0)$ : $a(x-x_0)+b(y-y_0)=0$
- Cercle de centre $\Omega(a;b)$ et rayon $r$ : $(x-a)^2+(y-b)^2=r^2$

---

### Chapitre 8 — Probabilités et variables aléatoires (ordre=8)

**Fichier source :** `08_cours_probabilite_cond_var_aleatoire.pdf`

**Leçons :**
- L1 : Probabilités conditionnelles et indépendance
- L2 : Variables aléatoires discrètes — loi, espérance, variance

**Concepts clés :**
- **Probabilité conditionnelle** : $P(A|B) = \frac{P(A \cap B)}{P(B)}$
- **Formule des probabilités totales** : si $(B_i)$ partition : $P(A) = \sum_i P(A|B_i)P(B_i)$
- **Indépendance** : $A$ et $B$ indépendants $\Leftrightarrow P(A \cap B) = P(A) \cdot P(B)$
- **Variable aléatoire** discrète $X$ : loi $P(X=x_i) = p_i$, $\sum p_i = 1$
- **Espérance** : $E(X) = \sum x_i p_i$
- **Variance** : $V(X) = E(X^2) - [E(X)]^2 = \sum x_i^2 p_i - [E(X)]^2$
- **Écart-type** : $\sigma(X) = \sqrt{V(X)}$
- **Loi binomiale** $B(n,p)$ : $P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$ ; $E(X)=np$ ; $V(X)=np(1-p)$
- Arbres de probabilité pour calculer $P(A \cap B)$ par produit des branches

---

## Instructions d'exécution

Après génération du fichier :
```bash
docker compose run --rm --entrypoint python web manage.py seed_maths_premiere
```

Le fichier doit être enregistré dans :
`backend/courses/management/commands/seed_maths_premiere.py`
