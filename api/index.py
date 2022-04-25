# Any api requests should be handled here
from flask import Blueprint
from api.menu import menuBlueprint 
from api.auth import authBlueprint
from api.order import orderBlueprint
from api.bidding import bidsBlueprint

apiBlueprint = Blueprint('app_api', __name__, url_prefix='/api')

#requests to /api
@apiBlueprint.route('/')
def index():
    return 'All api calls should be made to this prefix'
    
apiBlueprint.register_blueprint(menuBlueprint)
apiBlueprint.register_blueprint(authBlueprint)
apiBlueprint.register_blueprint(orderBlueprint)
apiBlueprint.register_blueprint(bidsBlueprint)