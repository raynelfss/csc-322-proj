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
        bid = [listToDict(row) for row in rows][0]
        return bid

def deleteBid(bidID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM BiddingSystemTable WHERE bidID=?", (bidID,))

def getAllBids(): 
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM BiddingSystemTable")
        bids = [listToDict(row) for row in rows]
        return bids

def getBidByID(bidID): 
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM BiddingSystemTable WHERE bidID=?",(bidID,)) 
        bid = [listToDict(row) for row in rows][0]
        return bid

def listToDict(bid):
    return {
        'bidID': bid[0],
        'employeeID': bid[1],
        'amount': bid[2],
        'orderID': bid[3],
    }