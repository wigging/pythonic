"""Module for config settings."""

import os

api_key = os.getenv("API_KEY")

api_url = os.getenv("API_URL", "http://localhost:8090")

save_path = "~/Desktop/downloads"
