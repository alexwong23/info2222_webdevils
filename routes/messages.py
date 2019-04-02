from bottle import template, request, redirect
import random, helperMethods

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
    updatedDict = {'user':{}, 'receiver':{}}
    user = helperMethods.token_user_info()
    updatedDict['user'] = user

    cur.execute('SELECT id, unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)',(receipient,))
    con.commit()
    updatedDict['receiver'] = helperMethods.userToDict(cur.fetchone())
    print(updatedDict['receiver'])
    return template('message.tpl',updatedDict)



# def message_user_send(receipient):




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
