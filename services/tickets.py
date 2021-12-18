from dto import TicketDto, TicketListResponse, TicketBuyResponse, BuyTicketDto
from main import db
from models import Ticket, TicketStatusEnum, FlightSeatsByClass


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

    # todo заменить passenger_id на id пользователя
    @classmethod
    def buy(cls, data: BuyTicketDto) -> TicketBuyResponse:
        passenger_id = 1
        prices = FlightSeatsByClass.query.filter_by(
            flight_id=data.flight_id,
            seat_class=data.seat_class
        ).one()
        # todo проверить, есть ли свободные места
        ticket = Ticket(
            status=TicketStatusEnum.CREATED,
            passenger_id=passenger_id,
            **data.dict(),
        )
        ticket.price = prices.price
        # todo отправлять email об успешной покупке с id билета
        ticket.status = TicketStatusEnum.BOOKED
        db.session.add(ticket)
        db.session.commit()
