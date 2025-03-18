---
title: Flask app configuration
date: March 12, 2025
---

The [dotenv](https://pypi.org/project/python-dotenv/) package can be used to load configuration settings for a Flask app. The configuration is defined in a `.env` file which is ignored by version control to ensure items like API keys and passwords are not shared with others.

In the example project shown below, the `__init__.py` is the application factory for the Flask app. It loads the configuration settings from the `.env` file which are stored in the `app.config` attribute. It also registers the routes which are discussed next.

```text
.
├── .env
├── pyproject.toml
├── src/
│   └── flaskr/
│       ├── __init__.py
│       └── routes.py
└── uv.lock
```

```python
# __init__.py

from flask import Flask
from dotenv import dotenv_values
from . import routes

def create_app():
    app = Flask(__name__)

    # Load configuration from .env file then store configuration settings in the
    # config attribute of the flask object
    config = dotenv_values(".env")
    app.config.from_mapping(config)

    app.register_blueprint(routes.bp)

    return app
```

Contents of the `.env` file are shown below.

```text
USERNAME="homer"
PASSWORD="alpha12345"
```

The `routes.py` file (see below) loads the USERNAME and PASSWORD from the `current_app.config` attribute. Note that the USERNAME and PASSWORD are defined in the `.env` file. This approach allows all the configuration settings for the Flask app to be defined in the `.env` file.

```python
# routes.py

from flask import Blueprint
from flask import current_app

bp = Blueprint("routes", __name__)

@bp.route("/")
def home():
    """Home page."""
    return "<p>Hello there!</p>"

@bp.route("/config")
def read_config():
    """Display config values."""
    config = current_app.config
    username = config["USERNAME"]
    password = config["PASSWORD"]
    return f"<p>USERNAME is {username}</p><p>PASSWORD is {password}</p>"
```

See the `pythonic/projects/flask-config` directory in the [pythonic](https://github.com/wigging/pythonic) repository on GitHub for the example code. The `.env` file is not in the repository because it is ignored by git; therefore, it must be created with the contents shown above to run the example code.
