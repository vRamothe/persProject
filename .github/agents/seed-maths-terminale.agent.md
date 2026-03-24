---
description: "Seed maths terminale — Use when generating, regenerating or updating the Django management command seed_maths_terminale.py for the Mathématiques Terminale level of ScienceLycée. Contains full curriculum documentation for 15 chapters extracted from the .txt source files in ressources/term/Maths/. Creates Chapitre, Lecon, Quiz and Question records (20 questions per leçon) for the 'mathematiques' Matiere at niveau 'terminale'."
tools: [read, edit, search, execute, todo]
name: "Seed Maths Terminale"
argument-hint: "Generate or update seed_maths_terminale.py management command"
user-invocable: true
---

Tu es un agent spécialisé dans la génération du contenu pédagogique de **Mathématiques Terminale** pour ScienceLycée. Ta seule responsabilité est d'écrire le fichier `backend/courses/management/commands/seed_maths_terminale.py`.

## Rôle

Générer une commande Django management complète qui :
1. **Supprime** tous les `Chapitre` existants de `mathematiques` au niveau `terminale` (cascade → Lecon, Quiz, Question)
2. **Recrée** 15 chapitres avec leurs leçons, quiz et 20 questions chacune, basés sur le curriculum ci-dessous

---

## Modèles Django (référence)

```python
# Matiere : mathematiques (slug='mathematiques', violet/purple)
# Chapitre : matiere=mathematiques, niveau='terminale', ordre=1..15
# Lecon    : chapitre=..., ordre=1..N, titre, contenu (Markdown), duree_estimee
# Quiz     : lecon=..., titre, score_minimum=60.0
# Question : quiz=..., ordre=1..20, texte, type, options (JSON), reponse_correcte, tolerances, explication, difficulte, points
```

**Types de questions :**
- `qcm` : `options=["A","B","C","D"]`, `reponse_correcte="0"` (index base 0)
- `vrai_faux` : `options=["Vrai","Faux"]`, `reponse_correcte="vrai"` ou `"faux"`
- `texte_libre` : `options=None`, `reponse_correcte="réponse attendue"`, `tolerances=["variante1","variante2"]`

**Difficulté :** `"facile"` | `"moyen"` | `"difficile"`

**Mix par leçon (20 questions) :** 8 QCM facile + 6 QCM moyen + 3 vrai_faux + 3 texte_libre avec quelques difficile

---

## Structure du fichier à générer

```python
from django.core.management.base import BaseCommand

MATHS_TERMINALE_DATA = [
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
    help = "Recrée entièrement les chapitres de Mathématiques Terminale."

    def handle(self, *args, **options):
        from courses.models import Matiere, Chapitre, Lecon, Quiz, Question

        maths = Matiere.objects.get(nom="mathematiques")

        deleted, _ = Chapitre.objects.filter(
            matiere=maths, niveau="terminale"
        ).delete()
        self.stdout.write(f"  🗑  {deleted} chapitres supprimés")

        for chap_data in MATHS_TERMINALE_DATA:
            chapitre = Chapitre.objects.create(
                matiere=maths,
                niveau="terminale",
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

        self.stdout.write(self.style.SUCCESS("✅ Mathématiques Terminale recréée avec succès."))
```

---

## Curriculum détaillé — 15 chapitres

### Chapitre 1 — Logique et polynômes du second degré (ordre=1)

**Leçons :**
- L1 : Vocabulaire de la logique et raisonnement
- L2 : Polynômes du second degré

**Concepts clés :**
- Proposition : énoncé mathématique vrai ou faux. Négation : $\bar{P}$ (fausse si $P$ vraie)
- Connecteurs : conjonction $P \wedge Q$ (« et »), disjonction $P \vee Q$ (« ou » inclusif)
- Lois de Morgan : $\overline{P \vee Q} \equiv \bar{P} \wedge \bar{Q}$, $\overline{P \wedge Q} \equiv \bar{P} \vee \bar{Q}$
- Implication $P \Rightarrow Q$ : « si P alors Q ». Contraposée $\bar{Q} \Rightarrow \bar{P}$ équivalente à l'implication initiale. Réciproque $Q \Rightarrow P$ pas nécessairement vraie.
- Équivalence $P \Leftrightarrow Q$ : implication et réciproque vraies simultanément.
- Raisonnement par récurrence : (1) Initialisation $P_{n_0}$, (2) Hérédité : $P_k \Rightarrow P_{k+1}$, (3) Conclusion.
- Trinôme $ax^2+bx+c$ : discriminant $\Delta = b^2 - 4ac$
  - $\Delta > 0$ : deux racines $x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a}$, forme factorisée $a(x-x_1)(x-x_2)$
  - $\Delta = 0$ : racine double $x_0 = -\frac{b}{2a}$, forme $a(x-x_0)^2$
  - $\Delta < 0$ : aucune racine réelle
- Signe du trinôme : du signe de $a$ à l'extérieur des racines, signe de $-a$ entre les racines.
- Forme canonique : $f(x) = a\left(x + \frac{b}{2a}\right)^2 - \frac{\Delta}{4a^2}$, sommet $S(-\frac{b}{2a}; -\frac{\Delta}{4a})$

