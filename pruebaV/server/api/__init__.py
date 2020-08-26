import os
from flask import Flask 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS 


#configuracion de iniciar app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
ma = Marshmallow(app)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#configuracion base de datos

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'jsons.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#blueprints

from api.core.views import core


app.register_blueprint(core)