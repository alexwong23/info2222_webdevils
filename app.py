# http://localhost:8080/
# http://pwp.stevecassidy.net/bottle/forms-processing.html
# https://bottle.readthedocs.io/en/latest/tutorial_app.html
# https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

from bottle import run, template, debug, Bottle, redirect, response, request
from routes.index import indexRouter
from routes.users import usersRouter

import sqlite3
con = sqlite3.connect('./db/webdevils.db')
cur = con.cursor()
import populate_data # import to generate db

COOKIE_SECRET_KEY = "some-secret" # prevent cookie manipulation
app = Bottle()

# from bottle import static_file, os
# path = os.path.abspath(__file__)
# dir_path = os.path.dirname(path)
# print(dir_path)
app.merge(indexRouter)
# @app.route('/static/<filepath:path>')
# def server_static(filepath):
#     return static_file(filepath, root='/')
app.mount('/users', usersRouter)



@app.route('/<url:path>')
def error(url):
    return template('error.tpl', {
        'title': 'Error: 404 Not Found',
        'message': 'We could not find the requested URL: ' + url
    })

# run only if using this file directly
if __name__ == '__main__':
    debug(True) # full stacktrace of python interpreter
    app.run(host='localhost', port=8080, reloader=True)
    # debug and reloader ONLY for dev env, not production env
