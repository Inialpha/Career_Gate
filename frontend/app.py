from flask import Flask, render_template
from views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")

