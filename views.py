from flask import request, jsonify, abort, make_response
from main import app
from models import Locality, Ticket, Station


@app.route('/')
@app.route('/home/')
def home():
    return jsonify()


@app.route('/locality/')
def get_locality():
    localities = Locality.query.all()
    return jsonify([l.to_dict() for l in localities])


@app.route('/tickets/')
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([l.to_dict() for l in tickets])


@app.route('/stations/')
def get_stations():
    station = Station.query.all()
    return jsonify([l.to_dict() for l in station])


@app.route('/locality/<int:locality_id>', methods=['GET'])
def get_locality_id(locality_id):

    rez_locality = Locality.query.filter_by(id=locality_id,).first()

    return jsonify(rez_locality.to_dict())


@app.route('/tickets/<int:tickets_id>', methods=['GET'])
def get_tickets_id(tickets_id):

    rez_tickets = Ticket.query.filter_by(id=tickets_id,).first()

    return jsonify(rez_tickets.to_dict())


@app.route('/stations/<int:locality_id>', methods=['GET'])
def get_stations_id(locality_id):

    rez_stations = Station.query.filter_by(id_locality=locality_id,).all()

    return jsonify([l.to_dict() for l in rez_stations])


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)




@app.route('/tickets', methods=['POST'])
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