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
from modules.veterinario.domain.models.models import Association, Parent, Child

db.create_all()
rolAdm = Rol(id = 1, description = "Adm Rol")
db.session.add(rolAdm)
db.session.add(Child(id=1))
db.session.add(Parent(id=2))
db.session.add(Association(left_id=2, right_id=1, extra_data="Primer"))
db.session.commit()

db.metadata.clear()

Rol.query.all()
Association.query.all()
Parent.query.all()
Child.query.all()

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
