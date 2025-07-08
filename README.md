# !!!!!!!!! VOIR COMMANDES.TXT

# Examen PyQt6 - Partie 1 : Signaux, Slots et Affichage de Messages

## Description

Cette application illustre les concepts fondamentaux de signaux et slots en PyQt6/PySide6. Elle permet à l'utilisateur de saisir un message qui s'affiche ensuite dans une zone dédiée et dans une fenêtre pop-up.

## Fonctionnalités

- **Interface graphique** avec QLineEdit, QPushButton et QLabel
- **Signal/Slot** : connexion du signal `clicked` du bouton à une méthode personnalisée
- **Validation** : aucune action si le champ de saisie est vide
- **Affichage double** : dans le label principal ET dans une fenêtre pop-up
- **Interface créée** avec Qt Designer (fichier .ui)

## Installation

### 1. Vérifier la version de Python
```bash
python3.13 --version
```

### 2. Créer et activer l'environnement virtuel
```bash
python3.13 -m venv env
.\env\Scripts\activate  # Windows
# ou
source env/bin/activate  # Linux/Mac
```

### 3. Installer les dépendances
```bash
pip install pyside6 pyside6-designer
# ou
pip install -r requirements.txt
```

## Utilisation

### 1. Conversion du fichier .ui (optionnel)
```bash
python convert_ui.py
```

### 2. Lancement de l'application
```bash
python main.py
```

## Structure du projet

```
examen1/
├── interface.ui          # Interface graphique (Qt Designer)
├── main.py              # Application principale
├── convert_ui.py        # Script de conversion .ui → .py
├── requirements.txt     # Dépendances
└── README.md           # Documentation
```

## Fonctionnement

1. **Saisir un message** dans le champ de texte
2. **Cliquer sur le bouton** "Afficher le message" ou appuyer sur Entrée
3. **Voir le résultat** :
   - Dans la zone d'affichage avec le préfixe "Message saisi : "
   - Dans une fenêtre pop-up
4. **Champ vide** : message d'avertissement affiché

## Contraintes respectées

✅ Signal `clicked` du bouton relié à une méthode slot  
✅ Traitement exclusivement via la méthode slot  
✅ Aucune action si le champ est vide  
✅ Préfixe "Message saisi : " ajouté  
✅ Fichier .ui utilisé  
✅ Alternative avec fenêtre pop-up implémentée  

## Concepts démontrés

- **Signaux et Slots** : mécanisme de communication entre objets Qt
- **Chargement d'interface** : utilisation de fichiers .ui
- **Validation d'entrée** : vérification des données utilisateur
- **Feedback visuel** : changement de style selon le contexte 
