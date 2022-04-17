from flask import session

def isChef():
    return (session.get('loggedIn') == True
        and session.get('userType') == 'employee' 
        and session.get('employeeType') == 'chef')
    
def isLoggedIn():
    return session.get('loggedIn') == True