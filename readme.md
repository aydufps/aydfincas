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
from modules.administrador.domain.models.Rol import Rol
from modules.administrador.domain.models.Usuario import Usuario
from modules.capataz.domain.models.Insumo import Insumo
from modules.veterinario.domain.models.Animal import Animal
from modules.veterinario.domain.models.Vacuna import Vacuna
from modules.veterinario.domain.models.AnimalVacuna import AnimalVacuna

db.create_all()
rolAdm = Rol(id = 1, description = "Adm Rol")
db.session.add(rolAdm)
db.session.commit()

db.metadata.clear()

Rol.query.all()

### anexos

api url

https://aydfincas.herokuapp.com/

class User(Base):
id = Column(Integer, primary_key=True, index=True)
username = Column(String(64), index=True, unique=True)
email = Column(String(120), index=True, unique=True)
state = Column(String(30))
venues = relationship("Venue")
role = Column(String(10), default="customer")
