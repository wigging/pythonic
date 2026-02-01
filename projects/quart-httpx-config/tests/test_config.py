"""Tests for configuration settings."""

import pytest

from myapp import config
from myapp.config import get_config


@pytest.fixture(autouse=True)
def reset_config():
    """Reset global config object for each test."""
    config._config = None


def test_config():
    """Test config settings."""
    conf = get_config()
    assert conf.base_url == "https://example.com"
    assert conf.timeout == 40


def test_config_global():
    """Test global config object for equality."""
    config1 = get_config()
    config2 = get_config()

    assert config1 is config2
    assert config1 == config2


def test_missing_env(monkeypatch):
    """Test for error when environment variables are missing."""
    monkeypatch.delenv("BASE_URL", raising=False)
    monkeypatch.delenv("TIMEOUT", raising=False)

    with pytest.raises(KeyError):
        get_config()
