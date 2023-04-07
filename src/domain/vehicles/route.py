from flask import request,jsonify
import domain.vehicles.controller as Controller


def vehicles_route(app):
        @app.route('/vehicles', methods=['GET'])
        def get_all_vehicles():
            return Controller.get_all_vehicles()
                
                
        # para obtener informacion por id , solo exite para obtenes datos
        # en concreto id y string
        @app.route('/vehicles/<int:id>', methods=['GET'])
        def get_vehicles(id):
            return Controller.get_vehicles_by_id(id)

        @app.route('/vehicles', methods=['POST'])
        def create_vehicle():
            body = request.get_json()        
            return Controller.create_vehicle(body)