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
    user = helperMethods.token_user_info()
    if(user['unikey'] != ''):
        #earliest sender would be seen first
        cur.execute("""SELECT DISTINCT messages.receiver_first_name, messages.receiver_last_name, messages.receiver_unikey FROM users INNER JOIN messages ON (users.id == messages.sender_id) WHERE unikey= (?) ORDER BY messages.date_created DESC""",(user['unikey'],))
        con.commit()
        #contains the list of all the senders id
        all_receivers = helperMethods.usersList(cur.fetchall())

        return template('message2.tpl',{
                'user': user,
                'messages': "",
                'sender_names': all_receivers,
                'receiver': ""
            })
        # cannot redirect as we need to
        # redirect('/messages/' + user['unikey'])
    else:
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'error_message': 'You have to login to view this page.'
        })



def messages_page(receiver):
    user = helperMethods.token_user_info()
    if(user['unikey'] != ''):
        receiver = helperMethods.get_user_details(receiver)
        messages = helperMethods.messages_to_list(user['id'], receiver['id'])

        cur.execute("""SELECT DISTINCT messages.receiver_first_name, messages.receiver_last_name, messages.receiver_unikey FROM users INNER JOIN messages ON (users.id == messages.sender_id) WHERE unikey= (?) ORDER BY messages.date_created DESC""",(user['unikey'],))
        con.commit()
        #contains the list of all the senders id
        all_receivers = helperMethods.usersList(cur.fetchall())

        return template('message.tpl', {
                'user': user,
                'receiver': receiver,
                'messages': messages,
                'sender_names':all_receivers
            })
    else:
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'error_message': 'You have to login to view this page.'
        })

def messages_check(receiver,text_Message):
    user = helperMethods.token_user_info()
    if(user['unikey'] != ''):
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
    else:
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'error_message': 'You have to login to view this page.'
        })



#-----------------------------------------------------------------------------
# Search Users in Messages
#-----------------------------------------------------------------------------

def search_users(query):
    user = helperMethods.token_user_info()
    if(user['unikey'] != ""):
        if(query is None or query == ""): # prevents error in front end
            redirect('/messages')
        else:
            cur.execute("""
                SELECT first_name, last_name, unikey
                FROM users WHERE unikey LIKE ? OR first_name LIKE ? OR last_name LIKE ?
                """, ('%' + query + '%', '%' + query + '%', '%' + query + '%'))
            con.commit()
            results = helperMethods.usersList(cur.fetchall())
            if(len(results) == 0):
                print(results)
                results = [['0 results for ', '\'' + query + '\'', 'search?query=']]
            return template('message2.tpl',{
                    'user': user,
                    'messages': "",
                    'sender_names': results,
                    'receiver': ""
                })
    else: # user not logged in
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'error_message': 'You have to login to search for user details.'
        })
