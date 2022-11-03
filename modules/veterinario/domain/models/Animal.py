from index import db
from modules.shared.infrastructure.helpers.sqlalchemyst import table_args


class Animal(db.Model):
    __tablename__ = "animales"
    __table_args__ = table_args

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    detalles = db.Column(db.String(100), nullable=False, default="")
    precio = db.Column(db.String(100), nullable=False, default="")
    estado = db.Column(db.Boolean, nullable=False, default=True)
    genero = db.Column(db.Boolean,  nullable=False, default=False)
    enVenta = db.Column(db.Boolean,  nullable=False, default=False)
    padre_id = db.Column(db.Integer, db.ForeignKey("animales.id"))
    madre_id = db.Column(db.Integer, db.ForeignKey("animales.id"))
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    vacunas = db.relationship("AnimalVacuna")
    created_at = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())

    def asJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "detalles": self.detalles,
            "precio": self.precio,
            "estado": self.estado,
            "genero": self.genero,
            "enVenta": self.enVenta,
            "padre_id": self.padre_id,
            "madre_id": self.madre_id,
            "vacunas": [i.asJSON() for i in self.vacunas],
            "create_at": str(self.created_at.strftime('%Y-%m-%d')),
            "fecha_nacimiento": str(self.fecha_nacimiento.strftime('%Y-%m-%d')),
        }
