from bottle import route, get, post, request, redirect, static_file

import routes.index as index
import routes.users as users
import routes.messages as messages
import routes.admin as admin

from bottle import response #do we need this?

#-----------------------------------------------------------------------------
'''
    This file will handle our typical Bottle requests and responses
    You should not have anything beyond basic page loads, handling forms and
    maybe some simple program logic
'''

#-----------------------------------------------------------------------------
# Static file paths
#-----------------------------------------------------------------------------

@route('/public/<file:path>')
def serve_css(file):
    return static_file(file, root='public/')

#-----------------------------------------------------------------------------
# Index
#-----------------------------------------------------------------------------

@get('/')
@get('/home')
def get_index():
    return index.index_page()

@get('/signup')
def get_signup():
    return index.signup_page()

@post('/signup')
def post_signup():
    signup_unikey = request.forms.get('signup_unikey')
    signup_first_name = request.forms.get('signup_first_name')
    signup_last_name = request.forms.get('signup_last_name')
    signup_password = request.forms.get('signup_password')
    signup_confirm_password = request.forms.get('signup_confirm_password')
    return index.signup_check(signup_unikey, signup_first_name, signup_last_name, signup_password, signup_confirm_password)

@get('/login')
def get_login_controller():
    return index.login_page()

@post('/login')
def post_login():
    unikey = request.forms.get('unikey')
    password = request.forms.get('password')
    return index.login_check(unikey, password)

@get('/logout')
def get_logout_controller():
    return index.logout_check()

@get('/about')
def get_about():
    return index.about_page()

@get('/contact')
def get_contact():
    return index.contact_page()

#-----------------------------------------------------------------------------
# Users
#-----------------------------------------------------------------------------

@get('/users')
def redirect_profile():
    return users.redirect_profile_page()

@get('/users/<unikey>')
def get_profile(unikey):
    return users.profile_page(unikey)

@get('/users/<unikey>/edit')
def get_edit_profile(unikey):
    return users.edit_profile_page(unikey)

@post('/users/editprofile')
def post_edit_profile():
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    return users.edit_profile_check(first_name, last_name)

@get('/users/<unikey>/changepassword')
def get_change_password(unikey):
    return users.change_password_page(unikey)

@post('/users/changepassword')
def post_edit_profile():
    new_password = request.forms.get('new_password')
    confirm_password = request.forms.get('confirm_password')
    return users.change_password_check(new_password, confirm_password)

#-----------------------------------------------------------------------------
# Messages
#-----------------------------------------------------------------------------

@get('/messages')
def get_all_messages():
    return messages.all_messages_page()

@get('/messages/<receiver>')
def get_receiver_messages(receiver):
    return messages.messages_page(receiver)

@post('/messages/<receiver>/send')
def post_messages(receiver):
    text_Message = request.forms.get('textSend')
    return messages.messages_check(receiver, text_Message)

#-----------------------------------------------------------------------------
# Messages
#-----------------------------------------------------------------------------

@get('/admin')
def get_admin():
    return admin.admin_page()


#-----------------------------------------------------------------------------
# Error
#-----------------------------------------------------------------------------

@get('/<url:path>')
def error(url):
    return index.error_page(url)
