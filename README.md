# Application Messages - Signaux et Slots (PyQt6)

Une application graphique développée avec PyQt6 qui illustre les concepts de signaux et slots, avec intégration d'une base de données MySQL.

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