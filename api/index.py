# Any api requests should be handled here
from flask import Blueprint
from api.menu import menuBlueprint 

apiBlueprint = Blueprint('app_api', __name__, url_prefix='/api')

#requests to /api
@apiBlueprint.route('/')
def index():
    return 'All api calls should be made to this prefix'
    
apiBlueprint.register_blueprint(menuBlueprint)
