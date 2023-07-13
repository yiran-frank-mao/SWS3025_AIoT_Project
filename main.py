from flask import Flask
from flask import render_template, send_from_directory
from Sensors.TemperatureSensor import TemperatureSensor
from flask_cors import CORS

app = Flask(__name__, template_folder='web')
cors_app = CORS(app)
api = Flask(__name__)
cors_api = CORS(api)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/web/<path:name>')
def return_flutter_doc(name):
    datalist = str(name).split('/')
    DIR_NAME = "web"
    if len(datalist) > 1:
        for i in range(0, len(datalist) - 1):
            DIR_NAME += '/' + datalist[i]
    return send_from_directory(DIR_NAME, datalist[-1])


@api.route('/api/sensors/temperature')
def get_temperature():
    return str(TemperatureSensor().get_value()[0])


@api.route('/api/sensors/humidity')
def get_humidity():
    return str(TemperatureSensor().get_value()[1])


if __name__ == '__main__':
    api.run(port=8123)
    app.run(host='0.0.0.0', port=8080)