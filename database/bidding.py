from helpers import DatabaseConnection

def createTable():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS BiddingSystemTable (
            BidID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            EmployeeID INTEGER NOT NULL,
            Amount DOUBLE NOT NULL,
            OrderID INTEGER NOT NULL )
        """)

def deleteTable(): # testing
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE IF EXISTS BiddingSystemTable")

def addBid(employeeID, amount, orderID): # creates bid
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("""INSERT INTO BiddingSystemTable (EmployeeID, 
            Amount, OrderID) VALUES (?,?,?) RETURNING *""",
            (employeeID, amount, orderID,))
        bid = [listToDict(row) for row in rows][0]
        return bid

def deleteBid(bidID): # deletes a specific bid
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM BiddingSystemTable WHERE BidID=?", (bidID,))

def deleteBidByOrderID(orderID): 
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM BiddingSystemTable WHERE OrderID=?", (orderID,))

def getAllBids(): # returns all existing bids
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM BiddingSystemTable")
        bids = [listToDict(row) for row in rows]
        return bids

def getBidsByOrderID(orderID): # returns all bids on a specific orderID
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM BiddingSystemTable WHERE OrderID=?",(orderID,)) 
        bids = [listToDict(row) for row in rows]
        return bids

def getBidsByID(bidID): # returns a specific bid
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM BiddingSystemTable WHERE BidID=?",(bidID,)) 
        bid = [listToDict(row) for row in rows][0]
        return bid

def listToDict(bid):
    return {
        'bidID': bid[0], 'employeeID': bid[1], 'amount': bid[2], 'orderID': bid[3],
    }