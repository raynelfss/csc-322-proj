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
            correct = sha256_crypt.verify(data['password'], user[2]) 
            # verifies the password and returns True if correct
            if correct:
                session['loggedIn'] = True
                session['userID'] = user[0]
                session['userType'] = user[3]
                if (user[3] == 'employee'):
                    # get employeeType
                    employee = employees.getEmployee(user[0])
                    session['employeeID'] = employee[0]
                    session['employeeType'] = employee[2]
                elif (user[3] == 'customer'):
                    customer = customers.getCustomerByUserID(user[0])
                    session['customerID'] = customer[0]
                return redirect('/') # redirects to homepage
            else: return 'password is incorrect'     
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
            userID, customerID = customers.createCustomer(data['username'], passwordHash,
                data['name'], data['phoneNumber'])
            session['loggedIn'] = True
            session['userType'] = 'customer'
            session['userID'] = userID
            session['customerID'] = customerID
            print('Registered')
            return redirect('/') # redirects to homepage
        except Exception as e:
            print(e, '\n')
            return abort(500)





