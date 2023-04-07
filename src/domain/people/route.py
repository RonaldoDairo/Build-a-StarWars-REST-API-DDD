from flask import request, jsonify
from models.index import db, People
import domain.people.controller as Controller

def people_route(app):

    @app.route('/people', methods=['GET'])
    def get_all_people():
        return Controller.get_all_people()

    # para obtener informacion por id , solo exite para obtenes datos
    # en concreto id y string
    @app.route('/people/<int:id>', methods=['GET'])
    def get_people_by_id(id):
        return Controller.get_people_by_id(id)

    @app.route('/people', methods=['POST'])
    def create_person():
        body = request.get_json()
        new_person =Controller.create_person(body)
        return jsonify(new_person), 201
    