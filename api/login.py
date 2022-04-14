from passlib.hash import sha256_crypt
from flask import Blueprint, abort, request, session, redirect
import userlogin

loginBlueprint = Blueprint('app_login', __name__, url_prefix = '/auth')

@loginBlueprint.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        try: 
            data = request.json
            user = login(data['username'])
            correct = sha256_crypt.verify(data['password'], user[2]) 
            # verifies the password and returns True if correct
            if correct:
                session['loggedIn'] = True
                return redirect('/') # redirects to homepage
            else:
                return 'password is incorrect'
            
        except Exception as e:
            print(e, '\n')
            return abort(500)

@loginBlueprint.route('/register', methods = ['POST'])
def register():
    if request.method == 'POST':
        try: 
            data = request.json
            hashedPassword = sha256_crypt.encrypt(data['password']) #hashes password
            userlogin.register(data['username'], hashedPassword)
            session['loggedIn'] = True
            return redirect('/') # redirects to homepage
        except Exception as e:
            print(e, '\n')
            return abort(500)



