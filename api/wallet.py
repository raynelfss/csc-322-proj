from flask import Blueprint, abort, request, session
from database import customers
from helpers import isLoggedIn

walletBlueprint = Blueprint('app_wallet', __name__, url_prefix = '/wallet')
@walletBlueprint.route('/', methods = ['GET', 'PUT'])
def index():
    if request.method == 'GET':
        if not isLoggedIn(): abort(403)
        try:
            balance = customers.getBalance(session['customerID'])
            return {'response': { 'balance': balance['balance'] } }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)   # returns internal server error

    elif request.method == 'PUT':
        if not isLoggedIn(): abort(403)
        try:
            data = request.json
            balance = customers.getBalance(session['customerID'])
            balance['balance'] += float(data['balance'])
            customers.updateBalance(session['customerID'], balance['balance'])
            provisional = customers.getBalance(session['customerID'])
            
            return { 'response': { 'balance': provisional['balance'] } }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500)
