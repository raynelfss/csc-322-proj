import sqlite3

def createTable(): #creates the table
    connection = sqlite3.connect('test1.db')
    cursor = connection.cursor()
    command1 = """CREATE TABLE IF NOT EXISTS DeezNuts(id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT, img_url TEXT, description TEXT, price INTEGER)"""
    cursor.execute(command1)
    connection.commit()
    connection.close()

def add(id, name, img_url, description, price):#adds items to table
    connection = sqlite3.connect('test1.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO DeezNuts VALUES ({id},'{name}','{img_url}','{description}',{price})".format(
        id = id, name = name, img_url = img_url, description = description, price = price))
    connection.commit()
    connection.close()

def deleteByID(id): #deletes items in the table by id
    connection = sqlite3.connect('test1.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM DeezNuts WHERE id={id}".format(id = id))
    connection.commit()
    connection.close()

def view(): #views all items from table
    connection = sqlite3.connect('test1.db')
    cursor = connection.cursor()
    rows = cursor.execute("SELECT * FROM DeezNuts")
    rowsOutput = [row for row in rows]
    connection.commit()
    connection.close()
    return rowsOutput
