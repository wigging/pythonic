---
title: Update page with Ajax and Flask
date: February 4, 2023
---

This Flask webapp example uses Ajax to update the page with results from the post request. The results are returned as JSON which is used to update the div tags.

<p><img src="../../assets/images/flask-ajax.png" style="max-width:100%;" alt="flask ajax"></p>

```python
# app.py

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

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
        'a': a,
        'b': b,
        'sum_ab': sum_ab,
        'mult_ab': mult_ab,
        'div_ab': div_ab
    }

    return jsonify(res)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js" integrity="sha512-894YE6QWD5I59HgZOGReFYm4dnWc1Qt5NtvYSaNcOP+u1T9qYdvdihz0PPSiiqn/+/3e7Jo4EaG7TubfWGUrMQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

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

                <br>
                <div id="numA"></div>
                <div id="numB"></div>
                <div id="sumAB"></div>
                <div id="multAB"></div>
                <div id="divAB"></div>

            </div>
        </div>
    </div>

    <script type="text/javascript">
        $("form").submit(function(event) {

            $.ajax({
                method: "POST",
                url: "/results",
                data: {
                    numberA: $("input[name=numberA]").val(),
                    numberB: $("input[name=numberB]").val()
                },
                success: function(result) {
                    $("#numA").html("<p>Number A is " + result.a + "</p>");
                    $("#numB").html("<p>Number B is " + result.b + "</p>");
                    $("#sumAB").html("<p>Sum A + B is " + result.sum_ab + "</p>");
                    $("#multAB").html("<p>Multiply A x B is " + result.mult_ab + "</p>");
                    $("#divAB").html("<p>Divide A / B is " + result.div_ab + "</p>");
                }
            });

            event.preventDefault();
        });
    </script>

</body>
</html>
```
