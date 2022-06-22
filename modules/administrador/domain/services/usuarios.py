from flask_restful import Resource, reqparse
from index import api, db
from modules.administrador.domain.models.Usuario import Usuario
from modules.shared.infrastructure.repositories.SendEmail import enviarEmail
from modules.shared.infrastructure.repositories.parsemodel import hasRequiredFields


class Usuarios(Resource):
    def get(self):
        return [rol.asJSON() for rol in Usuario.query.all()]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('rol_id', type=str)
        parser.add_argument('clave', type=str)
        args = parser.parse_args()
        isValid = hasRequiredFields(args, ["name", "email", "rol_id"])
        if not isValid:
            return None, 400
        name = args['name']
        email = args['email']
        rol_id = args['rol_id']
        usuario = Usuario(name=name, email=email, rol_id=rol_id)
        try:
            db.session.add(usuario)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        finally:
            enviarEmail(email, name, usuario.id)
        return usuario.asJSON(), 201

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True,
                            help="El campo id es obligatorio")
        parser.add_argument('nombre', type=str)
        parser.add_argument('correo', type=str)
        parser.add_argument('rol_id', type=str)
        args = parser.parse_args()
        id = args['id']
        item = Usuario.query.get_or_404(id)
        item.name = args['nombre']
        item.email = args['correo']
        item.rol_id = args['rol_id']
        try:
            db.session.add(item)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return item.asJSON(), 201


class UsuariosRol(Resource):
    def get(self, rol_id):
        return [i.asJSON() for i in Usuario.query.filter(Usuario.rol_id == rol_id)]


class UsuarioR(Resource):
    def get(self, id):
        item = Usuario.query.filter(Usuario.id == id).first()
        if item != None:
            return item.asJSON()
        return None


class ItemRouter(Resource):

    def delete(self, id):
        item = Usuario.query.get(id)
        try:
            db.session.delete(item)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return item.asJSON(), 204


def loadusers():
    api.add_resource(Usuarios, '/usuarios')
    api.add_resource(UsuarioR, '/usuarios/<int:id>')
    api.add_resource(UsuariosRol, '/usuarios/rol/<int:rol_id>')
    api.add_resource(ItemRouter, '/usuario/<int:id>')
