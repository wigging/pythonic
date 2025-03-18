---
title: Doctest with Python
date: November 17, 2023
---

The docstring of the `adder()` function shown below contains two examples of how to use the function. The function resides in a file named `example.py`. Use the `doctest` module to test the examples in this docstring.

```python
# This function resides in a file named example.py

def adder(x, y):
    """
    Add two numbers.

    Parameters
    ----------
    x : int or float
        First number.
    y : int or float
        Second number.

    Returns
    -------
    z : int or float
        The result of adding two numbers.

    Example
    -------
    >>> adder(1, 2)
    3

    >>> adder(1.5, 8)
    9.5
    """
    z = x + y
    return z
```

Running doctest on the example produces the following output:

```text
$ python -m doctest -v example.py

Trying:
    adder(1, 2)
Expecting:
    3
ok
Trying:
    adder(1.5, 8)
Expecting:
    9.5
ok
1 items had no tests:
    example
1 items passed all tests:
   2 tests in example.adder
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
```

This docstring imports NumPy where it is used to add two arrays.

```python
# This function resides in a file named example.py

def array_adder(x, y):
    """
    Add two arrays.

    Parameters
    ----------
    x : ndarray
        First array.
    y : ndarray
        Second array.

    Returns
    -------
    z : ndarray
        The result of adding two arrays.

    Example
    -------
    >>> import numpy as np
    >>> a = np.array([1, 2, 3])
    >>> b = np.array([5, 6, 7])
    >>> array_adder(a, b)
    array([ 6,  8, 10])
    """
    z = x + y
    return z
```

```text
$ python -m doctest -v example.py

Trying:
    import numpy as np
Expecting nothing
ok
Trying:
    a = np.array([1, 2, 3])
Expecting nothing
ok
Trying:
    b = np.array([5, 6, 7])
Expecting nothing
ok
Trying:
    array_adder(a, b)
Expecting:
    array([ 6,  8, 10])
ok
1 items had no tests:
    example
1 items passed all tests:
   4 tests in example.array_adder
4 tests in 2 items.
4 passed and 0 failed.
Test passed.
```
