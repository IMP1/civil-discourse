import datetime

def getMessageCount(db, discussion_id):
    return db(db.message.conversation == discussion_id).count()

def getMessages(db, discussion_id):
    return db(db.message.conversation == discussion_id).select(orderby=db.message.time)

def getRecentMessages(db, count):
    return db(db.message.id > 0).select(orderby=~db.message.time, limitby=(0, count))

def getMostRecentMessage(db, discussion_id):
    return db(db.message.conversation == discussion_id).select(orderby=~db.message.time, limitby=(0, 1)).first()

def getLastMessageTime(db, discussion_id):
    last_time = getMostRecentMessage(db, discussion_id).time
    time_now = datetime.datetime.utcnow()
    delta_time = time_now - last_time
    elapsed_days = delta_time.days
    if elapsed_days < 0:
        return "in the future somehow"
    if elapsed_days == 0:
        elapsed_seconds = delta_time.seconds
        if elapsed_seconds < 5:
            return "just now"
        if elapsed_seconds < 60:
            return str(elapsed_seconds) + " seconds ago"
        if elapsed_seconds < 120:
            return "a minute ago"
        if elapsed_seconds < 60 * 60:
            return str(elapsed_seconds / 60) + " minutes ago"
        if elapsed_seconds < 60 * 60 * 24:
            return str(elapsed_seconds / 60 / 60) + " hours ago"
    if elapsed_days == 1:
        return "yesterday"
    if elapsed_days < 7:
        return str(elapsed_days) + " days ago"
    if elapsed_days < 31:
        return str(elapsed_days / 7) + " weeks ago"
    if elapsed_days < 365:
        return str(elapsed_days / 30) + " months ago"
    if elapsed_days < 365 * 2:
        return "a year ago"
    return str(elapsed_days / 365) + " years ago"

def hasUserContributed(db, discussion_id, user_id):
    return db((db.message.conversation == discussion_id) & (db.message.author == user_id)).count() > 0

def hasSiteTags(db, discussion_id):
    return db((db.conversation_tag.conversation == discussion_id) & (db.conversation_tag.tag == db.tag.id) & (db.tag.scope == 'site')).count() > 0

def hasUserTags(db, discussion_id):
    return db((db.conversation_tag.conversation == discussion_id) & (db.conversation_tag.tag == db.tag.id) & (db.tag.scope == 'user')).count() > 0

def getSiteTags(db, discussion_id):
    return db((db.conversation_tag.conversation == discussion_id) & (db.conversation_tag.tag == db.tag.id) & (db.tag.scope == 'site')).select(db.tag.ALL)

def getUserTags(db, discussion_id):
    return db((db.conversation_tag.conversation == discussion_id) & (db.conversation_tag.tag == db.tag.id) & (db.tag.scope == 'user')).select(db.tag.ALL)