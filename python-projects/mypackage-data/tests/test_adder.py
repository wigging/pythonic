from mypackage import adder


def test_adder():
    s = adder(2, 3)
    assert s == 5
