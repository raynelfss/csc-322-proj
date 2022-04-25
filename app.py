from flask import Flask, render_template, request, abort, redirect, session
from api.index import apiBlueprint #imports apiBlueprint from ./api/index.py
from helpers import isChef, isCustomer, isLoggedIn, getNav, getSidebarNav

app = Flask(__name__, static_url_path='', static_folder="build", template_folder='build')
app.secret_key = 'deezNuts' 

@app.route('/')
def index(): 
    return render_template("main.html", currentUrl="/", nav=getNav())

@app.route('/menu')
def menupage(): return render_template("menu.html", currentUrl="/menu", nav=getNav())

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard-page.html", nav=getSidebarNav(), currentUrl='/dashboard')

@app.route('/dashboard/menu')
def menueditpage(): 
    if isChef():
        return render_template("menu-staff.html", nav=getSidebarNav(), currentUrl='/dashboard/menu')
    else:
        return abort(403)

@app.route('/dashboard/orders')
def orderspage():
    if isChef():
        return render_template("orders-page.html", nav=getSidebarNav(), currentUrl='/dashboard/orders')
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

@app.route('/checkout')
def checkout():
    if not isCustomer():
        return abort(403)
    return render_template("checkout.html")

        
@app.route('/orders/<id>')
def order(id):
    return render_template("order.html")

@app.route('/bid')
def bid():
    return render_template("bids.html")

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

# all api calls /api
app.register_blueprint(apiBlueprint)

if __name__ == '__main__': 
    app.run(debug = True, use_reloader = True)
