from flask import Blueprint, abort, request, session
from database import ratings
import helpers
import datetime

orderBlueprint = Blueprint('app_order', __name__, url_prefix = '/ratings')
@orderBlueprint.route('/', methods = ['GET', 'POST', 'DELETE'])

def index():
    if request.method == 'GET':
        if not helpers.isCustomer(): abort(403) # not authorized
        
        try: return { 'response': ratings.getAllRatings()}   # returns table in JSON format
        except Exception as e:
            print(e, '\n')
            return abort(500) # returns internal server error
    elif request.method == 'POST': # Add rating to ratings 
        if not helpers.isCustomer(): abort(403) # only customers should be able to write reviews. 
        try:
            data = request.json # grab json data which is saved as a dictionary
            ratings.addRating(
                data['UserID'], data['Rating'], data['DishID']
            )
            return {'ratingID': 'successfully posted rating'}

        except Exception as e:
            print('error: ', e, '\n')
            return abort(500) # returns internal server error

    elif request.method == 'DELETE': # deletes entire table
        if not helpers.isCustomer(): abort(403) # not authorized
        try: 
            ratings.deleteTable()
            return { 'response': 'deleted' }
        except Exception as e:
            print(e, '\n')
            return abort(500)