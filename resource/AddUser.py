from flask_restful import Resource, reqparse
from modules.user import UserModule


class AddNewUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="category field is empty"
                        )

    def post(self, name):
        if not UserModule.find_by_username(name):
            data = AddNewUser.parser.parse_args()
            person = UserModule(1, name, data['password'])
            person.save_to_db()
            return {"message": f"user {name} added successfully"}, 200
        return {"message": f"user {name} exists"}, 400

    def delete(self, name):
        person = UserModule.find_by_username(name)
        if person:
            person.delete_from_db()
            return {"message": f"{name} deleted from database"}
        else:
            return {"message": f"no such {name} in database"}
