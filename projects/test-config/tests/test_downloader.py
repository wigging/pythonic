"""Tests for the downloader module."""

import importlib

import pytest

import mypkg
from mypkg import config


def test_downloader_defaults():
    importlib.reload(config)

    err = "API_KEY environment variable is not set"
    with pytest.raises(RuntimeError, match=err):
        mypkg.download_file()


def test_downloader_env(monkeypatch, capsys):
    monkeypatch.setenv("API_KEY", "12345")

    importlib.reload(config)
    mypkg.download_file()

    captured = capsys.readouterr()
    assert "Saved file to ~/Desktop/downloads\n" in captured.out
