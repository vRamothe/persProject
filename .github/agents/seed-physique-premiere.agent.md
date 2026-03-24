---
description: "Seed physique première — Use when generating, regenerating or updating the Django management command seed_physique_premiere.py for the Physique Première level of ScienceLycée. Contains full curriculum documentation for 9 chapters extracted from the PDF source files in ressources/1ere/PC/. Creates Chapitre, Lecon, Quiz and Question records (20 questions per leçon) for the 'physique' Matiere at niveau 'premiere'."
tools: [read, edit, search, execute, todo]
name: "Seed Physique Première"
argument-hint: "Generate or update seed_physique_premiere.py management command"
user-invocable: true
---

Tu es un agent spécialisé dans la génération du contenu pédagogique de **Physique Première** pour ScienceLycée. Ta seule responsabilité est d'écrire le fichier `backend/courses/management/commands/seed_physique_premiere.py`.

## Rôle

Générer une commande Django management complète qui :
1. **Supprime** tous les `Chapitre` existants de `physique` au niveau `premiere` (cascade → Lecon, Quiz, Question)
2. **Recrée** les chapitres avec leurs leçons, quiz et 20 questions chacune, basés sur le curriculum ci-dessous

---

## Modèles Django (référence)

```python
# Matiere : physique (slug='physique', couleur bleu/blue)
# Chapitre : matiere=physique, niveau='premiere', ordre=1..N
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

PHYSIQUE_PREMIERE_DATA = [...]

class Command(BaseCommand):
    help = "Recrée entièrement les chapitres de Physique Première."

    def handle(self, *args, **options):
        from courses.models import Matiere, Chapitre, Lecon, Quiz, Question

        physique = Matiere.objects.get(nom="physique")

        deleted, _ = Chapitre.objects.filter(
            matiere=physique, niveau="premiere"
        ).delete()
        self.stdout.write(f"  🗑  {deleted} chapitres supprimés")

        for chap_data in PHYSIQUE_PREMIERE_DATA:
            chapitre = Chapitre.objects.create(
                matiere=physique,
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

        self.stdout.write(self.style.SUCCESS("✅ Physique Première recréée avec succès."))
```

---

## Curriculum détaillé — 9 chapitres

Sources : `/home/vivien/dev/persProject/ressources/1ere/PC/Chapitre8_*.pdf` à `Chapitre17_*.pdf`

### Chapitre 1 — Interactions et champs (ordre=1)

**Fichier source :** `Chapitre8_Interactions_et_champs.pdf`

**Leçons :**
- L1 : Les quatre interactions fondamentales
- L2 : Champ gravitationnel et champ électrique

**Concepts clés :**
- **Interactions fondamentales** : gravitationnelle (longue portée, toujours attractive), électromagnétique, nucléaire forte, nucléaire faible
- **Interaction gravitationnelle** (Newton) : $F = G\frac{m_1 m_2}{d^2}$ avec $G = 6{,}67 \times 10^{-11}$ N·m²/kg²
- **Interaction électrostatique** (Coulomb) : $F = k\frac{|q_1 q_2|}{d^2}$ avec $k = 9 \times 10^9$ N·m²/C²
- **Champ gravitationnel** $\vec{g}$ : vecteur en chaque point de l'espace ; force $\vec{P} = m\vec{g}$
  - Près de la Terre : $g \approx 9{,}81$ m/s² (vertical, vers le bas)
- **Champ électrique** $\vec{E}$ : créé par une charge ; force $\vec{F} = q\vec{E}$
  - Lignes de champ : de + vers –
- **Champ uniforme** (condensateur plan) : $E = \frac{U}{d}$ (U tension, d distance)
- Notion de superposition des champs : principe de superposition

---

### Chapitre 2 — Statique des fluides (ordre=2)

**Fichier source :** `Chapitre9_Statique_des_fluides.pdf`

**Leçons :**
- L1 : Pression dans un fluide au repos
- L2 : Poussée d'Archimède

**Concepts clés :**
- **Pression** $P$ : $P = \frac{F}{S}$ (Pa = N/m²) ; pression atmosphérique $P_0 \approx 10^5$ Pa
- **Loi fondamentale de la statique des fluides** : $P_2 - P_1 = -\rho g (z_2 - z_1)$ (hauteur)
  - Simplifiée : $P = P_0 + \rho g h$ (h = profondeur)
- **Communicants** : même fluide en équilibre → même niveau (même pression)
- **Poussée d'Archimède** $\vec{\Pi}$ : $\Pi = \rho_{fluide} \cdot V_{immergé} \cdot g$ (vers le haut)
  - Flottement : $\Pi \geq P$ (poids)
  - Corps coulé : $\Pi < P$
  - Corps en équilibre : $\Pi = P$
- **Baromètre** : hauteur de mercure $h$ telle que $P_0 = \rho_{Hg} g h$ → $h \approx 760$ mm de Hg

