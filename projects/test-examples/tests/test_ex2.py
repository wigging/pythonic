from examples import ex2
import pytest


def test_ex2():
    d = ex2.run_divider()
    assert d == pytest.approx(0.4347, rel=1e-3)
