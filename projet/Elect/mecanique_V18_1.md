# ARCHITECTURE MÉCANIQUE V18.1 — MODUS JP0F

**Véhicule :** VF1JP0F0H43308282 — Renault Modus 1.5 dCi K9K766
> Architecture mécanique complète Phase 0 (V1 fait rouler) + perspective Phase 2 (K9K896).
> Document de référence pour l'exécution mécanique.

---

## 0 — VISION D'ENSEMBLE

L'architecture mécanique est structurée en sous-systèmes interdépendants. Cette représentation par couches permet de comprendre comment chaque modification s'intègre au système global et quelles sont les contraintes/dépendances.

**Limite globale du projet** : TL4B043 plafonne à 260 Nm — c'est le verrou principal qui dimensionne toute la chaîne mécanique en aval.

---

## 1 — DIAGRAMME ARCHITECTURE MÉCANIQUE

Voir diagramme dans la conversation (système IT mécanique en 6 couches).

---

## 2 — COUCHE 1 : GROUPE MOTOPROPULSEUR

### Moteur thermique K9K766 (V1) → K9K896 (Phase 2)

**K9K766 V1 (actuel)** :
- 1461 cm³ Euro 4 Common Rail
- 86 ch / 200 Nm stock
- 240-260 Nm après reprog stage 0
- ECU Delphi Siemens

**K9K896 Phase 2 (futur)** :
- 1461 cm³ Euro 6 Common Rail
- 110 ch / 240 Nm stock
- 260 Nm plat après reprog stage 2
- ECU Bosch EDC17C84
- FAP + pompe huile variable

### Maintenance préventive K9K766 (V1)

| Action | Référence | Statut |
|---|---|---|
| Kit distribution + pompe à eau | SKF 123 dents | ✅ Autodoc |
| Joints SPI (×3) | Corteco + Reinz | ✅ Amazon/Autodoc/Oscaro |
| Calorstat / thermostat | AISIN THRAZ-7009 | ✅ Oscaro |
| Bougies préchauffage | OE + graisse cuivre Bardahl | ✅ Carter Cash |
| Capteur PMH | Bosch | À commander si défaut |
| EGR | Nettoyage ou remplacement | À évaluer |
| Coussinets bielle | Après inspection | ⬜ Différé |
| Boulons bielle | ET ENGINETEAM | ✅ Trodo |
| Catch can | Alu, montage Phase 0 | À sourcer |

---

## 3 — COUCHE 2 : TRANSMISSION

### TL4B043 — verrou principal du projet

- Boîte 6 vitesses manuelle Renault (Duster II)
- **Couple d'entrée max : 240-260 Nm** (limite haute, dégradation au-delà)
- Neuve (Eurofrance24) avec garantie 12 mois — **NE PAS OUVRIR**
- Huile MOTUL 75W-80 (4L pour rinçage + remplissage)

### Cardans et différentiel

- **Cardans SKF** (Autodoc) — D 187,99€ + G 172,30€
- **Différentiel ouvert intégré** (pas de modification)
- **Serrage cardans : 280 Nm roues au sol** (critique)

### Embrayage et accouplement

- **Valeo 845077 Kit 4P Conversion** (Carter Cash, 340,90€)
- Volant rigide + disque 228mm + mécanisme + CSC neufs
- Vis volant : 65 Nm
- **Émetteur Valeo 804816** (Trodo)
- **Durite HEL CCK171_VER** (Ultraperformance, aviation tressée)
- **Biellette reprise couple Lemförder 36284 01** (Carter Cash)

### Support BV

- **Support BV gauche Lemförder 37966 01** (Autodoc, 61,99€)
- Insert Powerflex PF-F60525 (déjà payé GT2i)
- **Support alu supérieur** : récupération casse Clio 3 GT (OE 8200338385)

### Levier de vitesses (suppression Quickshift)

- **Levier 6V + rotule + embase** : casse Clio 3 GT
- Câbles sélection + engagement : casse
- Habillage console : casse
- **Reprog UCH BVR → BVM** (Renolink, nécessaire)
- Contacteur pédale embrayage **METZGER** (Autodoc)
- Contacteur marche arrière **Febi 37169** (Autodoc)

---

## 4 — COUCHE 3 : SUSPENSION ET DIRECTION

### Amortisseurs Bilstein B8

