from http import HTTPStatus
from flask import jsonify, request, Response

from dto import StationUpdateDto
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
    rez_locality = Locality.query.get(locality_id)
    rez_locality.update(request.json)
    return Response(status=HTTPStatus.OK)


@app.route('/localities/<int:locality_id>', methods=['DELETE'])
def delete_locality(locality_id):
    rez_locality = Locality.query.get(locality_id)
    rez_locality.delete()
    return Response(status=HTTPStatus.OK)


