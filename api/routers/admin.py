from flask import Blueprint,request, redirect,url_for, jsonify, make_response

from api.controllers.authorizationMethods       import token_required
from api.controllers.tables.personController    import UserController, AdminController
from api.routers.mainRouter                     import MainRouter
   
admin = Blueprint("api_admin", __name__)

router = MainRouter(AdminController)
@admin.route("/getAll")
def all():
    return router.getAll()


@admin.route("/getOne")
def one():
    adminId = request.args.get("adminId")
    return router.getOne(adminId)


@admin.route("/post",methods=["POST"])
def post():
    if request.method =="POST":
        email       = request.args.get("email")
        name        = request.args.get("name")
        password1   = request.args.get("password1")
        password2   = request.args.get("password2")

        resp, code  = router.post(email=email,name=name,password1=password1,password2=password2)
        return jsonify(resp), code

    return 404

@admin.route("/update",methods=["POST"])
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

@admin.route("/delete",methods=["POST"]) 
def delete():
    if request.method =="POST":
        id          = request.args.get("id")
        resp, code  = router.delete(id)
        return jsonify(resp), code

    return 404

    # @admin.route("/getClasses",methods=["GET"]) 
    # def getClasses():
    #     if request.method =="GET":
    #         id              = request.args.get("id")
    #         resp, code      = self.controller.get_classes_from_admin_by_id(id)

    #         return jsonify(resp), code
        
    #     return 404