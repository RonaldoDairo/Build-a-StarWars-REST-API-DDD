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
    return new_person.only_people() # solo serializa lo que quiero que serialize