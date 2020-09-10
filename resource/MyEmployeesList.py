from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from modules.MyEmployeeModules import EmployeeModules


class Employee(Resource):
    # TBL_NAME = 'employees'
    parser = reqparse.RequestParser()
    parser.add_argument('category',
                        type=str,
                        required=True,
                        help="category field is empty"
                        )
    parser.add_argument('fixedAmount',
                        type=float,
                        required=False,
                        help="fixedAmount field is empty"
                        )
    parser.add_argument('salaryType',
                        type=str,
                        required=True,
                        help="salaryType field is empty"
                        )
    parser.add_argument('percentage',
                        type=float,
                        required=False,
                        help="percentage field is empty"
                        )
    parser.add_argument('saleAmount',
                        type=float,
                        required=False,
                        help="saleAmount field is empty"
                        )

    def get(self, name):
        person = EmployeeModules.find_by_name(name)
        if person:
            return person.json()
        return {"message": f"Person {name} does not exist"}, 404


    def post(self, name):
        if EmployeeModules.find_by_name(name):
            return {"message": f"Person {name} already exists"}, 400

        data = Employee.parser.parse_args()
        person = EmployeeModules(1, name, data["category"], data["fixedAmount"], data['salaryType'],
                                 data['percentage'],  data['saleAmount'])
        try:
            person.save_to_db()
        except:
            return {"message": f"Could not add {name}"}
        else:
            return person.json()

    def put(self, name):
        person = EmployeeModules.find_by_name(name)
        data = Employee.parser.parse_args()
        if person:
            person.category = data['category']
            person.salary_type = data['salaryType']
            person.calculate_salary(data["fixedAmount"], data['percentage'], data['saleAmount'])
            person.save_to_db()
            message = "updated in list"
        else:
            person = EmployeeModules(1, name, data["category"], data["fixedAmount"], data['salaryType'],
                                     data['percentage'], data['saleAmount'])
            person.save_to_db()
            message = "added to list"
        return {f"{message}": person.json()}

    def delete(self, name):
        person = EmployeeModules.find_by_name(name)

        if person:
            person.delete_from_db()
            return {"message": f"Person {name} deleted from database"}
        else:
            return {"message": "no such person in database"}


class MyEmployeesList(Resource):
    #@jwt_required()
    def get(self):
        persons = EmployeeModules.get_db()
        _persons = []
        for person in persons:
            _persons.append(person.json())
        return {"message": _persons}
