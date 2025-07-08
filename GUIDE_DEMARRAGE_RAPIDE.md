# ⚡ Guide de Démarrage Rapide - Git

## 🚀 Pour les étudiants pressés !

### 📥 Récupérer l'examen 1
```bash
# Cloner et récupérer la branche examen1
git clone -b examen1 https://github.com/hrhouma1/Pyside6-examens.git examen1-project
cd examen1-project

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python main.py
```

### 📥 Récupérer l'examen 2
```bash
# Cloner et récupérer la branche examen2
git clone -b examen2 https://github.com/hrhouma1/Pyside6-examens.git examen2-project
cd examen2-project

# Installer les dépendances
pip install -r requirements.txt

# Démarrer MySQL (Windows)
net start mysql

# Tester la connexion à la base de données
python connect_database.py

# Ajouter des données de test
python add_mysql_test_data.py

# Lancer l'application
python main_simple.py
```

### 🔄 Si vous avez déjà le dépôt
```bash
cd Pyside6-examens

# Mettre à jour
git fetch origin

# Basculer vers examen1
git checkout -b examen1 origin/examen1

# OU basculer vers examen2
git checkout -b examen2 origin/examen2
```

### 🔍 Voir les branches disponibles
```bash
# Voir toutes les branches
git branch -a

# Voir l'historique
git log --oneline -10
```

### 🆘 En cas de problème
```bash
# Voir le statut
git status

# Récupérer les dernières modifications
git fetch origin

# Forcer la récupération d'une branche
git checkout -B examen1 origin/examen1
```

---

**📖 Pour plus de détails, consultez `GUIDE_GIT_ETUDIANTS.md`** 