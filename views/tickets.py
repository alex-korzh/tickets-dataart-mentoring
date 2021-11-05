from flask import jsonify

from main import app
from models import Ticket


@app.route('/tickets/', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([l.to_dict() for l in tickets])


@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_tickets_id(ticket_id):
    rez_tickets = Ticket.query.get(ticket_id)
    return jsonify(rez_tickets.to_dict())
