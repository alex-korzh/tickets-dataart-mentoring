from flask import jsonify, request
from main import app
from models import Ticket
from .common import HttpStatus


@app.route('/tickets/', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([l.to_dict() for l in tickets])


@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_tickets_id(ticket_id):
    rez_tickets = Ticket.query.get(ticket_id)
    return jsonify(rez_tickets.to_dict())


@app.route('/tickets/<int:ticket_id>', methods=['PUT', 'DELETE'])
def update_ticket(ticket_id):
    rez_ticket = Ticket.query.get(ticket_id)
    construct = {}
    if request.method == 'PUT':
        rez_ticket.update(request.json)
        construct['success'] = True
        construct['message'] = 'Data saved'
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
    elif request.method == 'DELETE':
        try:
            rez_ticket.delete()
            construct['success'] = True
            construct['message'] = 'Ticket has been delete.'
            response = jsonify(construct)
            response.status_code = HttpStatus.OK
        except Exception as e:
            construct['success'] = False
            construct['error'] = str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST

    return response

