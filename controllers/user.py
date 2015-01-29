# -*- coding: utf-8 -*-

# 
def login():
    # Create the form.
    form = SQLFORM.factory(db.user)
    # If the form is valid:
    if form.validate() and db(db.user.username == form.vars.username).select():
            # Log the user in.
            user = db(db.user.username == form.vars.username).select(db.user.id)[0]
            session.logged_in_user = user.id
            # Let them know they've been successful.
            session.flash = "You've successfully logged in!"
            # If we were going somewhere:
            if session.redirection != None:
                # Then get back on track!
                target = session.redirection
                del session.redirection
                redirect(target)
            else:
                # Otherwise go to the homepage.
                redirect(URL('default', 'index.html'))
    return dict(form=form)

# 
def register():
    # Create the form.
    form = SQLFORM.factory(db.user)
    if form.validate():
        # Add the user to the database.
        user_id = db.user.insert(**form.vars)
        # Log in the user.
        session.logged_in_user = user_id
        session.flash = "You've successfully registered and have been logged in!"
        # If we were going somewhere:
        if session.redirection != None:
            # Then get back on track!
            target = session.redirection
            del session.redirection
            redirect(target)
        else:
            # Otherwise go to the homepage.
            redirect(URL('default', 'index.html'))
    return dict(form=form)