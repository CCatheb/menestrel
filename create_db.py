from tinydb import TinyDB
import os

# Liste des scènes et phases
scenes = [
    "Ville", "Village", "Ruelle Sombre", "Plaine", "Marais", "Cave", 
    "Cimetière", "Forêt", "Temple", "Taverne", "Montagne", "Marché"
]
phases = ["Exploration", "Combat", "Repos"]

# Chemin du fichier dans le répertoire courant
db_path = os.path.join(os.getcwd(), "data.json")
if os.path.exists(db_path):
    os.remove(db_path)  # Supprime l'ancien fichier pour une nouvelle génération

# Initialisation de la base de données TinyDB
db = TinyDB(db_path)

# Génère les entrées pour chaque combinaison de scène et de phase
for scene in scenes:
    for phase in phases:
        for i in range(1, 4):  # Trois chemins par combinaison
            db.insert({
                "type": "music",
                "tags": {
                    "scene": scene,
                    "phase": phase
                },
                "path": f"{scene}/{phase}/{i}"
            })

# Message de confirmation
print(f"Base de données générée dans {db_path} avec toutes les entrées.")
