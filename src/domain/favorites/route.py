from flask import request, jsonify
from models.index import db, Favorites
import domain.favorites.controller as  Controller

def favorite_route(app):

    @app.route('/user/favorites', methods=['GET'])
    def get_favorites():
        return Controller.get_all_favorites()