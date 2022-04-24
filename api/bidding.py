from flask import Blueprint, abort, request, session
from database import orders, customers, bidding
import helpers
import datetime

bidsBlueprint = Blueprint('app_bids', __name__, url_prefix = '/bids')
@bidsBlueprint.route('/', methods = ['GET', 'POST', 'DELETE'])

def index(): # route to handle requests
    if request.method == 'GET':   # Retrieve all items from menu
        if not helpers.isManager(): abort(403) # not authorized
        try: return { 'response': bidding.getAllBids() } 
        except Exception as e:
            print(e, '\n')
            return abort(500) # returns internal server error

    elif request.method == 'POST':
        if not helpers.isDeliveryBoy(): abort(403)
        try:
            data = request.json
            bidding.addBid(
                data['bidID'], session['employeeID'],
                data['amount'], data['orderID']
            )
            return { bidding.getAllBids() }

        except Exception as e:
            print(e, '\n')
            return abort(500)

    elif request.method == 'DELETE': # deletes entire table
        if not helpers.isManager(): abort(403) # not authorized
        try: 
            bidding.deleteTable()
            return { 'response': 'deleted' }
        except Exception as e:
            print(e, '\n')
            return abort(500)

@bidsBlueprint.route('/<id>', methods = ['GET', 'DELETE'])
def order(bidID):
    if request.method == 'GET':
        try: return { 'response': bidding.getBidByID(bidID) }
        except Exception as e:
            print(e, '\n')
            return abort(500)
                
    elif request.method == 'DELETE':
        if not helpers.isManager(): abort(403) # not authorized
        try: 
            bidding.deleteBid(bidID)
            return { 'response': 'deleted' }
        except Exception as e:
            print(e, '\n')
            return abort(500)
