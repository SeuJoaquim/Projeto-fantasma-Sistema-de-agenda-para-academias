from flask import Blueprint,request, redirect,url_for, jsonify, make_response

from api.controllers.authorizationMethods       import token_required
from api.controllers.tables.personController    import ProfessorController
from api.routers.mainRouter                     import MainRouter

professor = Blueprint("professor", __name__)

router = MainRouter(ProfessorController)
@professor.route("/getAll")
def all():
    return router.getAll()


@professor.route("/getOne")
def one():
    id = request.args.get("id")
    return router.getOne(id)


@professor.route("/post",methods=["POST"])
def post():
    if request.method =="POST":
        email       = request.args.get("email")
        name        = request.args.get("name")
        photo       = request.args.get("photo")
        password1   = request.args.get("password1")
        password2   = request.args.get("password2")
        graduation  = request.args.get("graduation")
        telefoneNumber   = request.args.get("telefoneNumber")

        resp, code  = router.post(email=email,name=name, password1=password1,password2=password2,graduation=graduation,telefoneNumber=telefoneNumber,photo=photo)
        return jsonify(resp), code

    return 404

@professor.route("/update",methods=["POST"])
def update():
    if request.method =="POST":
        id          = request.args.get("id")
        email       = request.args.get("email")
        name        = request.args.get("name")
        photo       = request.args.get("photo")
        password1   = request.args.get("password1")
        password2   = request.args.get("password2")
        graduation  = request.args.get("graduation")
        telefoneNumber   = request.args.get("telefoneNumber")
        
        resp, code  = router.update(email=email,name=name, password1=password1,password2=password2,graduation=graduation,telefoneNumber=telefoneNumber,photo=photo)
        return jsonify(resp), code

    return 404

@professor.route("/delete",methods=["POST"]) 
def delete():
    if request.method =="POST":
        id          = request.args.get("id")
        resp, code  = router.delete(id)
        return jsonify(resp), code

    return 404

@professor.route("/getClasses",methods=["GET"]) 
def getClasses():
    if request.method =="GET":
        id              = request.args.get("id")
        resp, code      = router.getClasses(id)
        return jsonify(resp), code
    
    return 404