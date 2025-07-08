# !!!! VOIR COMMANDES.TXT

# Application Messages - Signaux et Slots (PyQt6/PySide6)

Une application graphique développée avec PyQt6/PySide6 qui illustre les concepts de signaux et slots, avec intégration d'une base de données MySQL.

## 📚 Guides pour les étudiants

### 🎯 Guides Git
- **[📖 Guide Git Exhaustif](GUIDE_GIT_ETUDIANTS.md)** - Guide complet pour récupérer les branches et commits
- **[⚡ Guide de Démarrage Rapide](GUIDE_DEMARRAGE_RAPIDE.md)** - Pour récupérer rapidement une branche

### 🌿 Branches disponibles
- **`examen1`** - Version basique avec interface simple
- **`examen2`** - Version complète avec base de données MySQL

### 💡 Démarrage rapide
```bash
# Récupérer l'examen 1
git clone -b examen1 https://github.com/hrhouma1/Pyside6-examens.git examen1-project

# Récupérer l'examen 2
git clone -b examen2 https://github.com/hrhouma1/Pyside6-examens.git examen2-project
```

### 🔄 PyQt6 vs PySide6
Ce projet supporte les deux frameworks :
- **PyQt6** - Version originale avec `uic.loadUi()`
- **PySide6** - Version alternative avec `QUiLoader()`
- **Fichiers disponibles** :
  - `main.py` - Version PySide6 avec fichier .ui
  - `main_simple.py` - Version PySide6 100% Python (recommandé)

## Fonctionnalités

- **Partie 1** : Affichage de messages avec signaux et slots
  - Champ de saisie de texte (QLineEdit)
  - Bouton d'envoi (QPushButton)
  - Zone d'affichage (QLabel)
  - Validation des champs vides

- **Partie 2** : Intégration avec base de données MySQL
  - Insertion des messages dans la base de données
  - Affichage des messages stockés
  - Gestion automatique de la création de la base de données et des tables

## Prérequis

1. **Python 3.8+**
2. **MySQL Server** installé et configuré
3. **Accès à une base de données MySQL** (utilisateur root ou autre utilisateur avec privilèges)

## Installation

### 1. Installer les dépendances Python

```bash
pip install -r requirements.txt
```

### 2. Configuration de la base de données

Modifiez les paramètres de connexion dans `config.py` ou directement dans `main.py` :

```python
self.db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'votre_mot_de_passe',  # Modifiez selon votre configuration
    'database': 'messages_app'
}
```

### 3. Création de la base de données (optionnel)

L'application crée automatiquement la base de données et la table. Vous pouvez aussi exécuter le script SQL manuellement :

```bash
mysql -u root -p < setup_database.sql
```

## Utilisation

### Lancer l'application

```bash
python main.py
```

### Fonctionnement

1. **Saisie de message** : Tapez votre message dans le champ de saisie
2. **Envoi** : Cliquez sur le bouton "Envoyer" ou appuyez sur Entrée
3. **Affichage** : Le message apparaît dans la zone d'affichage avec le préfixe "Message saisi : "
4. **Sauvegarde** : Le message est automatiquement sauvegardé dans la base de données
5. **Visualisation** : Les messages de la base de données sont affichés dans la zone inférieure
6. **Rafraîchissement** : Utilisez le bouton "Rafraîchir les messages" pour mettre à jour la liste

### Contraintes respectées

- ✅ Signal `clicked` du bouton relié à une méthode (slot)
- ✅ Traitement exclusif via la méthode slot
- ✅ Aucune action si le champ est vide
- ✅ Insertion en base de données
- ✅ Création automatique de la base et de la table

## Structure du projet

```
examen2/
├── main.py              # Application principale
├── config.py            # Configuration de la base de données
├── requirements.txt     # Dépendances Python
├── setup_database.sql   # Script SQL d'initialisation
└── README.md           # Documentation
```

## Signaux et Slots utilisés

- `QPushButton.clicked` → `on_send_button_clicked()`
- `QLineEdit.returnPressed` → `on_send_button_clicked()`
- `QPushButton.clicked` → `load_messages_from_db()`

## Gestion des erreurs

- Connexion à la base de données
- Création de la base de données et des tables
- Insertion et récupération des données
- Validation des champs vides
- Messages d'erreur via QMessageBox

## Personnalisation

Vous pouvez modifier :
- Les paramètres de base de données dans `config.py`
- L'apparence de l'interface via les styles CSS
- La taille maximale des messages
- Les messages d'erreur et d'information

## Dépannage

### Erreur de connexion MySQL
- Vérifiez que MySQL Server est démarré
- Vérifiez les identifiants de connexion
- Assurez-vous que l'utilisateur a les privilèges nécessaires

### Erreur d'importation PyQt6
```bash
pip install PyQt6
```

### Erreur mysql-connector-python
```bash
pip install mysql-connector-python
``` 
=======
# Pyside6-examens

## Hypothèses

* Tu as deux dossiers locaux déjà prêts :

  * `projet_examen1/` → ira dans la branche `examen1`
  * `projet_examen2/` → ira dans la branche `examen2`
* Le dépôt distant GitHub est vide ou contient juste un README :
  `https://github.com/ton-utilisateur/mon-projet.git`

---

## Étapes pour le premier dossier : `projet_examen1/`

```bash
cd projet_examen1
git init
git checkout -b examen1
git add .
git commit -m "Initial commit pour examen1"
git remote add origin https://github.com/ton-utilisateur/mon-projet.git

# Si le dépôt distant contient déjà un README :
git pull origin main --allow-unrelated-histories

# Pousser sur la branche examen1
git push -u origin examen1
```

---

## Étapes pour le second dossier : `projet_examen2/`

```bash
cd ../projet_examen2
git init
git checkout -b examen2
git add .
git commit -m "Initial commit pour examen2"
git remote add origin https://github.com/ton-utilisateur/mon-projet.git

# Facultatif si le dépôt distant a déjà des fichiers :
git pull origin main --allow-unrelated-histories

# Pousser sur la branche examen2
git push -u origin examen2
```

---

## Résultat

Tu auras :

* `projet_examen1/` poussé sur la branche `examen1`
* `projet_examen2/` poussé sur la branche `examen2`
* Les deux branches dans **le même dépôt distant GitHub**

---

## Pour vérifier

Va sur GitHub → ton dépôt → onglet "Branches", tu devrais voir :

* `main` (s'il existait)
* `examen1`
* `examen2`

>>>>>>> 6c583e7085cb286b0736453c54ea060a8ebac786
