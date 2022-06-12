from flask_restful import Resource, reqparse, request
from index import api, db
from modules.administrador.domain.models.Usuario import Usuario
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel


class Login(Resource):
    def get(self):
        return parsemodel(Usuario.query.all())

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True,
                            help="El campo email es obligatorio")
        parser.add_argument('clave', type=str, required=True,
                            help="El campo clave es obligatorio")
        args = parser.parse_args()
        clave = args['clave']
        email = args['email']
        item = Usuario.query.filter(Usuario.email == email).filter(
            Usuario.clave == clave).first()
        if item != None:
            return item.asJSON(), 200
        return None, 401


def loadauth():
    api.add_resource(Login, '/login')
