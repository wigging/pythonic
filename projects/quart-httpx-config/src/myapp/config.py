"""Module for configuration settings."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True, slots=True)
class Config:
    """Configuration settings object."""

    base_url: str
    timeout: int


_config: Config | None = None


def get_config() -> Config:
    """Get configuration settings (created once on first call)."""
    global _config

    if _config is None:
        load_dotenv()
        base_url = os.environ["BASE_URL"]
        timeout = os.environ["TIMEOUT"]
        _config = Config(base_url=base_url, timeout=int(timeout))

    return _config
