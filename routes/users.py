from bottle import template, Bottle, redirect, request, response
import helperMethods

import sqlite3
con = sqlite3.connect('./db/webdevils.db')
cur = con.cursor()

COOKIE_SECRET_KEY = "some-secret"
usersRouter = Bottle()

@usersRouter.route('/<unikey>')
def userProfile(unikey):
    cur.execute('SELECT unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)', (unikey,))
    user = helperMethods.userToDict(cur.fetchone())
    reqUnikey = request.get_cookie('unikey', secret=COOKIE_SECRET_KEY)
    if(user is None or reqUnikey is None or reqUnikey != user['unikey']):
        return template('error.tpl', {
            'title': 'User Error',
            'message': 'Invalid URL provided: ' + unikey
        })
    elif(user is not None):
        info = {
            'user': user
        }
        return template('userProfile.tpl', info)
    else:
        return template('error.tpl', {
            'title': 'Error 404: Not Found',
            'message': 'We could not find the requested URL: ' + unikey
        })

@usersRouter.route('/<unikey>/edit')
def userEditProfile(unikey):
    info = {
        'addr': 'this is edit page',
        'environ': 'editing success'
    }
    return template('home.tpl', info) # u
