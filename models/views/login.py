import models
from models.views import app_views
from flask import render_template, request, abort, session, redirect, flash, url_for
import requests
from models.forms.login import LoginForm
from flask_login import login_user, logout_user
from hashlib import md5


@app_views.route('/login', methods=['GET', "POST"], strict_slashes=True)
def login():

    if request.method == "POST":

        form = request.form
        email = form.get('email')
        password = form.get('password')

        user = models.storage.get_by_email(email)
        if user and user.password == md5(password.encode()).hexdigest():
            login_user(user)
            flash("You are now logged in!", category='green')
            return redirect("/homepage")
        else:
            flash('Username and password are not match! Please try again', category='red')
    return render_template('newlogin.html')


@app_views.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("app_views.landingpage"))
