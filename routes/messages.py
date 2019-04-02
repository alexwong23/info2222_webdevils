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
# Template Message
#-----------------------------------------------------------------------------

def message_user(receipient):
    updatedDict = {'user':{},'receiver':{},'messages':None,'othersReceivers':{}}
    user = helperMethods.token_user_info()

    # SELECT users.id, users.unikey, users.password, users.first_name, users.last_name, users.status
    #     FROM messages JOIN users ON messages.receiver_id=users.id OR messages.sender_id=users.id
    #     WHERE messages.sender_id=5 OR messages.receiver_id=5 ORDER BY messages.date_created ASC
    receiver_tuple = cur.execute("""
        SELECT users.id, users.unikey, users.password, users.first_name, users.last_name, users.status
        FROM messages JOIN users ON messages.receiver_id=users.id
        WHERE messages.sender_id=(?) ORDER BY messages.date_created ASC""",
        (user['id'],)).fetchone()
    con.commit()
    receiver = helperMethods.userToDict(receiver_tuple)
    print("receiver is :" + receiver['unikey'])
    if(receiver['unikey'] != ""):
        redirect('/messages/' + receiver['unikey'])
    else:
        redirect('/messages/' + 'admin1')


def message_user(receipient):
    user = helperMethods.token_user_info()
    cur.execute('SELECT id, unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)',(receipient,))
    con.commit()
    receiver = helperMethods.userToDict(cur.fetchone())
    messages = helperMethods.messages_to_list(user['id'], receiver['id'])
    return template('message.tpl', {
            'user': user,
            'receiver': receiver,
            'messages': messages
        })

def message_user_send(receipient,text_Message):
    user = helperMethods.token_user_info()

    cur.execute('SELECT id, unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)',(receipient,))
    con.commit()
    receiver = helperMethods.userToDict(cur.fetchone())

    if text_Message is "":
        redirect('/messages/'+receiver['unikey'])
    else:
        cur.execute('INSERT INTO messages (date_created,text,sender_id,receiver_id) VALUES (datetime("now", "localtime"),?,?,?)',(text_Message,user['id'],receiver['id']))
        con.commit()
        redirect('/messages/'+receiver['unikey'])







# @messageRouter.route('/<unikey>/<receipient>', method="GET")
# def messageProfile(unikey,receipient):
#     # cur.execute('SELECT id,unikey, text, date_created, sender_id, receiver_id FROM messages WHERE unikey=(?) AND sender_id=(?)', (unikey,receipient))
#     # user = helperMethods.userToMessages(cur.fetchone())
#     # cur.execute('SELECT id,unikey, text, date_created, sender_id, receiver_id FROM messages WHERE unikey=(?)', (receipient,))
#     # receipient = helperMethods.receipientToMessages(cur.fetchone())
#     # user.update(receipient)
#     dictMessage = {'user': unikey, 'receiver': receipient}
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
