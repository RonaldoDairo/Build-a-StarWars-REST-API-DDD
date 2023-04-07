from models.index import db, Planets


def get_all_planets():
    all_planets = Planets.query.all()
    print("***",all_planets)
    # another form to do it 
    # serialize_all_planets = [user.serialize() for user in all_planets]
    serialize_all_planets = list(map(lambda planet : planet.serialize(), all_planets))
    print(all_planets)
    return serialize_all_planets
def all_planets_by_id(id):
    planet = Planets.query.get(id)
    if planet is None:
        return planet 
    return planet.serialize()

def create_planet(data):
    new_planet= Planets(data['description'], data['history'], data['tipes'], data['people_id'] )
    db.session.add(new_planet)
    db.session.commit()
    return new_planet.serialize()
           
    