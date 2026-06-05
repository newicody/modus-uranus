# Projet Modus JP0F → TL4 — Build robuste 120 ch+

**Véhicule :** Renault Modus 1.5 dCi 86 ch Phase 2 (2008) — **VF1JP0F0H43308282**
Moteur **K9K766** · boîte d'origine **JA5 QuickShift** → conversion **TL4B043 manuelle 6 rapports (neuve)** · 130 000 km
**Objectif :** fiabilisation totale + montée en puissance maîtrisée, **couple bridé boîte 240-260 Nm**, contrôle technique OK.

---

## Stratégie (V0 → V1 → V2 → Phase 2)
| Étape | Périmètre | Visée |
|---|---|---|
| **V0** | Infrastructure : caisson sous coffre, tirages câbles V1+V2, suppression masses châssis, **anti-corrosion**, **insonorisation** | Q3 2026 |
| **V1** | **Mécanique complète + élec passif → la Modus roule** (TL4, transmission, freins AV+AR, suspension, FMIC, reprog stage 0) | Q3-Q4 2026 |
| **V2** | Architecture **iBSG 48V** (6 modules custom, MCU AURIX) | Q1-Q2 2027 |
| **Phase 2** | Swap **K9K896** + gros turbo (iBSG conservé) | Q3-Q4 2027+ |

> Dépose **moteur + boîte ensemble par l'AVANT** (cric + palette + pneu), en V0/V1 caisse ouverte. Cloche K9K commune (766↔896) → swap Phase 2 direct.

---

## Organisation du dépôt

### `doc/` — base documentaire SOURCE (ne pas alourdir)
- **`modus jp0f dci 1.5 86ch dynamic/MODUS_JP0F_dossier_unifie.pdf`** ⭐ — atlas démontage : schémas + nomenclatures OE + couples + glossaire (référence principale terrain)
- `…/pb/` — MR atelier (00-91), **PartSouq** ×9 (OE par pièce), CatCar (carrosserie), `vis/` (catalogue visserie Ø×pas×long→OE), `.xps` (couples/procédures, ex. `freins.xps`)
- `clio3/` — Dialogys train AV/AR, fusée, cardans, pédalier + `specs.md` (géométrie châssis) + MR385 porte-fusée
- `duster2/` — schémas TL4 (`SCHEMAS_TL4_HD.pdf`, `boite.xps`)
- `Modus_Ph2_-_815-10_FRA.pdf` — notice propriétaire (réservoir 49 L, témoin filtre gazole, masses)

### `projet/` — plan, procédures, budgets
- **`AUDIT_PROJET_MODUS_V18_1.md`** — audit/plan maître (stratégie V0/V1/V2)
- **`PROCEDURES_REFONTE.md`** — procédures repérées `[sch.N·rep]` + OE + couples + 🔴 single-use
- **`BUDGET_REFONTE_V19.md`** — budget par version V0/V1/V2 + Phase 2
- **`FINALISATION_V19.md`** ⭐ — référentiel technique consolidé (toutes les réfs OE/couples/donneur/géométrie) + nettoyage + handoff
- `Casse`, `Fournisseurs`, `Entretient(_phase_2)`, `Outils(_audit)`, `ct`, `Tache_phase_2`
- `Elect/` — architecture iBSG 48V, câblage V1 (`elec_V18_1_V1.md`), confort, mécanique, rénovation

---

## Décisions actées
- Boîte **TL4B043 neuve** (Eurofrance24, OE **320109255R / 8201057476**) — ne pas ouvrir (garantie).
- Donneur casse **Clio 3 Ph2 GT dCi 105** (K9K764/TL4 002) ; **Modus 105/106** préférable pour la patte alu support gauche (8200338385, même châssis J77).
- Embrayage **Valeo 845077** (volant rigide) + émetteur Valeo 804816 + contacteur Metzger + reprog **UCH BVR→BVM** (suppression QuickShift).
- **Démarreur Modus stock reconditionné** (pas Clio GT).
- Batterie **EverExceed LiFePO4 12V 8Ah** + supercondos Maxwell 16V 100F, relocalisés caisson AR.
- **Conversion disque arrière** (CT + 120 ch+) : **bolt-on** (trous de chape présents).

---

## Corrections importantes (appliquées / à appliquer)
- 🔴 **Disques de frein** : « Disques AV TRW DF4274BS » = en réalité **disque ARRIÈRE 240mm**, doublon des Brembo 09.9078.75 (AR). → retirer 1 jeu AR + **ajouter vrais disques AVANT 260mm**.
- Étriers AR = **TRW BHQ243 (G) / BHQ244 (D)** ; chapes = **BDA671 + BDA1088** ; disque AR = Brembo 09.9078.75 **ou** TRW DF4274BS (un seul). Abandonner BDA604/605 (Audi).
- **Fusées AR** : conversion bolt-on → **aucune fusée AR à acheter/récupérer** (mettre à jour `Casse`).
- Cardans **SKF VKJC 6010 (G) / 6009 (D)**. SPI sortie diff TL4 **8200884113 (D) / 7703087223 (G)**.
- **Berceau = 6 points M12** (7703602210/212/251/266). **Support moteur fort couple = SOUDÉ** (banc + traverse pièce A).
- **Insonorisation** : **Reckhorn ABX-tra 2,5mm + mousse ODIPIE + feutre capot casse** (remplace HASKYY) — corrosion traitée d'abord, 0 mousse pare-feu/capot.
- Remplacer **RoyPow 18Ah** par **EverExceed 8Ah**.

---

## Statut & priorités prochaine session
1. Refondre **Taches** au format V0/V1/V2 (intégrer `PROCEDURES_REFONTE`).
2. Acheter **disques AV 260mm** + 2ᵉ chape AR **BDA1088** ; retirer doublons panier.
3. Vérifier supports étrier AV ABS 260mm + kit Goodridge AV+AR.
4. Mesurer emplacement roue de secours (caisson V0).
5. Relever longueurs **vis de cloche TL4** côté `duster2/` (réfs PartSouq = JA5).
6. (Option) créer `GUIDE_INTEGRATION_V18_1.md` ou retirer sa référence dans l'AUDIT.

---
*Détails techniques complets : voir `projet/FINALISATION_V19.md`. Dernière mise à jour : 5 juin 2026.*
