import argparse
from datetime import date, datetime

from flask_restful import Resource, reqparse
from index import api, db
from modules.administrador.domain.models.Rol import Rol
from modules.shared.infrastructure.repositories.parsemodel import (
    hasRequiredFields, parsemodel)
from modules.veterinario.domain.models.Animal import Animal
from modules.veterinario.domain.models.AnimalVacuna import AnimalVacuna


def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


class Animales(Resource):
    def get(self):
        return [rol.asJSON() for rol in Animal.query.all()]
        # return db.session.query(AnimalVacuna.animales).filter(AnimalVacuna.animal_id == id).all()

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
        parser.add_argument('genero', type=bool)
        args = parser.parse_args()
        nombre = args['nombre']
        detalles = args['detalles']
        animal = Animal(nombre=nombre, detalles=detalles,
                        padre_id=args["padre_id"], madre_id=args["madre_id"], fecha_nacimiento=args["fecha_nacimiento"], genero=args["genero"])
        try:
            db.session.add(animal)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return animal.asJSON(), 201

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True,
                            help="El campo id es obligatorio")
        parser.add_argument('nombre', type=str)
        parser.add_argument('padre_id', type=str)
        parser.add_argument('madre_id', type=str)
        parser.add_argument('detalles', type=str)
        parser.add_argument('precio', type=str)
        parser.add_argument('fecha_nacimiento', type=valid_date)
        parser.add_argument('genero', type=bool)
        parser.add_argument('enVenta', type=bool)
        args = parser.parse_args()
        id = args['id']
        item = Animal.query.get_or_404(id)
        item.nombre = item.nombre if args["nombre"] is None else args["nombre"]
        item.detalles = item.detalles if args["detalles"] is None else args["detalles"]
        item.precio = item.precio if args["precio"] is None else args["precio"]
        item.padre_id = item.padre_id if args["padre_id"] is None else args["padre_id"]
        item.madre_id = item.madre_id if args["madre_id"] is None else args["madre_id"]
        item.fecha_nacimiento = item.fecha_nacimiento if args[
            "fecha_nacimiento"] is None else args["fecha_nacimiento"]
        item.genero = item.genero if args["genero"] is None else args["genero"]
        item.enVenta = item.genero if args["enVenta"] is None else args["enVenta"]
        try:
            db.session.add(item)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            return None, 400
        return item.asJSON(), 201


class AnimalRouter(Resource):
    def get(self, id):
        return Animal.query.get_or_404(id).asJSON()

    def delete(self, id):
        item = Animal.query.get(id)
        try:
            db.session.delete(item)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return item.asJSON(), 204


class AnimalesEnVenta(Resource):
    def get(self):
        return [i.asJSON() for i in Animal.query.filter(Animal.enVenta == True)]


def animales():
    api.add_resource(Animales, '/animales')
    api.add_resource(AnimalesEnVenta, '/animales-en-venta')
    api.add_resource(AnimalRouter, '/animal/<int:id>')
