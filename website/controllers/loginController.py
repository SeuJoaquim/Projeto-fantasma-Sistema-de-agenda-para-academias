import datetime
import jwt
from functools import wraps

from website                                    import key
from website.database.models.personModels       import User
from website.controllers.userDatabaseController import user_by_email

from werkzeug.security import check_password_hash
from flask import jsonify, request

class LoginController():
    def execute(self, auth):
        if not auth or not auth.username or not auth.password:
            return jsonify({'message': 'could not verify1', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
        
        user = user_by_email(auth.username)
        if not user:
            return jsonify({'message': 'user not found', 'data': []}), 401

        if user and check_password_hash(user.password, auth.password):
            token = jwt.encode({'email': user.email, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) },
                            key,algorithm="HS256")
            return jsonify({'message': 'Validated successfully', 'token': token,
                            'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

        return jsonify({'message': 'could not verify2', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return jsonify({'message': 'token is missing', 'data': []}), 401
        try:
            data            = jwt.decode(token, key, algorithms=["HS256"])
            current_user    = user_by_email(email=data['email'])
        except:
            return jsonify({'message': 'token is invalid or expired', 'data': []}), 401
        return f(current_user, *args, **kwargs)
    return decorated