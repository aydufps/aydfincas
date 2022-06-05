from index import db


class Insumo(db.Model):
    __tablename__ = "insumos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String, nullable=False)
    detalles = db.Column(db.String, nullable=False)
    unidades = db.Column(db.Integer, nullable=False, default=0)
    estado = db.Column(db.Boolean, nullable=False, default=True)

    def toJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "detalles": self.detalles,
            "unidades": self.unidades,
            "estado": self.estado
        }
