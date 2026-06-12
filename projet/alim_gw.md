# Système de Refroidissement Biphasique Extrême (12 kW GaN) - Cartouche Megadrive

Ce dépôt contient les spécifications, les scripts d'optimisation mathématique et les dossiers de conception CAO/Électronique pour le projet de refroidissement par immersion biphasique appliqué à un étage de puissance de 12 kW (GaN MOSFETs), confiné dans le volume d'une cartouche de jeu Megadrive.

---

## 🛠️ Analyse de l'Architecture Thermique Hybride

L'architecture propose un système de refroidissement à **double couche parallèle** :
1. **Couche Interne (Convection Biphasique) :** Le fluide s'évapore au contact des GaN, monte en pression, est accéléré dans une tuyère en spirale (échangeur de quantité de mouvement), puis est évacué par durite vers le radiateur principal.
2. **Couche Externe (Conduction Haute Performance) :** La chaleur résiduelle hautement concentrée sur les parois de cette spirale en aluminium est captée par une couche de **carbone pyrolytique**, puis transférée à un **waterblock externe** qui coiffe la cartouche. Ce waterblock est lui aussi relié au radiateur.

### Est-ce un choix pertinent ou une erreur de design ?
**C'est un excellent choix d'ingénierie avancée**, indispensable pour dissiper 12 kW dans ce volume. Voici pourquoi :
* **Prévention du "Thermal Choking" (Engorgement thermique) :** L'aluminium, bien que bon conducteur, s'échaufferait plus vite que la capacité du fluide interne à évacuer les calories au niveau de la spirale d'accélération. La cartouche deviendrait un bloc de métal brûlant.
* **Rôle du Carbone Pyrolytique :** Ce matériau possède une conductivité thermique anisotrope exceptionnelle ($> 1500 \text{ W/mK}$ dans le plan). Il va "étaler" le point chaud de la spirale sur toute la surface de la cartouche pour éviter un gradient thermique destructeur.
* **Le Waterblock Externe :** Il agit comme un bouclier thermique actif. Il intercepte les calories par conduction *avant* qu'elles ne fassent fondre le plastique environnant ou la console, complétant ainsi le travail de la boucle principale de fluide.

---

## 📅 Plan de Développement Global
