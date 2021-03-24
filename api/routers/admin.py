from flask import Blueprint,request, redirect,url_for, jsonify, make_response

from api.controllers.authorizationMethods       import token_required
from api.controllers.tables.personController    import UserController, AdminController


class mainRouter():
    def __init__(self, controller=UserController):
        self.controller = controller()

    def getAll(self):
        return jsonify(self.controller.get_All())
    
    def getOne(self,id):
        data, code = self.controller.get_query_by_id(id)
        return jsonify(data) , code

    def post(self, **kwargs):

        email           = kwargs.get("email")
        name            = kwargs.get("name")
        photo           = kwargs.get("photo")
        password1       = kwargs.get("password1")
        password2       = kwargs.get("password2")
        graduation      = kwargs.get("graduation")
        telefoneNumber  = kwargs.get("telefoneNumber")
        

        if (self.controller.__class__.__name__) == "UserController":
            resp, code        = self.controller.post(email,name,password1)
            return jsonify(resp), code



    
admin = Blueprint("admin", __name__)

router = mainRouter(AdminController)
@admin.route("/getAll")
def all():
    return router.getAll()


@admin.route("/getOne")
def one():
    adminId = request.args.get("adminId")
    return router.getOne(adminId)


    # @admin.route("/post",methods=["POST"])
    # def post():
    #     if request.method =="POST":
    #         email           = request.args.get("email")
    #         name            = request.args.get("name")
    #         password        = request.args.get("password")
    #         resp, code      = self.controller.post(email,name,password)

    #         return jsonify(resp), code
        
    #     return 404

    # @admin.route("/update",methods=["POST"])
    # def update():
    #     if request.method =="POST":
    #         id              = request.args.get("id")
    #         email           = request.args.get("email")
    #         name            = request.args.get("name")
    #         password1        = request.args.get("password1")
    #         password2        = request.args.get("password2")
    #         resp, code      = self.controller.update(id,email,name,password1,password2)

    #         return jsonify(resp), code
        
    #     return 404

    # @admin.route("/delete",methods=["POST"]) 
    # def delete():
    #     if request.method =="POST":
    #         id              = request.args.get("id")
    #         resp, code      = self.controller.delete(id)

    #         return jsonify(resp), code
        
    #     return 404

    # @admin.route("/getClasses",methods=["GET"]) 
    # def getClasses():
    #     if request.method =="GET":
    #         id              = request.args.get("id")
    #         resp, code      = self.controller.get_classes_from_admin_by_id(id)

    #         return jsonify(resp), code
        
    #     return 404