from index import db
from modules.shared.infrastructure.helpers.sqlalchemyst import table_args


class Rol(db.Model):
    __tablename__ = "roles"
    __table_args__ = table_args
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    usuarios = db.relationship("Usuario")

    def asJSON(self):
        return {
            "id": self.id,
            "descripcion": self.description,
            "estado": self.estado,
            "create_at": str(self.created_at.strftime('%Y-%m-%d')),
            "usuarios": [usuario.asJSON() for usuario in self.usuarios]
        }
