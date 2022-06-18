from flask_restful import Resource, reqparse
from index import api, db
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel
from modules.veterinario.domain.models.AnimalVacuna import AnimalVacuna
from modules.veterinario.domain.models.Vacuna import Vacuna
import argparse
from datetime import date, datetime


def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


class Vacunas(Resource):
    def get(self):
        return [rol.asJSON() for rol in Vacuna.query.all()]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', type=str, required=True,
                            help="El campo nombre es obligatorio")
        parser.add_argument('detalles', type=str, required=True,
                            help="El campo detalles es obligatorio")
        parser.add_argument('fecha_vencimiento_lote', type=valid_date, required=True,
                            help="El campo fecha_vencimiento_lote es obligatorio")
        parser.add_argument('unidades', type=int)
        args = parser.parse_args()
        nombre = args['nombre']
        detalles = args['detalles']
        fecha_vencimiento_lote = args['fecha_vencimiento_lote']
        unidades = args['unidades']
        vacuna = Vacuna(nombre=nombre, detalles=detalles,
                        fecha_vencimiento_lote=fecha_vencimiento_lote, unidades=unidades)
        try:
            db.session.add(vacuna)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return vacuna.asJSON(), 201

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True,
                            help="El campo id es obligatorio")
        parser.add_argument('nombre', type=str)
        parser.add_argument('detalles', type=str)
        parser.add_argument('unidades', type=int)
        parser.add_argument('fecha_vencimiento_lote', type=valid_date)
        args = parser.parse_args()
        id = args['id']
        item = Vacuna.query.get_or_404(id)
        item.nombre = args['nombre']
        item.detalles = args['detalles']
        item.unidades = args['unidades']
        item.fecha_vencimiento_lote = args['fecha_vencimiento_lote']
        try:
            db.session.add(item)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return item.asJSON(), 201


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
