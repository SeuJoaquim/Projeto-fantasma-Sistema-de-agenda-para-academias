from website import db
from api.database.models.personModels           import User
from werkzeug.security                              import generate_password_hash, check_password_hash


class ValidationController():     
    def __init__(self, object = User):
        self.flash = []
        self.object = object

    def execute(self,email,firstName,password1,password2):
        
        def DataIsValid():
            def flash(message, category):
                self.flash.append({
                    "message": message,
                    "category": category
                })
            isValid = True
            user        = self.object.query.filter_by(email=email).first()
            if user:
                flash("Email already exists.", category="error")
                isValid = False           
            if len(email) < 4:
                flash("Email must be greater then 4 characters.", category='error')
                isValid = False
            if len(firstName) <2:
                flash("First Name must be greater then 1 characters.", category='error')
                isValid = False
            if password1 != password2:
                flash("Password don\'t match.", category='error')
                isValid = False
            if len(password1) <7:
                flash("Password must be at least 7 characters.", category='error')
                isValid = False

            if isValid:
                flash("Account created!", category='success')
                data = {}
                data["messages"] = self.flash
                data["data"]     = [email,firstName,password1]
                return True, data
            
            data = {}
            data["messages"] = self.flash
            data["data"]     = []
            return False, data

        return DataIsValid()


        
        

            