from flask import Blueprint, abort, request, session
from database import orders, customers
from helpers import isChef, isDeliveryBoy, isLoggedIn, isManager, isCustomer
from database.shoppingCart import calcPrices, getDishes
from database.customers import getBalance, getMoneySpent, updateBalance, updateMoneySpent
from datetime import datetime

orderBlueprint = Blueprint('app_order', __name__, url_prefix = '/order')

@orderBlueprint.route('/', methods = ['GET', 'POST', 'DELETE'])
def index():    # route to handle requests
    if request.method == 'GET':   # Retrieve all items 
        if not (isChef() or isDeliveryBoy() or isManager()): abort(403) # not authorized
        
        try: return { 'response': orders.getAllOrders() }   # returns table in JSON format
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error

    elif request.method == 'POST': # Add item to menu
        if not isCustomer(): abort(403) # only customers should be able to order for now
        try:
            data = request.json # grab json data which is saved as a dictionary
            
            # convert dishIDs to string
            dishes = ','.join([str(dishID) for dishID in data['dishIDs']])
            
            # calculate price
            cost = calcPrices(data['dishIDs'], data['deliveryMethod']) 
            customer = customers.getCustomerByCustomerID(session['customerID'])
            
            # use store address if pickup
            if data['deliveryMethod'] == 'pickup':
                address = '160 Convent Ave, New York, NY 10031' # store address
            else: address = data['address']

            # check if user has enough money
            moneySpent = customer['moneySpent'] + cost
            newBalance = customer['balance'] - cost
            if newBalance < 0:
                newBalance = 0
                return abort(400, 'Insufficient funds.')

            newOrderCount = customer['numberOfOrders'] + 1
            orderID = orders.placeOrder(
                dishes, session['customerID'], address, cost,
                datetime.now(), data['deliveryMethod'], 'pending',
                newBalance, moneySpent, newOrderCount
            )
            print('Order Placed', orderID)
            return { 'response': { 'orderID': orderID } }

        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error

    elif request.method == 'DELETE': # deletes entire table
        if not isChef(): abort(403) # not authorized
        try: 
            orders.deleteTable()
            return { 'response': 'deleted' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)

@orderBlueprint.route('/<id>', methods = ['GET', 'PUT', 'DELETE'])
def order(id):
    if request.method == 'GET':
        try:
            order = orders.getOrderByID(id)
            dishes = getDishes(order['dishIDs']) # get dishes
            order['dishes'] = dishes # add dishes to order
            return { 'response': order }
        
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)
    
    elif request.method == 'PUT':
        if not isLoggedIn() or isDeliveryBoy() : abort(403)
        try:
            data = request.json
            dishes = ','.join( [ str(dishID) for dishID in data['dishIDs'] ] )
            print(dishes)
            print(data['customerID'])
            
            price = calcPrices( data['dishIDs'], data['deliveryMethod'] )
            print(price)
            if (isManager() or isChef()) and data['status'] == 'cancelled': 
                orders.updateOrder(id, dishes, data['customerID'], data['address'], price,
                    data['datetime'], data['deliveryMethod'], data['status'])
                balance = getBalance(data['customerID'])['balance']
                spent = getMoneySpent(data['customerID'])['balance']
                balance = balance + price
                spent = spent - price
                updateBalance(data['customerID'], balance)
                updateMoneySpent(data['customerID'], spent)
            else:
                orders.updateOrder(id, dishes, data['customerID'], data['address'], price,
                data['datetime'], data['deliveryMethod'], data['status'])
            return { 'response': orders.getOrderByID(id) }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)

    elif request.method == 'DELETE': # deletes specific items from table by ID
        if not isManager() and not isChef(): abort(403) # not authorized
        try:
            orders.getOrderByID(id)
            return { 'response': 'deleted' }
        
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)    

@orderBlueprint.route('/inprogress', methods=['GET'])
def inProgress():
    if request.method == 'GET':
        if not (isChef() or isDeliveryBoy()): abort(403) # not authorized
        try:
            ordersInProgress = orders.getOrdersInProgress()
            return { 'response': ordersInProgress }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)   