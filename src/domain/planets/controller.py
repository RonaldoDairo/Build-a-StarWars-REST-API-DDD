import domain.planets.repository as Repository
import handel_response as Response


def get_all_planets():
    all_planets = Repository.get_all_planets()
    return Response.response_ok(all_planets)

def all_planets_by_id(id):
    planet = Repository.all_planets_by_id(id)
    if planet is None:
        return Response.response_error( 'user not found', 404)
    return planet

def create_planet(data):
    if data['description'] is None or data['description'] == '':
        return Response.response_error( 'description not valid', 400)
    
    if data['rotation_period'] is None or data['rotation_period'] == '':
        return Response.response_error( 'rotation_period not valid', 400)
    
    return Repository.create_planet(data), 201
