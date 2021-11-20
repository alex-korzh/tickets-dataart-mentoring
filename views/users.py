from http import HTTPStatus
from flask import jsonify, request, Response
from main import app
from models import User
from services.users import UserService


@app.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all()
    return jsonify([s.json() for s in users])


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_id(user_id):
    users = UserService.get_one_by_id(user_id)
    return users.json()


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # todo update всего пользователя - не нужен, единственное что может админ - банить. Сделать поле is_blocked и вместо update менять только его
    rez_user = User.query.get(user_id)
    rez_user.update(request.json)
    return Response(status=HTTPStatus.OK)


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # todo не удалять а сделать поле is_deleted, отмечать его
    users = UserService.delete(user_id)
    return Response(status=HTTPStatus.OK)




# Проверка пароля на надежность
#def password_strong(data):
    #    return not(len(data) < 10 or data.isdigit() or data.isalpha() or data.islower() or data.isupper()) \
#            and data.isalnum()
