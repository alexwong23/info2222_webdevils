from bottle import template, request, redirect, response

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
# Index
#-----------------------------------------------------------------------------

def index_page():
    info = {
        'addr': request.remote_addr,
        'environ': request.environ['HTTP_USER_AGENT']
    }
    return template("index.tpl", info) # unsafe from malicious content

#-----------------------------------------------------------------------------
# Login
#-----------------------------------------------------------------------------

def login_page():
    info = {
        'user': {'unikey': ""},
        'message': ''
    }
    return template("login.tpl", info)  # unsafe from malicious content



#-----------------------------------------------------------------------------

# Check the login credentials
def login_check(unikey, password):
    # # By default assume bad creds
    # login = True
    #
    # if username != "admin": # Wrong Username
    #     err_str = "Incorrect Username"
    #     login = False
    #
    # if password != "password": # Wrong password
    #     err_str = "Incorrect Password"
    #     login = False
    #
    # if login:
    #     return page_view("valid", name=username)
    # else:
    #     return


    errors = helperMethods.formErrors(request.forms, ['unikey', 'password'])
    cur.execute('SELECT unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)', (unikey,))
    user = helperMethods.userToDict(cur.fetchone())
    if(user is not None and unikey and password):
        if(user['unikey'] == unikey and user['password'] == password):
            response.set_cookie('unikey', user['unikey'], secret=COOKIE_SECRET_KEY)
            redirect('/users/' + unikey)
        else:
            errors.append('Login Failed: Invalid UniKey or Password.')
    elif(user is None and unikey and password):
        errors.append("Login Failed: The user does not exist.")
    info = {
        'user': {'unikey': unikey},
        'message': errors
    }
    return template("login.tpl", info)

#-----------------------------------------------------------------------------
# About Us & Contact Us
#-----------------------------------------------------------------------------

def about_page():
    return template("about.tpl")

def contact_page():
    return template("contact.tpl")

# info = {
#     'garble': about_garble()
# }

# # Returns a random string each time
# def about_garble():
#     garble = ["leverage agile frameworks to provide a robust synopsis for high level overviews.",
#     "iterate approaches to corporate strategy and foster collaborative thinking to further the overall value proposition.",
#     "organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment.",
#     "bring to the table win-win survival strategies to ensure proactive domination.",
#     "ensure the end of the day advancement, a new normal that has evolved from generation X and is on the runway heading towards a streamlined cloud solution.",
#     "provide user generated content in real-time will have multiple touchpoints for offshoring."]
#     return garble[random.randint(0, len(garble) - 1)]

#-----------------------------------------------------------------------------
# Error
#-----------------------------------------------------------------------------

def error_page(url):
    return template("error.tpl", {
        'title': 'Error: 404 Not Found',
        'message': 'We could not find the requested URL: ' + url
    })
