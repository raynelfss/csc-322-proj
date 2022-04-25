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
    
def isLoggedIn():
    return session.get('loggedIn') == True
    
def isChef():
    return (session.get('loggedIn') == True
        and session.get('userType') == 'employee' 
        and session.get('employeeType') == 'chef')

def isDeliveryBoy():
    return (session.get('loggedIn') == True
        and session.get('userType') == 'employee' 
        and session.get('employeeType') == 'deliveryPerson') #placeholder name
    
def isCustomer():
    return (session.get('loggedIn') == True
        and session.get('userType') == 'customer')

def isManager():
    return (session.get('loggedIn') == True
        and session.get('userType') == 'employee' 
        and session.get('employeeType') == 'manager')

def calcPrices(dishIDs, deliveryStatus):
    totalPrice = 0
    for dishID in dishIDs:
        dish = menu.getById(dishID)
        totalPrice += dish['price']

    if deliveryStatus: # additional delivery cost
        totalPrice += 2.99 # base delivery fee
    
    totalPrice *= 1.08875 # 8.875% tax rate
    roundedPrice = round(totalPrice, 2) # rounds to nearest hundredth
    return roundedPrice

# listToDict ??

def getDishes(dishIDString):
    dishIDs = dishIDString.split(',') # [dishID, dishID]
    dishCount = {} # {dishID: quantity}
    for dishID in dishIDs:
        if dishID in dishCount:
            dishCount[dishID] += 1
        else:
            dishCount[dishID] = 1
    dishes = []
    for dishID in dishCount: # itterate through keys in dishCount
        dish = menu.getById(dishID) # get dish from db
        dish['quantity'] = dishCount[dishID] # add quantity to dish
        dishes.append(dish) # add dish to dishes
    return dishes

def getNav():
    if isLoggedIn():
        return [
            {'url': '/', 'name': 'Home'},
            {'url': '/menu', 'name':'Menu'},
            {'url': '/about', 'name':'About'},
            {'url': '/logout', 'name':'Logout'},
        ]
    else:
        return [
            {'url': '/', 'name': 'Home'},
            {'url': '/menu', 'name':'Menu'},
            {'url': '/about', 'name':'About'},
            {'url': '/login', 'name':'Login'},  
        ]

def getSidebarNav():
    if isChef():
        return [
            {'url': '/dashboard', 'name': 'Home'},
            {'url': '/dashboard/menu', 'name':'Menu'},
            {'url': '/dashboard/orders', 'name':'Orders'},
            {'url': '/logout', 'name':'Logout'}, 
        ]
    else:
        return [
            
        ]