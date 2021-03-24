from flask import Blueprint, render_template, redirect, request, jsonify, url_for
from website.controllers.validationController       import ValidationController
from website.controllers.loginController            import LoginController
from website.controllers.tables.userController      import UserController


userController          = UserController()
validationController    = ValidationController()

auth = Blueprint("auth", __name__)

# Authentication Services
@auth.route("/signUp", methods=["POST"])
def signUp():
    if request.method =="POST":
        email       = request.form.get("email")
        name        = request.form.get("name")
        password1   = request.form.get("password1")
        password2   = request.form.get("password2")
        
        resp, code  = userController.post(email,name,password1,password2)
        return jsonify(resp), code


@auth.route("/login", methods=["POST"])
def login():
    if request.method =="POST":
        auth                    = request.authorization
        loginController         = LoginController()
        return loginController.execute(auth)
        
        

