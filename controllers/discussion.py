# -*- coding: utf-8 -*-
import datetime

def __get_feed(discussion_id):
    discussion = db.conversation[discussion_id]
    feed = CAT(
        XML("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"),
        XML("<feed xmlns=\"http://www.w3.org/2005/Atom\">\n"),
        XML("\t<title>"), discussion.title, XML("</title>\n"),
        XML("\t<link href=\""), URL("discussion", "view", args=[discussion_id]), XML("\" />\n"),
        XML("\t<id>"), "", XML("</id>\n"),
        XML("\t<updated>"), "2016-01-01T00:00:02Z", XML("</updated>\n"),
    )
    for comment in db(db.message.conversation == discussion_id).select():
        print(URL("discussion", "view", args=[discussion_id], anchor="message-" + str(comment.id), scheme=True, host=True))
        feed = CAT(feed, 
            XML("\t<entry>\n"),
            XML("\t\t<title>"), "Reply by User", XML("</title>\n"),
            XML("<link href=\""), URL("discussion", "view", args=[discussion_id], anchor="message-" + str(comment.id), scheme=True, host=True), XML("\" rel=\"alternate\" />"),
            XML("\t\t<updated>"), str(comment.time).replace(" ", "T") + "Z", XML("</updated>\n"),
            XML("\t\t<content type=\"xhtml\"><p>"), comment.contents, XML("</p></content>\n"),
            XML("\t\t<author>\n"),
            XML("\t\t\t<name>"), db.user[comment.author].username, XML("</name>\n"),
            XML("\t\t</author>\n"),
            XML("\t</entry>\n"),
        )
    feed = CAT(feed, XML("</feed>"))
    return feed

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
    if (request.args[-1] == "feed"):
        print("getting feed!")
        return __get_feed(discussion_id)
    form = SQLFORM.factory(db.message.contents)
    if form.validate():
        message_id = db.message.insert(author=session.logged_in_user, conversation=discussion_id, contents=form.vars.contents, time=datetime.datetime.utcnow())
        session.flash = ""
        redirect(URL(args=[discussion_id], anchor="message-"+str(message_id)))
    return dict(discussion_id=discussion_id, form=form)

def search():
    if request.vars.search_text == "" and not request.vars.search_tag:
        # Remove empty search text var in URL
        redirect(URL('discussion', 'search'))
    return dict()

def rules():
    return dict()