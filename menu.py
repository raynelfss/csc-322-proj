# Operations that make changes to menu in database
import sqlite3

def getConnection(): # helper function that saves lines
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()
    return connection, cursor

def createTable():  # creates the table
    connection, cursor = getConnection()
    command1 = """CREATE TABLE IF NOT EXISTS Menu( id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, img_url TEXT, description TEXT, price REAL NOT NULL
    )"""
    cursor.execute(command1)
    connection.commit()
    connection.close()

def deleteTable(): # only used for testing purposes
    connection, cursor = getConnection()
    command1 = "DROP TABLE Menu"
    cursor.execute(command1)
    connection.commit()
    connection.close()

def add(name, img_url, description, price): # adds items to table
    connection, cursor = getConnection()
    cursor.execute("INSERT INTO Menu (name, img_url, description, price) VALUES (?,?,?,?)",
                   (name, img_url, description, price))
    connection.commit()
    connection.close()

def deleteById(id): # deletes items in the table by id
    connection, cursor = getConnection()
    cursor.execute("DELETE FROM Menu WHERE id=?", (id,))
    connection.commit()
    connection.close()

def deleteAll():
    connection, cursor = getConnection()
    cursor.execute("DELETE FROM Menu")
    connection.commit()
    connection.close()

def getById(id):
    connection, cursor = getConnection()
    rows = cursor.execute("SELECT * FROM Menu WHERE id=?", (id,)) 
    row = [row for row in rows][0]
    connection.close()
    return row

def getAll():  # returns all items from Menu
    connection, cursor = getConnection()
    rows = cursor.execute("SELECT * FROM Menu")
    rowsOutput = [row for row in rows]
    connection.close()
    return rowsOutput

def updateByID(id, name, img_url, description, price):
    connection, cursor = getConnection()
    print(id, name, img_url, description, price)
    cursor.execute("UPDATE Menu SET name=?, img_url=?, description=?, price=? WHERE id=?",
                    (name, img_url, description, price, id), ) 
    connection.commit()
    connection.close()