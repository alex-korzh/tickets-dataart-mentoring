import enum
from datetime import datetime

from main import db
from models.base import ChangeableMixin

flight_to_station = db.Table(
    'flight_to_station',
    db.metadata,
    db.Column('flight_id', db.ForeignKey('flight.id')),
    db.Column('station_id', db.ForeignKey('station.id'))
)


class StationTypeEnum(enum.Enum):
    airport = "A"
    railway_station = "R"


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
    id_station_departure = db.Column(db.Integer, db.ForeignKey("station.id"))
    id_station_arrival = db.Column(db.Integer, db.ForeignKey("station.id"))
    departure_time = db.Column(db.DateTime, default=datetime.utcnow)
    arrival_time = db.Column(db.DateTime, default=datetime.utcnow)
    passenger_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    flight_id = db.Column(db.Integer, db.ForeignKey("flight.id"))

    def __repr__(self):
        return f"Ticket {self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "id_station_departure": self.id_station_departure,
            "id_station_arrival": self.id_station_arrival,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
        }


class Flight(db.Model, ChangeableMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    departure_time = db.Column(db.DateTime, default=datetime.utcnow)
    arrival_time = db.Column(db.DateTime, default=datetime.utcnow)
    stations = db.relationship("Station", secondary=flight_to_station)

    def __repr__(self):
        return f"Flight {self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "stations": self.stations,
        }