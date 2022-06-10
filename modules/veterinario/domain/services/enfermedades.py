from flask_restful import Resource, reqparse
from index import api, db
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel
from modules.veterinario.domain.models.AnimalVacuna import AnimalVacuna
from modules.veterinario.domain.models.Enfermedad import Enfermedad
from modules.veterinario.domain.models.Vacuna import Vacuna


class Enfermedades(Resource):
    def get(self):
        return parsemodel(Enfermedad.query.all())

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
        db.session.add(enfermedad)
        db.session.commit()
        return enfermedad.toJSON(), 201


def enfermedades():
    api.add_resource(Enfermedades, '/enfermedades')
