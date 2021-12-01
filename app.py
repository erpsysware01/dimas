from flask import Flask
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://iaqqzyhiqpcumq:d7a472e0ec5c4c4c5d633e50d2eff7cb1c3d3afa1262aa0902f7f29c76e0c8ee@ec2-44-198-211-34.compute-1.amazonaws.com:5432/dd8crl0af2jhnd'
# db =SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Hello world ***'

if __name__== '__main__':
    app.run()