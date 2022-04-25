from helpers import DatabaseConnection

def createShoppingCart():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ShoppingCartTable (
            ShoppingCartID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            DishIDs TEXT,
            TotalPrice DOUBLE NOT NULL DEFAULT 0 )
        """)

def deleteTable(): # testing (deletes entire sql table)
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE ShoppingCartTable")

def displayCarts(): # testing (shows all carts)
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM ShoppingCartTable")
        carts = [listToDict(row) for row in rows]
        return carts

def deleteAllCarts(): # empties carts but not delete the table
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM ShoppingCartTable") 

def deleteCart(shoppingCartID): # deletes specific cart
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM ShoppingCartTable WHERE ShoppingCartID=?",
            (shoppingCartID,))

def displayCartByID(shoppingCartID): # displays specific cart
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM ShoppingCartTable WHERE ShoppingCartID=?",
        (shoppingCartID,))
        cart = [listToDict(row) for row in rows]
        return cart

def updateCart(shoppingCartID, dishIDs, totalPrice): # deletes or adds to a cart
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""UPDATE ShoppingCartTable SET (DishIDs=?, TotalPrice=?)
            WHERE ShoppingCartID=?""", (dishIDs, totalPrice, shoppingCartID,))

def listToDict(cart): # helper
    return {
        'shoppingCartID': cart[0], 'dishIDs': cart[1], 'totalPrice': cart[2]
    }
