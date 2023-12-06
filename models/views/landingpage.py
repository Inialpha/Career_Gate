from models.views import app_views
from flask import render_template, session, redirect, url_for
from models.news import articles

@app_views.route('/', methods=['GET'], strict_slashes=True)
def landingpage():
    
    #return html.content
    return render_template('landingpage.html', articles=articles)
