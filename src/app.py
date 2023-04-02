"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Vehicles
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)
#******************************** USER
@app.route('/user', methods=['GET'])
def handle_hello():
    all_user = User.query.all()
    # another form to do it 
    # serialize_all_user = [user.serialize() for user in all_user]
    serialize_all_user = list(map(lambda user : user.serialize(), all_user))
    print(all_user)
    return jsonify(serialize_all_user), 200
 # para obtener informacion por id , solo exite para obtenes datos
 # en concreto id y string
@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    print(id)
    user = User.query.get(id)
    user_serialize = user.serialize()
    return jsonify(user.serialize),200

@app.route('/user', methods=['POST'])
def create_user():
    data = (request.get_json())
    new_user= User(data['email'], data['password'], data['username'])
    db.session.add(new_user)
    db.session.commit()
    print(new_user)
    print(request.get_json())
    return jsonify("Hola Soy El Post "),200
#***************************************PEOPLE
@app.route('/people', methods=['POST'])
def create_person():
    data = (request.get_json())
    print('data del  ******', data)
    new_person = People(data['username'], data['history'], data['description'], data['user_id'])
    print('new_person ******', new_person)
    db.session.add(new_person)
    db.session.commit()
    print('new_person ******', new_person)
    return jsonify(new_person.serialize()),200
#******************************************PLANETS********************************************************
@app.route('/planets', methods= ['POST'])
def create_planet():
    data = (request.get_json())
    print('data del planet  ******', data)
    new_planet= Planets(data['description'], data['history'], data['tipes'], data['people_id'] )
    print('new_planet ****', new_planet)
    db.session.add(new_planet)
    db.session.commit()
    print('new_planet ****', new_planet)
    return jsonify(new_planet.serialize())
#**************************************VEHICLE***********************************************************
@app.route('/vehicles', methods=['POST'])
def create_vehicle():
    data = (request.get_json())
    print('data  del vehicle*******', data)
    new_vecicle = Vehicles(data['description'], data['history'], data['model'], data['year'], data['vehicles_id'] )
    print('new_vehicle ******', new_vecicle)
    db.session.add(new_vecicle)
    db.session.commit()
    print('new_vehicle ******', new_vecicle)
    return jsonify(new_vecicle.serialize())
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)