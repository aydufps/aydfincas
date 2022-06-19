from flask_restful import Resource
from index import api, mail
from flask_mail import Message

from modules.shared.infrastructure.repositories.SendEmail import enviarEmail
# from modules.shared.infrastructure.repositories.SendEmail import enviarEmail

emisor = "jefersonurielhc@ufps.edu.co"
receptor = "asimplemailmore@gmail.com"
asunto = "Cambio de clave"
mensaje = ""
clave = "mjsytbqwyfgsgzdg"


# enviarEmail()


class Mail(Resource):
    def post(self):
        # msg = Message('Hello', sender='jefersonurielhc@ufps.edu.co',
        #              recipients = ['asimplemailmore@gmail.com'])
        # msg.body = "Hello Flask message sent from Flask-Mail"
        # mail.send(msg)
        enviarEmail()
        return "Sent"


def loadmail():
    api.add_resource(Mail, '/mail')
