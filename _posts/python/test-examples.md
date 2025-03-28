---
title: Test Examples with Python
date: November 8, 2022
---

Example scripts are often available for Python packages to demonstrate how to use the package. The examples are typically part of the repository where the package is developed. Tests should be written to ensure the examples continue to work with new versions of the package.

Below is the structure of a project for developing a Python package. Notice the `examples` directory that contains example scripts for demonstrating functions from `mypackage`.

```
myproject/
├── README.md
├── examples/
│   ├── ex1.py
│   └── ex2.py
├── pyproject.toml
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── adder.py
│       └── divider.py
└── tests/
    ├── test_adder.py
    ├── test_divider.py
    ├── test_ex1.py
    └── test_ex2.py
```

To ensure pytest can discover the examples, add the project to the Python path as shown below in the `pyproject.toml` file:

```toml
[tool.pytest.ini_options]
pythonpath = ["."]
```

The content of the first example is shown below along with the associated test. The test imports the example and asserts the value of the `a` variable.

```python
# Example 1 from examples/ex1.py

from mypackage import adder

x = 2.5
y = 8

a = adder(x, y)
print('a is', a)
```

```python
# Test for example 1 from tests/test_ex1.py

from examples import ex1

def test_ex1():
    a = ex1.a
    assert a == 10.5
```

The content of the second example is shown below along with the test. Unlike the previous example, this example contains all its code within functions. The test imports the example and asserts the returned value of the `run_divider()` function.

```python
# Example 2 from examples/ex2.py

from mypackage import divider

def run_divider():
    x = 4
    y = 9.2
    d = divider(x, y)
    return d

def main():
    d = run_divider()
    print('d is', d)

if __name__ == '__main__':
    main()
```

```python
# Test for example 2 from tests/test_ex2.py

from examples import ex2
import pytest

def test_ex2():
    d = ex2.run_divider()
    assert d == pytest.approx(0.4347, rel=1e-3)
```
