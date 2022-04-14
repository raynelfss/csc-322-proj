import sqlite3

def getConnection(): # helper function that saves lines
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()
    return connection, cursor

def createUserTable():  # creates a table for all users
    connection, cursor = getConnection()
    command1 = """CREATE TABLE IF NOT EXISTS login(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username UNIQUE TEXT, password TEXT)"""
    cursor.execute(command1)
    connection.commit()
    connection.close()

def login(username): # looks for existing users
    connection, cursor = getConnection()
    rows = cursor.execute("SELECT * FROM Menu WHERE username=?", (username,)) 
    row = [row for row in rows][0]
    connection.close()
    return row # returns a user's info based on the username

def register(username, password): # registers new users
    connection, cursor = getConnection()
    cursor.execute("INSERT INTO login (username, password) VALUES (?,?)",
                    (username, password))
    connection.commit()
    connection.close()
    