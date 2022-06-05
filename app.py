from flask_restful import reqparse, Resource
from index import app, api

from modules.administrador.domain.services.usuarios import loadusers
from modules.administrador.domain.services.roles import loadroles
from modules.auth.domain.services.login import loadauth
from modules.capataz.domain.services.insumos import insumos
from modules.veterinario.domain.services.animales import animales
from modules.veterinario.domain.services.vacunas import vacunas


parser = reqparse.RequestParser()


loadauth()
loadroles()
loadusers()
insumos()
animales()
vacunas()


class status (Resource):
    def get(self):
        try:
            return {'data': 'Utilise postman o insomia para hacer solicitudes a los endpoint'}
        except:
            return {'data': 'Algo salio mal'}


api.add_resource(status, '/')

if __name__ == '__main__':
    app.run()
