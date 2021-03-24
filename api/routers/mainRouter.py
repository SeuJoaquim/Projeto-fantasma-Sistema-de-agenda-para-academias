from flask import jsonify

class MainRouter():
    def __init__(self, controller):
        self.controller = controller()

    def getAll(self):
        return self.controller.get_All()
    
    def getOne(self,id):
        return self.controller.get_query_by_id(id)
        

    def post(self, **kwargs):
        email           = kwargs.get("email")
        name            = kwargs.get("name")
        photo           = kwargs.get("photo")
        password1       = kwargs.get("password1")
        password2       = kwargs.get("password2")
        graduation      = kwargs.get("graduation")
        telefoneNumber  = kwargs.get("telefoneNumber")
        return self.controller.post(email=email,name=name, password1=password1,password2=password2,graduation=graduation,telefoneNumber=telefoneNumber,photo=photo)
    
    def update(self, **kwargs):
        email           = kwargs.get("email")
        name            = kwargs.get("name")
        photo           = kwargs.get("photo")
        password1       = kwargs.get("password1")
        password2       = kwargs.get("password2")
        graduation      = kwargs.get("graduation")
        telefoneNumber  = kwargs.get("telefoneNumber")
        return self.controller.update(email=email,name=name, password1=password1,password2=password2,graduation=graduation,telefoneNumber=telefoneNumber,photo=photo)
         
    def delete(self,id):
        return self.controller.delete(id)

    def getClasses(self,id):
        return self.controller.get_classes_from_user_by_id(id)
