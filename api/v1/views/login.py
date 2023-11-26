#!/usr/bin/python3
""" objects that handle all default RestFul API actions for login """
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from flask_login import login_user, current_user
from hashlib import md5
from flask import session

@app_views.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():
    """
    login a user
    """
    data = request.get_json()
    if not data:

        abort(400, description="Not a JSON")

    if 'email' not in data:
        abort(400, description="Missing email")
    if 'password' not in data:
        abort(400, description="Missing password")

    users = storage.all(User).values()
    for user in users:
        if user.email == data['email']:
            if user.password == md5(data['password'].encode()).hexdigest():
                return jsonify(user.to_dict()), 201
    abort(404, description="Not Found")


@app_views.route('/homepage', methods=['POST', 'GET']
, strict_slashes=False)
def homepage():
    session.permanent = True
    print(str(current_user))
    return str(current_user)

