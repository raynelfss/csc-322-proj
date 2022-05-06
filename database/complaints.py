from database.bidding import listToDict
from helpers import DatabaseConnection

#Not completely sure what the datatype for processed should be, left is as text for now

def createTable():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ComplaintSystemTable (
            ComplaintID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            ComplainerID INTEGER NOT NULL,
            ComplaineeID INTEGER NOT NULL,
            Message TEXT NOT NULL,
            Processed TEXT NOT NULL)                                       
        """)


def deleteTable(): 
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE IF EXISTS ComplaintSystemTable")

def addComplaint(complainerID, complaineeID, message, processed):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("""INSERT INTO ComplaintSystemTable (ComplainerID, ConplaineeID,
        Message, Processed) VALUES (?,?,?,?) RETURNING *""",
            (complainerID, complaineeID, message, processed,))

        complaint = [listToDict(row) for row in rows][0]
        return complaint

def deleteBid(complaintID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM ComplaintSystemTable WHERE ComplaintID=?", (complaintID,))

def deleteBidsByComplainer(complainerID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM ComplaintSystemTable WHERE ComplainerID=?", (complainerID,))

def deleteBidsByComplainee(complaineeID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM ComplaintSystemTable WHERE ComplaineeID=?", (complaineeID,))

def updateComplaintMessage(complaintID, message):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""UPDATE CustomerTable SET (message) VALUES(?) WHERE ComplaintID=?""", (message, complaintID))

def listToDict(complaint):
    return {
        'ComplaintID': complaint[0], 'ComplainerID': complaint[1],
        'ComplaineeID': complaint[2], 'Message': complaint[3],
        'Processed': complaint[4]       
    }
