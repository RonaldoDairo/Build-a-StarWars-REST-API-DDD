from models.db import db

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200),unique=False, nullable=False)
    history =db.Column(db.String(200), unique=False, nullable = False)
    model= db.Column(db.String(200), unique=False, nullable = False)
    year = db.Column(db.String(200), unique=False, nullable= False) 
    vehicles_id = db.Column(db.Integer)

    def __init__(self, description, history, model, year, vehicles_id):
        self.description = description
        self.history = history
        self.model = model
        self.year = year
        self.vehicles_id = vehicles_id
    
    def serialize(self):
        return{
            "id" : self.id,
            "description" : self.description,
            "history" : self.history,
            "model" : self.model,
            "year": self.year,
            "vehicles_id" : self.vehicles_id
        }
    def serialize_populate(self):
        return{
            "id": self.id,
            "description": self.description
        }
