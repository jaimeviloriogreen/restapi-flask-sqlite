
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin

from models import ModelProducts, Products
from settings import Connect

app = Flask(__name__)
CORS(app)

db_file = "database/database.sqlite3"
db = Connect()

#? Home
@cross_origin
@app.route("/")
def home():
    return render_template("index.html")

#? All products
@cross_origin
@app.route("/products")
def get_products():
    conn = db.get_connect(db_file)
    result = ModelProducts.all_products(conn)
    products = Products.to_dict(result)
    return jsonify(products)

#? One product
@cross_origin
@app.route("/product")
@app.route("/product/<string:name>")
def get_product(name = None):
    if name:
        conn = db.get_connect(db_file)
        result = ModelProducts.one_product(conn, name)
        
        if result:
            product = Products.to_dict(result)
            return jsonify(product)
        else:
            return jsonify({"Error":"No product name found!"})
            
    return  jsonify({"Error":"No product name given!"})

#? Delete one product
@cross_origin
@app.route("/product")
@app.route("/product/<string:name>",  methods=["DELETE"])
def delete_product(name = None):
    if name:
        conn = db.get_connect(db_file)
        result = ModelProducts.delete_product(conn, name)
        
        if(result > 0): 
            return jsonify({"deleted":"ok"})
        
        return jsonify({"Error":"No product name found!"})
            
    return  jsonify({"Error":"No product name given!"})

#? Update a product
@cross_origin
@app.route("/product", methods=["PUT"])
def update_product():
    to_update = request.json
    product = Products.validate_keys(to_update)
    
    if product:
        conn = db.get_connect(db_file)
        result = ModelProducts.update_product(conn, product)
        
        if( result > 0 ): return jsonify({"updated":"ok"})
        
    return  jsonify({"Error":"No product name found!"})
        
#? Add a product
@cross_origin
@app.route("/product", methods=["POST"])
def add_product():
    to_insert = request.json
    product = Products.validate_keys(to_insert)
    
    if product:
        conn = db.get_connect(db_file)
        result = ModelProducts.insert_product(conn, product)
        
        if( result > 0 ): return jsonify({"inserted":"ok"})
        
    return  jsonify({"Error":"No product have been inserted!"})
    
    
#? Error Handling
@app.errorhandler(404)
def page_error404(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.debug(debug=True)