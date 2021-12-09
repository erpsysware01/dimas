from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_script import Manager
from flask_migrate import  Migrate

# from route_test import app1
# from route_masjid import route_masjid


app = Flask(__name__)




# app.register_blueprint(app_file1)
# app.register_blueprint(testget)
#DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iaqqzyhiqpcumq:d7a472e0ec5c4c4c5d633e50d2eff7cb1c3d3afa1262aa0902f7f29c76e0c8ee@ec2-44-198-211-34.compute-1.amazonaws.com:5432/dd8crl0af2jhnd'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://iaqqzyhiqpcumq:d7a472e0ec5c4c4c5d633e50d2eff7cb1c3d3afa1262aa0902f7f29c76e0c8ee@ec2-44-198-211-34.compute-1.amazonaws.com:5432/dd8crl0af2jhnd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
#
# Init DB
db =SQLAlchemy(app)
migrate = Migrate(app, db)
# from database import Masjid
# from database import User_dimas





# Init MA
ma = Marshmallow(app)



  #
from route_masjid import route_masjid
app.register_blueprint(route_masjid,url_prefix='/api')


