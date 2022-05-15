from helpers import DatabaseConnection

def createTable():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS SalaryTable (
            EmployeeID INTEGER PRIMARY KEY NOT NULL,
            Salary INTEGER NOT NULL)                                       
        """)

def deleteTable(): 
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE IF EXISTS SalaryTable")

def addSalary(employeeID, salary): 
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("INSERT INTO SalaryTable EmployeeID=?, Salary=?", 
            (employeeID, salary,))

def getSalaries():
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM SalaryTable")
        salaries = [listToDict(row) for row in rows]
        return salaries

def getSalary(employeeID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("SELECT * FROM SalaryTable WHERE EmployeeID=?", (employeeID,)) 

def updateSalary(employeeID, salary):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("UPDATE SalaryTable SET Salary=? WHERE EmployeeID=?", 
        (salary, employeeID,))    

def listToDict(salary):
    return { 'employeeID': salary[0], 'salary': salary[1] }