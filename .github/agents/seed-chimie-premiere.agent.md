---
description: "Seed chimie première — Use when generating, regenerating or updating the Django management command seed_chimie_premiere.py for the Chimie Première level of ScienceLycée. Contains full curriculum documentation for 10 chapters extracted from the PDF source files in ressources/1ere/PC/. Creates Chapitre, Lecon, Quiz and Question records (20 questions per leçon) for the 'chimie' Matiere at niveau 'premiere'."
tools: [read, edit, search, execute, todo]
name: "Seed Chimie Première"
argument-hint: "Generate or update seed_chimie_premiere.py management command"
user-invocable: false
---

Tu es un agent spécialisé dans la génération du contenu pédagogique de **Chimie Première** pour ScienceLycée. Ta seule responsabilité est d'écrire le fichier `backend/courses/management/commands/seed_chimie_premiere.py`.

## Rôle

Générer une commande Django management complète qui :
1. **Supprime** tous les `Chapitre` existants de `chimie` au niveau `premiere` (cascade → Lecon, Quiz, Question)
2. **Recrée** les chapitres avec leurs leçons, quiz et 20 questions chacune, basés sur le curriculum ci-dessous

## Référence Codebase Obligatoire

1. **Lire `CODEBASE_REFERENCE.md`** (sections 1.4–1.8) en premier pour connaître la structure des modèles `Matiere`, `Chapitre`, `Lecon`, `Quiz`, `Question`.
2. **Ne lire les fichiers source** que si la structure des modèles a changé et que la référence semble obsolète.

---

## Modèles Django (référence)

```python
# Matiere : chimie (slug='chimie', couleur emeraude/emerald)
# Chapitre : matiere=chimie, niveau='premiere', ordre=1..N
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

CHIMIE_PREMIERE_DATA = [...]

class Command(BaseCommand):
    help = "Recrée entièrement les chapitres de Chimie Première."

    def handle(self, *args, **options):
        from courses.models import Matiere, Chapitre, Lecon, Quiz, Question

        chimie = Matiere.objects.get(nom="chimie")

        deleted, _ = Chapitre.objects.filter(
            matiere=chimie, niveau="premiere"
        ).delete()
        self.stdout.write(f"  🗑  {deleted} chapitres supprimés")

        for chap_data in CHIMIE_PREMIERE_DATA:
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

        self.stdout.write(self.style.SUCCESS("✅ Chimie Première recréée avec succès."))
```

---

## Curriculum détaillé — 8 chapitres

Sources : `/home/vivien/dev/persProject/ressources/1ere/PC/Chapitre1_Transformation_chimique.pdf` à `Chapitre11_Energie_reactions_chimique.pdf`

### Chapitre 1 — Suivi d'une transformation chimique (ordre=1)

**Fichier source :** `Chapitre1_Transformation_chimique.pdf`

**Leçons :**
- L1 : Tableau d'avancement et avancement maximal
- L2 : Réactif limitant et taux d'avancement

**Concepts clés :**
- **Réaction chimique** : transformation de réactifs en produits
- **Tableau d'avancement** : colonnes = espèces, lignes = état initial / en cours / état final
  - Avancement $x$ (mol), avancement maximal $x_{max}$ (réactif limitant épuisé)
- **Réactif limitant** : celui qui s'épuise en premier (donne $x_{max}$ le plus petit)
- **Réactif en excès** : toujours présent à l'état final
- **Taux d'avancement final** : $\tau = \frac{x_{final}}{x_{max}}$ ; réaction totale si $\tau = 1$
- Équation bilan équilibrée : coefficients stœchiométriques ($a$, $b$, $c$, $d$)
  $aA + bB \to cC + dD$
- Relation quantités de matière : $\frac{\Delta n_A}{a} = \frac{\Delta n_B}{b} = \frac{\Delta n_C}{c} = x$

---

### Chapitre 2 — Oxydoréduction (ordre=2)

**Fichier source :** `Chapitre2_Oxydoreduction.pdf`

**Leçons :**
- L1 : Couples oxydant/réducteur et demi-équations
- L2 : Réactions d'oxydoréduction et prévision

**Concepts clés :**
- **Oxydant** : espèce pouvant capter des électrons
- **Réducteur** : espèce pouvant céder des électrons
- **Couple Ox/Réd** (noté $\text{Ox/Réd}$) : même élément à deux degrés d'oxydation différents
- **Demi-équation électronique** :
  - $\text{Ox} + n e^- \to \text{Réd}$ (réduction)
  - $\text{Réd} \to \text{Ox} + n e^-$ (oxydation)
  - Équilibrer : charges avec $H^+$ et $H_2O$
