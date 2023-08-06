from app import db

class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(20), unique=False, nullable=False)
    product_cost = db.Column(db.String(20), unique=False, nullable=False)

 
