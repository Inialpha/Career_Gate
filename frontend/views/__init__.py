from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/")


from views.signup import *
from views.landingpage import *
from views.homepage import *
from views.login import *
from views.interviews import *
from views.resume import *
from views.users import *
