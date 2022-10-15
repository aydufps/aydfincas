from index import db
from modules.shared.infrastructure.helpers.sqlalchemyst import table_args


class AnimalVacuna(db.Model):
    __tablename__ = "animales_vacunas"
    __table_args__ = table_args
    animal_id = db.Column(db.ForeignKey("animales.id"),
                          nullable=False, primary_key=True)
    vacuna_id = db.Column(db.Integer, db.ForeignKey("vacunas.id"),
                          nullable=False, primary_key=True)
    # vacuna_nombre = db.Column(db.String(50), db.ForeignKey("vacunas.nombre"),
    #                          nullable=False, primary_key=True)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    vacunas = db.relationship("Vacuna")
    animales = db.relationship("Animal")

    def asJSON(self):
        return {
            "animal_id": self.animal_id,
            "vacuna_id": self.vacuna_id,
            # "vacuna_nombre": self.vacuna_nombre,
            "estado": self.estado,
            "create_at": str(self.created_at.strftime('%Y-%m-%d')),
        }
