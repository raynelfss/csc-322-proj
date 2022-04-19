from helpers import DatabaseConnection

def createTable():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS BiddingSystemTable (
            BidID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            EmployeeID INTEGER NOT NULL,
            Amount DOUBLE NOT NULL,
            OrderID INTEGER NOT NULL
        )
        """)

def deleteTable(): # testing
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE IF EXISTS BiddingSystemTable")

def addBid(bidID, employeeID, amount, orderID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("""INSERT INTO BiddingSystemTable (bidID, employeeID, 
            amount, orderID) VALUES (?,?,?,?) RETURNING *""",
            (bidID, employeeID, amount, orderID))
        row = [row for row in rows][0]
        return row

def deleteBid(bidID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM BiddingSystemTable WHERE bidID=?", (bidID,))

def viewAllBids(): 
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM BiddingSystemTable")
        rowsOutput = [row for row in rows]
        return rowsOutput

def getBidByID(bidID): 
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM BiddingSystemTable WHERE bidID=?",(bidID,)) 
        row = [row for row in rows][0]
        return row