from views import app_views
from flask import render_template, request, abort
import requests

@app_views.route('/login', methods=['GET', "POST"], strict_slashes=True)
def login():

    return render_template('login.html')
