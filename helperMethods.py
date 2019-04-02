from bottle import template, request

import sqlite3
con = sqlite3.connect('./db/webdevils.db')
cur = con.cursor()
COOKIE_SECRET_KEY = "some-secret" # prevent cookie manipulation

def userToDict(tuple):
    if(tuple is None):
        dict = {
            'id': '',
            'unikey': '',
            'first_name': '',
            'last_name': '',
            'status': ''
        }
    else:
        dict = {
            'id': tuple[0],
            'unikey': tuple[1],
            'first_name': tuple[3],
            'last_name': tuple[4],
            'status': tuple[5]
        }
    return dict

def userToMessageAttacher(tuples):
    messagesList = []

    for a in tuples:
        messagesList.append((a[0],a[1]))

    return messagesList



def formErrors(form, required):
    messages = []
    for field in required:
        value = form.get(field)
        if value is "" or value is None:
            messages.append(
                ("You must enter a value for %s in the form" % field))
    return messages

def token_user_info():
    token = request.get_cookie('token', secret=COOKIE_SECRET_KEY)
    cur.execute("""
        SELECT users.id, users.unikey, users.password, users.first_name, users.last_name, users.status
        FROM user_sessions JOIN users ON user_sessions.user_id = users.id WHERE token=(?)""", (token,))
    user = userToDict(cur.fetchone())
    con.commit()
    return user
