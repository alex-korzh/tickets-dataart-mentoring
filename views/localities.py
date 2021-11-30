from http import HTTPStatus
from flask import jsonify, request, Response
from main import app
from services.localities import LocalityService
from models import Locality


@app.route('/localities', methods=['GET'])
def get_locality():
    localities = LocalityService.get_all()
    return jsonify([s.json() for s in localities])


@app.route('/localities/<int:locality_id>', methods=['GET'])
def get_locality_id(locality_id):
    station = LocalityService.get_one_by_id(locality_id)
    return station.json()


@app.route('/localities/<int:locality_id>', methods=['PUT'])
def update_locality(locality_id):
    LocalityService.put_by_id(locality_id, request.json)
    return Response(status=HTTPStatus.OK)


@app.route('/localities/<int:locality_id>', methods=['DELETE'])
def delete_locality(locality_id):
    LocalityService.delete_by_id(locality_id)
    return Response(status=HTTPStatus.OK)


