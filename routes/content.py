from bottle import template, request, redirect, response
from datetime import datetime

import string, random, helperMethods
'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''

# remove this and put it in sql file handler
con = helperMethods.con
cur = con.cursor()
COOKIE_SECRET_KEY = helperMethods.COOKIE_SECRET_KEY  # prevent cookie manipulation

#-----------------------------------------------------------------------------
# Content
#-----------------------------------------------------------------------------


def show_content(section,page1):

    user = helperMethods.token_user_info()

    int = None

    # if (page1 == 'Basic HTML'):
    #     int = 1
    # elif(page1 == 'Formatting'):
    #     int = 2
    # elif(page1 == 'Forms and Input'):
    #     int = 3
    # elif(page1 == 'Properties'):
    #     int = 4
    # elif(page1 == 'Selectors'):
    #     int = 5
    # elif(page1 == 'Functions'):
    #     int = 6
    page1 = page1.replace("-", " ")


    cur.execute('SELECT title,description,category_type FROM all_content WHERE name = (?)',(page1,))
    con.commit()

    information = helperMethods.usersList(cur.fetchall())

    return template('content.tpl',{'user':user,'content':information})
