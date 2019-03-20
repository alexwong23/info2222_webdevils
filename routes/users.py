from bottle import template, Bottle, redirect

usersRouter = Bottle()

# simulates user is logged in
user = {
    'name': 'alex',
    'id': 470066919
}

@usersRouter.route('/<id>')
def userProfile(id):
    info = {
        'user': user
    }
    if(id == user['id']):
        return template('userProfile.tpl', info)
    else:
        return redirect('/')
