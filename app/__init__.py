
from flask import Flask  
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = 'mariadb://root:hendra24@localhost/bigpro'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:postgres@localhost/'

db = SQLAlchemy(app)

app.config.from_object(Config)
from app.controllers import *
assets = Environment(app)

jwt = JWTManager(app)

from app.models import historiModel, userModel, dosenModel
from app import routes

