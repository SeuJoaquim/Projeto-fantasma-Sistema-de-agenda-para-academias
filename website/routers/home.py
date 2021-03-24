from flask import Blueprint,request, render_template,make_response, redirect,url_for, jsonify, make_response

from website.controllers.loginController        import token_required
from website.controllers.tables.userController  import UserController

from website.database.models.personModels       import User, Admin, Professor
from website.database.models.classModels        import Modality, Class
from website.database.models.relationshipModels import UserClassRelationship


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






userController = UserController()

@home.route("/user/getAll")
def getAll():
    return jsonify(userController.get_All())

@home.route("/user/getOne")
def getOne():
    userId = request.args.get("userId")
    data, code = userController.get_query_by_id(userId)
    return jsonify(data) , code


@home.route("/user/post",methods=["POST"])
def post():
    if request.method =="POST":
        email           = request.args.get("email")
        name            = request.args.get("name")
        password        = request.args.get("password")
        resp, code      = userController.post(email,name,password)

        return jsonify(resp), code
    
    return 404

@home.route("/user/update",methods=["POST"])
def update():
    if request.method =="POST":
        id              = request.args.get("id")
        email           = request.args.get("email")
        name            = request.args.get("name")
        password1        = request.args.get("password1")
        password2        = request.args.get("password2")
        resp, code      = userController.update(id,email,name,password1,password2)

        return jsonify(resp), code
    
    return 404

@home.route("/user/delete",methods=["POST"]) 
def delete():
    if request.method =="POST":
        id              = request.args.get("id")
        resp, code      = userController.delete(id)

        return jsonify(resp), code
    
    return 404

@home.route("/user/getClasses",methods=["GET"]) 
def getClasses():
    if request.method =="GET":
        id              = request.args.get("id")
        resp, code      = userController.get_classes_from_user_by_id(id)

        return jsonify(resp), code
    
    return 404


@home.route("/teste", methods=["GET"])
def loco():
    from website.database.teste import execute, e
    execute()
    # e()
    return "a"