# Will handle all requests for menu in here
from flask import Blueprint, abort, request
import menu # imports from ./menu.py

menuBlueprint = Blueprint('app_menu', __name__, url_prefix='/menu')
 
@menuBlueprint.route('/', methods = ['GET', 'POST', 'DELETE']) # url would be {address}/api/menu
def index():    # route to handle requests for menu
    if request.method == 'GET':     # Retrieve all items from menu
        try: return { 'response': menu.getAll() }   # returns table in JSON format
        except: return abort(500)   # returns internal server error

    elif request.method == 'POST': # Add item to menu
        try:
            data = request.json # grab json data which is saved as a dictionary
            menu.add( data['name'], data['img_url'], data['description'], data['price'])
            return { 'response': menu.getAll() }
        except Exception as e:
            print(e)
            print("\n")
            return abort(500) # returns internal server error

    elif request.method == 'DELETE': #deletes entire table
        try: 
            menu.deleteAll()
            return { 'response': 'deleted' }
        except Exception as e:
            print(e)
            return abort(500)

@menuBlueprint.route('/<id>', methods = ['GET', 'DELETE', 'PUT']) # url would be {address}/api/menu/<id> 
def menuItems(id):
    if request.method == 'GET':     # Retrieve a specific item from menu
        try: return { 'response': menu.getById(id) }    # returns row in JSON format
        except Exception as e: 
            print(e)
            return abort(500)   # returns internal server error
    
    elif request.method == 'DELETE':    # deletes specific items from table by ID
        try:
            menu.deleteById(id)
            return { 'response': 'deleted' }
        except Exception as e:
            print(e)
            return abort(500)
    
    elif request.method == "PUT":
        try:
            data = request.json 
            menu.updateByID(id, data['name'], data['img_url'], data['description'], data['price'])
            return { 'response': menu.getAll() }
        except Exception as e:
            print(e)
            return abort(500)