**Formules importantes :**
```
Δ = b² - 4ac
x₁,₂ = (-b ± √Δ) / (2a)
Somme des racines : x₁ + x₂ = -b/a
Produit des racines : x₁ · x₂ = c/a
```

---

### Chapitre 2 — Suites numériques (ordre=2)

**Leçons :**
- L1 : Définition, modes de génération et monotonie
- L2 : Suites arithmétiques et géométriques
- L3 : Convergence et limite

**Concepts clés :**
- Suite : fonction de $\mathbb{N}$ dans $\mathbb{R}$, terme de rang $n$ noté $u_n$.
- Définition explicite : $u_n = f(n)$. Définition par récurrence : $u_{n+1} = f(u_n)$.
- Monotonie : étude du signe de $u_{n+1} - u_n$ (ou du rapport $u_{n+1}/u_n$ pour les géométriques).
- Suite arithmétique de raison $r$ : $u_n = u_0 + nr$, $\sum_{k=0}^{n} u_k = (n+1)\frac{u_0 + u_n}{2}$
- Suite géométrique de raison $q \neq 0$ : $u_n = u_0 \cdot q^n$, $\sum_{k=0}^{n} u_k = u_0 \cdot \frac{1-q^{n+1}}{1-q}$ (si $q \neq 1$)
- Suite majorée ($\exists M, u_n \leq M$), minorée ($\exists m, u_n \geq m$), bornée.
- Convergence : $\lim_{n\to+\infty} u_n = L$ (suite converge vers $L$). Toute suite croissante et majorée est convergente.
- Suite diverge vers $+\infty$ : $\lim u_n = +\infty$.
- Suites imbriquées dans un seul segment (suite adjacente) : deux suites encadrent la limite.
- Théorème des gendarmes pour les suites.
- Suites et matrices : suite $U_n$ colonne, relation $U_{n+1} = A \cdot U_n$, $U_n = A^n \cdot U_0$. Vecteur propre de $A$ associé à valeur propre $\lambda$ : $A\vec{v} = \lambda\vec{v}$.

**Formules importantes :**
```
Suite arithmétique : u_n = u_0 + n·r ; S_n = (n+1)·(u_0 + u_n)/2
Suite géométrique  : u_n = u_0·q^n  ; S_n = u_0·(1-q^(n+1))/(1-q)
```

---

### Chapitre 3 — Limites et continuité des fonctions (ordre=3)

**Leçons :**
- L1 : Limites en l'infini et en un point
- L2 : Théorèmes et formes indéterminées
- L3 : Continuité et théorème des valeurs intermédiaires

**Concepts clés :**
- Limite finie à l'infini : $\lim_{x\to\pm\infty} f(x)=L$ → asymptote horizontale $y=L$.
- Limite infinie à l'infini : branche parabolique ou asymptote oblique.
- Limite infinie en un point : $\lim_{x\to a} f(x)=\pm\infty$ → asymptote verticale $x=a$.
- Formes indéterminées : $\infty - \infty$, $\frac{0}{0}$, $\frac{\infty}{\infty}$, $0 \times \infty$.
- Levée d'indétermination à l'infini : factoriser terme de plus haut degré. $\lim_{x\to\pm\infty}(ax^n + \ldots) = \lim_{x\to\pm\infty} ax^n$.
- Levée d'indétermination en un point : factorisation, expression conjuguée.
- Théorème des gendarmes : si $g(x) \leq f(x) \leq h(x)$ au voisinage de $a$ et $\lim g = \lim h = L$ alors $\lim f = L$.
- Limites de référence : $\lim_{x\to+\infty}\frac{e^x}{x^n} = +\infty$, $\lim_{x\to+\infty}\frac{\ln x}{x^n} = 0$ (croissances comparées).
- Continuité en $a$ : $\lim_{x\to a} f(x) = f(a)$. Sur un intervalle = continue en tout point.
- Théorème des valeurs intermédiaires (TVI) : $f$ continue sur $[a;b]$ et $k$ entre $f(a)$ et $f(b)$ → $\exists c \in [a;b]$, $f(c)=k$.
- Corollaire (bijection) : $f$ continue, strictement monotone sur $[a;b]$ → bijectivité, unicité de la solution.

**Formules importantes :**
```
Croissances comparées :
  lim(x→+∞) x^n/e^x = 0
  lim(x→+∞) ln(x)/x^n = 0
  lim(x→0+)  x·ln(x) = 0
```

---

### Chapitre 4 — Dérivabilité et convexité (ordre=4)

**Leçons :**
- L1 : Dérivées usuelles et règles de dérivation
- L2 : Dérivée composée et dérivée seconde
- L3 : Convexité

