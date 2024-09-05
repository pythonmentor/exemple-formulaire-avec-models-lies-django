# Exemple de formulaire avec modèles liés avec HTMX

Cet exemple a été construit pour montrer comment permettre la création 
inline d'un objet lié au modèle gérer par un formulaire.

## Dépendance
- Les dépendances python sont gérée à l'aide de pipenv. Il est nécessaire de l'installer avec pip install pipenv ou uv tool install pipenv (si vous travaillez avec uv), ou encore pipx install pipenv (si vous travaillez avec pipx).
- Les dépendances front-end sont gérée à l'aide de npm. Il est nécessaire d'installer node.js au préalable pour pouvoir travailler avec cet exemple

## Tester l'exemple
Voici les étapes pour tester l'exemple
1. Installer les dépendances avec `pipenv install`
2. Ouvrir un terminal, se positioner dans le répertoire frontend et exécuter `npm install`, puis exécuter npm start
3. Ouvrir un second terminal à la racine du projet et exécuter les commandes `python manage.py migrate` et `python manage.py runserver`
4. Visiter la page d'accueil du projet à l'aidresse [http://127.0.0.1:8000](http://127.0.0.1:8000)