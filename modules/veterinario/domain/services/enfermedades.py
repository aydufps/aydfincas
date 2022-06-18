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

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True,
                            help="El campo id es obligatorio")
        parser.add_argument('nombre', type=str)
        parser.add_argument('detalles', type=str)
        args = parser.parse_args()
        id = args['id']
        item = Enfermedad.query.get_or_404(id)
        item.nombre = args['nombre']
        item.detalles = args['detalles']
        try:
            db.session.add(item)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return item.asJSON(), 201


class EnfermedadRouter(Resource):

    def delete(self, id):
        item = Enfermedad.query.get(id)
        try:
            db.session.delete(item)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return item.asJSON(), 204


def enfermedades():
    api.add_resource(Enfermedades, '/enfermedades')
    api.add_resource(EnfermedadRouter, '/enfermedad/<int:id>')
