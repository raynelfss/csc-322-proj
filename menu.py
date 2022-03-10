# Operations that make changes to menu in database
import sqlite3


def createTable():  # creates the table
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()
    command1 = """CREATE TABLE IF NOT EXISTS Menu(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, 
        img_url TEXT, 
        description TEXT, 
        price REAL NOT NULL
    )"""
    cursor.execute(command1)
    connection.commit()
    connection.close()


def deleteTable():  # only used for testing purposes
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()
    command1 = "DROP TABLE Menu"
    cursor.execute(command1)
    connection.commit()
    connection.close()


def add(name, img_url, description, price):  # adds items to table
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Menu (name, img_url, description, price) VALUES (?,?,?,?)",
                   (name, img_url, description, price))
    connection.commit()
    connection.close()


def deleteById(id):  # deletes items in the table by id
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Menu WHERE id=?", (id,))
    connection.commit()
    connection.close()

def deleteAll():
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Menu")
    connection.commit()
    connection.close()

def getById(id):
    # TODO:
    # get and return item from Menu with id
    pass

def getAll():  # returns all items from Menu
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()
    rows = cursor.execute("SELECT * FROM Menu")
    rowsOutput = [row for row in rows]
    connection.close()
    return rowsOutput
