# Programme Python : Description Changer

Ce programme Python permet de changer automatiquement la description d'un compte Discord à intervalles réguliers. Il utilise le module `requests` pour envoyer des requêtes PATCH à l'API Discord, et le module `pystyle` pour le design.

## Installation des modules

```bash
python -m pip install -r requirements.txt
```

ou vous pouvez simplement lancer le start.bat

## Utilisation du programme

### Configuration

Avant de lancer le programme, vous devez configurer les paramètres dans le fichier `config.json`. Les paramètres disponibles sont :

- `"token"` : le jeton d'authentification de votre compte Discord.
- `"time"` : l'intervalle de temps en secondes entre chaque changement de description.
- `"descriptions"` : une liste de descriptions à appliquer à votre compte. Le programme choisira une description aléatoire parmi cette liste à chaque intervalle.
- `"end"` : la chaîne de caractères à ajouter à la fin de chaque description.

Vous devez remplir les champs correspondants dans le fichier `config.json` avant d'exécuter le programme.

### Lancement du programme

Une fois que vous avez configuré les paramètres dans le fichier `config.json`, vous pouvez lancer le programme en exécutant le fichier `main.py`.

Le programme va changer la description de votre compte Discord à intervalles réguliers en utilisant les descriptions fournies dans `config.json`. Les résultats de chaque requête seront affichés à l'écran.

### Commandes disponibles

- `help` : Affiche les commandes disponibles.
- `config` : Ouvre le fichier `config.json` dans le bloc-notes pour le configurer.
- `start` : Lance le script de changement automatique de description.
- `clear` : Efface les données affichées à l'écran.
- `exit` : Ferme le programme.

## Licence

Ce programme est sous licence MIT. Veuillez consulter le fichier `LICENSE` pour plus d'informations.
