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
# Index
#-----------------------------------------------------------------------------

def index_page():
    info = {
        'user': helperMethods.token_user_info(),
        'addr': request.remote_addr,
        'environ': request.environ['HTTP_USER_AGENT']
    }
    return template("index.tpl", info) # unsafe from malicious content

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
            'message': 'You are already logged in.'
        })
    else:
        return template("login.tpl", {
            'user': user,
            'user_input': '',
            'message': ''
        })

# Check the login credentials
def login_check(unikey, password):
    errors = helperMethods.formErrors(request.forms, ['unikey', 'password'])
    user_tuple = cur.execute('SELECT id, unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)', (unikey,)).fetchone()
    con.commit()
    user = helperMethods.userToDict(user_tuple)
    if(user is not None and unikey and password):
        if(user['unikey'] == unikey and user_tuple[2] == password):
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
        'message': errors
    })

def logout_check():
    user = helperMethods.token_user_info()
    if(user['unikey'] != ''):
        token = request.get_cookie('token', secret=COOKIE_SECRET_KEY)
        con.execute("DELETE FROM user_sessions WHERE token=(?)", (token,))
        con.commit()
        response.delete_cookie('token')
        return template("login.tpl", {
            'user': helperMethods.token_user_info(),
            'user_input': '',
            'message': ''
        })
    else:
        return template('error.tpl', {
            'user': user,
            'title': 'Logout Error:',
            'message': 'You are not logged in.'
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
        'message': 'We could not find the requested URL: ' + url
    })
