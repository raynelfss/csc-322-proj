from helpers import DatabaseConnection

def createRatingsTable():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS RatingSystemTable (
                RatingID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                UserID INTEGER NOT NULL,
                Review TEXT NOT NULL, 
                Rating INTEGER NOT NULL DEFAULT 0,
                DishID INTEGER NOT NULL )
            """)

def deleteTable():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE IF EXISTS RatingSystemTable")

def addRating(userID, rating, review, dishID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("""INSERT INTO RatingSystemTable (UserID, Rating, review, DishID)
            VALUES (?,?,?,?) RETURNING *""",(userID, rating, review, dishID,))
        rating = [listToDict(row) for row in rows][0]
        return rating

def deleteRating(ratingID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM RatingSystemTable WHERE RatingID=?", (ratingID,))

def getRatingByID(ratingID): # returns a specific rating by its ID
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM RatingSystemTable WHERE RatingID=?", (ratingID,))
        rating = [listToDict(row) for row in rows][0]
        return rating

def getAllRatings():
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM RatingSystemTable")
        ratings = [listToDict(row) for row in rows]
        return ratings

def getRatingsByDish(dishID): # returns a list of ratings for a certain dishID 
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM RatingSystemTable WHERE DishID=?", (dishID,))
        ratings = [listToDict(row) for row in rows]
        return ratings

def avgRatingOfDish(dishID): # returns the avg rating of a dish
    ratingSum = 0
    averageRating = 0
    ratings = getRatingsByDish(dishID)
    
    for rating in ratings: ratingSum += rating['Rating']
    averageRating = ratingSum/len(ratings)

    return round(averageRating, 1) # rounds rating to 1 decimal place

def topThreeRated(menuList):
    allRatings = {}
    topThree = []

    for item in menuList:
        ratingNum = avgRatingOfDish(menuList['dishID'])
        allRatings[menuList['dishID']] = ratingNum 
        
    for i in range(3):
        maxKey = max(allRatings, key= allRatings.get)
        topThree.append(maxKey)
        allRatings.pop(maxKey)

    return topThree
    
def listToDict(rating):
    return {
        'RatingID': rating[0], 'UserID': rating[1],
        'Review': rating[2], 'Rating': rating[3], 
        'DishID': rating[4]
    }
