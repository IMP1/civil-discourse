import datetime

# -*- coding: utf-8 -*-
def new():
    if not session.logged_in_user:
        session.redirection = URL('discussion', 'new', vars=request.vars)
        session.flash = SPAN('You are not currently signed in. Sign in or ', A('Register', _href=URL('user', 'register')), '!')
        redirect(URL('user', 'login'))
    # Create the form.
    form = SQLFORM.factory(db.conversation.title, db.message.contents)
    if form.validate():
        # 1. Create conversation
        discussion_id = db.conversation.insert(title=form.vars.title)
        # 2. Create message with filled in information (time now, signed in user, conversation just created)
        message_id = db.message.insert(author=session.logged_in_user, conversation=discussion_id, contents=form.vars.contents, time=datetime.datetime.utcnow())
        # Redirect to the new discussion
        session.flash = "You've successfully started a discussion!"
        redirect(URL('discussion', 'view', args=[discussion_id], anchor="message-"+str(message_id)))
    return dict(form=form)

def view():
    discussion_id = request.args[0]
    form = SQLFORM.factory(db.message.contents)
    if form.validate():
        message_id = db.message.insert(author=session.logged_in_user, conversation=discussion_id, contents=form.vars.contents, time=datetime.datetime.utcnow())
        session.flash = ""
        redirect(URL(args=[discussion_id], anchor="message-"+str(message_id)))
    return dict(discussion_id=discussion_id, form=form)

def search():
    if not request.vars.search_text:
        if request.vars.search_tag:
            redirect(URL('tags'))
        else:
            redirect(URL('all'))
    return dict()

def rules():
    return dict()

def all():
    return dict()

def tags():
    return dict()