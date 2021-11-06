from flask import jsonify, request
from main import app
from models import Station
from .common import HttpStatus


@app.route('/stations/', methods=['GET'])
def get_stations():
    stations = Station.query.all()
    return jsonify([l.to_dict() for l in stations])


@app.route('/localities/<int:locality_id>/stations/', methods=['GET'])
def get_stations_locality_id(locality_id):
    rez_stations = Station.query.filter_by(id_locality=locality_id).first()
    return jsonify([l.to_dict() for l in rez_stations])


@app.route('/stations/<int:station_id>', methods=['GET'])
def get_stations_id(station_id):
    rez_stations = Station.query.get(station_id)
    return jsonify([l.to_dict() for l in rez_stations])


@app.route('/stations/<int:station_id>', methods=['PUT', 'DELETE'])
def update_station(station_id):
    rez_station = Station.query.get(station_id)
    construct = {}
    if request.method == 'PUT':
        rez_station.update(request.json)
        construct['success'] = True
        construct['message'] = 'Data saved'
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
    elif request.method == 'DELETE':
        try:
            rez_station.delete()
            construct['success'] = True
            construct['message'] = 'Station has been delete.'
            response = jsonify(construct)
            response.status_code = HttpStatus.OK
        except Exception as e:
            construct['success'] = False
            construct['error'] = str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST

    return response

