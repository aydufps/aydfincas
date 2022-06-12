from flask import jsonify
from flask_restful import Resource, reqparse
from index import api, db
from modules.administrador.domain.models.Rol import Rol
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel


class Roles(Resource):
    def get(self):
        data = Rol.query.all()
        return [rol.asJSON() for rol in data]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('descripcion', type=str)
        args = parser.parse_args()
        isValid = hasRequiredFields(args, ["descripcion"])
        if not isValid:
            return None, 400
        description = args['descripcion']
        rol = Rol(description=description)
        try:
            db.session.add(rol)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return rol.asJSON(), 201


def loadroles():
    api.add_resource(Roles, '/roles')
