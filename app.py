
from flask_restful import reqparse, Resource

from src.administrador.domain.services.usuarios import loadusers
from src.administrador.domain.services.roles import loadroles
from src.auth.domain.services.login import loadauth
from index import app, api

parser = reqparse.RequestParser()


loadauth()
loadroles()
loadusers()


class status (Resource):
    def get(self):
        try:
            return {'data': 'Api is Running'}
        except:
            return {'data': 'An Error Occurred during fetching Api'}


api.add_resource(status, '/')

if __name__ == '__main__':
    app.run()
