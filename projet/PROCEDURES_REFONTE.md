# PROCÉDURES — REFONTE V19 (pour /projet)
### Modus JP0F K9K766 JA5 QuickShift → TL4B043 neuve · build robuste 120 ch+ · couple bridé 240-260 Nm

**Véhicule :** VF1JP0F0H43308282 · 130 000 km · extraction **moteur+boîte par l'AVANT** (cric + palette + pneu)
**Boîte :** TL4B043 **NEUVE** (Eurofrance24, OE 320109255R / 8201057476 — NE PAS OUVRIR, garantie 12 mois)
**Donneur casse :** Clio 3 Ph2 GT dCi 105 (K9K764 / TL4 002) — accessoires + train + levier/pédalier
> Note : pour la **patte alu support gauche (8200338385)** et les pièces côté caisse, un **Modus/Grand Modus dCi 105/106** (même châssis J77) est un donneur plus juste que la Clio 3 GT — à viser si dispo.
**Doc atelier :** RTA B775.5 + B700.5 · **`MODUS_JP0F_dossier_unifie.pdf`** (schémas + OE) · `freins.xps` (couples freinage)

---

## LÉGENDE DE REPÉRAGE
- **[sch.N·repX]** = schéma N° et repère X dans `MODUS_JP0F_dossier_unifie.pdf` (ex. [sch.10] = cardans).
- **OE** = référence pièce · **C =** couple en N.m · **🔴** = visserie/écrou **NON réutilisable** (neuf obligatoire) · **⚠️** = point de vigilance.

### Couples critiques (récap)
Roue C105 · écrou transmission/moyeu M16 **C280 🔴** · berceau M12 **C105** (×6) [sch.8] · support BV C62 / goujon C180 / caisse C62 [sch.5] · tampon/coiffe C62 [sch.4] · biellettes reprise couple **C105** [sch.6] · volant K9K **C65 + Loctite Frenetanch 🔴** [sch.3] · poulie vilo C2daN+115° 🔴 · chapeau bielle **C25+50° 🔴** · paliers vilo C60-67 · support étrier **C105** · colonnettes frein C32 · disque C15. Standard : M6=10·M8=25·M10=50/62·M12=105·M14=180·M16=280.

---

# PHASE 0-A — PRÉPARATION (voiture roulante → baie prête)

### ⬜ 00 — Préparation box (établi, rangement visserie par bocaux étiquetés)
### ⬜ 01 — Déconnexion cardans au parking (boîte engagée pour bloquer) [sch.10] — écrou moyeu **C280 🔴**
### ⬜ 02 — Garage + levage 4 chandelles + WD-40 sur visserie exposée
### Vidanges & purges
### ⬜ 03a — Vidange huile moteur (bouchon Corteco ✅)
### ⬜ 03b — Vidange boîte JA5 [sch.2]
### ⬜ 03c — Vidange LDR
### ⬜ 03d — Purge/vidange DOT4 (MOTUL 2 L ✅) — **se fait avec la purge embrayage/freins en fin de remontage**
### ⬜ 03d-bis — **Purge circuit gazole** [sch.16] : couper l'alim, débrancher la durite d'alimentation pompe→filtre pour vider. ⚠️ diamètre durite **à mesurer** (non donné par la notice ; réservoir 49 L, purge eau via filtre gazole).
### Dépose baie moteur
### ⬜ 03e — Dépose batterie + support + bac
### ⬜ 03f — Dépose filtre à air + boîte à air OEM
### ⬜ 03g/03h — Nettoyage baie + dessous de caisse (voir Protocole)
### Suppression QuickShift (JA5 → manuelle)
### ⬜ 04a — Dépose robot QuickShift
### ⬜ 04b — Dépose faisceau BVR
### ⬜ 04c — Dépose sélecteur QuickShift + prépa console levier 6V
### ⬜ 04d — Inspection zone pédalier [sch. pédalier MR]
> Électronique : **reprog UCH BVR→BVM** + contacteur pédale embrayage **METZGER (OE 8200276359)** — voir `elec_V18_1`.
### Habitacle
### ⬜ 24-PRE — Dépose sièges + habillages (accès plancher/pare-feu)
### ANTI-CORROSION — 5 PHASES (zones planchers/longerons [sch.41-49], essieu, cavités)
### ⬜ AC-1 — Démontage, tri, « bocal Essence F » pour visserie · agrafes garde-boue 7703077435 par **lot de 10** [sch.14]
### ⬜ AC-2 — Préparation surface (brossage, P240/P320, dégraissage acétone/IPA)
### ⬜ AC-3 — Conversion rouille FÉROSE (zones R1-R2 seulement, séchage 24 h)
### ⬜ AC-4 — Blindage époxy RESTOM EAF 2092 (2 couches, 48 h)
### ⬜ AC-5 — Infiltration interne OWATROL pur (essieu, barre antidévers, cavités)
> ⚠️ Ordre : Férose → Restom époxy (ext.) → PUIS Owatrol (int.). Visserie corrodée : **rivnut/autoperforante** si tôle non structurelle ; **rivnut M8/M10 ou boulon traversant** si structurel (jamais autoperforante).
### INSONORISATION (après corrosion, surface propre/sèche) — Reckhorn ABX-tra 2,5 mm + mousse ODIPIE
### ⬜ 24a — Portes ×4 : alubutyl centre tôle ext. (~0,8 m²) + mousse dos garniture (~1,5 m²)
### ⬜ 24b — Pare-feu CÔTÉ HABITACLE : alubutyl (~0,3 m²) + mousse (~1 m²)
### ⬜ 24c — Plancher : alubutyl ciblé + mousse (~1 m²)
### ⬜ 24d — Coffre + passages roue AR : alubutyl cloches (~0,5 m²) + mousse plancher (~1 m²)
### ⬜ 24e — Pare-feu CÔTÉ BAIE (Phase 0-B, baie vide) : alubutyl ~0,3 m², face alu visible, **0 mousse (incendie)**
### ⬜ 24f — Remontage sièges + habillages
> ⚠️ JAMAIS de mousse sur pare-feu/capot. Sous capot : alubutyl chutes + **feutre capot Modus d'origine (casse)**. Ne pas masquer trous d'évacuation / passe-fils / capteurs de choc.
### Batterie / câblage
### ⬜ 26 — Relocation batterie sous banquette AR (Maxwell 16V 100F supercap + RoyPow LiFePO4 12V 18Ah) — voir `elec_V18_1`
### ⬜ 25a/25b — Inspection câblage + masses accessibles
### ⬜ 02b/02c — Graissage + inspection sous-caisse détaillée

