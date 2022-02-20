from flask import Flask
from flask import render_template
from flask import request

from bokeh.plotting import figure
from bokeh.embed import components


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plot', methods=['POST'])
def plot():
    xdata = request.form['xdata']
    ydata = request.form['ydata']

    x = list(map(float, xdata.split(', ')))
    y = list(map(float, ydata.split(', ')))

    p = figure(plot_width=400, plot_height=400)
    p.circle(x, y, size=12, line_color='navy', fill_color='orange')
    script, div = components(p)

    return render_template('plot.html', script=script, div=div)
