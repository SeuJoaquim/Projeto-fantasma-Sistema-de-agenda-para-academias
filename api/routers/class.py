from flask import Blueprint,request, redirect,url_for, jsonify, make_response

from api.controllers.authorizationMethods       import token_required
from api.controllers.tables.classController     import ClassController
from api.routers.mainRouter                     import MainRouter


classe = Blueprint("classe", __name__)


router = MainRouter(ClassController)
controller = ClassController()

@classe.route("/getAll")
def all():
    return router.getAll()


@classe.route("/getOne")
def one():
    id = request.args.get("id")
    return router.getOne(id)


@classe.route("/post",methods=["POST"])
def post():
    if request.method =="POST":
        date            = request.args.get("date")
        name            = request.args.get("name")
        maxNumber       = request.args.get("maxNumber")
        minNumber       = request.args.get("minNumber")
        professor_id    = request.args.get("professor_id")
        modality_id     = request.args.get("modality_id")


        resp, code  = controller.post(name, date, maxNumber, minNumber, professor_id, modality_id)
        return jsonify(resp), code

    return 404

@classe.route("/update",methods=["POST"])
def update():
    if request.method =="POST":
        id          = request.args.get("id")
        date            = request.args.get("date")
        name            = request.args.get("name")
        maxNumber       = request.args.get("maxNumber")
        minNumber       = request.args.get("minNumber")
        professor_id    = request.args.get("professor_id")
        modality_id     = request.args.get("modality_id")
        
        resp, code  = controller.post(id,name, date, maxNumber, minNumber, professor_id, modality_id)
        return jsonify(resp), code

    return 404

@classe.route("/delete",methods=["POST"]) 
def delete():
    if request.method =="POST":
        id          = request.args.get("id")
        resp, code  = router.delete(id)
        return jsonify(resp), code

    return 404

@classe.route("/insert",methods=["POST"]) 
def insert():
    if request.method =="POST":
        user_id     = request.args.get("user_id")
        class_id    = request.args.get("class_id")
        
        resp, code      = controller.insert_user_in_class(user_id,class_id)
        return jsonify(resp), code
    
    return 404


@classe.route("/getUsers")
def one():
    id = request.args.get("id")
    resp, code  = controller.get_users_in_classe_by_id(id)
    return jsonify(resp), code 

@classe.route("/getProfessors")
def one():
    id = request.args.get("id")
    resp, code  = controller.get_professor_in_classe_by_id(id)
    return jsonify(resp), code