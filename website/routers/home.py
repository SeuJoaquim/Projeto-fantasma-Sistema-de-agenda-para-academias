from flask import Blueprint,request, render_template,make_response, redirect,url_for, jsonify, make_response

from api.controllers.authorizationMethods           import token_required
from api.controllers.tables.personController import UserController

from api.database.models.personModels       import User, Admin, Professor
from api.database.models.classModels        import Modality, Class
from api.database.models.relationshipModels import UserClassRelationship


home = Blueprint("home", __name__)

@home.route("/", methods=["GET"])
def main_home():
    return render_template("home.html")

# Authentication Routes
@home.route("/login")
def login():
    return render_template("/login.html")

@home.route("/logout")
def logout():
    resp = make_response(redirect(url_for("home.login")))
    resp.set_cookie("token","", expires=0)
    return resp

@home.route("/signUp")
def signUp():
    return render_template("signUp.html")









# @home.route("/teste", methods=["GET"])
# def loco():
#     from website.database.teste import execute, e
#     execute()
#     # e()
#     return "a"