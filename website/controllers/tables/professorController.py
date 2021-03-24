from website.database.models.personModels           import Professor
from website.database.models.classModels            import Class
from website.controllers.tables.userController      import UserController
from website.controllers.validationController       import ValidationController
from werkzeug.security import generate_password_hash, check_password_hash
from website import db

class ProfessorController(UserController):
    def __init__(self, object=Professor):
        super().__init__(object)

    """ Retorna objeto dicionário com informações específicas  """
    def get_json(self,dict):
        data = {}
        data["id"]              = dict.id
        data["email"]           = dict.email
        data["name"]            = dict.name
        data["graduation"]      = dict.graduation
        data["telefoneNumber"]  = dict.telefoneNumber
        data["photo"]           = dict.photo
        return data

    """Cadastro de usuários com validação de existência"""
    def post(self,email,name,password1,password2,graduation,telefoneNumber,photo):
        data = {}
        validationController    = ValidationController(object=self.object) 
        validation, resp        = validationController.execute(email,name,password1,password2)

        if validation:
            email       = resp["data"][0]
            name        = resp["data"][1]
            password    = resp["data"][2]

            new_user = self.object(email=email,name=name, password=generate_password_hash(password,method="sha256"),graduation=graduation,telefoneNumber=telefoneNumber,photo=photo)
            db.session.add(new_user)
            db.session.commit()

            data["message"] = resp["messages"]
            data["data"]    = self.get_json(new_user)

            return resp["messages"], 200


        return data, 401

    """Retorna todas as classes de um professor específico."""
    def get_classes_from_professor_by_id(self, id):
        data = {}

        def classe_get_json(dict):
            data = {}
            data["name"]            = dict.name
            data["date"]            = dict.date
            data["maxNumber"]       = dict.maxNumber
            data["minNumber"]       = dict.minNumber
            data["professor_id"]    = dict.professor_id
            data["modality_id"]     = dict.modality_id
            return data

        try:
            classes       = Class.query.filter_by(professor_id=id).all()
            if classes:
                classList     = []
                for clas in classes:
                    classList.append(classe_get_json(clas))
    
                data["message"] = "successfully fetched!"
                data["data"]    = classList
                return data, 200
            else:
                data["message"] = "Given id does not correspond to any class id"
                data["data"]    = {}
                return data, 401
        
        except:
            data["message"] = "Error, could not query"
            data["data"]    = {}
            return data, 401

    """Retorna todas as classes de um usuário específico."""
    def get_classes_from_user_by_id(self,id):
        return self.get_classes_from_professor_by_id(id)

