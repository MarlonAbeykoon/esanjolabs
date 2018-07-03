import jwt
from flask import request, current_app
from functools import wraps


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # try:
            jwt_token = request.headers.get('Authorization')
            secret_key = current_app.config.get('SECRET_KEY')

            try:
                jwt.decode(jwt_token, secret_key)
            except jwt.ExpiredSignatureError:
                print('Your token has expired!')
                # Handle the exception here by raising with a meaningful error
            return f(*args, **kwargs)
    return decorated

