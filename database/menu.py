# Operations that make changes to menu in database
from helpers import DatabaseConnection

def createTable():  # creates food table
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS FoodTable (
            DishID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            DishName TEXT NOT NULL,
            Description TEXT,
            Price DOUBLE NOT NULL,
            ImageURL TEXT,
            ChefID INTEGER NOT NULL
        )
        """)

def deleteTable(): # only used for testing purposes
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE FoodTable")

def add(dishName, description, price, imageURL, chefID): 
    # adds items to table
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""INSERT INTO FoodTable 
            (DishName, Description, Price, ImageURL, chefID) 
            VALUES (?,?,?,?,?)""",
            (dishName, description, price, imageURL, chefID,))

def deleteById(id): # deletes a specific item
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM FoodTable WHERE DishID=?", (id,))

def deleteAll(): # deletes all items
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM FoodTable")

def getById(id): # returns a specific item
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM FoodTable WHERE DishID=?", (id,)) 
        row = [row for row in rows][0]
        return row

def getAll():  # returns all items from Menu
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM FoodTable")
        rowsOutput = [row for row in rows]
        return rowsOutput

def updateByID(id, name, img_url, description, price): # updates specific items
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""UPDATE FoodTable SET name=?, img_url=?,
            description=?, price=? WHERE DishID=?""",
            (name, img_url, description, price, id,)) 