---

# PHASE 0-B — EXTRACTION + MAINTENANCE MOTEUR (2-3 j)

### ⬜ 05 — Démontage face avant complète [sch.15] + bouclier/déflecteur [sch.13] (C M8 25) — **libère le passage avant**
### ⬜ 06 — Extraction moteur + JA5 **par l'avant** [sch.1] : abaisser/déposer berceau [sch.8] (6× M12 **C105**), banc Mot.1453
### ⬜ 07 — Séparation moteur / JA5 [sch.3] (JA5 → revente)
### ⬜ 08 — Embrayage NEUF **Valeo 845077** (volant rigide + disque 228 + mécanisme + CSC, vis incluses) — volant **C65 + Loctite 🔴** [sch.3]
### ⬜ 09 — Distribution + pompe à eau **SKF 123 dents** (piges YATO) — poulie vilo **C2daN+115° 🔴**
### ⬜ 10 — Courroie accessoires + galets
### ⬜ 11 — Joints SPI ×3 🔴 : vilo AV **Corteco 20031906B** · vilo AR **Reinz 81-38528-00** · AAC **Reinz 81-34367-00**
### ⬜ 12 — Calorstat **AISIN THRAZ-7009**
### ⬜ 13 — Turbo **KP35 d'origine CONSERVÉ** (Phase 0)
### ⬜ 14 — ~~BV39 hybride~~ → **REPORTÉ Phase 1** · 14b — oil catch can
### ⬜ 15 — EGR nettoyage/remplacement · 16 — Contrôle injecteurs (<20 ml/min)
### ⬜ 17 — **Coussinets de bielle + vis NEUVES C25+50° 🔴** (boulons ✅ Trodo, coussinets ACL/King après inspection) — ⚠️ **point faible K9K, cœur de la fiabilisation**
### ⬜ 18 — Bougies préchauffage + graisse cuivrée · 19 — Capteur PMH Bosch
### ⬜ 20 — Supports moteur neufs + inserts **Powerflex PF-F60920 + PF-F60821** [sch.4] (✅ payé)
### ⬜ 21 — Révision alternateur · 22 — Démarreur donneur (casse) · 23 — Nettoyage bloc 360°
### ⬜ 25c — Fiabilisation câblage moteur (accès 360°)
> ⚠️ **4ᵉ point + supports raides = priorité** (volant rigide = à-coups secs). Support **fort-couple soudé** [sch.7] : à souder sur banc + traverse latérale extrême AV (pièce A) — à décider maintenant (caisse ouverte) ou réserver Phase 2.

---

# PHASE 0-C — BAIE VIDE + TL4 + RÉINSERTION + FMIC (2-3 j)

