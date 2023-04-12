from models.index import db, Favorites
from flask import jsonify # este jsonify solo esta aqui para el addpoint de delete


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
    return new_person.serialize() # solo serializa lo que quiero que serialize pero igual no influye
    #en lo que imprime realmente.
def Delete_by_id_favorite_person(id):
    person = Favorites.query.get(id)
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person successfully deleted.'}), 200
    else:
        return jsonify({'message': 'Person not found.'}), 404

def create_favorite_planet(data):
    new_planet = Favorites(data['user_id'],data['user_id_people'], data['user_id_planets'], data['user_id_vehicles'])
    print('newww ',new_planet)
    db.session.add(new_planet)
    db.session.commit()
    print('newww ',new_planet)
    # return new_p.serialize() 
    return new_planet.only_planet() # solo serializa lo que quiero que serialize pero igual no influye
    #en lo que imprime realmente.

def Delete_by_id_favorite_planet(id):
    planet = Favorites.query.get(id)
    if planet:
        db.session.delete(planet)
        db.session.commit()
        return jsonify({'message': 'Planet successfully deleted.'}), 200
    else:
        return jsonify({'message': 'Planet not found.'}), 404

def create_favorite_vehicle(data):
    new_vehicle = Favorites(data['user_id'],data['user_id_people'], data['user_id_planets'], data['user_id_vehicles'])
    print('newww ',new_vehicle)
    db.session.add(new_vehicle)
    db.session.commit()
    print('newww ',new_vehicle)
    # return new_p.serialize() 
    return new_vehicle.only_vehicle() # solo serializa lo que quiero que serialize pero igual no influye
    #en lo que imprime realmente.

def Delete_by_id_favorite_vehicle(id):
    vehicle = Favorites.query.get(id)
    if vehicle:
        db.session.delete(vehicle)
        db.session.commit()
        return jsonify({'message': 'Vehicle successfully deleted.'}), 200
    else:
        return jsonify({'message': 'Vehicle not found.'}), 404