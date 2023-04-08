import domain.people.repository as Repository
import handel_response as Response
import domain.users.controller as UserController


def get_all_people():
    all_people = Repository.get_all_people()
    return Response.response_ok(all_people)

def get_people_by_id(user_id):
    people = Repository.get_people_by_id(user_id)
    if people is None:
        return Response.response_error('user no found', 404)
    return people

def create_person(data):
    if data['username'] is None or data['username'] == '':
        return Response.response_error('username require', 400)
    
    # person = UserController.get_user_by_id(data['user_id'])

    # if person is None:
    #     return Response.response_error('user no valid', 400)
    
    return Repository.create_person(data)