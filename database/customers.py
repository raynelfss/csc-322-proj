from helpers import getConnection

def createCustomerTable():  # creates a table for all users
    connection, cursor = getConnection()
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS CustomerTable (
        CustomerID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        UserID INTEGER UNIQUE NOT NULL,
        Name TEXT NOT NULL,
        PhoneNumber TEXT UNIQUE NOT NULL,
        VipStatus BOOLEAN NOT NULL DEFAULT FALSE,
        Balance DOUBLE NOT NULL DEFAULT 0,
        NumberOfOrders INTEGER NOT NULL DEFAULT 0,
        MoneySpent DOUBLE NOT NULL DEFAULT 0,
        ShoppingCartID INTEGER UNIQUE NOT NULL,
        Karen BOOLEAN NOT NULL DEFAULT FALSE,
        DemotionPoints INTEGER NOT NULL DEFAULT 0
    )
    """
    )
    connection.commit()
    connection.close()

# use this to create user, customer and shopping cart
def createCustomer(username, passwordHash, name, phoneNumber):
    connection, cursor = getConnection()

    # Add User
    rows = cursor.execute("INSERT INTO AuthenticationTable (Username, PasswordHash, Role) VALUES (?,?,?) RETURNING UserID",
                                            (username, passwordHash, 'customer'), )
    userID = [row for row in rows][0][0]

    # Add Shopping Cart
    rows = cursor.execute("INSERT INTO ShoppingCartTable DEFAULT VALUES RETURNING ShoppingCartID")
    shoppingCartID = [row for row in rows][0][0]

    # Add Customer
    cursor.execute("INSERT INTO CustomerTable (UserID, Name, PhoneNumber, ShoppingCartID) VALUES (?,?,?,?)",
                                                (userID, name, phoneNumber, shoppingCartID),)

    connection.commit()
    connection.close()
    return userID


    

