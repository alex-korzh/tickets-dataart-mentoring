from main import db


class Locality(db.Model):
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
            "longitude": self.longitude
        }
