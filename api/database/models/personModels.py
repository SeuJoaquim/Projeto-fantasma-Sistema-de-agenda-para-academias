from website import db

""" Classe inicial com informações base """
class Person():
    id              = db.Column(db.Integer, primary_key=True)
    email           = db.Column(db.String(150), unique=True)
    name            = db.Column(db.String(150))
    password        = db.Column(db.String(150))
    

""" Tabela de usuários """
class User(db.Model, Person):
    pass

""" Tabela de admins """
class Admin(db.Model, Person):
    isAdmin = db.Column(db.Boolean, default=True)

""" Tabela de professores """
class Professor(db.Model, Person):
    graduation      = db.Column(db.String(200))
    telefoneNumber  = db.Column(db.String( 15)) 
    photo           = db.Column(db.String())
