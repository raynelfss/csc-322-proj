from database.customers import listToDict
from helpers import DatabaseConnection


def createTable(): # testing
    with DatabaseConnection('./database/database.db') as cursor:   ##**I'm assuming 'amount' is number of items in order
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ChefOrder (
            ItemID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            ChefID INTEGER NOT NULL,
            OrderID INTEGER NOT NULL,
            Amount INTEGER NOT NULL,                    
            Status TEXT NOT NULL)
        """)
def deleteTable():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE ChefOrder")
        

def addOrdertoChef(chefID, orderID, amount, status):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("""INSERT INTO OrderTable (ChefID, OrderID, Amount, Status) VALUES (?,?,?,?) RETURNING *""",
            (chefID, orderID, amount, status,))
        cheforder = [listToDict(row) for row in rows][0]
        return cheforder

def deleteChefOrder(itemID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM ChefOrder WHERE ItemID=?", (itemID,))

def getAllChefOrders():
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM ChefOrder")
        cheforders = [listToDict(row) for row in rows]
        return cheforders

def getChefOrderByID(itemID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM ChefOrder WHERE ItemID= ?", (itemID,))
        cheforder = [listToDict(row) for row in rows]
        return cheforder

def updateChefOrder(itemID,chefID, orderID, amount, status):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""UPDATE ChefOrder SET ChefID =?, OrderID = ?, Amount = ?, Status = ?
                            WHERE ItemID = ?""", (chefID, orderID, amount,status, itemID,))
def listToDict(chefOrder):
    return {
        'itemID': chefOrder[0], 
        'chefID': chefOrder[1],
        'orderID': chefOrder[2],
        'amount': chefOrder[3],
        'status': chefOrder[4]
    }