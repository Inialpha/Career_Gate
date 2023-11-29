from views import app_views
from flask import render_template, session, redirect
import requests


@app_views.route('/users', methods=['GET'], strict_slashes=True)
def get_user():
    """get a user"""
    user = session.get('user')
    if user:
        return render_template('users.html', user=user);
    return redirect('/login')

@app_views.route('/admin', methods=['GET'], strict_slashes=True)
def admin():
    """add a new admin"""
    user = session.get('user')
    if user is None:
        return redirect("/")

    return render_template('admin.html', user=user)
