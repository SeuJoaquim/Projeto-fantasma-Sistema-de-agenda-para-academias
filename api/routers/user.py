from flask import Blueprint,request, redirect,url_for, jsonify, make_response

from api.controllers.authorizationMethods       import token_required
from api.controllers.tables.personController    import UserController
from api.routers.mainRouter                     import MainRouter

user = Blueprint("user", __name__)

router = MainRouter(UserController)
@user.route("/getAll")
def all():
    return router.getAll()


@user.route("/getOne")
def one():
    userId = request.args.get("userId")
    return router.getOne(userId)


@user.route("/post",methods=["POST"])
def post():
    if request.method =="POST":
        email       = request.args.get("email")
        name        = request.args.get("name")
        password1   = request.args.get("password1")
        password2   = request.args.get("password2")

        resp, code  = router.post(email=email,name=name,password1=password1,password2=password2)
        return jsonify(resp), code

    return 404

@user.route("/update",methods=["POST"])
def update():
    if request.method =="POST":
        id          = request.args.get("id")
        email       = request.args.get("email")
        name        = request.args.get("name")
        password1   = request.args.get("password1")
        password2   = request.args.get("password2")
        resp, code  = router.update(email=email,name=name,password1=password1,password2=password2)
        return jsonify(resp), code

    return 404

@user.route("/delete",methods=["POST"]) 
def delete():
    if request.method =="POST":
        id          = request.args.get("id")
        resp, code  = router.delete(id)
        return jsonify(resp), code

    return 404

@user.route("/getClasses",methods=["GET"]) 
def getClasses():
    if request.method =="GET":
        id              = request.args.get("id")
        resp, code      = router.getClasses(id)
        return jsonify(resp), code
    
    return 404