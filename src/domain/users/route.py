from flask import request, jsonify
from models.index import db, User
import domain.users.controller as Controller

def user_route(app):
    
    @app.route('/user', methods=['GET'])
    def get_all_users():
        return Controller.get_all_users()
    # para obtener informacion por id , solo exite para obtenes datos
    # en concreto id y string
    @app.route('/user/<int:id>', methods=['GET'])
    def get_user(id):
        return Controller.get_user_by_id(id)

    @app.route('/user', methods=['POST'])
    def create_user():
        body = request.get_json()
        return Controller.create_user(body)