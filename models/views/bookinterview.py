from models.views import app_views
from flask import render_template, session
import requests


@app_views.route('/bookinterview', methods=['GET', 'POST'], strict_slashes=True)
def bookinterview():
    """create a resume"""
    user = session.get('user')

    return render_template('bookinterview.html', user=user);
