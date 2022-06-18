from index import db
from modules.shared.infrastructure.helpers.sqlalchemyst import table_args


class Vacuna(db.Model):
    __tablename__ = "vacunas"
    __table_args__ = table_args
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    detalles = db.Column(db.String(50), nullable=False, default="")
    estado = db.Column(db.Boolean, nullable=False, default=True)
    animales = db.relationship("AnimalVacuna")
    created_at = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    fecha_vencimiento_lote = db.Column(db.Date, nullable=False)
    unidades = db.Column(db.Integer, nullable=False, default=0)

    def asJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "detalles": self.detalles,
            "estado": self.estado,
            "unidades": self.unidades,
            "create_at": str(self.created_at.strftime('%Y-%m-%d')),
            "animales": [i.asJSON() for i in self.animales],
            "fecha_vencimiento_lote": str(self.fecha_vencimiento_lote.strftime('%Y-%m-%d'))
        }
