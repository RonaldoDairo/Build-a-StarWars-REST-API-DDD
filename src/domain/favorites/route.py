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