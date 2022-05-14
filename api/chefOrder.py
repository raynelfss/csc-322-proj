from flask import Blueprint, abort, request, session
from database import orders, chefOrder
from helpers import isChef, isDeliveryBoy, isLoggedIn, isManager, isCustomer

from datetime import datetime

chefOrderBlueprint = Blueprint('app_order', __name__, url_prefix = '/chefOrder')

@chefOrderBlueprint.route('/', methods = ['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':   # Retrieve all items 
        if not (isChef() or isDeliveryBoy() or isManager()): abort(403) # not authorized
        try: return { 'response': chefOrder.getAllChefOrders() }   # returns table in JSON format
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error
    
    elif request.method == 'POST': # Add item to menu
        if not isLoggedIn(): abort(403)         ##CHANGE THIS, Not really sure who should decide this
        try: 
            data = request.json

            chefOrder.addOrdertoChef(chefID = data['chefID']     
            ,orderID = data['orderID']  
            ,amount = data['amount']    ##Helper function should prob get this? idk
            ,status = data['status'])
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error

    elif request.method == 'DELETE':
        if not isManager(): abort(403)
        try:
            chefOrder.deleteTable()
            return {'response': 'cheforders table has been deleted'}
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error

@chefOrderBlueprint.route('/<id>', methods = ['GET', 'DELETE'])
def index(id):
    if request.method == 'GET':   # Retrieve all items 
        if not (isChef() or isDeliveryBoy() or isManager()): abort(403) # not authorized
        try: return { 'response': chefOrder.getChefOrderByID(id) }   # returns table in JSON format
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error
    #elif request.method == 'POST'
    #  method could update the chef order(too much work... I doubt we will use it this project)
    #  

    elif request.method == 'DELETE':
        if not isManager(): abort(403)
        try:
            chefOrder.deleteChefOrder(id)
            return {'response': 'cheforder has been deleted'}
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error