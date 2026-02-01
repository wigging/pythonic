"""Tests for HTTP async client."""

import pytest

import myapp.http_client as http_module
from myapp.http_client import init_client, get_client, close_client


@pytest.fixture(autouse=True)
def reset_client():
    """Reset global HTTP client for each test."""
    http_module._client = None


def test_missing_client():
    """Test for error when client has not been initialized."""
    with pytest.raises(RuntimeError, match="Client not initialized"):
        get_client()


def test_init_client():
    """Test client initialization."""
    init_client()
    client = get_client()

    assert client is not None
    assert client.timeout.connect == 40


@pytest.mark.asyncio
async def test_close_client():
    """Test for error after closing the client."""
    init_client()

    await close_client()

    with pytest.raises(RuntimeError, match="Client not initialized"):
        get_client()
