from index import db


class Vacuna(db.Model):
    __tablename__ = "vacunas"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String, nullable=False)
    detalles = db.Column(db.String, nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    animales = db.relationship("AnimalVacuna", back_populates="vacuna")

    def toJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "detalles": self.detalles,
            "estado": self.estado
        }
