from flask_restful import Resource, reqparse
from index import api, db
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel
from modules.veterinario.domain.models.AnimalVacuna import AnimalVacuna
from modules.veterinario.domain.models.Vacuna import Vacuna


class Vacunas(Resource):
    def get(self):
        return [rol.asJSON() for rol in Vacuna.query.all()]

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
        vacuna = Vacuna(nombre=nombre, detalles=detalles)
        try:
            db.session.add(vacuna)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return vacuna.asJSON(), 201


class VacunaRouter(Resource):

    def delete(self, id):
        item = Vacuna.query.get(id)
        try:
            db.session.delete(item)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return item.asJSON(), 204


def vacunas():
    api.add_resource(Vacunas, '/vacunas')
    api.add_resource(VacunaRouter, '/vacuna/<int:id>')
