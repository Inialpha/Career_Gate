from models.views import app_views
from flask import render_template
import requests
from flask_login import current_user, login_required


@app_views.route('/homepage', methods=['GET', 'POST'], strict_slashes=True)
@login_required
def homepage():
    """Every users homepage"""
    user = current_user
    if user:
        return render_template('homepage.html', user=user);
    return "You are not logged in. Please login!"
