import stpkg


def test_adder():
    z = stpkg.add(10, 1.5)
    assert z == 11.5
