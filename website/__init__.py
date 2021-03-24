from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import random
import string


db = SQLAlchemy()
DB_NAME = "database/database.db"
gen = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(gen) for i in range(12))


def create_app():
    # App configuration
    app = Flask(__name__, template_folder="./views/templates",static_url_path='', static_folder="./views/static" )
    app.config["SECRET_KEY"] = key
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    

    db.init_app(app)

    # Urls and homes
    from .routers.home import home as home_router
    from .routers.auth import auth as auth_router
    from .routers.app  import app as app_router
    app.register_blueprint(home_router, url_prefix="/")
    app.register_blueprint(auth_router, url_prefix="/auth")
    app.register_blueprint(app_router, url_prefix="/app")


    create_database(app)
    
    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")

