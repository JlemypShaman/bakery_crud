from flask import Flask, request, jsonify, render_template
from models import db, Product
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error": "Nie znaleziono produktu"}), 404
    return jsonify(product.to_dict())

@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()
    if not data.get("name") or not data.get("price") or not data.get("baked_date"):
        return jsonify({"error": "Brak wymaganych pól"}), 400
    product = Product(
        name=data["name"],
        description=data.get("description", ""),
        price=data["price"],
        baked_date=date.fromisoformat(data["baked_date"])
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201

@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error": "Nie znaleziono produktu"}), 404
    data = request.get_json()
    product.name = data.get("name", product.name)
    product.description = data.get("description", product.description)
    product.price = data.get("price", product.price)
    if "baked_date" in data:
        product.baked_date = date.fromisoformat(data["baked_date"])
    db.session.commit()
    return jsonify(product.to_dict())

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error": "Nie znaleziono produktu"}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Produkt został usunięty"}), 200

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
