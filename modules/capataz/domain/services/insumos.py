from flask_restful import Resource, reqparse
from index import api, db
from modules.capataz.domain.models.Insumo import Insumo
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel


class Insumos(Resource):
    def get(self):
        return parsemodel(Insumo.query.all())

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', type=str)
        parser.add_argument('detalles', type=str)
        parser.add_argument('unidades', type=str)
        args = parser.parse_args()
        isValid = hasRequiredFields(args, ["nombre", "detalles", "unidades"])
        if not isValid:
            return None, 400
        nombre = args['nombre']
        detalles = args['detalles']
        unidades = args['unidades']
        insumo = Insumo(nombre=nombre, detalles=detalles, unidades=unidades)
        db.session.add(insumo)
        db.session.commit()
        return insumo.toJSON(), 201


def insumos():
    api.add_resource(Insumos, '/insumos')
