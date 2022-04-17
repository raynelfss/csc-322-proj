import sqlite3 # database
from flask import session

# helper functions and classes
class DatabaseConnection:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.connection = sqlite3.connect(self.file_name)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.commit()
        self.connection.close()
    
def getConnection(): # bouta be obsolete real fast
    connection = sqlite3.connect('./database/database.db')
    cursor = connection.cursor()
    return connection, cursor

def isChef():
    return (session.get('loggedIn') == True
        and session.get('userType') == 'employee' 
        and session.get('employeeType') == 'chef')
    
def isLoggedIn():
    return session.get('loggedIn') == True