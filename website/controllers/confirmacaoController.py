from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from website.database.models.userModel import User


class ConfirmnController():
    def __init__(self,email,password):
        self.email      = email
        self.password  = password
        self.flash      = []

    def execute(self):
        def flash(message, category):
                self.flash.append({
                    "message": message,
                    "category": category
                })

        data = {}

        user        = User.query.filter_by(email=self.email).first()
        if user:
            if check_password_hash(user.password, self.password):
                flash("Logged in sucessfully!", category="success")
                login_user(user, remember=True)
                data["code"]        = 200
                data["description"] = "Request accepted!"
                data["messages"]    = self.flash

            else:
                flash("Incorrect password, try again.", category="error")
                data["code"]        = 400
                data["description"] = "Bad Request"
                data["messages"]    = self.flash
        else:
            flash("Email does not exist.", category="error")
            data["code"]        = 400
            data["description"] = "Bad Request"
            data["messages"]    = self.flash
        
        return data