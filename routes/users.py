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
# Users
#-----------------------------------------------------------------------------

def redirect_profile_page():
    user = helperMethods.token_user_info()
    redirect('/users/' + user['unikey'])

def profile_page():
    user = helperMethods.token_user_info()
    if(user['unikey'] != ""):
        return template('userProfile.tpl', {
            'user': user
        })
    else: # user not logged in
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'message': 'You have to login to view this page.'
        })

#-----------------------------------------------------------------------------
# Edit Profile
#-----------------------------------------------------------------------------

def edit_profile_page(unikey):
    cur.execute('SELECT unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)', (unikey,))
    user = helperMethods.userToDict(cur.fetchone())
    info = {'user': user}
    return template('editprofile.tpl', info)

def edit_profile_check(first_name, last_name):
    req_unikey = request.get_cookie('unikey', secret=COOKIE_SECRET_KEY)
    cur.execute('UPDATE users SET first_name=(?), last_name=(?) WHERE unikey=(?)', (first_name, last_name, req_unikey))
    con.commit()
    return redirect(f"/users/{req_unikey}")


#-----------------------------------------------------------------------------
# Change Password
#-----------------------------------------------------------------------------

def change_password_page(unikey):
    info = {
        'unikey': unikey,
        'error': ''
    }
    return template('changepassword.tpl', info)

def change_password_check(new_password, confirm_password):
    req_unikey = request.get_cookie('unikey', secret=COOKIE_SECRET_KEY)
    if (new_password == confirm_password):
        cur.execute('UPDATE users SET password=(?) WHERE unikey=(?)', (new_password, req_unikey))
        con.commit()
        return redirect(f"/users/{req_unikey}")
    else:
        info = {
            'unikey': req_unikey,
            'error': 'Passwords does not match. Please re-enter your new password'
        }
        return template('changepassword.tpl', info)
