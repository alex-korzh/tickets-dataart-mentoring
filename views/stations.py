from http import HTTPStatus
from flask import jsonify, request, Response
from dto import StationUpdateDto
from main import app
from models import Station
from services.stations import StationService


@app.route('/stations', methods=['GET'])
def get_stations():
    stations = StationService.get_all()
    return jsonify([s.json() for s in stations])


@app.route('/stations/<int:station_id>', methods=['GET'])
def get_stations_id(station_id):
    station = StationService.get_one_by_id(station_id)
    return station.json()


@app.route('/localities/<int:locality_id>/stations/', methods=['GET'])
def get_stations_locality_id(locality_id):
    rez_stations = StationService.get_all_by_locality(locality_id)
    return jsonify([s.json() for s in rez_stations])


@app.route('/stations/<int:station_id>', methods=['PUT'])
def update_station(station_id):
    rez_station = Station.query.get(station_id)
    update_dto = StationUpdateDto(**request.json)
    rez_station.update(name=update_dto.name, station_type=update_dto.station_type)
    return Response(status=HTTPStatus.OK)


@app.route('/stations/<int:station_id>', methods=['DELETE'])
def delete_station(station_id):
    StationService.delete_by_id(station_id)
    return Response(status=HTTPStatus.OK)