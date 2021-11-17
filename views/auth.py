from http import HTTPStatus

from flask import request, Response
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from pydantic import ValidationError
from werkzeug.security import check_password_hash

from dto import LoginDto, CredentialsDto, RefreshDto
from main import app
from models import User


@app.route('/login/', methods=['POST'])
def login():
    try:
        login_data = LoginDto(**request.json)
    except ValidationError:
        return Response(status=HTTPStatus.BAD_REQUEST)
    user = User.query.filter_by(email=login_data.email).one_or_none()
    if not user:
        return Response(status=HTTPStatus.NOT_FOUND)
    if check_password_hash(user.password, login_data.password):
        return Response(status=HTTPStatus.UNAUTHORIZED)

    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    res = CredentialsDto(
        id=user.id,
        access_token=access_token,
        refresh_token=refresh_token,
    )
    return res.json()


@app.route('/refresh/', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return RefreshDto(access_token=access_token).json()


# регистрацию сделаем позже