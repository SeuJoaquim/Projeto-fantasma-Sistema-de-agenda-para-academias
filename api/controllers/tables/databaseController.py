from website import db

class DatabaseController():
    def __init__(self, object):
        self.object = object

    """ Retorna objeto do id especificado  """
    def get_query_by_id(self,id):
        try:
            return self.get_json(self.object.query.filter_by(id=id).first()), 200
        except:
            return False, 400

    """ Retorna objeto dicionário com informações específicas  """
    def get_json(self,dict):
        pass
    
    """Retorna todos os objetos """
    def get_All(self,name=""):
        data = {}
        if name:
            users = self.object.query.filter(self.object.name.like(f'%{name}%')).all()
        else:
            users = self.object.query.all()
        if users:
            result = []
            for u in users:
                result.append(self.get_json(u))

            data["message"] = "successfully fetched"
            data["data"]    = result
            return data

        data["message"] = "nothing found"
        data["data"]    = {}
        return data
    
    """Cadastro de objeto"""
    def post(self):
        pass

    """Atualização de objeto"""
    def update(self):
        pass

    """Delete de objeto"""
    def delete(self,id):
        data = {}
        query = self.object.query.get(id)
        if not query:
            data["message"] = "Query don't exist"
            data["data"]    = {}
            return data, 404

        if query:
            try:
                db.session.delete(query)
                db.session.commit()
                result = self.get_json(query)
                data["message"] = "successfully deleted"
                data["data"]    = result
                return data, 200
            except:
                data["message"] = "unable to delete"
                data["data"]    = {}
                return data, 500