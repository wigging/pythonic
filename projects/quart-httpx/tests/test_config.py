"""Tests for configuration settings."""

import pytest

from quart_httpx.config import get_config


def test_get_config(mock_env_vars):
    conf = get_config()
    assert conf.base_url == "https://example.com"
    assert conf.timeout == 40


def test_get_config_is_cached(mock_env_vars):
    config1 = get_config()
    config2 = get_config()

    assert config1 is config2


def test_get_config_missing(mock_env_missing):
    with pytest.raises(KeyError):
        get_config()