- **Réaction redox** : addition des deux demi-équations (électrons se compensent)
  - La réaction a lieu entre l'**oxydant le plus fort** et le **réducteur le plus fort** selon la règle du gamma (γ)
- **Nombre d'oxydation** : charge fictive de l'atome si les liaisons étaient ioniques
  - Monoatomique : NO = charge de l'ion
  - Dans une molécule : $\sum NO = 0$, dans un ion polyatomique : $\sum NO = $ charge

---

### Chapitre 3 — Dosage et titrage (ordre=3)

**Fichier source :** `Chapitre3_Dosage.pdf`

**Leçons :**
- L1 : Dosage par étalonnage
- L2 : Titrage direct — équivalence et calcul

**Concepts clés :**
- **Dosage par étalonnage** : mesure d'une propriété physique (absorbance, conductivité) pour déterminer une concentration à partir d'une courbe d'étalonnage
- **Titrage** : détermination d'une concentration par réaction chimique quantitative avec un réactif de concentration connue (le **titrant**)
- **Équivalence** : toute la quantité de substance titrée a réagi avec le titrant ; $n_{\text{titré}} = n_{\text{titrant}}$ (aux coeff. stœchiométriques près)
- Point d'équivalence : détecté par changement de couleur (indicateur), saut de pH, conductimétrie ou potentiométrie
- **Calcul à l'équivalence** :
  $\frac{C_a \cdot V_a}{a} = \frac{C_b \cdot V_{b,eq}}{b}$
- **Titrage acido-basique** : $n_{H^+} = n_{HO^-}$ à l'équivalence
- **Titrage redox** : même principe avec les quantités d'oxydant/réducteur
- Courbe de titrage : pH = f(V titrant) ou E = f(V), zone équivalence = point d'inflexion

---

### Chapitre 4 — Structure et polarité des espèces chimiques (ordre=4)

**Fichier source :** `Chapitre4_Structure_polarite_especes_chimiques.pdf`

**Leçons :**
- L1 : Schéma de Lewis et géométrie des molécules
- L2 : Polarité des liaisons et des molécules

**Concepts clés :**
- **Schéma de Lewis** : représentation des liaisons covalentes et doublets non liants
  - Règles d'octet (et duet pour H, He)
  - Liaisons simples (—), doubles (=), triples (≡)
