from http import HTTPStatus
from flask import jsonify, request, Response

from dto import StationUpdateDto
from main import app
from services.stations import StationService
from models import Locality


@app.route('/localities', methods=['GET'])
def get_locality():
    stations = StationService.get_all()
    return jsonify([s.json() for s in stations])
    ality.query.all()
    rez = jsonify([l.to_dict() for l in localities])
    return rez


@app.route('/localities/<int:locality_id>', methods=['GET'])
def get_locality_id(locality_id):
    rez_locality = Locality.query.get(locality_id)
    return jsonify(rez_locality.to_dict())


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


