from index import db


class ModelAdministrador(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)

    def toJSON(self):
        rep = {
            "user_id": self.user_id,
            "user_name": self.user_name
        }
        return rep
