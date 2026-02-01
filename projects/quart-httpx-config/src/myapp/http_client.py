"""Module for the HTTP async client."""

import httpx

from .config import get_config


_client: httpx.AsyncClient | None = None


def init_client() -> None:
    """Initialize a global HTTP async client."""
    global _client

    conf = get_config()
    _client = httpx.AsyncClient(base_url=conf.base_url, timeout=conf.timeout)


def get_client() -> httpx.AsyncClient:
    """Get the HTTP async client or throw error."""
    if _client is None:
        raise RuntimeError("Client not initialized")
    return _client


async def close_client() -> None:
    """Close the HTTP async client."""
    global _client

    if _client:
        await _client.aclose()
        _client = None
