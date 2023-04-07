from models.index import db, People

def get_all_people():
    all_people = People.query.all()
    # another form to do it 
    # serialize_all_user = [user.serialize() for user in all_user]
    serialize_all_people = list(map(lambda people : people.serialize(), all_people))
    print(all_people)
    return serialize_all_people

def get_people_by_id(user_id):
    people = People.query.get(user_id)
    if people is None:
        return people
    return people.serialize()
    
def create_person(data):
    new_person = People(data['username'], data['history'], data['description'], data['user_id'])
    db.session.add(new_person)
    db.session.commit()
    return new_person.serialize()
