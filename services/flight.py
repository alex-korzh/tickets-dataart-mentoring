from dto import FlightDto, FlightListResponse
from models import Flight


class FlightService:
    @staticmethod
    def get_all() -> FlightListResponse:
        flights = Flight.query.all()
        return FlightListResponse(flights=[FlightDto(**s.to_dict()) for s in flights])

    @staticmethod
    def get_one_by_id(id: int) -> FlightDto:
        # todo подробный вид рейса должен быть подробнее ))
        rez_flight = Flight.query.get(id)
        return FlightDto(**rez_flight.to_dict())

    @staticmethod
    def get_all_by_station(id: int) -> FlightListResponse:
        rez_flights = Flight.query.filter_by(station_id=id).all()
        return FlightListResponse(flights=[FlightDto(**s.to_dict()) for s in rez_flights])

    @staticmethod
    def delete(id: int) -> None:
        rez_flight = Flight.query.get(id)
        rez_flight.delete()

# todo создание рейсов с ценой
