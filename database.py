from app import db,app
from flask_migrate import  Migrate
from passlib.apps import custom_app_context as pwd_context
migrate = Migrate(app, db)

class User_dimas(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(30))
    user_type = db.Column(db.Integer)

# Product Class/Model
class Masjid(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(150))


  def __init__(self, name):
    self.name = name

