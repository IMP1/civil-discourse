db = DAL('sqlite://store.db')

db.define_table('user',
                    Field('username', 'string', requires=[IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'user.username')]),
                    Field('password', 'password', requires=[IS_NOT_EMPTY()]),
               )