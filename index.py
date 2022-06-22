import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, engine_from_config
from flask_cors import CORS
from flask_mail import Mail
app = Flask(__name__)
app.debug = False
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
mail = Mail(app)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://rwoknghjanqvdf:9730eeb60bfb038f183fc4583bbef8e63046d70534f058faf6b988bd36428078@ec2-34-200-35-222.compute-1.amazonaws.com:5432/d22op733jj8jo3"

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(
#    os.path.join(os.path.dirname(__file__), 'app.db'))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tigersjo_develop:Soporte2014@tigersjob.com.co/tigersjo_fincas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
''' app.config['SQLALCHEMY_ENGINE_OPTIONS '] = {'mysql_engine': 'InnoDB'} '''
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jefersonurielhc@ufps.edu.co'
app.config['MAIL_PASSWORD'] = 'mjsytbqwyfgsgzdg'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
