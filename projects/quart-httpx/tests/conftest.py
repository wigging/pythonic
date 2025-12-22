import pytest

from quart_httpx.main import app


@pytest.fixture
def client():
    return app.test_client()
