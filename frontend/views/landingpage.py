from views import app_views
from flask import render_template

@app_views.route('/', methods=['GET'], strict_slashes=True)
def landingpage():
    return render_template('landingpage.html')
