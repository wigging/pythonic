from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    values = request.form['values']
    multiplier = request.form['multiplier']

    vals = list(map(int, values.split(', ')))
    mult = int(multiplier)

    y = []
    for val in vals:
        y.append(val * mult)

    return render_template('results.html', results=y)
