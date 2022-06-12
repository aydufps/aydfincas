from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, engine_from_config
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tigersjo_develop:Soporte2014@tigersjob.com.co/tigersjo_fincas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS '] = {'mysql_engine': 'InnoDB'}
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
