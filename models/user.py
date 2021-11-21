from main import db
from models.base import ChangeableMixin


class User(db.Model, ChangeableMixin):

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String)
    email = db.Column(db.String)
    is_admin = db.Column(db.Boolean)
    password = db.Column(db.String)
    is_deleted = db.Column(db.Boolean)
    is_blocked = db.Column(db.Boolean)

    def __repr__(self):
        return f"User {self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "is_admin": self.is_admin,
            "is_deleted": self.is_deleted,
            "is_blocked": self.is_blocked,
        }
