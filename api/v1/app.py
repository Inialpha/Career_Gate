#!/usr/bin/python3
""" Flask Application """
from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify, session
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
from datetime import timedelta
from flask_session import Session
from flask_login import LoginManager
from models.user import User

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.secret_key = b'0cbc6611f5540bd0809a388dc95a615b'

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
login_manager.init_app(app)

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Set your desired session lifetime
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
#sess = Session(app)
#sess.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    print("\n\n\nid:", user_id)
    return

@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

Swagger(app)


if __name__ == "__main__":
    """ Main Function """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5001'
    app.run(host=host, port=port, threaded=True)
