from bottle import template, request, redirect, response

import string, random, helperMethods
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
# Admin
#-----------------------------------------------------------------------------

def admin_page():
    user = helperMethods.token_user_info()
    if(user['status'] == 1):
        return template("admin.tpl", {
            'user': helperMethods.token_user_info()
        })
    else:
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'error_message': 'Only the administrator can view this page.'
        })


#-----------------------------------------------------------------------------
# Admin Change Status
#-----------------------------------------------------------------------------

def change_status(query, unikey, status):
    user = helperMethods.token_user_info()
    if(user['unikey'] != "" and user['status'] == 1):
        print('hello')
        if(query is None or query == "" or status is None
            or status == ""): # prevents error in front end
            redirect('users/search')
        else:
            # we assume we dont need validation for status and unikey
            # need to prevent from changing to admin
            print('world')
            cur.execute('UPDATE users SET status=(?) WHERE unikey=(?)', (status, unikey))
            con.commit()
            redirect('/users/search?query=' + query)
    else:
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to change status',
            'error_message': 'Only the administrator can change the status of other users.'
        })
