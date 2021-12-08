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
# ma = Marshmallow(app)



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
# class MasjidSchema(ma.Schema):
#   class Meta:
#     fields = ('id', 'name')

# Init schema
# product_schema = ProductSchema(strict=True)
# products_schema = ProductSchema(many=True, strict=True)
# For those getting this error "TypeError: __init__() got an unexpected keyword argument 'strict'
# ". Try to remove strict=True from both Schemas, as from marshmallow 3.x.x, Schemas are always strict.
# More info here: https://marshmallow.readthedocs.io/en/stable/upgrading.html
# masjid_schema = MasjidSchema()
# masjids_schema = MasjidSchema(many=True)

# @app.route('/hello',methods=['GET'])
# def hello():
#     return jsonify({'msg':'Hello World'})

# @route_masjid.route('/',methods=['GET'])
# def get():
#     return jsonify({'msg':'Hello World'})


if __name__== '__main__':
    # from database import Masjid
  #   from database import User_dimas
  #
  from route_masjid import route_masjid
    # from route_use import route_user



  app.register_blueprint(route_masjid)
  # app.register_blueprint(route_user)
  # db.create_all()
  # app.run(debug=True)
  app.run()

