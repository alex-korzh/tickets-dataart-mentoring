from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://tickets:postgres@localhost:5432/tickets"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from views import *
from models import *

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
