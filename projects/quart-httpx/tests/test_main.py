"""Tests for Quart app routes."""

import pytest
import pytest_asyncio
import respx
from httpx import Response

from quart_httpx.main import app
from quart_httpx import config
from quart_httpx.http_client import init_client, close_client


MOCK_USERS = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Doe", "email": "jane@example.com"},
]

MOCK_POSTS = [
    {"id": 1, "title": "First Post", "body": "Hello world", "userId": 1},
    {"id": 2, "title": "Second Post", "body": "Another post", "userId": 1},
]


@pytest_asyncio.fixture
async def client(mock_env_vars):
    config._config = None
    init_client()
    test_client = app.test_client()
    yield test_client
    await close_client()


@pytest.mark.asyncio
async def test_root(client):
    response = await client.get("/")
    assert response.status_code == 200

    data = await response.get_json()
    assert data == {"status": "ok", "message": "Server is running"}


@pytest.mark.asyncio
@respx.mock
async def test_get_users(client):
    respx.get("https://jsonplaceholder.typicode.com/users").mock(
        return_value=Response(200, json=MOCK_USERS)
    )

    response = await client.get("/users")
    assert response.status_code == 200

    data = await response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["id"] == 1
    assert data[0]["name"] == "John Doe"
    assert data[0]["email"] == "john@example.com"


@pytest.mark.asyncio
@respx.mock
async def test_get_posts(client):
    respx.get("https://jsonplaceholder.typicode.com/posts").mock(
        return_value=Response(200, json=MOCK_POSTS)
    )

    response = await client.get("/posts")
    assert response.status_code == 200

    data = await response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["id"] == 1
    assert data[0]["title"] == "First Post"
    assert data[0]["body"] == "Hello world"
