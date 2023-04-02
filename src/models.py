from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#**************************USER***************************
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    people = db.relationship('People' , back_populates ='user')
    
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
        "people": list(map(lambda people: people.serialize_populate(), self.people))
        # do not serialize the password, its a security breach
        }
    def serialize_populate(self):
        return{
            "id" : self.id,
            "username" : self.username
        }

#**************************PEOPLE***************************************
class People(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    history_person = db.Column(db.String(255), unique=False, nullable=False)
    description = db.Column(db.String(200),unique=False, nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='people')
    # planets = db.relationship('Planets', back_populates='people')
   
    def __init__(self, username, history_person, description, user_id):
        self.username = username
        self.history_person = history_person
        self.description = description
        self.user_id = user_id

    def serialize(self):
        return{
            "id": self.id,
            "username":self.username,
            "history": self.history_person,
            "description": self.description,
            "user_id" : self.user_id,
            "user": self.user.serialize(),
            # "planets": list(map(lambda planets: planets.serialize_populate(), self.planets))
        }
    def serialize_populate(self):
        return{
            "id": self.id,
            "username": self.username,
            "description": self.description
        }
#******************************************PLANETS*******************************************************

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200),unique=False, nullable=False)
    history =db.Column(db.String(250), unique=False, nullable = False)
    tipes = db.Column(db.String(250), unique=False, nullable = False)
    people_id= db.Column(db.Integer, )
    # db.ForeignKey('people.id')
    # people = db.relationship('People', back_populates='planets')

    def __init__(self, description, history, tipes, people_id ):
        self.description= description
        self.history = history
        self.tipes = tipes
        self.people_id = people_id
        
    def serialize(self):
        return{
            "id": self.id,
            "description": self.description,
            "history": self.history_person,
            "tipes" : self.tipes,
            "people_id" : self.people_id,
            # "user": self.people.serialize()
        }
    def serialize_populate(self):
        return{
            "id": self.id,
            "description": self.description
        }
# this only runs if `$ python src/app.py` is executed