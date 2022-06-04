from flask_restful import Resource, reqparse
from index import api, db
from src.administrador.domain.models.Usuario import Usuario
from src.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel


class Login(Resource):
    def get(self):
        return parsemodel(Usuario.query.all())

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str)
        parser.add_argument('clave', type=str)
        args = parser.parse_args()
        isValid = hasRequiredFields(args, ["clave", "email"])
        if not isValid:
            return None, 400
        clave = args['clave']
        email = args['email']
        item = Usuario.query.filter(Usuario.email == email).filter(
            Usuario.clave == clave).first()
        if item != None:
            return item.toJSON(), 200
        return None, 401


def loadauth():
    api.add_resource(Login, '/login')
