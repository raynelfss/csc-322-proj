from helpers import DatabaseConnection

def createTable(): # testing
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS OrderTable (
            OrderID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            DishIDs TEXT NOT NULL,
            CustomerID INTEGER NOT NULL,
            Address TEXT NOT NULL,
            Cost DOUBLE NOT NULL,
            Datetime DATETIME NOT NULL,
            EmployeeID INTEGER,
            DeliveryMethod TEXT NOT NULL,
            Status TEXT NOT NULL )
        """)

def deleteTable(): # testing
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE OrderTable")

def addOrderToTable(dishIDs, customerID, address, cost, datetime, deliveryMethod, status):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("""INSERT INTO OrderTable (DishIDs, CustomerID, 
            Address, Cost, Datetime, DeliveryMethod, Status) VALUES (?,?,?,?,?,?,?,?) RETURNING *""",
            (dishIDs, customerID, address, cost, datetime, deliveryMethod, status,))
        order = [listToDict(row) for row in rows][0]
        return order

# Place Order and updates User
def placeOrder(dishIDs, customerID, address, cost, datetime, deliveryMethod, status, newBalance, newOrderCount):
    print(dishIDs)
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("""INSERT INTO OrderTable (DishIDs, CustomerID, 
            Address, Cost, Datetime, DeliveryMethod, Status) 
            VALUES (?,?,?,?,?,?,?) RETURNING OrderID""", 
            (dishIDs, customerID, address, cost, datetime, deliveryMethod, status,))
        
        OrderID = [row for row in rows][0][0]
        cursor.execute("UPDATE CustomerTable SET Balance=?, NumberOfOrders=? WHERE CustomerID=?",
            (newBalance, newOrderCount, customerID,))
        return OrderID

def getAllOrders(): # returns all orders
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM OrderTable")
        orders = [listToDict(row) for row in rows]
        return orders

def getOrdersInProgress():
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM OrderTable WHERE (Status != 'complete' AND Status != 'cancelled')")
        return [listToDict(row) for row in rows]

def getOrderByID(id): # returns specific order
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM OrderTable WHERE OrderID=?", (id,)) 
        order = [listToDict(row) for row in rows][0]
        return order

def getOrdersBycustomerID(id): # returns all orders of one customer
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM OrderTable WHERE CustomerID=?", (id,)) 
        orders = [listToDict(row) for row in rows]
        return orders

def updateOrder(id, dishIDs, customerID, address, cost, datetime, deliveryMethod, status):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""UPDATE OrderTable SET DishIDs=?, CustomerID=?, Address=?, Cost=?,
            Datetime=?, DeliveryMethod=?, Status=? WHERE OrderID=?""",
            (dishIDs, customerID, address, cost, datetime, deliveryMethod, status, id,))

def deleteOrder(id):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM OrderTable WHERE OrderID=?", (id,))

def listToDict(order):
    return {
        'orderID': order[0], 'dishIDs': order[1],
        'customerID': order[2], 'address': order[3],
        'cost': order[4], 'datetime': order[5],
        'employeeID': order[6], 'deliveryMethod': order[7],
        'status': order[8],
    }