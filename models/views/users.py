from models.views import app_views
from flask import render_template, session, redirect, request, flash, url_for
from flask_login import login_required, current_user
import models


@app_views.route('/users', methods=['GET'], strict_slashes=True)
@login_required
def users():
    """get a user"""
    from models.user import User
    users = models.storage.all(User).values()
    user_list = []
    for user in users:
        if user.user_type == "client":
            user_list.append(user)
    return render_template('users.html', users=user_list)
    return redirect('/login')

@app_views.route('/admin', methods=['GET', 'POST'], strict_slashes=True)
@login_required
def admin():
    """add a new admin"""
    if current_user.user_type == "admin":
        if request.method == "POST":
            email = request.form['email']
            user = models.storage.get_by_email(email)
            if user:
                user.user_type = "admin"
                models.storage.save()
                flash("{} {} added as Administrator".format(user.first_name, user.last_name), category="success")
                return redirect(url_for('app_views.homepage'))
        return render_template('admin.html')
    return redirect(url_for('app_views.homepage'))

@app_views.route('/user_details/<id>', methods=['GET'], strict_slashes=True)
@login_required
def user_details(id):
    """ get a user """
    from models.user import User
    user = models.storage.get(User, id)
    return render_template('user_details.html', user=user)
