# http://localhost:8080/
# http://pwp.stevecassidy.net/bottle/forms-processing.html
# https://bottle.readthedocs.io/en/latest/tutorial_app.html

from bottle import run, template, debug, Bottle
from routes.users import usersRouter
import sqlite3

# create database
# con = sqlite3.connect('./db/webdevils.db')
# con.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, unikey char(8) NOT NULL, password char(20) NOT NULL, is_admin bool NOT NULL, name char(100) NOT NULL, date_created char(20) NOT NULL)")
# con.execute("INSERT INTO users (unikey, password, name, is_admin, date_created) VALUES ('admin001', 'admin001', 'admin', 1, datetime('now', 'localtime'))")
# con.execute("INSERT INTO users (unikey, password, name, is_admin, date_created) VALUES ('test0001', 'test0001', 'test 1', 0, datetime('now', 'localtime'))")
# con.execute("INSERT INTO users (unikey, password, name, is_admin, date_created) VALUES ('test0002', 'test0002', 'test 2', 0, datetime('now', 'localtime'))")
# con.execute("INSERT INTO users (unikey, password, name, is_admin, date_created) VALUES ('test0003', 'test0003', 'test 3', 0, datetime('now', 'localtime'))")
# con.commit()

# simulates user is logged in
user = {
    'name': 'alex',
    'id': 470066919
}

mainRoute = Bottle()

@mainRoute.route('/')
def homepage():
    info = {
        'user': user,
        'title': 'Home Page',
        'content': 'Hello World'
    }
    return template('home.tpl', info) # unsafe from malicious content

@mainRoute.route('/contactus')
def contactus():
    info = {
        'user': user
    }
    return template('contactus.tpl', info)

@mainRoute.route('/login')
def homepage():
    info = {
        'user': user
    }
    return template('home.tpl', info) # unsafe from malicious content


@mainRoute.route('/<url>')
def error(url):
    info = {
        'user': user,
        'url': url
    }
    return template('error.tpl', info)

mainRoute.mount('/users', usersRouter)
debug(True) # full stacktrace of python interpreter
mainRoute.run(host='localhost', port=8080, reloader=True)
# debug and reloader ONLY for dev env, not production env
