import enum
from main import db
from datetime import datetime
from models.base import ChangeableMixin


class Gender(enum.Enum):
    Woman = "W"
    Men = "M"


class User(db.Model, ChangeableMixin):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    is_admin = db.Column(db.Boolean)
    password = db.Column(db.String)
    is_deleted = db.Column(db.Boolean)
    is_blocked = db.Column(db.Boolean)
    is_active = db.Column(db.Boolean)

    def __repr__(self):
        return f"User {self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_admin": self.is_admin,
            "is_deleted": self.is_deleted,
            "is_blocked": self.is_blocked,
            "is_active": self.is_active,
        }


class Profile(db.Model, ChangeableMixin):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    full_name = db.Column(db.String)
    #TODO Погуглить ограничить количество символов серии и номера паспорта
    passport_page_2 = db.Column(db.Integer)
    passport_date_of_issue = db.Column(db.DateTime, default=datetime.utcnow)
    passport_is_issued_by = db.Column(db.String)
    residence_address = db.Column(db.String)
    gender = db.Column(db.Enum(Gender))
    date_of_birth = db.Column(db.DateTime, default=datetime.date)

    def __repr__(self):
        return f"Profile {self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "full_name": self.full_name,
            "passport_page_2": self.Passport_Page_2,
            "passport_date_of_issue": self.passport_Date_of_issue,
            "passport_is_issued_by": self.passport_is_issued_by,
            "residence_address": self.residence_address,
            "gender": self.gender,
            "date_of_birth": self.Date_of_birth,
        }
