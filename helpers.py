from dis import dis
import sqlite3 # database
from flask import session
# from api import ratings
# from database import menu, ratings
from collections import Counter

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
    return (session.get('loggedIn') == True 
    and session.get('loggedIn') == True)

def isEmployee():
    return session.get('userType') == 'employee' 
    
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
        dish = getById(dishID)
        totalPrice += dish['price']

    if deliveryStatus: # additional delivery cost
        totalPrice += 2.99 # base delivery fee
    
    totalPrice *= 1.08875 # 8.875% tax rate
    roundedPrice = round(totalPrice, 2) # rounds to nearest hundredth
    return roundedPrice

def getDishes(dishIDString):
    dishIDs = dishIDString.split(',') # [dishID, dishID]
    dishCount = {} # {dishID: quantity}
    
    dishCount = Counter(dishIDs)
    dishes = [{**getById(dishID), 'quantity': dishCount[dishID]} for dishID in dishCount]
    return dishes

# def topThreeDishes(ordersList): # returns the 3 most requested dishIDs
#     # ordersList = orders.getAllOrders() # returns a list of dictionaries
#     frequencies = {}
#     topThree = []
#     for order in ordersList:
#         dishIDsString = ordersList['dishIDs']
#         dishIDs = dishIDsString.split(',') # [dishID, dishID]
#         for dishID in dishIDs:
#             if dishID in frequencies: frequencies[dishID] += 1
#             else: frequencies[dishID] = 1
    
#     for i in range(3):
#         maxKey = max(frequencies, key=frequencies.get)
#         topThree.append(maxKey)
#         frequencies.pop(maxKey)
        
#     return topThree

# def topThreeRated(menuList):
#     allRatings = {}
#     topThree = []

#     for item in menuList:
#         ratingNum = ratings.avgRatingOfDish(menuList['dishID'])
#         allRatings[menuList['dishID']] = ratingNum 
        
#     for i in range(3):
#         maxKey = max(allRatings, key= allRatings.get)
#         topThree.append(maxKey)
#         allRatings.pop(maxKey)

#     return topThree

def getNav():
    if isLoggedIn():
        return [
            {'url': '/', 'name': 'Home'},
            {'url': '/menu', 'name': 'Menu'},
            {'url': '/about', 'name': 'About'},
            {'url': '/logout', 'name': 'Logout'},
            {'url': '/orderhistory', 'name': 'Order History'},
            {'url': '/dashboard', 'name' : 'Dashboard'}
        ]
    else:
        return [
            {'url': '/', 'name': 'Home'},
            {'url': '/menu', 'name': 'Menu'},
            {'url': '/about', 'name': 'About'},
            {'url': '/login', 'name': 'Login'},  
        ]

def getSidebarNav():
    if isChef():
        return [
            {'url': '/', 'name': 'Home'},
            {'url': '/dashboard', 'name': 'Dashboard'},
            {'url': '/dashboard/menu', 'name':'Menu'},
            {'url': '/dashboard/orders', 'name':'Orders'},
            {'url': '/logout', 'name':'Logout'}, 
        ]
    elif isCustomer():
        return [
            {'url': '/', 'name': 'Home'},
            {'url': '/dashboard', 'name': 'Dashboard'},
            {'url': '/dashboard/wallet', 'name' : 'Wallet'},
            {'url': '/dashboard/settings', 'name' : 'Settings'},
        ]

    else: return []