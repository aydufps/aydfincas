# Sistema de Gestion de Gincas Ganaderas

[API_URL](https://aydfincas.herokuapp.com/)

```
npm i -g heroku
heroku login
heroku create aydfincas --buildpack heroku/python
git add .
git commit -m "Flask-Restful-Heroku api"
heroku git:remote -a aydfincas
git push heroku master
```

## SQLAlchemy

from modules.administrador.domain.models.Models import User
from modules.administrador.domain.models.Models import Product
from modules.administrador.domain.models.Models import Order

```
from index import db
from modules.administrador.domain.models.Rol import Rol
from modules.administrador.domain.models.Usuario import Usuario
from modules.capataz.domain.models.Insumo import Insumo
from modules.veterinario.domain.models.Vacuna import Vacuna
from modules.veterinario.domain.models.Animal import Animal
db.create_all()
db.session.commit()

from modules.veterinario.domain.models.AnimalVacuna import AnimalVacuna
Animal.vacunas = db.relationship("AnimalVacuna") #warning ya existe la clave
db.create_all()
db.session.commit()
AnimalVacuna.vacuna = db.relationship("Vacuna") #warning ya existe la clave
db.create_all()
db.session.commit()

from modules.veterinario.domain.models.models import Association, Parent, Child
from modules.veterinario.domain.models.models import AnimalVacuna, Animal, Vacuna
db.create_all()
db.session.commit()

db.session.add(AnimalVacuna(animal_id=1, vacuna_id=1))
db.session.commit()

db.create_all()
rolAdm = Rol(id = 1, description = "Adm Rol")
db.session.add(rolAdm)
db.session.add(Child(id=1))
db.session.add(Parent(id=2))
db.session.add(Association(left_id=2, right_id=1, extra_data="Primer"))
db.session.add(Association(left_id=2, right_id=1, extra_data="Primer"))
db.session.add(AnimalVacuna(animal_id=1, vacuna_id=1))
db.session.add(Vacuna(id=2))
db.session.commit()
vacuna = db.relationship("Vacuna")
db.metadata.clear()

Rol.query.all()
Association.query.all()
Parent.query.all()
Child.query.all()

AnimalVacuna.query.all()
Animal.query.all()
Vacuna.query.all()


###
from modules.veterinario.domain.models.Enfermedad import Enfermedad
db.create_all()
db.session.commit()

###



```

## _Extras_

```
try:
<use session>
session.commit()
except:
session.rollback()
raise
finally:
session.close() # optional, depends on use case
```
