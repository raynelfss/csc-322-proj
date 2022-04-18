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
        rows = cursor.execute("""INSERT INTO OrderTable (DishIDs, CustomerID, Address, Cost, Datetime,
                DeliveryMethod, Status) VALUES (?,?,?,?,?,?,?,?) RETURNING *""",
                (DishIDs, CustomerID, Address, Cost, Datetime, DeliveryMethod, Status))
        row = [row for row in rows][0]
        return row

def viewAllOrders(): # returns all orders
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM OrderTable")
        rowsOutput = [row for row in rows]
        return rowsOutput

def getOrderByID(id): # returns specific order
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM OrderTable WHERE OrderID=?", (id,)) 
        row = [row for row in rows][0]
        return row

def getOrdersByCustomerID(id): # returns all orders of one customer
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM OrderTable WHERE CustomerID=?", (id,)) 
        rows = [row for row in rows]
        return rows

def updateOrder(id, DishIDs, CustomerID, Address, Cost, Datetime, EmployeeID, DeliveryMethod, Status):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""UPDATE OrderTable (DishIDs, CustomerID, Address, Cost, Datetime,
        EmployeeID, DeliveryMethod, Status) VALUES (?,?,?,?,?,?,?,?,?) WHERE OrderID=?""",
        (DishIDs, CustomerID, Address, Cost, Datetime, EmployeeID, DeliveryMethod, Status, id,))

def deleteOrder(id):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM OrderTable WHERE OrderID=?", (id,))
