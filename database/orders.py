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
                Status TEXT NOT NULL
            )
        """)

def deleteTable(): # testing
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE OrderTable")

def addOrderToTable(DishIDs, CustomerID, Address, Cost, Datetime, DeliveryMethod, Status):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("""INSERT INTO OrderTable (DishIDs, CustomerID, 
            Address, Cost, Datetime, DeliveryMethod, Status) 
            VALUES (?,?,?,?,?,?,?,?) RETURNING *""",
            (DishIDs, CustomerID, Address, Cost, Datetime,
                DeliveryMethod, Status))
        order = [listToDict(row) for row in rows][0]
        return order

# Place Order and updates User
def placeOrder(DishIDs, CustomerID, Address, Cost, Datetime, DeliveryMethod, Status, newBalance, newOrderCount):
    print(DishIDs)
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("""INSERT INTO OrderTable (DishIDs, CustomerID, 
            Address, Cost, Datetime, DeliveryMethod, Status) 
            VALUES (?,?,?,?,?,?,?) RETURNING OrderID""",
            (DishIDs, CustomerID, Address, Cost,
                Datetime, DeliveryMethod, Status))
        OrderID = [row for row in rows][0][0]
        cursor.execute("""UPDATE CustomerTable SET Balance=?, NumberOfOrders=?
            WHERE CustomerID=?""", (newBalance, newOrderCount, CustomerID))
        return OrderID

def getAllOrders(): # returns all orders
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM OrderTable")
        orders = [listToDict(row) for row in rows]
        return orders

def getOrdersInProgress():
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM OrderTable WHERE Status!='complete'")
        return [listToDict(row) for row in rows]

def getOrderByID(id): # returns specific order
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM OrderTable WHERE OrderID=?", (id,)) 
        order = [listToDict(row) for row in rows][0]
        return order

def getOrdersByCustomerID(id): # returns all orders of one customer
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM OrderTable WHERE CustomerID=?", (id,)) 
        orders = [listToDict(row) for row in rows]
        return orders

def updateOrder(id, DishIDs, CustomerID, Address, Cost, Datetime, EmployeeID, DeliveryMethod, Status):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""UPDATE OrderTable (DishIDs, CustomerID, Address, Cost,
            Datetime, EmployeeID, DeliveryMethod, Status) VALUES (?,?,?,?,?,?,?,?,?)
            WHERE OrderID=?""",(DishIDs, CustomerID, Address, Cost, Datetime, EmployeeID,
            DeliveryMethod, Status, id,))

def deleteOrder(id):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM OrderTable WHERE OrderID=?", (id,))

def listToDict(order):
    return {
        'orderID': order[0],
        'dishIDs': order[1],
        'customerID': order[2],
        'address': order[3],
        'cost': order[4],
        'datetime': order[5],
        'employeeID': order[6],
        'deliveryMethod': order[7],
        'status': order[8],
    }