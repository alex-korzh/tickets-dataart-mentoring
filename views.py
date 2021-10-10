from flask import jsonify

from main import app

LOCALITIES1 = ""

LOCALITIES = [
    {
        "id": 1,
        "name": "Kyiv",
        "population": 3000000,
        "latitude": 50.271678,
        "longitude": 30.312568
    },
    {
        "id": 2,
        "name": "Moscow",
        "population": 12000000,
        "latitude": 55.8661894,
        "longitude": 37.8326612,
    }
]


@app.route("/locality")
def get_locality():
    return jsonify(LOCALITIES)
