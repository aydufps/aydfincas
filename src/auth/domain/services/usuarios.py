from flask import jsonify
from flask_restful import Resource, reqparse
from index import api, db
from src.auth.domain.models.Rol import Rol
from src.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel


class Usuarios(Resource):
    def get(self):
        return parsemodel(Rol.query.all())

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('descripcion', type=str)
        args = parser.parse_args()
        isValid = hasRequiredFields(args, ["descripcion"])
        if not isValid:
            return None, 400
        description = args['descripcion']
        rol = Rol(description=description)
        db.session.add(rol)
        db.session.commit()
        return rol.toJSON(), 201


def loadroles():
    api.add_resource(Usuarios, '/usuarios')
