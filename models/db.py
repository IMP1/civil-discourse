db = DAL('sqlite://store.db')

db.define_table('user',
                    Field('username', 'string', requires=[IS_NOT_EMPTY(error_message='The username cannot be empty.'), IS_NOT_IN_DB(db, 'user.username', error_message='Sorry! This name has already been taken.')]),
                    Field('password', 'password', requires=[IS_NOT_EMPTY(error_message='The password cannot be empty')]),
               )

db.define_table('tag',
                    Field('name', 'string', requires=[IS_NOT_EMPTY(error_message='The tag name cannot be empty.'), IS_NOT_IN_DB(db, 'tag.name', error_message='Sorry! This tag already exists.')]),
                    Field('scope', 'string', requires=[IS_IN_SET(('user', 'site'))]),
               )

# Groups messages
db.define_table('conversation',
                    Field('title', 'string', requires=[IS_NOT_EMPTY(error_message='You must provide a discussion title.')]),
               )

db.define_table('message',
                    Field('author', db.user),
                    Field('conversation', db.conversation),
                    Field('contents', 'text', requires=[IS_NOT_EMPTY(error_message='You haven\'t written a message.')]),
                    Field('time', 'datetime'),
                )


db.define_table('conversation_tag',
                    Field('conversation', db.conversation),
                    Field('tag', db.tag,)
               )

if db(db.tag.id > 0).count() == 0:
    db.tag.insert(name="cd-rules", scope="site")
    db.tag.insert(name="religion", scope="user")
    db.tag.insert(name="politics", scope="user")
    db.tag.insert(name="philosophy", scope="user")