### Deploy en heroku

npm i -g heroku
heroku login
heroku create aydfincas --buildpack heroku/python
git add .
git commit -m "Flask-Restful-Heroku api"
heroku git:remote -a aydfincas
git push heroku master

### Sql alchemist

from index import db
from src.auth.domain.models.Rol import Rol
from src.auth.domain.models.Usuario import Usuario
db.create_all()
rolAdm = Rol(id = 1, description = "Adm Rol")
db.session.add(rolAdm)
db.session.commit()

db.metadata.clear()

Rol.query.all()

### anexos

api url

https://aydfincas.herokuapp.com/
