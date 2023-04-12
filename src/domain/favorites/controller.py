import domain.favorites.repository as Repository
import handel_response as Response 

def get_all_favorites():
    all_favorites = Repository.get_all_favorites()
    return Response.response_ok(all_favorites)

def create_favorite_person(data):
    # if data['user_id_people'] is None or data['user_id_people'] == '':
    #     return Response.response_error('username require', 400)
    return Repository.create_favorite_person(data)

def Delete_by_id_favorite_person(user_id):
    people = Repository.Delete_by_id_favorite_person(user_id)
    if people is None:
        return Response.response_error('user no found', 404)
    return people

def create_favorite_planet(data):
    # if data['user_id_people'] is None or data['user_id_people'] == '':
    #     return Response.response_error('username require', 400)

    return Repository.create_favorite_planet(data)

def Delete_by_id_favorite_planet(user_id):
    planet = Repository.Delete_by_id_favorite_planet(user_id)
    # if planet is None:
    #     return Response.response_error('user no found', 404)
    return planet

def create_favorite_vehicle(data):
    # if data['user_id_people'] is None or data['user_id_people'] == '':
    #     return Response.response_error('username require', 400)

    return Repository.create_favorite_vehicle(data)

def Delete_by_id_favorite_vehicle(user_id):
    vehicle = Repository.Delete_by_id_favorite_vehicle(user_id)
    # if vehicle is None:
    #     return Response.response_error('user no found', 404)
    return vehicle