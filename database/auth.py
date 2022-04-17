from helpers import getConnection

def createUserTable():  # creates a table for all users
    connection, cursor = getConnection()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS AuthenticationTable (
            UserID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Username TEXT UNIQUE NOT NULL,
            PasswordHash TEXT NOT NULL,
            Role TEXT NOT NULL
        )
        """
    )
    connection.commit()
    connection.close()

def getUserByUsername(username): # looks for existing users
    connection, cursor = getConnection()
    rows = cursor.execute("SELECT * FROM AuthenticationTable WHERE Username=?", (username,)) 
    row = [row for row in rows][0]
    connection.close()
    return row # returns a user's info based on the username

# use createCustomer to register new customers
def addUser(username, password, role): # registers new users
    connection, cursor = getConnection()
    cursor.execute("INSERT INTO login (Username, Password, Role) VALUES (?,?, ?)",
                    (username, password, role), )
    connection.commit()
    connection.close()
    