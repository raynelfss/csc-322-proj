import sqlite3
from colorama import Cursor

def createLoginTable():  # creates the table
    connection = sqlite3.connect('login.db')
    cursor = connection.cursor()
    command1 = """CREATE TABLE IF NOT EXISTS login(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT, password TEXT)"""
    cursor.execute(command1)
    connection.commit()
    connection.close()

def login():  # backend support for login
    db = sqlite3.connect('login.sqlite')
    db.execute('CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT')
    db.execute("INSERT INTO login (username, password) VALUES('admin', 'admin')")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM login where username=? AND password=?", ())