from flask_restful import Resource
from index import api, mail
from flask_mail import Message
from flask_restful import Resource, reqparse
from modules.administrador.domain.models.Usuario import Usuario
from index import db

from modules.shared.infrastructure.repositories.SendEmail import enviarEmail
# from modules.shared.infrastructure.repositories.SendEmail import enviarEmail

emisor = "jefersonurielhc@ufps.edu.co"
receptor = "asimplemailmore@gmail.com"
asunto = "Cambio de clave"
mensaje = ""
clave = "mjsytbqwyfgsgzdg"


class Mail(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('correo', type=str, required=True,
                            help="El campo correo es obligatorio")
        args = parser.parse_args()
        item = Usuario.query.filter(Usuario.email == args["correo"]).first()
        if item != None:
            enviarEmail(args["correo"], item.name, item.id)
            return "Se ha enviado un correo de recuperacion de clave"
        return "No existe este usuario"


class MailRouter(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('clave', type=str, required=True,
                            help="El campo clave es obligatorio")
        parser.add_argument('id', type=int, required=True,
                            help="El campo id es obligatorio")
        args = parser.parse_args()
        item = Usuario.query.get_or_404(args['id'])
        item.clave = args['clave']
        try:
            db.session.add(item)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, 400
        return f'{item.name.capitalize()}, Se ha actualizado tu clave', 200


def loadmail():
    api.add_resource(Mail, '/mail')
    api.add_resource(MailRouter, '/nueva_clave')
