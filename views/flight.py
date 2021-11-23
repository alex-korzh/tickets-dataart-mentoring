from http import HTTPStatus
from flask import jsonify, request, Response

from dto import FlightDto
from main import app
from models import Flight
from services.flight import FlightService


@app.route('/flights', methods=['GET'])
def get_flights():
    flights = FlightService.get_all()
    return jsonify([s.json() for s in flights])


@app.route('/flights/<int:flight_id>', methods=['GET'])
def get_flight_id(flight_id):
    flight = FlightService.get_one_by_id(flight_id)
    return flight.json()


@app.route('/stations/<int:station_id>/flights', methods=['GET'])
def get_all_by_station(station_id):
    rez_flights = FlightService.get_all_by_station(station_id)
    return jsonify([s.json() for s in rez_flights])


@app.route('/flights/<int:flight_id>', methods=['PUT'])
def update_flight(flight_id):
    rez_flight = Flight.query.get(flight_id)
    update_dto = FlightDto(**request.json)
    rez_flight.update(name=update_dto.name, station_type=update_dto.flight_type)
    return Response(status=HTTPStatus.OK)


