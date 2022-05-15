from flask import Blueprint, abort, request, session
from database import salaries
from helpers import isEmployee, isManager 

salaryBlueprint = Blueprint('app_salary', __name__, url_prefix = '/salary')
@salaryBlueprint.route('/', methods = ['GET', 'POST', 'DELETE'])
def index():
    if not isManager(): abort(403)
    if request.method == 'GET':
        try: return { 'response': salaries.getSalaries() }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)
    
    elif request.method == 'POST':
        try:
            data = request.json
            salaries.addSalary(data['employeeID'], data['salary'])
            return { 'response': 'successfully added employee salary'}
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)          

    elif request.method == 'DELETE':
        try:
            salaries.deleteTable()
            return { 'response': 'successfully deleted salary table'}
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)       

@salaryBlueprint.route('/<id>', methods = ['GET', 'PUT'])
def salary(id):
    if request.method == 'GET':
        if not (isEmployee() and (session['employeeID'] == id)): abort(403)
        try: return { 'response': salaries.getSalary(id) }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)

    elif request.method == 'PUT':
        if not isManager(): abort(403)
        try:
            data = request.json
            salaries.updateSalary(id, data['salary'])
            return { 'response': 'successfully updated employee salary'}
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)        