from db_object import DatabaseObject

class User(DatabaseObject):
    
    def __init__(self, db, id)
        self._db = db
        self._id = id

    def getUsername(self):
        return self.__getData().username