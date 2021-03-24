from flask import Blueprint,request, redirect,url_for, jsonify, make_response

from api.controllers.authorizationMethods       import token_required
from api.controllers.tables.modalityController  import ModalityController
from api.routers.mainRouter                     import MainRouter


modality = Blueprint("modality", __name__)


router = MainRouter(ModalityController)
controller = ModalityController()

@modality.route("/getAll")
def all():
    return router.getAll()


@modality.route("/getOne")
def one():
    id = request.args.get("id")
    return router.getOne(id)


@modality.route("/post",methods=["POST"])
def post():
    if request.method =="POST":
        name            = request.args.get("name")
        resp, code      = controller.post(name)
        return jsonify(resp), code

    return 404

@modality.route("/update",methods=["POST"])
def update():
    if request.method =="POST":
        id          = request.args.get("id")
        name            = request.args.get("name")
        
        resp, code  = controller.post(id,name)
        return jsonify(resp), code

    return 404

@modality.route("/delete",methods=["POST"]) 
def delete():
    if request.method =="POST":
        id          = request.args.get("id")
        resp, code  = router.delete(id)
        return jsonify(resp), code

    return 404

@modality.route("/getClasses")
def one():
    id = request.args.get("id")
    resp, code  = controller.get_classes_from_modality_by_id(id)
    return jsonify(resp), code 
