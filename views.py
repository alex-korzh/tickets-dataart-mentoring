from flask import jsonify

from main import app

#
# LOCALITIES = [
#     {
#         "id": 1,
#         "name": "Kyiv",
#         "population": 3000000,
#         "latitude": 50.271678,
#         "longitude": 30.312568
#     },
#     {
#         "id": 2,
#         "name": "Moscow",
#         "population": 12000000,
#         "latitude": 55.8661894,
#         "longitude": 37.8326612,
#     }
# ]
#
from models import Locality


@app.route("/locality")
def get_locality():
    localities = Locality.query.all()
    return jsonify([l.to_dict() for l in localities])
