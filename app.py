from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_script import Manager
from flask_migrate import  Migrate

# from app_file1 import app_file1
# import testget
import os
import requests
################################################
####https://www.youtube.com/watch?v=PTZiDnuC86g#
################################################


#init app
app = Flask(__name__)
# app.register_blueprint(app_file1)
# app.register_blueprint(testget)
#DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iaqqzyhiqpcumq:d7a472e0ec5c4c4c5d633e50d2eff7cb1c3d3afa1262aa0902f7f29c76e0c8ee@ec2-44-198-211-34.compute-1.amazonaws.com:5432/dd8crl0af2jhnd'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://iaqqzyhiqpcumq:d7a472e0ec5c4c4c5d633e50d2eff7cb1c3d3afa1262aa0902f7f29c76e0c8ee@ec2-44-198-211-34.compute-1.amazonaws.com:5432/dd8crl0af2jhnd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

# Init DB
db =SQLAlchemy(app)
migrate = Migrate(app, db)
# from database import Masjid
# from database import User_dimas


# Init MA
ma = Marshmallow(app)



# # Product Class/Model
# class Product(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String(100), unique=True)
#   description = db.Column(db.String(200))
#   price = db.Column(db.Float)
#   qty = db.Column(db.Integer)

  # def __init__(self, name, description, price, qty):
  #   self.name = name
  #   self.description = description
  #   self.price = price
  #   self.qty = qty

# Product Schema
class MasjidSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name')

# Init schema
# product_schema = ProductSchema(strict=True)
# products_schema = ProductSchema(many=True, strict=True)
# For those getting this error "TypeError: __init__() got an unexpected keyword argument 'strict'
# ". Try to remove strict=True from both Schemas, as from marshmallow 3.x.x, Schemas are always strict.
# More info here: https://marshmallow.readthedocs.io/en/stable/upgrading.html
masjid_schema = MasjidSchema()
masjids_schema = MasjidSchema(many=True)

# Create a Product
@app.route('/masjid', methods=['POST'])
def add_masjid():
  name = request.json['name']


  new_masjid = Masjid(name)

  db.session.add(new_masjid)
  db.session.commit()

  return masjid_schema.jsonify(new_masjid)

# Get All masjid
@app.route('/masjid', methods=['GET'])
def get_products():
  all_masjid = Masjid.query.all()
  result = masjids_schema.dump(all_masjid)

  # return jsonify(result.data)
  return jsonify(result)

# Get Single Products
@app.route('/masjid/<id>', methods=['GET'])
def get_all_masjid(id):
  product = Masjid.query.get(id)
  return masjid_schema.jsonify(product)

# Update a Product
@app.route('/masjid/<id>', methods=['PUT'])
def update_product(id):
  masjid = Masjid.query.get(id)

  name = request.json['name']

  masjid.name = name


  db.session.commit()

  return masjid_schema.jsonify(masjid)

# Delete Product
@app.route('/masjid/<id>', methods=['DELETE'])
def delete_masjid(id):
  # masjid = Masjid.query.get(id)
  # # Masjid.query.filter_by(id=id).delete()
  # # db.session.add(Masjid)
  # db.session.delete(masjid)
  # #
  # db.session.commit()
  record_obj = db.session.query(Masjid).filter(Masjid.id == id).first()
  db.session.delete(record_obj)
  db.session.commit()

  return masjid_schema.jsonify(record_obj)


# @app.route('/')
# def hello():
#     return 'Hello world ***'
@app.route('/',methods=['GET'])
def get():
    return jsonify({'msg':'Hello World'})

if __name__== '__main__':
  # from database import User_test3

  from database import Masjid
  from database import User_dimas

  # db.create_all()
  app.run(debug=True)
  # app.run()

