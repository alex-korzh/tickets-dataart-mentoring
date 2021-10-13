from flask import jsonify
from main import app
from models import Locality
from models import Ticket
from datetime import datetime


@app.route('/')
@app.route('/home')
def home():
    title = "Главная страница"
    source = """<html><body>
            <h1>{{h1}}</h1>
            <h3><a href="{{url_for('hello')}}">Страница с приветом...</a></h3>
            </body></html>"""
    return jsonify(source, h1=title)
    # return jsonify(
    #     'index.html',
    #     title='Home Page',
    #     year=datetime.now().year,
    # )


@app.route("/locality")
def get_locality():
    localities = Locality.query.all()
    return jsonify([l.to_dict() for l in localities])


@app.route("/Tickets")
def get_Tickets():
    Tickets = Ticket.query.all()
    return jsonify([l.to_dict() for l in Tickets])

