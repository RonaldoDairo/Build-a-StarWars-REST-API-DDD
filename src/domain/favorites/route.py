from flask import request, jsonify
from models.index import db, Favorites
import domain.favorites.controller as  Controller

def favorite_route(app):

    @app.route('/user/favorites', methods=['GET'])
    def get_favorites():
        return Controller.get_all_favorites()

    @app.route('/favorites/people', methods=['POST'])
    def create_favorite_person():
        body = request.get_json()
        new_person =Controller.create_favorite_person(body)
        print('****person*',new_person)
        return jsonify(new_person), 201
    @app.route('/favorites/people/<int:id>', methods=['DELETE'])
    def delete_favorite_person(id):

        return Controller.Delete_by_id_favorite_person(id)

        
    
    @app.route('/favorites/planets', methods=['POST'])
    def create_favorite_planet():
        body = request.get_json()
        new_planet =Controller.create_favorite_planet(body)
        print('****person*',new_planet)
        return jsonify(new_planet), 201
    
    @app.route('/favorites/planets/<int:id>', methods=['DELETE'])
    def delete_favorite_planet(id):
        
        return Controller.Delete_by_id_favorite_planet(id)

    @app.route('/favorites/vehicles', methods=['POST'])
    def create_favorite_vehicle():
        body = request.get_json()
        new_vehicle =Controller.create_favorite_vehicle(body)
        print('****person*',new_vehicle)
        return jsonify(new_vehicle), 201
    
    @app.route('/favorites/vehicles/<int:id>', methods=['DELETE'])
    def delete_favorite_vehicle(id):
        
        return Controller.Delete_by_id_favorite_vehicle(id)