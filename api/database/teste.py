from website import db
from website.database.models.personModels       import User, Admin, Professor
from website.database.models.classModels        import Modality, Class
from website.database.models.relationshipModels import UserClassRelationship



from werkzeug.security import generate_password_hash, check_password_hash

def execute():
    new_user = User(email="test232e@gmail.com",name="papa", password=generate_password_hash("1234567",method="sha256"))
    db.session.add(new_user)
    db.session.commit()

    new_user = User(email="e@gmail.com",name="papa", password=generate_password_hash("1234567",method="sha256"))
    db.session.add(new_user)
    db.session.commit()

    
    new_professor = Professor(email="professor@gmail.com",name="Edna", password=generate_password_hash("1234567",method="sha256"), graduation="3º ano", telefoneNumber = "389")
    db.session.add(new_professor)
    db.session.commit()
    
    new_modality = Modality(name="Natacao")
    db.session.add(new_modality)
    db.session.commit()


    new_class = Class(name="Natacao", date="now", maxNumber=1,minNumber=2, professor_id=1,modality_id=1,)
    db.session.add(new_class)
    db.session.commit()

    new_class = Class(name="eafa", date="esw", maxNumber=1,minNumber=2, professor_id=1,modality_id=1,)
    db.session.add(new_class)
    db.session.commit()

    new_rela = UserClassRelationship(user_id=1, class_id=1)
    db.session.add(new_rela)
    db.session.commit()

    new_rela = UserClassRelationship(user_id=1, class_id=2)
    db.session.add(new_rela)
    db.session.commit()

    new_rela = UserClassRelationship(user_id=2, class_id=1)
    db.session.add(new_rela)
    db.session.commit()

def e():
    cla     = Class.query.filter_by(id=1).first()
    tables  = UserClassRelationship.query.filter_by(class_id=cla.id).all()
    
    for table in tables:
        user_id = table.user_id
        user = User.query.filter_by(id=user_id).first()
        print(user.email)