from db import db


class EmployeeModules(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(40))
    category = db.Column(db.String(70))
    salary = db.Column(db.FLOAT(precision=2))
    salaryType = db.Column(db.String(15))

    def __init__(self, _id, name, category, fixed_amount, salary_type, percentage, sale_amount):
        self.id = EmployeeModules.id_identificator(_id)
        self.name = name
        self.category = category
        self.salary_type = salary_type
        self.salary = self.calculate_salary(fixed_amount, percentage, sale_amount)

    def calculate_salary(self, fixed_amount, percentage, sale_amount):
        if self.salary_type == 'fixed':
            salary = self.fixed_amount
        elif self.salary_type == 'mixed':
            salary = sale_amount * percentage / 100 + fixed_amount
        else:
            salary = sale_amount * percentage / 100
        return salary

    @classmethod
    def id_identificator(cls, _id):
        persons = EmployeeModules.get_db()
        if persons:
            for person in persons:
                if _id == person.id:
                    _id += 1
            return _id
        else:
            return _id

    def json(self):
        return {"ID": self.id, "name": self.name, "category": self.category, "salary": self.salary}

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
        persons = EmployeeModules.get_db()
        for person in persons:
            if person.id > _id:
                person.id -= 1
                person.save_to_db()
