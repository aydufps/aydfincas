from datetime import datetime
from index import db
from modules.shared.infrastructure.repositories.parsemodel import parsemodel


class AnimalVacuna(db.Model):
    __tablename__ = "animales_vacunas"
    animal_id = db.Column(db.ForeignKey("animales.id"), primary_key=True)
    vacuna_id = db.Column(db.ForeignKey("vacunas.id"), primary_key=True)
    vacuna = db.relationship("Vacuna")


class Animal(db.Model):
    __tablename__ = "animales"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    detalles = db.Column(db.String, nullable=False, default="")
    fechaRegistro = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    estado = db.Column(db.Boolean, nullable=False, default=True)
    vacunas = db.relationship("AnimalVacuna")

    def toJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "detalles": self.detalles,
            "estado": self.estado,
            "fecha_registro": str(self.fechaRegistro.strftime('%Y-%m-%d')),
            "vacunas": parsemodel(self.vacunas)
        }


class Vacuna(db.Model):
    __tablename__ = "vacunas"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String, nullable=False)
    detalles = db.Column(db.String, nullable=False, default="")
    estado = db.Column(db.Boolean, nullable=False, default=True)

    def toJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "detalles": self.detalles,
            "estado": self.estado
        }
