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
    # Get the form inputs
    xdata = request.form['xdata']
    ydata = request.form['ydata']

    # Convert form input to a list of floats representing x and y values
    x = list(map(float, xdata.split(', ')))
    y = list(map(float, ydata.split(', ')))

    # Create a Bokeh plot using the x and y values
    p = figure(plot_width=400, plot_height=400)
    p.circle(x, y, size=12, line_color='navy', fill_color='orange')

    # Get HTML components to embed in a web page
    script, div = components(p)

    return render_template('plot.html', script=script, div=div)
