from views import app_views
from flask import render_template, session
import requests


@app_views.route('/homepage', methods=['GET', 'POST'], strict_slashes=True)
def homepage():
    """Every users homepage"""
    user = session.get('user')
    if user:
        return render_template('homepage.html', user=user);
    return "You are not logged in. Please login!"
