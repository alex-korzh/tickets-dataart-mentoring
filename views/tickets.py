from flask import jsonify, request, Response
from main import app
from models import Ticket
from http import HTTPStatus
from dto import StationUpdateDto
from services.tickets import StationService


@app.route('/tickets', methods=['GET'])
def get_tickets():
    tickets = StationService.get_all()
    return jsonify([s.json() for s in tickets])


@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_tickets_id(ticket_id):
    ticket = StationService.get_one_by_id(ticket_id)
    return ticket.json()


@app.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    rez_tickets = Ticket.query.get(ticket_id)
    rez_tickets.update(request.json)
    return Response(status=HTTPStatus.OK)


@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    rez_tickets = Ticket.query.get(ticket_id)
    rez_tickets.delete()
    return Response(status=HTTPStatus.OK)

