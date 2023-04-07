import domain.vehicles.repository as Repository
import handel_response as Response 

def get_all_vehicles():
    all_vehicles = Repository.get_all_vehicles()
    return Response.response_ok(all_vehicles)

def get_vehicles_by_id(id):
    vehicle = Repository.get_vehicles_by_id(id)

    if vehicle is None:
        return Response.response_error( 'user not found', 404)
    return vehicle

def create_vehicle(data):
    if data['description'] is None or data['description'] == '':
        return Response.response_error( 'description not valid', 400)
    
    if data['history'] is None or data['history'] == '':
        return Response.response_error( 'history not valid', 400)
    
    return Repository.create_vehicle(data), 201