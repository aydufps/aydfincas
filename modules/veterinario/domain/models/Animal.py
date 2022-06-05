from datetime import datetime

from index import db
from modules.veterinario.domain.models.AnimalVacuna import association_table


class Animal(db.Model):
    __tablename__ = "animales"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String, nullable=False)
    detalles = db.Column(db.String, nullable=False)
    fechaRegistro = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    estado = db.Column(db.Boolean, nullable=False, default=True)
    #vacunas = db.relationship("AnimalVacuna", back_populates="animal")
    vacunas = db.relationship("Vacuna", secondary=association_table)

    def toJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "detalles": self.detalles,
            "estado": self.estado,
            "fecha_registro": str(self.fechaRegistro.strftime('%Y-%m-%d')),
            "vacunas": str(self.vacunas)
        }
