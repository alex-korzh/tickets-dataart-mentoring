import random
from typing import List
from werkzeug.security import generate_password_hash
from dto import UserDto, SignupDto, UsersListResponse
from models import User
from main import db
from utils import send_verification_email


class UserService:
    @staticmethod
    def get_all() -> List[UserDto]:
        tickets = User.query.all()
        return UsersListResponse(tickets=[UserDto(**s.to_dict()) for s in tickets])

    @staticmethod
    def get_one_by_id(id: int) -> UserDto:
        rez_ticket = User.query.get(id)
        return UserDto(**rez_ticket.to_dict())

    @staticmethod
    def delete(id: int) -> None:
        rez_user = User.query.get(id)
        rez_user.is_deleted = True
        db.session.commit()

    @staticmethod
    def blocked_user(id: int) -> None:
        rez_user = User.query.get(id)
        rez_user.is_blocked = True
        db.session.commit()

    @staticmethod
    def create(data: SignupDto) -> UserDto:
        new_user = User(email=data.email, password=generate_password_hash(data.password))
        db.session.add(new_user)
        db.session.commit()
        code = random.randint(1000, 9999)
        send_verification_email(data.email, str(code))
        return UserDto(**new_user.to_dict())


