from models.db import db

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200),unique=False, nullable=False)
    diameter =db.Column(db.Integer, unique=False, nullable = False)
    climate = db.Column(db.String(250), unique=False, nullable = False)
    terrain =db.Column(db.String(250), unique=False, nullable = False)
    rotation_period =db.Column(db.Integer, unique=False, nullable = False)
    # people_id= db.Column(db.Integer)
    # db.ForeignKey('people.id')
    # people = db.relationship('People', back_populates='planets')
    favorites = db.relationship('Favorites')
    # people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    # people= db.relationship('People')
    

    def __init__(self, description, diameter, climate, terrain, rotation_period):
        self.description= description
        self.diameter = diameter
        self.climate = climate
        self.terrain = terrain
        self.rotation_period = rotation_period
        # self.people_id = people_id
        
    def serialize(self):
        return{ 
            "id": self.id,
            "description": self.description,
            "diameter": self.diameter,
            "climate" : self.climate,
            "terrain" : self.terrain,
            "rotation_period" : self.rotation_period
            # "user": self.people.serialize()
        }
    def serialize_populate(self):
        return{
            "id": self.id,
            "description": self.description
        }