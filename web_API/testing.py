from flask import Flask
from flask import request, session, redirect, url_for
from flask import send_from_directory
from flask import render_template
import random
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index():
    return "Testing Console is running..."

@app.route('/api/sensors/temperature')
def get_temperature():
    y = 26
    return str(y+random.randint(-5, 5))

@app.route('/api/sensors/humidity')
def get_humidity():
    x = 60
    return str(x+random.randint(-5, 5))

if __name__ == '__main__':
    app.run(port=8080)