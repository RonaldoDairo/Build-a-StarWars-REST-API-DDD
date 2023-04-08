import domain.favorites.repository as Repository
import handel_response as Response 

def get_all_favorites():
    all_favorites = Repository.get_all_favorites()
    return Response.response_ok(all_favorites)

def create_favorite_person(data):
    # if data['user_id_people'] is None or data['user_id_people'] == '':
    #     return Response.response_error('username require', 400)

    return Repository.create_favorite_person(data)