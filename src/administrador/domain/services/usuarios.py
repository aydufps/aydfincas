from flask_restful import Resource, reqparse
from index import api, db
from src.administrador.domain.models.Usuario import Usuario
from src.shared.infrastructure.repositories.parsemodel import hasRequiredFields, parsemodel


class Usuarios(Resource):
    def get(self):
        return parsemodel(Usuario.query.all())

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('rol_id', type=str)
        parser.add_argument('clave', type=str)
        args = parser.parse_args()
        isValid = hasRequiredFields(args, ["name", "email", "rol_id", "clave"])
        if not isValid:
            return None, 400
        name = args['name']
        email = args['email']
        rol_id = args['rol_id']
        clave = args['clave']
        usuario = Usuario(name=name, email=email, rol_id=rol_id, clave=clave)
        db.session.add(usuario)
        db.session.commit()
        return usuario.toJSON(), 201


class UsuariosRol(Resource):
    def get(self, rol_id):
        return parsemodel(Usuario.query.filter(Usuario.rol_id == rol_id))


class UsuarioR(Resource):
    def get(self, id):
        item = Usuario.query.filter(Usuario.id == id).first()
        if item != None:
            return item.toJSON()
        return None


def loadusers():
    api.add_resource(Usuarios, '/usuarios')
    api.add_resource(UsuarioR, '/usuarios/<int:id>')
    api.add_resource(UsuariosRol, '/usuarios/rol/<int:rol_id>')
