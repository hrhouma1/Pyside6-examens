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

