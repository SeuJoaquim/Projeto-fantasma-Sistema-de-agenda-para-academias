from website.database.models.userModel import User

def user_by_email(email):
    try:
        return User.query.filter_by(email=email).first()
    except:
        return None