from flask import Blueprint, render_template, redirect, request, jsonify, url_for
from .controllers.validationController  import ValidationController
from .controllers.loginController import LoginController


auth = Blueprint("auth", __name__)


# Authentication Services
@auth.route("/signUp", methods=["POST"])
def signUp():
    if request.method =="POST":
        email       = request.form.get("email")
        firstName   = request.form.get("firstName")
        password1   = request.form.get("password1")
        password2   = request.form.get("password2")
        
        validationController        = ValidationController(email,firstName,password1,password2) 
        resp, code                  = validationController.execute()

        
        return jsonify(resp), code


@auth.route("/login", methods=["POST"])
def login():
    if request.method =="POST":
        auth                    = request.authorization
        loginController         = LoginController()
        return loginController.execute(auth)
        
        

