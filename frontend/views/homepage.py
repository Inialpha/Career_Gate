from views import app_views
from flask import render_template, session
import requests


@app_views.route('/homepage', methods=['GET', 'POST'], strict_slashes=True)
def homepage():
    """Every users homepage"""
    res = requests.get("http://0.0.0.0:5001/api/v1/homepage")
    return render_template('homepage.html');
