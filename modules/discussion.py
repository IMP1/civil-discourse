from db_object import DatabaseObject
from message import Message

class Discussion(DatabaseObject):
    
    def getMessages(self, oldest_first=True):
        if oldest_first:
            order = db.message.time
        else:
            order = ~db.message.time
        message_list = list()
        for msg in db(db.message.conversation == discussion_id).select(orderby=order):
            message_list.append(Message(self._db, msg.id))
        return message_list
    
    def getMessageCount(self):
        return db(db.message.conversation == discussion_id).count()