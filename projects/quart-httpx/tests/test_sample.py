"""Tests sample route."""

import pytest

from quart_httpx import main


@pytest.mark.asyncio
async def test_sample(client, monkeypatch):
    mock_response_data = {"slideshow": {"title": "Sample Slideshow"}}

    class MockResponse:
        def json(self):
            return mock_response_data

    class MockAsyncClient:
        async def get(self, url):
            assert url == "/json"
            return MockResponse()

        async def aclose(self):
            pass

    monkeypatch.setitem(main.state, "client", MockAsyncClient())

    response = await client.get("/sample")
    assert response.status_code == 200

    data = await response.get_json()
    assert data == mock_response_data
