from dis import dis
import sqlite3 # database
from flask import session
from database import menu

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
    
def isChef():
    return (session.get('loggedIn') == True
        and session.get('userType') == 'employee' 
        and session.get('employeeType') == 'chef')
    
def isLoggedIn():
    return session.get('loggedIn') == True

def calcPrices(dishIDs, deliveryStatus):
    totalPrice = 0
    for dishID in dishIDs:
        dish = menu.getById(dishID)
        totalPrice += dish[3]

    if deliveryStatus: # additional delivery cost
        totalPrice += 7.99 # base delivery fee
    
    totalPrice *= 1.08875 # 8.875% tax rate
    roundedPrice = round(totalPrice, 2) # rounds to nearest hundredth
    return roundedPrice