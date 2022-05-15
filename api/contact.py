from flask import Blueprint, abort, request
from database import contacts
from helpers import isManager

contactBlueprint = Blueprint('app_contacts', __name__, url_prefix = '/contacts')
@contactBlueprint.route('/', methods = ['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        try: return { 'response': contacts.getContacts() }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error
    
    elif request.method == 'POST':
        try:
            data = request.json
            contacts.addContact(data['name'], data['email'], data['message'], False)
            return { 'response': 'successfully posted contact form' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error

    elif request.method == 'DELETE':
        if not isManager(): abort(403)
        try:
            contacts.deleteTable()
            return { 'response': 'successfully deleted contacts table' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error

@contactBlueprint.route('/<id>', methods = ['GET', 'DELETE'])
def contact(id):
    if request.method == 'GET':
        try:
            contact = contacts.getContact(id)
            return { 'response': contact }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error
    
    elif request.method == 'DELETE':
        try:
            contacts.deleteContact(id)
            return { 'response': 'successfully deleted contact' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error
