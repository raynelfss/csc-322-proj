from flask import Flask, render_template, request, abort, redirect, session
from api.index import apiBlueprint #imports apiBlueprint from ./api/index.py
import helpers
app = Flask(__name__, static_url_path = '', static_folder = "build", template_folder = 'build')
app.secret_key = 'deezNuts' 

@app.route('/')
def index(): 
    return render_template("main.html", currentUrl = "/", nav = helpers.getNav())

@app.route('/menu')
def menupage(): return render_template("menu.html", currentUrl = "/menu", nav = helpers.getNav())

# Dashboard pages.
@app.route('/dashboard')
def dashboard():
    if helpers.isLoggedIn():
        return render_template("dashboard-page.html", nav = helpers.getSidebarNav(), currentUrl = '/dashboard')
    else: return abort(403)

@app.route('/dashboard/menu')
def menueditpage(): 
    if helpers.isChef() or helpers.isManager():
        return render_template("menu-staff.html", nav = helpers.getSidebarNav(), currentUrl = '/dashboard/menu')
    else: return abort(403)

@app.route('/dashboard/orders')
def orderspage():
    if helpers.isChef() or helpers.isManager():
        return render_template("orders-page.html", nav = helpers.getSidebarNav(), currentUrl = '/dashboard/orders')
    else: return abort(403)

@app.route('/dashboard/settings')
def dashsettings():
    if helpers.isLoggedIn():
        return render_template("dashboard-settings.html", nav = helpers.getSidebarNav(), currentUrl = '/dashboard/settings')
    else: return abort(403)

@app.route('/dashboard/wallet')
def dashWallet():
    if helpers.isLoggedIn() and helpers.isCustomer():
        return render_template("dashboard-wallet.html", nav = helpers.getSidebarNav(), currentUrl = '/dashboard/wallet')
    else: return abort(403)

@app.route('/dashboard/bid')
def bid():
    if helpers.isLoggedIn() and helpers.isDeliveryBoy():
        return render_template("bid-page.html", nav = helpers.getSidebarNav(), currentUrl = '/dashboard/bid')

@app.route('/dashboard/deliverystatus')
def deliverystatus():
    if helpers.isLoggedIn():
        return render_template("dashboard-deliverystat.html", nav = helpers.getSidebarNav(), currentUrl = '/dashboard/deliverystatus')

@app.route('/dashboard/chefprogress')
def chefprogress(): 
    if helpers.isLoggedIn() and (helpers.isChef() or helpers.isManager()):
        return render_template("dashboard-chefprogress.html", currentUrl = "/chefprogress", nav = helpers.getSidebarNav())
    else: return abort(403)

@app.route('/dashboard/chefprogress/<id>')
def orderstatus(id):
    if helpers.isLoggedIn() and (helpers.isChef() or helpers.isManager()):
        return render_template("dashboard-chefprogress-order.html", currentUrl = "/chefprogress", nav = helpers.getSidebarNav())
    else: return abort(403)

@app.route('/login')
def login():
    if helpers.isLoggedIn(): return redirect('/') 
    return render_template("userlogin.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/register')
def register(): 
    if helpers.isLoggedIn(): return redirect('/') 
    return render_template("register.html")

@app.route('/checkout')
def checkout():
    if not helpers.isCustomer(): return render_template("checkout.html", login = True, currentUrl = "/checkout", nav = helpers.getNav())
    return render_template("checkout.html", login = False, currentUrl = "/checkout", nav = helpers.getNav())

@app.route('/aftercheckout')
def aftercheckout():
    if not helpers.isCustomer(): return render_template("aftercheckout.html", login = True, currentUrl = "/aftercheckout", nav = helpers.getNav())
    return render_template("aftercheckout.html", login = False, currentUrl = "/aftercheckout", nav = helpers.getNav())

@app.route('/dashboard/orderhistory')
def orderhistory(): return render_template("orderhistory.html", currentUrl = "/orderhistory", nav = helpers.getNav())
        
@app.route('/orders/<id>')
def order(id): return render_template("order.html")

@app.errorhandler(404)
def not_found(e): return render_template("404.html")

# all api calls /api
app.register_blueprint(apiBlueprint)

if __name__ == '__main__':  app.run(debug = True, use_reloader = True)
