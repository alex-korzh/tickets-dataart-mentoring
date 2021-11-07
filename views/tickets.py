from flask import jsonify, request, Response
from main import app
from models import Ticket
from http import HTTPStatus


@app.route('/tickets/', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([l.to_dict() for l in tickets])


@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_tickets_id(ticket_id):
    rez_tickets = Ticket.query.get(ticket_id)
    return jsonify(rez_tickets.to_dict())


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

