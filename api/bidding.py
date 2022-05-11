from urllib import response
from flask import Blueprint, abort, request, session
from database import bidding
import helpers
import datetime

bidsBlueprint = Blueprint('app_bids', __name__, url_prefix = '/bids')

@bidsBlueprint.route('/', methods = ['GET', 'POST', 'DELETE'])
def index(): # route to handle requests
    if request.method == 'GET':   # Retrieve all items from menu
        if not helpers.isManager(): abort(403) # not authorized
        
        try: return { 'response': bidding.getAllBids() } 
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error

    elif request.method == 'POST':
        if not helpers.isDeliveryBoy(): abort(403)
        try:
            data = request.json
            bidding.addBid( session['employeeID'], data['amount'], data['orderID'] )
            return { 'response': 'successfully posted bid' }

        except Exception as e:
            print('error: ', e, '\n')
            abort(500)

    elif request.method == 'DELETE': # deletes entire table
        if not helpers.isManager(): abort(403) # not authorized
        try: 
            bidding.deleteTable()
            return { 'response': 'deleted' }
        except Exception as e:
            print(e, '\n')
            abort(500)

@bidsBlueprint.route('/<id>', methods = ['GET', 'DELETE'])
def bid(bidID):
    if request.method == 'GET':
        # if not helpers.isDeliveryBoy(): abort(403)
        try: return { 'response': bidding.getBidsByID(bidID) }
        except Exception as e:
            print(e, '\n')
            abort(500)
                
    elif request.method == 'DELETE':
        if not helpers.isDeliveryBoy() or not helpers.isManager(): abort(403) # not authorized
        try: 
            bidding.deleteBid(bidID)
            return { 'response': 'deleted' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)

@bidsBlueprint.route('/orderID/<id>', methods = ['GET', 'DELETE'])
def bidsOnOrder(orderID):
    if request.method == 'GET':
        if not helpers.isManager(): abort(403)
        
        try: return { 'response': bidding.getBidsByOrderID(orderID) }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)
                
    elif request.method == 'DELETE':
        if not helpers.isManager(): abort(403) # not authorized
        try: 
            bidding.deleteBidByOrderID(orderID)
            return { 'response': 'deleted' }
        
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)