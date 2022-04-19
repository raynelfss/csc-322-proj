from flask import Blueprint, abort, request, session
from database import orders, customers
from helpers import isChef, isCustomer, calcPrices
from datetime import datetime


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
        if not isCustomer(): abort(403) # only customers should be able to order for now

        if True:
            data = request.json # grab json data which is saved as a dictionary
            # convert dishIDs to string
            dishes = ','.join([str(dishID) for dishID in data['dishIDs']])
            # calculate price
            cost = calcPrices(data['dishIDs'], data['deliveryMethod']) 
            customer = customers.getCustomerByCustomerID(session['customerID'])
            # check if user has enough money
            if data['deliveryMethod'] == 'pickup':
                address = '160 Convent Ave, New York, NY 10031' # store address
            else:
                address = data['address']
            newBalance = customer[5] - cost
            if newBalance < 0:
                newBalance = 0
                # ignore for now
                # return abort(400, 'Insufficient funds.')
            newOrderCount = customer[6] + 1
            orderID = orders.placeOrder(
                dishes,
                session['customerID'],
                address,
                cost,
                datetime.now(),
                data['deliveryMethod'],
                'pending',
                newBalance,
                newOrderCount
            )
            print('Order Placed', orderID)
            return { 'response': {'orderID': orderID}}
        # except Exception as e:
        #     print('error: ', e, '\n')
        #     return abort(500) # returns internal server error

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

@orderBlueprint.route('/inprogress', methods=['GET'])
def inprogress():
    if request.method == 'GET':
        if not isChef(): abort(403) # not authorized
        try:
            ordersInProgress = orders.getOrdersInProgress()
            return {'response': ordersInProgress}
        except Exception as e:
            print(e, '\n')
            return abort(500)   