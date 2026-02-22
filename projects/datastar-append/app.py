"""Entrypoint for Quart app.

Use this command to run the app
uv run app.py
"""

from quart import Quart, render_template

app = Quart(__name__)


@app.get("/")
async def index():
    return await render_template("index.html")


@app.get("/snippet")
async def snippet():
    headers = {"datastar-selector": "#hal", "datastar-mode": "append"}
    return await render_template("snippet.html"), headers


app.run()
