from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import testget
import os
import requests
################################################
####https://www.youtube.com/watch?v=PTZiDnuC86g#
################################################


#init app
app = Flask(__name__)
#DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iaqqzyhiqpcumq:d7a472e0ec5c4c4c5d633e50d2eff7cb1c3d3afa1262aa0902f7f29c76e0c8ee@ec2-44-198-211-34.compute-1.amazonaws.com:5432/dd8crl0af2jhnd'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://iaqqzyhiqpcumq:d7a472e0ec5c4c4c5d633e50d2eff7cb1c3d3afa1262aa0902f7f29c76e0c8ee@ec2-44-198-211-34.compute-1.amazonaws.com:5432/dd8crl0af2jhnd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

# Init DB
db =SQLAlchemy(app)

# Init MA
ma = Marshmallow(app)

class User_test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)

    def __init__(self,username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username

# Product Class/Model
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)

  def __init__(self, name, description, price, qty):
    self.name = name
    self.description = description
    self.price = price
    self.qty = qty

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty')

# Init schema
# product_schema = ProductSchema(strict=True)
# products_schema = ProductSchema(many=True, strict=True)
# For those getting this error "TypeError: __init__() got an unexpected keyword argument 'strict'
# ". Try to remove strict=True from both Schemas, as from marshmallow 3.x.x, Schemas are always strict.
# More info here: https://marshmallow.readthedocs.io/en/stable/upgrading.html
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create a Product
@app.route('/product', methods=['POST'])
def add_product():
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  new_product = Product(name, description, price, qty)

  db.session.add(new_product)
  db.session.commit()

  return product_schema.jsonify(new_product)

# Get All Products
# @app.route('/product', methods=['GET'])
# def get_products():
#   all_products = Product.query.all()
#   result = products_schema.dump(all_products)
#
#   # return jsonify(result.data)
#   return jsonify(result)

# Get Single Products
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
  product = Product.query.get(id)
  return product_schema.jsonify(product)

# Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)

  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  product.name = name
  product.description = description
  product.price = price
  product.qty = qty

  db.session.commit()

  return product_schema.jsonify(product)

# Delete Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)


# @app.route('/')
# def hello():
#     return 'Hello world ***'
@app.route('/',methods=['GET'])
def get():
    return jsonify({'msg':'Hello World'})

if __name__== '__main__':
    # app.run(debug=True)
    app.run()