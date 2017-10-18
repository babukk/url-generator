
import sys
from sqlalchemy import create_engine, MetaData
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import app_config

app = Flask(__name__, instance_relative_config=True)

app.config.from_object(app_config['development'])
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
ma = Marshmallow(app)
db.init_app(app)

from . import views, models

try:
    db.create_all()
    print "----------------- done "
except exc.SQLAlchemyError as ex:
    print "Fatal error: " + str(ex)
    sys.exit(1)

# --------------------------------------------------------------------------------------------------
def create_app():
    return app
