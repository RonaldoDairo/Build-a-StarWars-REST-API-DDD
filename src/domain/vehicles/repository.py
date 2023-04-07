from models.index import db, Vehicles


def get_all_vehicles():
    all_vehicles = Vehicles.query.all()
    # another form to do it 
    # serialize_all_vehicles = [user.serialize() for user in all_planets]
    serialize_all_vehicles = list(map(lambda vehicle : vehicle.serialize(), all_vehicles))
    return serialize_all_vehicles

def get_vehicles_by_id(id):
    vehicles = Vehicles.query.get(id)
    if vehicles is None :
        return vehicles
    return vehicles.serialize()

def create_vehicle(data):
    new_vehicle = Vehicles(data['description'], data['history'], data['model'], data['year'], data['vehicles_id'] )
    db.session.add(new_vehicle)
    db.session.commit()
    return new_vehicle.serialize()