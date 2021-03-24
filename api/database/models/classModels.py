from website import db

""" Tabela de modalidades """
class Modality(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(150))

""" Tabela de Classes """
class Class(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(150))
    date            = db.Column(db.String(150))
    
    maxNumber       = db.Column(db.Integer)
    minNumber       = db.Column(db.Integer)

    # FOREIGN KEYS Many to One
    professor_id    = db.Column(db.Integer, db.ForeignKey("professor.id"))
    modality_id     = db.Column(db.Integer, db.ForeignKey("modality.id"))
