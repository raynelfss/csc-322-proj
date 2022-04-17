import sqlite3

DenisseDB = "database.db"
conn = sqlite3.connect(DenisseDB)
cur = conn.cursor()

cur.execute( # Create the Blacklist Table
    """
    CREATE TABLE IF NOT EXISTS BlacklistTable (
        BlacklistID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        BannedIPs TEXT NOT NULL
    )
    """
)

cur.execute( # Create the Authentication
    """
    CREATE TABLE IF NOT EXISTS AuthenticationTable (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Username TEXT NOT NULL,
        PasswordHash TEXT NOT NULL,
        Role TEXT NOT NULL
    )
    """
)

cur.execute( # Create Customer Table
    """
    CREATE TABLE IF NOT EXISTS CustomerTable (
        CustomerID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        UserID INTEGER UNIQUE NOT NULL,
        Name TEXT NOT NULL,
        PhoneNumber TEXT UNIQUE NOT NULL,
        VipStatus BOOLEAN NOT NULL DEFAULT FALSE,
        Balance DOUBLE NOT NULL DEFAULT 0,
        NumberOfOrders INTEGER NOT NULL DEFAULT 0,
        MoneySpent DOUBLE NOT NULL DEFAULT 0,
        ShoppingCartID INTEGER UNIQUE NOT NULL,
        Karen BOOLEAN NOT NULL DEFAULT FALSE,
        DemotionPoints INTEGER NOT NULL DEFAULT 0
    )
    """
)

cur.execute( # Create Employee Table
    """
    CREATE TABLE IF NOT EXISTS EmployeeTable (
        EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        UserID INTEGER UNIQUE NOT NULL,
        EmployeeType TEXT NOT NULL,
        DemotionPoints INTEGER NOT NULL DEFAULT 0,
        EmploymentStatus BOOLEAN NOT NULL
    )
    """
)

cur.execute( # Create Shopping Cart Table
    """
    CREATE TABLE IF NOT EXISTS ShoppingCartTable (
        ShoppingCartID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        DishIDs TEXT,
        TotalPrice DOUBLE NOT NULL DEFAULT 0
    )
    """
)

cur.execute( # Create Food Table
    """
    CREATE TABLE IF NOT EXISTS FoodTable (
        DishID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        DishName TEXT NOT NULL,
        Description TEXT,
        Price DOUBLE NOT NULL DEFAULT 1,
        ImageURL TEXT,
        ChefID INTEGER UNIQUE NOT NULL
    )
    """
)

cur.execute( # Create Orders Table
    """
    CREATE TABLE IF NOT EXISTS OrderTable (
        OrderID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        DishIDs TEXT NOT NULL,
        CustomerID INTEGER NOT NULL,
        Address TEXT NOT NULL,
        Cost DOUBLE NOT NULL,
        Datetime DATETIME NOT NULL,
        EmployeeID INTEGER,
        DeliveryMethod TEXT NOT NULL,
        Status TEXT NOT NULL
    )
    """
)

cur.execute( # Create Rating System Table
    """
    CREATE TABLE IF NOT EXISTS RatingSystemTable (
        RatingID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        EmployeeID INTEGER NOT NULL,
        Amount DOUBLE NOT NULL DEFAULT 0,
        OrderID INTEGER NOT NULL
    )
    """
)

cur.execute( # Create Bidding System Table
    """
    CREATE TABLE IF NOT EXISTS BiddingSystemTable (
        BidID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        EmployeeID INTEGER NOT NULL,
        Amount DOUBLE NOT NULL,
        OrderID INTEGER NOT NULL
    )
    """
)

# Save and Commit Everything
conn.commit()
conn.close()