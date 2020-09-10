from db import db


class PersonReview(db.Model):
    __tablename__ = "PersonReview"
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(40))
    reports = db.column(db.string(100))
    
    def __init__(self, _id, name , reports):
        self.id = _id
        self.name = name
        self.reports = reports

    def job_review(self):
        pass

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
