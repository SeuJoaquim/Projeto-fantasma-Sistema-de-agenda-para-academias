from flask import Blueprint,request, render_template,make_response, redirect,url_for, jsonify, make_response
from .controllers.loginController import token_required

router = Blueprint("router", __name__)

@router.route("/", methods=["GET"])
def home():
    return render_template("home.html")

# Authentication Routes
@router.route("/login")
def login():
    return render_template("/login.html")

@router.route("/logout")
def logout():
    resp = make_response(redirect(url_for("router.login")))
    resp.set_cookie("token","", expires=0)
    return resp

@router.route("/signUp")
def signUp():
    return render_template("signUp.html")


# App Routes
@router.route("/app")
@token_required
def app(current_user):
    return render_template("/app/index.html")

@router.route("/app/user")
@token_required
def user(current_user):
    data = {}
    data["email"] = current_user.email
    data["first_name"] = current_user.first_name
    return jsonify(data)
