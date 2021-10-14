from flask import jsonify, abort
from main import app
from models import Locality
from models import Ticket


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
    rez_locality = filter(lambda t: t['id'] == locality_id, Locality)
    if len(rez_locality) == 0:
        abort(404)
    return jsonify({'locality': rez_locality[0]})


