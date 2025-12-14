from quart import Quart, render_template, request

app = Quart(__name__)


@app.get("/")
async def root():
    return await render_template("index.html")


@app.post("/results")
async def results():
    form = await request.form
    nums = form["numbers"]

    y = [float(n) for n in nums.split(",")]
    x = list(range(1, len(y) + 1))
    data = {"x": x, "y": y}

    return await render_template("results.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
