from typing import List
from dto import FlightDto
from models import Flight, flight_to_station


class FlightService:
    @staticmethod
    def get_all() -> List[FlightDto]:
        flights = Flight.query.all()
        return [FlightDto(**s.to_dict()) for s in flights]

    @staticmethod
    def get_one_by_id(id: int) -> FlightDto:
        rez_flight = Flight.query.get(id)
        return FlightDto(**rez_flight.to_dict())

    @staticmethod
    def get_all_by_station(id: int) -> FlightDto:
        rez_flights = Flight.query.filter_by(station_id=id).all()
        return [FlightDto(**s.to_dict()) for s in rez_flights]