### ⬜ 24e — Insonorisation pare-feu côté baie (baie vide)
### ⬜ 27 — Présentation TL4B043 baie vide
### ⬜ 28 — Prépa TL4 (NE PAS OUVRIR) : support BV **Lemförder 37966 01** + insert **Powerflex PF-F60525** [sch.5] · patte alu sup. (casse) · contacteur MAR Febi · **MOTUL 75W-80 ~2,5 L** [sch.2]
### ⬜ 29 — Accouplement moteur + TL4 [sch.3] (Loctite 518 + biellette **Lemförder 36284 01** [sch.6] **C105**) — ⚠️ vis de cloche : côté K9K **commun** (confirmé par P2-14 « cloche identique »), longueurs à vérifier vs duster2/
### ⬜ 30 — Circuit hydraulique embrayage : émetteur **Valeo 804816** → durite **HEL CCK171** → CSC (inclus 845077) · contacteur **METZGER**
### ⬜ 31 — Réinsertion bloc **par l'avant** [sch.1]
### ⬜ 32 — FMIC **NRF 30481** sur traverse AV
### ⬜ 33 — Filtre à air Green (à commander) · 34 — Vase expansion alu 1,2 bar (à commander)
### ⬜ 35 — Cardans **SKF VKJC 6010 (G) / 6009 (D)** [sch.10] + graisse molybdène ·🔴 SPI diff **8200884113 (D)/7703087223 (G)**
### ⬜ 36 — Face avant + carrosserie (passage roue BLIC + cache moteur BLIC) [sch.13/14/15]
### ⬜ 37 — Reconnexion + câble batterie AR · 38 — Remplissages + filtres
### ⬜ 39 — Pédalier embrayage (donneur) · 40 — Émetteur Valeo 804816 · 41 — Levier 6V + câbles TL4 (donneur) · 42 — Contacteur METZGER
### ⬜ 43 — Purge hydraulique embrayage + freins (DOT4) — colonnettes **C32**, purge AV C6,5 / AR C10

---

# PHASE 0 — FREINAGE : CONVERSION DISQUE ARRIÈRE (pour CT + 120 ch+)
[sch.12] Trous de chape **présents** sur la fusée AR (photos) → **bolt-on**.
- Disque-roulement AR (×2) : **Brembo 09.9078.75** *ou* **TRW DF4274BS** (240×8, roulement+ABS) — **un seul des deux**
- Étriers : **TRW BHQ243 (AR G) / BHQ244 (AR D)** (alu, frein à main) · Chapes : **TRW BDA671 + BDA1088** · Plaquettes **GDB1330**
- Écrou + capuchon moyeu AR **🔴 NEUFS** · couples : support étrier **C105**, disque **C15**, colonnettes **C32**
> Abandonner BDA604/605 (Audi). V46-0969/0970, 178170/171, QWH205 = équivalents concurrents (ne pas cumuler).

---

# PHASE 1 — TURBO HYBRIDE + INJECTEURS + REPROG (260 Nm optimisé)
### ⬜ P1-01 — Turbo hybride **BV39 VGT** (géométrie variable) + couverture céramique + durite huile
### ⬜ P1-02 — Meilleurs injecteurs [sch.18] (injecteur OE 166001137R, vis bride 7701477646)
### ⬜ P1-03 — Reprog fine : élargir la plage, **brider couple 240-260 Nm (protection TL4)**
> Le bas moteur fiabilisé en Phase 0 (coussinets + vis 🔴) encaisse la montée en couple.

---

# PHASE 2 — SWAP K9K896 (260 Nm plat large plage) — détail dans `Tache_phase_2`
Sourcer K9K896 casse (Duster II 110-115 / Dokker / Logan II) + ECU **Bosch EDC17C84** + faisceau. **Cloche K9K identique** → accouplement TL4 direct (Loctite 518). Reprog Kess/KTAG bench. Gros turbo + meilleur démarreur.

---

# FICHIERS /projet ET RACINE À METTRE À JOUR (un par un)

| Fichier | Action |
|---|---|
| `Taches` | **Remplacer** par ce document (PROCEDURES_REFONTE V19) ou fusionner — il intègre tâches 00-43 + repérage + OE/couples |
| `Nettoyage_et_inspection` | **Supprimer** (doublon de `Protocole_préparation`, version V8 plus ancienne) |
| `Protocole_préparation` | Garder ; MAJ insonorisation **Haskyy 2mm → Reckhorn ABX-tra 2,5mm + mousse ODIPIE** |
| `AUDIT_PROJET_MODUS_V18_1` | MAJ : cardans **VKJC 6009/6010** · SPI diff **8200884113/7703087223** · support fort-couple **SOUDÉ** [sch.7] · **berceau 6 pts M12** · conversion disque AR (BHQ243/244 + BDA671/1088 + Brembo/TRW) · donneur Modus 105 (alt. patte alu) |
| `Tache_phase_2` | OK (cloche identique confirmée) ; ajouter repérage [sch.] |
| `Elect/elec_V18_1` | OK (BVR→BVM + Metzger déjà présents) |
| `ct` | Ajouter : conversion disque AR = point CT freinage |
| `Budget` / `Budget_phase_2` | Ajouter : disque-roulement AR + chapes BDA + étriers BHQ + alubutyl Reckhorn + mousse ODIPIE |
| `README` (racine) | Pointer vers `doc/` (3 PDF + dossier unifié) et `projet/` (plan + procédures V19) |

> **doc/ doit rester simple** : 3 PDF source + `MODUS_JP0F_dossier_unifie.pdf` + `MODUS_JP0F_visserie.pdf`. Sortir `00_DOSSIER_MAITRE` de `doc/` (→ remplacé par ce fichier dans projet/).
