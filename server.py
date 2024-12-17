from flask import Flask, jsonify, request
from flask_cors import CORS  # Importer CORS
import sqlite3
from model import Product

app = Flask(__name__)

# Appliquer CORS globalement sur toutes les routes
CORS(app)

# Route pour récupérer les produits avec pagination
@app.route("/products", methods=["GET"])
def get_products():
    # Récupérer le paramètre start (id_start)
    start = request.args.get("id_start", default=0, type=int)  # Default à 0 si non précisé
    limit = 24  # Nombre de produits par requête

    # Connexion à la base de données
    conn = sqlite3.connect("./db.sql")
    cursor = conn.cursor()

    # Requête SQL pour récupérer les produits à partir de `start` avec une limite de 24 produits
    cursor.execute("""
        SELECT * FROM products
        WHERE id >= ?
        LIMIT ?;
    """, (start, limit))
    
    rows = cursor.fetchall()
    conn.close()

    # Transformer les résultats en objets Product
    products = [
        Product(id=row[0], name=row[1], description=row[2], price=row[3], image_url=row[4]).to_dict()
        for row in rows
    ]

    return jsonify({"products": products})

if __name__ == "__main__":
    app.run(debug=True, port=8080)