from website import db
from website.database.models.userModel import User
from website.controllers.userDatabaseController import user_by_email
from werkzeug.security import generate_password_hash, check_password_hash



class ValidationController():
    def __init__(self,email,firstName,password1,password2):
        self.email      = email
        self.firstName  = firstName
        self.password1  = password1
        self.password2  = password2
        self.flash      = []

    def execute(self):
        def FormIsValid():
            def flash(message, category):
                self.flash.append({
                    "message": message,
                    "category": category
                })
            isValid = True
            user        = user_by_email(self.email)
            if user:
                flash("Email already exists.", category="error")
                isValid = False
                
            if len(self.email) < 4:
                flash("Email must be greater then 4 characters.", category='error')
                isValid = False
            if len(self.firstName) <2:
                flash("First Name must be greater then 1 characters.", category='error')
                isValid = False
            if self.password1 != self.password2:
                flash("Password don\'t match.", category='error')
                isValid = False
            if len(self.password1) <7:
                flash("Password must be at least 7 characters.", category='error')
                isValid = False

            if isValid:
                new_user = User(email=self.email,first_name=self.firstName, password=generate_password_hash(self.password1,method="sha256"))
                db.session.add(new_user)
                db.session.commit()
                

                flash("Account created!", category='success')
                isValid = True
            
            return isValid

        if FormIsValid():
            user        = user_by_email(self.email)
            data = {}
            data["code"]        = 200
            data["description"] = "Request accepted!"
            data["messages"]    = self.flash
        else:
            data = {}
            data["code"]        = 400
            data["description"] = "Bad Request"
            data["messages"]    = self.flash

        return data



        
        

            