from index import db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def toJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
