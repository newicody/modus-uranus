# FINALISATION V19 — MODUS JP0F → TL4 — HANDOFF NOUVELLE CONVERSATION
**Synthèse de toute la conversation · état repository · nettoyage · MAJ par fichier · référentiel technique consolidé**
Véhicule VF1JP0F0H43308282 · K9K766 JA5 QuickShift → TL4B043 neuve · build robuste 120 ch+ · couple bridé 240-260 Nm · 5 juin 2026

---

## 0 — STRATÉGIE ACTUELLE (rappel, à conserver)
| Étape | Périmètre | Visée |
|---|---|---|
| **V0** | Infra : caisson sous coffre, tirages câbles V1+V2, suppression masses châssis, **anti-corrosion**, **insonorisation** | Q3 2026 |
| **V1** | Mécanique complète + élec passif → **la Modus roule** (TL4, transmission, freins AV+AR, suspension, FMIC, reprog stage 0) | Q3-Q4 2026 |
| **V2** | Architecture **iBSG 48V** (6 modules, MCU AURIX) | Q1-Q2 2027 |
| **Phase 2** | Swap **K9K896** + gros turbo (iBSG conservé) | Q3-Q4 2027+ |
> La dépose **moteur+boîte ensemble par l'AVANT** se fait en V0/V1 (caisse ouverte). Cloche K9K commune (766↔896) → swap P2 direct.

---

