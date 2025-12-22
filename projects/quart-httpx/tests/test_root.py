"""Tests root route."""

import pytest


@pytest.mark.asyncio
async def test_root(client):
    response = await client.get("/")
    assert response.status_code == 200

    data = await response.get_json()
    assert data["message"] == "hello there"
    assert data["routes"] == ["/sample", "/delay4"]
