from flask import Blueprint, abort, request, session
from database import orders, customers
import helpers


walletBlueprint = Blueprint('app_wallet', __name__, url_prefix = '/wallet')

@walletBlueprint.route('/', methods = ['GET', 'PUT'])
def index():
    if request.method == 'GET':
        if not helpers.isLoggedIn(): return abort(403)
        try:
            customer = customers.getCustomerByCustomerID(session['customerID'])
            balance = customer['balance']
            return {'response': {'balance' : balance}}
        except Exception as e:
            print('error:', e, '\n')
            return abort(500)   # returns internal server error

    elif request.method == 'PUT':
        if not helpers.isLoggedIn(): return abort(403)
        try:
            data = request.json

            customer = customers.getCustomerByCustomerID(session['customerID'])
            customer['balance'] += float(data['balance'])
            customers.updateCustomer(session['customerID'], customer['name'], customer['phoneNumber'],
                customer['vipStatus'], customer['balance'], customer['numberOfOrders'], customer['moneySpent'],
                customer['shoppingCartID'], customer['karen'], customer['demotionPoints'])
            provisional = customers.getCustomerByCustomerID(session['customerID'])
            return {'response' : {'balance' : provisional['balance']}}
        except Exception as e:
            print('error: ', e, '\n')
            return abort(500)
