from http import HTTPStatus
from flask import jsonify, request, Response
from main import app
from models import User


@app.route('/users/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([l.to_dict() for l in users])


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_id(user_id):
    rez_user = User.query.get(user_id)
    return jsonify(rez_user.to_dict())


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    rez_user = User.query.get(user_id)
    rez_user.update(request.json)
    return Response(status=HTTPStatus.OK)


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    rez_user = User.query.get(user_id)
    rez_user.delete()
    return Response(status=HTTPStatus.OK)

