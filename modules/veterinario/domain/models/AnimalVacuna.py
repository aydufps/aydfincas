from datetime import datetime
from index import db


class AnimalVacuna(db.Model):
    __tablename__ = "animales_vacunas"
    animal_id = db.Column(db.ForeignKey("animales.id"), primary_key=True)
    vacuna_id = db.Column(db.ForeignKey("vacunas.id"), primary_key=True)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    fechaRegistro = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    vacuna = db.relationship("Vacuna")

    def toJSON(self):
        return {
            "animal_id": self.animal_id,
            "vacuna_id": self.vacuna_id,
            "estado": self.estado,
            "fecha_registro": str(self.fechaRegistro.strftime('%Y-%m-%d')),
            # "vacunas":  self.vacunas[0].toJSON()
        }
