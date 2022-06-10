from index import db


class Enfermedad(db.Model):
    __tablename__ = "enfermedades"
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
