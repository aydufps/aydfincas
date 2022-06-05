from index import db


class Association(db.Model):
    __tablename__ = "association"
    left_id = db.Column(db.ForeignKey("left.id"), primary_key=True)
    right_id = db.Column(db.ForeignKey("right.id"), primary_key=True)
    extra_data = db.Column(db.String(50))
    child = db.relationship("Child")


class Parent(db.Model):
    __tablename__ = "left"
    id = db.Column(db.Integer, primary_key=True)
    children = db.relationship("Association")


class Child(db.Model):
    __tablename__ = "right"
    id = db.Column(db.Integer, primary_key=True)
