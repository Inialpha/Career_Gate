from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/")


from models.views.signup import *
from models.views.landingpage import *
from models.views.homepage import *
from models.views.login import *
from models.views.interviews import *
from models.views.resume import *
from models.views.users import *
from models.views.webhook import *
