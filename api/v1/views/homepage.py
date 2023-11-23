#!/usr/bin/python3
""" objects that handle all default RestFul API actions for login """
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request, current_app
from flasgger.utils import swag_from
from hashlib import md5
from flask import session

#@app_views.route('/homepage', methods=['GET'], strict_slashes=False)
#def homepage():
#    """
#    return current user
#    """
#    print(session)
#    return jsonify(session['user']), 200
