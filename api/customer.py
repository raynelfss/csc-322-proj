from flask import Blueprint, abort, request, session
from database import customers
from helpers import isLoggedIn, isManager

customerBlueprint = Blueprint('app_customer', __name__, url_prefix = '/customer')

@customerBlueprint.route('/', methods = ['GET', 'DELETE'])
def index():
    if request.method == 'GET':
        
        try: return { 'response': customers.getAllCustomers() }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)
    
    elif request.method == 'DELETE':
        if not isManager(): abort(403)
        try:
            customers.deleteCustomerTable() 
            return { 'response': 'successfully deleted customer table' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)

@customerBlueprint.route('/<id>', methods = ['GET', 'POST', 'DELETE'])
def customer(customerID): 
    if request.method == 'GET':
        try:
            customer = customers.getCustomerByCustomerID(customerID)
            return { 'response': customer }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)
    
    elif request.method == 'POST':
        if not isManager(): abort(403)
        try:
            data = request.json
            customers.updateCustomer(customerID, session['userID'], data['name'], data['phoneNumber'],
                data['vipStatus'], data['balance'], data['numberOfOrders'], data['moneySpent'],
                data['shoppingCartID'], data['karen'], data['demotionPoints'])
            return { 'response': 'successfully updated customer info' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)
    
    elif request.method == 'DELETE':
        if not isManager(): abort(403)
        try:
            customers.deleteCustomer(customerID)
            return { 'response': 'successfully deleted customer info' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)

@customerBlueprint.route('/editcustomer', methods = ['GET', 'PUT'])
def updateCustomer():
    if not isLoggedIn(): abort(403)
    if request.method == 'GET':
        try:
            customer = customers.getCustomerByUserID(session['userID'])
            return {'response': {'name' : customer['name'], 'number' : customer['phoneNumber']}}
        except Exception as e:
            print('error:', e, '\n')
            abort(500)   
    elif request.method == 'PUT':
        try:
            data = request.json
            customer = customers.getCustomerByUserID(session['userID'])
            customers.updateCustomer(customer['customerID'], data['name'], data['number'],
            customer['vipStatus'], customer['balance'], customer['numberOfOrders'], customer['moneySpent'],
            customer['shoppingCartID'], customer['karen'], customer['demotionPoints'])
            return {'response' : { 'name': customers.getCustomerByUserID(session['userID'])['name'], 'number' : customers.getCustomerByUserID(session['userID'])['phoneNumber']}}
        except Exception as e:
            print('error:', e, '\n')
            abort(500)