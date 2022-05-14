import json
from flask import Blueprint, abort, request, session
from database import orders, chefOrder
from helpers import isChef, isDeliveryBoy, isLoggedIn, isManager, isCustomer
from datetime import datetime

chefOrderBlueprint = Blueprint('app_chefOrder', __name__, url_prefix = '/chefOrder')
@chefOrderBlueprint.route('/', methods = ['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':  # Retrieve all items 
        if not (isChef() or isDeliveryBoy() or isManager()): abort(403) # not authorized
        try: return { 'response': chefOrder.getAllChefOrders() }   # returns table in JSON format
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error
    
    elif request.method == 'POST': # Add item to menu
        if not isChef(): abort(403)       
        try: 
            data = request.json
            chefOrder.addOrdertoChef( ## Helper function should prob get this? idk
                chefID = data['chefID'],
                orderID = data['orderID'],
                amount = data['amount'], 
                status = data['status']
            )
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error

    elif request.method == 'DELETE':
        if not isManager(): abort(403)
        try:
            chefOrder.deleteTable()
            return { 'response': 'Chef Orders table has been deleted' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error

@chefOrderBlueprint.route('/<orderID>/<itemID>', methods = ['GET', 'POST', 'DELETE'])
def index(orderID, itemID):
    if request.method == 'GET':   # Retrieve all items 
        if not (isChef() or isDeliveryBoy() or isManager()): abort(403) # not authorized
        try: # returns table in JSON format
            return { 'response': chefOrder.getChefOrderByID(itemID, orderID) } 
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error
    
    elif request.method == 'POST': # method could update the chef order
        if not isChef(): abort(403)
        try:
            data = request.json
            chefOrder.updateChefOrder( itemID, data['chefID'], orderID, data['amount'], data['status'])
            return { 'response': 'successfully updated Chef Order' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error

    elif request.method == 'DELETE':
        if not (isManager() or isChef()): abort(403)
        try:
            chefOrder.deleteChefOrder(itemID, orderID)
            return { 'response': 'Chef Order has been deleted' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error