import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(
    os.path.join(os.path.dirname(__file__), 'app.db'))

db = SQLAlchemy(app)
