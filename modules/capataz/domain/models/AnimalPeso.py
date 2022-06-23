from index import db
from modules.shared.infrastructure.helpers.sqlalchemyst import table_args


class AnimalPeso(db.Model):
    __tablename__ = "animales_peso"
    __table_args__ = table_args
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    peso = db.Column(db.Float, nullable=False, default=0.0)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    nombre = db.Column(db.String, nullable=False, default="N/A")
    animal_id = db.Column(db.Integer, db.ForeignKey(
        "animales.id"), nullable=False, primary_key=True)
    created_at = db.Column(
        db.DateTime, server_default=db.func.current_timestamp(), primary_key=True)

    def asJSON(self):
        return {
            "id": self.id,
            "peso": self.peso,
            "estado": self.estado,
            "animal_id": self.animal_id,
            "nombre": self.nombre,
            "create_at": str(self.created_at.strftime('%Y-%m-%d'))
        }
