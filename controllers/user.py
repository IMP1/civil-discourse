# -*- coding: utf-8 -*-

# 
def login():
    if request.vars.redirect:
        session.redirection = request.vars.redirect
    # Create the form.
    form = FORM(
                INPUT(_name='username', requires=IS_IN_DB(db, 'user.username', error_message="That username doesn't exist.")),
                INPUT(_name='password', requires=IS_NOT_EMPTY(error_message="That password is incorrect.")),
                INPUT(_type='submit')
               )
    # If the form is valid:
    if form.validate():
        # Log the user in.
        user = db((db.user.username == form.vars.username) & (db.user.password == form.vars.password)).select(db.user.id)
        if user:
            session.logged_in_user = user[0].id
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
                redirect(URL('default', 'index'))
        else:
            form.errors.password = "Incorrect password"
    return dict(form=form)

# 
def register():
    if request.vars.redirect:
        session.redirection = request.vars.redirect
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
            redirect(URL('default', 'index'))
    return dict(form=form)

def logout():
    session.flash = "You've successfully been logged out."
    del session.logged_in_user
    redirect(URL('default', 'index'))
    
def profile():
    return dict()