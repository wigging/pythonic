"""Main entrypoint for the Quart application.

Run with the following command:
uv run quart --app quart_httpx.main run
"""

from quart import Quart

from .http_client import init_client, get_client, close_client


app = Quart(__name__)


@app.before_serving
async def startup():
    """Create a global HTTP async client before serving."""
    init_client()


@app.after_serving
async def shutdown():
    """Clean up resources after serving."""
    await close_client()


@app.get("/")
async def root():
    """Return server status."""
    return {"status": "ok", "message": "Server is running"}


@app.get("/users")
async def get_users():
    """Fetch and return user data from JSONPlaceholder API."""
    client = get_client()
    response = await client.get("https://jsonplaceholder.typicode.com/users")
    return response.json()


@app.get("/posts")
async def get_posts():
    """Fetch and return posts data from JSONPlaceholder API."""
    client = get_client()
    response = await client.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()
