from website.database.models.personModels           import Admin
from website.controllers.tables.userController      import UserController

class AdminController(UserController):
    def __init__(self, object=Admin):
        super().__init__(object)

    """Retorna todas as classes de um usuário específico."""
    def get_classes_from_user_by_id(self,id):
        return None, 400