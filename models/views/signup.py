from models.views import app_views
from flask import render_template, flash, url_for, redirect
import models
from models.forms.signup import SignupForm

@app_views.route('/signup', methods=['GET', 'POST'], strict_slashes=True)
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password1.data

        data = {'first_name': first_name, 'last_name': last_name,
                'email': email, 'password': password}
        from models.user import User
        user = User(**data)
        user.save()
        flash("Account created successfully! Please login", category='success')
        return redirect(url_for('app_views.login'))
    return render_template('signup.html', form=form)
