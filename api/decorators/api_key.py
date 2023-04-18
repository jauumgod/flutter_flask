from functools import wraps
from flask import request, abort



def require_api_key(view_function):
    @wraps(view_function)
    def decorate_function(*args, **kwargs):
        if request.headers.get('x-api-key') == "chave-api-key":
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorate_function