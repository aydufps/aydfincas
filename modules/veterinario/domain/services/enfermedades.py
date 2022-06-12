from flask_restful import Resource, reqparse
from index import api, db
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel
from modules.veterinario.domain.models.AnimalVacuna import AnimalVacuna
from modules.veterinario.domain.models.Enfermedad import Enfermedad
from modules.veterinario.domain.models.Vacuna import Vacuna


class Enfermedades(Resource):
    def get(self):
        return [i.asJSON() for i in Enfermedad.query.all()]

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
        enfermedad = Enfermedad(nombre=nombre, detalles=detalles)
        try:
            db.session.add(enfermedad)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return enfermedad.asJSON(), 201


def enfermedades():
    api.add_resource(Enfermedades, '/enfermedades')
