from quart import Quart, render_template

app = Quart(__name__)


@app.route("/")
async def root():
    return await render_template("index.html")


@app.get("/snippet")
async def button_example():
    return await render_template("snippet.html")


app.run()
