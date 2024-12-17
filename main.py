import os
from db import create_db, faker_products
import server

# Initialiser la base de données si elle n'existe pas
if not os.path.exists("db.sql"):
    print("Base de données non existante, création en cours...")
    create_db()
    faker_products()
    print("Base de données et produits fictifs créés.")

# Démarrer le serveur Flask
print("Démarrage du serveur...")
server.app.run(debug=True, port=8080)