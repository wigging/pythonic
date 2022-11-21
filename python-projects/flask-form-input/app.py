from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    a = float(request.form['numberA'])
    b = float(request.form['numberB'])

    sum_ab = a + b
    mult_ab = a * b
    div_ab = a / b

    res = {
        'a': a, 'b': b,
        'sum_ab': sum_ab, 'mult_ab': mult_ab, 'div_ab': div_ab
    }

    return render_template('results.html', results=res)
