from helpers import DatabaseConnection

def createTable():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ThreadsTable (
            CommentID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            CommentorID  INTEGER NOT NULL,
            DiscussionID INT NOT NULL,
            Comment TEXT NOT NULL,
            Flag BOOLEAN NOT NULL )                                       
        """)

def deleteTable():
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DROP TABLE IF EXISTS ThreadsTable")

def getAllComments():
    with DatabaseConnection('./database/database.db') as cursor:
        rows = cursor.execute("SELECT * FROM ThreadsTable")
        comments = [listToDict(row) for row in rows]
        return comments

def addComment(commmentorID, discussionID, comment, flag):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("""INSERT INTO ThreadsTable (CommentorID, DiscussionID, Comment, Flag)
            VALUES (?,?,?,?)""", (commmentorID, discussionID, comment, flag,))

def getCommentsByDiscussion(discussionID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows=cursor.execute("SELECT * FROM ThreadsTable WHERE DiscussionID=?", (discussionID,))
        complaints = [listToDict(row) for row in rows]
        return complaints

def getCommentByID(commentID):
    with DatabaseConnection('./database/database.db') as cursor:
        rows=cursor.execute("SELECT * FROM ThreadsTable WHERE CommentID=?", (commentID,))
        complaints = [listToDict(row) for row in rows]
        return complaints

def deleteCommentsByDiscussion(discussionID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM ThreadsTable WHERE DiscussionID=?", (discussionID,))

def deleteCommentsByID(commentID):
    with DatabaseConnection('./database/database.db') as cursor:
        cursor.execute("DELETE FROM ThreadsTable WHERE CommentID=?", (commentID,))

def listToDict(comment):
    return {
        'commentID': comment[0], 'commentorID': comment[1],
        'discussionID': comment[2], 'comment': comment[3],
        'flag': comment[4]       
    }