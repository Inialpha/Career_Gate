from views import app_views
from flask import render_template

@app_views.route('/signup', methods=['GET'], strict_slashes=True)
def signup():
    return render_template('signup.html')
