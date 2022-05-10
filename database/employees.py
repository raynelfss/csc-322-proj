from helpers import DatabaseConnection

def createEmployeeTable():  # creates a table for all users
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS EmployeeTable (
            EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            UserID INTEGER UNIQUE NOT NULL,
            EmployeeType TEXT NOT NULL,
            DemotionPoints INTEGER NOT NULL DEFAULT 0,
            EmploymentStatus BOOLEAN NOT NULL )
        """)

def deleteTable():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE IF EXISTS EmployeeTable")

# use this to create user and employee
def createEmployee(username, passwordHash, employeeType):
    with DatabaseConnection('./database/database.db') as cursor:
        # Add User
        rows = cursor.execute("""INSERT INTO AuthenticationTable 
            (Username, PasswordHash, Role) VALUES (?,?,?) RETURNING UserID""",
            (username, passwordHash, 'employee',))
        userID = [row for row in rows][0][0]
    
        # Add Customer
        cursor.execute("""INSERT INTO EmployeeTable (UserID, EmployeeType, EmploymentStatus) 
            VALUES (?,?,?)""", (userID, employeeType, True,))
            
        return userID

def getEmployees():
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM EmployeeTable")
        employees = [listToDict(row) for row in rows]
        return employees
        
def getEmployee(userID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM EmployeeTable WHERE UserID=?", (userID,))
        employee = [listToDict(row) for row in rows][0]
        return employee

def getEmployeeDemotionPoint(userID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT DemotionPoints FROM EmployeeTable WHERE UserID=?", (userID,))
        return [listToDictPoints(row) for row in rows][0]

def updateEmployeeDemotionPoint(userID,demotionPoints):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("UPDATE EmployeeTable SET DemotionPoints = ? WHERE UserID=?", (demotionPoints,userID,))

def fireEmployee(userID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM EmployeeTable WHERE UserID=?", (userID,))

def listToDictPoints(employee):
    return {
        'demotionPoints': employee[0]
    }
def demoteOnePoint(userID): 
    points = getEmployeeDemotionPoint(userID)
    points -=1
    updateEmployeeDemotionPoint(userID,points)


def promoteOnePoint(userID):
    points = getEmployeeDemotionPoint(userID)
    points +=1
    updateEmployeeDemotionPoint(userID,points)
    
def listToDict(employee):
    return {
        'employeeID': employee[0], 'userID': employee[1], 
        'employeeType': employee[2], 'demotionPoints': employee[3],
        'employmentStatus': employee[4],
    }
