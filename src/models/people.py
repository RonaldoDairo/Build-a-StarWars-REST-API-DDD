from models.db import db 

class People(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(255), unique=False, nullable=False)
    height = db.Column(db.String(255), unique=False, nullable=False)
    mass = db.Column(db.String(200),unique=False, nullable=False)
    birth_year =db.Column(db.String(255), unique=False, nullable=False)
    # user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    # user = db.relationship('User', back_populates='people')
    # planets = db.relationship('Planets', back_populates='people')
    # FALTARIA CAMPO FAVORITE QUE BUSCARIA LA TABLA FAVORITE (BACKPOPULATE)
    favorites = db.relationship('Favorites')
    # planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    # planets= db.relationship('Planets') 

   
    def __init__(self, username, description, height, mass, birth_year ):
        self.username = username
        self.description = description
        self.height = height
        self.mass = mass
        self.birth_year = birth_year
        # self.user_id = user_id
        

    def serialize(self):
        return{
           "id": self.id,
            "username":self.username,
            "description": self.description,
            "height": self.description,
            "mass": self.description,
            "birth_year": self.description,
            # "user_id" : self.user_id,
            # "user": self.user.serialize()
            # "planets": list(map(lambda planets: planets.serialize_populate(), self.planets))
        }
    def serialize_populate(self):
        return{
            "id": self.id,
            "username": self.username,
            "description": self.description
        }

