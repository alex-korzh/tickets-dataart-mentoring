from flask import jsonify, make_response
from main import app


class HttpStatus:
    OK = 200
    CREATED = 201
    NOT_FOUND = 404
    BAD_REQUEST = 400


@app.route('/')
@app.route('/home/')
def home():
    return jsonify()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
