# BUDGET — ANALYSE & MISE À JOUR V20 (10 juin 2026)

Mise à jour de `Budget.md` après vérifications de cette session.

---

## 1. Où on en est — PAYÉ À CE JOUR : **1 375,23 €**
> Le tableau « 1 087 € » en tête de `Budget.md` est **obsolète** : il oublie ManoMano + Amazon (listés plus bas dans le même fichier).

| Fournisseur | Détail | € | Version |
|---|---|---|---|
| Eurofrance24 | TL4B043 neuve + livraison | 531,79 | V1 |
| GT2i | Powerflex ×6 | 392,40 | V1 |
| Norauto ×3 | Outillage (chandelles, extracteur, clés…) | 162,88 | Outillage |
| ManoMano | Clé dynamo 30-345 Nm + clé angulaire + mousse | 89,80 (+ mousse à chiffrer) | Outillage/V0 |
| Amazon | SPI Corteco + Loctite + LiFePO4 8Ah + clips + Férose + Owatrol + Reckhorn | 198,36 | V0/V1 |
| **TOTAL PAYÉ** | | **1 375,23 €** (+ mousse ManoMano) | |

---

## 2. ✅ Freins résolus — AV 260 + AR 240 (ta correction #1 tombe)

**Brembo 09.9078.75 = disque AVANT 260×22 mm ventilé/rainuré** (gamme Brembo Max/Xtra), et il **monte sur le Modus 1.5 dCi 86 cv**.

Conséquences :
- Tu n'as **PAS** de disque avant manquant → **le 09.9078.75 EST ton disque avant** (~49-83 €). La ligne « disques AV 260 mm à ajouter 50-80 € » **disparaît**.
- Côté **arrière** (conversion disque) = **TRW DF4274BS** : disque **240×8 mm, plein, AVEC roulement de roue + bague ABS intégrés**, 4×100, centrage 52,3 — c'est **exactement** le disque AR de conversion. Équivalents : Brembo 08.A141.17 / SKF VKBD1015.
- ⚠️ Prendre la version **AVEC roulement** (DF4274**BS**), **pas** DF4274S (sans roulement).
- **Donc AUCUN doublon** : 09.9078.75 = AV 260, DF4274BS = AR 240 → deux essieux, **les deux nécessaires**. La « correction #1 » tombe : tu gardes les deux, **rien ne manque**.

---

## 3. Pièces verrouillées cette session (deltas vs `Budget.md`)

| Poste | `Budget.md` | Verrouillé V20 | Note |
|---|---|---|---|
| Triangles AV ×2 | MEYLE 125,98 | **Lemförder 29699 01 / 29700 01** | pas de MEYLE-HD pour ce bras → premium ; prix ~140-180 (à confirmer) |
| Rotule axiale int. ×2 | MEYLE 16-160310015 (**annulée**) | **Lemförder 29465 01** *(ou MEYLE-HD MAR0497HD)* | re-sourcer ~60-90 |
| Rotule direction ext. | MEYLE M14×1.5 | **MEYLE-HD 16-16 020 0011 / 0012** | HD dispo |
| Plaquettes AV | Brembo P68033X 45,49 | **TRW GDB1614** *(réf `train_avant_V19`)* | vérifier P68033X vs GDB1614 |
| Étriers AV | FEBI 125,48 | **FEBI 178170 / 178171** [OE 7701208332/333 TRW] | ✓ confirmé |
| Chape étrier AV | TRW 64,98 | **FEBI 198806** [OE 7701059704] | ✓ |
| Biellette stab AV | MEYLE 88,12 | **MEYLE-HD 35-16 060 0021/HD** [551107916R] | ✓ |
| Amortisseur AV | Bilstein 35-128649 | confirmé [OE 8200675732] | ✓ |
| Disque AV | (cru manquant) | **Brembo 09.9078.75** (260 ✓ 86cv) | ✓ résolu |

---

## 4. Restant à commander (mis à jour, priorité V0 → V1)

1. ~~Disques AV 260 mm~~ → **RÉSOLU** (= Brembo 09.9078.75, ton disque avant).
2. **Disque AR 240 roulement+ABS ×2** = **TRW DF4274BS** (avec roulement, ou Brembo 08.A141.17 / SKF VKBD1015) — **déjà au budget** ✓
3. **Triangle Lemförder ×2** (remplace MEYLE) — ~140-180 €
4. **Rotule axiale Lemförder 29465 01 ×2** (remplace MEYLE annulée) — ~60-90 €
5. 2ᵉ chape étrier AR **BDA1088** — ~66 €
6. Pneus 195/55 R16 ×4 — 280-320 €
7. Insono Reckhorn + ODIPIE + feutre capot — 80-115 €
8. Matériaux caisson + câbles V1/V2 — 220-470 €
9. Pièces casse (levier/pédalier/câbles + patte alu) — 100-300 €
10. Coussinets de bielle (après inspection) — 40-80 €
11. Démarreur recond (charbons/bagues) — 20-40 €

> À retirer du panier : RoyPow 18Ah, BDA604/605, ligne « fusées AR version disque ». **Plus de doublon disque** : AV 260 + AR 240 = deux axes, les deux gardés.

---

## 5. Totaux par phase (corrigés)

| Étape | € mini | € maxi |
|---|---|---|
| **Payé à ce jour** | **1 375** | **1 375** |
| V0 Infra (restant) | ~440 | ~700 |
| V1 Roulante (restant) | ~3 600 | ~4 100 |
| V2 iBSG 48V | 1 110 | 2 800 |
| Phase 2 K9K896 | 1 860 | 3 935 |
| **TOTAL PROJET** | **~8 400** | **~12 900** |
| **dont reste à dépenser** | **~7 000** | **~11 500** |

Ajustements vs `Budget.md` : +triangle Lemförder, +rotule axiale re-sourcée, −« disque AV manquant » (n'existait pas). Le payé réel (1 375) corrige le 1 087 du tableau de tête.
