import sqlite3

connection = sqlite3.connect('test1.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS DeezNuts(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT, img_url TEXT, description TEXT, price INTEGER)"""

cursor.execute(command1)

def add():#add items to table
    cursor.execute("INSERT INTO DeezNuts VALUES (89, 'Crystal', 'cats.com/img', 'meow', 300)")

connection.commit()

#connection.close()

def view():#view all items from table
    cursor.execute("SELECT * FROM DeezNuts")

results = cursor.fetchall()
print(results)

#retrieve data
for row in cursor.execute('SELECT * FROM DeezNuts ORDER BY price'):
    print(row)