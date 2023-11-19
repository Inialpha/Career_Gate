#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

@app_views.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    """
    Creates a user
    """
    if request.method == "GET":
        return "Signup"

    data = request.get_json()
    if 'first_name' not in data:
        abort(400, description="Missing first_name")
    if 'last_name' not in data:
        abort(400, description="Missing last_name")
    if not data:
        abort(400, description="Not a JSON")
    if 'email' not in data:
        abort(400, description="Missing email")
    if 'password' not in data:
        abort(400, description="Missing password")

    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)
