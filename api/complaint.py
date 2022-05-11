from flask import Blueprint, abort, request, session
from database import complaints
from helpers import isManager

complaintBlueprint = Blueprint('app_complaints', __name__, url_prefix = '/complaints')

@complaintBlueprint.route('/', methods = ['GET', 'POST','DELETE'])
def index():
    if request.method == 'GET':
        try: return { 'response': complaints.getComplaints() }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error
    
    elif request.method == 'POST': 
        try:
            data = request.json
            complaints.updateComplaint( data['ComplaintID'], data['Message'] )
            return { 'response': 'successfully updated complaint' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error
    
    elif request.method == 'DELETE':
        if not isManager(): abort(403)
        try:
            complaints.deleteTable()
            return { 'response': 'complaints table has been deleted' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error

@complaintBlueprint.route('/<id>', methods = ['GET','DELETE'])
def complaint(id):
    if request.method == 'GET':
        try:
            complaint = complaints.getComplaintByID(id)
            return { 'response': complaint }
        
        except Exception as e:
            print('error: ', e , '\n')
            abort(500)
   
    elif request.method == 'DELETE':
        if not isManager(): abort(403)
        try:
            complaints.deleteComplaint(id)
            return {'response': 'Successfully deleted complaint' }
        except Exception as e:
            print('error: ', e , '\n')
            abort(500)
