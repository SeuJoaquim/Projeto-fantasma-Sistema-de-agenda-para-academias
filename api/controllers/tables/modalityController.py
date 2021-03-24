from api.database.models.classModels        import Modality, Class

from flask import jsonify
from website import db

class ModalityController(DatabaseController):
    def __init__(self, object=Modality):
        super().__init__(object)

    """ Retorna objeto dicionário com informações específicas  """
    def get_json(self,dict):
        # name="Natacao", date="now", maxNumber=1,minNumber=2, professor_id=1,modality_id=1,
        data = {}
        data["id"]      = dict.id
        data["name"]    = dict.name
        return data

    """Cadastro de modalityes com validação de existência"""
    def post(self,name):
        data = {}
        try:
            new_modality = Modality(name=name)
            db.session.add(new_modality)
            db.session.commit()
            data["message"] = "Successfully added"
            data["data"]    = self.get_json(new_modality)
            return data, 200

        except:
            data["message"] = "Unable to add modality"
            data["data"]    = {}
            return data, 404

    """Atualiza modality baseado no ID, caso o mesmo exista."""
    def update(self,id,name):
        data = {}
        modality = self.get_query_by_id(id)[0]
        if not modality:
            data["message"] = "modality don't exist"
            data["data"]    = {}
            return data, 404


        if modality:
            try:
                modality.name             = name
                db.session.commit()
                result          = self.get_json(modality)
                
                data["message"] = "successfully updated"
                data["data"]    = result
                return data, 201
            except:
                data["message"] = "unable to update"
                data["data"]    = {}
                return data, 500

    """Retorna todas as classes de um modality específica."""
    def get_classes_from_modality_by_id(self, id):
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
            classes       = Class.query.filter_by(modality_id=id).all()
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
