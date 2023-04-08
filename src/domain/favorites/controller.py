import domain.favorites.repository as Repository
import handel_response as Response 

def get_all_favorites():
    all_favorites = Repository.get_all_favorites()
    return Response.response_ok(all_favorites)