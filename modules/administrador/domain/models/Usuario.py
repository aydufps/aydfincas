from index import db
from modules.shared.infrastructure.helpers.sqlalchemyst import table_args


class Usuario(db.Model):
    __tablename__ = "usuarios"
    __table_args__ = table_args
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    clave = db.Column(db.String(200), nullable=True, default="")
    estado = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())

    def asJSON(self):
        return {
            "id": self.id,
            "nombre": self.name,
            "correo": self.email,
            "rol_id": self.rol_id,
            "estado": self.estado,
            "create_at": str(self.created_at.strftime('%Y-%m-%d')),
        }
