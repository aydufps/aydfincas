from flask_restful import Resource
from index import app, api

from modules.administrador.domain.services.usuarios import loadusers
from modules.administrador.domain.services.roles import loadroles
from modules.auth.domain.services.login import loadauth
from modules.capataz.domain.services.insumos import insumos
from modules.shared.domain.services.mail import loadmail
from modules.veterinario.domain.services.animales import animales
from modules.veterinario.domain.services.animales_vacunas import animalesAndVacunasEndpoint
from modules.veterinario.domain.services.enfermedades import enfermedades
from modules.veterinario.domain.services.vacunas import vacunas


loadauth()
loadroles()
loadusers()
insumos()
animales()
vacunas()
animalesAndVacunasEndpoint()
enfermedades()
loadmail()


class status (Resource):
    def get(self):
        try:
            return {'data': 'Utilise postman o insomia para hacer solicitudes a los endpoint'}
        except:
            return {'data': 'Algo salio mal'}


api.add_resource(status, '/')

if __name__ == '__main__':
    app.run()
