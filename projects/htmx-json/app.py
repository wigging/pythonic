from quart import Quart, render_template, request

app = Quart(__name__)


@app.get("/")
async def index():
    """Main app page."""
    return await render_template("index.html")


@app.get("/update")
async def update():
    """Update the status message."""
    return await render_template("update.html")


@app.get("/update-editor")
async def update_editor():
    """Update text content in the Ace editor using JSON data."""
    return {"content": "New content is here.\nAnother line goes here too."}


@app.post("/save")
async def save():
    """Save the editor content."""
    form = await request.form
    content = form.get("content", "")

    # This `content` could be saved to a file or database
    print(f"***\n{content}\n***")

    return await render_template("save.html", content=content)


if __name__ == "__main__":
    app.run(debug=True)
