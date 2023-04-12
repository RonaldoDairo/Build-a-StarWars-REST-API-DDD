from models.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    # people = db.relationship('People' , back_populates ='user')
    favorites = db.relationship('Favorites', back_populates='user' )
    
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
        "is_active":self.is_active,
        "favorites": list(map(lambda favorite: favorite.serialize_favs_user(), self.favorites))
        # "people": list(map(lambda people: people.serialize_populate(), self.people))
        # do not serialize the password, its a security breach
        }
    def serialize_populate(self):
        return{
            "id" : self.id,
            "username" : self.username
        }
