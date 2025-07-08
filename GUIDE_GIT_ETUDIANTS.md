# 📚 Guide Git Exhaustif pour les Étudiants

## 🎯 Objectif
Ce guide vous explique comment récupérer et travailler avec les branches `examen1`, `examen2` et des commits spécifiques du dépôt du cours.

---

## 📋 Table des matières

1. [Prérequis](#prérequis)
2. [Cloner le dépôt](#cloner-le-dépôt)
3. [Récupérer une branche spécifique](#récupérer-une-branche-spécifique)
4. [Récupérer un commit spécifique](#récupérer-un-commit-spécifique)
5. [Naviguer entre les branches](#naviguer-entre-les-branches)
6. [Commandes essentielles](#commandes-essentielles)
7. [Scénarios pratiques](#scénarios-pratiques)
8. [Dépannage](#dépannage)
9. [Résumé des commandes](#résumé-des-commandes)

---

## 🔧 Prérequis

### Installation de Git
```bash
# Vérifier si Git est installé
git --version

# Si Git n'est pas installé, téléchargez-le depuis :
# https://git-scm.com/downloads
```

### Configuration initiale (à faire une seule fois)
```bash
# Configurer votre nom
git config --global user.name "Votre Nom"

# Configurer votre email
git config --global user.email "votre.email@example.com"

# Vérifier la configuration
git config --list
```

---

## 📥 Cloner le dépôt

### Méthode 1 : Cloner tout le dépôt
```bash
# Cloner le dépôt complet
git clone https://github.com/hrhouma1/Pyside6-examens.git

# Entrer dans le dossier
cd Pyside6-examens

# Voir toutes les branches disponibles
git branch -a
```

### Méthode 2 : Cloner une branche spécifique directement
```bash
# Cloner seulement la branche examen1
git clone -b examen1 https://github.com/hrhouma1/Pyside6-examens.git examen1-project

# Cloner seulement la branche examen2
git clone -b examen2 https://github.com/hrhouma1/Pyside6-examens.git examen2-project
```

---

## 🌿 Récupérer une branche spécifique

### Étape 1 : Voir toutes les branches disponibles
```bash
# Voir les branches locales
git branch

# Voir toutes les branches (locales + distantes)
git branch -a

# Voir seulement les branches distantes
git branch -r
```

### Étape 2 : Récupérer et basculer vers une branche

#### Option A : Créer une branche locale à partir d'une branche distante
```bash
# Récupérer la branche examen1
git checkout -b examen1 origin/examen1

# OU récupérer la branche examen2
git checkout -b examen2 origin/examen2
```

#### Option B : Basculer vers une branche existante
```bash
# Si la branche existe déjà localement
git checkout examen1

# OU
git checkout examen2
```

#### Option C : Récupérer les dernières modifications
```bash
# Mettre à jour toutes les branches distantes
git fetch origin

# Basculer vers la branche souhaitée
git checkout examen1
git pull origin examen1
```

### Étape 3 : Vérifier que vous êtes sur la bonne branche
```bash
# Voir la branche actuelle
git branch

# Voir le statut
git status

# Voir l'historique des commits
git log --oneline -10
```

---

## 🎯 Récupérer un commit spécifique

### Méthode 1 : Voir l'historique des commits
```bash
# Voir tous les commits avec leurs hash
git log --oneline

# Voir l'historique avec plus de détails
git log --graph --oneline --all

# Voir les commits d'une branche spécifique
git log --oneline origin/examen1
git log --oneline origin/examen2
```

### Méthode 2 : Récupérer un commit spécifique par son hash
```bash
# Récupérer un commit spécifique (remplacer abc1234 par le hash réel)
git checkout abc1234

# Créer une nouvelle branche à partir de ce commit
git checkout -b nouvelle-branche abc1234

# Revenir à la branche principale
git checkout main
```

### Méthode 3 : Récupérer un commit par message
```bash
# Rechercher un commit par son message
git log --grep="message recherché"

# Exemple : chercher les commits contenant "examen"
git log --grep="examen"
```

---

## 🔄 Naviguer entre les branches

### Basculer entre les branches
```bash
# Aller sur la branche main
git checkout main

# Aller sur la branche examen1
git checkout examen1

# Aller sur la branche examen2
git checkout examen2

# Revenir à la branche précédente
git checkout -
```

### Créer une nouvelle branche
```bash
# Créer une nouvelle branche à partir de la branche actuelle
git checkout -b ma-nouvelle-branche

# Créer une branche à partir d'une branche spécifique
git checkout -b ma-branche origin/examen1
```

### Supprimer une branche
```bash
# Supprimer une branche locale (après avoir basculé vers une autre)
git branch -d nom-branche

# Forcer la suppression
git branch -D nom-branche
```

---

## 📝 Commandes essentielles

### Informations sur le dépôt
```bash
# Voir le statut actuel
git status

# Voir les branches
git branch -a

# Voir les commits récents
git log --oneline -10

# Voir les modifications
git diff

# Voir les fichiers modifiés
git diff --name-only
```

### Mise à jour du dépôt
```bash
# Récupérer les dernières modifications de toutes les branches
git fetch origin

# Mettre à jour la branche actuelle
git pull origin nom-branche

# Mettre à jour toutes les branches
git pull --all
```

### Gestion des fichiers
```bash
# Voir les fichiers dans le dépôt
ls -la

# Voir l'arborescence
tree

# Voir le contenu d'un fichier
cat nom-fichier.py

# Éditer un fichier
code nom-fichier.py
```

---

## 🎯 Scénarios pratiques

### Scénario 1 : Récupérer le code de l'examen 1
```bash
# 1. Cloner le dépôt
git clone https://github.com/hrhouma1/Pyside6-examens.git
cd Pyside6-examens

# 2. Récupérer la branche examen1
git checkout -b examen1 origin/examen1

# 3. Vérifier les fichiers
ls -la

# 4. Voir les commits de cette branche
git log --oneline

# 5. Lancer l'application (si applicable)
python main.py
```

### Scénario 2 : Récupérer le code de l'examen 2
```bash
# 1. Si vous avez déjà le dépôt, mettre à jour
git fetch origin

# 2. Récupérer la branche examen2
git checkout -b examen2 origin/examen2

# 3. Vérifier les fichiers
ls -la

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Lancer l'application
python main.py
```

### Scénario 3 : Comparer deux branches
```bash
# 1. Basculer vers la première branche
git checkout examen1

# 2. Voir les fichiers
ls -la

# 3. Basculer vers la deuxième branche
git checkout examen2

# 4. Voir les fichiers
ls -la

# 5. Comparer les branches
git diff examen1..examen2

# 6. Voir les commits différents
git log --oneline examen1..examen2
```

### Scénario 4 : Récupérer un commit spécifique
```bash
# 1. Voir l'historique
git log --oneline

# 2. Récupérer un commit spécifique (exemple : abc1234)
git checkout abc1234

# 3. Créer une branche à partir de ce commit
git checkout -b travail-sur-commit abc1234

# 4. Revenir à la branche principale
git checkout main
```

---

## 🚨 Dépannage

### Problème : "Branch not found"
```bash
# Solution : Récupérer toutes les branches distantes
git fetch origin

# Puis essayer de nouveau
git checkout -b examen1 origin/examen1
```

### Problème : "Already exists"
```bash
# Solution : Basculer vers la branche existante
git checkout examen1

# OU supprimer et récréer
git branch -D examen1
git checkout -b examen1 origin/examen1
```

### Problème : "Permission denied"
```bash
# Solution : Vérifier les permissions
ls -la

# Changer les permissions si nécessaire
chmod +x script.py

# Ou utiliser sudo (Linux/Mac)
sudo git clone ...
```

### Problème : "Merge conflict"
```bash
# Solution : Abandonner le merge
git merge --abort

# OU résoudre les conflits
git status
# Éditer les fichiers en conflit
git add .
git commit -m "Résolution des conflits"
```

### Problème : "Détaché HEAD"
```bash
# Solution : Créer une branche
git checkout -b nouvelle-branche

# OU revenir à une branche existante
git checkout main
```

---

## 📋 Résumé des commandes

### Commandes de base
```bash
# Cloner le dépôt
git clone https://github.com/hrhouma1/Pyside6-examens.git

# Voir les branches
git branch -a

# Récupérer une branche
git checkout -b examen1 origin/examen1

# Mettre à jour
git fetch origin
git pull origin examen1

# Voir l'historique
git log --oneline

# Voir le statut
git status
```

### Commandes avancées
```bash
# Récupérer un commit spécifique
git checkout abc1234

# Créer une branche à partir d'un commit
git checkout -b nouvelle-branche abc1234

# Comparer deux branches
git diff examen1..examen2

# Voir les fichiers modifiés entre branches
git diff --name-only examen1..examen2

# Rechercher dans l'historique
git log --grep="message"

# Voir les commits par auteur
git log --author="nom"
```

---

## 🎓 Conseils pour les étudiants

### Bonnes pratiques
1. **Toujours vérifier** la branche actuelle avant de travailler
2. **Faire des sauvegardes** régulières de votre travail
3. **Lire les messages de commit** pour comprendre l'évolution
4. **Utiliser des noms de branches descriptifs**
5. **Documenter** vos modifications

### Workflow recommandé
```bash
# 1. Récupérer les dernières modifications
git fetch origin

# 2. Créer une branche pour votre travail
git checkout -b mon-travail origin/examen1

# 3. Travailler sur vos fichiers
# ... modifications ...

# 4. Voir les modifications
git status
git diff

# 5. Sauvegarder votre travail (optionnel)
git add .
git commit -m "Mon travail sur l'examen"
```

---

## 📞 Support

### En cas de problème
1. Vérifiez les **messages d'erreur** attentivement
2. Consultez la section **Dépannage** ci-dessus
3. Utilisez `git status` pour comprendre la situation
4. Demandez de l'aide au professeur ou aux assistants

### Ressources utiles
- [Documentation Git officielle](https://git-scm.com/doc)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

---

## 🏁 Conclusion

Ce guide vous donne tous les outils nécessaires pour :
- ✅ Récupérer n'importe quelle branche du dépôt
- ✅ Accéder à des commits spécifiques
- ✅ Naviguer efficacement dans l'historique Git
- ✅ Résoudre les problèmes courants
- ✅ Travailler de manière organisée

**Bonne chance pour vos examens !** 🎉

---

*Guide créé pour le cours PySide6 - Professeur Haythem Rehouma* 