## 1 — ÉTAT DU REPOSITORY (carte)
**Racine** : `README.md` (point d'entrée).
**`doc/`** = base documentaire SOURCE (simple), à garder ainsi :
- `Modus_Ph2_-_815-10_FRA.pdf` (notice propriétaire — réservoir 49 L, témoin filtre gazole, masses)
- `clio3/` (Dialogys train AV/AR, fusée, cardans, pédalier, direction + `specs.md` géométrie châssis + MR385 porte-fusée)
- `duster2/` (`SCHEMAS_TL4_HD.pdf`, `boite.xps`)
- `modus jp0f dci 1.5 86ch dynamic/` : **`MODUS_JP0F_dossier_unifie.pdf`** (atlas schémas+OE+glossaire), `pb/` (MR atelier 00-91, **PartSouq** ×9 = OE par pièce, CatCar carrosserie, PR0401, `.xps` couples/procédures, `vis/` = catalogue visserie Ø×pas×long→OE)
**`projet/`** = plan + procédures + budgets + Elect/.

---

## 2 — NETTOYAGE (suppressions / corrections fichiers)
| Fichier | Problème | Action |
|---|---|---|
| `projet/Elect/Readme.md` | **Doublon exact** de `Elect/README.md` (même taille) | **SUPPRIMER** |
| `projet/elec` | Câblage **V16**, remplacé par `Elect/elec_V18_1_V1.md` | **SUPPRIMER** (ou archiver) |
| `projet/modus` | Stub 1 ligne | **SUPPRIMER** |
| `projet/Taches` | Structure Phase 0-A/B/C, remplacée par refonte + à refondre V0/V1/V2 | **Archiver** → remplacer par refonte alignée (voir §3) |
| `doc/.../pb/*.zip` (cour, etanche, freins, supo, vidangediesel, buteeedeprep, moto, rivets) | **Doublons** des `.xps` (sources) | **SUPPRIMER** (garder les `.xps`) |
| `doc/.../pb/rtacomp.pdf` | Doublon données garde-boue (= PartSouq « Protections passage de roue ») | **SUPPRIMER** |
| `doc/.../pb/0893D.pdf` | Doublon de `91 - Note technique rouge 0893D` | Vérifier puis supprimer un |
| `doc/.../duster2/up` · `vis/ref` (vide) · `photos/phots` (1 o) | Fichiers parasites | **SUPPRIMER** |
| `GUIDE_INTEGRATION_V18_1.md` | Cité « livré » dans l'AUDIT mais **ABSENT** du repo | À créer ou retirer la référence |
> Note : `ARPCatalog.pdf` déjà retiré ✅. `Nettoyage_et_inspection` déjà supprimé ✅.

---

## 3 — MISE À JOUR PAR FICHIER (patches précis)

### `AUDIT_PROJET_MODUS_V18_1.md`
- **Action #2** « Sourcer fusées AR version disque » → **RÉSOLU** : trous de chape **présents** sur la fusée AR (photos) → conversion **bolt-on**, pas de fusée spécifique. Remplacer par : *« Conversion disque AR validée : disque-roulement Brembo 09.9078.75 ou TRW DF4274BS (240×8, roulement+ABS) + chapes TRW BDA671/BDA1088 + étriers TRW BHQ243(G)/BHQ244(D) + plaquettes GDB1330. Écrou+capuchon moyeu NEUFS. »*
- **Action #1** BDA604/605 → confirmer fait (incompatibles Audi).
- Ajouter au §mécanique les **réfs/corrections validées** :
  - Cardans **SKF VKJC 6010 (G) / 6009 (D)**
  - SPI sortie diff TL4 **8200884113 (D) / 7703087223 (G)** · bouchon vidange joint cuivre **331729798R** · huile **75W-80 ~2,5 L**
  - **Berceau = 6 points M12** (vis H embase 7703602210/212/251/266) · berceau 8200766078 + traverse 8200537419
  - **Support moteur fort couple = SOUDÉ** (planche 30 : banc de réparation + traverse latérale extrême AV) — décider V0 (caisse ouverte) ou Phase 2
  - **Vis de cloche** : réfs PartSouq = boîte **JA5** (goujon 7703027524, vis embase 7703002709/710/751) ; côté K9K commun → réutilisables TL4, longueurs à vérifier vs `duster2/`
  - **4ᵉ point (biellette sup.)** : hard-point caisse (R, M12) existe (specs.md) ; priorité fiabilité avec volant rigide

### `PROCEDURES_REFONTE.md` (déjà committé) — réaligner sur V0/V1/V2
Mapping des tâches refonte vers la stratégie actuelle :
- **V0** = tâches 03d-bis (purge gazole), 03g/h (nettoyage), AC-1..5 (corrosion), 24a-f (insonorisation), 26 (batterie), tirages câbles, suppression masses.
- **V1** = tâches 05-43 (extraction par l'avant, embrayage Valeo, distrib SKF, SPI, coussinets 🔴, supports, accouplement TL4, réinsertion, FMIC, conversion disque, conversion manuelle, purges).
- **Phase 2** = swap K9K896 (`Tache_phase_2`).
Conserver le **repérage [sch.N·rep] + OE + couple + 🔴 single-use**.

### `Protocole_préparation` + `renovation_V18_1.md` — INSONORISATION (incohérence à trancher)
L'AUDIT/Protocole disent **HASKYY alubutyl 2 mm** ; le dernier plan validé en conversation est **Reckhorn ABX-tra 2,5 mm + mousse ODIPIE + feutre capot d'origine**. → **Aligner sur Reckhorn 2,5mm + ODIPIE** (plan de coupe par zone dans `dossier_unifie` §V). Règles : corrosion traitée AVANT, jamais d'alubutyl sur tôle nue/rouillée, **zéro mousse pare-feu/capot** (incendie), ne pas masquer évacuations/passe-fils/capteurs de choc.

### `ct`
Ajouter : **conversion disque AR** = point CT freinage (équilibrage AV/AR, frein de stationnement sur étriers BHQ).

### `Budget` / `Budget_phase_2` (action #11 — à refondre V0/V1/V2)
Ajouter lignes : disque-roulement AR ×2 + chapes BDA671/1088 + étriers BHQ243/244 + plaquettes GDB1330 ; alubutyl Reckhorn ABX-tra (~2 m²) + mousse ODIPIE (4-5 m²) + feutre capot casse ; agrafes 7703077435 (lots de 10) ; consommables visserie M6/M8/M12 + rivnuts.

### `README.md` (racine)
Pointer clairement : `doc/` (sources + `dossier_unifie.pdf`) · `projet/` (AUDIT V18.1 = maître, `PROCEDURES_REFONTE` = procédures, `Elect/` = électrique/iBSG).

---

## 4 — RÉFÉRENTIEL TECHNIQUE CONSOLIDÉ (source unique de vérité)

### Boîte / donneur
TL4B043 **neuve** OE **320109255R / 8201057476** (ne pas ouvrir). Donneur Clio 3 GT dCi 105 (accessoires/train) ; **Modus 105/106** préférable pour patte alu **8200338385** (même châssis J77). Démarreur **Modus stock reconditionné** (décidé). Rapports TL4 043 : 1=3,73 / 2=1,95 / 3=1,32 / 4=0,975 / 5=0,763 / 6=0,638 · couple conique 16/71=4,44 → correction tachymétrique obligatoire.

### Couples critiques (N.m)
Roue 105 · écrou moyeu M16 **280 🔴** · berceau M12 **105** (×6) · support BV 62 / goujon 180 / caisse 62 · tampon/coiffe 62 · biellettes 105 · volant K9K **65 + Loctite 🔴** · poulie vilo 2 daN+115° 🔴 · bielle **25+50° 🔴** · paliers vilo 60-67 · support étrier 105 · colonnettes 32 · disque 15. Std : M6=10·M8=25·M10=50/62·M12=105·M14=180·M16=280.

### Visserie OE (PartSouq) — par organe
- **Cloche/embrayage (JA5)** : goujon 7703027524 · vis embase 7703002710/2709/2751 · écrou H 7703033148 · vis carter M8×125 7703101443
- **Train avant** : 6× vis H embase M12 7703602210/212/251/266 · vis RLX 7703008192
- **Protecteur sous moteur** : 7703019211 · 7703017096 · 7703602209 · écrou M12 7703034257 · rivet 054000001R · 7703072337
- **Gardes-boue** : agrafe 7703077435 (lot 10) · vis 7703017090 · écrou Ø5 7703041045 (≥060619)/7703034260 · rivet 7703072361 · écrou plast. 7703081199
- **Décodeur visserie standard** (`vis/`) : Ø×pas×long×classe → OE (ex. vis M6×100×35 cl.10.9 = 7703009041 · écrou H M12×150 = 5003032197)

### Étanchéité 🔴
SPI diff 8200884113/7703087223 · SPI vilo AV Corteco 20031906B / AR Reinz 81-38528-00 / AAC Reinz 81-34367-00 · joint bouchon 331729798R.

### Freinage
AV 260 mm ABS (FEBI/TRW, Clio 3 GT) · **AR conversion disque** : Brembo 09.9078.75 *ou* TRW DF4274BS (240×8 roulement+ABS) + chapes BDA671/1088 + étriers BHQ243/244 + plaquettes GDB1330 + roulement SKF VKBA 3596 · flexibles Goodridge/HEL. Abandonner BDA604/605.

### Liaison sol / supports
Cardans VKJC 6009/6010 · fusées AV neuves VAICO · roulement SKF VKBA 3596 · suspension Bilstein B8 + Eibach Pro-Kit + Powerflex ×6 · jantes JR-7 16" + 195/55 R16 · support BV Lemförder 37966 01 + Powerflex PF-F60525 · biellette inf. Lemförder 36284 01 · supports moteur Powerflex PF-F60920/821 · **4ᵉ point** + support fort-couple soudé (option robustesse).

### Moteur (fiabilisation K9K)
Embrayage Valeo 845077 (volant rigide, CSC) + émetteur Valeo 804816 + durite HEL CCK171 + contacteur Metzger (OE 8200276359) · distrib SKF 123 dents · calorstat Aisin THRAZ-7009 · **coussinets ACL/King + vis bielle NEUVES 🔴 (point faible K9K)** · FMIC NRF 30481 · KP35 (V1) → BV39 VGT (Phase 1) → K9K896 + EDC17C84 (Phase 2).

### Conversion QuickShift → manuelle
Reprog **UCH BVR→BVM** + contacteur Metzger + pédalier/levier 6V donneur (déjà couvert `elec_V18_1_V1.md`).

### Carburant / divers (notice 815-10)
Réservoir **49 L** · purge eau via filtre gazole · **durite pompe gazole : diamètre à MESURER** (non donné par la notice). Roue 105 N.m.

### Index schémas (`dossier_unifie.pdf`)
1 ensemble moteur-boîte · 2 carters BV · 3 embrayage/cloche · 4 pend. D · 5 pend. G · 6 biellette inf · 7 support fort-couple soudé · 8 train AV/berceau · 9 fusée AV · 10 cardans · 11 train AR · 12 fusée AR/disque · 13 bouclier+déflecteur · 14 gardes-boue · 15 face avant · 16 réservoir · 17 ouvrants · 18 injecteurs · 41-49 carrosserie/planchers.

---

## 5 — POINT DE DÉPART NOUVELLE CONVERSATION (à coller)
> Projet Modus JP0F (K9K766 JA5) → TL4B043 neuve, build robuste 120 ch+, couple bridé 240-260 Nm. Stratégie **V0 (infra/corrosion/iso) → V1 (mécanique+élec passif, roulante) → V2 (iBSG 48V) → Phase 2 (K9K896)**. Dépose moteur+boîte par l'avant. Repo `newicody/modus-` : `doc/` = sources + `MODUS_JP0F_dossier_unifie.pdf` (schémas+OE+glossaire) ; `projet/` = `AUDIT_PROJET_MODUS_V18_1.md` (maître), `PROCEDURES_REFONTE.md` (procédures repérées [sch.N·rep]+OE+couples+🔴), `Elect/` (iBSG/câblage). Conversion disque AR validée (BHQ243/244+BDA671/1088+Brembo/TRW). Voir `FINALISATION_V19.md` pour le référentiel technique consolidé.

### Restant prioritaire pour la prochaine session
1. Refondre **Budget V0/V1/V2** (action #11) et **Taches V0/V1/V2** (action #12) en intégrant la refonte.
2. Trancher l'insonorisation (Reckhorn 2,5mm + ODIPIE retenu).
3. Vérifier supports étrier AV ABS 260 mm + kit Goodridge AV+AR (actions #8/#9).
4. Mesurer emplacement roue de secours (caisson V0, action #3).
5. Créer `GUIDE_INTEGRATION_V18_1.md` (cité mais absent) ou retirer la référence.
6. Vis de cloche TL4 : relever longueurs côté `duster2/` (vs JA5).
