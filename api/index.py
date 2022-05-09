# Any api requests should be handled here
from flask import Blueprint
from api.menu import menuBlueprint 
from api.auth import authBlueprint
from api.order import orderBlueprint
from api.bidding import bidsBlueprint
from api.customer import customerBlueprint
from api.wallet import walletBlueprint
from api.ratings import ratingBlueprint
from api.shoppingCart import cartBlueprint

apiBlueprint = Blueprint('app_api', __name__, url_prefix = '/api')

#requests to /api
@apiBlueprint.route('/')
def index(): return 'All api calls should be made to this prefix'
    
apiBlueprint.register_blueprint(authBlueprint)
apiBlueprint.register_blueprint(bidsBlueprint)
apiBlueprint.register_blueprint(customerBlueprint)
apiBlueprint.register_blueprint(menuBlueprint)
apiBlueprint.register_blueprint(orderBlueprint)
apiBlueprint.register_blueprint(ratingBlueprint)
apiBlueprint.register_blueprint(cartBlueprint)
apiBlueprint.register_blueprint(walletBlueprint)