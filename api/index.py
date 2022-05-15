# Any api requests should be handled here
from flask import Blueprint
from api.auth import authBlueprint
from api.bidding import bidsBlueprint
from api.complaint import complaintBlueprint
from api.contact import contactBlueprint
from api.customer import customerBlueprint
from api.employee import employeeBlueprint
from api.menu import menuBlueprint 
from api.order import orderBlueprint
from api.ratings import ratingBlueprint
from api.salary import salaryBlueprint
from api.shoppingCart import cartBlueprint
from api.wallet import walletBlueprint

apiBlueprint = Blueprint('app_api', __name__, url_prefix = '/api')

#requests to /api
@apiBlueprint.route('/')
def index(): return 'All api calls should be made to this prefix'
    
apiBlueprint.register_blueprint(authBlueprint)
apiBlueprint.register_blueprint(bidsBlueprint)
apiBlueprint.register_blueprint(complaintBlueprint)
apiBlueprint.register_blueprint(contactBlueprint)
apiBlueprint.register_blueprint(customerBlueprint)
apiBlueprint.register_blueprint(employeeBlueprint)
apiBlueprint.register_blueprint(menuBlueprint)
apiBlueprint.register_blueprint(orderBlueprint)
apiBlueprint.register_blueprint(ratingBlueprint)
apiBlueprint.register_blueprint(salaryBlueprint)
apiBlueprint.register_blueprint(cartBlueprint)
apiBlueprint.register_blueprint(walletBlueprint)