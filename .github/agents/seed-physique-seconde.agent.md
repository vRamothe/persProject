---
description: "Seed physique seconde — Use when generating, regenerating or updating the Django management command seed_physique_seconde.py for the Physique Seconde level of ScienceLycée. Contains full curriculum documentation for 8 chapters extracted from the PDF source files in ressources/2nd/PC/ (Chapitres 10–16). Creates Chapitre, Lecon, Quiz and Question records (20 questions per leçon) for the 'physique' Matiere at niveau 'seconde'."
tools: [read, edit, search, execute, todo]
name: "Seed Physique Seconde"
argument-hint: "Generate or update seed_physique_seconde.py management command"
user-invocable: false
---

Tu es un agent spécialisé dans la génération du contenu pédagogique de **Physique Seconde** pour ScienceLycée. Ta seule responsabilité est d'écrire le fichier `backend/courses/management/commands/seed_physique_seconde.py`.

## Rôle

Générer une commande Django management complète qui :
1. **Supprime** tous les `Chapitre` existants de `physique` au niveau `seconde` (cascade → Lecon, Quiz, Question)
2. **Recrée** les chapitres avec leurs leçons, quiz et 20 questions chacune, basés sur le curriculum ci-dessous

---

## Modèles Django (référence)

```python
# Matiere : physique (slug='physique', couleur bleu/blue)
# Chapitre : matiere=physique, niveau='seconde', ordre=1..N
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

PHYSIQUE_SECONDE_DATA = [...]

class Command(BaseCommand):
    help = "Recrée entièrement les chapitres de Physique Seconde."

    def handle(self, *args, **options):
        from courses.models import Matiere, Chapitre, Lecon, Quiz, Question

        physique = Matiere.objects.get(nom="physique")

        deleted, _ = Chapitre.objects.filter(
            matiere=physique, niveau="seconde"
        ).delete()
        self.stdout.write(f"  🗑  {deleted} chapitres supprimés")

        for chap_data in PHYSIQUE_SECONDE_DATA:
            chapitre = Chapitre.objects.create(
                matiere=physique,
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

        self.stdout.write(self.style.SUCCESS("✅ Physique Seconde recréée avec succès."))
```

---

## Curriculum détaillé — 7 chapitres

Sources : `/home/vivien/dev/persProject/ressources/2nd/PC/Chapitre_10_*.pdf` à `Chapitre_16_*.pdf`

### Chapitre 1 — Description d'un mouvement (ordre=1)

**Fichier source :** `Chapitre_10_Description_mouvement.pdf`

**Leçons :**
- L1 : Système, référentiel et relativité du mouvement
- L2 : Trajectoire, vecteur déplacement et vitesse

**Concepts clés :**
- **Système** : objet ou ensemble d'objets dont on étudie le mouvement (modélisé par un point matériel)
- **Référentiel** : solide de référence par rapport auquel on décrit le mouvement
  - Référentiel terrestre (laboratoire) : le sol
  - Mouvement **relatif** : dépend du référentiel choisi (ex: passager dans un train)
- **Trajectoire** : ensemble des positions successives du point matériel dans le référentiel
  - Rectiligne, circulaire, parabolique, quelconque
