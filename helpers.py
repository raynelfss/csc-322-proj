import sqlite3
from flask import session

# helper functions
def getConnection():
    connection = sqlite3.connect('./database/database.db')
    cursor = connection.cursor()
    return connection, cursor

def isChef():
    return (session.get('loggedIn') == True
        and session.get('userType') == 'employee' 
        and session.get('employeeType') == 'chef')
    
def isLoggedIn():
    return session.get('loggedIn') == True