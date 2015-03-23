
def getMessages(discussion_id, db)
    return db(db.message.conversation == discussion_id).select(orderby=db.message.time)