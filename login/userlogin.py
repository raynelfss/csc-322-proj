import sqlite3

def createLoginTable():  # creates the table
    connection = sqlite3.connect('login.db')
    cursor = connection.cursor()
    command1 = """CREATE TABLE IF NOT EXISTS login(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT)"""
    cursor.execute(command1)
    connection.commit()
    connection.close()