- **Méthode VSEPR** (répulsion des paires d'électrons) : géométrie 3D
  - 2 liaisons, 0 doublet libre → linéaire (180°)
  - 3 liaisons, 0 doublet libre → trigonale plane (120°)
  - 4 liaisons, 0 doublet libre → tétraédrique (109,5°)
  - 3 liaisons, 1 doublet libre → pyramidale trigonale (~107°)
  - 2 liaisons, 2 doublets libres → coudée (~104,5°)
- **Électronégativité** : aptitude à attirer les électrons dans une liaison ($\chi_{O} > \chi_{N} > \chi_{C} > \chi_{H}$)
- **Liaison polarisée** : si $|\Delta\chi| > 0,4$ → charge partielle $\delta^+$ et $\delta^-$
- **Moment dipolaire** de la molécule : vecteur somme des moments de liaison
  - Molécule **polaire** : $\vec{\mu} \neq \vec{0}$ (symétrie brisée)
  - Molécule **apolaire** : $\vec{\mu} = \vec{0}$ (symétrie totale, ex: $CO_2$, $CH_4$, $CCl_4$)

---

### Chapitre 5 — Cohésion et mélanges des espèces chimiques (ordre=5)

**Fichier source :** `Chapitre5_Cohesion_melange_especes_chimiques.pdf`

**Leçons :**
- L1 : Interactions intermoléculaires
- L2 : Miscibilité et solubilité — règle de similitude

**Concepts clés :**
- **Interactions de Van der Waals** : interactions faibles entre molécules
  - Interactions de dispersion (London) : entre toutes les molécules (charges fluctuantes)
  - Interactions dipôle-dipôle : entre molécules polaires
  - Cet ordre croissant pour les alcanes : plus la molécule est grosse, plus les interactions sont fortes
- **Liaison hydrogène** : interaction spécifique O–H···O, N–H···N, F–H···F (plus forte que VdW)
  - Explique les températures d'ébullition élevées de l'eau, de l'éthanol…
- **Cristaux ioniques** : liaisons électrostatiques entre cations et anions (ex: NaCl)
- **Solides moléculaires** : molécules maintenues par VdW
- **Règle de similitude** : les espèces de même nature d'interactions se dissolvent entre elles
  - Polaire dans polaire (eau/éthanol), apolaire dans apolaire (huile/hexane)
  - « Qui se ressemble s'assemble »
- **Solubilité** $s$ (g/L ou mol/L) : quantité maximale dissoutable

---

### Chapitre 6 — Structure des composés organiques (ordre=6)

**Fichier source :** `Chapitre6_Structure_composes_organiques.pdf`

**Leçons :**
- L1 : Groupes caractéristiques et familles organiques
- L2 : Isomérie structurale

**Concepts clés :**
- **Chimie organique** : chimie des composés du carbone (sauf CO, CO₂, carbonates)
- **Squelette carboné** : chaîne (linéaire, ramifiée) ou cyclique
- **Groupes caractéristiques** :
  - Alcool : –OH (hydroxyle) → alcane + ol
  - Aldéhyde : –CHO (carbonyle terminal) → alcanal
  - Cétone : >C=O (carbonyle interne) → alcanone
  - Acide carboxylique : –COOH → acide alcanoïque
  - Ester : –COO– → alcanoate d'alkyle
  - Amine : –NH₂ → alcanamine
  - Amide : –CONH₂
- **Nomenclature** : préfixe (nb de C) + suffixe (groupe) : méth-, éth-, prop-, but-, pent-...
- **Isomérie structurale** : même formule brute, structures différentes
  - Isomérie de chaîne (ramification différente)
  - Isomérie de position (groupe en position différente)
  - Isomérie de fonction (groupes différents)

---

### Chapitre 7 — Synthèse organique (ordre=7)

**Fichier source :** `Chapitre7_Synthese_organique.pdf`

**Leçons :**
- L1 : Estérification et hydrolyse
- L2 : Techniques de synthèse et purification

**Concepts clés :**
- **Réaction d'estérification** : Acide carboxylique + Alcool ⇌ Ester + Eau (équilibre, lente, athermique)
  - Catalyseur acide ($H^+$, $H_2SO_4$)
  - Taux d'estérification à l'équilibre ≈ 67% pour 1 mol d'acide + 1 mol d'alcool
- **Hydrolyse** : réaction inverse (ester + eau → acide + alcool)
- **Déplacer l'équilibre** (Le Chatelier) :
  - Excès d'un réactif → favorise l'estérification
  - Éliminer l'eau ou l'ester → déplace vers les produits
- **Techniques expérimentales** :
  - Chauffage à reflux : évite les pertes de réactifs volatils
  - Distillation : séparation par température d'ébullition
  - Extraction liquide-liquide : ampoule à décanter, deux phases non miscibles
  - Recristallisation : purification solide-liquide
  - Lavage : neutralisation des réactifs restants (base/acide)
- **Rendement** : $r = \frac{n_{\text{produit expérimental}}}{n_{\text{produit théorique}}} \times 100\%$

---

### Chapitre 8 — Énergie des réactions chimiques (ordre=8)

**Fichier source :** `Chapitre11_Energie_reactions_chimique.pdf`

**Leçons :**
- L1 : Énergie de liaison et enthalpie de réaction
- L2 : Combustion et pouvoir calorifique

**Concepts clés :**
- **Énergie de liaison** $E_l$ : énergie à fournir pour rompre une liaison covalente (en kJ/mol)
- **Enthalpie de réaction** $\Delta H$ :
  $\Delta H = \sum E_l(\text{liaisons rompues}) - \sum E_l(\text{liaisons formées})$
  - $\Delta H < 0$ : réaction **exothermique** (libère de la chaleur)
  - $\Delta H > 0$ : réaction **endothermique** (absorbe de la chaleur)
- **Combustion** : réaction d'un combustible avec le dioxygène
  - Combustion complète du carbone : $C + O_2 \to CO_2$
  - Combustion complète du méthane : $CH_4 + 2O_2 \to CO_2 + 2H_2O$
  - Combustion incomplète : production de CO (dangereux)
- **Pouvoir calorifique** $PCI$ : énergie libérée par la combustion complète d'une unité de masse
- **Bilan énergétique global** : somme des énergies libérées et absorbées au cours de plusieurs réactions (loi de Hess)
- Énergie massique et volumique : conversions entre kJ/mol, kJ/g, kJ/L

---

## Instructions d'exécution

Après génération du fichier :
```bash
docker compose run --rm --entrypoint python web manage.py seed_chimie_premiere
```

Le fichier doit être enregistré dans :
`backend/courses/management/commands/seed_chimie_premiere.py`
