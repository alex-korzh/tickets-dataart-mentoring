from flask import request, jsonify, abort, make_response
from main import app
from models import Locality, Ticket


@app.route('/')
@app.route('/home/')
def home():
    return jsonify()


@app.route('/locality/')
def get_locality():
    localities = Locality.query.all()
    return jsonify([l.to_dict() for l in localities])


@app.route('/Tickets/')


def get_Tickets():
    tickets = Ticket.query.all()
    return jsonify([l.to_dict() for l in tickets])


@app.route('/locality/<int:locality_id>', methods=['GET'])
def get_locality_id(locality_id):

    rez_locality = Locality.query.filter_by(id=locality_id).first()

    return jsonify(rez_locality.to_dict())



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/Tickets', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    ticket = {
        'id': tickets[-1]['id'] + 1,
        'title': tickets.json['title'],
        'description': tickets.json.get('description', ""),
        'done': False
    }
    ticket.append(task)
    return jsonify({'ticket': ticket}), 201