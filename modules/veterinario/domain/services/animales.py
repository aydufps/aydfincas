import argparse
from datetime import date, datetime
from flask_restful import Resource, reqparse
from index import api, db
from modules.administrador.domain.models.Rol import Rol
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel
from modules.veterinario.domain.models.Animal import Animal


def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


class Animales(Resource):
    def get(self):
        return [rol.asJSON() for rol in Animal.query.all()]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', type=str, required=True,
                            help="El campo nombre es obligatorio")
        parser.add_argument('padre_id', type=str, required=True,
                            help="El campo padre_id es obligatorio")
        parser.add_argument('madre_id', type=str, required=True,
                            help="El campo madre_id es obligatorio")
        parser.add_argument('detalles', type=str, required=True,
                            help="El campo detalles es obligatorio")
        parser.add_argument('fecha_nacimiento', type=valid_date, required=True,
                            help="El campo fecha_nacimiento es obligatorio")
        args = parser.parse_args()
        nombre = args['nombre']
        detalles = args['detalles']
        animal = Animal(nombre=nombre, detalles=detalles,
                        padre_id=args["padre_id"], madre_id=args["madre_id"], fecha_nacimiento=args["fecha_nacimiento"])
        try:
            db.session.add(animal)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return animal.asJSON(), 201


def animales():
    api.add_resource(Animales, '/animales')
