from models.db import db

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200),unique=False, nullable=False)
    history =db.Column(db.String(250), unique=False, nullable = False)
    tipes = db.Column(db.String(250), unique=False, nullable = False)
    people_id= db.Column(db.Integer)
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
            "history": self.history,
            "tipes" : self.tipes,
            "people_id" : self.people_id,
            # "user": self.people.serialize()
        }
    def serialize_populate(self):
        return{
            "id": self.id,
            "description": self.description
        }