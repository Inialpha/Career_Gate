from views import app_views

@app_views.route('/', methods=['GET', 'POST'], strict_slashes=True)
def homepage():
    """Every users homepage"""
    return render_template('homepage.html');
