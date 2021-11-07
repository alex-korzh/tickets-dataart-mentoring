from http import HTTPStatus
from flask import jsonify, request, Response
from main import app
from models import Locality


@app.route('/localities/', methods=['GET'])
def get_locality():
    localities = Locality.query.all()
    return jsonify([l.to_dict() for l in localities])


@app.route('/localities/<int:locality_id>', methods=['GET'])
def get_locality_id(locality_id):
    rez_locality = Locality.query.get(locality_id)
    return jsonify(rez_locality.to_dict())


@app.route('/localities/<int:locality_id>', methods=['PUT'])
def update_locality(locality_id):
    rez_locality = Locality.query.get(locality_id)
    rez_locality.update(request.json)
    return Response(status=HTTPStatus.OK)


@app.route('/localities/<int:locality_id>', methods=['DELETE'])
def delete_locality(locality_id):
    rez_locality = Locality.query.get(locality_id)
    rez_locality.delete()
    return Response(status=HTTPStatus.OK)


