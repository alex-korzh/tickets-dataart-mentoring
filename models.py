import enum
from main import db
from datetime import datetime


class StationTypeEnum(enum.Enum):
    airport = "A"
    railway_station = "R"


class AccountType(enum.Enum):
    Administrator = "A"
    User = "U"


class ChangeableMixin:

    def update(self, data):
        for k, v in data.items():
            if hasattr(self, k):
                setattr(self, k, v)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()


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


class User(db.Model, ChangeableMixin):
    # todo name и surname = одно поле full_name
    # todo account_type не нужен, достаточно is_admin
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String)
    account_type = db.Column(db.Enum(AccountType))
    password = db.Column(db.String)

    def __repr__(self):
        return f"User {self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "account_type": self.account_type,
            "password": self.password,
        }

#Подумать над структурой таблици, что можно добавить