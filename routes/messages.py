from bottle import template, request, redirect
import random, helperMethods

from datetime import datetime

'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''

# remove this and put it in sql file handler
import sqlite3
con = sqlite3.connect('./db/webdevils.db')
cur = con.cursor()
COOKIE_SECRET_KEY = "some-secret" # prevent cookie manipulation

#-----------------------------------------------------------------------------
# Messages
#-----------------------------------------------------------------------------

def all_messages_page():
    # incomplete
    redirect('/messages/' + receiver['unikey'])

def messages_page(receiver):
    user = helperMethods.token_user_info()
    cur.execute('SELECT id, unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)',(receiver,))
    con.commit()
    receiver = helperMethods.userToDict(cur.fetchone())
    messages = helperMethods.messages_to_list(user['id'], receiver['id'])
    return template('message.tpl', {
            'user': user,
            'receiver': receiver,
            'messages': messages
        })

def messages_check(receiver,text_Message):
    user = helperMethods.token_user_info()
    if(user['status'] == 2):
        return template('error.tpl', {
            'user': helperMethods.token_user_info(),
            'title': 'Error: Account Muted',
            'message': 'Your account is not allowed to message users. Please contact the administrator for further inquiries.'
        })
    cur.execute('SELECT id, unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)',(receiver,))
    con.commit()
    receiver = helperMethods.userToDict(cur.fetchone())
    if text_Message is "":
        redirect('/messages/'+receiver['unikey'])
    else:
        cur.execute('INSERT INTO messages (date_created,text,sender_id,receiver_id) VALUES (datetime("now", "localtime"),?,?,?)',(text_Message,user['id'],receiver['id']))
        con.commit()
        redirect('/messages/'+receiver['unikey'])


# @messageRouter.route('/<unikey>/<receiver>', method="GET")
# def messageProfile(unikey,receiver):
#     # cur.execute('SELECT id,unikey, text, date_created, sender_id, receiver_id FROM messages WHERE unikey=(?) AND sender_id=(?)', (unikey,receiver))
#     # user = helperMethods.userToMessages(cur.fetchone())
#     # cur.execute('SELECT id,unikey, text, date_created, sender_id, receiver_id FROM messages WHERE unikey=(?)', (receiver,))
#     # receiver = helperMethods.receiverToMessages(cur.fetchone())
#     # user.update(receiver)
#     dictMessage = {'user': unikey, 'receiver': receiver}
#     return template('message.tpl',dictMessage)
#
# @messageRouter.route('/send', method="POST")
# def messageSend():
#     message = request.forms.get('textSend')
#     cur.execute('SELECT unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)', (unikey,))
#     user = helperMethods.userToDict(cur.fetchone())
#     if(user is not None and unikey and password):
#         if(user['unikey'] == unikey and user['password'] == password):
#             response.set_cookie('unikey', user['unikey'], secret=COOKIE_SECRET_KEY)
#             redirect('/users/' + unikey)
#         else:
#             errors.append('Login Failed: Invalid UniKey or Password.')
#     elif(user is None and unikey and password):
#         errors.append("Login Failed: The user does not exist.")
#     info = {
#         'user': {'unikey': unikey},
#         'message': errors
#     }
#     return template('login.tpl', info)
