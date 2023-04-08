from models.db import db  

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_id_people= db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
    user_id_planets= db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)
    user_id_vehicles= db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    user = db.relationship('User')
    people = db.relationship('People')
    planets = db.relationship('Planets')
    vehicles = db.relationship('Vehicles')
    
    

    def __init__(self, user_id,  user_id_people, user_id_planets, user_id_vehicles):
        self.user_id_people = user_id_people
        self.user_id_planets = user_id_planets
        self.user_id_vehicles = user_id_vehicles
    
    def serialize(self):
        return{
        "id" : self.id,
        "user_id": self.user_id,
        "user_id_people" : self.user_id_people,
        "user_id_planets" : self.user_id_planets,
        "user_id_vehicles" : self.user_id_vehicles,
        }


        

        