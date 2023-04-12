from models.db import db

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    passengers = db.Column(db.String(200),unique=False, nullable=False)
    length = db.Column(db.String(200), unique=False, nullable = False)
    model= db.Column(db.String(200), unique=False, nullable = False)
    year = db.Column(db.String(200), unique=False, nullable= False) 
    cargo_capacity = db.Column(db.String(200),unique=False, nullable= False)
    favorites = db.relationship('Favorites')

    def __init__(self, passengers, length, model, year, cargo_capacity):
        self.passengers = passengers
        self.length = length
        self.model = model
        self.year = year
        self.cargo_capacity = cargo_capacity
    
    def serialize(self):
        return{
            "id" : self.id,
            "passengers" : self.passengers,
            "length" : self.length,
            "model" : self.model,
            "year": self.year,
            "cargo_capacity" : self.cargo_capacity
        }
    def serialize_populate(self):
        return{
            "id": self.id,
            "passengers": self.passengers
        }
