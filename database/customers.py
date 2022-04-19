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
            DemotionPoints INTEGER NOT NULL DEFAULT 0
        )
        """)

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

def getCustomerByCustomerID(customerID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM CustomerTable WHERE CustomerID=?", (customerID, ))
        return [row for row in rows][0]
        # return [getCustomerDictionary(row) for row in rows][0]

def getCustomerByUserID(userID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM CustomerTable WHERE UserID=?", (userID, ))
        return [row for row in rows][0]
def updateCustomer(customerID, name, phoneNumber, vipStatus, balance, numberOfOrders, moneySpent, shoppingCartID, karen, demotionPoints):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""UPDATE CustomerTable SET Name=?, PhoneNumber=?, VipStatus=?, Balance=?, NumberOfOrders=?, 
        MoneySpent=?, ShoppingCartID=?, Karen=?, DemotionPoints=? WHERE CustomerID=?""", (name, phoneNumber, vipStatus, balance,
        numberOfOrders, moneySpent, shoppingCartID, karen, demotionPoints, customerID))

# def getCustomerDictionary(row):
#     return {
#         customerID: row[0],
#         userID: row[1],
#         name: row[2],
#         phoneNumber: row[3],
#         vipStatus: row[4],
#         balance: row[5],
#         numberOfOrders: row[6],
#         moneySpent: row[7],
#         shoppingCartID: row[8],
#         karen: row[9],
#         demotionPoints: row[10]
#     }
    

