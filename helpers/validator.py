# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import request, Response, g
from functools import wraps
from helpers.response_builder import resp


def client_checker(no_auth=False, role='', features=''):
    """used for JWT authentification
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.headers.get('token', None)
            get_json = request.get_json(force=True, silent=True)
            if get_json:
                request_params = get_json
            else:
                request_params = request.form

            if token is None:

                if no_auth:
                    return f(request_params=request_params, *args, **kwargs)
                else:
                    return resp(400)

            

            return f(
                request_params=request_params,
                *args,
                **kwargs)

        return decorated_function
    return decorator
