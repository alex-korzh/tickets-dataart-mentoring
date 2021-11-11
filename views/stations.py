from http import HTTPStatus
from flask import jsonify, request, Response
from main import app
from models import Station


@app.route('/stations/', methods=['GET'])
def get_stations():
    stations = Station.query.all()
    return jsonify([l.to_dict() for l in stations])


@app.route('/stations/<int:station_id>', methods=['GET'])
def get_stations_id(station_id):
    rez_stations = Station.query.get(station_id)
    return jsonify([rez_stations.to_dict() for l in rez_stations])


@app.route('/localities/<int:locality_id>/stations/', methods=['GET'])
def get_stations_locality_id(locality_id):
    rez_stations = Station.query.filter_by(id_locality=locality_id).first()
    return jsonify([l.to_dict() for l in rez_stations])


@app.route('/stations/<int:station_id>', methods=['PUT'])
def update_station(station_id):
    rez_station = Station.query.get(station_id)
    rez_station.update(request.json)
    return Response(status=HTTPStatus.OK)


@app.route('/stations/<int:station_id>', methods=['DELETE'])
def delete_station(station_id):
    rez_station = Station.query.get(station_id)
    rez_station.delete()
    return Response(status=HTTPStatus.OK)
