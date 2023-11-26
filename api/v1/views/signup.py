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
    if not data:
        abort(401, description="Not a JSON")
    if 'first_name' not in data:
        abort(403, description="Missing first_name")
    if 'last_name' not in data:
        abort(403, description="Missing last_name")
    if 'email' not in data:
        abort(405, description="Missing email")
    if 'password' not in data:
        abort(406, description="Missing password")
    #print("\n\n", data)
    for user in storage.all(User).values():
        if user.email == data['email']:
            return jsonify({"status": "emailerror"}), 201

    
    print("\n\n", data)
    inp = {'firstname': 'Inimfon ', 'lastname': 'Ebong ', 'email': 'ebonginimfon8@gmail.com', 'password': 'Test'}
    data['user_type'] = "admin"
    instance = User(**data)
    instance.save()
    return jsonify({"status": "OK"}), 201
