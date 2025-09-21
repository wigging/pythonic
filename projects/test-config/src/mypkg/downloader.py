"""Module for the download function."""

from . import config


def download_file():
    """Download a file."""
    if config.api_key is None:
        raise RuntimeError("API_KEY environment variable is not set")

    print("API_KEY is", config.api_key)
    print("Saved file to", config.save_path)
