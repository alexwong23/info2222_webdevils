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
    updatedDict = {'user':{},'receiver':{},'messages':None}
    user = helperMethods.token_user_info()
    updatedDict['user'] = user

    cur.execute('SELECT id, unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)',(receipient,))
    con.commit()
    updatedDict['receiver'] = helperMethods.userToDict(cur.fetchone())



    # cur.execute('SELECT text FROM messages WHERE (sender_id = (?) AND receiver_id = (?)) ORDER BY date_created ASC',(updatedDict['user']['id'],updatedDict['receiver']['id'],))
    # con.commit()
    # allMessages = cur.fetchall()

#     SELECT *
# FROM (  SELECT SUM(Fdays) AS fDaysSum
#         FROM tblFieldDays
#         WHERE tblFieldDays.NameCode=35
#         AND tblFieldDays.WeekEnding=1) A -- use you real query here
# CROSS JOIN (SELECT SUM(CHdays) AS hrsSum
#             FROM tblChargeHours
#             WHERE tblChargeHours.NameCode=35
#             AND tblChargeHours.WeekEnding=1) B -- use you real query here

    cur.execute('SELECT * FROM (SELECT sender_id ,text FROM messages WHERE (sender_id = (?) AND receiver_id = (?)) OR (sender_id = (?) AND receiver_id = (?)) ORDER BY date_created ASC)',(updatedDict['user']['id'],updatedDict['receiver']['id'],updatedDict['receiver']['id'],updatedDict['user']['id']))
    con.commit()
    allMessages = helperMethods.userToMessageAttacher(cur.fetchall())
    updatedDict['messages']= allMessages



    # cur.execute('SELECT text FROM messages WHERE sender_id = (?) AND receiver_id = (?) ORDERBY date_created ASC',(receipient['id'],user['id'],))
    # con.commit()
    # sender_messages = cur.fetchone()

    return template('message.tpl',updatedDict)



def message_user_send(receipient,text_Message):
    user = helperMethods.token_user_info()

    cur.execute('SELECT id, unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)',(receipient,))
    con.commit()
    receiver = helperMethods.userToDict(cur.fetchone())


    cur.execute('INSERT INTO messages (date_created,text,sender_id,receiver_id) VALUES (datetime("now", "localtime"),?,?,?)',(text_Message,user['id'],receiver['id']))
    con.commit()

    stringer = '/messages/'+receiver['unikey']
    redirect(stringer)







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
