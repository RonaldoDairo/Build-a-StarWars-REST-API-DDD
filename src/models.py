from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#**************************USER***************************
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    people = db.relationship('People')
    
    def __init__(self,email,password,username):
        self.email = email
        self.password = password
        self.username = username
        self.is_active = True

  
    def serialize(self):
        return {
        "id": self.id,
        "email": self.email,
        "username": self.username,
        "active":self.is_active,
        # do not serialize the password, its a security breach
        }

#**************************PEOPLE***************************************
class People(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    history_person = db.Column(db.String(255), unique=False, nullable=False)
    description = db.Column(db.String(200),unique=False, nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='people')
    
    def __init__(self, username, history_person, description, user_id):
        self.username = username
        self.history_person = history_person
        self.description = description
        self.user_id = user_id

    def serialize(self):
        return{
            "username":self.username,
            "history": self.history_person,
            "description": self.description,
            "user_id" : self.user_id,
            "user": self.user.serialize()
        }
# this only runs if `$ python src/app.py` is executed