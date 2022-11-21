from mypackage import adder
import pytest


def test_adder():
    x = 4
    y = 3.1
    a = adder(x, y)
    assert a == pytest.approx(7.1)
