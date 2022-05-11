from flask import Blueprint, abort, request, session
from database import employees
from helpers import isManager 

employeeBlueprint = Blueprint('app_employee', __name__, url_prefix = '/employee')

@employeeBlueprint.route('/', methods = ['GET', 'DELETE'])
def index():
    if request.method == 'GET':
        try: return { 'response': employees.getEmployees() }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)
    
    elif request.method == 'DELETE':
        if not isManager(): abort(403)
        try:
            employees.deleteTable()
            return { 'response': 'successfully deleted employee table'}
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)

@employeeBlueprint.route('/<id>', methods = ['GET', 'DELETE'])
def employee(userID):
    if request.method == 'GET':
        try: return { 'response': employees.getEmployee(userID) }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)
    elif request.method == 'DELETE':
        if not isManager(): abort(403)
        try:
            employees.fireEmployee(userID)
            return { 'response': 'successfully removed employee' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)