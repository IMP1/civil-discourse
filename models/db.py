# Create Database
db = DAL('sqlite://store.db')

# User table
db.define_table('user',
                    Field('username', 'string', requires=[IS_NOT_EMPTY(error_message='The username cannot be empty.'), 
                                                          IS_NOT_IN_DB(db, 'user.username', error_message='Sorry! This name has already been taken.'),
                                                          IS_LENGTH(16, error_message='Sorry! You can\'t have a username longer than 16 characters.')]),
                    Field('password', 'password', requires=[IS_NOT_EMPTY(error_message='The password cannot be empty')]))

db.define_table('user_group',
                    Field('name', 'string'))
db.define_table('user_membership',
                    Field('user', db.user),
                    Field('user_group', db.user_group))

# Tag table
db.define_table('tag',
                    Field('name', 'string', requires=[IS_NOT_EMPTY(error_message='The tag name cannot be empty.'), 
                                                      IS_NOT_IN_DB(db, 'tag.name', error_message='Sorry! This tag already exists.'),
                                                      IS_LENGTH(24, error_message='Sorry! You can\'t have a tag longer than 24 characters.')]),
                    Field('scope', 'string', requires=[IS_IN_SET(('user', 'site'))]))

# Conversation table
db.define_table('conversation',
                    Field('title', 'string', requires=[IS_NOT_EMPTY(error_message='You must provide a discussion title.')]))

# Message table
db.define_table('message',
                    Field('author', db.user),
                    Field('conversation', db.conversation),
                    Field('contents', 'text', requires=[IS_NOT_EMPTY(error_message='You haven\'t written a message.')]),
                    Field('time', 'datetime'))

# Tags for conversations
db.define_table('conversation_tag',
                    Field('conversation', db.conversation),
                    Field('tag', db.tag,))

# Add some default tags
if db(db.tag.id > 0).count() == 0:
    db.tag.insert(name='cd-rules', scope='site')
    db.tag.insert(name='religion', scope='user')
    db.tag.insert(name='politics', scope='user')
    db.tag.insert(name='philosophy', scope='user')
    
# Add the user groups
if db(db.user_group.id > 0).count() == 0:
    db.user_group.insert(name='admin')
    db.user_group.insert(name='user')
    db.user_group.insert(name='banned')