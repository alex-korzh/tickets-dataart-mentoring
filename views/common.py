from flask import jsonify, make_response
from main import app
from models import Locality, Ticket, Station


@app.route('/')
@app.route('/home/')
def home():
    return jsonify()


@app.route('/localities/', methods=['GET'])
def get_locality():
    localities = Locality.query.all()
    return jsonify([l.to_dict() for l in localities])


@app.route('/tickets/', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([l.to_dict() for l in tickets])


@app.route('/stations/', methods=['GET'])
def get_stations():
    station = Station.query.all()
    return jsonify([l.to_dict() for l in station])


@app.route('/localities/<int:locality_id>', methods=['GET'])
def get_locality_id(locality_id):
    rez_locality = Locality.query.get(locality_id)
    return jsonify(rez_locality.to_dict())


@app.route('/localities/<int:locality_id>/stations/', methods=['GET'])
def get_stations_locality_id(locality_id):
    rez_stations = Station.query.filter_by(id_locality=locality_id).first()
    return jsonify([l.to_dict() for l in rez_stations])


@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_tickets_id(ticket_id):
    rez_tickets = Ticket.query.get(ticket_id)
    return jsonify(rez_tickets.to_dict())


@app.route('/stations/<int:station_id>', methods=['GET'])
def get_stations_id(station_id):
    rez_stations = Station.query.get(station_id)
    return jsonify([l.to_dict() for l in rez_stations])


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# TODO сделать эндпоинт для вывода станций конкретного города
