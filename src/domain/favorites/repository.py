from models.index import db, Favorites

def get_all_favorites():
    all_favorites =  Favorites.query.all()
    # another form to do it 
    # serialize_all_favorite = [favorite.serialize() for user in all_user]
    serialize_all_favorite = list(map(lambda favorite : favorite.serialize(), all_favorites))
    return serialize_all_favorite

def create_favorite_person(data):
    new_person = Favorites(data['user_id'],data['user_id_people'], data['user_id_planets'], data['user_id_vehicles'])
    print('newww ',new_person)
    db.session.add(new_person)
    db.session.commit()
    print('newww ',new_person)
    # return new_person.serialize() 
    return new_person.only_people() # solo serializa lo que quiero que serialize pero igual no influye
    #en lo que imprime realmente.
def Delete_by_id_favorite_person(user_id):
    people =  Favorites.query.get(user_id)
    if people is None:
        return people
    return people.only_people()

def create_favorite_planet(data):
    new_planet = Favorites(data['user_id'],data['user_id_people'], data['user_id_planets'], data['user_id_vehicles'])
    print('newww ',new_planet)
    db.session.add(new_planet)
    db.session.commit()
    print('newww ',new_planet)
    # return new_p.serialize() 
    return new_planet.only_planet() # solo serializa lo que quiero que serialize pero igual no influye
    #en lo que imprime realmente.

def create_favorite_vehicle(data):
    new_vehicle = Favorites(data['user_id'],data['user_id_people'], data['user_id_planets'], data['user_id_vehicles'])
    print('newww ',new_vehicle)
    db.session.add(new_vehicle)
    db.session.commit()
    print('newww ',new_vehicle)
    # return new_p.serialize() 
    return new_vehicle.only_vehicle() # solo serializa lo que quiero que serialize pero igual no influye
    #en lo que imprime realmente.