from models.index import db, Favorites

def get_all_favorites():
    all_favorites =  Favorites.query.all()
    # another form to do it 
    # serialize_all_favorite = [favorite.serialize() for user in all_user]
    serialize_all_favorite = list(map(lambda favorite : favorite.serialize(), all_favorites))
    return serialize_all_favorite