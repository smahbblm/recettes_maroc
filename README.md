# Recettes Maroc - Projet Django

Petite documentation pour initialiser et structurer le dépôt avant de le pousser sur GitHub.

Structure observée

- `manage.py` - script Django
- `config_recettes/` - settings, urls et configuration WSGI/ASGI
- `recettes/` - application Django principale
  - `recettes/models/` - models découpés par fichier
  - `recettes/views.py`, `recettes/admin.py`, `recettes/tests.py`
- `venv/` - environnement virtuel (ignoré dans le dépôt)

  l'ajoute  d'application : accounts/ en utilisant cette commande : (venv) PS D:\recettes_maroc> python manage.py startapp preferences
  


Étapes recommandées avant push initial

1. Vérifier les modèles
   - Ajouter vos classes de modèles dans `recettes/models/*.py`.
   - Assurez-vous qu'il y a `recettes/models/__init__.py` (déjà ajouté) pour que Django découvre les modèles.

2. Installer les dépendances et créer la base
   - Activez votre venv puis installez les dépendances depuis `requirements.txt`.

3. Migrations et admin
   - Exécuter `makemigrations` et `migrate`.
   - Créer un superuser avec `createsuperuser`.

Commandes utiles (PowerShell sous Windows)

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Préparer le dépôt Git

```powershell
git init
git add .
git commit -m "Initial project skeleton"
# Créer un repo GitHub via interface web ou GitHub CLI, puis :
git remote add origin <remote-url>
git push -u origin main
```

Remarques

- N'ajoutez pas `SECRET_KEY` ou autres secrets dans le dépôt public ; préférez des variables d'environnement.
- Conservez `DEBUG = True` seulement pour le développement.
