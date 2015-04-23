class DatabaseObject(object):
    
    def __init__(self, db, id):
        self._db = db
        self._id = id
        
    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.getId() == self.getId()
    
    def __getData(self):
        return self._db(self._db.user.id == self._id).select().first()
    
    def getId(self):
        return self._id