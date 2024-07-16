#!/usr/bin/python3
"""
initialize the models package
"""
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from models.views import app_views
import models.views

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://{}:{}@{}/{}'.format(
    getenv('MYSQL_USER'),
    getenv('MYSQL_PWD'),
    getenv('MYSQL_HOST'),
    getenv('MYSQL_DB')
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "app_views.login"
login_manager.login_message_category = "info"

from os import getenv
app.register_blueprint(app_views)
storage_t = getenv("STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
