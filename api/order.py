from asyncio.windows_events import NULL
from crypt import methods
from flask import Blueprint, abort, request, session
from database import orders
from helpers import isChef, calcPrices

orderBlueprint = Blueprint('app_order', __name__, url_prefix = '/order')

@orderBlueprint.route('/', methods = ['GET', 'POST', 'DELETE'])
def index():    # route to handle requests for menu
    if request.method == 'GET':   # Retrieve all items from menu
        if not isChef(): abort(403) # not authorized
        try: return { 'response': orders.viewAllOrders() }   # returns table in JSON format
        except Exception as e:
            print(e, '\n')
            return abort(500) # returns internal server error

    elif request.method == 'POST': # Add item to menu
        try:
            data = request.json # grab json data which is saved as a dictionary
            order = orders.addOrderToTable(
                data['OrderID'],
                data['DishIDs'],
                session['CustomerID'],
                data['Address'],
                data['Cost'],
                data['Datetime'],
                data['DeliveryMethod'],
                'pending'
            )
            return { 'response': order }
        except Exception as e:
            print(e, '\n')
            return abort(500) # returns internal server error

    elif request.method == 'DELETE': # deletes entire table
        if not isChef(): abort(403) # not authorized
        try: 
            orders.deleteTable()
            return { 'response': 'deleted' }
        except Exception as e:
            print(e, '\n')
            return abort(500)

@orderBlueprint.route('/<id>', methods = ['GET', 'PUT', 'DELETE'])
def order(id):
    if request.method == 'GET':
        try: return { 'response': orders.getOrderByID(id) }
        except Exception as e:
            print(e, '\n')
            return abort(500)
    
    elif request.method == 'PUT':
        #if not manager() : abort(403)
        try:
            data = request.json
            dishes = ','.join([str(dishID) for dishID in data['dishIDs']])
            price = calcPrices(data['dishIDs'], data['DeliveryMethod']) 
            orders.updateOrder(id, dishes, data['CustomerID'], data['Address'], price,
                data['Datetime'], data['deliveryMethod'], 'status')
            return { 'response': orders.getOrderByID(id) }
        except Exception as e:
            print(e, '\n')
            return abort(500)
    
    # elif request.method == 'DELETE': # deletes specific items from table by ID
    #     if not manager(): abort(403) # not authorized
    #     try:
    #         orders.deleteOrder(id)
    #         return { 'response': 'deleted' }
    #     except Exception as e:
    #         print(e, '\n')
    #         return abort(500)