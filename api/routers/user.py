from flask import Blueprint,request, redirect,url_for, jsonify, make_response

from api.controllers.authorizationMethods       import token_required
from api.controllers.tables.personController    import UserController

user = Blueprint("user", __name__)
userController = UserController()


@user.route("/getAll")
def getAll():
    return jsonify(userController.get_All())

@user.route("/getOne")
def getOne():
    userId = request.args.get("userId")
    data, code = userController.get_query_by_id(userId)
    return jsonify(data) , code


@user.route("/post",methods=["POST"])
def post():
    if request.method =="POST":
        email           = request.args.get("email")
        name            = request.args.get("name")
        password        = request.args.get("password")
        resp, code      = userController.post(email=email, name=name, password1=password,password2=password)

        return jsonify(resp), code
    
    return 404

@user.route("/update",methods=["POST"])
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

@user.route("/delete",methods=["POST"]) 
def delete():
    if request.method =="POST":
        id              = request.args.get("id")
        resp, code      = userController.delete(id)

        return jsonify(resp), code
    
    return 404

@user.route("/getClasses",methods=["GET"]) 
def getClasses():
    if request.method =="GET":
        id              = request.args.get("id")
        resp, code      = userController.get_classes_from_user_by_id(id)

        return jsonify(resp), code
    
    return 404