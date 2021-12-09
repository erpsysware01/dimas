#
# from flask import Flask, request, jsonify,Blueprint
# # from app import db,app
# from database import User_dimas
# from flask_marshmallow import Marshmallow
#
# route_user = Blueprint('route_user',__name__)
# ma = Marshmallow(app)
#
# class UserSchema(ma.Schema):
#   class Meta:
#     fields = ('id', 'name','username','password','user_type','masjid_id')
#
# user_schema = UserSchema()
# users_schema = UserSchema(many=True)
#
#
# # Create a Product
# @route_user.route('/user', methods=['POST'])
# def add_user():
#   name = request.json['name']
#   username = request.json['username']
#   password = request.json['password']
#   user_type = request.json['user_type']
#   masjid_id = request.json['masjid_id']
#
#   new_user = User_dimas(name,username,password,user_type,masjid_id)
#
#   db.session.add(new_user)
#   db.session.commit()
#
#   return user_schema.jsonify(new_user)
#
# # Get All masjid
# @route_user.route('/user', methods=['GET'])
# def get_products():
#   all_user = User_dimas.query.all()
#   result = users_schema.dump(all_user)
#
#   # return jsonify(result.data)
#   return jsonify(result)
#
# # Get Single Products
# @route_user.route('/user/<id>', methods=['GET'])
# def get_all_masjid(id):
#   user = User_dimas.query.get(id)
#   return user_schema.jsonify(user)
#
# # Update a Product
# @route_user.route('/user/<id>', methods=['PUT'])
# def update_user(id):
#   user = User_dimas.query.get(id)
#
#   name = request.json['name']
#   username = request.json['username']
#   password = request.json['password']
#   user_type = request.json['user_type']
#   masjid_id = request.json['masjid_id']
#
#   user.name = name
#   user.username = username
#   user.password = password
#   user.user_type = user_type
#   user.masjid_id = masjid_id
#
#   db.session.commit()
#
#   return user_schema.jsonify(user)
#
# # Delete Product
# @route_user.route('/user/<id>', methods=['DELETE'])
# def delete_masjid(id):
#   # masjid = Masjid.query.get(id)
#   # # Masjid.query.filter_by(id=id).delete()
#   # # db.session.add(Masjid)
#   # db.session.delete(masjid)
#   # #
#   # db.session.commit()
#   record_obj = db.session.query(User_dimas).filter(User_dimas.id == id).first()
#   db.session.delete(record_obj)
#   db.session.commit()
#
#   return user_schema.jsonify(record_obj)
#
#
# @route_user.route('/user_login', methods=['POST'])
# def user_login():
#
#   username = request.json['username']
#   password = request.json['password']
#   record_obj = db.session.query(User_dimas).filter(User_dimas.username == username,
#                                                    User_dimas.password == password).first()
#
#
#   # new_user = User_dimas(name,username,password,user_type,masjid_id)
#
#   # db.session.add(new_user)
#   # db.session.commit()
#
#   return user_schema.jsonify(record_obj)
#
