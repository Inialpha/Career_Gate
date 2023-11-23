#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.interviews import *
from api.v1.views.signup import *
from api.v1.views.login import *
from api.v1.views.homepage import *
