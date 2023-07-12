from flask import Flask
from flask import request, session, redirect, url_for
from flask import send_from_directory
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Testing Console is running..."

@app.route('/api/sensors/temperature')
def get_temperature():
    return 26.5

@app.route('/api/sensors/humidity')
def get_humidity():
    return 60

if __name__ == '__main__':
    app.run(port=8080)