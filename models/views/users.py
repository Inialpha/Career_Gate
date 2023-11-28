from models.views import app_views
from flask import render_template, session, redirect
import requests
import models


@app_views.route('/users', methods=['GET'], strict_slashes=True)
def users():
    """get a user"""
    from models.user import User
    users = models.storage.all(User) 
    return render_template('users.html', users=users)
    return redirect('/login')

@app_views.route('/admin', methods=['GET'], strict_slashes=True)
def admin():
    """add a new admin"""
    if user is None:
        return redirect("/")

    return render_template('admin.html', user=user)

@app_views.route('/user_details/<id>', methods=['GET'], strict_slashes=True)
def user_details(id):
    """ get a user """
    user = models.storage.get(User, id)
    return render_template('user_detail.html', user=user)
