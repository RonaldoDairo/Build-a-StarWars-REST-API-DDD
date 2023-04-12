from models.db import db  

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_id_people= db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
    user_id_planets= db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)
    user_id_vehicles= db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    #BACKPOPULATE TO FAVORITE
    user = db.relationship('User', back_populates= 'favorites')
    people = db.relationship('People',back_populates= 'favorites')
    planets = db.relationship('Planets',back_populates= 'favorites')
    vehicles = db.relationship('Vehicles',back_populates= 'favorites')
    
    

    def __init__(self, user_id,  user_id_people, user_id_planets, user_id_vehicles):
        self.user_id= user_id
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
    
    def serialize_favs_user(self):
        return{
            "id": self.id,
            "user_id_people" : self.user_id_people,
            "user_id_planets" : self.user_id_planets,
            "user_id_vehicles" : self.user_id_vehicles
        }


    def only_people(self):
        return{
        "id" : self.id,
        "user_id_people" : self.user_id_people,
        }

    def only_planet(self):
        return{
        "id" : self.id,
        "user_id_planets" : self.user_id_planets,
        }

    def only_vehicle(self):
        return{
        "id" : self.id,
        "user_id_vehicles" : self.user_id_vehicles,
        }
    
    

        

        