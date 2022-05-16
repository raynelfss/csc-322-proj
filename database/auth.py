from helpers import DatabaseConnection

def createUserTable():  # creates a table for all users
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS AuthenticationTable (
            UserID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Username TEXT UNIQUE NOT NULL,
            PasswordHash TEXT NOT NULL,
            Role TEXT NOT NULL )
        """)

def getUserByUsername(username): # looks for existing users
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("""SELECT * FROM AuthenticationTable WHERE Username=?""", (username,))
        users = [listToDict(row) for row in rows]
        if users: return users[0] # returns a user's info based on the username
        return ''

def getAllUsers():
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("""SELECT * FROM AuthenticationTable""")
        users = [listToDict(row) for row in rows]
        if users: return users
        return ''

# use createCustomer to register new customers
def addUser(username, password, role): # registers new users
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""INSERT INTO login (Username, Password, Role)
            VALUES (?,?, ?)""", (username, password, role,))

def updatePasswordByID(userID, newPassword):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""UPDATE AuthenticationTable SET PasswordHash=? Where UserID=?""", (newPassword, userID,))

def listToDict(user):
    return {
        'userID': user[0], 'username': user[1],
        'passwordHash': user[2], 'role': user[3], # customer, employee
    }