from models.db import db 
    
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
            # "user": self.user.serialize()
            # "planets": list(map(lambda planets: planets.serialize_populate(), self.planets))
        }
    def serialize_populate(self):
        return{
            "id": self.id,
            "username": self.username,
            "description": self.description
        }

