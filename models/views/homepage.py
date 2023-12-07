from models.views import app_views
from flask import render_template, redirect, flash, url_for
import requests
from flask_login import current_user, login_required


@app_views.route('/homepage', methods=['GET', 'POST'], strict_slashes=True)
@login_required
def homepage():
    """Every users homepage"""
    user = current_user
    return render_template('homepage.html', user=user);
