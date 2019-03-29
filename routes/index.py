from bottle import template, Bottle, redirect, request, response
import helperMethods

import sqlite3
con = sqlite3.connect('./db/webdevils.db')
cur = con.cursor()

COOKIE_SECRET_KEY = "some-secret"
indexRouter = Bottle()

@indexRouter.route('/')
def homepage():
    info = {
        'addr': request.remote_addr,
        'environ': request.environ['HTTP_USER_AGENT']
    }
    return template('home.tpl', info) # unsafe from malicious content

@indexRouter.route('/contactus')
def contactus():
    info = {}
    return template('contactus.tpl', info)

@indexRouter.route('/login')
def login():
    info = {
        'user': {'unikey': ""},
        'message': ''
    }
    return template('login.tpl', info) # unsafe from malicious content

@indexRouter.route('/login', method="POST")
def loginhandler():
    unikey = request.forms.get('unikey')
    password = request.forms.get('password')
    errors = helperMethods.validateForm(request.forms, ['unikey', 'password'])
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
    return template('login.tpl', info)

@indexRouter.route('/logout')
def logout():
    # if user is NOT logged in
        # redirect back to login page
    # if logged if __name__ == '__main__':
    response.delete_cookie('unikey')
        # remove user from session?
    return redirect('/')
