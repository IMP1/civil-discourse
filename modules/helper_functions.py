from gluon import current
T = current.T
import datetime

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
            return T("just now")
        if elapsed_seconds < 60:
            return T("%s %%{second} ago", symbols=elapsed_seconds)
        if elapsed_seconds < 60 * 60:
            return T("%s %%{minute} ago", symbols=(elapsed_seconds / 60))
        if elapsed_seconds < 60 * 60 * 24:
            return T("%s %%{hour} ago", symbols=(elapsed_seconds / 60 / 60))
    if elapsed_days == 1:
        return "yesterday"
    if elapsed_days < 7:
        return T("%s %%{day} ago", symbols=(elapsed_days))
    if elapsed_days < 30:
        return T("%s %%{week} ago", symbols=(elapsed_days / 7))
    if elapsed_days < 365:
        return T("%s %%{month} ago", symbols=(elapsed_days / 30))
    return T("%s %%{year} ago", symbols=(elapsed_days / 365))

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