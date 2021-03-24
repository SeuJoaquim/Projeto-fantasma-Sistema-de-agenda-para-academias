from api.database.models.classModels            import Class
from api.database.models.personModels           import User, Admin, Professor
from api.controllers.validationController       import ValidationController
from api.controllers.tables.databaseController  import DatabaseController
from api.database.models.relationshipModels     import UserClassRelationship

from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
from website import db


class UserController(DatabaseController):
    def __init__(self, object=User):
        super().__init__(object)
    
    """ Retorna objeto dicionário com informações específicas  """
    def get_json(self,dict):
        data = {}
        data["id"]          = dict.id
        data["email"]       = dict.email
        data["name"]        = dict.name
        return data

    """Cadastro de usuários com validação de existência"""
    def post(self, **kwargs):
        data = {}
        email           = kwargs.get("email")
        name            = kwargs.get("name")
        photo           = kwargs.get("photo")
        password1       = kwargs.get("password1")
        password2       = kwargs.get("password2")
        graduation      = kwargs.get("graduation")
        telefoneNumber  = kwargs.get("telefoneNumber")
        
        if (self.object.__name__ == "User") or (self.object.__name__ == "Admin"):
            validationController    = ValidationController(object=self.object) 
            validation, resp        = validationController.execute(email,name,password1,password2)
            if validation:
                email       = resp["data"][0]
                name        = resp["data"][1]
                password    = resp["data"][2]

                new_user = self.object(email=email,name=name, password=generate_password_hash(password,method="sha256"))
                db.session.add(new_user)
                db.session.commit()

                data["message"] = resp["messages"]
                data["data"]    = self.get_json(new_user)

                return resp, 200
            return resp, 401
        
        
        elif (self.object.__name__) == "Professor":
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
            return resp, 401

        return {}, 400

        

    """Atualiza usuário baseado no ID, caso o mesmo exista."""
    def update(self,**kwargs):
        data = {}
        id           = kwargs.get("id")
        email           = kwargs.get("email")
        name            = kwargs.get("name")
        photo           = kwargs.get("photo")
        password1       = kwargs.get("password1")
        password2       = kwargs.get("password2")
        graduation      = kwargs.get("graduation")
        telefoneNumber  = kwargs.get("telefoneNumber")

        user = self.get_query_by_id(id)[0]

        if not user:
            if (self.object.__name__ == "User") or (self.object.__name__ == "Admin"):
                return self.post(email=email, name=name, password1=password1,password2=password2)
            elif (self.object.__name__) == "Professor":
                return self.post(email=email,name=name, password1=password1,password2=password2,graduation=graduation,telefoneNumber=telefoneNumber,photo=photo)

        pass_hash = generate_password_hash(password1)

        if user:
            # try:
            user.password   = pass_hash
            user.name       = name
            user.email      = email
            if (self.object.__name__) == "Professor":
                self.graduation = graduation
                self.telefoneNumber = telefoneNumber
                self.photo = photo

            db.session.commit()
            result          = self.get_json(user)
                
            data["message"] = "successfully updated"
            data["data"]    = result
            return data, 201
            # except:
            #     data["message"] = "unable to update"
            #     data["data"]    = {}
            #     return data, 500

    """Retorna todas as classes de um usuário específico."""
    def get_classes_from_user_by_id(self,id):
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

        user        = self.get_query_by_id(id)[0]

        if user:
            classes     = UserClassRelationship.query.filter_by(user_id=user.id).all()

            if classes:
                classesList = []

                for table in classes:
                    class_id = table.class_id
                    user    = Class.query.filter_by(id=class_id).first()
                    classesList.append(classe_get_json(user))
        
                data["message"] = "successfully updated"
                data["data"]    = classesList
                return data, 200
            else:
                data["message"] = "This user does not have any classes"
                data["data"]    = {}
                return data, 400
        
        else:
            data["message"] = "This user does not exists"
            data["data"]    = {}
            return data, 400

class AdminController(UserController):

    def __init__(self, object=Admin):
        super().__init__(object)

    """Retorna todas as classes de um usuário específico."""
    def get_classes_from_user_by_id(self,id):
        return None, 400

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

