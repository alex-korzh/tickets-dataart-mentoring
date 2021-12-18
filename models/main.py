from enum import Enum, auto

from main import db
from datetime import datetime
from models.base import ChangeableMixin


flight_to_station = db.Table(
    'flight_to_station',
    db.metadata,
    db.Column('flight_id', db.ForeignKey('flight.id')),
    db.Column('station_id', db.ForeignKey('station.id'))
)


class StationTypeEnum(Enum):
    AIRPORT = "A"
    RAILWAY_STATION = "R"


class TicketStatusEnum(Enum):
    CREATED = auto()
    BOOKED = auto()
    CANCEL_BOOKED = auto()
    PAID = auto()
    REFUND_AFTER_PAYMENT = auto()


class SeatClassEnum(Enum):
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()


class Locality(db.Model, ChangeableMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    population = db.Column(db.Integer)
    latitude = db.Column(db.DECIMAL)
    longitude = db.Column(db.DECIMAL)

    def __repr__(self):
        return f"Locality {self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }


class Station(db.Model, ChangeableMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    station_type = db.Column(db.Enum(StationTypeEnum))
    id_locality = db.Column(db.Integer, db.ForeignKey("locality.id"))

    def __repr__(self):
        return f"Station {self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "id_locality": self.id_locality,
            "station_type": self.station_type,
        }


class Ticket(db.Model, ChangeableMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    status = db.Column(db.Enum(TicketStatusEnum))
    id_station_departure = db.Column(db.Integer, db.ForeignKey("station.id"))
    id_station_arrival = db.Column(db.Integer, db.ForeignKey("station.id"))
    passenger_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    flight_id = db.Column(db.Integer, db.ForeignKey("flight.id"))
    passenger_data = db.Column(db.JSON)
    seat_class = db.Column(db.Enum(SeatClassEnum))
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"Ticket {self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "id_station_departure": self.id_station_departure,
            "id_station_arrival": self.id_station_arrival,
        }


class FlightSeatsByClass(db.Model, ChangeableMixin):
    # todo учесть то что это цена за всю поездку, а пассажир едет только часть пути.
    id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey("flight.id"))
    price = db.Column(db.Integer)
    seats_number = db.Column(db.Integer)
    seat_class = db.Column(db.Enum(SeatClassEnum))


class Flight(db.Model, ChangeableMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    stations = db.relationship("Station", secondary=flight_to_station)
    departure_time = db.Column(db.DateTime, default=datetime.utcnow)
    arrival_time = db.Column(db.DateTime, default=datetime.utcnow)
    # todo подумать как изменить структуру чтобы возвращать первую и последнюю станции рейса (добавить даты в промежуточную таблицу?)
    # todo ввести количество посадочных мест чтобы не продать лишних билетов

    seats_prices = db.relationship("TicketSeatsByClass")

    def __repr__(self):
        return f"Flight {self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
          #  Здесь можно ночальную и конечную станцию и время получать запросом. Нужно подумать
            "stations": self.stations,
        }