- **AV ×2 : Bilstein B8 35-128649** (R.tech, 277,33€)
- **AR ×2 : Bilstein B8 24-128650** (Autodoc, 271,98€)
- Sport monotube hautes performances
- Conçus pour ressorts surbaissés (Eibach Pro-Kit)

### Ressorts Eibach Pro-Kit

- **Kit AV+AR Eibach E10-75-008-01-22** (Oscaro, 179,50€)
- Surbaissement -30mm
- Maintien de la garde au sol fonctionnelle

### Coupelles AV

- **Kit complet SNR KB655.32** (Oscaro, 117,80€/paire)
- 6 pièces : butée + roulement + coupelle + écrou + visserie
- Inclus pour les deux côtés

### Kit protection amortisseur

- **MEYLE 16-14 740 0001** (Oscaro, 17,28€)
- Capuchons et soufflets de protection

### Triangles AV

- **MEYLE D + G** (Autodoc, 62,99€ pièce)
- **Powerflex PF-F60901 + PF-F60902** (GT2i, déjà payés)
- Combinaison Triangles MEYLE + silentblocs Powerflex

### Rotules direction

- **Rotules extérieures MEYLE M14x1.5** (Autodoc, 18,99€ pièce)
- **Rotules intérieures MEYLE 16-16 031 0015** (Amazon)
- **Soufflets SKF VKJP 2011** ×2 (Carter Cash, 21,60€)
- Direction assistée hydraulique (EPAS) — pas de modification

### Biellettes anti-roulis

- **AR MEYLE 130mm** ×2 (Autodoc, 28,49€ pièce)
- **AV MEYLE 35-16 060 0021/HD** ×2 (Oscaro, 15,57€ pièce)

### Roulements et moyeux AV

- **Roulements SKF VKBA 3596** ×2 (Oscaro, 55,40€/paire)
- **Moyeux MEYLE** ×2 (Autodoc, 59,98€/paire)
- **Pressage Norauto** (atelier — service inclus)

### Fusées AV

- **VAICO D + G** (Autodoc, 80,49€ + 79,49€)

### Fusées AR (CRITIQUE)

- **Version disque à sourcer** (OE Renault concession ou casse Clio 3 GT)
- BDA604 + BDA605 Amazon = AUDI INCOMPATIBLES (à retirer)
- Coût estimé : 50-180€ selon source

### Powerflex (silentblocs polyuréthane)

- **6 pièces déjà payées (GT2i 392,40€)** :
  - PF-F60901-2 : Triangle AV avant
  - PF-F60902-2 : Triangle AV arrière
  - PF-F60920 : Support moteur supérieur
  - PF-F60821 : Support moteur inférieur
  - PF-F60525 : Support BV
  - PF-R60810-2 : Essieu AR

---

## 5 — COUCHE 4 : FREINAGE

### Disques

- **AV TRW DF4274BS 260mm** (Oscaro, 109,88€/paire) — ventilés
- **AR Brembo 09.9078.75 240mm** (Amazon, 83,26€/paire) — pleins
- Conversion AR tambour → disque

### Étriers

- **AV : FEBI fonte G + D** (Autodoc, 62,99€ + 62,49€)
- **AR : TRW alu G + D** (Autodoc, 107,99€ + 108,99€)
- Étriers neufs (vs reconditionnés casse)

### Supports d'étriers

- **AV : TRW ×2** (Autodoc, 64,98€) — ⚠️ vérifier compatibilité ABS/260mm
- **AR : TRW ×1** (Autodoc, 65,99€) — ⚠️ vérifier si universel G+D ou besoin 2e côté
- Vis M12 cl. 10.9 ×8 (à acheter séparément, 10-20€)

### Plaquettes

- **AV : Brembo P 68 033X performance** (Amazon, 45,49€)
- **AR : TRW GDB1330** (Carter Cash, 19,90€)
- Repousse-piston rotatif NEO TOOLS (Autodoc)

### Flexibles aviation tressée

- **AV : Goodridge** (kit aviation, 109,23€)
- **AR : Goodridge** (à clarifier avec conversion disque, kit séparé possible)
- DOT4 MOTUL ×4 (2L) pour purge complète (Autodoc)

### Maître-cylindre

