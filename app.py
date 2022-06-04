
from flask_restful import Resource, reqparse
from src.administrador.domain.services.usuarios import loadusers
from src.auth.domain.services.roles import loadroles
from src.shared.infrastructure.repositories.parsemodel import parsemodel
from src.auth.domain.models.ModelAdministrador import ModelAdministrador
from src.auth.domain.services.login import loadauth
from index import app, api

parser = reqparse.RequestParser()


class SingIn(Resource):
    def get(self):
        items = ModelAdministrador.query.all()
        return parsemodel(items)

    def post(self, todo_id):
        print(todo_id)
        args = parser.parse_args()
        return args, 201
        # return TODOS[todo_id], 201


loadauth()
loadroles()
loadusers()
api.add_resource(SingIn, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
