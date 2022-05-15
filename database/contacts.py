from helpers import DatabaseConnection

def createTable():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ContatcsTable (
            ContactID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Name TEXT NOT NULL,
            Email TEXT NOT NULL,
            Message TEXT NOT NULL,
            Contacted BOOLEAN NOT NULL)                                       
        """)

def deleteTable(): 
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE IF EXISTS ContatcsTable")

def addContact(name, email, message, contacted):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("""INSERT INTO ContatcsTable (Name,
            Email, Message, Contacted) VALUES (?,?,?,?) RETURNING *""",
            (name, email, message, contacted,))

        contacts = [listToDict(row) for row in rows][0]
        return contacts

def getContacts():
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM ContatcsTable")
        contacts = [listToDict(row) for row in rows]
        return contacts

def getContact(contactID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("SELECT * FROM ContatcsTable WHERE ContactID=?", (contactID,)) 

def deleteContact(contactID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM ContatcsTable WHERE ContactID=?", (contactID,))

def listToDict(contacts):
    return {
        'contactID': contacts[0], 'name': contacts[1],
        'email': contacts[2], 'message': contacts[3],
        'contacted': contacts[4]       
    }