- **Conservation OE** (bocal d'origine pour CT)
- **NE PAS toucher** — risque conformité

---

## 6 — COUCHE 5 : ROUES ET PNEUMATIQUES

### Jantes

- **Japan Racing JR-7 16×7 ET38 4×100** (Ultraperformance, 596€)
- Noir brillant (×4)
- Conforme aux 4×100 OE Modus
- Compatible disques 260mm AV + 240mm AR

### Pneumatiques

- **195/55 R16** (×4)
- Diamètre = origine ±0,6mm (compteur exact)
- À acheter Norauto (240-400€)
- Montage + équilibrage Norauto

### Géométrie

- **OBLIGATOIRE fin de chantier** (Norauto)
- Parallélisme, carrossage, chasse à régler
- Critique pour CT

---

## 7 — COUCHE 6 : ADMISSION ET ÉCHAPPEMENT

### Admission

- **Filtre à air Green** (à commander Ultraperformance)
- **Boîte à air conservée** (OE modifiée si nécessaire)
- Capteur débit d'air OE

### FMIC (Front Mount Intercooler)

- **NRF 30481** (Oscaro, 118,90€)
- Préparation Phase 2 (turbo plus gros)
- Échangeur plus efficace que stock

### Catch can (Oil catch can)

- Alu, entre vanne EGR et admission
- À sourcer (~30-50€ AliExpress ou européen)
- Vidanger tous les 5 000 km

### Échappement

- **Conservation OE Phase 0**
- Ligne complète si défaillance
- **Phase 2 : à évaluer selon diamètre ligne aval K9K896**

### Turbo

- **KP35 stock conservé V1**
- **Gros turbo à définir Phase 2** (BV43, BV45, ou GTB1749V)

---

## 8 — COUCHE 7 : INFRASTRUCTURE MOTEUR

### Cooling (refroidissement)

- **Vase d'expansion alu 1.2 bar** (à commander, ~30-50€)
- **Calorstat AISIN THRAZ-7009** (Oscaro)
- Liquide LDR neuf (G12++ ou OE)
- Joints toriques neufs sur durites principales

### Carburant

- **Pompe à carburant OE** (vérification débit)
- **Filtre à carburant OE neuf**
- Décanteur eau (purge périodique)

### Lubrification

- **Huile moteur Castrol Edge 5W-30 (5L)**
- **Filtre huile OE**
- Bouchon vidange Corteco M16×1.5 (Autodoc)

---

## 9 — INTÉGRATION SYSTÉMIQUE

### Diagramme des dépendances

```
[K9K766 V1 / K9K896 P2]
    ↓ Couple 200-260 Nm
[Embrayage Valeo 845077]
    ↓ Couple transmis
[TL4B043 6V] ← LIMITE 260 Nm
    ↓ Couple aux roues
[Cardans SKF] ← 280 Nm serrage cardan
    ↓ Couple
[Moyeux MEYLE]
    ↓
[Roulements SKF VKBA 3596]
    ↓
[Jantes JR-7 + Pneus 195/55 R16]
    ↓
[Suspension Bilstein B8 + Eibach + Powerflex]
    ↓ Forces dynamiques
[Châssis Modus]
    ↓
[Freinage FEBI/TRW + Brembo + Goodridge]
```

### Contraintes inter-systèmes

| Contrainte | Origine | Impact |
|---|---|---|
| Couple max 260 Nm | TL4B043 | Reprog moteur limitée |
| Diamètre disque 260mm AV | Jantes JR-7 16" | Supports étriers spécifiques |
| Garde sol -30mm | Eibach Pro-Kit | Suspension B8 obligatoire |
| 4×100 ET38 | Jantes JR-7 | Entraxe boulon-moyeu OE |
| Fixations supports | Berceau OE | Pas de modification châssis |

---

## 10 — ORDRE DE MONTAGE

L'ordre est critique pour éviter retravail :

1. **Démontage complet** (Phase 0)
2. **Anti-corrosion** (avant remontage de toute pièce)
3. **Insonorisation** (sur surface propre et sèche)
4. **Châssis et points de fixation** (vérification, retaraudage si besoin)
5. **Berceau et supports moteur** (Powerflex inserts)
6. **Moteur + TL4B043 accouplés** (Loctite 518 plan de joint)
7. **Réinsertion bloc** (par l'avant + cric + palette + pneu)
8. **Cardans + serrage 280 Nm roues au sol** (CRITIQUE)
9. **Embrayage hydraulique** (CSC + émetteur + durite HEL)
10. **Freinage** (étriers + disques + flexibles + plaquettes + purge)
11. **Suspension** (B8 + Eibach + coupelles + soufflets)
12. **Direction** (rotules + soufflets + biellettes)
13. **Roues + serrage 280 Nm cardans roues au sol**
14. **Géométrie** (Norauto)
15. **Remplissages** (huiles, LDR, DOT4, carburant)
16. **Démarrage et rodage** (50→1 000 km)
17. **Reprog stage 0** (240-260 Nm)
18. **Test routier final**

---

## 11 — POINTS DE VIGILANCE MÉCANIQUE

### Vis et serrages critiques

| Composant | Couple | Note |
|---|---|---|
| Vis volant rigide | 65 Nm | Loctite 243 |
| Vis embrayage 845077 | 25 Nm + 90° | OE Renault |
| Cardans | 280 Nm | **Roues au sol** |
| Vis triangles AV | 90 Nm + 90° | Loctite 243 |
| Vis amortisseurs | 65 Nm | OE |
| Vis supports étrier M12 cl. 10.9 | 130 Nm | À acheter |
| Boulons bielle | 25 Nm + 50° | OE |
| Vis culasse | OE séquence | Si dépose |
| Bougie de préchauffage | 10 Nm | Graisse cuivre Bardahl |
| Bouchon vidange Corteco | 30 Nm | Joint nouveau à chaque vidange |

### Anti-marquage / réutilisation

- **TL4B043 neuve** : NE PAS OUVRIR (garantie 12 mois)
- **Disques Brembo AR** : pas de manipulation des surfaces de freinage
- **Cardans SKF** : graisse molybdène Febi 02582 sur cannelures
- **Bilstein B8** : ressorts Eibach SEULS (pas mélange OE)
- **Coupelles SNR** : monter avec roulements neufs (jamais réutiliser)
- **Powerflex** : graisse au silicone fournie pour pose

### Phase 2 compatibilité

- Embrayage Valeo 845077 : compatible K9K896 (cloche K9K identique)
- TL4B043 : compatible K9K896 (cloche K9K identique)
- Cardans SKF : compatibles
- Train roulant complet : compatible
- **Seul change pour Phase 2 : moteur thermique + ECU + faisceau moteur + FAP**

---

## 12 — BUDGET RÉCAPITULATIF MÉCANIQUE

### Engagé / Payé

| Source | Montant |
|---|---|
| TL4B043 (Eurofrance24) | 532 € |
| Powerflex ×6 (GT2i) | 392 € |
| **TOTAL PAYÉ** | **924 €** |

### En panier

| Catégorie | Montant |
|---|---|
| Carter Cash (embrayage + plaquettes + soufflets + biellette) | 436 € |
| Autodoc (cardans + distribution + freinage + suspension AR + fusées AV + supports + huiles + outils) | 1 841 € |
| Oscaro (coupelles + ressorts + FMIC + disques + roulements + biellettes) | 662 € |
| Ultraperformance (jantes JR-7) | 596 € |
| R.tech (Bilstein B8 AV) | 277 € |
| Amazon (Brembo + Corteco + Meyle rotules + boulons + Loctite) | ~340 € |
| Trodo (passage de roue + cache moteur + émetteur + boulons bielle) | 186 € |
| Goodridge (flexibles aviation) | 109 € |
| **TOTAL PANIERS** | **~4 447 €** |

### Reste à acheter

| Catégorie | € mini | € maxi |
|---|---|---|
| Fusées AR version disque | 50 | 180 |
| Vis supports étrier M12 ×8 | 10 | 20 |
| Pneus 195/55 R16 ×4 | 240 | 400 |
| Casse Clio 3 GT (levier + pédalier + câbles + support alu) | 100 | 300 |
| Outils manquants | 43 | 55 |
| Coussinets bielle (différé) | 0 | 80 |
| Divers (vis, consommables) | 30 | 80 |
| **TOTAL RESTE MÉCANIQUE** | **473** | **1 115** |

### Total mécanique Phase 0

| | Mini | Maxi |
|---|---|---|
| Payé + paniers + reste | 5 844 € | 6 486 € |

---

*MÉCANIQUE V18.1 — 1er juin 2026*
*Architecture systémique 7 couches pour Phase 0 (V1)*
*Préparation Phase 2 (K9K896) intégrée*
