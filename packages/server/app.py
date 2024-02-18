import time
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/launch", methods=['GET'])
def get_launch():
    return {'time': time.time()}