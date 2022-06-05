from index import db


class Rol(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String, nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    usuarios = db.relationship("Usuario")

    def toJSON(self):
        return {
            "id": self.id,
            "descripcion": self.description,
            "estado": self.estado
        }
