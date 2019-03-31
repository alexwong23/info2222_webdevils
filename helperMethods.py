def userToDict(tuple):
    if(tuple is None):
        return None
    dict = {
        'unikey': tuple[0],
        'password': tuple[1],
        'name': tuple[2],
        'is_admin': tuple[3]
    }
    return dict

def validateForm(form, required):
    messages = []
    for field in required:
        value = form.get(field)
        if value is "" or value is None:
            messages.append(("You must enter a value for %s in the form" % field))
    return messages
