from models.views import app_views
from flask import render_template, session, redirect, url_for

@app_views.route('/', methods=['GET'], strict_slashes=True)
def landingpage():

    if session.get('user', None):
        return redirect('/homepage')
    return render_template('index.html')
