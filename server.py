from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect =  create_engine("sqlite:///chinook.db")
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from employees")
        return {'employees' : [i[0] for i in query.cursor.fetchall()]}

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        #return jsonify(result)
        return dumps(result, indent=4)

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)


class Customers(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from customers")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        print(dumps(result, indent=4))
        return dumps(result, indent=4


#routes
api.add_resource(Employees, '/employees') 
api.add_resource(Tracks, '/tracks')
api.add_resource(Employees_Name, '/employees/<employee_id>')
api.add_resource(Customers, '/customers')

if __name__ == '__main__':
    app.run(port='5002')
