from flask import render_template, send_from_directory
from api import app

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)