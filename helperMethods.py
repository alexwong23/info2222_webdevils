from bottle import template, request

import sqlite3
con = sqlite3.connect('./db/webdevils.db')
cur = con.cursor()
COOKIE_SECRET_KEY = "some-secret" # prevent cookie manipulation


def empty_user_details():
    return {
        'id': '',
        'unikey': '',
        'first_name': '',
        'last_name': '',
        'status': ''
    }

def user_to_dict(tuple):
    if(tuple is None):
        dict = empty_user_details()
    else:
        dict = {
            'id': tuple[0],
            'unikey': tuple[1],
            'first_name': tuple[3],
            'last_name': tuple[4],
            'status': tuple[5]
        }
    return dict

def get_user_details(unikey):
    tuple = cur.execute('SELECT id, unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)', (unikey,)).fetchone()
    con.commit()
    return user_to_dict(tuple)

def messages_to_list(user_id, receiver_id):
    # cross join
    messages_tuple = cur.execute("""SELECT * FROM
        (SELECT sender_id ,text, date_created FROM messages
            WHERE (sender_id = (?) AND receiver_id = (?))
            OR (sender_id = (?) AND receiver_id = (?))
            ORDER BY date_created ASC)""",
        (user_id, receiver_id, receiver_id, user_id)).fetchall()
    con.commit()
    messages_list = []
    for a in messages_tuple:
        messages_list.append((a[0],a[1],dateSplitter(a[2])))
    return messages_list

def dateSplitter(b):
    newlist = []
    list_strings = b.split()
    date = list_strings[0]
    time = list_strings[1]
    newlist.append(date)
    newlist.append(time)
    return newlist

def usersList(a):
    newList = []
    for user in a:
        newList.append(user)
    return newList



def senderString(a):
    stringer = ""
    for user in a:
        stringger += stringger+' user_id = ' + user

    return stringer


def formErrors(form, required):
    messages = []
    for field in required:
        value = form.get(field)
        if value is "" or value is None:
            messages.append(("Please provide a %s." % field))
    return messages

def signupErrors(form, required):
    messages = []
    for field in required:
        value = form.get(field)
        if value is "" or value is None:
            if(field == 'signup_unikey'):
                messages.append(("Please provide a unikey."))
            elif(field == 'signup_first_name'):
                messages.append(("Please provide a first name."))
            elif(field == 'signup_last_name'):
                messages.append(("Please provide a last name."))
            elif(field == 'signup_password'):
                messages.append(("Please provide a password."))
            elif(field == 'signup_confirm_password'):
                messages.append(("Please confirm the password."))
    return messages

def token_user_info():
    token = request.get_cookie('token', secret=COOKIE_SECRET_KEY)
    cur.execute("""
        SELECT users.id, users.unikey, users.password, users.first_name, users.last_name, users.status
        FROM user_sessions JOIN users ON user_sessions.user_id = users.id WHERE token=(?)""", (token,))
    con.commit()
    user = user_to_dict(cur.fetchone())
    return user
