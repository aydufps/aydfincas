from flask_restful import Resource, reqparse
from index import api, db
from src.administrador.domain.models.Usuario import Usuario
from src.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel


class Login(Resource):
    def get(self):
        return parsemodel(Usuario.query.all())

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        args = parser.parse_args()
        isValid = hasRequiredFields(args, ["name", "email"])
        if not isValid:
            return None, 400
        name = args['name']
        email = args['email']
        user = Usuario(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return None, 200


def loadauth():
    api.add_resource(Login, '/login')