---

### Chapitre 3 — Mouvements et forces (ordre=3)

**Fichier source :** `Chapitre10_Mouvements_forces.pdf`

**Leçons :**
- L1 : Cinématique — vecteurs position, vitesse et accélération
- L2 : Principe fondamental de la dynamique (PFD)

**Concepts clés :**
- **Vecteur position** $\vec{OM}(t)$ ; vecteur vitesse $\vec{v} = \frac{d\vec{OM}}{dt}$ ; vecteur accélération $\vec{a} = \frac{d\vec{v}}{dt}$
- Mouvement **rectiligne uniforme** (MRU) : $\vec{a} = \vec{0}$, vitesse constante
- Mouvement **rectiligne uniformément varié** (MRUV) : $\vec{a}$ constant
  - $v(t) = v_0 + at$ ; $x(t) = x_0 + v_0 t + \frac{1}{2}at^2$
- **Principe d'inertie** (1ère loi de Newton) : si $\sum \vec{F} = \vec{0}$ → MRU ou repos
- **PFD** (2ème loi de Newton) : $\sum \vec{F} = m\vec{a}$
  - $\vec{F}$ résultante (N), $m$ masse (kg), $\vec{a}$ accélération (m/s²)
  - Applications : chute libre ($a = g$), plan incliné, fil/poulie
- **Forces usuelles** : poids $\vec{P} = m\vec{g}$, réaction normale $\vec{N}$, tension $\vec{T}$, frottement
- **3ème loi** (action-réaction) : $\vec{F}_{A/B} = -\vec{F}_{B/A}$

---

### Chapitre 4 — Travail et énergie cinétique (ordre=4)

**Fichier source :** `Chapitre12_Travail_Energie_cinetique.pdf`

**Leçons :**
- L1 : Travail d'une force
- L2 : Théorème de l'énergie cinétique (TEC)

**Concepts clés :**
- **Travail** d'une force $\vec{F}$ lors d'un déplacement $\vec{d}$ : $W = \vec{F} \cdot \vec{d} = F \cdot d \cdot \cos\theta$
  - $W > 0$ : force motrice ; $W < 0$ : force résistante ; $W = 0$ si $\perp$ déplacement
  - Unité : joule (J = N·m)
- **Travail du poids** : $W_{\vec{P}} = mg(z_A - z_B) = mgh$ (indépendant du chemin)
- **Travail de la réaction normale** : nul (perpendiculaire au déplacement)
- **Énergie cinétique** : $E_c = \frac{1}{2}mv^2$ (J)
- **Théorème de l'énergie cinétique** : $\sum W_{\text{forces}} = \Delta E_c = E_{c,B} - E_{c,A}$
- Force motrice : accélère le système ; force résistante : freine
- Puissance : $P = \frac{W}{\Delta t} = \vec{F} \cdot \vec{v}$ (W = J/s)

---

### Chapitre 5 — Énergie potentielle et mécanique (ordre=5)

**Fichier source :** `Chapitre13_Energie_potentielle_mecanique.pdf`

**Leçons :**
- L1 : Énergie potentielle de pesanteur
- L2 : Conservation de l'énergie mécanique

**Concepts clés :**
- **Forces conservatives** : leur travail ne dépend pas du chemin (ex: poids, élasticité)
- **Énergie potentielle de pesanteur** : $E_{pp} = mgz$ (z altitude; référence choisie)
  - $W_{\vec{P}} = -\Delta E_{pp} = -(E_{pp,B} - E_{pp,A})$
- **Énergie mécanique** : $E_m = E_c + E_{pp}$
- **Conservation** : si les seules forces sont conservatives → $E_m = \text{cte}$
  - $E_{c,A} + E_{pp,A} = E_{c,B} + E_{pp,B}$
- **Non conservation** : si forces de frottement → $\Delta E_m = W_{\text{frottements}} < 0$
- Énergie potentielle élastique : $E_{pe} = \frac{1}{2}kx^2$ (ressort de raideur $k$, allongement $x$)
- Bilan d'énergie : $E_m(\text{final}) = E_m(\text{initial}) + W_{\text{forces non conservatives}}$

---

### Chapitre 6 — Aspects énergétiques de l'électricité (ordre=6)

**Fichier source :** `Chapitre14_Aspects_energetique_electricite.pdf`

**Leçons :**
- L1 : Puissance et énergie électrique
- L2 : Rendement et effet Joule

**Concepts clés :**
- **Puissance électrique** : $P = U \cdot I$ (W = V·A) ; puissance crête vs consommation réelle
- **Énergie électrique** : $E = P \cdot \Delta t = U \cdot I \cdot \Delta t$ (J ou kWh)
  - Conversion : 1 kWh = $3{,}6 \times 10^6$ J
