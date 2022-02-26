from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update', methods=['POST'])
def update():
    xdata = request.form['xdata']
    ydata = request.form['ydata']

    x = list(map(float, xdata.split(', ')))
    y = list(map(float, ydata.split(', ')))

    res = {'xValues': x, 'yValues': y}

    return jsonify(res)
