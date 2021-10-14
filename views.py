from flask import jsonify
from main import app
from models import Locality
from models import Ticket
from flask.views import View


def home():
    return jsonify('index.html', context='Это главная страница')


app.add_url_rule('/', view_func=home)
app.add_url_rule('/home', view_func=home)


class Showlocalitys(View):

    def dispatch_request(self):
        localitys = Locality.query.all()
        return jsonify([l.to_dict() for l in localities])
        #return jsonify('users.html', objects=localitys)


app.add_url_rule('/locality/', view_func=Showlocalitys.as_view('show_localitys'))

@app.route("/locality")
def get_locality():
    localities = Locality.query.all()
    return jsonify([l.to_dict() for l in localities])


@app.route("/Tickets")
def get_Tickets():
    Tickets = Ticket.query.all()
    return jsonify([l.to_dict() for l in Tickets])


# @app.route('/')
# @app.route('/home')
#def home():
# title = "Главная страница"
    #source = """<html><body>
    #        <h1>{{h1}}</h1>
    #        <h3><a href="{{url_for('hello')}}">Страница с приветом...</a></h3>
    #        </body></html>"""
    # return jsonify(source, h1=title)
    # return jsonify(
    #     'index.html',
    #     title='Home Page',
    #     year=datetime.now().year,
    # )


