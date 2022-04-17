# Operations that make changes to menu in database
from helpers import getConnection

def createTable():  # creates food table
    connection, cursor = getConnection()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS FoodTable (
            DishID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            DishName TEXT NOT NULL,
            Description TEXT,
            Price DOUBLE NOT NULL,
            ImageURL TEXT,
            ChefID INTEGER UNIQUE NOT NULL
        )
        """
    )
    connection.commit()
    connection.close()

def deleteTable(): # only used for testing purposes
    connection, cursor = getConnection()
    cursor.execute("DROP TABLE FoodTable")
    connection.commit()
    connection.close()

def add(dishName, description, price, imageURL, chefID): # adds items to table
    connection, cursor = getConnection()
    cursor.execute("INSERT INTO FoodTable (DishName, Description, Price, ImageURL, chefID) VALUES (?,?,?,?,?)",
                   (dishName, description, price, imageURL, chefID, ))
    connection.commit()
    connection.close()

def deleteById(id): # deletes a specific item
    connection, cursor = getConnection()
    cursor.execute("DELETE FROM FoodTable WHERE DishID=?", (id,))
    connection.commit()
    connection.close()

def deleteAll(): # deletes all items
    connection, cursor = getConnection()
    cursor.execute("DELETE FROM FoodTable")
    connection.commit()
    connection.close()

def getById(id): # returns a specific item
    connection, cursor = getConnection()
    rows = cursor.execute("SELECT * FROM FoodTable WHERE DishID=?", (id,)) 
    row = [row for row in rows][0]
    connection.close()
    return row

def getAll():  # returns all items from Menu
    connection, cursor = getConnection()
    rows = cursor.execute("SELECT * FROM FoodTable")
    rowsOutput = [row for row in rows]
    connection.close()
    return rowsOutput

def updateByID(id, name, img_url, description, price): # updates specific items
    connection, cursor = getConnection()
    print(id, name, img_url, description, price)
    cursor.execute("UPDATE Menu SET name=?, img_url=?, description=?, price=? WHERE DishID=?",
                    (name, img_url, description, price, id, )) 
    connection.commit()
    connection.close()