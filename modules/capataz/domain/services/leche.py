from flask_restful import Resource, reqparse
from index import api, db
from modules.capataz.domain.models.AnimalLeche import AnimalLeche
from modules.capataz.domain.models.AnimalPeso import AnimalPeso
from modules.capataz.domain.models.Insumo import Insumo
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel


class AnimalesLecheRouter(Resource):
    def get(self):
        return [i.asJSON() for i in AnimalLeche.query.all()]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('litros', type=float, required=True,
                            help="El campo litros es obligatorio")
        parser.add_argument('animal_id', type=str, required=True,
                            help="El campo animal_id es obligatorio")
        parser.add_argument('nombre', type=str, required=True,
                            help="El campo nombre es obligatorio")
        parser.add_argument('unidades', type=str)
        args = parser.parse_args()
        item = AnimalLeche(
            litros=args['litros'], animal_id=args['animal_id'], nombre=args["nombre"])
        try:
            db.session.add(item)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return item.asJSON(), 201


def animalesprodleche():
    api.add_resource(AnimalesLecheRouter, '/animales_produccion_leche')
