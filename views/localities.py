from flask import jsonify, request
from main import app
from models import Locality
from .common import HttpStatus


@app.route('/localities/', methods=['GET'])
def get_locality():
    localities = Locality.query.all()
    return jsonify([l.to_dict() for l in localities])


@app.route('/localities/<int:locality_id>', methods=['GET'])
def get_locality_id(locality_id):
    rez_locality = Locality.query.get(locality_id)
    return jsonify(rez_locality.to_dict())


@app.route('/localities/<int:locality_id>', methods=['PUT', 'DELETE'])
def update_locality(locality_id):
    rez_locality = Locality.query.get(locality_id)
    construct = {}
    if request.method == 'PUT':
        rez_locality.update(request.json)
        construct['success'] = True
        construct['message'] = 'Data saved'
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
    elif request.method == 'DELETE':
        try:
            rez_locality.delete()
            construct['success'] = True
            construct['message'] = 'locality has been delete.'
            response = jsonify(construct)
            response.status_code = HttpStatus.OK
        except Exception as e:
            construct['success'] = False
            construct['error'] = str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST

    return response
