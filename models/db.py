db = DAL('sqlite://store.db')

db.define_table('user',
                    Field('username', 'string', requires=[IS_NOT_EMPTY(error_message='The username cannot be empty.'), IS_NOT_IN_DB(db, 'user.username', error_message='Sorry! This name has already been taken.')]),
                    Field('password', 'password', requires=[IS_NOT_EMPTY(error_message='The password cannot be empty')]),
               )

# Groups messages
db.define_table('conversation')

db.define_table('message',
                    Field('author', db.user),
                    Field('conversation', db.conversation),
                    Field('contents', 'text', requires=[IS_NOT_EMPTY(error_message='You haven\'t written a message.')]),
                    Field('time', 'datetime')
                )

