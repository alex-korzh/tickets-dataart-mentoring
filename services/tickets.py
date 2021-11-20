from typing import List
from dto import TicketDto
from models import Ticket


# TODO попробуй закончить
class StationService:
    @staticmethod
    def get_all() -> List[TicketDto]:
        tickets = Ticket.query.all()
        return [TicketDto(**s.to_dict()) for s in tickets]

    @staticmethod
    def get_one_by_id(id: int) -> TicketDto:
        rez_ticket = Ticket.query.get(id)
        return TicketDto(**rez_ticket.to_dict())
