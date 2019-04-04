from bottle import template, request, redirect, response
from datetime import datetime

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
# Index
#-----------------------------------------------------------------------------

def index_page():
    return template("index.tpl", {
        'user': helperMethods.token_user_info()
    }) # unsafe from malicious content

#-----------------------------------------------------------------------------
# Login
#-----------------------------------------------------------------------------

def login_page():
    # secure login page, if user is already logged in
    user = helperMethods.token_user_info()
    if(user['unikey'] != ''):
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'error_message': 'You are already logged in.'
        })
    else:
        return template("login.tpl", {
            'user': user,
            'user_input': '',
            'error_message': ''
        })

# Check the login credentials
def login_check(unikey, password):
    errors = helperMethods.formErrors(request.forms, ['unikey', 'password'])
    user = helperMethods.get_user_details(unikey)
    user_password = cur.execute('SELECT password FROM users WHERE unikey=(?)', (unikey,)).fetchone()[0]
    con.commit()
    if(user is not None and unikey and password):
        if(user['unikey'] == unikey and user_password == password):
            if(user['status'] == 3):
                return template('error.tpl', {
                    'user': helperMethods.token_user_info(),
                    'title': 'Error: Account Banned',
                    'error_message': 'Your account has been banned. Please contact the administrator for further inquiries.'
                })
            else:
                token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
                con.execute("INSERT INTO user_sessions (token, user_id, date_created) VALUES ((?), (?), datetime('now', 'localtime'))", (token, user['id'],))
                con.commit()
                response.set_cookie('token', token, secret=COOKIE_SECRET_KEY)
                redirect('/users/' + unikey)
        else:
            errors.append('Login Failed: Invalid UniKey or Password.')
    elif(user is None and unikey and password):
        errors.append("Login Failed: The user does not exist.")
    user = helperMethods.token_user_info()
    return template("login.tpl", {
        'user': user,
        'user_input': unikey, # save user input
        'error_message': errors
    })

def logout_check():
    user = helperMethods.token_user_info()
    if(user['unikey'] != ''):
        token = request.get_cookie('token', secret=COOKIE_SECRET_KEY)
        con.execute("DELETE FROM user_sessions WHERE token=(?)", (token,))
        con.commit()
        response.delete_cookie('token')
        return template("login.tpl", {
            'user': helperMethods.empty_user_details(), # remove the user to correct layout navbar,
            'user_input': '',
            'error_message': ''
        })
    else:
        return template('error.tpl', {
            'user': user,
            'title': 'Logout Error:',
            'error_message': 'You are not logged in.'
        })

#-----------------------------------------------------------------------------
#Sign up
#-----------------------------------------------------------------------------
def signup_page():
    user = helperMethods.token_user_info()
    if(user['unikey'] != ''):
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'error_message': 'You are already logged in.'
        })
    else:
        return template('signup.tpl', {
                'user': user,
                'error_message': ''
            })


def signup_check(signup_unikey, signup_first_name, signup_last_name, signup_password, signup_confirm_password):
    errors = helperMethods.formErrors(request.forms, ['signup_unikey', 'signup_first_name', 'signup_last_name', 'signup_password', 'signup_confirm_password'])
    user = helperMethods.get_user_details(signup_unikey)
    if user['unikey'] == signup_unikey:
        user = helperMethods.empty_user_details() # remove the user to correct layout navbar
        return template("login.tpl", {
            'user': user,
            'user_input': signup_unikey, # save user input
            'error_message': ['Account already exists, Please Sign In'],
        })
    else:
        if (signup_password == signup_confirm_password):
            cur.execute('INSERT INTO users (unikey, password, status, first_name, last_name, date_created) VALUES (?,?,?,?,?,(datetime("now", "localtime")))',(signup_unikey, signup_password, 0, signup_first_name, signup_last_name))
            con.commit()
            return template("login.tpl", {
                'user': user,
                'user_input': signup_unikey, # save user input
                'error_message': ['Sign up successful, Please log in']
            })
        else:
            errors.append('Passwords do not match. Please re-enter your new password.')
            return template('signup.tpl', {
                'user': helperMethods.token_user_info(),
                'error_message': errors
            })


#-----------------------------------------------------------------------------
# About Us & Contact Us
#-----------------------------------------------------------------------------

def about_page():
    return template("about.tpl", {
        'user': helperMethods.token_user_info()
    })

def contact_page():
    return template("contact.tpl", {
        'user': helperMethods.token_user_info()
    })

#-----------------------------------------------------------------------------
# Error
#-----------------------------------------------------------------------------

def error_page(url):
    return template("error.tpl", {
        'user': helperMethods.token_user_info(),
        'title': 'Error: 404 Not Found',
        'error_message': 'We could not find the requested URL: ' + url
    })
