from flask import jsonify, request, Response
from main import app
from models import Ticket
from http import HTTPStatus
from dto import StationUpdateDto
from services.tickets import TicketService


@app.route('/tickets', methods=['GET'])
def get_tickets():
    tickets = TicketService.get_all()
    return jsonify([s.json() for s in tickets])


@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_tickets_id(ticket_id):
    ticket = TicketService.get_one_by_id(ticket_id)
    return ticket.json()


@app.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    rez_tickets = Ticket.query.get(ticket_id)
    rez_tickets.update(request.json)
    return Response(status=HTTPStatus.OK)


@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    TicketService.delete_by_id(ticket_id)
    return Response(status=HTTPStatus.OK)
