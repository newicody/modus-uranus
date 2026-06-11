# SPEC — modus-uranus populate (v3)

Outil unifié de gestion + visualisation du projet Modus Uranus, alimenté par les fichiers du repo..
**Vue principale : Atelier** (réaliste) — la voiture en 3D, taxonomie mécanique réelle. Accent misé sur le process de réparation et le controle des opération et le respect des opération réglementaires ainsi que la detection d'erreurs/défaillances/risques/choix/procédures non conformes... (c'est a dire l'action du mécanicien et de ce qu'on sait sur ce qu'il fait/rapporte/choisis)
*(La vue « City » — voiture en ville sur Uranus — est **reportée** : elle se fera plus tard via une **ROM Megadrive SGDK** tournant sur la voiture + une couche d'interaction navigateur.)*

---

## 1. Taxonomie réaliste — Mode Atelier (mécanique pure)

Plus de métaphore ici (la métaphore ville est **reportée** — cf. note en tête). Systèmes auto réels :

| Système | Sous-systèmes | Données |
|---|---|---|
| Groupe motopropulseur (K9K766) | bloc, distribution, injection, suralimentation, lubrification | `organes_mecaniques.csv` |
| Transmission | embrayage, BV TL4, différentiel, cardans | `organes_mecaniques.csv` |
| Liaison au sol / suspension | triangles, fusées, roulements, amortisseurs, ressorts, barre stab | *liaison_sol.csv* |
| Direction | crémaillère, rotules, colonne | *direction.csv* |
| Freinage | étriers, disques, plaquettes, maître-cylindre, flexibles | *freinage.csv* |
| Échappement & dépollution | collecteur, ligne, EGR | *echappement.csv* |
| Refroidissement & thermique | radiateur, GMV, thermostat, clim | *thermique.csv* |
| Fluides | LDR, huile, gasoil, liquide de frein, lave-glace | *fluides.csv* |
| Habitacle & confort | sièges, console, sellerie, clim | *habitacle.csv* |
| Carrosserie & structure | caisse, berceau, ouvrants, boucliers, étanchéité, insono | *carrosserie.csv* |
| Sécurité | airbags, ceintures, ABS/ESP, absorbeurs de choc | *securite.csv* |
| Électrique / électronique | → réseaux ci-dessous | `reseau_*.csv` |

### Réseaux électriques — gardés séparés + ajout des typiques automobiles
| Réseau | Rôle | Source |
|---|---|---|
| **12V** puissance/servitudes | batterie, alternateur, fusibles, consommateurs | `reseau_12v.csv` |
| **48V** iBSG | hybridation légère | `reseau_48v.csv` |
| **5V** | capteurs / glovebox / USB | `reseau_5v_glovebox.csv` `reseau_5v_usb.csv` |
| **3V3** | logique | `reseau_3v3.csv` |
| **CAN bus** (H/L) ⊕ | multiplexage moteur ↔ habitacle | *reseau_can.csv* |
| **LIN bus** ⊕ | capteurs/actionneurs lents | *reseau_lin.csv* |
| **Masse / ground** ⊕ | réseau de masse (souvent oublié, critique) | *reseau_masse.csv* |
| **Éclairage / signalisation** ⊕ | feux, clignotants | *reseau_eclairage.csv* |
| **Diagnostic / K-line (OBD)** ⊕ | prise diag, lignes K | *reseau_diag.csv* |
| **15kw plasma haute fréquence-- | amélioration du coefficient de trainé au maximum pas 0.15!!!| option @maginale rouge gazon (le plus tard possible) prévoir menu spéciale mais pas maintenant reparle en un jour j'essaye d'oublier.
⊕ = réseaux typiques à ajouter.

---

## 2. Modèle de données — divisé + standard automobile

- **On NE fusionne PAS.** Un CSV par système/réseau (comme aujourd'hui).
- **Schéma standard inspiré TecDoc** (le standard des catalogues européens, Oscaro/Autodoc) : logique `groupe de montage → article générique → article (OE + critères)`. Colonnes de base communes à tous les CSV :
  `id, nom, systeme, sous_systeme, X, Y, Z, zone, ref_oe, ref_montee, etat, phase, couple_nm`
  - **etat** : `origine | déposée | nettoyée | traitée | à_changer | montée`
  - **phase** : `V0 | V1 | V2 | P2`
- **Tables auxiliaires injectées par système** (pas fusionnées), liées par `id` : `*_couples`, `*_photos`, `*_historique`. Chaque système garde ses spécificités sans alourdir le tronc commun.
- **Tables transverses :**
  - `cameras.csv` : `id, nom, X, Y, Z, cible_X, cible_Y, cible_Z, pieces_surbrillance, youtube_url(optionnel), commentaire`
  - `historique.md` : métadonnées photos/infos/plans par `piece_id` (N-N : une photo peut viser plusieurs pièces).
  - `budget.csv`, `taches.csv`, `fournisseurs.csv` : **dérivés** (sync des `.md` de `projet/`).

---

## 3. Validation des données (nos données **prépondérantes** sur TecDoc)

**Nos données = source de vérité** ; TecDoc sert de **contre-référence** pour recouper → **double validation** (toi + IA/TecDoc).

**Bouton « Validate »** sur une pièce / un groupe / une entrée d'historique :
- interroge les IA en comparant **nos données** à TecDoc (OE, montage, cohérence cône/couple…) ;
- vérifie qu'une **modification d'historique** est plausible (« serrage au couple bien noté ? pièce montée cohérente ? ») ;
- peut s'appuyer sur des **photos de preuve** (serrage au couple, montage) attachées à la pièce → réduit les erreurs ;
- résultat : ✅ cohérent / ⚠️ à vérifier / ❌ conflit + motif. **Toi seul valides** ; l'IA conseille.

## 4. Onglets & navigation

**Onglets :** `Atelier` (3D réaliste) · `Photos` · `Budget` · `Tâches` · `Fournisseurs`.

**Navigation Atelier :**
1. **Par système / réseau** : filtrer → pièces en 3D + liste. Clic pièce → **surbrillance** immédiate + panneau droit.
2. **Par localisation = CAMÉRA VIRTUELLE (prioritaire)** : se placer (« devant la roue ») → voir tous les systèmes à cet endroit **ou** isoler une pièce, superposer d'autres systèmes, avec schémas + infos. C'est le cœur de la navigation.

**Panneau droit (clic pièce/groupe) :** réf OE + réf montée, état, phase, couple, **historique photos**, **plan/schéma**, **commentaires** éditables.

**Flux vidéo YouTube = option SECONDAIRE** (à brancher plus tard sur les caméras). La caméra **virtuelle** (localisation) est le besoin réel.

---

## 5. IA — répartition des moteurs

- **DeepSeek + Gemini (serveur local)** → mises à jour **rapides/en masse** des fichiers git : édition de CSV, génération de lignes, parsing, sync `.md`→`.csv`. Routine et volume.
- **Claude Pro** → **analyse des images** (vision) : reconnaissance pièce sur photo + commentaire → mapping vers `historique.md`. Intégration dans le mode atelier de la prise de photo selon l'opération effectuée exemple : serrage au couple : photo ou video + son, montage de piece, vérification temp réel de l'action effectuée, check liste a valider soit meme dans l'atelier puis controlée, a la fin on vérifie l'ensemble des opération quand on a cliqué fin de l'intervention
- **Claude (backend)** → **modifications avancées** : architecture, refonte, raisonnement complexe (ce projet).
- Dans tous les cas : l'IA **propose**, tu **valides** ; édition manuelle toujours possible.

---

## 6. Réorganisation `projet/` (compatibilité outil)

```
ia/populate/
  atelier.html            ← vue 3D réaliste (ex p2p6, généré)
  data/
    <systeme>.csv          ← un CSV par système/réseau (NON fusionnés)
    <systeme>_couples.csv  ← tables auxiliaires par système
    <systeme>_photos.csv
    cameras.csv
    historique.md
    budget.csv / taches.csv / fournisseurs.csv  ← dérivés
  plans/                   ← schémas RTA/PartSouq extraits
photos/                    ← toutes les photos centralisées
projet/                    ← docs humains .md (SOURCE des dérivés)
```
- `projet/`, `fournisseurs/`, `taches`, `ct`… restent en **markdown `.md`** (compatibilité GitHub) — c'est la source ; l'outil lit les `.csv` dérivés. Renommer juste les fichiers sans extension (`Budget`, `Fournisseurs`…) en `.md`.

---

## 7. Manques relevés (déjà intégrés)

1. **Filtre PHASE V0/V1/V2/P2** transversal (pièces/tâches/budget).
2. **État + workflow rénovation** par pièce (lié `ia/corrosion`, `ia/boulons`).
3. **Photo↔pièce en N-N** (une photo = plusieurs pièces).
4. **Écriture git** : un navigateur ne pushe pas → outil **local** (génère/lit les fichiers) + éditions **exportées** pour recommit (ou via le serveur DeepSeek/Gemini local).
5. **Recalage des coordonnées** édition manuelle si base pas bien renseignée.
6. **Recherche** par nom/OE.
7. **Couples** en overlay (moyeu 280, triangle 90+90°…).
8. **Inventaire Casse (donneur)**, **Outillage**, **Entretien** : filtres/onglets.
9. **Index des plans** liés aux pièces.

---

## 8. PDF impression (plans + nomenclatures)

Généré depuis la **même source** (les CSV par système) → cohérence garantie, **splittable/parsable** :
- 1 section par **système** (titre + pagination), avec son **schéma/éclaté** + **tableau nomenclature** (OE | montée | état | phase | couple | prix).
- Annexes : couples critiques, budget par phase, fournisseurs.
- A4, marges propres, 1 pièce = 1 ligne. Régénéré en relisant le git.

---

## 9. Roadmap

- **A — Données** : standardiser les CSV **divisés** (schéma TecDoc-like + colonnes système/phase/état/montée), créer les CSV systèmes manquants + réseaux typiques, `cameras.csv` + `historique.md`, réorg `projet/`.
- **B — Atelier 3D** : nav système + **caméra virtuelle**, clic→surbrillance, panneau droit (photos/plan/commentaires).
- **C — Onglets** : Photos, Budget, Tâches, Fournisseurs (dérivés des `.md`).
- **D — Caméras** : option vidéo YouTube secondaire.
- **E — IA images** : Claude vision (mapping pièces) + bouton Validate.
- **F — PDF** impression.

→ Démarrage **Phase A** après validation.
