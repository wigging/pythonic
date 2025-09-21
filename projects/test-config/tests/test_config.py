"""Tests for the config module."""

import importlib
from mypkg import config


def test_config_defaults():
    assert config.api_key is None
    assert config.api_url == "http://localhost:8090"
    assert config.save_path == "~/Desktop/downloads"


def test_config_env(monkeypatch):
    monkeypatch.setenv("API_KEY", "12345")
    monkeypatch.setenv("API_URL", "https://www.apple.com")

    importlib.reload(config)

    assert config.api_key == "12345"
    assert config.api_url == "https://www.apple.com"
    assert config.save_path == "~/Desktop/downloads"
