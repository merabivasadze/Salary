from db import db
from modules.Person import Person


class PersonReview(db.Model, Person):
    __tablename__ = "PersonReview"
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(40))
    category = db.Column(db.String(40))
    manager = db.Column(db.String(40))
    date = db.Column(db.DATE)  # need help
    reports = db.column(db.string(100))
    performance_score = db.Column(db.String(20))
    
    def __init__(self, _id, name, reports, category, salary_type, manager, date):
        super().__init__(_id, name, category, salary_type)
        self.id = _id
        self.name = name
        self.reports = reports
        self.manager = manager
        self.date = date
        self.performance_score = performance_score()

    def performance_score(self):
        score = "scored by manager"
        return score


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_db(cls):
        persons = cls.query.filter_by().all()
        return persons

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
