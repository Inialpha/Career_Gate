from models.views import app_views
from flask import render_template, flash, url_for, redirect, request
import models
from models.forms.signup import SignupForm

@app_views.route('/signup', methods=['GET', 'POST'], strict_slashes=True)
def signup():
    if request.method == 'POST':
        form = request.form
        name = form.get('full_name')
        email = form.get('email')
        password1 = form.get('password1')
        password2 = form.get('password2')
        
        try:
            name = name.split()
            first_name = name[0]
            last_name = name[1]

        except IndexError:
            flash("Please Enter full name", category="warning")
            return redirect(url_for('app_views.signup'))
        #if password1 != password2:
        #    flash("password fields must match", category="warning")
        #    return redirect(url_for('app_views.signup'))

        data = {'first_name': first_name, 'last_name': last_name,
                'email': email, 'password': password1}
        from models.user import User
        user = models.storage.get_by_email(email)
        if not user:
            user = User(**data)
            user.save()
            flash("Account created successfully! Please login", category='success')
            return redirect(url_for('app_views.login'))
        flash("Email already in use please try a different email", category="warning")
    return render_template('newsignup.html')
