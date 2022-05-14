from helpers import DatabaseConnection

def createTable():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS DiscussionsTable (
            DiscussionID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Subject TEXT NOT NULL,
            CreatorID INT NOT NULL)                                       
        """)

def deleteTable(): 
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE IF EXISTS DiscussionsTable")

def getDiscussions():
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM DiscussionTable")
        discussions = [listToDict(row) for row in rows]
        return discussions

def addDiscussion(subject, creatorID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("""INSERT INTO ComplaintSystemTable (Subject=?, CreatorID=?) RETURNING *""",
            (subject,creatorID,))
        discussion = [listToDictID(row) for row in rows][0]
        return discussion['discussionID']  #should return the discussion ID

def getDiscussionByID(discussionID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM DiscussionsTable Where DiscussionID=?", (discussionID,))
        discussion = [listToDict(row) for row in rows][0]
        return discussion

def deleteDiscussionByID(discussionID): 
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM DiscussionsTable WHERE DiscussionID=?", (discussionID,))

def listToDictID(discussion): return { 'discussionID': discussion[0] }

def listToDict(discussion):
    return {
        'discussionID': discussion[0], 'subject': discussion[1],
        'creatorID': discussion[2]
    }
