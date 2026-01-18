"""Shared pytest fixtures."""

import pytest

from quart_httpx import config


@pytest.fixture(autouse=True)
def reset_config(monkeypatch):
    """Reset global config and prevent load_dotenv from loading .env file."""
    config._config = None
    monkeypatch.setattr("quart_httpx.config.load_dotenv", lambda: None)


@pytest.fixture
def mock_env_vars(monkeypatch):
    """Mock environment variables."""
    monkeypatch.setenv("BASE_URL", "https://example.com")
    monkeypatch.setenv("TIMEOUT", "41")


@pytest.fixture
def mock_env_missing(monkeypatch):
    """Mock missing environment variables."""
    monkeypatch.delenv("BASE_URL", raising=False)
    monkeypatch.delenv("TIMEOUT", raising=False)
