from website.database.models.classModels            import Class
from website.database.models.personModels           import User, Professor
from website.database.models.relationshipModels     import UserClassRelationship
from website.controllers.tables.databaseController  import DatabaseController

from flask import jsonify
from website import db

class ClassController(DatabaseController):
    def __init__(self, object=Class):
        super().__init__(object)

    """Gera dicionário somente com ID, EMAIL e PRIMEIRO NOME do classe"""
    def get_json(self,dict):

        data = {}
        data["name"]            = dict.name
        data["date"]            = dict.date
        data["maxNumber"]       = dict.maxNumber
        data["minNumber"]       = dict.minNumber
        data["professor_id"]    = dict.professor_id
        data["modality_id"]     = dict.modality_id

        return data

    """Cadastro de classes com validação de existência"""
    def post(self,name, date, maxNumber, minNumber, professor_id, modality_id):
        data = {}
        try:
            new_class = Class(name=name, date=date, maxNumber=maxNumber,minNumber=minNumber, professor_id=professor_id,modality_id=modality_id)
            db.session.add(new_class)
            db.session.commit()
            data["message"] = "Successfully added"
            data["data"]    = self.get_json(new_class)
            return data, 200

        except:
            data["message"] = "Unable to add class"
            data["data"]    = {}
            return data, 404

    """Atualiza classe baseado no ID, caso o mesmo exista."""
    def update(self,name, date, maxNumber, minNumber, professor_id, modality_id):
        data = {}
        classe = Class.query.get(id)

        if not classe:
            data["message"] = "classe don't exist"
            data["data"]    = {}
            return data, 404


        if classe:
            try:
                classe.name             = name
                classe.date             = date
                classe.maxNumber        = maxNumber
                classe.minNumber        = minNumber
                classe.professor_id     = professor_id
                classe.modality_id      = modality_id
                
                
                db.session.commit()
                result          = self.get_json(classe)
                
                data["message"] = "successfully updated"
                data["data"]    = result
                return data, 201
            except:
                data["message"] = "unable to update"
                data["data"]    = {}
                return data, 500

    """Deleta classe com base no ID da request"""
    def delete(self,id):
        data = {}
        classe = Class.query.get(id)
        if not classe:
            data["message"] = "classe don't exist"
            data["data"]    = {}
            return data, 404

        if classe:
            try:
                db.session.delete(classe)
                db.session.commit()
                result = get_json(classe)
                data["message"] = "successfully deleted"
                data["data"]    = result
                return data, 200
            except:
                data["message"] = "unable to delete"
                data["data"]    = {}
                return data, 500

    """Adiciona Usuário àlguma classe pelo seus ID."""
    def insert_user_in_class(self,user_id,class_id):
        data = {}
        table_row  = UserClassRelationship.query.filter_by(class_id=class_id).all()
        for field in table_row:
            if field.user_id == user_id:
                data["message"] = "This relationship already exists"
                data["data"]    = {}
                return data, 401

        try:
            new_rela = UserClassRelationship(user_id=user_id, class_id=class_id)
            db.session.add(new_rela)
            db.session.commit()
            data["message"] = "successfully created relationship"
            data["data"]    = self.get_json(self.get_query_by_id(new_rela.class_id))
            return data, 200
        
        except:
            data["message"] = "Unable to acess database"
            data["data"]    = {}
            return data, 400

    """Retorna todas os usuários de alguma classe específica."""
    def get_users_in_classe_by_id(self,id):
        data = {}
        def user_get_json(dict):
            data = {}
            data["id"]          = dict.id
            data["email"]       = dict.email
            data["name"]        = dict.name
            return data
        
        try:
            classe = self.get_query_by_id(id)[0]
            if classe:
                table  = UserClassRelationship.query.filter_by(class_id=classe.id).all()
                usersList = []

                for user in table:
                    user_id = user.user_id
                    user    = User.query.filter_by(id=user_id).first()
                    usersList.append(user_get_json(user))
                
                data["message"] = "successfully fetched"
                data["data"]    = usersList
                return data, 200

            else:
                data["message"] = "This class does not exists"
                data["data"]    = {}
                return data, 401
        
        except:
            data["message"] = "Unable to acess database"
            data["data"]    = {}
            return data, 400
   
    """Retorna todas os professores de alguma classe específica."""
    def get_professor_in_classe_by_id(self,id):
        data = {}
        def user_get_json(dict):
            data = {}
            data["id"]          = dict.id
            data["email"]       = dict.email
            data["name"]        = dict.name
            return data

        try:
            classe          = self.get_query_by_id(id)[0]
            if classe:
                professor_id    = classe.professor_id
                professor       = Professor.query.filter_by(id=professor_id).first()
                professorObj    = user_get_json(professor)
                
                data["message"] = "successfully fetched"
                data["data"]    = professorObj
                return data, 200
            
            else:
                data["message"] = "This class does not exists"
                data["data"]    = {}
                return data, 401
        
        except:
            data["message"] = "Unable to acess database"
            data["data"]    = {}
            return data, 400