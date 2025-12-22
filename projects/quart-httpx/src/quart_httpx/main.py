"""Main entry for Quart application."""

import httpx
from quart import Quart

app = Quart(__name__)

state: dict[str, httpx.AsyncClient] = {}


@app.before_serving
async def startup():
    state["client"] = httpx.AsyncClient(base_url="https://httpbin.org", timeout=20)


@app.get("/")
async def root():
    return {"message": "hello there", "routes": ["/sample", "/delay4"]}


@app.get("/sample")
async def sample():
    client = state["client"]
    response = await client.get("/json")
    return response.json()


@app.get("/delay4")
async def delay4():
    client = state["client"]
    response = await client.get("/delay/4")
    return response.json()


@app.after_serving
async def shutdown():
    client = state["client"]
    await client.aclose()
    state.clear()
    print("\nClosed client and shutdown server")


if __name__ == "__main__":
    app.run(debug=True)
