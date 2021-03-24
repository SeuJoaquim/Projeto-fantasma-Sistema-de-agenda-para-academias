import datetime
import jwt
from functools import wraps

from api.database.models.personModels           import User, Admin
from api.controllers.tables.personController      import UserController

from werkzeug.security import check_password_hash
from flask import jsonify, request
from website import key

class LoginController():
    def execute(self, auth):
        if not auth or not auth.username or not auth.password:
            return jsonify({'message': 'could not verify1', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
        
        user = User.query.filter_by(email=auth.username).first()
        if not user:
            return jsonify({'message': 'user not found', 'data': []}), 401

        if user and check_password_hash(user.password, auth.password):
            token = jwt.encode({'email': user.email, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) },
                            key,algorithm="HS256")
            return jsonify({'message': 'Validated successfully', 'token': token,
                            'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

        return jsonify({'message': 'could not verify2', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401


