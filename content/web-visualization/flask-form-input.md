+++
title = "Form input"
date = 2022-11-01
+++

An HTML form collects user input on a web page. Using Flask, the input can be evaluated in Python and used elsewhere in the web application. As an example, in the `app.py` file shown below, the index or home page renders the HTML form. The input from the form is handled as two numbers. The sum, product, and fraction of the numbers are calculated then passed to the results page.

```python
# app.py

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
```

<p><img src="/pythonic/img/flask-form-input-index.png" style="max-width:500px;" alt="index page"></p>

<p><img src="/pythonic/img/flask-form-input-results.png" style="max-width:400px;" alt="results page"></p>

The HTML templates used by the app are shown below. Notice that [Bootstrap](https://getbootstrap.com) is used for the style and layout of the pages.

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet">

    <title>Home Page</title>

    <style type="text/css">
        body { background-color: lightgray; }
        input { max-width: 200px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col">

                <h1 class="mt-3">Submit numbers</h1>

                <p>Input numbers A and B into the form below then click the Submit button to see the results.</p>

                <h2>Form</h2>
                <form action="/results" method="POST">
                    <div class="mb-3">
                        <label for="numberA" class="form-label">Number A</label>
                        <input type="number" step="any" class="form-control" name="numberA">
                    </div>
                    <div class="mb-3">
                        <label for="numberB" class="form-label">Number B</label>
                        <input type="number" step="any" class="form-control" name="numberB">
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>

            </div>
        </div>
    </div>
</body>
</html>
```

```html
<!-- results.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet">

    <title>Results Page</title>

    <style type="text/css">
        body { background-color: lightgray; }
    </style>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col">

                <h1 class="mt-3">Results</h1>

                <p>Below are the results calculated from the form values.</p>

                <p>Number A = {{ results['a'] }}</p>
                <p>Number B = {{ results['b'] }}</p>
                <p>A + B = {{ results['sum_ab'] }}</p>
                <p>A x B = {{ results['mult_ab'] }}</p>
                <p>A / B = {{ results['div_ab'] }}</p>

            </div>
        </div>
    </div>

</body>
</html>
```
