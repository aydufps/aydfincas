from flask_restful import Resource, reqparse
from index import api, db
from modules.administrador.domain.models.Rol import Rol
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel
from modules.veterinario.domain.models.Animal import Animal


class Animales(Resource):
    def get(self):
        return [rol.asJSON() for rol in Animal.query.all()]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', type=str)
        parser.add_argument('detalles', type=str)
        args = parser.parse_args()
        isValid = hasRequiredFields(args, ["nombre", "detalles"])
        if not isValid:
            return None, 400
        nombre = args['nombre']
        detalles = args['detalles']
        animal = Animal(nombre=nombre, detalles=detalles)
        try:
            db.session.add(animal)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return animal.asJSON(), 201


def animales():
    api.add_resource(Animales, '/animales')
