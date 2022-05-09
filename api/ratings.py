from crypt import methods
from flask import Blueprint, abort, request, session
from database import ratings
import helpers
import datetime

ratingBlueprint = Blueprint('app_ratings', __name__, url_prefix = '/ratings')

@ratingBlueprint.route('/', methods = ['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        if not helpers.isCustomer(): abort(403) # not authorized
        
        try: return { 'response': ratings.getAllRatings() }   # returns table in JSON format
        except Exception as e:
            print('error: ', e, '\n')
            return abort(500) # returns internal server error
    
    elif request.method == 'POST': # Add rating to ratings 
        if not helpers.isCustomer(): abort(403) # only customers should be able to write reviews. 
        try:
            data = request.json # grab json data which is saved as a dictionary
            ratings.addRating( data['UserID'], data['Rating'], data['DishID'] )
            return { 'ratingID': 'successfully posted rating' }

        except Exception as e:
            print('error: ', e, '\n')
            return abort(500) # returns internal server error

    elif request.method == 'DELETE': # deletes entire table
        if not helpers.isManager(): abort(403) # not authorized
        try: 
            ratings.deleteTable()
            return { 'response': 'deleted' }
        except Exception as e:
            print('error: ', e, '\n')
            return abort(500)

@ratingBlueprint.route('/<id>', methods = ['GET', 'DELETE'])
def rating(ratingId):
    if request.method == 'GET':
        try:
            rating = ratings.getRatingByID(ratingId)
            return { 'response': rating }
        except Exception as e:
            print('error: ', e, '\n')
            return abort(500)
    
    elif request.method == 'DELETE':
        try:
            ratings.deleteRating(ratingId)
            return { 'response': 'successfully deleted rating' }
        except Exception as e:
            print('error: ', e, '\n')
            return abort(500)