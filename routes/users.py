from bottle import template, Bottle, redirect, request, response
import helperMethods
import sqlite3

COOKIE_SECRET_KEY = "some-secret"

con = sqlite3.connect('./db/webdevils.db')
cur = con.cursor()

usersRouter = Bottle()

@usersRouter.route('/<unikey>')
def userProfile(unikey):
    cur.execute('SELECT unikey, password, name, is_admin FROM users WHERE unikey=(?)', (unikey,))
    user = helperMethods.userToDict(cur.fetchone())
    unikey = request.get_cookie('unikey', secret=COOKIE_SECRET_KEY)
    if(unikey is None or unikey != user['unikey']):
        return template('error.tpl', {
            'title': 'Error: User not found',
            'message': 'Please login'
        })
    else:
        info = {
            'user': user
        }
        return template('userProfile.tpl', info)
