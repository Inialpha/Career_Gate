from views import app_views
from flask import render_template, session, redirect

@app_views.route('/', methods=['GET'], strict_slashes=True)
def landingpage():

    if session.get('user', None):
        return redirect('/homepage')
    return render_template('landingpage.html')
