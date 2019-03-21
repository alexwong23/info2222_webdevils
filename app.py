# http://localhost:8080/
# http://pwp.stevecassidy.net/bottle/forms-processing.html
# https://bottle.readthedocs.io/en/latest/tutorial_app.html

from bottle import run, template, debug, Bottle, redirect, response, request
from routes.index import indexRouter
from routes.users import usersRouter
import sqlite3

COOKIE_SECRET_KEY = "some-secret" # prevent cookie manipulation

# create database
con = sqlite3.connect('./db/webdevils.db')
cur = con.cursor()
# con.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, unikey char(8) NOT NULL, password char(20) NOT NULL, is_admin bool NOT NULL, name char(100) NOT NULL, date_created char(20) NOT NULL)")
# con.execute("INSERT INTO users (unikey, password, name, is_admin, date_created) VALUES ('admin001', 'admin001', 'admin', 1, datetime('now', 'localtime'))")
# con.execute("INSERT INTO users (unikey, password, name, is_admin, date_created) VALUES ('test0001', 'test0001', 'test 1', 0, datetime('now', 'localtime'))")
# con.execute("INSERT INTO users (unikey, password, name, is_admin, date_created) VALUES ('test0002', 'test0002', 'test 2', 0, datetime('now', 'localtime'))")
# con.execute("INSERT INTO users (unikey, password, name, is_admin, date_created) VALUES ('test0003', 'test0003', 'test 3', 0, datetime('now', 'localtime'))")
# con.commit()

app = Bottle()
app.merge(indexRouter)
app.mount('/users', usersRouter)

@app.route('/<url:path>')
def error(url):
    info = {
        'title': 'Error: 404 Not Found',
        'message': 'We could not find the requested URL: ' + url
    }
    return template('error.tpl', info)

# run only if using this file directly
if __name__ == '__main__':
    debug(True) # full stacktrace of python interpreter
    app.run(host='localhost', port=8080, reloader=True)
    # debug and reloader ONLY for dev env, not production env
