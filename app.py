
from flask_restful import reqparse
from src.administrador.domain.services.usuarios import loadusers
from src.administrador.domain.services.roles import loadroles
from src.auth.domain.services.login import loadauth
from index import app, api

parser = reqparse.RequestParser()


loadauth()
loadroles()
loadusers()

if __name__ == '__main__':
    app.run(debug=True)
