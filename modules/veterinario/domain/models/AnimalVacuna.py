from datetime import datetime
from index import db

association_table = db.Table(
    "association",
    db.metadata,
    db.Column("animal_id", db.ForeignKey("animales.id")),
    db.Column("vacuna_id", db.ForeignKey("vacunas.id")),
)


class AnimalVacuna(db.Model):
    __tablename__ = "animales_vacunas"
    vacuna_id = db.Column(db.ForeignKey("vacunas.id"), primary_key=True)
    animal_id = db.Column(db.ForeignKey("animales.id"), primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    detalles = db.Column(db.String, nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    fechaRegistro = db.Column(
        db.DateTime, nullable=False, primary_key=True, default=datetime.now())
    #animal = db.relationship("Animal", back_populates="vacunas")
    #vacuna = db.relationship("Vacuna", back_populates="animales")

    def toJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "detalles": self.detalles,
            "estado": self.estado,
            "fecha_registro": str(self.fechaRegistro.strftime('%Y-%m-%d'))
        }
