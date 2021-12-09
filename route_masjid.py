
from flask import Flask, request, jsonify,Blueprint, render_template, session,abort
from app import db,ma
from database import Masjid
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_script import Manager
from flask_migrate import  Migrate

# from app_file1 import app_file1
# import testget
import os
import requests
route_masjid = Blueprint('route_masjid',__name__,url_prefix='/apio')
# ma = Marshmallow(app)

class MasjidSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name')

masjid_schema = MasjidSchema()
masjids_schema = MasjidSchema(many=True)


# # Get All masjid
# @route_masjid.route('/masjid', methods=['GET'])
# def get_products():
#   all_masjid = Masjid.query.all()
#   result = masjids_schema.dump(all_masjid)
#
#   # return jsonify(result.data)
#   return jsonify(result)

# Create a Product
@route_masjid.route('/masjid', methods=['POST'])
def add_masjid():
  name = request.json['name']

  # print(name)
  new_masjid = Masjid(name)
  # new_masjid = Masjid.query.get(1)
  # print(new_masjid)
  db.session.add(new_masjid)
  db.session.commit()

  return masjid_schema.jsonify(new_masjid)

# Get All masjid
@route_masjid.route('/masjid', methods=['GET'])
def get_products():
  all_masjid = Masjid.query.all()
  result = masjids_schema.dump(all_masjid)

  # return jsonify(result.data)
  return jsonify(result)

# Get Single Products
@route_masjid.route('/masjid/<id>', methods=['GET'])
def get_all_masjid(id):
  product = Masjid.query.get(id)
  return masjid_schema.jsonify(product)

# Update a Product
@route_masjid.route('/masjid/<id>', methods=['PUT'])
def update_product(id):
  masjid = Masjid.query.get(id)

  name = request.json['name']

  masjid.name = name


  db.session.commit()

  return masjid_schema.jsonify(masjid)

# Delete Product
@route_masjid.route('/masjid/<id>', methods=['DELETE'])
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
@route_masjid.route('/',methods=['GET'])
def get():
    return jsonify({'msg':'Hello World'})

