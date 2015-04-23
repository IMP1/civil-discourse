import datetime
from db_object import DatabaseObject
from gluon import current
T = current.T

class Message(DatabaseObject):
    
    def __init__(self, db, id):
        self._db = db
        self._id = id
    
    def getTime(self):
        return self.__getData().time
    
    def getElapsedTime(self):
        return datetime.dateime.utcnow() - self.getTime()
        
    def getFriendlyTime(self):
        elapsed_days = self.getElapsedTime().days
        if elapsed_days < 0:
            return "in the future somehow"
        if elapsed_days == 0:
            elapsed_seconds = delta_time.seconds
            if elapsed_seconds < 5:
                return T("just now")
            if elapsed_seconds < 60:
                return T("%s %%{second} ago", symbols=elapsed_seconds)
            if elapsed_seconds < 60 * 60:
                return T("%s %%{minute} ago", symbols=(elapsed_seconds / 60))
            if elapsed_seconds < 60 * 60 * 24:
                return T("%s %%{hour} ago", symbols=(elapsed_seconds / 60 / 60))
        if elapsed_days == 1:
            return T("yesterday")
        if elapsed_days < 7:
            return T("%s %%{day} ago", symbols=(elapsed_days))
        if elapsed_days < 30:
            return T("%s %%{week} ago", symbols=(elapsed_days / 7))
        if elapsed_days < 365:
            return T("%s %%{month} ago", symbols=(elapsed_days / 30))
        return T("%s %%{year} ago", symbols=(elapsed_days / 365))
    
    @staticmethod
    def getMostRecent(discussion=None, count=1):
        if count > 1:
            message_list = list()
            return message_list
        else:
            if discussion == None:
                result = db(db.message.id > 0).select(orderby=~db.message.time, limitby=(0, 1)).first()
            elif isinstance(discussion, int):
                result = db(db.message.conversation == discussion).select(orderby=~db.message.time, limitby=(0, 1)).first()
            elif isinstance(discussion, Discussion):
                result = db(db.message.conversation == discussion.getId()).select(orderby=~db.message.time, limitby=(0, 1)).first()
            return Message(result.id)
        
    @staticmethod
    def getMostRecent(discussion=None):