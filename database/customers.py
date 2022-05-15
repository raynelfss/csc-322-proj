from helpers import DatabaseConnection

def createCustomerTable():  # creates a table for all users
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS CustomerTable (
            CustomerID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            UserID INTEGER UNIQUE NOT NULL,
            Name TEXT NOT NULL,
            PhoneNumber TEXT UNIQUE NOT NULL,
            VipStatus BOOLEAN NOT NULL DEFAULT FALSE,
            Balance DOUBLE NOT NULL DEFAULT 0,
            NumberOfOrders INTEGER NOT NULL DEFAULT 0,
            MoneySpent DOUBLE NOT NULL DEFAULT 0,
            ShoppingCartID INTEGER UNIQUE NOT NULL,
            Karen BOOLEAN NOT NULL DEFAULT FALSE,
            DemotionPoints INTEGER NOT NULL DEFAULT 0 )
        """)

def deleteCustomerTable(): 
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE IF EXISTS CustomerTable")

# use this to create user, customer and shopping cart
def createCustomer(username, passwordHash, name, phoneNumber):
    with DatabaseConnection('./database/database.db') as cursor:
        # Add User
        rows = cursor.execute("""INSERT INTO AuthenticationTable 
            (Username, PasswordHash, Role) VALUES (?,?,?) RETURNING UserID""",
            (username, passwordHash, 'customer',))
        userID = [row for row in rows][0][0]

        # Add Shopping Cart
        rows = cursor.execute("""INSERT INTO ShoppingCartTable 
            DEFAULT VALUES RETURNING ShoppingCartID""")
        shoppingCartID = [row for row in rows][0][0]

        # Add Customer
        rows = cursor.execute("""INSERT INTO CustomerTable 
            (UserID, Name, PhoneNumber, ShoppingCartID) VALUES (?,?,?,?) RETURNING CustomerID""",
            (userID, name, phoneNumber, shoppingCartID,))
        customerID = [row for row in rows][0][0]
        return userID, customerID

def getAllCustomers():
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM CustomerTable")
        customers = [listToDict(row) for row in rows]
        return customers

def deleteCustomer(customerID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM CustomerTable WHERE CustomerID=?", (customerID,))

def getCustomerByCustomerID(customerID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM CustomerTable WHERE CustomerID = ?", (customerID,))
        return [listToDict(row) for row in rows][0]


def getCustomerByUserID(userID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM CustomerTable WHERE UserID = ?", (userID,))
        return [listToDict(row) for row in rows][0]

def getCustomerDemotionPoint(userID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT DemotionPoints FROM CustomerTable WHERE CustomerID = ?", (userID,))

        return [listToDictPoints(row) for row in rows][0]


def updateCustomer(customerID, name, phoneNumber, vipStatus, balance, numberOfOrders, moneySpent, shoppingCartID, karen, demotionPoints):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""UPDATE CustomerTable SET Name=?, PhoneNumber=?, VipStatus=?, Balance=?, NumberOfOrders=?, MoneySpent=?,
            ShoppingCartID=?, Karen=?, DemotionPoints=? WHERE CustomerID=?""", (name, phoneNumber,
            vipStatus, balance, numberOfOrders, moneySpent, shoppingCartID, karen, demotionPoints, customerID,))

def updateCustDemotionPoint(userID,demotionPoints):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""UPDATE CustomerTable SET DemotionPoints = ? WHERE CustomerID=?)""",(demotionPoints, userID,))

def getBalance(customerID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT Balance FROM CustomerTable WHERE CustomerID = ?", (customerID,))
        return [listToDictBal(row) for row in rows][0]

def updateBalance(customerID, balance):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("UPDATE CustomerTable SET Balance=? WHERE CustomerID=?", (balance, customerID,))

def getMoneySpent(customerID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT MoneySpent FROM CustomerTable WHERE CustomerID = ?", (customerID,))
        return [listToDictBal(row) for row in rows][0]

def updateMoneySpent(customerID, spent):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("UPDATE CustomerTable SET MoneySpent=? WHERE CustomerID=?", (spent, customerID,))

def getNumOfOrders(customerID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT NumberOfOrders FROM CustomerTable WHERE CustomerID = ?", (customerID,))
        return [listToDictBal(row) for row in rows][0]

def updateNumOrders(customerID, orders):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("UPDATE CustomerTable SET NumberOfOrders=? WHERE CustomerID=?", (orders, customerID,))

def demoteOnePoint(userID): 
    points = getCustomerDemotionPoint(userID)   #if error maybe because this doesnt return int value
    points -=1
    updateCustDemotionPoint(userID,points)


def promoteOnePoint(userID):
    points = getCustomerDemotionPoint(userID)
    points +=1
    updateCustDemotionPoint(userID,points)

def listToDictBal(customer):
    return {
        'balance': customer[0]
    }
def listToDictPoints(customer):
    return {
        'demotionPoints': customer[0]
    }

def listToDict(customer):
    return {
        'customerID': customer[0], 'userID': customer[1],
        'name': customer[2], 'phoneNumber': customer[3],
        'vipStatus': customer[4], 'balance': customer[5],
        'numberOfOrders': customer[6], 'moneySpent': customer[7],
        'shoppingCartID': customer[8], 'karen': customer[9],
        'demotionPoints': customer[10]
    }
    

