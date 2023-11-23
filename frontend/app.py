from flask import Flask, render_template
from views import app_views

app = Flask(__name__)
app.secret_key = "0cbc6611f5540bd0809a388dc95a615b"
app.register_blueprint(app_views)
if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")

