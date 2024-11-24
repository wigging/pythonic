from mypackage import divider
import pytest


def test_divider():
    x = 9
    y = 3
    d = divider(x, y)
    assert d == pytest.approx(3)
