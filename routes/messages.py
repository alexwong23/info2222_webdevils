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
    user = helperMethods.token_user_info()
    #earliest sender would be seen first
    cur.execute("""SELECT DISTINCT messages.receiver_first_name, messages.receiver_last_name, messages.receiver_unikey FROM users INNER JOIN messages ON (users.id == messages.sender_id) WHERE unikey= (?) ORDER BY messages.date_created DESC""",(user['unikey'],))
    con.commit()
    #contains the list of all the senders id
    all_receivers = helperMethods.usersList(cur.fetchall())

    # all_receivers.append('user4')
    # all_receivers.append('user2')


    # #Now map the sender_id to their first last_name
    # cur.execute('SELECT first_name,last_name FROM users WEHRE id = ?',(all_receivers))
    # con.commit()
    # all_sender_id  = helperMethods.usersList(cur.fetchall())


    return template('message2.tpl',{'user':user,'messages':"", 'sender_names':all_receivers,'receiver':""})
    # cannot redirect as we need to
    # redirect('/messages/' + user['unikey'])

def messages_page(receiver):
    user = helperMethods.token_user_info()
    receiver = helperMethods.get_user_details(receiver)
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
            'error_message': 'Your account is not allowed to message users. Please contact the administrator for further inquiries.'
        })
    receiver = helperMethods.get_user_details(receiver)

    if text_Message is "":
        redirect('/messages/'+receiver['unikey'])
    else:
        cur.execute('INSERT INTO messages (date_created, text, sender_id, receiver_unikey,receiver_id, receiver_first_name, receiver_last_name) VALUES (datetime("now", "localtime"),?,?,?,?,?,?)',(text_Message, user['id'], receiver['unikey'], receiver['id'],receiver['first_name'], receiver['last_name']))
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
#     user = helperMethods.get_user_details(unikey)
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
#         'error_message': errors
#     }
#     return template('login.tpl', info)
