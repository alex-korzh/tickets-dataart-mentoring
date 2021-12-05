from http import HTTPStatus
from flask import request, Response

from dto import FlightDto
from main import app
from models import Flight
from services.flight import FlightService

# todo посмотреть как реализовывается ограничение доступа


@app.route('/flights', methods=['GET'])
def get_flights():
    flights = FlightService.get_all()
    return flights.json()


@app.route('/flights/<int:flight_id>', methods=['GET'])
def get_flight_id(flight_id):
    flight = FlightService.get_one_by_id(flight_id)
    return flight.json()


@app.route('/stations/<int:station_id>/flights', methods=['GET'])
def get_all_by_station(station_id):
    rez_flights = FlightService.get_all_by_station(station_id)
    return rez_flights.json()


@app.route('/flights/<int:flight_id>', methods=['PUT'])
def update_flight(flight_id):
    rez_flight = Flight.query.get(flight_id)
    update_dto = FlightDto(**request.json)
    # TODO обновлять список станций
    rez_flight.update(name=update_dto.name)
    return Response(status=HTTPStatus.OK)


@app.route('/flights/<int:flight_id>', methods=['DELETE'])
def delete_flight(flight_id):
    FlightService.delete(flight_id)
    return Response(status=HTTPStatus.OK)

