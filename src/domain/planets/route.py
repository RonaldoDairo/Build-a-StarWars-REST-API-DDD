from flask import request, jsonify
from models.index import db, Planets
import domain.planets.controller as Controller

def planets_route(app):
        @app.route('/planets', methods=['GET'])
        def get_all_planets():
            return Controller.get_all_planets()
        # para obtener informacion por id , solo exite para obtenes datos
        # en concreto id y string
        @app.route('/planets/<int:id>', methods=['GET'])
        def get_planets(id):   
            return Controller.all_planets_by_id(id)

        @app.route('/planets', methods= ['POST'])
        def create_planet():
            body = request.get_json()
            return Controller.create_planet(body)
            