from index import db


class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    clave = db.Column(db.String, nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True)

    def toJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "rol": self.rol_id,
            "clave": self.clave,
            "estado": self.estado
        }
