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
            'message': 'Only the administrator can view this page.'
        })
