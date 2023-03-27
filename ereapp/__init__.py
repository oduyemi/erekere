from flask import Flask
from flask_sqlalchemy import SQLAlchemy


starter = Flask(__name__, instance_relative_config=True)
starter.config.from_pyfile('config.py', silent = False)
db = SQLAlchemy(starter)

from ereapp import adminroutes, userroutes