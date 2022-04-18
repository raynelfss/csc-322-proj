from helpers import DatabaseConnection

def createUserTable():  # creates a table for all users
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS AuthenticationTable (
            UserID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Username TEXT UNIQUE NOT NULL,
            PasswordHash TEXT NOT NULL,
            Role TEXT NOT NULL
        )
        """)

def getUserByUsername(username): # looks for existing users
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM AuthenticationTable WHERE Username=?", (username,)) 
        row = [row for row in rows][0]
        return row # returns a user's info based on the username

# use createCustomer to register new customers
def addUser(username, password, role): # registers new users
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("INSERT INTO login (Username, Password, Role) VALUES (?,?, ?)",
            (username, password, role,))
    