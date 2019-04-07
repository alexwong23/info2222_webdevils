from bottle import template, request, redirect

import random
import helperMethods
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
COOKIE_SECRET_KEY = "some-secret"  # prevent cookie manipulation

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------

def redirect_profile_page():
    user = helperMethods.token_user_info()
    if(user['unikey'] != ""):
        redirect('/users/' + user['unikey'])
    else:  # user not logged in
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'error_message': 'You have to login to view this page.'
        })

def profile_page(unikey):
    user = helperMethods.token_user_info()
    if(user['unikey'] != ""):
        any_user = helperMethods.get_user_details(unikey)
        return template('userProfile.tpl', {
            'user': user,
            'any_user': any_user
        })
    else:  # user not logged in
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'error_message': 'You have to login to view this page.'
        })

# -----------------------------------------------------------------------------
# Edit Profile
# -----------------------------------------------------------------------------


def edit_profile_page(unikey):
    user = helperMethods.token_user_info()
    if(user['unikey'] != ""):
        return template('editprofile.tpl', {
            'user': user,
            'error': ''
        })
    else:  # user not logged in
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'error_message': 'You have to login to view this page.'
        })


def edit_profile_check(first_name, last_name):
    user = helperMethods.token_user_info()
    if(user['unikey'] != ""):
        if first_name == "" or last_name == "":
            return template('editprofile.tpl', {
                'user': user,
                'error': 'First name or last name should not be empty. Please re-enter.'
            })
        cur.execute('UPDATE users SET first_name=(?), last_name=(?) WHERE unikey=(?)',
                    (first_name, last_name, user['unikey']))
        con.commit()
        return redirect(f"/users/{user['unikey']}")
    else:  # user not logged in
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'error_message': 'You have to login to view this page.'
        })

# -----------------------------------------------------------------------------
# Change Password
# -----------------------------------------------------------------------------


def change_password_page(unikey):
    user = helperMethods.token_user_info()
    if(user['unikey'] != ""):
        return template('changepassword.tpl', {
            'user': user,
            'error': ''
        })
    else:  # user not logged in
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'error_message': 'You have to login to view this page.'
        })


def change_password_check(new_password, confirm_password):
    user = helperMethods.token_user_info()
    if(user['unikey'] != ""):
        if len(new_password) < 8 or len(confirm_password) < 8:
            return template('changepassword.tpl', {
                'user': user,
                'error': 'Passwords has to be at least 8 characters long. Please re-enter your new password.'
            })
        if (new_password == confirm_password):
            cur.execute('UPDATE users SET password=(?) WHERE unikey=(?)',
                        (new_password, user['unikey']))
            con.commit()

            return redirect(f"/users/{user['unikey']}")
        else:
            return template('changepassword.tpl', {
                'user': user,
                'error': 'Passwords do not match. Please re-enter your new password.'
            })
    else:  # user not logged in
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'error_message': 'You have to login to view this page.'
        })

# -----------------------------------------------------------------------------
# Search Messages
# -----------------------------------------------------------------------------


def search_users(query):
    user = helperMethods.token_user_info()
    if(user['unikey'] != ""):
        if(query is None or query == ""):  # prevents error in front end
            return template('search_users', {
                'user': user,
                'query': query,
                'results': []
            })
        else:
            tuples = cur.execute("""
                SELECT id, unikey, password, first_name, last_name, status
                FROM users WHERE unikey LIKE ? OR first_name LIKE ? OR last_name LIKE ?
                """, ('%' + query + '%', '%' + query + '%', '%' + query + '%')).fetchall()
            con.commit()
            results = []
            for tuple in tuples:
                results.append(helperMethods.user_to_dict(tuple))
            return template('search_users', {
                'user': user,
                'query': query,
                'results': results
            })
    else:  # user not logged in
        return template('error.tpl', {
            'user': user,
            'title': 'Error: Unable to access page',
            'error_message': 'You have to login to search for user details.'
        })
