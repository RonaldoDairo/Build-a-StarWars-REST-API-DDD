from models.index import db,User

def get_all_users():
    all_user = User.query.all()
    # another form to do it 
    # serialize_all_user = [user.serialize() for user in all_user]
    serialize_all_user = list(map(lambda user : user.serialize(), all_user))
    return serialize_all_user

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user is None:
        return user
    return user.serialize()

def create_user(data):
    new_user= User(data['email'], data['password'], data['username'])
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()