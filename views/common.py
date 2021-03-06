from flask import jsonify, make_response
from main import app


@app.route('/')
@app.route('/home')
def home():
    return jsonify()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
