from database.auth import listToDict
from helpers import DatabaseConnection

def createRatingsTable():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS RatingSystemTable (
                RatingID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                UserID INTEGER NOT NULL,
                Rating INTEGER NOT NULL DEFAULT 0,
                DishID INTEGER NOT NULL )
            """)

def deleteTable():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE IF EXISTS RatingSystemTable")

def addRating(userID, rating, dishID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("""INSERT INTO RatingSystemTable (UserID, Rating, DishID)
            VALUES (?,?,?,?) RETURNING *""",(userID, rating, dishID,))
        rating = [listToDict(row) for row in rows][0]
        return rating

def deleteRating(ratingID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM RatingSystemTable WHERE RatingID=?", (ratingID,))

def getRatingByID(ratingID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM RatingSystemTable WHERE RatingID=?", (ratingID,))
        rating = [listToDict(row) for row in rows][0]
        return rating

def getAllRatings():
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM RatingSystemTable")
        ratings = [listToDict(row) for row in rows]
        return ratings

def getRatingsByDish(dishID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM RatingSystemTable WHERE DishID=?", (dishID,))
        ratings = [listToDict(row) for row in rows]
        return ratings

def avgRatingOfDish(dishID):
    ratingSum = 0
    averageRating = 0
    ratings = getRatingsByDish(dishID)
    
    for rating in ratings: ratingSum += rating[2]
    averageRating = ratingSum/len(ratings)

    return averageRating

def listToDict(rating):
    return {
        'RatingID': rating[0], 'UserID': rating[1],
        'Rating': rating[2], 'DishID': rating[3],
    }
