from passlib.hash import sha256_crypt
from flask import Blueprint, abort, request, session, redirect
from database import auth, customers, employees
from helpers import isLoggedIn

authBlueprint = Blueprint('app_login', __name__, url_prefix = '/auth')

@authBlueprint.route('/login', methods = ['POST'])
def login():
    if isLoggedIn(): redirect('/')
    if request.method == 'POST':
        try: 
            data = request.json # get user from db
            user = auth.getUserByUsername(data['username'])
            if not user:
                return abort(400, 'username does not exist')
            correct = sha256_crypt.verify(data['password'], user['passwordHash']) 
            # verifies the password and returns True if correct
            if not correct:
                return abort(400, 'password incorrect')
    
            session['loggedIn'] = True
            session['userID'] = user['userID']
            session['userType'] = user['role']
            if (user['role'] == 'employee'):
                # get employeeType
                employee = employees.getEmployee(user['userID'])
                session['employeeID'] = employee['employeeID']
                session['employeeType'] = employee['employeeType']
            elif (user[3] == 'customer'):
                customer = customers.getCustomerByUserID(user['userID'])
                session['customerID'] = customer['customerID']
            return redirect('/') # redirects to homepage
    
        except Exception as e:
            print(e, '\n')
            return abort(500)

@authBlueprint.route('/register', methods = ['POST']) # register customers
def register():
    if isLoggedIn(): redirect('/')
    if request.method == 'POST':
        try: 
            data = request.json
            passwordHash = sha256_crypt.encrypt(data['password']) # hashes password
            userID, customerID = customers.createCustomer(data['username'],
                passwordHash, data['name'], data['phoneNumber'])
            session['loggedIn'] = True
            session['userType'] = 'customer'
            session['userID'] = userID
            session['customerID'] = customerID
            print('Registered')
            return redirect('/') # redirects to homepage
        except Exception as e:
            print(e, '\n')
            return abort(500)





