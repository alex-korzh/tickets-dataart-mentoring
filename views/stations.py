from flask import jsonify, request

from main import app
from models import Station


@app.route('/stations/', methods=['GET'])
def get_stations():
    station = Station.query.all()
    return jsonify([l.to_dict() for l in station])


@app.route('/localities/<int:locality_id>/stations/', methods=['GET'])
def get_stations_locality_id(locality_id):
    rez_stations = Station.query.filter_by(id_locality=locality_id).first()
    return jsonify([l.to_dict() for l in rez_stations])


@app.route('/stations/<int:station_id>', methods=['GET'])
def get_stations_id(station_id):
    rez_stations = Station.query.get(station_id)
    return jsonify([l.to_dict() for l in rez_stations])


@app.route('/stations/<int:station_id>', methods=['PUT'])
def update_station(station_id):
    rez_station = Station.query.get(station_id)
    return rez_station.update(request.json)