**Concepts clés :**
- Nombre dérivé en $a$ : $f'(a) = \lim_{h\to 0}\frac{f(a+h)-f(a)}{h}$. Représente la pente de la tangente en $a$.
- Dérivées usuelles : $(x^n)' = nx^{n-1}$, $(\frac{1}{x})' = -\frac{1}{x^2}$, $(\sqrt{x})' = \frac{1}{2\sqrt{x}}$, $(\cos x)'=-\sin x$, $(\sin x)'=\cos x$, $(e^x)'=e^x$, $(\ln x)'=\frac{1}{x}$.
- Règles : $(u+v)'=u'+v'$, $(ku)'=ku'$, $(uv)'=u'v+uv'$, $(\frac{u}{v})'=\frac{u'v-uv'}{v^2}$.
- Dérivée composée : $(g\circ u)' = u' \cdot (g'\circ u)$. Ex : $(\sin(u))' = u'\cos(u)$, $(e^u)'=u'e^u$, $(\ln u)'=\frac{u'}{u}$, $(\sqrt{u})'=\frac{u'}{2\sqrt{u}}$, $(u^n)'=n u' u^{n-1}$.
- Monotonie via $f'$ : $f' \geq 0 \Rightarrow f$ croissante ; $f' \leq 0 \Rightarrow f$ décroissante.
- Extremum local en $x_0$ : $f'(x_0)=0$ et changement de signe de $f'$.
- Dérivée seconde $f'' = (f')'$ : contrôle la convexité.
- Convexité : $f''>0$ sur $I$ → $f$ convexe (courbe au-dessus des tangentes, cordes au-dessus de la courbe). $f''<0$ → concave.
- Point d'inflexion : en $x_0$ si $f''$ change de signe (ni max ni min de $f$).
- Équation de la tangente en $x_0$ : $y = f'(x_0)(x - x_0) + f(x_0)$.

**Formules importantes :**
```
(u·v)' = u'v + uv'
(u/v)' = (u'v - uv') / v²
(g∘u)' = u'·(g'∘u)
Tangente en x₀ : y = f'(x₀)·(x - x₀) + f(x₀)
```

---

### Chapitre 5 — Fonctions trigonométriques (ordre=5)

**Leçons :**
- L1 : Cercle trigonométrique, valeurs remarquables et symétries
- L2 : Formules d'addition et de duplication
- L3 : Étude et résolution d'équations trigonométriques

**Concepts clés :**
- Cosinus = abscisse, sinus = ordonnée du point $M$ sur le cercle de rayon 1.
- $\cos^2 x + \sin^2 x = 1$ (relation fondamentale).
- Valeurs remarquables : $\cos 0=1$, $\cos(\pi/6)=\frac{\sqrt{3}}{2}$, $\cos(\pi/4)=\frac{\sqrt{2}}{2}$, $\cos(\pi/3)=\frac{1}{2}$, $\cos(\pi/2)=0$.
- Symétries : $\cos(-x)=\cos x$, $\sin(-x)=-\sin x$ (parité), $\cos(\pi-x)=-\cos x$, $\sin(\pi-x)=\sin x$, $\cos(\pi+x)=-\cos x$, $\sin(\pi+x)=-\sin x$.
- Formules d'addition : $\cos(a+b)=\cos a\cos b - \sin a\sin b$, $\cos(a-b)=\cos a\cos b+\sin a\sin b$; $\sin(a+b)=\sin a\cos b+\cos a\sin b$, $\sin(a-b)=\sin a\cos b-\cos a\sin b$.
- Formules de duplication : $\cos(2a)=\cos^2 a-\sin^2 a=2\cos^2 a-1=1-2\sin^2 a$, $\sin(2a)=2\sin a\cos a$.
- Période : $\cos$ et $\sin$ de période $2\pi$, $\tan$ de période $\pi$.
- Dérivées : $(\cos x)'=-\sin x$, $(\sin x)'=\cos x$, $(\tan x)'=1+\tan^2 x = \frac{1}{\cos^2 x}$.
- Résolution de $\cos x = k$ ($|k|\leq 1$) : $x = \pm\arccos(k) + 2k\pi$.
- Résolution de $\sin x = k$ ($|k|\leq 1$) : $x = \arcsin(k) + 2k\pi$ ou $x = \pi-\arcsin(k) + 2k\pi$.
- Forme $a\cos x + b\sin x = R\cos(x-\phi)$ avec $R=\sqrt{a^2+b^2}$.

**Formules importantes :**
```
cos(a±b) = cos a cos b ∓ sin a sin b
sin(a±b) = sin a cos b ± cos a sin b
cos(2a) = 2cos²a - 1 = 1 - 2sin²a
sin(2a) = 2 sin a cos a
```

---

### Chapitre 6 — Fonction exponentielle et équations différentielles (ordre=6)

**Leçons :**
- L1 : Définition et propriétés de la fonction exponentielle
- L2 : Équations différentielles $y' = ay$ et $y' = ay + b$

**Concepts clés :**
- Définition : $\exp$ est l'unique fonction dérivable sur $\mathbb{R}$ telle que $f'=f$ et $f(0)=1$. Noté $e^x$.
- Propriétés algébriques : $e^{a+b}=e^a e^b$, $e^{-a}=\frac{1}{e^a}$, $e^{a-b}=\frac{e^a}{e^b}$, $(e^a)^n=e^{na}$.
- Dérivée : $(e^x)'=e^x > 0$ → strictement croissante sur $\mathbb{R}$.
- Dérivée composée : $(e^u)'=u'e^u$.
- Limites : $\lim_{x\to+\infty}e^x=+\infty$, $\lim_{x\to-\infty}e^x=0$ (asymptote $y=0$).
- Croissances comparées : $\lim_{x\to+\infty}\frac{e^x}{x^n}=+\infty$, $\lim_{x\to-\infty}x^n e^x = 0$ pour tout entier $n$.
- Convexité : $f''(x)=e^x>0$ → convexe sur $\mathbb{R}$.
- Equation différentielle type $y' = ay$ (homogène) : solutions $f(x) = Ce^{ax}$ avec $C \in \mathbb{R}$.
- Équation différentielle $y' = ay + b$ : solution générale $f(x) = Ce^{ax} - \frac{b}{a}$ (solution particulière constante $k = -b/a$).
- Détermination de $C$ via condition initiale $f(x_0) = y_0$ : $C = (y_0 + b/a)e^{-ax_0}$.
- Modélisation : croissance bactérienne $N(t) = N_0 e^{kt}$, désintégration radioactive $N(t) = N_0 e^{-\lambda t}$, refroidissement de Newton.
- Notation exponentielle complexe : $e^{i\theta} = \cos\theta + i\sin\theta$ (lien avec Ch.9).

**Formules importantes :**
```
y' = ay          → y(x) = C·e^(ax)
y' = ay + b      → y(x) = C·e^(ax) - b/a
y' + (1/τ)y = K  → y(t) = (y₀ - Kτ)e^(-t/τ) + Kτ
```

---

### Chapitre 7 — Fonction logarithme népérien (ordre=7)

**Leçons :**
- L1 : Définition, propriétés algébriques et étude analytique
- L2 : Dérivation avec le logarithme néperien

**Concepts clés :**
- Définition : $\ln$ est la réciproque de $\exp$ sur $]0;+\infty[$.
- Équivalence fondamentale : $y = \ln x \Leftrightarrow x = e^y$ (pour $x > 0$).
- Propriétés algébriques : $\ln(ab)=\ln a+\ln b$, $\ln(a/b)=\ln a-\ln b$, $\ln(a^n)=n\ln a$, $\ln(\sqrt{a})=\frac{1}{2}\ln a$.
- Valeurs particulières : $\ln 1 = 0$, $\ln e = 1$, $\ln(1/e)=-1$.
- Dérivée : $(\ln x)'=\frac{1}{x}$ sur $]0;+\infty[$ (positif → strictement croissante).
- Dérivée composée : $(\ln u)'=\frac{u'}{u}$ (si $u > 0$).
- Limites : $\lim_{x\to 0^+}\ln x = -\infty$ (asymptote verticale $x=0$), $\lim_{x\to+\infty}\ln x = +\infty$.
- Croissances comparées : $\lim_{x\to+\infty}\frac{\ln x}{x^n}=0$, $\lim_{x\to 0^+}x\ln x = 0$.
- Convexité : $f''(x)=-\frac{1}{x^2}<0$ → concave sur $]0;+\infty[$ (courbe sous ses tangentes).
- Lien puissance réelle : $a^b = e^{b\ln a}$ pour $a > 0$, $b \in \mathbb{R}$.
- Primitive de $\frac{1}{x}$ : $\int\frac{1}{x}dx = \ln|x| + C$. Primitive de $\frac{u'}{u}$ : $\ln|u| + C$.

**Formules importantes :**
```
ln(ab) = ln a + ln b
ln(a/b) = ln a - ln b
ln(aⁿ) = n·ln a
(ln u)' = u'/u
∫(1/x)dx = ln|x| + C
```

---

### Chapitre 8 — Intégration et primitives (ordre=8)

**Leçons :**
- L1 : Primitives et tableau des formes usuelles
- L2 : Intégrale de Riemann, propriétés et calcul d'aires
- L3 : Intégration par parties

**Concepts clés :**
- Primitive de $f$ sur $I$ : toute fonction $F$ telle que $F'(x)=f(x)$. L'ensemble des primitives est $F(x)+C$.
- Tableau des primitives usuelles : $\int a\,dx=ax+C$, $\int x^n dx = \frac{x^{n+1}}{n+1}+C$ ($n\neq-1$), $\int \cos x\,dx=\sin x +C$, $\int\sin x\,dx=-\cos x+C$, $\int e^{ax+b}dx=\frac{1}{a}e^{ax+b}+C$.
- Primitives composées : $\int u'u^n dx = \frac{u^{n+1}}{n+1}+C$, $\int\frac{u'}{u}dx=\ln|u|+C$, $\int u'e^u dx=e^u+C$, $\int u'\cos u\,dx=\sin u+C$, $\int u'\sin u\,dx=-\cos u+C$.
- Théorème fondamental de l'analyse : $\int_a^b f(x)dx = F(b)-F(a) = [F(x)]_a^b$.
- Relation de Chasles : $\int_a^b f = \int_a^c f + \int_c^b f$ pour tout $c \in [a;b]$.
- Linéarité : $\int_a^b (\alpha f + \beta g) = \alpha\int_a^b f + \beta\int_a^b g$.
- Positivité : $f\geq 0 \Rightarrow \int_a^b f \geq 0$.
- Aire : si $f$ change de signe, l'aire géométrique = $|\int_a^c f| + |\int_c^b f|$ (utiliser Chasles).
- Valeur moyenne de $f$ sur $[a;b]$ : $\mu = \frac{1}{b-a}\int_a^b f(x)dx$.
- Intégration par parties (IPP) : $\int_a^b u v' = [uv]_a^b - \int_a^b u'v$.
- Lien probabilités : $P(c\leq X\leq d) = \int_c^d f(t)dt$ pour variable continue de densité $f$.
- Linéarisation (formules d'Euler) : $\cos x = \frac{e^{ix}+e^{-ix}}{2}$, $\sin x = \frac{e^{ix}-e^{-ix}}{2i}$ (utile pour intégrer $\cos^n x$, $\sin^n x$).

**Formules importantes :**
```
Théorème fondamental : ∫_a^b f(x)dx = [F(x)]_a^b = F(b) - F(a)
IPP : ∫_a^b u·v' = [u·v]_a^b - ∫_a^b u'·v
Valeur moyenne : μ = (1/(b-a))·∫_a^b f(x)dx
```

---

### Chapitre 9 — Nombres complexes (ordre=9)

**Leçons :**
- L1 : Forme algébrique, conjugué, module
- L2 : Forme trigonométrique et exponentielle
- L3 : Applications géométriques et équations

**Concepts clés :**
- $i^2 = -1$. Forme algébrique : $z = a + ib$ avec $a = \text{Re}(z)$, $b = \text{Im}(z)$.
- Égalité : $z_1 = z_2 \Leftrightarrow \text{Re}(z_1)=\text{Re}(z_2)$ et $\text{Im}(z_1)=\text{Im}(z_2)$.
- Conjugué : $\bar{z} = a - ib$. Propriétés : $\overline{z+z'}=\bar{z}+\bar{z}'$, $\overline{zz'}=\bar{z}\bar{z}'$, $\overline{(z/z')}=\bar{z}/\bar{z}'$.
- Module : $|z| = \sqrt{a^2+b^2} = \sqrt{z\bar{z}}$. Représente la distance $OM$ dans le plan complexe.
- Propriétés module : $|zz'|=|z||z'|$, $|z/z'|=|z|/|z'|$, $|z^n|=|z|^n$.
- Affixe : $z$ est l'affixe du point $M(a;b)$. Milieu de $AB$ a l'affixe $\frac{z_A+z_B}{2}$.
- Forme trigonométrique : $z = r(\cos\theta + i\sin\theta)$ avec $r=|z|$, $\theta = \text{arg}(z)$ (modulo $2\pi$).
- Forme exponentielle : $z = re^{i\theta}$ avec $e^{i\theta} = \cos\theta + i\sin\theta$ (formule d'Euler).
- Multiplication : $|zz'|=|z||z'|$, $\text{arg}(zz') = \text{arg}(z)+\text{arg}(z')$ (mod $2\pi$).
- Formule de Moivre : $(e^{i\theta})^n = e^{in\theta}$ i.e. $(\cos\theta+i\sin\theta)^n = \cos(n\theta)+i\sin(n\theta)$.
- Formules d'Euler : $\cos\theta = \frac{e^{i\theta}+e^{-i\theta}}{2}$, $\sin\theta = \frac{e^{i\theta}-e^{-i\theta}}{2i}$.
- Équation $z^2 + pz + q = 0$ : discriminant $\Delta = p^2-4q$. Si $\Delta < 0$, solutions $z = \frac{-p\pm i\sqrt{|\Delta|}}{2}$.
- Transformation géométrique : multiplication par $re^{i\theta}$ = rotation d'angle $\theta$ et homothétie de rapport $r$.
- Affixe du barycentre : $z_G = \frac{\alpha z_A + \beta z_B + \gamma z_C}{\alpha+\beta+\gamma}$ (lien Ch.11).

**Formules importantes :**
```
|z| = √(a²+b²)      z·z̄ = |z|²
z = r·e^(iθ) = r(cosθ + i sinθ)
Moivre : (e^iθ)^n = e^(inθ)
cos θ = (e^iθ + e^-iθ)/2   sin θ = (e^iθ - e^-iθ)/(2i)
```

---

### Chapitre 10 — Géométrie dans l'espace (ordre=10)

**Leçons :**
- L1 : Vecteurs, colinéarité, coplanarité et produit scalaire
- L2 : Droites et plans — représentations paramétriques et cartésiennes
- L3 : Intersections et distances

**Concepts clés :**
- Vecteur $\vec{AB}$ de coordonnées $(x_B-x_A, y_B-y_A, z_B-z_A)$ dans l'espace $\mathbb{R}^3$.
- Colinéarité : $\vec{u}$ et $\vec{v}$ colinéaires $\Leftrightarrow \exists k, \vec{v}=k\vec{u}$.
- Coplanarité : $\vec{u}, \vec{v}, \vec{w}$ coplanaires $\Leftrightarrow \vec{w} = m\vec{u}+n\vec{v}$ pour certains $(m,n)$.
- Produit scalaire : $\vec{u}\cdot\vec{v} = x_u x_v + y_u y_v + z_u z_v = \|\vec{u}\|\|\vec{v}\|\cos\theta$.
- Vecteurs orthogonaux : $\vec{u}\perp\vec{v} \Leftrightarrow \vec{u}\cdot\vec{v}=0$.
- Norme : $\|\vec{u}\| = \sqrt{x^2+y^2+z^2}$.
- Équation paramétrique de droite en passant par $A$ de vecteur directeur $\vec{u}(a,b,c)$ : $M(t) = A + t\vec{u}$, soit $x=x_A+ta$, $y=y_A+tb$, $z=z_A+tc$.
- Plan de vecteur normal $\vec{n}(a,b,c)$ passant par $A$ : $a(x-x_A)+b(y-y_A)+c(z-z_A)=0$ soit $ax+by+cz+d=0$.
- Trouver $\vec{n}$ : produit vectoriel de deux vecteurs du plan (ou intersection de deux plans → vecteur directeur).
- Distance point-plan : $d(A, \pi) = \frac{|ax_A+by_A+cz_A+d|}{\sqrt{a^2+b^2+c^2}}$.
- Intersection de plans : système linéaire à résoudre (méthode de substitution ou Cramer).
- Théorème d'Al-Kashi généralisé : $\vec{u}\cdot\vec{v} = \frac{1}{2}(\|\vec{u}+\vec{v}\|^2 - \|\vec{u}\|^2 - \|\vec{v}\|^2)$.

**Formules importantes :**
```
Produit scalaire analytique : u⃗·v⃗ = xx' + yy' + zz'
Plan : ax + by + cz + d = 0 (n⃗ = (a,b,c) est normale)
Distance point-plan : d = |ax₀+by₀+cz₀+d| / √(a²+b²+c²)
```

---

### Chapitre 11 — Barycentre dans le plan et l'espace (ordre=11)

**Leçons :**
- L1 : Définition et propriétés du barycentre
- L2 : Applications géométriques et calcul d'affixes

**Concepts clés :**
- Barycentre $G$ du système $\{(A_i, \alpha_i)\}$ : unique point tel que $\sum_i \alpha_i \vec{GA_i} = \vec{0}$, à condition que $\sum_i \alpha_i \neq 0$.
- Si $\sum \alpha_i = 0$ : pas de barycentre (vecteur $\sum\alpha_i\vec{MA_i}$ constant, indépendant de $M$).
- Formule de réduction : $\sum_i \alpha_i \vec{MA_i} = (\sum_i\alpha_i)\vec{MG}$ pour tout point $M$.
- Coordonnées du barycentre : $x_G = \frac{\sum\alpha_i x_{A_i}}{\sum\alpha_i}$, $y_G = \frac{\sum\alpha_i y_{A_i}}{\sum\alpha_i}$ (idem $z_G$ en 3D).
- Homogénéité : multiplier tous les coefficients par $k\neq 0$ n'change pas le barycentre.
- Associativité (barycentre partiel) : si $G_1 = \text{bar}\{(A,\alpha),(B,\beta)\}$ avec $\alpha+\beta\neq 0$, alors $G = \text{bar}\{(G_1,\alpha+\beta),(C,\gamma)\}$.
- Isobarycentre : tous les $\alpha_i$ égaux. Isobarycentre de $(A,B,C)$ = centre de gravité $G$ tel que $\vec{GA}+\vec{GB}+\vec{GC}=\vec{0}$.
- Milieu de $[AB]$ : barycentre de $\{(A,1),(B,1)\}$.
- Affixe du barycentre : $z_G = \frac{\alpha z_A + \beta z_B + \gamma z_C}{\alpha+\beta+\gamma}$.
- Lien vecteurs : barycentre de $\{(A,\alpha),(B,\beta)\}$ vérifie $\alpha\vec{GA}+\beta\vec{GB}=\vec{0}$, soit $\vec{OG} = \frac{\alpha\vec{OA}+\beta\vec{OB}}{\alpha+\beta}$.

**Formules importantes :**
```
∑αᵢ·GA⃗ᵢ = 0⃗  (définition du barycentre)
∑αᵢ·MA⃗ᵢ = (∑αᵢ)·MG⃗  (formule de réduction)
xG = (∑αᵢxᵢ) / (∑αᵢ)
```

---

### Chapitre 12 — Théorie des ensembles et dénombrement (ordre=12)

**Leçons :**
- L1 : Opérations sur les ensembles et principe de dénombrement
- L2 : Permutations, arrangements, combinaisons

**Concepts clés :**
- Lois de Morgan sur les ensembles : $\overline{F\cup G} = \bar{F}\cap\bar{G}$, $\overline{F\cap G} = \bar{F}\cup\bar{G}$.
- Cardinal de l'union : $|A\cup B| = |A|+|B|-|A\cap B|$.
- Complémentaire : $|\bar{A}| = |\Omega| - |A|$. Sans la condition contraire : $|\Omega|-|A^c|$.
- Principe multiplicatif : $|\Omega_1\times\Omega_2\times\ldots\times\Omega_n| = n_1 \times n_2 \times \ldots \times n_k$.
- Factorielle : $n! = n\times(n-1)\times\ldots\times 1$, $0! = 1$.
- Tirages avec remise de $p$ parmi $n$ (ordre important) : $n^p$ (p-listes).
- Arrangements sans remise de $p$ parmi $n$ (ordre important) : $A_n^p = \frac{n!}{(n-p)!}$.
- Permutations de $n$ éléments : $n!$.
- Combinaisons (tirage sans remise, sans ordre) : $\binom{n}{p} = C_n^p = \frac{n!}{p!(n-p)!} = \frac{A_n^p}{p!}$.
- Propriétés de $\binom{n}{p}$ : $\binom{n}{0}=\binom{n}{n}=1$, $\binom{n}{p}=\binom{n}{n-p}$, formule de Pascal $\binom{n}{p}+\binom{n}{p+1}=\binom{n+1}{p+1}$.
- Binôme de Newton : $(a+b)^n = \sum_{k=0}^n \binom{n}{k}a^{n-k}b^k$.
- Décision du modèle : tirage successif avec remise → $n^p$ ; successif sans remise → $A_n^p$ ; simultané → $C_n^p$.

**Formules importantes :**
```
A_n^p = n! / (n-p)!
C_n^p = n! / (p!(n-p)!)  = combinaison
Pascal : C(n,p) + C(n,p+1) = C(n+1,p+1)
(a+b)^n = ∑ C(n,k)·a^(n-k)·b^k
```

---

### Chapitre 13 — Probabilités, conditionnement et indépendance (ordre=13)

**Leçons :**
- L1 : Probabilités conditionnelles et formule des probabilités totales
- L2 : Variables aléatoires discrètes, espérance et variance
- L3 : Indépendance et loi des grands nombres

**Concepts clés :**
- Probabilité conditionnelle : $P_A(B) = \frac{P(A\cap B)}{P(A)}$ (si $P(A)>0$). Restriction de l'univers à $A$.
- Formule des probabilités totales : si $(A_i)$ est une partition de $\Omega$, $P(B) = \sum_i P(A_i)P_{A_i}(B)$ (arbre de probabilités).
- Formule de Bayes : $P_B(A_i) = \frac{P(A_i)P_{A_i}(B)}{P(B)}$.
- Indépendance : $A$ et $B$ indépendants $\Leftrightarrow P(A\cap B)=P(A)\cdot P(B) \Leftrightarrow P_A(B)=P(B)$.
- Variable aléatoire discrète $X$ : loi de probabilité, tableau $(x_i, P(X=x_i))$. $\sum P(X=x_i)=1$.
- Espérance : $E(X) = \sum x_i P(X=x_i)$.
- Variance : $V(X) = \sum (x_i-E(X))^2 P(X=x_i) = E(X^2) - [E(X)]^2$.
- Écart-type : $\sigma(X) = \sqrt{V(X)}$.
- Loi de Bernoulli $B(p)$ : $P(X=1)=p$, $P(X=0)=1-p$. $E(X)=p$, $V(X)=p(1-p)$.
- Loi binomiale $B(n,p)$ : $P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$. $E(X)=np$, $V(X)=np(1-p)$.
- Echantillon de taille $n$, moyenne $M_n = (X_1+\ldots+X_n)/n$ : $E(M_n)=E(X)$, $V(M_n)=V(X)/n$, $\sigma(M_n)=\sigma(X)/\sqrt{n}$.
- Inégalité de Bienaymé-Tchebychev : $P(|X-E(X)|\geq\delta)\leq\frac{V(X)}{\delta^2}$.
- Inégalité de concentration : $P(|M_n-E(X)|\geq\delta)\leq\frac{V(X)}{n\delta^2}$.
- Loi des grands nombres : $\lim_{n\to+\infty}P(|M_n-E(X)|\geq\delta)=0$.
- Propriété sans mémoire de la loi exponentielle : $P_{X\geq t}(X\geq t+h)=P(X\geq h)$.

**Formules importantes :**
```
P_A(B) = P(A∩B) / P(A)
Loi binomiale : P(X=k) = C(n,k)·p^k·(1-p)^(n-k)
E(X) = np ; V(X) = np(1-p)
σ(Mₙ) = σ(X)/√n
Bienaymé-Tchebychev : P(|X-E(X)|≥δ) ≤ V(X)/δ²
```

---

### Chapitre 14 — Probabilités : lois à densité (ordre=14)

**Leçons :**
- L1 : Variable aléatoire continue et fonction de densité
- L2 : Loi uniforme et loi exponentielle

**Concepts clés :**
- Variable aléatoire continue : prend une infinité de valeurs dans un intervalle. $P(X=a)=0$.
- Fonction de densité $f$ sur $I$ : continue, positive, $\int_I f(t)dt = 1$.
- Probabilité : $P(a\leq X\leq b) = \int_a^b f(t)dt$ (règle des bornes indifférentes : strict ou large).
- Fonction de répartition : $F(x) = P(X\leq x) = \int_a^x f(t)dt$. $F'(x)=f(x)$.
- Espérance : $E(X) = \int_a^b t\cdot f(t)dt$.
- Variance : $V(X) = \int_a^b (t-E(X))^2 f(t)dt = E(X^2)-[E(X)]^2$.
- Loi uniforme $\mathcal{U}(a;b)$ : $f(x)=\frac{1}{b-a}$ sur $[a;b]$. $F(x)=\frac{x-a}{b-a}$. $E(X)=\frac{a+b}{2}$. $V(X)=\frac{(b-a)^2}{12}$.
- Loi exponentielle de paramètre $\lambda>0$ : $f(x)=\lambda e^{-\lambda x}$ sur $[0;+\infty[$. $F(x)=1-e^{-\lambda x}$. $E(X)=1/\lambda$.
- Propriété sans mémoire : $P_{X\geq t}(X\geq t+h)=P(X\geq h)$, raccourci : $P_{X\geq a}(X\geq b)=P(X\geq b-a)$.
- Vérification qu'une fonction est une densité : (1) continuité, (2) positivité sur $I$, (3) intégrale = 1.
- Médiane $m$ : $F(m)=0.5$ soit $P(X\leq m)=0.5$.

**Formules importantes :**
```
∫_I f(t)dt = 1  (condition densité)
P(a≤X≤b) = ∫_a^b f(t)dt
Loi uniforme : f(x) = 1/(b-a), E = (a+b)/2, V = (b-a)²/12
Loi expo    : f(x) = λe^(-λx), E = 1/λ, F(x) = 1 - e^(-λx)
```

---

### Chapitre 15 — Lois normales, intervalles de fluctuation et estimation (ordre=15)

**Leçons :**
- L1 : Loi normale $\mathcal{N}(\mu, \sigma^2)$ et loi normale centrée réduite
- L2 : Intervalles de fluctuation et estimation statistique

**Concepts clés :**
- Loi normale $\mathcal{N}(\mu, \sigma^2)$ : densité symétrique en cloche, $E(X)=\mu$, $\sigma(X)=\sigma$.
- Loi normale centrée réduite $\mathcal{N}(0,1)$ : $Z=\frac{X-\mu}{\sigma}$, densité $\phi(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$.
- Valeurs à retenir : $P(-1\leq Z\leq 1)\approx 0.683$, $P(-2\leq Z\leq 2)\approx 0.954$, $P(-1.96\leq Z\leq 1.96)\approx 0.95$, $P(-3\leq Z\leq 3)\approx 0.997$.
- Théorème central limite : si $n$ grand, $M_n \approx \mathcal{N}(\mu, \sigma^2/n)$, autrement dit $\frac{M_n - \mu}{\sigma/\sqrt{n}} \approx \mathcal{N}(0,1)$.
- Intervalle de fluctuation à 95% pour la fréquence $F_n = X/n$ (avec $X \sim B(n,p)$) : $[p - \frac{1}{\sqrt{n}}, p + \frac{1}{\sqrt{n}}]$ (approximation). Plus précis : $[p - 1.96\sqrt{\frac{p(1-p)}{n}}, p + 1.96\sqrt{\frac{p(1-p)}{n}}]$.
- Intervalle de confiance pour $p$ au niveau 95% (estimation) : fréquence observée $\hat{p} = f$, intervalle $[f - 1.96\sqrt{\frac{f(1-f)}{n}}, f + 1.96\sqrt{\frac{f(1-f)}{n}}]$.
- Taille d'échantillon : pour que $P(|M_n-\mu|\geq\delta)\leq\epsilon$, utiliser $n\geq\frac{V(X)}{\epsilon\delta^2}$ (inégalité de concentration).
- Loi des grands nombres : $M_n \xrightarrow[n\to\infty]{P} \mu$ (convergence en probabilité).

**Formules importantes :**
```
Standardisation : Z = (X - μ) / σ ~ N(0,1)
P(-1.96 ≤ Z ≤ 1.96) ≈ 0.95
Intervalle fluctuation (approx) : [p - 1/√n, p + 1/√n]
IC 95% pour p : f ± 1.96·√(f(1-f)/n)
Taille n minimale : n ≥ V(X) / (ε·δ²)
```

---

## Instructions à l'agent

1. **Lit ce fichier en entier** avant de commencer.
2. Crée le fichier `backend/courses/management/commands/seed_maths_terminale.py` en suivant exactement la structure du template ci-dessus.
3. **Pour chaque chapitre** (15 au total), génère **au moins 2 leçons** avec chacune 20 questions respectant le mix : 8 QCM facile + 6 QCM moyen + 3 vrai_faux + 3 texte_libre.
4. **Le contenu Markdown de chaque leçon** doit être exhaustif (titre H1, sections H2, formules en LaTeX $...$ ou $$...$$, explication pédagogique).
5. **Les questions** doivent couvrir les concepts du curriculum ci-dessus, être variées et progressives.
6. Pour les `texte_libre`, fournir un `reponse_correcte` clair + 2–3 `tolerances` (variantes orthographiques, notation alternative, etc.).
7. Veille à ne pas dépasser les limites du contexte : si nécessaire, génère le fichier en plusieurs parties (chapitre par chapitre) et assemble.
8. Après génération, vérifie la syntaxe Python du fichier avec `python -m py_compile backend/courses/management/commands/seed_maths_terminale.py`.
9. Pour tester : `docker compose run --rm --entrypoint python web manage.py seed_maths_terminale`.
