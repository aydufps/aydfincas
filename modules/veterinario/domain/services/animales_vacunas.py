from flask_restful import Resource, reqparse
from index import api, db
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel
from modules.veterinario.domain.models.AnimalVacuna import AnimalVacuna
from modules.veterinario.domain.models.Vacuna import Vacuna


class AnimalesVacunasRouter(Resource):
    def get(self):
        return parsemodel(AnimalVacuna.query.all())

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('vacuna_id', type=str)
        parser.add_argument('animal_id', type=str)
        args = parser.parse_args()
        isValid = hasRequiredFields(args, ["vacuna_id", "animal_id"])
        if not isValid:
            return None, 400
        animal_id = args['animal_id']
        vacuna_id = args['vacuna_id']
        vacuna = AnimalVacuna(animal_id=animal_id, vacuna_id=vacuna_id)
        db.session.add(vacuna)
        db.session.commit()
        return vacuna.toJSON(), 201


def animalesAndVacunasEndpoint():
    api.add_resource(AnimalesVacunasRouter, '/animales/vacunas')
