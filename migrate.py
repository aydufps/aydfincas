from index import db
from modules.administrador.domain.models.Rol import Rol
from modules.administrador.domain.models.Usuario import Usuario
from modules.capataz.domain.models.Insumo import Insumo
from modules.veterinario.domain.models.Animal import Animal
from modules.veterinario.domain.models.AnimalVacuna import AnimalVacuna
from modules.veterinario.domain.models.Enfermedad import Enfermedad
from modules.veterinario.domain.models.Vacuna import Vacuna

db.create_all()
db.session.commit()
