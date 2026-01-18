"""Module for configuration settings.

This assumes that a `.env` file is available and it contains `BASE_URL` and
`TIMEOUT` environment variables.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True, slots=True)
class Config:
    """Configuration settings."""

    base_url: str
    timeout: int


_config: Config | None = None


def get_config() -> Config:
    """Get configuration settings (created once on first call)."""
    global _config

    if _config is None:
        load_dotenv()
        _config = Config(
            base_url=os.environ["BASE_URL"], timeout=int(os.environ["TIMEOUT"])
        )

    return _config
