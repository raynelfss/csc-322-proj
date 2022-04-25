from flask import Blueprint, abort, request, session
from database import shoppingCart
import helpers

cartBlueprint = Blueprint('app_cart', __name__, url_prefix = '/cart')
@cartBlueprint.route('/', methods = ['DELETE']) 
def index():
    if request.method == 'DELETE':
        if not helpers.isManager(): abort(403)
        try:
            shoppingCart.deleteAllCarts()
        except Exception as e:
            print(e, '\n')
            return abort(500)

@cartBlueprint.route('/<id>', methods = ['GET', 'PUT', 'DELETE'])
def cart(shoppingCartID):
    if request.method == 'GET':
        try:
            return { 'response': shoppingCart.displayCartByID(shoppingCartID) }
        except Exception as e:
            print(e, '\n')
            return abort(500)
    
    elif request.method == 'PUT':
        try:
            data = request.json
            dishes = ','.join( [ str(dishID) for dishID in data['dishIDs'] ] )
            price = helpers.calcPrices( data['dishIDs'], data['DeliveryMethod'] ) 
            shoppingCart.updateCart(shoppingCartID, dishes, price)
            return { 'response': shoppingCart.displayCartByID(shoppingCartID) }
        except Exception as e:
            print(e, '\n')
            return abort(500)

    elif request.method == 'DELETE':
        try:
            shoppingCart.deleteCart(shoppingCartID)
            return { 'response': 'deleted' }
        except Exception as e:
            print(e, '\n')
            return abort(500)

