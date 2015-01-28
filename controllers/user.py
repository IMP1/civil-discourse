def login():
    # Create the form
    form = FORM(INPUT(_name='username', requires=[IS_NOT_EMPTY(), IS_IN_DB(db, "user.username")]), INPUT(_type='submit'))
    # If the form is valid
    if form.validate(formname="login") and db(db.user.username == form.vars.username).select():
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