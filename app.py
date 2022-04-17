from flask import Flask, render_template, request, abort, redirect, session
from api.index import apiBlueprint #imports apiBlueprint from ./api/index.py
from helpers import isChef, isLoggedIn

app = Flask(__name__, static_url_path='', static_folder="build", template_folder='build')

@app.route('/')
def index(): 
    return render_template("main.html", currentUrl="/")

@app.route('/menu')
def menupage(): return render_template("menu.html")

@app.route('/menu/edit')
def menueditpage(): 
    if isChef():
        return render_template("menu-staff.html")
    else:
        return abort(403)

@app.route('/login')
def login():
    if isLoggedIn():
        return redirect('/') 
    return render_template("userlogin.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/register')
def register(): 
    if isLoggedIn():
        return redirect('/') 
    return render_template("register.html")

# all api calls /api
app.register_blueprint(apiBlueprint)

if __name__ == '__main__': 
    app.secret_key = 'deezNuts' 
    app.run(debug = True, use_reloader = True)
