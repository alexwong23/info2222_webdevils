from bottle import template, Bottle, redirect, request, response
import helperMethods

import sqlite3
con = sqlite3.connect('./db/webdevils.db')
cur = con.cursor()

COOKIE_SECRET_KEY = "some-secret"
usersRouter = Bottle()


@usersRouter.route('/<unikey>')
def userProfile(unikey):
    cur.execute(
        'SELECT unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)', (unikey,))
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
    cur.execute(
        'SELECT unikey, password, first_name, last_name, status FROM users WHERE unikey=(?)', (unikey,))
    user = helperMethods.userToDict(cur.fetchone())
    info = {
        'user': user
    }
    return template('editprofile.tpl', info)  # u


@usersRouter.route('/<unikey>/changepassword')
def userChangePassword(unikey):
    return template('changepassword.tpl')


@usersRouter.route('/editprofile', method="POST")
def editprofile():
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    reqUnikey = request.get_cookie('unikey', secret=COOKIE_SECRET_KEY)
    cur.execute(
        'UPDATE users SET first_name=(?), last_name=(?) WHERE unikey=(?)', (first_name, last_name, reqUnikey))
    con.commit()
    return redirect(f"/users/{reqUnikey}")


@usersRouter.route('/changepassword', method="POST")
def changepassword():
    print("hello")
    new_password = request.forms.get('new_password')
    confirm_password = request.forms.get('confirm_password')
    reqUnikey = request.get_cookie('unikey', secret=COOKIE_SECRET_KEY)
    if (new_password == confirm_password):
        cur.execute(
            'UPDATE users SET password=(?) WHERE unikey=(?)', (new_password, reqUnikey))
        con.commit()
        return redirect(f"/users/{reqUnikey}")
    else:
        return "wrong password"
