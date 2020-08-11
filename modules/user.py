from db import db


class UserModule(db.Model):
    __tablename__ = "users"

    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(40), unique=False, nullable=False)

    def __init__(self, _id, username, password):
        self.id = UserModule.id_identificator(_id)
        self.username = username
        self.password = password

    @classmethod
    def id_identificator(cls, _id):
        persons = UserModule.get_db()
        if persons:
            for person in persons:
                if _id == person.id:
                    _id += 1
            return _id
        else:
            return _id

    @classmethod
    def find_by_username(cls, username):
        return UserModule.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, userid):
        return UserModule.query.filter_by(id=userid).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_db(cls):
        users = cls.query.filter_by().all()
        return users
