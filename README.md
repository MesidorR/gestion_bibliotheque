# 📚 Gestion Bibliothèque

Ce projet Django est une application web permettant aux utilisateurs de gérer une collection de livres. Il inclut les fonctionnalités d’authentification, d’ajout de livres, d’affichage de liste, détails et bien plus encore.

## ✨ Fonctionnalités

- Inscription et connexion des utilisateurs
- Ajout de livres avec informations :
  - Titre
  - Auteur
  - ISBN (Facultatif)
  - Description (Facultatif)
  - Date de publication
- Liste des livres enregistrés
- Attribution automatique du livre à l’utilisateur connecté
- Interface utilisateur avec Bootstrap
- Éditeur de texte enrichi avec django-summernote pour description

## ⚙️ Installation

1. **Cloner le projet :**
   ``` bash
   git clone https://github.com/ton-utilisateur/gestion_bibliotheque.git
   cd gestion_bibliotheque
   ```
   
### Créer un environnement virtuel et l’activer :
```bash
python -m venv environnement
.\environnement\Scripts\activate
```

### Installer les dépendances :
```bash
pip install -r requirements.txt
```

### Appliquer les migrations et lancer le serveur :
```bash
python manage.py migrate
python manage.py runserver
````
### 🧪 Créer un superutilisateur
```bash
python manage.py createsuperuser
```
### 📝 Dépendances
Voir le fichier ``requirements.txt``

### 👤  Auteur
Projet réalisé par Rickenly MESIDOR – dans le cadre du cours LOG3300
