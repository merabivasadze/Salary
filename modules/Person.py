from db import db

class Person(db.Model):
    __tablename__ = "Persons"

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(40))
    category = db.Column(db.String(70))
    salary_type = db.Column(db.string(20))

    def __init__(self, _id, name, category, salary_type):
        self.id = _id
        self.name = name
        self.category = category
        self.salary_type = salary_type
