from flask_restful import Resource
from index import api, mail
from flask_mail import Message
from flask_restful import Resource, reqparse
from modules.administrador.domain.models.Usuario import Usuario

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


def loadmail():
    api.add_resource(Mail, '/mail')
