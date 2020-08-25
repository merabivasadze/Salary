from flask import Flask, redirect
from flask_restful import Api
from flask_jwt import JWT
from resource.AddUser import AddNewUser
from Security import authentification, identity

from resource.MyEmployeesList import MyEmployeesList, Employee


app = Flask(__name__)
app.secret_key = "JohnIsAegon"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
jwt = JWT(app, authentification, identity)

@app.route('/')
def redirect2url():
    return redirect("https://documenter.getpostman.com/view/11858352/T1LV7hv3?version=latest")


api.add_resource(Employee, '/MyFirstApi/<string:name>')
api.add_resource(MyEmployeesList, '/MyFirstApi')
api.add_resource(AddNewUser, '/AddNewUser/<string:name>')


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    print("Demo line")
    app.run(port=5000, debug=True)