- **Effet Joule** : énergie dissipée par résistance $R$ : $P_J = R \cdot I^2 = \frac{U^2}{R}$
- **Loi d'Ohm** : $U = R \cdot I$ (V, Ω, A)
- **Association de résistances** :
  - Série : $R_{eq} = R_1 + R_2$
  - Parallèle : $\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2}$
- **Rendement** : $\eta = \frac{P_{\text{utile}}}{P_{\text{absorbée}}} = \frac{E_{\text{utile}}}{E_{\text{absorbée}}}$ ; $0 \leq \eta \leq 1$
- Générateur : $E = r \cdot I + U$ (force électromotrice, résistance interne $r$)

---

### Chapitre 7 — Ondes mécaniques (ordre=7)

**Fichier source :** `Chapitre15_Ondes-mecaniques.pdf`

**Leçons :**
- L1 : Propagation et célérité
- L2 : Caractéristiques d'une onde periodic (période, fréquence, longueur d'onde)

**Concepts clés :**
- **Onde mécanique** : perturbation se propageant dans un milieu matériel (sans transport de matière)
  - Longitudinale (déplacement || propagation) : son
  - Transversale (déplacement ⊥ propagation) : corde vibrante
- **Célérité** (vitesse de propagation) $v$ (m/s) : dépend du milieu, **pas** de la source
  - Son dans l'air : $v \approx 340$ m/s ; dans l'eau : $\approx 1500$ m/s
- **Retard** $\tau = \frac{d}{v}$ (s) : décalage temporel entre deux points séparés de $d$
- Onde **périodique** : modèle ondulatoire se répète ; période $T$ (s), fréquence $f = \frac{1}{T}$ (Hz)
- **Longueur d'onde** : $\lambda = v \cdot T = \frac{v}{f}$ (m) — distance parcourue pendant une période
- **Diagramme espace** (à $t$ fixe) : sinusoïde de longueur d'onde $\lambda$
- **Diagramme temporel** (en un point) : sinusoïde de période $T$

---

### Chapitre 8 — Modèles de la lumière (ordre=8)

**Fichier source :** `Chapitre16_Modèles_lumiere.pdf`

**Leçons :**
- L1 : Modèle ondulatoire de la lumière
- L2 : Modèle corpusculaire — le photon

**Concepts clés :**
- **Lumière = onde électromagnétique** (pas besoin de milieu matériel)
  - Vitesse dans le vide : $c = 3 \times 10^8$ m/s
  - Spectre visible : $\lambda \in [400 \text{ nm} ; 800 \text{ nm}]$ (violet → rouge)
  - $\lambda = \frac{c}{f}$ ; $f \cdot T = 1$
- **Modèle corpusculaire** : la lumière est constituée de **photons**
  - Énergie d'un photon : $E = hf = \frac{hc}{\lambda}$ avec $h = 6{,}63 \times 10^{-34}$ J·s (constante de Planck)
  - Unité pratique : eV (électronvolt), 1 eV = $1{,}6 \times 10^{-19}$ J
- **Dualité onde-corpuscule** : la lumière se comporte comme une onde (diffraction, interférences) et comme corpuscule (effet photoélectrique)
- **Interaction lumière-matière** : absorption d'un photon → niveau d'énergie $E = hf$
  - Émission spontanée, absorption, émission stimulée (laser)
- **Spectres** : raies d'émission ou d'absorption caractéristiques d'un élément

---

### Chapitre 9 — Images et couleurs (ordre=9)

**Fichier source :** `Chapitre17_Image_et_couleurs.pdf`

**Leçons :**
- L1 : Lentille convergente et construction d'images
- L2 : Formation d'images et synthèse des couleurs

**Concepts clés :**
- **Lentille mince convergente** : distance focale $f' > 0$, vergence $V = \frac{1}{f'}$ (dioptries)
- **Foyers** : foyer image $F'$ (à droite), foyer objet $F$ (à gauche)
- **Relation de conjugaison** : $\frac{1}{\overline{OA'}} - \frac{1}{\overline{OA}} = \frac{1}{f'}$
  (avec valeurs algébriques, O = centre optique)
- **Grandissement** : $\gamma = \frac{\overline{A'B'}}{\overline{AB}} = \frac{\overline{OA'}}{\overline{OA}}$
  - $|\gamma| > 1$ : image agrandie ; $|\gamma| < 1$ : image réduite
  - $\gamma < 0$ : image renversée
- **Œil** : modèle réduit, lentille = cristallin, $f'$ variable (accommodation)
  - Punctum remotum (PR) et punctum proximum (PP)
- **Synthèse additive** (lumières colorées) : rouge + vert + bleu = blanc ; complémentaires
- **Synthèse soustractive** (pigments/filtres) : cyan + magenta + jaune = noir ; filtres absorbent

---

## Instructions d'exécution

Après génération du fichier :
```bash
docker compose run --rm --entrypoint python web manage.py seed_physique_premiere
```

Le fichier doit être enregistré dans :
`backend/courses/management/commands/seed_physique_premiere.py`
