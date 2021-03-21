from website.database.models.userModel          import User
from website.controllers.validationController   import ValidationController
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
from website import db

def user_by_email(email):
    try:
        return User.query.filter_by(email=email).first()
    except:
        return None

def get_json(dict):
    data = {}
    data["id"]          = dict.id
    data["email"]       = dict.email
    data["first_name"]  = dict.first_name
    return data


def get_Users(name=""):
    data = {}
    if name:
        users = User.query.filter(User.name.like(f'%{name}%')).all()
    else:
        users = User.query.all()
    if users:
        result = []
        for u in users:
            result.append(get_json(u))

        data["message"] = "successfully fetched"
        data["data"]    = result
        return data

    data["message"] = "nothing found"
    data["data"]    = {}
    return data


"""Retorna usuário específico pelo ID no parametro da request"""

def get_user_by_id(id):
    user = User.query.get(id)
    data = {}
    if user:
        result = get_json(user)
        data["message"] = "successfully fetched"
        data["data"]    = result
        return data, 201

    data["message"] = "user don't exist"
    data["data"]    = {}
    return data, 404


"""Cadastro de usuários com validação de existência"""
def post_user(email,first_name,password):
    validationController    = ValidationController(email,first_name,password,password) 
    resp, code              = validationController.execute()

    return resp, code


"""Atualiza usuário baseado no ID, caso o mesmo exista."""


def update_user(id, email, first_name, password ):
    data = {}
    user = User.query.get(id)

    if not user:
        data["message"] = "user don't exist"
        data["data"]    = {}
        return data, 404

    pass_hash = generate_password_hash(password)

    if user:
        try:
            user.password   = pass_hash
            user.first_name = first_name
            user.email      = email
            db.session.commit()
            result          = get_json(user)
            
            data["message"] = "successfully updated"
            data["data"]    = result
            return data, 201
        except:
            data["message"] = "unable to update"
            data["data"]    = {}
            return data, 500


"""Deleta usuário com base no ID da request"""


def delete_user(id):
    data = {}
    user = User.query.get(id)
    if not user:
        data["message"] = "user don't exist"
        data["data"]    = {}
        return data, 404

    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            result = get_json(user)
            data["message"] = "successfully deleted"
            data["data"]    = result
            return data, 200
        except:
            data["message"] = "unable to delete"
            data["data"]    = {}
            return data, 500

