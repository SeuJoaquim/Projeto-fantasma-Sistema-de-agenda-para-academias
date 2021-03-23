from website import db

class UserClassRelationship(db.Model):
    user_id     = db.Column(db.Integer, db.ForeignKey("user.id"),primary_key=True)
    class_id    = db.Column(db.Integer, db.ForeignKey("class.id"),primary_key=True)