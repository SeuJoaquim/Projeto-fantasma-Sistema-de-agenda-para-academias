from flask import Blueprint, render_template, redirect, request, jsonify
from .controllers.validationController import ValidationController
from .controllers.confirmacaoController import ConfirmnController

auth = Blueprint("auth", __name__)

# Acess Routes
@auth.route("/login")
def login():
    return render_template("auth/login.html")

@auth.route("/logout")
def logout():
    return {}

@auth.route("/signUp")
def signUp():
    return render_template("auth/signUp.html")


# Authentication Services
@auth.route("/validacao", methods=["POST"])
def validacao():
    if request.method =="POST":
        email       = request.form.get("email")
        firstName   = request.form.get("firstName")
        password1   = request.form.get("password1")
        password2   = request.form.get("password2")
        
        validationController    = ValidationController(email,firstName,password1,password2) 
        resp                    = validationController.execute()

        
        return jsonify(resp)


@auth.route("/confirmacao", methods=["POST"])
def confirmacao():
    if request.method =="POST":
        data = {}
        email       = request.form.get("email")
        password    = request.form.get("password")

        confirmacaoController   = ConfirmnController(email,password)
        resp                    = confirmacaoController.execute()
        
        return jsonify(resp)

