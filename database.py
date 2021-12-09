from init import db,app
from flask_migrate import  Migrate
# from passlib.apps import custom_app_context as pwd_context
migrate = Migrate(app, db)


# Product Class/Model
class Masjid(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(150))

  def __init__(self, name):
    self.name = name

class User_dimas(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  username = db.Column(db.String(32))
  password = db.Column(db.String(32))
  user_type = db.Column(db.Integer)  # 1 super admin #2 admin #3 user
  masjid_id = db.Column(db.Integer)


  def __init__(self, name,username,password,user_type,masjid_id):
      self.name = name
      self.username = username
      self.password = password
      self.user_type =user_type
      self.masjid_id = masjid_id



