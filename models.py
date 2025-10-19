from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)
    baked_date = db.Column(db.Date, nullable=False)

    #new
    ingredients = db.Column(db.String(300), nullable=True)
    is_gluten_free = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "baked_date": self.baked_date.isoformat(),
            "ingredients": self.ingredients,
            "is_gluten_free": self.is_gluten_free,
        }
