from index import db
from modules.shared.infrastructure.helpers.sqlalchemyst import table_args


class Enfermedad(db.Model):
    __tablename__ = "enfermedades"
    __table_args__ = table_args
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    detalles = db.Column(db.String(200), nullable=False, default="")
    estado = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())

    def asJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "detalles": self.detalles,
            "estado": self.estado,
            "create_at": str(self.created_at.strftime('%Y-%m-%d')),
        }
