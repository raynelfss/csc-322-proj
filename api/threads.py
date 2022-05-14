from flask import Blueprint, abort, request, session
from database import threads
from helpers import isCustomer, isManager

complaintBlueprint = Blueprint('app_threads', __name__, url_prefix = '/threads')

@complaintBlueprint.route('/', methods = ['GET', 'POST','DELETE'])
def index():
    if request.method == 'GET':
        try: return { 'response': threads.getAllComments() }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error
    
    elif request.method == 'POST':
        if not isCustomer(): abort(403) 
        try:
            data = request.json
            threads.addComment( data['CommentorID'], data['DiscussionID'], data['Comment'], data['Flag'] )
            return { 'response': 'successfully posted discussion' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error
    
    elif request.method == 'DELETE':
        if not isManager(): abort(403)
        try:
            threads.deleteTable()
            return { 'response': 'discussions table has been deleted' }
        except Exception as e:
            print('error: ', e, '\n')
            abort(500) # returns internal server error

## SPECIFIC COMMENTS SPECIFIED BY COMMENT ID which is (id)
@complaintBlueprint.route('/<id>', methods = ['GET','DELETE'])
def comment(id):
    if request.method =='GET':
        try:
            comment = threads.getCommentByID(id)
            return { 'response': comment }
        except Exception as e:
            print('error: ', e , '\n')
            abort(500)

    elif request.method == 'DELETE':
        if not isManager(): abort (403)
        try:
            threads.deleteCommentsByID(id)
            return {'response': 'Successfully deleted discussion' }
        except Exception as e:
            print('error: ', e , '\n')
            abort(500)

## GROUP OF COMMENTS SPECIFIED BY DISCUSSION ID which is (id)
@complaintBlueprint.route('/disc/<id>', methods = ['GET','DELETE'])
def comment(id):
    if request.method =='GET':
        try:
            comments = threads.getCommentsByDiscussion(id)
            return { 'response': comments }
        except Exception as e:
            print('error: ', e , '\n')
            abort(500)

    elif request.method == 'DELETE':
        if not isManager(): abort (403)
        try:
            threads.deleteCommentsByDiscussion(id)
            return { 'response': 'Successfully deleted discussion' }
        except Exception as e:
            print('error: ', e , '\n')
            abort(500)