from flask import Blueprint, abort, request, session
from database import discussions, threads
from helpers import isCustomer, isManager

complaintBlueprint = Blueprint('app_discussions', __name__, url_prefix = '/discussions')
@complaintBlueprint.route('/', methods = ['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        try: return { 'response': discussions.getDiscussions() }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error
    
    elif request.method == 'POST':
        if not isCustomer(): abort(403) 
        try:
            data = request.json
            discussions.addDiscussion( data['Subject'], data['CreatorID'] )
            return { 'response': 'successfully posted discussion' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error
    
    elif request.method == 'DELETE':
        if not isManager(): abort(403)
        try:
            discussions.deleteTable()
            threads.deleteTable()
            return { 'response': 'discussions table has been deleted' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error

@complaintBlueprint.route('/<id>', methods = ['GET', 'DELETE'])
def discussion(id):
    if request.method =='GET':
        try:
            discussion = discussions.getDiscussionByID(id)
            return { 'response': discussion }
        except Exception as e:
            print('error: ', e , '\n')
            abort(500)

    elif request.method == 'DELETE':
        if not isManager(): abort (403)
        try:
            discussions.deleteDiscussionByID(id)
            threads.deleteCommentsByDiscussion(id)
            return { 'response': 'Successfully deleted discussion' }
        except Exception as e:
            print('error: ', e , '\n')
            abort(500)
        