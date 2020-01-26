from flask import request, jsonify
import functools

users = {"Booker": "password",
         "Annabel": "password",
         "Steve": "password",
         "Tawny": "password",
         "Kasha": "password",
         "Tameika": "password",
         "Marie": "password",
         "Samual": "password",
         "Cyrus": "password",
         "Joya": "password"}


def ok_user_and_password(username, password):
    """Test whether the supplied username and password match."""
    return users.get(username) == password


def authenticate():
    """ Return a response indicating a failure to authenticate."""
    message = {'message': "Authenticate."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Main"'

    return resp


def requires_authorization(f):
    """A python decorator which requires HTTP basic authentication."""

    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not ok_user_and_password(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated
