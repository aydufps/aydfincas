from flask_restful import Resource, reqparse
from index import api, db
from modules.capataz.domain.models.Insumo import Insumo
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel


class Insumos(Resource):
    def get(self):
        return [i.asJSON() for i in Insumo.query.all()]

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
        try:
            db.session.add(insumo)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return insumo.asJSON(), 201

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True,
                            help="El campo id es obligatorio")
        parser.add_argument('nombre', type=str)
        parser.add_argument('detalles', type=str)
        parser.add_argument('unidades', type=str)
        args = parser.parse_args()
        id = args['id']
        item = Insumo.query.get_or_404(id)
        isValid = hasRequiredFields(args, ["nombre", "detalles", "unidades"])
        if not isValid:
            return None, 400
        item.nombre = args['nombre']
        item.detalles = args['detalles']
        item.unidades = args['unidades']
        try:
            db.session.add(item)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return item.asJSON(), 201


class SingleInsumo(Resource):

    def delete(self, id):
        item = Insumo.query.get(id)
        try:
            db.session.delete(item)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return item.asJSON(), 204


def insumos():
    api.add_resource(Insumos, '/insumos')
    api.add_resource(SingleInsumo, '/insumo/<int:id>')
