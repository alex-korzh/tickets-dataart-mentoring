from dto import TicketDto, TicketListResponse
from models import Ticket


# TODO попробуй закончить
class TicketService:
    @staticmethod
    def get_all() -> TicketListResponse:
        tickets = Ticket.query.all()
        return TicketListResponse(tickets=[TicketDto(**s.to_dict()) for s in tickets])

    @staticmethod
    def get_one_by_id(id: int) -> TicketDto:
        rez_ticket = Ticket.query.get(id)
        return TicketDto(**rez_ticket.to_dict())

    @staticmethod
    def delete_by_id(id: int) -> None:
        rez_locality = Ticket.query.get(id)
        rez_locality.delete()
