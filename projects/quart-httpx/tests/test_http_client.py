"""Tests for HTTP async client."""

import pytest

import quart_httpx.http_client as http_module
from quart_httpx.http_client import init_client, get_client, close_client


@pytest.fixture(autouse=True)
def reset_client():
    """Reset the HTTP client state before and after each test."""
    http_module._client = None
    yield
    http_module._client = None


def test_get_client_raises_when_not_initialized():
    with pytest.raises(RuntimeError, match="Client not initialized"):
        get_client()


def test_init_client(mock_env_vars):
    init_client()

    client = get_client()
    assert client is not None
    assert client.timeout.connect == 40


@pytest.mark.asyncio
async def test_close_client(mock_env_vars):
    init_client()

    await close_client()

    with pytest.raises(RuntimeError, match="Client not initialized"):
        get_client()


@pytest.mark.asyncio
async def test_close_client_when_none():
    await close_client()
