import sqlite3
from helpers import getConnection

def createEmployeeTable():  # creates a table for all users
    connection, cursor = getConnection()
    cursor.execute(
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
    connection.commit()
    connection.close()

# use this to create user and employee
def createEmployee(username, passwordHash, employeeType):
    connection, cursor = getConnection()

    # Add User
    rows = cursor.execute("INSERT INTO AuthenticationTable (Username, PasswordHash, Role) VALUES (?,?,?) RETURNING UserID",
                                            (username, passwordHash, 'employee',))
    userID = [row for row in rows][0][0]

    # Add Customer
    cursor.execute("INSERT INTO EmployeeTable (UserID, EmployeeType, EmploymentStatus) VALUES (?,?,?)",
                                                (userID, employeeType, True,))

    connection.commit()
    connection.close()
    return userID

def getEmployees():
    connection, cursor = getConnection()
    rows = cursor.execute("SELECT * FROM EmployeeTable")
    employees = [row for row in rows]
    connection.commit()
    connection.close()
    return employees
    

def getEmployee(userID):
    connection, cursor = getConnection()
    rows = cursor.execute("SELECT * FROM EmployeeTable WHERE UserID=?", (userID,))
    employee = [row for row in rows][0]
    connection.commit()
    connection.close()
    return employee


# from passlib.hash import sha256_crypt
# passHash = sha256_crypt.hash('password')
# createEmployee('chefHusan', passHash, 'chef')
# print(getEmployees())