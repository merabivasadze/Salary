from db import db

class Person(db.Model):
    __tablename__ = "Persons"

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(40))
    category = db.Column(db.String(70))

    def __init__(self, _id, name, category):
        self.id = _id
        self.name = name
        self.category = category
