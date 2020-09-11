from db import db
from modules.Person import Person


class PersonalInfo(db.Model, Person):
    __tablename__ = "PersonalInfo"
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(40))
    job_start_date = db.column(db.string(15))
    job_finish_date = db.column(db.string(15))
    address = db.column(db.string(50))
    email = db.column(db.string(15))
    phone = db.column(db.string(15))
    category = db.Column(db.String(70))

    def __init__(self, _id, name, salary_type, job_start_date, job_finish_date, address, email, phone, category):
        super().__init__(_id, name, category, salary_type)
        self.id = _id
        self.name = name
        self.job_start_date = job_start_date
        self.job_finish_date = job_finish_date
        self.address = address
        self.email = email
        self.phone = phone
        self.category = category

    def salary_for_period(self,):
        return

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
        _id = self.id
        db.session.delete(self)
        db.session.commit()