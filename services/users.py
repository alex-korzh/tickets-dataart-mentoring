from typing import List
from dto import UserDto
from models import User
from main import db


class StationService:
    @staticmethod
    def get_all() -> List[UserDto]:
        tickets = User.query.all()
        return [UserDto(**s.to_dict()) for s in tickets]

    @staticmethod
    def get_one_by_id(id: int) -> UserDto:
        rez_ticket = User.query.get(id)
        return UserDto(**rez_ticket.to_dict())

    @staticmethod
    def delete(id: int) -> UserDto:
        rez_user = User.query.get(id)
        setattr(rez_user, "is_deleted", True)
        db.session.commit()
        return UserDto(**rez_user.to_dict())
