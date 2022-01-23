---
title: Deploy on Heroku
permalink: heroku
---

[Heroku](https://www.heroku.com) makes it easy to deploy a Python Flask application. To get started, create a project folder and a virtual environment in that folder. Notice that `env` is the name of the virtual environment discussed below; it can be called `myenv` or something else.

```bash
# Create a project folder
$ mkdir flask-heroku
$ cd flask-heroku

# Create and activate a virtual environment in the project folder
$ python -m venv env
$ source env/bin/activate
```

Install Flask and gunicorn in the environment. Save the dependencies list to a requirements text file.

```python
(env) $ pip install Flask
(env) $ pip install gunicorn
(env) $ pip freeze > requirements.txt
```

Build a basic Flask web app and save it as `hello.py`.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, Python!</h1>"
```

Create a `Procfile` for Heroku containing the following:

```
web: gunicorn hello:app
```

Initialize a local Git repository for the project. In this example the default branch is called `main`.

```bash
(env) $ git init
(env) $ git add .
(env) $ git commit -m 'Initial commit'
```

Now go to the Heroku website at <https://www.heroku.com> and create an account if you don't already have one. Then follow Heroku's Python documentation to setup their command line tool. Once everything is setup, go to the command line and login with

```bash
$ heroku login
```

Create a Heroku application named `flaskheroku21`. The application name can be anything that is available on the Heroku service. Push it to the Heroku remote repository, then open the deployed app in your web browser.

```bash
(env) $ heroku create flaskheroku21
(env) $ git push heroku main
(env) $ heroku open
```