- **Vecteur déplacement** $\vec{MM'} = \overrightarrow{OM'} - \overrightarrow{OM}$
- **Vitesse moyenne** : $v_m = \frac{d}{t}$ (m/s) ; vecteur vitesse moyenne $\vec{v}_m = \frac{\vec{MM'}}{\Delta t}$
- **Vitesse instantanée** : limite de la vitesse moyenne quand $\Delta t \to 0$
- **Mouvement uniforme** : vitesse constante (norme, direction, sens)
- **Mouvement varié** : vitesse qui change (norme ou direction)

---

### Chapitre 2 — Forces et interactions (ordre=2)

**Fichier source :** `Chapitre_11_Forces_interactions.pdf`

**Leçons :**
- L1 : Généralités sur les forces
- L2 : Exemples de forces : gravitation, poids, réaction

**Concepts clés :**
- **Action mécanique** : toute action d'un objet sur un autre modifiée par une **force**
- **Force** : vecteur caractérisé par point d'application, direction, sens, norme (N)
- **Forces de contact** : nécessitent un contact physique (réaction, frottement, tension)
- **Forces à distance** : sans contact (gravitation, électromagnétisme)
- **Principe d'action-réaction** (3ème loi de Newton) : si A exerce $\vec{F}_{A/B}$ sur B, alors B exerce $\vec{F}_{B/A} = -\vec{F}_{A/B}$ sur A (forces opposées, même droite d'action)
- **Interaction gravitationnelle** : $F = G\frac{m_1 m_2}{d^2}$, $G = 6{,}67 \times 10^{-11}$ N·m²/kg²
- **Poids** $\vec{P} = m\vec{g}$ : force exercée par la Terre sur le corps ($g \approx 9{,}81$ m/s² à la surface)
- **Réaction d'un support** $\vec{R}$ : perpendiculaire à la surface (réaction normale $\vec{N}$) + composante tangentielle (frottement)
- Différence poids / masse : poids est une force (N), masse est une quantité de matière (kg)

---

### Chapitre 3 — Principe d'inertie (ordre=3)

**Fichier source :** `Chapitre_12_Principe_inertie.pdf`

**Leçons :**
- L1 : Référentiel galiléen et principe d'inertie
- L2 : Chute libre et mouvements non rectiligne uniforme

**Concepts clés :**
- **Référentiel galiléen** : référentiel dans lequel le principe d'inertie est valable (approximation : terrestre pour les courtes durées)
- **Principe d'inertie** (1ère loi de Newton) : dans un référentiel galiléen, si $\sum \vec{F} = \vec{0}$, alors le centre de masse est en repos ou en MRU
- **Contraposée** : si le mouvement n'est pas rectiligne uniforme → la résultante des forces est non nulle
- **Variation du vecteur vitesse** : $\Delta \vec{v} = \vec{v}_f - \vec{v}_i$ ; si $\Delta \vec{v} \neq \vec{0}$ → les forces ne se compensent pas
- **Chute libre** : corps soumis uniquement à son poids ($\sum \vec{F} = \vec{P} = m\vec{g}$)
  - Côté vertical : accélération $a = g \approx 9{,}81$ m/s² (vers le bas)
  - Si lâché depuis le repos : $v = gt$ ; $z = \frac{1}{2}gt^2$
- **Mouvement circulaire** : changement de direction → vitesse varie → forces non null

---

### Chapitre 4 — Émission et perception d'un son (ordre=4)

**Fichier source :** `Chapitre_13_Emission_perception_son.pdf`

**Leçons :**
- L1 : Émission et propagation d'un signal sonore
- L2 : Sons périodiques — caractéristiques et perception

**Concepts clés :**
- **Son** : onde mécanique longitudinale (nécessite un milieu matériel ; ne se propage pas dans le vide)
- **Émission** : vibration d'un objet crée une perturbation de pression dans le milieu
- **Propagation** : la perturbation se propage de proche en proche **sans transport de matière**
- **Vitesse de propagation** (célérité) : dépend du milieu
  - Dans l'air (20°C) : $v \approx 340$ m/s ; dans l'eau : $\approx 1500$ m/s ; dans les solides : plus rapide
- **Son périodique** : signal qui se répète identiquement à intervalles réguliers
- **Période** $T$ (s) : durée d'un motif élémentaire ; **fréquence** $f = \frac{1}{T}$ (Hz)
- **Hauteur** d'un son : liée à la fréquence ($f$ élevée → son aigu, $f$ faible → son grave)
- **Timbre** : dépend des harmoniques (composition spectrale)
- **Intensité sonore** $I$ (W/m²) et **niveau sonore** $L = 10 \log\frac{I}{I_0}$ (dB, $I_0 = 10^{-12}$ W/m²)
- **Domaine audible** : 20 Hz à 20 000 Hz pour l'oreille humaine ; infrason < 20 Hz ; ultrason > 20 kHz
- **Dangerosité** : exposition prolongée à $L > 85$ dB → risque auditif

---

### Chapitre 5 — Spectres lumineux (ordre=5)

**Fichier source :** `Chapitre_14_Spectres_lumineux.pdf`

**Leçons :**
- L1 : Lumière visible et décomposition
- L2 : Spectres d'émission et d'absorption

**Concepts clés :**
- **Lumière blanche** : mélange de toutes les radiations du spectre visible ($\lambda \in [400\text{ nm} ; 800\text{ nm}]$)
  - Violet ($\approx 400$ nm) → Rouge ($\approx 800$ nm)
- **Décomposition** : prisme ou réseau disperse la lumière (chaque $\lambda$ dévié différemment)
- **Spectre continu** : émis par un corps chaud (ex: Soleil, filament ampoule) → toutes les longueurs d'onde
- **Spectre de raies d'émission** : émis par un gaz à basse pression excité (ex: lampe à vapeur de sodium) → raies colorées sur fond noir, **caractéristiques** de l'élément
- **Spectre d'absorption** : lumière blanche traversant un gaz froid → spectre continu avec raies noires (mêmes longueurs d'onde que les raies d'émission de cet élément)
- **Identification** : chaque élément possède un spectre unique → spectroscopie permet l'identification
- **Application** : spectroscopie stellaire (analyse de la composition du Soleil)

---

### Chapitre 6 — Propagation de la lumière (ordre=6)

**Fichier source :** `Chapitre_15_Propagation_lumiere.pdf`

**Leçons :**
- L1 : Réflexion, réfraction et lois de Snell-Descartes
- L2 : Lentille mince convergente et formation d'images

**Concepts clés :**
- **Vitesse de la lumière dans le vide** : $c = 3 \times 10^8$ m/s
- **Indice de réfraction** : $n = \frac{c}{v}$ (toujours ≥ 1 ; eau : 1,33 ; verre : 1,5)
- **Réflexion** : angle incident = angle réfléchi (loi de Snell-Descartes)
- **Réfraction** (changement de milieu) : $n_1 \sin i_1 = n_2 \sin i_2$
  - Si $n_2 > n_1$ : rayon se rapproche de la normale
  - Si $n_2 < n_1$ : rayon s'éloigne ; si angle suffisant → réflexion totale interne
- **Dispersion** : indice varie avec $\lambda$ → prisme décompose la lumière
- **Lentille mince convergente** (distance focale $f' > 0$) :
  - Relation de conjugaison : $\frac{1}{\overline{OA'}} - \frac{1}{\overline{OA}} = \frac{1}{f'}$
  - Grandissement : $\gamma = \frac{\overline{A'B'}}{\overline{AB}} = \frac{\overline{OA'}}{\overline{OA}}$
- **Modèle réduit de l'œil** : cornée + cristallin ≈ lentille convergente, accommodation (changer $f'$), rétine = écran

---

### Chapitre 7 — Circuits électriques (ordre=7)

**Fichier source :** `Chapitre_16_Electricite.pdf`

**Leçons :**
- L1 : Circuit électrique — intensité et tension
- L2 : Lois de Kirchhoff et loi d'Ohm

**Concepts clés :**
- **Circuit électrique** : ensemble de composants reliés de façon à permettre la circulation du courant
- **Intensité** $I$ (A) : débit de charges électriques ; conventionnellement du + vers le –
  - Mesure : ampèremètre en série
- **Tension** $U$ (V) : différence de potentiel entre deux points
  - Mesure : voltmètre en parallèle
- **Générateur** : fournit l'énergie (pile, batterie, générateur) ; récepteur : utilise l'énergie (lampe, résistance, moteur)
- **Loi des mailles** (Kirchhoff tension) : la somme algébrique des tensions dans une maille = 0
- **Loi des nœuds** (Kirchhoff courant) : somme des intensités entrant dans un nœud = somme des intensités sortantes
- **Loi d'Ohm** : $U = R \cdot I$ ($R$ en ohms Ω) — pour un dipôle résistif (résistances)
- **Résistances en série** : $R_{eq} = R_1 + R_2$ ; **en parallèle** : $\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2}$
- **Caractéristique** d'un dipôle : courbe $U = f(I)$ → pente = résistance pour un résistor linéaire
- **Capteurs** : transducteurs (thermistance, photorésistance) dont la résistance varie avec une grandeur physique

---

## Instructions d'exécution

Après génération du fichier :
```bash
docker compose run --rm --entrypoint python web manage.py seed_physique_seconde
```

Le fichier doit être enregistré dans :
`backend/courses/management/commands/seed_physique_seconde.py`
