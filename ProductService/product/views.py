from flask import Blueprint
from flask import request
from app import db
from product.model import Product

product_blueprint = Blueprint('product_blueprint', __name__)

@product_blueprint.route('/product', methods=['GET','POST'])
def product():
    
    if request.method == "POST":
        req = request.json
        product_name = req["name"]
        product_cost = req["price"]
    
        product_obj = Product(product_name = product_name, product_cost = product_cost)
        db.session.add(product_obj)
        db.session.commit()

        return "Product updated successfully"
    if request.method == "GET":
        product_dict = Product.query.all()
        res = []
        for p in product_dict:
            res.append(p.)
        