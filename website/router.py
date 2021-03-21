from flask import Blueprint,request, render_template,make_response, redirect,url_for, jsonify, make_response
from .controllers.loginController import token_required
from .controllers.userDatabaseController import *

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



# User Database Routes
@router.route("/user")
@token_required
def user(current_user):
    data = {}
    data["email"] = current_user.email
    data["first_name"] = current_user.first_name
    return jsonify(data)


@router.route("/user/getAll")
def getAll():
    return jsonify(get_Users())

@router.route("/user/getOne")
def getOne():
    userId = request.args.get("userId")
    data, code = get_user_by_id(userId)
    return jsonify(data) , code


@router.route("/user/post",methods=["POST"])
def post():
    if request.method =="POST":
        email           = request.args.get("email")
        first_name      = request.args.get("first_name")
        password        = request.args.get("password")
        resp, code      = post_user(email,first_name,password)

        return jsonify(resp), code
    
    return 404

@router.route("/user/update",methods=["POST"])
def update():
    if request.method =="POST":
        id              = request.args.get("id")
        email           = request.args.get("email")
        first_name      = request.args.get("first_name")
        password        = request.args.get("password")
        resp, code      = update_user(id,email,first_name,password)

        return jsonify(resp), code
    
    return 404

@router.route("/user/delete",methods=["POST"])
def delete():
    if request.method =="POST":
        id              = request.args.get("id")
        email           = request.args.get("email")
        first_name      = request.args.get("first_name")
        password        = request.args.get("password")
        resp, code      = delete_user(id)

        return jsonify(resp), code
    
    return 404
