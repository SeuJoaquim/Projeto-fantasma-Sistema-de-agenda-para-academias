import jwt
from functools import wraps
from api.database.models.personModels      import User, Admin
from website import key
from flask import request

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return {'message': 'token is missing', 'data': []}, 401
        try:
            data            = jwt.decode(token, key, algorithms=["HS256"])
            current_user    = User.query.filter_by(email=data['email']).first()
        except:
            return {'message': 'token is invalid or expired', 'data': []}, 401
        return f(current_user, *args, **kwargs)
    return decorated



def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return {'message': 'token is missing', 'data': []}, 401
        try:
            data            = jwt.decode(token, key, algorithms=["HS256"])
            current_user    = Admin.query.filter_by(email=data['email']).first()
        except:
            return {'message': 'token is invalid or expired', 'data': []}, 401
        return f(current_user, *args, **kwargs)
    return decorated